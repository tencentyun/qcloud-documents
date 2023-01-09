## 版本说明

| Flink 版本 | 说明                |
| :--------- | :------------------ |
| 1.11       | 不支持              |
| 1.13       | 支持 Source 和 Sink |
| 1.14       | 不支持              |


## 使用范围
可以作为 Source/Sink 使用。



## DDL 定义
用作数据目的：
```sql
CREATE TABLE hudi_sink
(
    uuid        VARCHAR(20) PRIMARY KEY NOT ENFORCED,
    name        VARCHAR(10),
    age         INT,
    ts          TIMESTAMP(3),
    `partition` VARCHAR(20)
) WITH (
    'connector' = 'hudi'
    , 'path' = 'hdfs://HDFS1000/data/hudi/mor'
    , 'table.type' = 'MERGE_ON_READ'  --  MERGE_ON_READ 表, 默认值为 COPY_ON_WRITE
    , 'write.tasks' = '3' -- 默认为4
    , 'compaction.tasks' = '4' -- 默认为4
    --  , 'hive_sync.enable' = 'true'  -- 默认值为false
    --  , 'hive_sync.db' = 'default'
    --  , 'hive_sync.table' = 'datagen_mor_1'
    --  , 'hive_sync.mode' = 'jdbc'
    --  , 'hive_sync.username' = ''
    --  , 'hive_sync.password' = ''
    --  , 'hive_sync.jdbc_url' = 'jdbc:hive2://172.28.1.185:7001'
    --  , 'hive_sync.metastore.uris' = 'thrift://172.28.1.185:7004'
);

```

作为数据源：
```sql
CREATE TABLE `source`
(
    uuid        VARCHAR(20) PRIMARY KEY NOT ENFORCED,
    name        VARCHAR(10),
    age         INT,
    ts          TIMESTAMP(3),
    `partition` VARCHAR(20)
) WITH (
      'connector' = 'hudi'
      , 'path' = 'hdfs://172.28.28.202:4007/path/hudidata'
      , 'table.type' = 'MERGE_ON_READ'  -- MOR 表, 目前无法读取增量数据
      , 'read.tasks' = '1'  -- 读task的并行度,默认值为4
      , 'hoodie.datasource.query.type' = 'snapshot' -- 默认值为snapshot, 可选值为 read_optimized, incremental
      , 'read.streaming.enabled' = 'true'  -- this option enable the streaming read
      , 'read.start-commit' = 'earliest' -- specifies the start commit instant time, the commit time format should be 'yyyyMMddHHmmss'
      , 'read.streaming.check-interval' = '4'
      );
```


## WITH 参数
### 通用参数

| 参数值    | 必填 | 默认值 | 描述                                                         |
| --------- | ---- | ------ | ------------------------------------------------------------ |
| connector | 是   | 无     | 必须填 hudi                                                  |
| path      | 是   | 无     | 数据的存储路径（如果存储到 HDFS，格式为 hdfs://；存储为 COS 为  COSN://$bucket/$path） |

### 作为 Sink 的参数

| 参数值     | 必填 | 默认值        | 描述                                                   |
| ---------- | ---- | ------------- | ------------------------------------------------------ |
| table.type | 否   | COPY_ON_WRITE | Hudi 表类型，可选值为 COPY_ON_WRITE 或者 MERGE_ON_READ |

#### HoodieRecord 字段相关

| 参数值                                      | 必填 | 默认值 | 描述                                                         |
| ------------------------------------------- | ---- | ------ | ------------------------------------------------------------ |
| hoodie.datasource.write.recordkey.field     | 否   | uuid   | key 字段，flink table 如果有 primary key，则采用 flink table 的 pk|
| hoodie.datasource.write.partitionpath.field | 否   | ""     | 分区路径字段，为空表示不分区          |
| write.precombine.field                      | 否   | ts     | 预合并时，相同 key 记录时候，用于比较(Object.compareTo(..))的字段 |

#### 并行度相关

| 参数值                      | 必填 | 默认值 | 描述                                        |
| --------------------------- | ---- | ------ | ------------------------------------------- |
| write.tasks                 | 否   | 4      | 写算子的并行度                              |
| write.index_bootstrap.tasks | 否   | 无     | index bootstrap 的并行度，默认为作业的并行度 |
| write.bucket_assign.tasks   | 否   | 无     | bucket assign 的并行度，默认为作业的并行度 |
| compaction.tasks            | 否   | 4      | compaction 任务的并行度                      |

#### compaction相关

| 参数值                      | 必填 | 默认值      | 描述                                                    |
| --------------------------- | ---- | ----------- | ------------------------------------------------------- |
| compaction.schedule.enabled | 否   | true        | 是否启动 compaction                                     |
| compaction.async.enabled    | 否   | true        | compaction 是否采用异步                                 |
| compaction.trigger.strategy | 否   | num_commits | num_commits / time_elapsed / num_and_time / num_or_time |

#### hive 元数据同步相关

| 参数值             | 必填 | 默认值 | 描述                        |
| ------------------ | ---- | ------ | --------------------------- |
| hive_sync.enable   | 否   | false  |           -                  |
| hive_sync.db       | 否   |    -    |                      -       |
| hive_sync.table    | 否   |    -    |         -                    |
| hive_sync.mode     | 否   | jdbc   | 可选值 hms，jdbc and hiveql |
| hive_sync.username | 否   | -       |          -                   |
| hive_sync.password | 否   |   -     |          -                   |
| hive_sync.jdbc_url | 否   |     -   |            -                 |

#### 更多参数
其他更详细的参数，可参见 [Flink Options]( https://hudi.apache.org/docs/0.10.1/configurations#Flink-Options)。



### 作为 Source 的参数

| 参数值                         | 必填 | 默认值   | 描述                                                         |
| ------------------------------ | ---- | -------- | ------------------------------------------------------------ |
| read.tasks                     | 否   | 4        | 读算子的并行度                                               |
| hoodie.datasource.query.type   | 否   | snapshot | 可选值 snapshot / read_optimized / incremental               |
| read.streaming.enabled         | 否   | false    |                     -                                         |
| read.streaming.check-interval  | 否   | 60       | 单位秒，streaming read的检查时间间隔                        |
| read.streaming.skip_compaction | 否   | false    |           -                                                   |
| read.start-commit              | 否   | 无       | 格式为 yyyyMMddHHmmss；可设置为 earliest，表示从最早的 commit 开始消费 |
| read.end-commit                | 否   | 无       | streaming read，无需设置该值                                  |



### 更详细的参数配置
可参见 [Flink Options](https://hudi.apache.org/docs/0.10.1/configurations/#FLINK_SQL)。



## COS 配置
无需做额外配置。path 填写为对应的 cosn 路径即可。


## HDFS 配置
### 获取 HDFS 链接配置 jar
Flink SQL 任务写 Hudi , 使用 HDFS 存储时需要使用包含 HDFS 配置信息的 jar 包来连接到 HDFS 集群。具体获取连接配置 jar 及其使用的步骤如下：
1. ssh 登录到对应 HDFS 集群节点。
2. 获取 hdfs-site.xml，EMR 集群中的配置文件在如下位置。 							 						
```
/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml
```
3. 对获取到的配置文件打 jar 包。
```bash
jar -cvf hdfs-xxx.jar hdfs-site.xml
```
4. 校验 jar 的结构（可以通过 vi 命令查看 ），jar 里面包含如下信息，请确保文件不缺失且结构正确。
```
vi hdfs-xxx.jar
```
```bash
META-INF/
META-INF/MANIFEST.MF
hdfs-site.xml
```

### 配置写入 HDFS 的用户

>? Flink 作业默认以 flink 用户操作 HDFS，若没有 HDFS 路径的写入权限，可通过 [作业高级参数](https://cloud.tencent.com/document/product/849/53391) 设置为有权限的用户，或者设置为超级用户 hadoop。
>
 ```
 containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
```

## Kerberos 认证授权
1. 登录集群 Master 节点，获取 krb5.conf、emr.keytab、core-site.xml、hdfs-site.xml 文件，路径如下。
```
/etc/krb5.conf
/var/krb5kdc/emr.keytab
/usr/local/service/hadoop/etc/hadoop/core-site.xml
/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml
```

2. 对获取的配置文件打 jar 包。					 							 							 					
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

5. 获取 kerberos principal，用于 [作业高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
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
   
6.  [作业高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。 							 							```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
security.kerberos.login.principal: hadoop/172.28.28.51@EMR-OQPO48B9
security.kerberos.login.keytab: emr.keytab
security.kerberos.login.conf: krb5.conf.path
```

## 常见问题
### hive sync
hive 表同步失败，报错。
```
java.lang.ClassNotFoundException: org.apache.hudi.hadoop.HoodieParquetInputFormat
```

请确认对应的 hive 环境,是否包含 Hudi 需要的 jar 包，详情请参见 [Hive](https://hudi.apache.org/docs/0.10.1/query_engine_setup#hive)。

hudi-hadoop-mr-bundle-x.y.z.jar [下载链接](https://repo1.maven.org/maven2/org/apache/hudi/hudi-hadoop-mr-bundle/0.10.1/)。
