创建表来存放 HDFS 中的数据

``` sql
mysql> create table sqoop_test_back(id int not null primary key auto_increment, title varchar (64), time  timestamp
content varchar(255));
Query OK, 0 rows affected (0.00 sec)
```

导出数据

``` shell
[hadoop@172 bin]$ ./sqoop-export --connect jdbc:mysql://172.31.20.31/test --username root --password ****** --table sqoop_test_back -export-dir /sqoopTest 
```

验证导出结果

``` shell
mysql> select * from sqoop_test_back
   -> ;
+----+---------+---------------------+---------+
| id | title   | time                | content |
+----+---------+---------------------+---------+
|  1 | first   | 2017-09-30 17:30:57 | AAAAA   |
|  2 | second  | 2017-09-30 15:53:30 | mr      |
|  3 | third   | 2017-09-30 15:53:43 | yarn    |
|  4 | forth   | 2017-09-30 16:28:05 | hive    |
|  5 | fifth   | 2017-09-30 17:07:04 | spark   |
|  6 | sixth   | 2017-09-30 17:11:37 | kyin    |
|  7 | seventh | 2017-09-30 17:31:21 | hbase   |
+----+---------+---------------------+---------+   
7 rows in set (0.00 sec)
```
