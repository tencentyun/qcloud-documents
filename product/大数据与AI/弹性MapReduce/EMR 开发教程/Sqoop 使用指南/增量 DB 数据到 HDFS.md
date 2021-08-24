Sqoop 是一款开源的工具，主要用于在 Hadoop 和传统数据库（MySQL、PostgreSQL 等）之间进行数据传递，可以将一个关系型数据库（例如 MySQL、Oracle、Postgres 等）中的数据导入到 Hadoop 的 HDFS 中，也可以将 HDFS 的数据导入到关系型数据库中。Sqoop 中一大亮点就是可以通过 Hadoop 的 MapReduce 把数据从关系型数据库中导入数据到 HDFS。

本文介绍了 Sqoop 的增量导入操作，即在数据库中的数据增加或更新后，把数据库的改动同步到导入 HDFS 的数据中。其中分为 append 模式和 lastmodified 模式，append 模式只能用在数据库的数据增加但不更新的场景，lastmodified 模式用在数据增加并且更新的场景。

## 1. 开发准备
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Sqoop 组件。 
- Sqoop 等相关软件安装在路径 EMR 云服务器的 `/usr/local/service/` 路径下。

## 2. 使用 append 模式 
本节将继续使用上一节的用例。

进入 [EMR 控制台](https://console.cloud.tencent.com/emr)，复制目标集群的实例 ID，即集群的名字。再进入关系型数据库控制台，使用 Ctrl+F 进行搜索，找到集群对应的 MySQL 数据库，查看该数据库的内网地址 $mysqlIP。

登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Sqoop 文件夹：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]# cd /usr/local/service/sqoop
```
连接 MySQL 数据库：
```
[hadoop@172 sqoop]$ mysql -h $mysqlIP –p
Enter password:
```
密码为您创建 EMR 集群的时候设置的密码。
连接了 MySQL 数据库之后，在表 sqoop_test 中新增一条数据，如下：
```
mysql> use test;
Database changed

mysql> insert into sqoop_test values(null, 'forth', now(), 'hbase');
Query ok, 1 row affected(0.00 sec)
```
查看表中的数据：
```
Mysql> select * from sqoop_test;
+----+--------+---------------------+---------+
| id | title  | time                | content |
+----+--------+---------------------+---------+
|  1 | first  | 2018-07-03 15:29:37 | hdfs    |
|  2 | second | 2018-07-03 15:30:57 | mr      |
|  3 | third  | 2018-07-03 15:31:07 | yarn    |
|  4 | forth  | 2018-07-03 15:39:38  | hbase    |
+----+--------+---------------------+---------+
4 rows in set (0.00 sec)
```
使用 append 模式将新增的数据同步到上一节中储存数据的 HDFS 路径中：
```
[hadoop@172 sqoop]$ bin/sqoop-import --connect jdbc:mysql://$mysqlIP/test --username 
root -P --table sqoop_test --check-column id  --incremental append --last-value 3 --target-dir 
/sqoop
```
其中 $mysqlIP 为您的 MySQL 数据库的内网地址。

执行命令会需要您输入数据库的密码，默认为您创建 EMR 集群时设置的密码。比普通的 sqoop-import 命令多出一些参数，其中 --check-column 为导入时参照的数据，--incremental 为导入的模式，在此例中为 append，--last-value 为参考数据的参考值，比该值更新的数据都会导入到 HDFS 中。

执行成功后，可以查看 HDFS 相应目录下更新后的数据：
```
[hadoop@172 sqoop]$ hadoop fs -cat /sqoop/*
1, first, 2018-07-03 15:29:37.0,hdfs
2, second, 2018-07-03 15:30:57.0,mr
3, third, 2018-07-03 15:31:07.0,yarn
4,forth,2018-07-03 15:39:38.0,hbase
```

### 使用 Sqoop job
使用 append 同步 HDFS 中的数据每次需要手动输入 --last-value，也可以使用 sqoop job 的方式，Sqoop 会自动保存上次导入成功的 last-value 值。如果要使用 sqoop job。需要启动 sqoop-metastore 进程，操作步骤如下：

首先在 conf/sqoop-site.xml 中启动 sqoop-metastore 进程：
```
<property>
  <name>sqoop.metastore.client.enable.autoconnect</name>
  <value>true</value>
</property>
```
然后在 bin 目录下启动 sqoop-metastore 服务：
```
./sqoop-metastore &
```

使用如下指令创建 Sqoop job：
>?此命令适用于 Sqoop 1.4.6 版本。

```
[hadoop@172 sqoop]$ bin/sqoop job --create job1 -- import --connect
jdbc:mysql://$mysqlIP/test --username root -P --table sqoop_test --check-column id 
--incremental append --last-value 4 --target-dir /sqoop
```
其中 $mysqlIP 为您的 MySQL 的内网地址。使用该命令就成功创建了一个 Sqoop job，每一次执行，会自动从上次更新的 last-value 值自动更新。

为 MySQL 中的 sqoop_test 表格新增一条记录：
```
mysql> insert into sqoop_test values(null, 'fifth', now(), 'hive');
Query ok, 1 row affected(0.00 sec)

Mysql> select * from sqoop_test;
+----+--------+---------------------+---------+
| id | title  | time                | content |
+----+--------+---------------------+---------+
|  1 | first  | 2018-07-03 15:29:37 | hdfs    |
|  2 | second | 2018-07-03 15:30:57 | mr      |
|  3 | third  | 2018-07-03 15:31:07 | yarn    |
|  4 | forth  | 2018-07-03 15:39:38  | hbase    |
|  5 | fifth  | 2018-07-03 16:02:29   | hive    |
+----+--------+---------------------+---------+
5 rows in set (0.00 sec)
```
然后执行 Sqoop job：
```
[hadoop@172 sqoop]$ bin/sqoop job --exec job1
```
执行该命令会让您输入 MySQL 的密码。执行成功后，可以查看 HDFS 相应目录下更新后的数据：
```
[hadoop@172 sqoop]$ hadoop fs -cat /sqoop/*
1, first, 2018-07-03 15:29:37.0,hdfs
2, second, 2018-07-03 15:30:57.0,mr
3, third, 2018-07-03 15:31:07.0,yarn
4,forth,2018-07-03 15:39:38.0,hbase
5,fifth,2018-07-03 16:02:29.0,hive
```

## 3. 使用 lastmodified 模式
直接创建一个 sqoop-import 的 lastmodified 模式的 Sqoop job，首先查询 sqoop_test 中最后更新的时间：
```
mysql> select max(time) from sqoop_test;
```
创建一个 Sqoop job：
```
[hadoop@172 sqoop]$ bin/sqoop job --create job2 -- import --connect jdbc:mysql://$mysqlIP/test --username root -P --table sqoop_test --check-column time --incremental lastmodified --merge-key id --last-value '2018-07-03 16:02:29' --target-dir /sqoop
```
**参数说明：**
- $mysqlIP 为您的 MySQL 的内网地址。
- --check-column 必须使用 timestamp。
- --incremental 模式选择 lastmodified。
- --merge-key 选择 ID。
- --last-value 为我们查询到的表中的最后更新时间。在此时间后做出的更新都会被同步到 HDFS 中，而 Sqoop job 每次会自动保存和更新该值。

对 MySQL 中的 sqoop_test 表添加数据并做出更改：
```
mysql> insert into sqoop_test values(null, 'sixth', now(), 'sqoop');
Query ok, 1 row affected(0.00 sec)

mysql> update sqoop_test set time=now(), content='spark' where id = 1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1 changed: 1 warnings: 0

Mysql> select * from sqoop_test;
+----+--------+---------------------+---------+
| id | title  | time                | content |
+----+--------+---------------------+---------+
|  1 | first  | 2018-07-03 16:07:46 | spark    |
|  2 | second | 2018-07-03 15:30:57 | mr      |
|  3 | third  | 2018-07-03 15:31:07 | yarn    |
|  4 | forth  | 2018-07-03 15:39:38  | hbase    |
|  5 | fifth  | 2018-07-03 16:02:29   | hive    |
|  6 | fifth  | 2018-07-03 16:09:58   | sqoop    |
+----+--------+---------------------+---------+
6 rows in set (0.00 sec)
```
执行 Sqoop job：
```
[hadoop@172 sqoop]$ bin/sqoop job --exec job2
```
执行该命令会让您输入 MySQL 的密码。执行成功后，可以查看 HDFS 相应目录下更新后的数据：
```
[hadoop@172 sqoop]$ hdfs dfs -cat /sqoop/*
1,first,2018-07-03 16:07:46.0,spark
2,second,2018-07-03 15:30:57.0,mr
3,third,2018-07-03 15:31:07.0,yarn
4,forth,2018-07-03 15:39:38.0,hbase
5,fifth,2018-07-03 16:02:29.0,hive
6,sixth,2018-07-03 16:09:58.0,sqoop
```
更多的 Sqoop 操作可以查看 [官方文档](http://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html)。
