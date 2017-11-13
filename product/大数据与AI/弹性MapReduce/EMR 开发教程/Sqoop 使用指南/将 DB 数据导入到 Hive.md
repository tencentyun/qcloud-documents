创建数据库：

``` sql
hive> creat database test;
OK
Time taken: 0.167 seconds
```

导入数据：

``` shell
[hadoop@172 bin]$ ./sqoop-import --connect jdbc:mysql://172.31.20.31/test --username root --password ****** --table sqoop_test --hive-database test -hive-import -hive-table sqoop_test
```

验证结果：

``` sql
hive> select * from sqoop_test
    > ;
OK
1 | first   2017-09-30 17:30:57  AAAAA   
2 | second  2017-09-30 15:53:30  mr      
3 | third   2017-09-30 15:53:43  yarn    
4 | forth   2017-09-30 16:28:05  hive    
5 | fifth   2017-09-30 17:07:04  spark  
6 | sixth   2017-09-30 17:11:37  kyin   
7 | seventh 2017-09-30 17:31:21  hbase   
Time taken: 0.897 seconds, Fetched: 7 row(s)
```
