
## 开始一个事务
```
postgres=# begin;
BEGIN
```
或
```
postgres=# begin TRANSACTION ; 
BEGIN
```
可以定义事务的级别
```
postgres=# begin transaction isolation level read committed ;
BEGIN
```

## 提交事务
**进程#1访问**
```
postgres=# begin;
BEGIN
postgres=# delete from tbase where id=5;
DELETE 1
postgres=#
postgres=# select * from tbase order by id;
 id |   nickname    
----+---------------
  1 | hello TBase
  2 | TBase好
  3 | TBase好
  4 | TBase default
```

TDSQL PostgreSQL版 完全支持 ACID 特性，没提交前开启另一个连接查询，会看到5条记录，这是 TDSQL PostgreSQL版 隔离性和多版本视图的实现，如下所示：

**进程#2访问**
```
postgres=# select * from tbase order by id;
 id |   nickname    
----+---------------
  1 | hello TBase
  2 | TBase好
  3 | TBase好
  4 | TBase default
  5 | TBase swap
(5 rows)
```


**进程#1提交数据**
```
postgres=# commit;
COMMIT
postgres=# 
```

**进程#2再查询数据，此时能看到已经提交的数据，这个级别叫“读已提交”。**
```
postgres=# select * from tbase order by id;
 id |   nickname    
----+---------------
  1 | hello TBase
  2 | TBase好
  3 | TBase好
  4 | TBase default
(4 rows)
```
 

## 回滚事务
```
postgres=# begin;
BEGIN
postgres=# delete from tbase where id in (3,4);
DELETE 2
postgres=# select * from tbase;
 id |  nickname   
----+-------------
  1 | hello TBase
  2 | TBase好
(2 rows)

postgres=# rollback;
ROLLBACK
```

Rollback 后数据回退。
```
postgres=# select * from tbase;
 id |   nickname    
----+---------------
  1 | hello TBase
  2 | TBase好
  3 | TBase好
  4 | TBase default
(4 rows)
```
 

## 事务读一致性 REPEATABLE READ
这种事务级别表示事务自始至终读取的数据都是一致的，如下所示：

```
\#session1

postgres=# create table t_repeatable_read (id int,mc text);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# insert into t_repeatable_read values(1,'tbase');
INSERT 0 1

postgres=# begin isolation level repeatable read ;
BEGIN
postgres=# select * from t_repeatable_read ;
 id |  mc   
----+-------
  1 | tbase
(1 row)

\#session2

postgres=# insert into t_repeatable_read values(1,'pgxz'); 
INSERT 0 1
postgres=# select * from t_repeatable_read;
 id |  mc   
----+-------
  1 | tbase
  1 | pgxz
(2 rows)

\#session1

postgres=# select * from t_repeatable_read ;
 id |  mc   
----+-------
  1 | tbase
(1 row)

postgres=#
```


## 行锁在事务中的运用
### 环境准备
```
postgres=# create table t_row_lock(id int,mc text,primary key (id));
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# 

postgres=# insert into t_row_lock values(1,'tbase'),(2,'pgxz');       
INSERT 0 2
postgres=# select * from t_row_lock;
 id |  mc   
----+-------
  1 | tbase
  2 | pgxz
(2 rows)
```

### 直接 update 获取
```
\#session1
postgres=# begin;
BEGIN
postgres=# set lock_timeout to 1;
SET
postgres=# update t_row_lock set mc='postgres' where mc='pgxz';
UPDATE 1
postgres=# 

\#session2

postgres=# begin;
BEGIN
postgres=# set lock_timeout to 1;
SET
postgres=#  update t_row_lock set mc='postgresql' where mc='tbase';        
UPDATE 1
postgres=# 
```
上面 session1 与 session2 分别持有 mc=pgxz 行和 mc=tbase 的行锁。

### select...for update 获取
```
\#session1 

postgres=#  
BEGIN
postgres=# set lock_timeout to 1; 
SET
postgres=# select * from t_row_lock where mc='pgxz' for update;
 id |  mc  
----+------
  2 | pgxz
(1 row)

\#session2 

postgres=# begin;
BEGIN
postgres=# set lock_timeout to 1; 
SET
postgres=# select * from t_row_lock where mc='tbase' for update;
 id |  mc  
----+------
  2 | pgxz
(1 row)
```
上面 session1 与 session2 分别持有 mc=pgxz 行和 mc=tbase 的行锁。

### 与 mysql 获取行级锁的区别
```
mysql> select version();
+-----------+
| version() |
+-----------+
| 5.6.36    |
+-----------+
1 row in set (0.00 sec)

\#sessin1

mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from t_row_lock where mc='pgxz' for update;
+----+------+
| id | mc   |
+----+------+
|  2 | pgxz |
+----+------+
1 row in set (0.00 sec)

\#session2

mysql> select * from t_row_lock where mc='tbase' for update;
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
mysql> 
```

这是因为 mysql 要使用行级锁需要有索引来配合使用，如下所示，使用 id 主键来获取行锁。
```
\#session1

mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from t_row_lock where id=1 for update;         
+----+-------+
| id | mc    |
+----+-------+
|  1 | tbase |
+----+-------+
1 row in set (0.00 sec)

\#session2

mysql> begin;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from t_row_lock where id=2 for update;
+----+------+
| id | mc   |
+----+------+
|  2 | pgxz |
+----+------+
1 row in set (0.00 sec)
```
 
