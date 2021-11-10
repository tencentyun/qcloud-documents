## 介绍
FileSystem connector 提供了对 `HDFS` 和 [COS](https://cloud.tencent.com/document/product/436) 等常见文件系统的写入支持。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围
FileSystem 支持作为 Append-Only 数据流的目的表 (Sink)，目前还不支持 Upsert 数据流的目的表。FileSystem 目前支持以下格式的数据写入：
- CSV
- JSON
- Avro
- Parquet
- Orc

>?目前使用数据格式 Avro、Parquet、Orc 写入时，需要 [手动上传额外的 jar 包](#jump) 才能使用。

## DDL 定义
#### 用作数据目的
```sql
CREATE TABLE `hdfs_sink_table` (
    `id` INT,
    `name` STRING,
    `part1` INT,
    `part2` INT
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

## WITH 参数

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

>? Flink 作业默认以 flink 用户操作 HDFS，若没有 HDFS 路径的写入权限，可通过作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 设置为有权限的用户，或者设置为超级用户 hadoop。
>```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
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

[](id:jump)
## 手动上传对应 Jar 包
1. 先下载对应 Jar 包到本地。
 - Avro：[Jar 包下载地址](https://repo.maven.apache.org/maven2/org/apache/flink/flink-avro/1.11.2/flink-avro-1.11.2-sql-jar.jar)
 - Parquet：[Jar 包下载地址](https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-parquet_2.11/1.11.2/flink-sql-parquet_2.11-1.11.2.jar)
 - Orc：[Jar 包下载地址](https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-orc_2.11/1.11.2/flink-sql-orc_2.11-1.11.2.jar)
2. 在 Oceanus 的程序包管理上传对应 Jar 包，详情可参见 [程序包管理](https://cloud.tencent.com/document/product/849/48295)。
3. 进入对应作业的开发调试界面，打开作业参数侧栏。
   ![](https://main.qcloudimg.com/raw/74fa13f156b114df80fd84aac4bf0554.png)
   在作业参数的引用程序包栏单击**添加程序包**，选择在第2步上传的 Jar 包，单击**确定**保存作业参数配置。
   ![](https://main.qcloudimg.com/raw/19734292615ac8cacb3c6a3a9422acef.png)
4. 发布作业。

## HDFS Kerberos 认证授权

1. 登录集群 Master 节点，获取 krb5.conf、emr.keytab、core-site.xml、hdfs-site.xml 文件，路径如下。
```
/etc/krb5.conf
/var/krb5kdc/emr.keytab
/usr/local/service/hadoop/etc/hadoop/core-site.xml
/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml
```
2. 对步骤1中获取的文件打 jar 包。
```
jar cvf hdfs-xxx.jar krb5.conf emr.keytab core-site.xml hdfs-site.xml
```
3. 校验 jar 的结构（可以通过 vim 命令查看 vim hdfs-xxx.jar），jar 里面包含如下信息，请确保文件不缺失且结构正确。
```
META-INF/
META-INF/MANIFEST.MF
emr.keytab
krb5.conf
hdfs-site.xml
core-site.xml
```
4. 在 [程序包管理](https://console.cloud.tencent.com/oceanus/resource) 页面上传 jar 包，并在作业参数配置里引用该程序包。
5. 获取 kerberos principal，用于作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
klist -kt /var/krb5kdc/emr.keytab

# 输出如下所示，选取第一个即可：hadoop/172.28.28.51@EMR-OQPO48B9
KVNO Timestamp     Principal
---- ------------------- ------------------------------------------------------
  2 08/09/2021 15:34:40 hadoop/172.28.28.51@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 HTTP/172.28.28.51@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 hadoop/VM-28-51-centos@EMR-OQPO48B9 
  2 08/09/2021 15:34:40 HTTP/VM-28-51-centos@EMR-OQPO48B9 
```
6. 作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
security.kerberos.login.principal: hadoop/172.28.28.51@EMR-OQPO48B9
security.kerberos.login.keytab: emr.keytab
security.kerberos.login.conf: krb5.conf
```
如果是 Flink-1.13 版本，需要在高级参数额外增加如下参数，其中参数的值需要为对应 `hdfs-site.xml` 中的值。
```
fs.hdfs.dfs.nameservices: HDFS17995
fs.hdfs.dfs.ha.namenodes.HDFS17995: nn2,nn1
fs.hdfs.dfs.namenode.http-address.HDFS17995.nn1: 172.28.28.214:4008
fs.hdfs.dfs.namenode.https-address.HDFS17995.nn1: 172.28.28.214:4009
fs.hdfs.dfs.namenode.rpc-address.HDFS17995.nn1: 172.28.28.214:4007
fs.hdfs.dfs.namenode.http-address.HDFS17995.nn2: 172.28.28.224:4008
fs.hdfs.dfs.namenode.https-address.HDFS17995.nn2: 172.28.28.224:4009
fs.hdfs.dfs.namenode.rpc-address.HDFS17995.nn2: 172.28.28.224:4007
fs.hdfs.dfs.client.failover.proxy.provider.HDFS17995: org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider
fs.hdfs.hadoop.security.authentication: kerberos
```

>! 历史 Oceanus 集群可能不支持该功能，您可通过 [在线客服](https://cloud.tencent.com/act/event/Online_service?from=doc_849) 联系我们升级集群管控服务，以支持 Kerberos 访问。

## 代码示例
```sql
CREATE TABLE datagen_source_table (
  id INT, 
  name STRING,
  part1 INT,
  part2 INT 
) WITH ( 
  'connector' = 'datagen',
  'rows-per-second'='1',  -- 每秒产生的数据条数
  'fields.part1.min'='1',
  'fields.part1.max'='2',
  'fields.part2.min'='1',
  'fields.part2.max'='2'
);

CREATE TABLE `hdfs_sink_table` (
    id INT,
    name STRING,
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

INSERT INTO `hdfs_sink_table` 
SELECT id, name, part1, part2
FROM datagen_source_table;
```

