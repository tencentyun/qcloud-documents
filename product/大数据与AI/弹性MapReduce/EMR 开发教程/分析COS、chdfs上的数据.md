本节将基于腾讯云对象存储 COS 展示 Impala 更多使用方法，数据来源于直接插入数据、COS 数据。

## 开发准备
1. 由于任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中先 [创建一个存储桶（Bucket）](https://cloud.tencent.com/document/product/436/13309)。
2. 确认您已开通腾讯云，且已创建一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Impala 组件，并且在基础配置页面开启对象存储的授权。
3. Impala 等相关软件安装在路径 EMR 云服务器的 `/usr/local/service/` 路径下。

## 操作步骤
登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，可选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并连接到 impala：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]$ impala-shel.sh -i $host:27001
```
$host 为您的 impala 数据节点所在的内网 IP。

### 步骤一：创建表（record）
```
[$host:27001 ] > create table record(id int, name string) row format delimited fields terminated by ',' stored as textfile location 'cosn://$bucketname/';
Query: create table record(id int, name string) row format delimited fields terminated by ',' stored as textfile location 'cosn://$bucketname/'
Fetched 0 row(s) in 3.07s
其中 $bucketname 为您的 COS 存储桶名加路径，如果使用 CHDFS 将 location 的值换成 ofs://$mountname/，$mountname 为您的 CHDFS 挂在地址加路径
查看表信息，确认 location 是 cos 路径
[$host:27001 ] > show create table record2;
Query: show create table record2
+----------------------------------------------------------------------+
| result                                                               |
+----------------------------------------------------------------------+
| CREATE TABLE default.record2 (                                       |
|   id INT,                                                            |
|   name STRING                                                        |
| )                                                                    |
| ROW FORMAT DELIMITED FIELDS TERMINATED BY ','                        |
| WITH SERDEPROPERTIES ('field.delim'=',', 'serialization.format'=',') |
| STORED AS TEXTFILE                                                   |
| LOCATION 'cosn://$bucketname'                                 |
| TBLPROPERTIES ('numFiles'='19', 'totalSize'='1870')                  |
+----------------------------------------------------------------------+
Fetched 1 row(s) in 5.90s
```

### 步骤二：向表中插入数据
```
[$host:27001] > insert into record values(1,"test");
Query: insert into record values(1,"test")
Query submitted at: 2020-08-03 11:29:16 (Coordinator: http://$host:27004)
Query progress can be monitored at: http:/$host:27004/query_plan?query_id=b246d3194efb7a8f:bc60721600000000
Modified 1 row(s) in 0.64s
```

### 步骤三：使用 impala 查询表
```
[$host:27001] > select * from record;
Query: select * from record
Query submitted at: 2020-08-03 11:29:31 (Coordinator: http://172.30.1.136:27004)
Query progress can be monitored at: http://$host:27004/query_plan?query_id=8148da96f8c0d369:4b26432a00000000
+----+---------+
| id | name    |
+----+---------+
| 1  | test    |
+----+---------+
Fetched 1 row(s) in 0.37s
```
