## 介绍
Hive Sink Connector 提供了对 Hive 的写入支持。当前支持的 Hive 版本有1.1.0、2.3.2、2.3.5和3.1.1版本。

## 使用范围
Hive connector 支持数据流的目的表（Sink），不支持 Upsert 数据流。支持 Text、SequenceFile、ORC、Parquet 格式的写入。

## 示例
#### 用作数据目的（Sink）
1. 需要在 Hive 数据库里建 Hive 表。
```SQL
# 在 Hive 的 testdb 数据库创建 test_sink 数据表
# 具体语法可以参考 Hive 的相关文档，这里不再赘述
USE testdb;
CREATE TABLE `test_sink` (
			`name` string,
			`age` int)
PARTITIONED BY (`dt` string, `hr` string)
STORED AS ORC;
```
2. 对 Hive 表的 HDFS 路径开启写权限。
 - 方式一：可登录 EMR Hive 集群节点（具体可参见 [Hive 基础操作](https://cloud.tencent.com/document/product/589/12317)），对目的库 testdb 库的 test_sink 表执行 chmod 操作。
```
hdfs dfs -chmod 777 /usr/hive/warehouse/testdb.db/test_sink
```
 - 方式二：在【作业管理】>【作业参数】中添加以下高级参数，可以 hadoop 用户角色获取 HDFS 路径权限。
```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
```
3. Flink SQL 使用，建表语法请参考 [CREATE TABLE](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/dev/table/sql/create.html#create-table)。
```SQL
# Flink SQL 中使用 Hive 表 testdb.test_sink, 这里的 CREATE TABLE 的表名对应 Hive 库的表名，库名通过 hive-database 参数指定
CREATE TABLE test_sink (
			name STRING,
			age INT,
			dt STRING,
			hr STRING
) PARTITIONED BY (dt, hr)
with (
			'connector.type' = 'hive',
			'hive-version' = '3.1.1',
			'hive-database' = 'testdb',
			'partition.time-extractor.timestamp-pattern'='$dt $hr:00:00',
			'sink.partition-commit.trigger'='partition-time',
			'sink.partition-commit.delay'='1 h',
			'sink.partition-commit.policy.kind'='metastore,success-file'
);
```

## 通用 WITH 参数

| 参数值                                     | 必填 | 默认值       | 描述                                                         |
| ------------------------------------------ | ---- | ------------ | ------------------------------------------------------------ |
| connector.type                             | 是   | 无           | 填 'hive' 选择使用 hive connector。                          |
| hive-version                               | 是   | 无           | EMR 创建的 Hive 集群对应的版本。                             |
| hive-database                              | 是   | 无           | 数据要写入的 Hive database。                                 |
| sink.partition-commit.trigger              | 否   | process-time | 分区关闭策略。可选值包括：<li/>process-time：当分区创建超过一定时间之后将这个分区关闭，分区创建时间为分区创建时的物理时间。<li/>partition-time：当分区创建超过一定时间之后将这个分区关闭，分区创建时间从分区中抽取出来。partition-time 依赖于 watermark 生成，需要配合 wartermark 才能支持自动分区发现。当 watermark 时间超过了 `从分区抽取的时间` 与 `delay 参数配置时间` 之和后会提交分区。 |
| sink.partition-commit.delay                | 否   | 0s           | 分区关闭延迟。当分区在创建超过一定时间之后将被关闭。         |
| sink.partition-commit.policy.kind          | 是   | 无           | 用于提交分区的策略。可选值可以组合使用，可选值包括：<li/>success-file：当分区关闭时将在分区对应的目录下生成一个 \_success 的文件。<li/>metastore：向 Hive Metastore 更新分区信息。<li/>custom：用户实现的自定义分区提交策略。 |
| partition.time-extractor.timestamp-pattern | 否   | 无           | 分区时间戳的抽取格式。需要写成 yyyy-MM-dd HH:mm:ss 的形式，并用 Hive 表中相应的分区字段做占位符替换。默认支持第一个字段为 yyyy-mm-dd hh:mm:ss。<li/>如果时间戳应该从单个分区字段 'dt' 提取，可以配置 '$dt'。<li/>如果时间戳应该从多个分区字段中提取，例如 'year'、'month'、'day' 和 'hour'，可以配置 '$year-$month-$day $hour:00:00'。<li/>如果时间戳应该从两个分区字段 'dt' 和 'hour' 提取，可以配置 '$dt $hour:00:00'。 |
| sink.partition-commit.policy.class         | 否   | 无           | 分区提交类，配合 sink.partition-commit.policy.kind = 'custom' 使用，类必须实现 PartitionCommitPolicy。 |
| partition.time-extractor.kind              | 否   | default      | 分区时间抽取方式。这个配置仅当 sink.partition-commit.trigger 配置为 partition-time 时生效。如果用户有自定义的分区时间抽取方法，配置为 custom。 |
| partition.time-extractor.class             | 否   | 无           | 分区时间抽取类，这个类必须实现 PartitionTimeExtractor 接口。 |

## Hive 配置
### 获取 Hive 连接配置 jar 包
Flink SQL 任务写 Hive 时需要使用包含 Hive 及 HDFS 配置信息的 jar 包来连接到 Hive 集群。具体获取连接配置 jar 及其使用的步骤如下：
1. ssh 登录到对应 Hive 集群节点。
2. 获取 hive-site.xml 和 hdfs-site.xml，EMR 集群中的配置文件在如下位置。
```
/usr/local/service/hive/conf/hive-site.xml
/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml
```
3. 对步骤2中获取到的 hive-site.xml 和 hdfs-site.xml 打 jar 包。
```
jar -cvf hive-xxx.jar hive-site.xml hdfs-site.xml
```
4. 校验 jar 的结构（可以通过 vi 命令查看 `vi hive-xxx.jar`），jar 里面包含如下信息，请确保文件不缺失且结构正确。
```bash
META-INF/
META-INF/MANIFEST.MF
hive-site.xml
hdfs-site.xml
```

### 在任务中使用配置 jar
Flink SQL 任务作业参数中选择：
1. 内置 Connector flink-connector-hive-${version}.jar，其中 version 为 Hive 对应的版本。
2. 引用程序包里面选择 Hive 连接配置 jar 包。（该 jar 包为通过“获取 Hive 连接配置 jar 包”步骤制作出来的 hive-xxx.jar，然后在程序包管理上传后可使用）。

>! 请确保您使用的 Hive connector 和 Hive 集群是同一个版本。

### 注意事项
若分区不可见，发现分区信息，参考命令：`msck repair table hive_table_xxx;`
