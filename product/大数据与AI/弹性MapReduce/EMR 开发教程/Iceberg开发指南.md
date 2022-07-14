## Iceberg 简介
Apache Iceberg 是一种新型的用于大规模数据分析的开源表格式。它被设计用于存储移动缓慢的大型表格数据。它旨在改善 Hive、Trino（PrestoSQL）和 Spark 中内置的事实上的标准表布局。Iceberg 可以屏蔽底层数据存储格式上的差异，向上提供统一的操作 API，使得不同的引擎可以通过其提供的 API 接入。

Apache Iceberg 具备以下能力：
- 模式演化（Schema evolution）：支持 Add（添加）、Drop（删除）、Update（更新）、Rename（重命名）和 Reorder（重排）表格式定义。
- 分区布局演变（Partition layout evolution）：可以随着数据量或查询模式的变化而更新表的布局。
- 隐式分区（Hidden partitioning）：查询不再取决于表的物理布局。通过物理和逻辑之间的分隔，Iceberg 表可以随着数据量的变化和时间的推移发展分区方案。错误配置的表可以得到修复，无需进行昂贵的迁移。
- 时光穿梭（Time travel）：支持用户使用完全相同的快照进行重复查询，或者使用户轻松检查更改。
- 版本回滚（Version rollback）：使用户可以通过将表重置为良好状态来快速纠正问题。

在可靠性与性能方面，Iceberg 可在生产中应用到数十 PB 的数据表，即使没有分布式 SQL 引擎，也可以读取这些巨大规模的表：
- 扫描速度快，无需使用分布式 SQL 引擎即可读取表或查找文件。
- 高级过滤，基于表元数据，使用分区和列级统计信息对数据文件以进行裁剪。

Iceberg 被设计用来解决最终一致的云对象存储中的正确性问题：
- 可与任何云存储一起使用，并且通过避免调用 list 和 rename 来减少 HDFS 的 NameNode 拥塞。
- 可序列化的隔离，表更改是原子性的，用户永远不会看到部分更改或未提交的更改。
- 多个并发写入使用乐观锁机制进行并发控制，即使写入冲突，也会重试以确保兼容更新成功。

Iceberg 设计为以快照（Snapshot）的形式来管理表的各个历史版本数据。快照代表一张表在某个时刻的状态。每个快照中会列出表在某个时刻的所有数据文件列表。Data 文件存储在不同的 Manifest 文件中，Manifest 文件存储在一个 Manifest List 文件中，Manifest 文件可以在不同的 Manifest List 文件间共享，一个 Manifest List 文件代表一个快照。
- Manifest list 文件是元数据文件，其中存储的是 Manifest 文件的列表，每个 Manifest 文件占据一行。
-	Manifest 文件是元数据文件，其中列出了组成某个快照的数据文件列表。每行都是每个数据文件的详细描述，包括数据文件的状态、文件路径、分区信息、列级别的统计信息（例如每列的最大最小值、空值数等）、文件的大小以及文件中数据的行数等信息。
- Data 文件是 Iceberg 表真实存储数据的文件，一般是在表的数据存储目录的 data 目录下。

## 使用示例
更多示例可参考 [Iceberg 官网示例](https://iceberg.apache.org/getting-started)。
1. 登录 master 节点，切换为 hadoop 用户。
2. Iceberg 相关的包放置在 `/usr/local/service/iceberg/` 下面。
3. 使用计算引擎查询数据。
 - Spark 引擎
    - Spark-SQL 交互式命令行
```
spark-sql --master local[*] --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions--conf spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog--conf spark.sql.catalog.local.type=hadoop --conf spark.sql.catalog.local.warehouse=/usr/hive/warehouse --jars /usr/local/service/iceberg/iceberg-spark3-runtime-0.11.0.jar

```
    - 插入和查询数据
```
CREATE TABLE local.default.t1 (id int, name string) USING iceberg;
INSERT INTO local.default.t1 values(1, "tom");
SELECT * from local.default.t1;
```
 - Hive 引擎
    - 使用 beeline
```
beeline -u jdbc:hive2://[hiveserver2_ip:hiveserver2_port] -n hadoop --hiveconf hive.input.format=org.apache.hadoop.hive.ql.io.HiveInputFormat --hiveconf hive.stats.autogather=false
```
    - 查询数据
```
ADD JAR /usr/local/service/hive/lib/iceberg-hive-runtime-0.11.0.jar;
CREATE EXTERNAL TABLE t1 STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler' LOCATION '/usr/hive/warehouse/default/t1';
select count(*) from t1;
```
 - Flink 引擎
    - 启动一个 Flink standalone 集群和 Flink 交互式
```
wget https://repo1.maven.org/maven2/org/apache/flink/flink-sql-connector-hive-3.1.2_2.11/1.12.1/flink-sql-connector-hive-3.1.2_2.11-1.12.1.jar
/usr/local/service/flink/bin/start-cluster.sh
sql-client.sh embedded -j /usr/local/service/iceberg/iceberg-flink-runtime-0.11.0.jar -j flink-sql-connector-hive-3.1.2_2.11-1.12.1.jar shell
```
    - 查询数据
```
CREATE CATALOG hive_catalog WITH ('type'='iceberg','catalog-type'='hive','uri'='hivemetastore_ip:hivemetastore_port','clients'='5','property-version'='1','warehouse'='hdfs:///usr/hive/warehouse/');
CREATE DATABASE hive_catalog.iceberg_db;
CREATE TABLE hive_catalog.iceberg_db.t1 (id BIGINT COMMENT 'unique id',data STRING);
INSERT INTO hive_catalog.iceberg_db.t1 values(1, 'tom');
SELECT count(*) from hive_catalog.iceberg_db.t1;
```

