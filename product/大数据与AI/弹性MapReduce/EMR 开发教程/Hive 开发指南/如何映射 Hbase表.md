使用 Hive 来映射 Hbase 表，可以使用 Hive 来读取 Hbase 上的数据，使用 Hive-SQL 语句在 Hbase 表上进行查询、插入等操作。

## 开发准备
- 确认已开通腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群时需要在软件配置界面选择 Hive、Hbase 组件。 
- Hive 等相关软件安装在路径 EMR 云服务器的 `/usr/local/service/` 路径下。

## 创建一个 Hbase 表 
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，进入 Hbase 文件夹并进入 Hbase shell：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]# cd /usr/local/service/hbase
[hadoop@10hbase]$ bin/hbase shell
```
在 Hbase 中建立一个新表，如下所示：
```
hbase(main):001:0> create 'test', 'cf'
hbase(main):003:0> put 'test', 'row1', 'cf:a', 'value1'
hbase(main):004:0> put 'test', 'row1', 'cf:b', 'value2'
hbase(main):005:0> put 'test', 'row1', 'cf:c', 'value3'
```
更多在 Hbase 中的操作详见 Hbase 操作指南，或者查看 [官方文档](http://hbase.apache.org/book.html#_introduction)。

创建完成后，可使用`list`和`scan`操作来查看新建的表。
```
hbase(main):001:0> list 'test'
TABLE                                                       
test                                                         
1 row(s) in 0.0030 seconds
=> ["test"]

hbase(main):002:0> scan 'test'
ROW  COLUMN+CELL                                             
row1   column=cf:a, timestamp=1530276759697, value=value1   
row2   column=cf:b, timestamp=1530276777806, value=value2   
row3   column=cf:c, timestamp=1530276792839, value=value3   
3 row(s) in 0.2110 seconds
```

## 映射 Hive 表
切换到 Hive 文件夹下，并且连接到 Hive 上：
```
[hadoop@172 hive]$ cd /usr/local/service/hive/
[hadoop@172 hive]$ bin/hive
```
接下来创建一个 Hive 外部表让它映射到第二步中创建的 Hbase 表上：
```
hive> CREATE EXTERNAL TABLE hive_test (
    > rowkey string,
    > a string,
    > b string,
    > c string
    > ) STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler' WITH
    > SERDEPROPERTIES("hbase.columns.mapping" = ":key,cf:a,cf:b,cf:c")
    > TBLPROPERTIES("hbase.table.name" = "test");
OK
Time taken: 2.086 seconds
```
这样就建立了一个 Hive 表到 Hbase 表的映射。可使用以下指令来查看 Hive 表中的元素：
```
hive> select * from hive_test;
OK
row1 value1	value2 value3
Time taken: 0.305 seconds, Fetched: 1 row(s)
```

