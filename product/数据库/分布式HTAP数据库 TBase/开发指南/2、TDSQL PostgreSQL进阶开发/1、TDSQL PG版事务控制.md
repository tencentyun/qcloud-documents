## TDSQL PG版事务控制

### 开始一个事务

```
postgres=# begin;
BEGIN
```

或者 

```
postgres=# begin TRANSACTION ; 
BEGIN
```

也可以定义事务的级别

```
postgres=# begin transaction isolation level read committed ;
BEGIN
```



### 提交事务

进程#1访问 

```
postgres=# begin;
BEGIN
postgres=# delete from tdsql_pg where id=5;
DELETE 1
postgres=#
postgres=# select * from tdsql_pg order by id;
 id |  nickname   
----+---------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 3 | tdsql_pg好
 4 | tdsql_pg default
```

TDSQL PostgreSQL也是完全支持ACID特性，没提交前开启另一个连接查询，你会看到是5条记录，这是TDSQL PostgreSQL隔离性和多版本视图的实现，如下所示

 

进程#2访问

```
postgres=# select * from tdsql_pg order by id;
 id |  nickname   
----+---------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 3 | tdsql_pg好
 4 | tdsql_pg default
 5 | tdsql_pg swap
(5 rows)
```



进程#1提交数据

```
postgres=# commit;
COMMIT
postgres=# 
```



进程#2再查询数据，这时能看到已经提交的数据了，这个级别叫“读已提交”

```
postgres=# select * from tdsql_pg order by id;
 id |  nickname   
----+---------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 3 | tdsql_pg好
 4 | tdsql_pg default
(4 rows)
```





### 回滚事务

```
postgres=# begin;
BEGIN
postgres=# delete from tdsql_pg where id in (3,4);
DELETE 2
postgres=# select * from tdsql_pg;
 id |  nickname  
----+-------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
(2 rows)
 
postgres=# rollback;
ROLLBACK
 
```

Rollback后数据又回来了

```
postgres=# select * from tdsql_pg;
 id |  nickname   
----+---------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 3 | tdsql_pg好
 4 | tdsql_pg default
(4 rows)
```



### 事务读一致性REPEATABLE READ

这种事务级别表示事务自始至终读取的数据都是一致的，如下所示

 

\#session1

 ```
 postgres=# create table t_repeatable_read (id int,mc text);
 NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
 CREATE TABLE
 postgres=# insert into t_repeatable_read values(1,'tdsql_pg');
 INSERT 0 1
 postgres=# begin isolation level repeatable read ;
 BEGIN
 postgres=# select * from t_repeatable_read ;
  id |  mc  
 ----+-------
  1 | tdsql_pg
 (1 row)
 ```



\#session2

```
postgres=# insert into t_repeatable_read values(1,'pgxz'); 
INSERT 0 1
postgres=# select * from t_repeatable_read;
 id |  mc  
----+-------
 1 | tdsql_pg
 1 | pgxz
(2 rows)
 
```



\#session1

```
postgres=# select * from t_repeatable_read ;
 id |  mc  
----+-------
 1 | tdsql_pg
(1 row)
 
postgres=#
```





### 行锁在事务中的运用

#### 环境准备

```
postgres=# create table t_row_lock(id int,mc text,primary key (id));
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# 
 
postgres=# insert into t_row_lock values(1,'tdsql_pg'),(2,'pgxz');    
INSERT 0 2
postgres=# select * from t_row_lock;
 id |  mc  
----+-------
 1 | tdsql_pg
 2 | pgxz
(2 rows)
```



#### 直接update获取

\#session1

```
postgres=# begin;
BEGIN
postgres=# set lock_timeout to 1;
SET
postgres=# update t_row_lock set mc='postgres' where mc='pgxz';
UPDATE 1
postgres=# 
```



\#session2

 ```
 postgres=# begin;
 BEGIN
 postgres=# set lock_timeout to 1;
 SET
 postgres=#  update t_row_lock set mc='postgresql' where mc='tdsql_pg';     
 UPDATE 1
 postgres=# 
 ```

上面session1与session2分别持有mc=pgxz行和mc=tdsql_pg的行锁



#### select...for update获取

\#session1 

```
postgres=#
BEGIN
postgres=# set lock_timeout to 1; 
SET
postgres=# select * from t_row_lock where mc='pgxz' for update;
 id |  mc  
----+------
 2 | pgxz
(1 row)
```



\#session2 

 ```
 postgres=# begin;
 BEGIN
 postgres=# set lock_timeout to 1; 
 SET
 postgres=# select * from t_row_lock where mc='tdsql_pg' for update;
  id |  mc  
 ----+------
  2 | pgxz
 (1 row)
 ```

上面session1与session2分别持有mc=pgxz行和mc=tdsql_pg的行锁



#### 与mysql获取行级锁的区别

```
mysql> select version();
+-----------+
| version() |
+-----------+
| 5.6.36   |
+-----------+
1 row in set (0.00 sec)
```



\#sessin1

```
mysql> begin;
Query OK, 0 rows affected (0.00 sec)
 
mysql> select * from t_row_lock where mc='pgxz' for update;
+----+------+
| id | mc  |
+----+------+
|  2 | pgxz |
+----+------+
1 row in set (0.00 sec)
```



\#session2

```
mysql> select * from t_row_lock where mc='tdsql_pg' for update;
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
mysql> 
 
```

这是因为mysql要使用行级锁需要有索引来配合使用，如下所示,使用id主键来获取行锁

 

\#session1

```
mysql> begin;
Query OK, 0 rows affected (0.00 sec)
 
mysql> select * from t_row_lock where id=1 for update;     
+----+-------+
| id | mc   |
+----+-------+
|  1 | tdsql_pg |
+----+-------+
1 row in set (0.00 sec)
```



\#session2

```
mysql> begin;
Query OK, 0 rows affected (0.00 sec)
 
mysql> select * from t_row_lock where id=2 for update;
+----+------+
| id | mc  |
+----+------+
|  2 | pgxz |
+----+------+
1 row in set (0.00 sec)
```



