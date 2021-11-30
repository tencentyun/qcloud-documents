本文介绍了使用腾讯云 Sqoop 服务将数据在 MySQL 和 Hive 之间相互导入导出的方法。

## 1. 开发准备
- 确认已开通腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Sqoop、Hive 组件。 
- Sqoop 等相关软件安装在路径 EMR 云服务器的`/usr/local/service/`路径下。

## 2. 将关系型数据库导入到 Hive 中
本节将继续使用上一节的用例。

进入 [弹性 MapReduce 控制台](https://console.cloud.tencent.com/emr)，复制目标集群的实例 ID，即集群的名字。再进入关系型数据库控制台，使用 Ctrl+F 进行搜索，找到集群对应的 MySQL 数据库，查看该数据库的内网地址 $mysqlIP。

登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Hive 文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]# cd /usr/local/service/hive
```
新建一个 Hive 数据库：
```
[hadoop@172 hive]$ hive
hive> create database hive_from_sqoop;
OK
Time taken: 0.167 seconds
```
使用 sqoop-import 命令把上一节中创建的 MySQL 数据库导入到 Hive 中：
```
[hadoop@172 hive]# cd /usr/local/service/sqoop
[hadoop@172 sqoop]$ bin/sqoop-import --connect  jdbc:mysql://$mysqlIP/test --username 
root -P --table sqoop_test_back --hive-database hive_from_sqoop --hive-import --hive-table hive_from_sqoop
```
- $mysqlIP：腾讯云关系型数据库（CDB）的内网地址。
- test：MySQL 数据库名称。
- --table：要导出的 MySQL 表名。
- --hive-database：Hive 数据库名。
- --hive-table：导入的 Hive 表名。

执行指令需要输入您的 MySQL 密码，默认为您创建 EMR 集群时设置的密码。执行成功后，可以在 Hive 中查看导入的数据库：
```
hive> select * from hive_from_sqoop;
OK
1	first	2018-07-03 16:07:46.0	spark
2	second	2018-07-03 15:30:57.0	mr
3	third	2018-07-03 15:31:07.0	yarn
4	forth	2018-07-03 15:39:38.0	hbase
5	fifth	2018-07-03 16:02:29.0	hive
6	sixth	2018-07-03 16:09:58.0	sqoop
Time taken: 1.245 seconds, Fetched: 6 row(s)
```

## 3. 将 Hive 导入到关系型数据库中
Sqoop 支持将 Hive 表中的数据导入到关系型数据库中。先在 Hive 中创建新表并导入数据。

登录 EMR 集群中的任意机器，最好是登录到 Master 节点。在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Hive 文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]# cd /usr/local/service/hive
```
新建一个 bash 脚本文件 gen_data.sh，在其中添加以下代码：
```
#!/bin/bash
MAXROW=1000000 #指定生成数据行数
for((i = 0; i < $MAXROW; i++))
do
　　　echo $RANDOM, \"$RANDOM\"
done
```
并按如下方式执行：
```
[hadoop@172 hive]$ ./gen_data.sh > hive_test.data
```
这个脚本文件会生成1,000,000个随机数对，并且保存到文件 hive_test.data 中。

使用如下指令把生成的测试数据先上传到 HDFS 中：
```
[hadoop@172 hive]$ hdfs dfs -put ./hive_test.data /$hdfspath
```
其中 $hdfspath 为 HDFS 上的您存放文件的路径。

连接 Hive 并创建测试表：
```
[hadoop@172 hive]$ bin/hive
hive> create database hive_to_sqoop;          #创建数据库 hive_to_sqoop
OK
Time taken: 0.176 seconds
hive> use hive_to_sqoop;                            #切换数据库
OK
Time taken: 0.176 seconds
hive> create table hive_test (a int, b string)
hive> ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
　　　　　　　　　　　　　　　　#创建数据表 hive_test, 并指定列分割符为’,’
OK
Time taken: 0.204 seconds
hive> load data inpath "/$hdfspath/hive_test.data" into table hive_test;   #导入数据
```
$hdfspath 为 HDFS 上的您存放文件的路径。

成功后可使用`quit`命令退出 Hive 数据仓库。连接关系型数据库并创建对应的表格：
```
[hadoop@172 hive]$ mysql -h $mysqlIP –p
Enter password:
```
其中 $mysqlIP 为该数据库的内网地址，密码为您创建集群时设置的密码。

在 MySQL 中创建一个名为 test 的表格，**MySQL 中的表字段名字和 Hive 中的表字段名字必须完全一致**：
```
mysql> create table table_from_hive (a int,b varchar(255));
```
成功创建表格后即可退出 MySQL。

使用 Sqoop 把 Hive 数据仓库中的数据导入到关系型数据库中有两种方法，可以直接使用 HDFS 存储的 Hive 数据，也可以使用 Hcatalog 来进行数据的导入。

### 使用 HDFS 中的 Hive 数据
切换进入 Sqoop 文件夹，然后使用以下指令把 Hive 数据库中的数据导出到关系型数据库中：
```
[hadoop@172 hive]$ cd  ../sqoop/bin
[hadoop@172 bin]$ ./sqoop-export --connect jdbc:mysql://$mysqlIP/test --username root -P 
--table table_from_hive --export-dir /usr/hive/warehouse/hive_to_sqoop.db/hive_test
```
其中 $mysqlIP 为您的关系型数据库的内网 IP 地址，test 为关系型数据库中的数据库名，--table 后跟的参数为您的关系型数据库的表名，--export-dir 后跟的参数为 Hive 表中的数据在 HDFS 中存储的位置。

### 使用 Hcatalog 进行导入
切换进入 Sqoop 文件夹，然后使用以下指令把 Hive 数据库中的数据导出到关系型数据库中：
```
[hadoop@172 hive]$ cd  ../sqoop/bin
[hadoop@172 bin]$ ./sqoop-export --connect jdbc:mysql://$mysqlIP/test --username root -P 
--table table_from_hive --hcatalog-database hive_to_sqoop --hcatalog-table hive_test
```
其中 $mysqlIP 为您的关系型数据库的内网 IP 地址，test 为关系型数据库中的数据库名，--table 后跟的参数为您的关系型数据库的表名，--hcatalog-database 后面跟的参数是要导出的 Hive 表所在的数据库的名称，--hcatalog-table 后面跟的参数是要 Hive 中要导出的表的名称。

操作完成后可以进入关系型数据库查看是否导入成功：
```
[hadoop@172 hive]$ mysql -h $mysqlIP –p                  #连接 MySQL
Enter password:
mysql> use test;
Database changed
mysql> select count(*) from table_from_hive;     #现在表中有1000000条数据
+----------+
| count(*) |
+----------+
| 1000000 |
+----------+
1 row in set (0.03 sec)
mysql> select * from table_from_hive limit 10;    #查看表中前10条记录
+-------+----------+
| a     | b        |
+-------+----------+
| 28523 |  "3394"  |
| 31065 |  "24583" |
|   399 |  "23629" |
| 18779 |  "8377"  |
| 25376 |  "30798" |
| 20234 |  "22048" |
| 30744 |  "32753" |
| 21423 |  "6117"  |
| 26867 |  "16787" |
| 18526 |  "5856"  |
+-------+----------+
10 rows in set (0.00 sec)
```
更多关于 sqoop-export 命令的参数可以通过如下命令查看：
```
[hadoop@172 bin]$ ./sqoop-export --help
```

## 4. 将 orc 格式的 Hive 表格导入到关系型数据库中
orc 是按列存储的一种文件存储格式，使用该格式能够极大的提升 Hive 的性能。本节介绍了如何创建一个 orc 格式的表并载入数据，然后使用腾讯云 Sqoop 服务把 Hive 中以 orc 格式进行存储的数据导出到关系型数据库。
>!将 orc 存储格式的 Hive 表格导入到关系型数据库中不能直接使用 HDFS 中存储的数据，只能使用 Hcatalog 进行操作。

本节将继续使用上一节的用例。

登录 EMR 集群的 Master 节点后，在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Hive 文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]# cd /usr/local/service/hive
```
在上一节中创建的 hive_from_sqoop 数据库中创建一个新表格：
```
[hadoop@172 hive]$ hive
hive> use hive_to_sqoop;
OK
Time taken: 0.013 seconds
hive> create table if not exists orc_test(a int,b string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' stored as orc;
```
可以通过如下指令来查看表格中数据的存储格式：	
```
hive> show create table orc_test;
OK
CREATE TABLE `orc_test`(
  `a` int,
  `b` string)
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.orc.OrcSerde'
WITH SERDEPROPERTIES (
  'field.delim'=',',
  'serialization.format'=',')
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'
LOCATION
  'hdfs://HDFS2789/usr/hive/warehouse/hive_to_sqoop.db/orc_test'
TBLPROPERTIES (
  'COLUMN_STATS_ACCURATE'='{\"BASIC_STATS\":\"true\"}',
  'numFiles'='0',
  'numRows'='0',
  'rawDataSize'='0',
  'totalSize'='0',
  'transient_lastDdlTime'='1533563293')
Time taken: 0.041 seconds, Fetched: 21 row(s)
```
由返回的数据可以看出该表格中的数据存储格式为 orc。

有多种方式可以向 orc 格式的 Hive 表格导入数据，下面主要介绍通过创建临时的存储格式为 text 的 Hive 表格来向 orc 存储格式的表格导入数据，这里我们使用上一节中创建的 hive_test 表格作为临时表格，使用以下指令来导入数据： 
```
hive> insert into table orc_test select * from hive_test;
```
导入成功后可通过`select`指令查看表格中的数据。

然后使用 Sqoop 把 orc 格式的 Hive 表格导出到 MySQL中。连接关系型数据库并创建对应的表格，连接关系型数据库的具体方式见上文：
```
[hadoop@172 hive]$ mysql -h $mysqlIP –p
Enter password:
```
其中 $mysqlIP 为该数据库的内网地址，密码为您创建集群时设置的密码。

在 MySQL 中创建一个名为 test 的表格，**MySQL 中的表字段名字和 Hive 中的表字段名字必须完全一致**：
```
mysql> create table table_from_orc (a int,b varchar(255));
```
成功创建表格后即可退出 MySQL。

切换进入 Sqoop 文件夹，然后使用以下指令把 Hive 数据库中以 orc 格式存储的数据导出到关系型数据库中：
```
[hadoop@172 hive]$ cd  ../sqoop/bin
[hadoop@172 bin]$ ./sqoop-export --connect jdbc:mysql://$mysqlIP/test --username root -P 
--table table_from_orc --hcatalog-database hive_to_sqoop --hcatalog-table orc_test
```
其中 $mysqlIP 为您的关系型数据库的内网 IP 地址，test 为关系型数据库中的数据库名，--table 后跟的参数为您的关系型数据库的表名，--hcatalog-database 后面跟的参数是要导出的 Hive 表所在的数据库的名称，--hcatalog-table 后面跟的参数是要 Hive 中要导出的表的名称。

导入成功后可以在 MySQL 中查看相应表中的数据：
```
mysql> select count(*) from table_from_orc;
+----------+
| count(*) |
+----------+
| 1000000 |
+----------+
1 row in set (0.24 sec)
mysql> select * from table_from_orc limit 10;
+-------+----------+
| a     | b        |
+-------+----------+
| 28523 |  "3394"  |
| 31065 |  "24583" |
|   399 |  "23629" |
| 18779 |  "8377"  |
| 25376 |  "30798" |
| 20234 |  "22048" |
| 30744 |  "32753" |
| 21423 |  "6117"  |
| 26867 |  "16787" |
| 18526 |  "5856"  |
+-------+----------+
10 rows in set (0.00 sec)
```

更多的 Sqoop 操作可以查看 [官方文档](http://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html)。
