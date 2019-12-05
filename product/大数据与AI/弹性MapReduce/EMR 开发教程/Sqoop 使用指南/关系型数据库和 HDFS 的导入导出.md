Sqoop 是一款开源的工具，主要用于在 Hadoop 和传统数据库（MySQL、PostgreSQL 等）之间进行数据传递，可以将一个关系型数据库（例如：MySQL、Oracle、Postgres 等）中的数据导入到 Hadoop 的 HDFS 中，也可以将 HDFS 的数据导入到关系型数据库中。Sqoop 中一大亮点就是可以通过 Hadoop 的 MapReduce 把数据从关系型数据库中导入数据到 HDFS。

本文介绍了使用腾讯云 Sqoop 服务将数据在 MySQL 和 HDFS 之间导入/导出的使用方法。

## 1. 开发准备
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Sqoop 组件。 
- Sqoop 等相关软件安装在路径 EMR 云服务器的` /usr/local/service/`路径下。

## 2. 新建一个 MySQL 表
首先要连接已经创建好的 MySQL 数据库，进入 EMR 控制台，复制目标集群的实例 ID，即集群的名字。再进入关系型数据库控制台，使用 Ctrl+F 进行搜索，找到集群对应的 MySQL 数据库，查看该数据库的内网地址 $mysqlIP。

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
连接了 MySQL 数据库之后，进入 test 数据库并且新建一个表，用户也可以自己选择目标数据库：
```
mysql> use test;
Database changed

mysql> create table sqoop_test(id int not null primary key auto_increment, title varchar(64), time timestamp, content varchar(255));
Query ok , 0 rows affected(0.00 sec)
```
该指令创建了一个 MySQL 表，它的主键为 ID，然后还有三列分别为 title、time 和 content。向该表中插入一些数据如下：
```
mysql> insert into sqoop_test values(null, 'first', now(), 'hdfs');
Query ok, 1 row affected(0.00 sec)

mysql> insert into sqoop_test values(null, 'second', now(), 'mr');
Query ok, 1 row affected (0.00 sec)

mysql> insert into sqoop_test values(null, 'third', now(), 'yarn');
Query ok, 1 row affected(0.00 sec)
```
使用如下指令可以查看表中的数据：
```
Mysql> select * from sqoop_test;
+----+--------+---------------------+---------+
| id | title  | time                | content |
+----+--------+---------------------+---------+
|  1 | first  | 2018-07-03 15:29:37 | hdfs    |
|  2 | second | 2018-07-03 15:30:57 | mr      |
|  3 | third  | 2018-07-03 15:31:07 | yarn    |
+----+--------+---------------------+---------+
3 rows in set (0.00 sec)
```
退出 MySQL 数据库：
```
Mysql> exit;
```

## 3. 将 MySQL 的数据导入到 HDFS 中
使用 sqoop-import 把上一步中创建的 sqoop_test 表中数据导入到 HDFS 中：
```
[hadoop@172 sqoop]$ bin/sqoop-import --connect jdbc:mysql://$mysqlIP/test --username root 
-P --table sqoop_test --target-dir /sqoop
```
其中 --connect 用于连接 MySQL 数据库，test 也可以换成您的数据库名字，-P 表示之后需要输入密码，--table 为您想要导出的数据库的名字，--target-dir 为导出到 HDFS 中的路径。**`/sqoop`文件夹在执行命令之前并未创建，如果文件夹已经存在会出错。**
回车之后需要您输入密码，密码为您创建 EMR 时设置的密码。

执行成功之后，可以在 HDFS 的相应路径下查看导入的数据：
```
[hadoop@172 sqoop]$ hadoop fs -cat /sqoop/*
1, first, 2018-07-03 15:29:37.0,hdfs
2, second, 2018-07-03 15:30:57.0,mr
3, third, 2018-07-03 15:31:07.0,yarn
```

## 4. 将 HDFS 的数据导入到 MySQL 中
首先需要在 MySQL 新建一个表准备存放 HDFS 中的数据：
```
[hadoop@172 sqoop]$ mysql -h $mysqlIP –p
Enter password:
mysql> use test;
Database changed

mysql> create table sqoop_test_back(id int not null primary key auto_increment, title varchar(64), time timestamp, (content varchar(255));
Query ok , 0 rows affected(0.00 sec)
```
查看表是否创建成功之后退出 MySQL：
```
mysql> show tables;                                                                     
+-----------------+
| Tables_in_test  |
+-----------------+
| sqoop_test      |
| sqoop_test_back |
+-----------------+
2 rows in set (0.00 sec)

mysql> exit;
```
使用 sqoop-export 把上一步导入 HDFS 中的数据再一次导入到 MySQL 中来：
```
[hadoop@172 sqoop]$ bin/sqoop-export --connect jdbc:mysql://172.16.16.42/test --username 
root -P --table sqoop_test_back --export-dir /sqoop
```
参数和 sqoop-import 类似，只不过变成了 --export-dir，该参数为 HDFS 中的存放数据的路径。回车之后也需要输入密码。
执行成功之后可以验证数据库 sqoop_test_back 中的数据：
```
[hadoop@172 sqoop]$ mysql -h $mysqlIP –p
Enter password:
mysql> use test;
Database changed

mysql> select * from sqoop_test_back;
+----+---------+---------------------+---------+
| id | title   | time                | content |
+----+---------+---------------------+---------+
|  1 | first   | 2018-07-03 15:29:37 | hdfs   |
|  2 | second  | 2018-07-03 15:30:57 | mr      |
|  3 | third   | 2018-07-03 15:31:07 | yarn    |
+----+---------+---------------------+---------+
3 rows in set (0.00 sec)
```
更多的 Sqoop 操作可以查看 [官方文档](http://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html)。
　　　
