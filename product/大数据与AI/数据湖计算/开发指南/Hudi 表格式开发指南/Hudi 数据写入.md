DLC Hudi 当前支持用 spark streaming 和 Flink 实时把外部数据入湖。

### Spark Streaming 实时写入
DLC 支持部署 Spark Streaming 作业，推荐使用 DLC Spark 作业写入 DLC Hudi 表。
- 代码示例
```java
kafkaDF.writeStream
    .option("checkpointLocation","cosn://<cos_bucket>/spark_hudi/spark_ck")
    .trigger(Trigger.ProcessingTime(10, TimeUnit.SECONDS))
    .queryName("write hudi")
    .foreachBatch((batchDF:DataFrame,_:Long)=>{
        batchDF.write
        .mode(SaveMode.Append)
        .format("hudi")
        .option("hoodie.datasource.write.table.type","MERGE_ON_READ")
        .option("hoodie.datasource.write.precombine.field","ts")
        .option("hoodie.datasource.write.recordkey.field","uuid")
        .option("hoodie.datasource.write.partitionpath.field","partitionpath")
        .option("hoodie.datasource.write.table.name","hudi_mor")
        .save("cosn://<cos_bucket>/spark_hudi/hudi_mor")
    }).start().awaitTermination()
```

### Flink 实时写入
除推荐的 DLC SPARK 作业外，您也可以选择腾讯云流计算 Oceanus 实时写入 DLC Hudi，详情参考[ Oceanus 产品文档](https://cloud.tencent.com/document/product/849)。
如您想通过自建 Flink 程序写入 DLC Hudi 表，可以参考如下代码示例：
```java
//准备flink stream table执行环境
EnvironmentSettings settings = EnvironmentSettings
    .newInstance()
    .inStreamingMode()
    .build();
StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env, settings) ;
```
```java
//指定kafka source表
tableEnv.executeSql("CREATE TABLE tbl_kafka (\n" +
    "\tuuid STRING,\n" +
    "\trider STRING,\n" +
    "\tdriver STRING,\n" +
    "\tbegin_lat DOUBLE,\n" +
    "\tbegin_lon DOUBLE,\n" +
    "\tend_lat DOUBLE,\n" +
    "\tend_lon DOUBLE,\n" +
    "\tfare DOUBLE,\n" +
    "\tpartitionpath STRING,\n" +
    "\tts BIGINT\n" +
    ") WITH (\n" +
    "  'connector' = 'kafka',\n" +
    "  'topic' = 'hudi_source',\n" +
    "  'properties.bootstrap.servers' = '<kafka_server>:9092',\n" +
    "  'properties.group.id' = 'test-group-10001',\n" +
    "  'scan.startup.mode' = 'latest-offset',\n" +
    "  'format' = 'json'\n" +
    ")");
```
```java
//指定hudi target表
tableEnv.executeSql("CREATE TABLE hudi_cow (\n" +
    "uuid STRING PRIMARY KEY NOT ENFORCED,\n" +
    "rider STRING,\n" +
    "driver STRING,\n" +
    "begin_lat DOUBLE,\n" +
    "begin_lon DOUBLE,\n" +
    "end_lat DOUBLE,\n" +
    "end_lon DOUBLE,\n" +
    "fare DOUBLE,\n" +
    "partitionpath STRING,\n" +
    "ts BIGINT\n" +
    ") " +
    "partitioned by(partitionpath) " +
    "WITH (\n" +
    "  'connector' = 'hudi',\n" +
    "  'path' = 'cosn://<cos_bucket>/flink_hudi/hudi_cow',\n" +
    "  'fs.cosn.impl' = 'org.apache.hadoop.fs.CosFileSystem',\n" +
    "  'fs.AbstractFileSystem.cosn.impl' = 'org.apache.hadoop.fs.CosN',\n" +
    "  'fs.cosn.bucket.region' = 'ap-chongqing',\n" +
    "  'fs.cosn.credentials.provider' = 'org.apache.hadoop.fs.auth.SimpleCredentialProvider',\n" +
    "  'fs.cosn.userinfo.secretId' = '<secretId>',\n" +
    "  'fs.cosn.userinfo.secretKey' = '<secretKey>',\n" +
    "  'table.type' = 'COPY_ON_WRITE',\n" +
    "  'write.operation' = 'upsert',\n" +
    "  'hoodie.datasource.write.recordkey.field' = 'uuid',\n" +
    "  'write.precombine.field' = 'ts',\n" +
    "  'write.tasks' = '1'\n" +
    ")");
```
```Java
//使用flink sql写入hudi表
tableEnv.executeSql("insert into hudi_cow select uuid,rider,driver,begin_lat,begin_lon,end_lat,end_lon,fare,partitionpath,ts from tbl_kafka");
```

### 相关配置
- 常用写入配置
<table>
<thead>
<tr>
<th>参数</th>
<th>默认值</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>hoodie.datasource.write.table.name</td>
<td>无</td>
<td>指定写入的 hudi 表名</td>
</tr>
<tr>
<td>hoodie.datasource.write.table.type</td>
<td>COPY_ON_WRITE</td>
<td>指定 hudi 表类型，一旦这个表类型被指定，后续禁止修改该参数，可选值：<code>COPY_ON_WRITE</code>， <code>MERGE_ON_READ</code></td>
</tr>
<tr>
<td>hoodie.datasource.write.operation</td>
<td>upsert</td>
<td>写 hudi 表指定的操作类型，当前支持 <code>upsert</code>、<code>delete</code>、<code>insert</code>、<code>bulk_insert</code>、<code>insert_overwrite</code>、<code>insert_overwrite_table</code> 方式</td>
</tr>
<tr>
<td>hoodie.datasource.write.recordkey.field</td>
<td>uuid</td>
<td>用于指定 hudi 的主键，hudi 表要求有唯一主键</td>
</tr>
<tr>
<td>hoodie.datasource.write.partitionpath.field</td>
<td>无</td>
<td>用于指定分区键，该值配合 hoodie.datasource.write.keygenerator.class 使用可以满足不同的分区场景</td>
</tr>
<tr>
<td>hoodie.datasource.write.hive_style_partitioning</td>
<td>false</td>
<td>用于指定分区方式是否和 hive 保持一致，建议该值设置为 true</td>
</tr>
<tr>
<td>hoodie.datasource.write.precombine.field</td>
<td>ts</td>
<td>该值用于在写之前对具有相同的 key 的行进行合并去重</td>
</tr>
</tbody></table>

- Compaction 配置
Compaction 用于合并 mor 表 Base 和 Log 文件，对于 Merge-On-Read 表，数据使用列式 Parquet 文件和行式 Avro 文件存储，更新被记录到增量文件，然后进行同步/异步 compaction 生成新版本的列式文件。
Merge-On-Read 表可减少数据摄入延迟，推荐使用同步产生 compaction 调度计划，异步执行 compaction 调度计划的方式。
<table>
<thead>
<tr>
<th>参数</th>
<th>默认值</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>hoodie.compact.schedule.inline</td>
<td>false</td>
<td>每次任务完成是否生成 compact plan，建议设置为 true</td>
</tr>
<tr>
<td>hoodie.compact.inline</td>
<td>false</td>
<td>是否在一个事务完成后内联执行压缩操作，这里开启并不一定每次都会触发索引操作后面还有策略判断</td>
</tr>
<tr>
<td>hoodie.compact.inline.trigger.strategy</td>
<td>CompactionTriggerStrategy.NUM_COMMITS</td>
<td>压缩策略参数，该参数有 NUM_COMMITS、TIME_ELAPSED、NUM_AND_TIME、NUM_OR_TIME<br><br>NUM_COMMITS根据提交次数来判断是否进行压缩;<br>TIME_ELAPSED 根据时间来判断是否进行压缩<br>NUM_AND_TIME 根据提交次数和时间来判断是否进行压缩<br>NUM_OR_TIME 根据提交次数或时间来判断是否进行压缩</td>
</tr>
<tr>
<td>hoodie.compact.inline.max.delta.commits</td>
<td>5</td>
<td>设置提交多少次后触发压缩策略。在 NUM_COMMITS、NUM_AND_TIME和NUM_OR_TIME 策略中生效</td>
</tr>
<tr>
<td>hoodie.compact.inline.max.delta.seconds</td>
<td>60 * 60（1小时）</td>
<td>设置在经过多长时间后触发压缩策略。在TIME_ELAPSED、NUM_AND_TIME和NUM_OR_TIME 策略中生效</td>
</tr>
<tr>
<td>hoodie.parquet.small.file.limit</td>
<td>104857600(100MB)</td>
<td>小于这个值的是小文件，新增的数据会优先往小文件里写</td>
</tr>
</tbody></table>

### 单表并发写入控制
如果写入时 Hudi 表只有一个客户端在写入，此时不会遇到写数据冲突的情况。
但在实际应用中，如果存在多个客户端同时写入，例如多个流程序需要同时写入同一张 Hudi 表的场景，就会出现写冲突造成任务失败的情况，这种情况我们称之为并发写，要解决并发写问题可以借助 DLC Metastore 实现基于乐观锁的并发写。
- 启用并发写入机制：
```SQL
hoodie.write.concurrency.mode=optimistic_concurrency_control

hoodie.cleaner.policy.failed.writes=LAZY
```

- 设置并发锁方式为 DLC Metastore 方式：
```SQL
hoodie.write.lock.provider=org.apache.hudi.hive.HiveMetastoreBasedLockProvider

hoodie.write.lock.hivemetastore.database=<database_name>

hoodie.write.lock.hivemetastore.table=<table_name>
```
- DLC Spark MultiWriter 示例：
```java
    kafkaDF.writeStream

      .option("checkpointLocation","cosn://<cos_bucket>/spark_hudi/spark_ck/writer2")

      .trigger(Trigger.ProcessingTime(10, TimeUnit.SECONDS))

      .queryName("write hudi")

      .foreachBatch((batchDF:DataFrame,_:Long)=>{

        batchDF.write

          .mode(SaveMode.Append)

          .format("hudi")

          .option("hoodie.datasource.write.table.type","MERGE_ON_READ")

          .option("hoodie.datasource.write.precombine.field","ts")

          .option("hoodie.datasource.write.recordkey.field","uuid")

          .option("hoodie.datasource.write.partitionpath.field","partitionpath")

          .option("hoodie.datasource.write.table.name","multi_writer")

          .option("hoodie.write.concurrency.mode","optimistic_concurrency_control")

          .option("hoodie.cleaner.policy.failed.writes","LAZY")

          .option("hoodie.write.lock.provider","org.apache.hudi.hive.transaction.lock.HiveMetastoreBasedLockProvider")

          .option("hoodie.write.lock.hivemetastore.database","spark_hudi")

          .option("hoodie.write.lock.hivemetastore.table","multi_writer")

          .save("cosn://<cos_bucket>/spark_hudi/multi_writer")

      }).start().awaitTermination()
```
