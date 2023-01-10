## 版本说明

| Flink 版本 | 说明                |
| :--------- | :------------------ |
| 1.11       | 不支持              |
| 1.13       | 支持 Source 和 Sink |
| 1.14       | 不支持              |


## 使用范围
可以作为 Source/Sink 使用。其中，作为 source 使用时，不支持 upsert 写入的源 iceberg。

## DDL 定义
用作数据目的：
```sql
CREATE TABLE `sink` (
`id` bigint,
`YCSB_KEY` string,
`FIELD0` string,
`FIELD1` string,
`FIELD2` string,
`database_name` string,
`table_name` string,
`op_ts` timestamp(3),
`date` string
) PARTITIONED BY (`date`) WITH (
 'connector' = 'iceberg',
 'warehouse'='hdfs://usr/hive/warehouse',
 'write.upsert.enable'='false', -- 是否开启upsert
 'catalog-type' = 'hive',
 'catalog-name'='xxx',
 'catalog-database'='xxx',
 'catalog-table'='xxx',
 -- Hive metastore 的 thrift URI，可以从hive-site.xml配置文件中获取，对应的Key为：hive-metastore-uris
 'uri'='thrift://ip:port',

 'engine.hive.enabled' = 'true',
 'format-version' = '2'
);
```
作为数据源：
```sql
CREATE TABLE `icesource` (
`id` bigint,
`YCSB_KEY` string,
`FIELD0` string,
`FIELD1` string,
`FIELD2` string,
`database_name` string,
`table_name` string,
`op_ts` timestamp(3),
PRIMARY KEY(id) NOT ENFORCED
) WITH (
'connector' = 'iceberg',
'catalog-name' = 'hive_catalog',
'catalog-type' = 'hive',
'catalog-database' = 'database_ta',
'catalog-table' = 't_p1_hive3_avro_3',
'warehouse'='hdfs://HDFS14979/usr/hive/warehouse',
'engine.hive.enabled' = 'true',
'format-version' = '2',
'streaming'='true',
'monitor-interval'='10'
--'start-snapshot-id' = '5451179941514600634',
--'streaming' = 'false'
);
```



## WITH 参数
### 通用参数

| 参数值           | 必填 | 默认值 | 描述                                                         |
| ---------------- | ---- | ------ | ------------------------------------------------------------ |
| connector        | 是   | 无     | 必须填 iceberg                                               |
| location         | 是   | 无     | 数据的存储路径（如果存储到 HDFS，格式为 hdfs:// ；存储为 COS 为   COSN://$bucket/$path）|
| catalog-name     | 是   | 无     | 自定义的 catalog 名                                            |
| catalog-type     | 是   | 无     | catalog 类型，可选值为 hadoop / hive / custom                |
| <nobr>catalog-database | 是   | 无     | iceberg 数据库名称                                            |
| catalog-table    | 是   | 无     | iceberg 表名称                                                |
| catalog-impl     | 否   | 无     | catalog-type 为 custom时，必填                                |
| uri              | 否   | 无     | Hive metastore 的 thrift URI，可以从 hive-site.xml 配置文件中获取，对应的 Key 为：hive-metastore-uris; Eg. thrift://172.28.1.149:7004 |
| format-version   | 否   | 1      | Iceberg 格式 请参见 [Iceberg Table Spec](https://iceberg.apache.org/spec/#format-versioning) |

更多参数请参见 [Configuration](https://iceberg.apache.org/docs/latest/configuration/)。

## COS 配置
无需做额外配置，path 填写为对应的 cosn 路径即可。

## HDFS 配置
### 获取 HDFS 链接配置 jar
Flink SQL 任务写 Hudi，使用 HDFS 存储时需要使用包含 HDFS 配置信息的 jar 包来连接到 HDFS 集群。具体获取连接配置 jar 及其使用的步骤如下：
1. ssh 登录到对应 HDFS 集群节点。
2. 获取 hdfs-site.xml，EMR 集群中的配置文件在如下位置。 							 						
```
/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml
```
3. 对获取到的配置文件 打 jar 包。
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

### 配置写入 hdfs 的用户
>? Flink 作业默认以 flink 用户操作 HDFS，若没有 HDFS 路径的写入权限，可通过 [作业高级参数](https://cloud.tencent.com/document/product/849/53391) 设置为有权限的用户，或者设置为超级用户 hadoop。
>
```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
```

## Kerberos 认证授权

1. 登录集群 Master 节点，获取 krb5.conf、emr.keytab、core-site.xml、hdfs-site.xml 文件，路径如下：
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

6.  [作业高级参数](https://cloud.tencent.com/document/product/849/53391) 配置。
```
containerized.taskmanager.env.HADOOP_USER_NAME: hadoop
containerized.master.env.HADOOP_USER_NAME: hadoop
security.kerberos.login.principal: hadoop/172.28.28.51@EMR-OQPO48B9
security.kerberos.login.keytab: emr.keytab
security.kerberos.login.conf: krb5.conf.path
```

