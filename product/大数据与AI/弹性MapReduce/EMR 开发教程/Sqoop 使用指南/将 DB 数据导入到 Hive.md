本文介绍了使用腾讯云 Sqoop 服务将数据从 MySQL 导入 Hive 的使用方法。
## 1. 开发准备
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Sqoop，Hive 组件。 
- Sqoop 等相关软件安装在路径 EMR 云服务器的` /usr/local/service/`路径 下。

## 2. 将关系型数据库导入到 Hive 中
本节将继续使用上一节的用例。
进入 EMR 控制台，复制目标集群的实例  ID，即集群的名字。再进入关系型数据库控制台，使用 Ctrl+F 进行搜索，找到集群对应的 MySQL 数据库，查看该数据库的内网地址 $mysqlIP。

登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考[登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。
在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Hive 文件夹：
```
[root@172 ~]# su Hadoop
[hadoop@172 ~]# cd /usr/local/service/hive
```
新建一个 Hive 数据库：
```
[hadoop@172 hive]$ hive
hive> creat database hive_from_sqoop;
OK
Time taken: 0.167 seconds
```
使用 sqoop-import 命令把上一节中创建的 MySQL 数据库导入到 Hive 中：
```
[hadoop@172 hive]# cd /usr/local/service/sqoop
[hadoop@172 sqoop]$ bin/sqoop-import --connect  jdbc:mysql://$mysqlIP/test --username 
root -P --table sqoop_test_back --hive-database test --hive-import --hive-table hive_from_sqoop
```
其中 $mysqlIP 为您的腾讯云关系型数据库（CDB）的内网地址。test 为您 MySQL 数据库的名字，--table 为要导出的 MySQL 表名，--hive-database 为您的 Hive 数据库名，--hive-table 为您要导入的 Hive 表名。
执行指令需要输入您的 MySQL 密码，默认为您创建 EMR 集群时设置的密码。
执行成功后，可以在 Hive 中查看您导入的数据库：
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
更多的 Sqoop 操作可以查看 [官方文档](http://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html)。
