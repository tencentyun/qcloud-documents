## 介绍
FileSystem connector 提供了对 HDFS 和 COS 等常见文件系统的写入支持。

## 使用范围
FileSystem 支持作为 Append-Only 数据流的目的表 (Sink)，目前还不支持 Upsert 数据流的目的表。FileSystem 目前支持以下格式的数据写入：
- CSV
- JSON
- Avro
- Parquet
- Orc

## 示例
#### 用作数据目的
```sql
CREATE TABLE `DataOutput` (
    f1 INT,
    f2 STRING,
    part1 INT,
    part2 INT
) PARTITIONED BY (part1, part2) WITH (
    'connector' = 'filesystem',
      'path' = 'hdfs://HDFS10000/data/',
    'format' = 'json',
    'sink.rolling-policy.file-size' = '1M',
    'sink.rolling-policy.rollover-interval' = '10 min',
    'sink.partition-commit.delay' = '1 s',
    'sink.partition-commit.policy.kind' = 'success-file'
);
```

## 通用 WITH 参数

| 参数值                                     | 必填 | 默认值       | 描述                                                         |
| ------------------------------------------ | ---- | ------------ | ------------------------------------------------------------ |
| path                                       | 是   | 无           | 文件写入的路径。                                             |
| sink.rolling-policy.file-size              | 否   | 128MB        | 文件最大大小。当当前写入的文件大小达到设置的阈值时，当前写入的文件将被关闭，并打开一个新的文件进行写入。 |
| sink.rolling-policy.rollover-interval      | 否   | 30min        | 文件最大持续写入时间。当当前写入的文件写入的时间超过了设置的阈值时，当前写入的文件将被关闭，并打开一个新的文件进行写入。 |
| sink.rolling-policy.check-interval         | 否   | 1min         | 文件检查间隔。FileSystem 按照这个间隔检查文件的写入时间是否已经满足了关闭条件，并将满足条件的文件进行关闭。 |
| sink.partition-commit.trigger              | 否   | process-time | 分区关闭策略。可选值包括：<li/>process-time：当分区创建超过一定时间之后将这个分区关闭，分区创建时间为分区创建时的物理时间。<li/>partition-time：当分区创建超过一定时间之后将这个分区关闭，分区创建时间从分区中抽取出来。partition-time 依赖于 watermark 生成，需要配合 wartermark 才能支持自动分区发现。当 watermark 时间超过了 `从分区抽取的时间` 与 `delay 参数配置时间` 之和后会提交分区。 |
| sink.partition-commit.delay                | 否   | 0s           | 分区关闭延迟。当分区在创建超过一定时间之后将被关闭。         |
| partition.time-extractor.kind              | 否   | default      | 分区时间抽取方式。这个配置仅当 sink.partition-commit.trigger 配置为 partition-time 时生效。如果用户有自定义的分区时间抽取方法，配置为 custom。 |
| partition.time-extractor.class             | 否   | 无           | 分区时间抽取类，这个类必须实现 PartitionTimeExtractor 接口。 |
| partition.time-extractor.timestamp-pattern | 否   | 无           | 分区时间戳的抽取格式。需要写成 yyyy-MM-dd HH:mm:ss 的形式，并用 Hive 表中相应的分区字段做占位符替换。默认支持第一个字段为 yyyy-mm-dd hh:mm:ss。<li/>如果时间戳应该从单个分区字段 'dt' 提取，可以配置 '$dt'。<li/>如果时间戳应该从多个分区字段中提取，例如 'year'、'month'、'day' 和 'hour'，可以配置 '$year-$month-$day $hour:00:00'。<li/>如果时间戳应该从两个分区字段 'dt' 和 'hour' 提取，可以配置 '$dt $hour:00:00'。 |
| sink.partition-commit.policy.kind          | 是   | 无           | 用于提交分区的策略。可选值包括：<li/>success-file：当分区关闭时将在分区对应的目录下生成一个 \_success 的文件。<li/>custom：用户实现的自定义分区提交策略。 |
| sink.partition-commit.policy.class         | 否   | 无           | 分区提交类，这个类必须实现 PartitionCommitPolicy。           |

## HDFS 配置
在 HDFS 上创建数据目录后，需为目录开启写权限，才可成功写入数据。流计算 Oceanus 写入 HDFS 的 user 是 flink。进行配置前，需要先导出 Hadoop 集群的 hdfs-site.xml 文件，以获取下列配置中所需的参数值，导出方式可参考 [导出软件配置](https://cloud.tencent.com/document/product/589/37098)。

HDFS 路径的形式为 `hdfs://${dfs.nameserivces}/${path}`，`${dfs.nameserivces}` 的值可在 hdfs-site.xml 中查找，`${path}` 为要写入的数据目录。

- 若目标 Hadoop 集群只有单个 Master，仅需要为 path 参数传入 HDFS 路径即可，无需使用高级参数。
- 若目标 Hadoop 集群为高可用的双 Master 集群，为 path 参数传入 HDFS 路径后，还需要在作业参数的 [高级参数](https://cloud.tencent.com/document/product/849/53391) 中对两个 Master 的地址和端口进行配置。以下是一个配置示例，相应的参数值都可在 hdfs-site.xml 中查找并替换。
```yml
fs.hdfs.dfs.nameservices: HDFS12345
fs.hdfs.dfs.ha.namenodes.HDFS12345: nn2,nn1
fs.hdfs.dfs.namenode.http-address.HDFS12345.nn1: 172.27.2.57:4008
fs.hdfs.dfs.namenode.https-address.HDFS12345.nn1: 172.27.2.57:4009
fs.hdfs.dfs.namenode.rpc-address.HDFS12345.nn1: 172.27.2.57:4007
fs.hdfs.dfs.namenode.http-address.HDFS12345.nn2: 172.27.1.218:4008
fs.hdfs.dfs.namenode.https-address.HDFS12345.nn2: 172.27.1.218:4009
fs.hdfs.dfs.namenode.rpc-address.HDFS12345.nn2: 172.27.1.218:4007
fs.hdfs.dfs.client.failover.proxy.provider.HDFS12345: org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider
```

## COS 配置
>?当写入 COS 时，Oceanus 作业所运行的地域必须和 COS 在同一个地域中。

在使用 COS 作为数据写入的文件系统时，用户需要在内置 Connector 中勾选 flink-connector-cos，并在作业参数的 [高级参数](https://cloud.tencent.com/document/product/849/53391) 中对 COS 的地址进行配置。流计算 Oceanus 写入 COS 的 user 是 flink。需要的配置项如下，其中地域的取值可参考 [对象存储-地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
```yml
fs.AbstractFileSystem.cosn.impl: org.apache.hadoop.fs.CosN
fs.cosn.impl: org.apache.hadoop.fs.CosFileSystem
fs.cosn.credentials.provider: org.apache.flink.fs.cos.OceanusCOSCredentialsProvider
fs.cosn.bucket.region: COS 所在的地域
fs.cosn.userinfo.appid: COS 所属用户的 appid
```

配置示意图：
![](https://main.qcloudimg.com/raw/56b95e89a8bddfec4a3d17ea5ee85bbd.png)

