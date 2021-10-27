Apache Hudi 在 HDFS 的数据集上提供了插入更新和增量拉取的流原语。

一般来说，我们会将大量数据存储到 HDFS，新数据增量写入，而旧数据鲜有改动，特别是在经过数据清洗，放入数据仓库的场景。而且在数据仓库如 hive 中，对于 update 的支持非常有限，计算昂贵。另一方面，若是有仅对某段时间内新增数据进行分析的场景，则 hive、presto、hbase 等也未提供原生方式，而是需要根据时间戳进行过滤分析。

在此需求下，Hudi 可以提供这两种需求的实现。第一个是对 record 级别的更新，另一个是仅对增量数据的查询。且 Hudi 提供了对 Hive、presto、Spark 的支持，可以直接使用这些组件对 Hudi 管理的数据进行查询。

Hudi 是一个通用的大数据存储系统，主要特性：
- 摄取和查询引擎之间的快照隔离，包括 Apache Hive、Presto 和 Apache Spark。
- 支持回滚和存储点，可以恢复数据集。
- 自动管理文件大小和布局，以优化查询性能准实时摄取，为查询提供最新数据。
- 实时数据和列数据的异步压缩。

## 时间轴
在它的核心，Hudi 维护一条包含在不同的**即时**时间所有对数据集操作的**时间轴**，从而提供了从不同时间点出发得到不同的视图下的数据集。

Hudi 即时包含以下组件：
- 操作类型：对数据集执行的操作类型。
- 即时时间：即时时间通常是一个时间戳（例如20190117010349），该时间戳按操作开始时间的顺序单调增加。
- 状态：即时的状态。

## 文件组织
Hudi 将 DFS 上的数据集组织到`基本路径`下的目录结构中。数据集分为多个分区，这些分区是包含该分区的数据文件的文件夹，这与 Hive 表非常相似。

每个分区被相对于基本路径的特定`分区路径`区分开来。在每个分区内，文件被组织为`文件组`，由`文件id`唯一标识。每个文件组包含多个`文件切片`，其中每个切片包含在某个提交/压缩即时时间生成的基本列文件`*.parquet`以及一组日志文件`*.log*`，该文件包含自生成基本文件以来对基本文件的插入/更新。

Hudi 采用 MVCC 设计，其中压缩操作将日志和基本文件合并以产生新的文件片，而清理操作则将未使用的/较旧的文件片删除以回收 DFS 上的空间。Hudi 通过索引机制将给定的 hoodie 键（记录键+分区路径）映射到文件组，从而提供了高效的 Upsert。

一旦将记录的第一个版本写入文件，记录键和`文件组`/`文件id`之间的映射就永远不会改变。简而言之，映射的文件组包含一组记录的所有版本。

## 存储类型
Hudi 支持以下存储类型：
- 写时复制：仅使用列文件格式（例如 parquet）存储数据。通过在写入过程中执行同步合并以更新版本并重写文件。
- 读时合并：使用列式（例如 parquet）+ 基于行（例如 avro）的文件格式组合来存储数据。 更新记录到增量文件中，然后进行同步或异步压缩以生成列文件的新版本。

下表总结了这两种存储类型之间的权衡：

| **权衡**        | **写时复制**                | **读时合并**           |
| --------------- | --------------------------- | ---------------------- |
| 数据延迟        | 更高                        | 更低                   |
| 更新代价（I/O）   | 更高（重写整个 parquet 文件） | 更低（追加到增量日志） |
| Parquet 文件大小 | 更小（高更新代价（I/o））   | 更大（低更新代价）     |
| 写放大          | 更高                        | 更低（取决于压缩策略） |

## Hudi 对 EMR 底层存储支持
- HDFS
- COS

## 安装 Hudi
进入 [EMR 购买页](https://buy.cloud.tencent.com/emapreduce?regionId=1#/)，选择**产品版本**为 EMR-V2.2.0，选择**可选组件**为 **hudi 0.5.1**。hudi 组件默认安装在 master 和 router 节点上。
>! hudi 组件依赖 hive 和 spark 组件， 如果选择安装 hudi 组件，EMR 将自动安装 hive 和 spark 组件。

## 使用示例
可参考 [hudi 官网示例](http://hudi.apache.org/docs/docker_demo.html)：
1. 登录 master 节点，切换为 hadoop 用户。
2. 加载 spark 配置。
```
cd /usr/local/service/hudi
ln -s /usr/local/service/spark/conf/spark-defaults.conf /usr/local/service/hudi/demo/config/spark-defaults.conf 
```
上传配置到 hdfs：
```
hdfs dfs -mkdir -p /hudi/config
hdfs dfs -copyFromLocal demo/config/* /hudi/config/
```
3.	修改 kafka 数据源。
```
/usr/local/service/hudi/demo/config/kafka-source.properties
bootstrap.servers=kafka_ip:kafka_port
```
上传第一批次数据：
```
cat demo/data/batch_1.json | kafkacat -b [kafka_ip] -t stock_ticks -P
```
4.	摄取第一批数据。
```
spark-submit --class org.apache.hudi.utilities.deltastreamer.HoodieDeltaStreamer --master yarn ./hudi-utilities-bundle_2.11-0.5.1-incubating.jar   --table-type COPY_ON_WRITE --source-class org.apache.hudi.utilities.sources.JsonKafkaSource --source-ordering-field ts  --target-base-path /usr/hive/warehouse/stock_ticks_cow --target-table stock_ticks_cow --props /hudi/config/kafka-source.properties --schemaprovider-class org.apache.hudi.utilities.schema.FilebasedSchemaProvider
spark-submit --class org.apache.hudi.utilities.deltastreamer.HoodieDeltaStreamer  --master yarn ./hudi-utilities-bundle_2.11-0.5.1-incubating.jar  --table-type MERGE_ON_READ --source-class org.apache.hudi.utilities.sources.JsonKafkaSource --source-ordering-field ts  --target-base-path /usr/hive/warehouse/stock_ticks_mor --target-table stock_ticks_mor --props /hudi/config/kafka-source.properties --schemaprovider-class org.apache.hudi.utilities.schema.FilebasedSchemaProvider --disable-compaction
```
5.	查看 hdfs 数据。
```
 hdfs dfs -ls /usr/hive/warehouse/
```
6.	同步 hive 元数据。
```
bin/run_sync_tool.sh  --jdbc-url jdbc:hive2://[hiveserver2_ip:hiveserver2_port]  --user hadoop --pass [password] --partitioned-by dt --base-path /usr/hive/warehouse/stock_ticks_cow --database default --table stock_ticks_cow
bin/run_sync_tool.sh  --jdbc-url jdbc:hive2://[hiveserver2_ip:hiveserver2_port]   --user hadoop --pass [password]--partitioned-by dt --base-path /usr/hive/warehouse/stock_ticks_mor --database default --table stock_ticks_mor --skip-ro-suffix
```
7.	使用计算引擎查询数据。
 - hive 引擎
```
beeline -u jdbc:hive2://[hiveserver2_ip:hiveserver2_port] -n hadoop --hiveconf hive.input.format=org.apache.hadoop.hive.ql.io.HiveInputFormat --hiveconf hive.stats.autogather=false
```
或者 spark 引擎
```
spark-sql --master yarn --conf spark.sql.hive.convertMetastoreParquet=false
```
hive/spark 引擎执行如下 sql 语句：
```
select symbol, max(ts) from stock_ticks_cow group by symbol HAVING symbol = 'GOOG';
select `_hoodie_commit_time`, symbol, ts, volume, open, close  from stock_ticks_cow where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor group by symbol HAVING symbol = 'GOOG';
select `_hoodie_commit_time`, symbol, ts, volume, open, close  from stock_ticks_mor where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor_rt group by symbol HAVING symbol = 'GOOG';
select `_hoodie_commit_time`, symbol, ts, volume, open, close  from stock_ticks_mor_rt where  symbol = 'GOOG';
```
 - 进入 presto 引擎
```
/usr/local/service/presto-client/presto --server localhost:9000 --catalog hive --schema default --user Hadoop
```
**presto 查询有下划线的字段需要用双引号**，例如 `"_hoodie_commit_time"`，执行如下 sql 语句：
```
select symbol, max(ts) from stock_ticks_cow group by symbol HAVING symbol = 'GOOG';
select "_hoodie_commit_time", symbol, ts, volume, open, close  from stock_ticks_cow where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor group by symbol HAVING symbol = 'GOOG';
select "_hoodie_commit_time", symbol, ts, volume, open, close  from stock_ticks_mor where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor_rt group by symbol HAVING symbol = 'GOOG';
```
8. 上传第二批数据。
```
cat demo/data/batch_2.json | kafkacat -b 10.0.1.70 -t stock_ticks -P
```
9. 摄取第二批增量数据。
```
spark-submit --class org.apache.hudi.utilities.deltastreamer.HoodieDeltaStreamer --master yarn ./hudi-utilities-bundle_2.11-0.5.1-incubating.jar   --table-type COPY_ON_WRITE --source-class org.apache.hudi.utilities.sources.JsonKafkaSource --source-ordering-field ts  --target-base-path /usr/hive/warehouse/stock_ticks_cow --target-table stock_ticks_cow --props /hudi/config/kafka-source.properties --schemaprovider-class org.apache.hudi.utilities.schema.FilebasedSchemaProvider
spark-submit --class org.apache.hudi.utilities.deltastreamer.HoodieDeltaStreamer  --master yarn ./hudi-utilities-bundle_2.11-0.5.1-incubating.jar  --table-type MERGE_ON_READ --source-class org.apache.hudi.utilities.sources.JsonKafkaSource --source-ordering-field ts  --target-base-path /usr/hive/warehouse/stock_ticks_mor --target-table stock_ticks_mor --props /hudi/config/kafka-source.properties --schemaprovider-class org.apache.hudi.utilities.schema.FilebasedSchemaProvider --disable-compaction
```
10.	查询增量数据，查询方法同步骤7。
11.	使用 hudi-cli 工具。
```
 cli/bin/hudi-cli.sh
connect --path /usr/hive/warehouse/stock_ticks_mor
compactions show all
compaction schedule
合并执行计划
 compaction run --compactionInstant [requestID] --parallelism 2 --sparkMemory 1G  --schemaFilePath /hudi/config/schema.avsc --retry 1
```
12.	 使用 tez/spark 引擎查询。
```
beeline -u jdbc:hive2://[hiveserver2_ip:hiveserver2_port] -n hadoop --hiveconf hive.input.format=org.apache.hadoop.hive.ql.io.HiveInputFormat --hiveconf hive.stats.autogather=false
set hive.execution.engine=tez;
set hive.execution.engine=spark;
```
然后执行 sql 查询，可参考步骤7。

## 与对象存储结合使用
与 hdfs 类似，需要在存储路径前加上`cosn://[bucket]`。参考如下操作：
```
bin/kafka-server-start.sh config/server.properties &
cat     demo/data/batch_1.json | kafkacat -b kafkaip -t stock_ticks -P
cat     demo/data/batch_2.json | kafkacat -b kafkaip -t stock_ticks -P
kafkacat -b kafkaip  -L
hdfs dfs -mkdir -p cosn://[bucket]/hudi/config
hdfs dfs -copyFromLocal demo/config/*  cosn://[bucket]/hudi/config/

spark-submit --class org.apache.hudi.utilities.deltastreamer.HoodieDeltaStreamer --master yarn ./hudi-utilities-bundle_2.11-0.5.1-incubating.jar   --table-type COPY_ON_WRITE --source-class org.apache.hudi.utilities.sources.JsonKafkaSource --source-ordering-field ts  --target-base-path cosn://[bucket]/usr/hive/warehouse/stock_ticks_cow --target-table stock_ticks_cow --props cosn://[bucket]/hudi/config/kafka-source.properties --schemaprovider-class org.apache.hudi.utilities.schema.FilebasedSchemaProvider

spark-submit --class org.apache.hudi.utilities.deltastreamer.HoodieDeltaStreamer  --master yarn ./hudi-utilities-bundle_2.11-0.5.1-incubating.jar  --table-type MERGE_ON_READ --source-class org.apache.hudi.utilities.sources.JsonKafkaSource --source-ordering-field ts  --target-base-path cosn://[bucket]/usr/hive/warehouse/stock_ticks_mor --target-table stock_ticks_mor --props cosn://[bucket]/hudi/config/kafka-source.properties --schemaprovider-class org.apache.hudi.utilities.schema.FilebasedSchemaProvider --disable-compaction

bin/run_sync_tool.sh  --jdbc-url jdbc:hive2://[hiveserver2_ip:hiveserver2_port] --user hadoop --pass isd@cloud --partitioned-by dt --base-path cosn://[bucket]/usr/hive/warehouse/stock_ticks_cow --database default --table stock_ticks_cow

bin/run_sync_tool.sh  --jdbc-url jdbc:hive2://[hiveserver2_ip:hiveserver2_port] --user hadoop --pass hive --partitioned-by dt --base-path cosn://[bucket]/usr/hive/warehouse/stock_ticks_mor --database default --table stock_ticks_mor --skip-ro-suffix


beeline -u jdbc:hive2://[hiveserver2_ip:hiveserver2_port] -n hadoop --hiveconf hive.input.format=org.apache.hadoop.hive.ql.io.HiveInputFormat --hiveconf hive.stats.autogather=false

spark-sql --master yarn --conf spark.sql.hive.convertMetastoreParquet=false

hivesqls:
select symbol, max(ts) from stock_ticks_cow group by symbol HAVING symbol = 'GOOG';
select `_hoodie_commit_time`, symbol, ts, volume, open, close  from stock_ticks_cow where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor group by symbol HAVING symbol = 'GOOG';
select `_hoodie_commit_time`, symbol, ts, volume, open, close  from stock_ticks_mor where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor_rt group by symbol HAVING symbol = 'GOOG';
select `_hoodie_commit_time`, symbol, ts, volume, open, close  from stock_ticks_mor_rt where  symbol = 'GOOG';

prestosqls:
/usr/local/service/presto-client/presto --server localhost:9000 --catalog hive --schema default --user Hadoop
select symbol, max(ts) from stock_ticks_cow group by symbol HAVING symbol = 'GOOG';
select "_hoodie_commit_time", symbol, ts, volume, open, close  from stock_ticks_cow where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor group by symbol HAVING symbol = 'GOOG';
select "_hoodie_commit_time", symbol, ts, volume, open, close  from stock_ticks_mor where  symbol = 'GOOG';
select symbol, max(ts) from stock_ticks_mor_rt group by symbol HAVING symbol = 'GOOG';
select "_hoodie_commit_time", symbol, ts, volume, open, close  from stock_ticks_mor_rt where  symbol = 'GOOG';

cli/bin/hudi-cli.sh
connect --path cosn://[bucket]/usr/hive/warehouse/stock_ticks_mor
compactions show all
compaction schedule
compaction run --compactionInstant [requestid]  --parallelism 2 --sparkMemory 1G  --schemaFilePath cosn://[bucket]/hudi/config/schema.avsc --retry 1
```


