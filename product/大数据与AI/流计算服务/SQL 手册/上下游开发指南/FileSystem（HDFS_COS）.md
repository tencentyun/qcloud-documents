## 介绍
FileSystem connector 提供了对 HDFS 和 COS 等常见文件系统的写入支持。

## 使用范围

FileSystem 支持作为 Append-Only 数据流的目的表（Sink），目前还不支持 Upsert 数据流的目的表。

FileSystem 目前支持以下格式的数据写入
* CSV
* JSON
* Avro
* Parquet
* Orc

## 示例：用作数据目的

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

| 参数值 | 必填 | 默认值 | 描述 |
| --- | --- | --- | --- |
| path | 是 | 无 | 文件写入的路径。 |
| sink.rolling-policy.file-size | 否 | 128MB | 文件最大大小。若当前写入的文件大小达到设置的阈值时，当前写入的文件将被关闭，并打开一个新的文件进行写入。 |
| sink.rolling-policy.rollover-interval | 否 | 30min | 文件最大持续写入时间。若当前写入的文件写入的时间超过了设置的阈值时，当前写入的文件将被关闭，并打开一个新的文件进行写入。 |
| sink.rolling-policy.check-interval | 否 | 1min | 文件检查间隔。FileSystem 按照这个间隔检查文件的写入时间是否已经满足了关闭条件，并将满足条件的文件进行关闭。 |
| sink.partition-commit.trigger | 否 | process-time | 分区关闭策略。可选值包括 * processing-time：当分区创建超过一定时间之后将这个分区关闭，分区创建时间为分区创建时的物理时间。* partition-time: 当分区创建超过一定时间之后将这个分区关闭，分区创建时间从分区中抽取出来。 |
| sink.partition-commit.delay | 否 | 0s | 分区关闭延迟。当分区在创建超过一定时间之后将被关闭。 |
| partition.time-extractor.kind | 否 | default | 分区时间抽取方式。这个配置仅当 sink.partition-commit.trigger 配置为 partition-time 时生效。如果用户有自定义的分区时间抽取方法，配置为 custom。 |
| partition.time-extractor.class | 否 | 无 | 分区时间抽取类，这个类必须实现 PartitionTimeExtractor 接口。 |
| sink.partition-commit.policy.kind | 是 | 无 | 用于提交分区的策略。可选值包括 * success-file: 当分区关闭时将在分区对应的目录下生成一个_success 的文件。* custom: 用户实现的自定义分区提交策略。 |
| sink.partition-commit.policy.class | 否 | 无 | 分区提交类，这个类必须实现 PartitionCommitPolicy。 |

## HDFS 配置

在使用 HDFS 作为数据写入的文件系统时，用户需要在作业参数的高级参数中对 HDFS 的地址进行配置。常见的配置项包括：
* fs.hdfs.dfs.nameservices: HDFS nameserivce 名称
* fs.hdfs.dfs.ha.namenodes.{nameservice}: nameservice 的 name node 列表
* fs.hdfs.dfs.namenode.http-address.${nameserivce}.${nn}: nameserivce 中 name node 的 Http 地址
* fs.hdfs.dfs.namenode.https-address.${nameservice}.${nn}: nameservice中 name node 的 Https 地址
* fs.hdfs.dfs.namenode.rpc-address.${nameservice}.${nn}: nameserivce 中 name node 的 Rpc 地址
* fs.hdfs.dfs.client.failover.proxy.provider.${nameservice}: org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider

如有多个 node，需配置每个 node 的 http-address、https-address 和 rpc-address。

## COS 配置

>?当写入 COS 时，Oceanus 作业所运行的地域必须和 COS 在同一个地域中。

在使用 COS 作为数据写入的文件系统时，用户需要在内置 Connector 中勾选 flink-connector-cos，并在作业参数的高级参数中对 COS 的地址进行配置。常见的配置项包括：
* fs.AbstractFileSystem.cosn.impl: org.apache.hadoop.fs.CosN
* fs.cosn.impl: org.apache.hadoop.fs.CosFileSystem
* fs.cosn.credentials.provider: org.apache.flink.fs.cos.OceanusCOSCredentialsProvider
* fs.cosn.bucket.region: COS 所在的地域（如 ap-guangzhou 或 ap-chengdu）
* fs.cosn.userinfo.appid: COS 所属用户的 AppID

配置示意图：
![](https://main.qcloudimg.com/raw/56b95e89a8bddfec4a3d17ea5ee85bbd.png)
