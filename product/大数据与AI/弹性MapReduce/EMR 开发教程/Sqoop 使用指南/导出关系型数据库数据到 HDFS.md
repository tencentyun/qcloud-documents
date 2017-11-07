Sqoop 是一种用于在 Hadoop 和关系数据库之间传输数据的工具，能够有效地在关系数据库（如 MySQL）和大数据产品（Hadoop/Hive 等）之间导入/导出数据。本文介绍了使用腾讯云 Sqoop 服务将数据在 MySQL 和 Hadoop/Hive/HBase 之间导入/导出的使用方法。使用 EMR 中的服务建议都使用 Hadoop 用户执行。

创建表并插入测试数据, 如下:

``` sql
mysql> create table sgoop_test(id int not null primary key auto_increment, title varchar(64), time timestamp, content varchar(255)
Query ok , 0 rows affected(0.00 sec)

mysql> insert into sgoop_test values(null, first, now), 'hdfs')
Query ok, 1 row affected(0.00 sec)

mysql> insert into sgoop_test values(null, 'second', now), 'mr')
Query ok, 1 row affected (0.00 sec)

mysql> insert into sgoop_test values(null, third, now), 'yarn')
Query ok, 1 row affected(0.00 sec)

mysql select * from sgoop_test;
+----+--------+---------------------+---------+
| id | title  | time                | content |
+----+--------+---------------------+---------+
|  1 | first  | 2017-09-30 15:53:03 | hdfs    |
|  2 | second | 2017-09-30 15:53:30 | mr      |
|  3 | third  | 2017-09-30 15:53:43 | yarn    |
+----+--------+---------------------+---------+
3 rows in set (0.00 sec)
```

将 sqoop_test 表中的数据导入到 HDFS 中

``` shell
./sqoop-import --connect jdbc:mysql://172.31.20.31/test --username root --password ****** --table sqoop_test --target-dir /sqoopTest
#--target-dir 参数指明在HDFS中的目录。
```

检验数据

``` shell
[hadoop@172 root]$ hadoop fs -cat /sqoopTest/*
1, first,2017-09-30 15:53:03.0,hdfs
2, second,2017-09-30 15:53:30.0,mr
3, third,2017-09-30 15:53:43.0,yarn
```
