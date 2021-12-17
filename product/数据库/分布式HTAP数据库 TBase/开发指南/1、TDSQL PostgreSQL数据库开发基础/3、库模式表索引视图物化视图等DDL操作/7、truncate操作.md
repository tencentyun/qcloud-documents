### truncate操作

truncate功能用于对表数据进行快速清除，truncate属于ddl级别，会给truncate表加上ACCESS EXCLUSIVE最高级别的锁

#### truncate普通表

```
postgres=# truncate table t1;
TRUNCATE TABLE
```

也可以一次truncate多个数据表

```
postgres=# truncate table t1,t2;
TRUNCATE TABLE
postgres=# 
```



#### truncate分区表

- truncate一个时间分区表

```
postgres=# \d+ t_time_range 
                Table "pgxz.t_time_range"
 Column |       Type       | Modifiers | Storage  | Stats target | Description 
--------+-----------------------------+-----------+----------+--------------+-------------
 f1   | bigint            |      | plain   |        | 
 f2   | timestamp without time zone |      | plain   |        | 
 f3   | character varying(20)    |      | extended |        | 
Has OIDs: no
Distribute By SHARD(f1)
    Location Nodes: dn001, dn002
Partition By: RANGE(f2)
  # Of Partitions: 12
  Start With: 2017-09-01
  Interval Of Partition: 1 MONTH
 
postgres=# select * from t_time_range;
 f1 |     f2      |  f3  
----+---------------------+-------
 1 | 2017-09-01 00:00:00 | tdsql_pg
 2 | 2017-10-01 00:00:00 | pgxz
(2 rows)
 
postgres=# truncate t_time_range  partition for  ('2017-09-01' ::timestamp without time zone); 
TRUNCATE TABLE
postgres=# select * from t_time_range;
 f1 |     f2      |  f3  
----+---------------------+------
 2 | 2017-10-01 00:00:00 | pgxz
(1 row)
 
postgres=# 

```

  

- truncate一个数字分区表

```
postgres=# \d+ t_range 
                  Table "pgxz.t_range"
 Column |       Type       |  Modifiers  | Storage | Stats target | Description 
--------+-----------------------------+---------------+---------+--------------+-------------
 f1   | integer           |        | plain  |        | 
 f2   | timestamp without time zone | default now() | plain  |        | 
 f3   | integer           |        | plain  |        | 
Has OIDs: no
Distribute By SHARD(f1)
    Location Nodes: dn01, dn02
Partition By: RANGE(f3)
  # Of Partitions: 3
  Start With: 1
  Interval Of Partition: 50
 
postgres=# select * from t_range ;
 f1 |       f2       | f3  
----+----------------------------+-----
 1 | 2017-12-22 11:47:39.153234 |  1
 2 | 2017-12-22 11:47:39.153234 |  50
 2 | 2017-12-22 11:47:39.153234 | 110
 3 | 2017-12-22 11:47:39.153234 | 100
(4 rows)
 
postgres=# truncate t_range  partition for  (1);  
TRUNCATE TABLE
postgres=# select * from t_range ;         
 f1 |       f2       | f3  
----+----------------------------+-----
 2 | 2017-12-22 11:47:39.153234 | 110
 3 | 2017-12-22 11:47:39.153234 | 100
(2 rows)
 
```

 

