## 介绍
Hive Connector 支持数据流的目的表，但只支持 append only，不支持 Upsert 数据流。数据格式支持包括 Text、SequenceFile、ORC 和 Parquet 等。

## 版本说明

| Flink 版本 | 说明                                                         |
| :-------- | :----------------------------------------------------------- |
| 1.11      | <li>支持 hive 版本 1.1.0、2.3.2、2.3.5、3.1.1</li><li>配置项 'connector.type' = 'hive'</li> |
| 1.13      | <li>支持 hive 版本 1.0.0 ~ 1.2.2、2.0.0 ~ 2.2.0、2.3.0 ~ 2.3.6、3.0.0 ~ 3.1.2</li><li>配置项 'connector' = 'hive'</li> |
| 1.14      | 不支持 |

## DDL 定义

#### 用作数据目的（Sink）

```sql
CREATE TABLE hive_table (
  `id` INT,
  `name` STRING,
  `dt` STRING,
  `hr` STRING
) PARTITIONED BY (dt, hr)
with (
    'connector' = 'hive',  -- Flink 1.13 请使用 'connector' = 'hive'
    'hive-version' = '3.1.1',
    'hive-database' = 'testdb',
    'partition.time-extractor.timestamp-pattern'='$dt $hr:00:00',
    'sink.partition-commit.trigger'='partition-time',
    'sink.partition-commit.delay'='1 h',
    'sink.partition-commit.policy.kind'='metastore,success-file'
);
```


## 作业配置
在 Hive 数据库中建 Hive 表。
```sql
# 在 Hive 的 testdb 数据库创建 hive_table 数据表
USE testdb;
CREATE TABLE `hive_table` (
  `id` int,
  `name` string)
PARTITIONED BY (`dt` string, `hr` string)
STORED AS ORC;
```

对 Hive 表的 HDFS 路径开启写权限。
 - 方式一：可登录 EMR Hive 集群节点（具体可参见 [Hive 基础操作](https://cloud.tencent.com/document/product/589/12317)），对目的库 testdb 库的 hive_table 表执行 chmod 操作。
```
hdfs dfs -chmod 777 /usr/hive/warehouse/testdb.db/hive_table
```
 - 方式二：在**作业管理 > 作业参数**中添加以下高级参数，可以 hadoop 用户角色获取 HDFS 路径权限。
```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
```

>? Flink SQL 中使用 Hive 表 testdb.hive_table，这里 CREATE TABLE 的表名对应 Hive 库的表名（Flink 1.13支持通过hive-table参数配置覆盖该值），库名通过 hive-database 参数指定。


## WITH 参数

| 参数值                                     | 必填 | 默认值       | 描述                                                         |
| ------------------------------------------ | ---- | ------------ | ------------------------------------------------------------ |
| connector.type                             | 是   | 无           | Flink-1.11支持，填 'hive' 选择使用 hive connector。          |
| connector                                  | 是   | 无           | Flink-1.13支持，填 'hive' 选择使用 hive connector。          |
| hive-version                               | 是   | 无           | EMR 创建的 Hive 集群对应的版本。                             |
| hive-database                              | 是   | 无           | 数据要写入的 Hive database。                                 |
| hive-table                                 | 否   | 无           | Flink-1.13支持，填写后该值会作为Hive库的对应表名             |
| sink.partition-commit.trigger              | 否   | process-time | 分区关闭策略。可选值包括：<li/>process-time：当分区创建超过一定时间之后将这个分区关闭，分区创建时间为分区创建时的物理时间。<li/>partition-time：当分区创建超过一定时间之后将这个分区关闭，分区创建时间从分区中抽取出来。partition-time 依赖于 watermark 生成，需要配合 wartermark 才能支持自动分区发现。当 watermark 时间超过了 `从分区抽取的时间` 与 `delay 参数配置时间` 之和后会提交分区。 |
| sink.partition-commit.delay                | 否   | 0s           | 分区关闭延迟。当分区在创建超过一定时间之后将被关闭。         |
| sink.partition-commit.policy.kind          | 是   | 无           | 用于提交分区的策略。可选值可以组合使用，可选值包括：<li/>success-file：当分区关闭时将在分区对应的目录下生成一个 \_success 的文件。<li/>metastore：向 Hive Metastore 更新分区信息。<li/>custom：用户实现的自定义分区提交策略。 |
| partition.time-extractor.timestamp-pattern | 否   | 无           | 分区时间戳的抽取格式。需要写成 yyyy-MM-dd HH:mm:ss 的形式，并用 Hive 表中相应的分区字段做占位符替换。默认支持第一个字段为 yyyy-mm-dd hh:mm:ss。<li/>如果时间戳应该从单个分区字段 'dt' 提取，可以配置 '$dt'。<li/>如果时间戳应该从多个分区字段中提取，例如 'year'、'month'、'day' 和 'hour'，可以配置 '$year-$month-$day $hour:00:00'。<li/>如果时间戳应该从两个分区字段 'dt' 和 'hour' 提取，可以配置 '$dt $hour:00:00'。 |
| sink.partition-commit.policy.class         | 否   | 无           | 分区提交类，配合 sink.partition-commit.policy.kind = 'custom' 使用，类必须实现 PartitionCommitPolicy。 |
| partition.time-extractor.kind              | 否   | default      | 分区时间抽取方式。这个配置仅当 sink.partition-commit.trigger 配置为 partition-time 时生效。如果用户有自定义的分区时间抽取方法，配置为 custom。 |
| partition.time-extractor.class             | 否   | 无           | 分区时间抽取类，这个类必须实现 PartitionTimeExtractor 接口。 |


## 代码示例

```sql
CREATE TABLE datagen_source_table (
  id INT,
  name STRING,
  log_ts TIMESTAMP(3),
  WATERMARK FOR log_ts AS log_ts - INTERVAL '5' SECOND
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '10'
);

CREATE TABLE hive_table (
  `id` INT,
  `name` STRING,
  `dt` STRING,
  `hr` STRING
) PARTITIONED BY (dt, hr)
with (
    'connector' = 'hive',  -- Flink 1.13 请使用 'connector' = 'hive'
    'hive-version' = '3.1.1',
    'hive-database' = 'testdb',
    'partition.time-extractor.timestamp-pattern'='$dt $hr:00:00',
    'sink.partition-commit.trigger'='partition-time',
    'sink.partition-commit.delay'='1 h',
    'sink.partition-commit.policy.kind'='metastore,success-file'
);

-- streaming sql, insert into hive table
INSERT INTO hive_table
SELECT id, name, DATE_FORMAT(log_ts, 'yyyy-MM-dd'), DATE_FORMAT(log_ts, 'HH')
FROM datagen_source_table;
```

## Hive 配置
### 获取 Hive 连接配置 jar 包
Flink SQL 任务写 Hive 时需要使用包含 Hive 及 HDFS 配置信息的 jar 包来连接到 Hive 集群。具体获取连接配置 jar 及其使用的步骤如下：
1. ssh 登录到对应 Hive 集群节点。
2. 获取 hive-site.xml 和 hdfs-site.xml，EMR 集群中的配置文件在如下位置。
```
/usr/local/service/hive/conf/hive-site.xml
/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml
```
3. 修改 hive-site.xml 文件
```
在hive-site增加如下配置，ip的值取配置文件里 hive.server2.thrift.bind.host 的 value
<property>
    <name>hive.metastore.uris</name>
    <value>thrift://ip:7004</value>
</property>
```
4. 获取 [hivemetastore-site.xml](https://oceanus-public-1257058918.cos.ap-guangzhou.myqcloud.com/hivemetastore-site.xml) 和 [hiveserver2-site.xml](https://oceanus-public-1257058918.cos.ap-guangzhou.myqcloud.com/hiveserver2-site.xml)，点击文件名下载。
5. 对获取到的配置文件 打 jar 包。
```
jar -cvf hive-xxx.jar hive-site.xml hdfs-site.xml hivemetastore-site.xml hiveserver2-site.xml
```
6. 校验 jar 的结构（可以通过 vi 命令查看 `vi hive-xxx.jar`），jar 里面包含如下信息，请确保文件不缺失且结构正确。
```bash
META-INF/
META-INF/MANIFEST.MF
hive-site.xml
hdfs-site.xml
hivemetastore-site.xml
hiveserver2-site.xml
```

### 在任务中使用配置 jar
引用程序包中选择 Hive 连接配置 jar 包（该 jar 包为在 [获取 Hive 连接配置 jar 包](#id) 中得到的 hive-xxx.jar，必须在依赖管理上传后才使用）。

## Kerberos 认证授权
1. 登录集群 Master 节点，获取 krb5.conf、emr.keytab、core-site.xml、hdfs-site.xml、hive-site.xml 文件，路径如下。
```
/etc/krb5.conf
/var/krb5kdc/emr.keytab
/usr/local/service/hadoop/etc/hadoop/core-site.xml
/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml
/usr/local/service/hive/conf/hive-site.xml
```
2. 修改 hive-site.xml 文件。在 hive-site.xml 中增加如下配置，IP 的值取配置文件中 `hive.server2.thrift.bind.host` 的 value。
```
<property>
    <name>hive.metastore.uris</name>
    <value>thrift://ip:7004</value>
</property>
```
3. 获取 [hivemetastore-site.xml](https://oceanus-public-1257058918.cos.ap-guangzhou.myqcloud.com/hivemetastore-site.xml) 和 [hiveserver2-site.xml](https://oceanus-public-1257058918.cos.ap-guangzhou.myqcloud.com/hiveserver2-site.xml)，点击文件名下载。
4. 对获取的配置文件打 jar 包。
```
jar cvf hive-xxx.jar krb5.conf emr.keytab core-site.xml hdfs-site.xml hive-site.xml hivemetastore-site.xml hiveserver2-site.xml
```
5. 校验 jar 的结构（可以通过 vim 命令查看 vim hive-xxx.jar），jar 里面包含如下信息，请确保文件不缺失且结构正确。
```
META-INF/
META-INF/MANIFEST.MF
emr.keytab
krb5.conf
hdfs-site.xml
core-site.xml
hive-site.xml
hivemetastore-site.xml
hiveserver2-site.xml
```
6. 在 [程序包管理](https://console.cloud.tencent.com/oceanus/resource) 页面上传 jar 包，并在作业参数配置里引用该程序包。
7. 获取 kerberos principal，用于作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
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
8. 作业 [高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
security.kerberos.login.principal: hadoop/172.28.28.51@EMR-OQPO48B9
security.kerberos.login.keytab: emr.keytab
security.kerberos.login.conf: ${krb5.conf.fileName}
```

>! 历史 Oceanus 集群可能不支持该功能，您可通过 [在线客服](https://cloud.tencent.com/act/event/Online_service?from=doc_849) 联系我们升级集群管控服务，以支持 Kerberos 访问。

## 注意事项
如果 Flink 作业正常运行，日志中没有报错，但是客户端查不到这个 Hive 表，可以使用如下命令对 Hive 表进行修复（需要将 `hive_table_xxx` 替换为要修复的表名）。
```
msck repair table hive_table_xxx;
```
