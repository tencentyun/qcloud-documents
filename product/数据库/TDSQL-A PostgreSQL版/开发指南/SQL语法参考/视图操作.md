## 视图修改
### 创建视图
```
DROP TABLE if exists t_range;
CREATE TABLE t_range(
   f1 bigint,
   f2 timestamp default now(),
   f3 integer
 ) PARTITION BY range (f3) begin (1) step (50) partitions (3) WITh (orientation = 'column') DISTRIBUTE BY shard(f1) TO GROUP default_group;
INSERT INTO t_range(f1,f3) VALUES(1,1);
 INSERT INTO t_range(f1,f3) VALUES(2,50);
 INSERT INTO t_range(f1,f3) VALUES(2,110);
 INSERT INTO t_range(f1,f3) VALUES(3,100);

postgres=# CREATE VIEW t_range_view as SELECT * FROM t_range;
CREATE VIEW
postgres=# SELECT * FROM t_range_view;
 f1 |       f2       | f3 
----+----------------------------+-----
 3 | 2021-01-19 20:22:14.392501 | 100
 1 | 2021-01-19 20:22:13.585137 |  1
 2 | 2021-01-19 20:22:13.685255 | 50
 2 | 2021-01-19 20:22:13.702273 | 110
(4 rows)
```

### 数据类型重定义
```
postgres=# create or replace view t_range_view as SELECT f1,f2::date FROM t_range;
CREATE VIEW
postgres=# SELECT * FROM t_range_view;                
 f1 |   f2   
----+------------
 1 | 2017-09-27
 2 | 2017-09-27
 2 | 2017-09-27
 1 | 2017-09-27
 3 | 2017-09-27
(5 rows)
```

### 数据类型重定义及取别名
```
postgres=# create view t_range_view as SELECT f1,f2::date as mydate FROM t_range;
CREATE VIEW
postgres=# SELECT * FROM t_range_view;                      
 f1 |  mydate  
----+------------
 1 | 2017-09-27
 2 | 2017-09-27
 2 | 2017-09-27
 1 | 2017-09-27
 3 | 2017-09-27
(5 rows)
```

TDSQL-A PostgreSQL版 支持视图引用表或字段改名联动，不受影响：
```
DROP TABLE IF EXISTS t;
CREATE TABLE t(id int,mc text); 
create view t_view as SELECT * FROM t;

postgres=# \d+ t_view
              View "tdapg.t_view"
 Column | Type  | Collation | Nullable | Default | Storage | Description 
--------+---------+-----------+----------+---------+----------+-------------
 id   | integer |      |     |     | plain  | 
 mc   | text  |      |     |     | extended | 
View definition:
 SELECT t.id,
  t.mc
  FROM t;

postgres=# ALTER TABLE t rename to t_new;
ALTER TABLE
Time: 62.875 ms
postgres=# ALTER TABLE t_new rename mc to mc_new;        
ALTER TABLE
Time: 22.081 ms
postgres=# \d+ t_view
              View "tdapg.t_view"
 Column | Type  | Collation | Nullable | Default | Storage | Description 
--------+---------+-----------+----------+---------+----------+-------------
 id   | integer |      |     |     | plain  | 
 mc   | text  |      |     |     | extended | 
View definition:
 SELECT t_new.id,
  t_new.mc_new AS mc
  FROM t_new;
```


## 视图删除
```
postgres=# DROP TABLE if exists t;
DROP TABLE
postgres=# drop view if exists t_view;
DROP VIEW
postgres=# CREATE TABLE t (id int,mc text);
CREATE TABLE
postgres=# CREATE VIEW t_view as SELECT * FROM t;
CREATE VIEW
postgres=# CREATE VIEW t_view_1 as SELECT * FROM t_view;
CREATE VIEW
postgres=# CREATE VIEW t_view_2 as SELECT * FROM t_view; 
CREATE VIEW
postgres=# drop view t_view_2;
DROP VIEW
\#使用 cascade 强制删除依赖对象
postgres=# DROP VIEW t_view; 
ERROR: cannot drop view t_view because other objects depend on it
DETAIL: view t_view_1 depends on view t_view
HINT: Use DROP ... CASCADE to drop the dependent objects too.
postgres=# DROP VIEW t_view cascade;
NOTICE: drop cascades to view t_view_1
DROP VIEW 
```

## 物化视图
### 创建物化视图
```
postgres=# CREATE MATERIALIZED VIEW t_range_mv AS SELECT f1,f2::date FROM t_range;    
SELECT 5
postgres=# SELECT * FROM t_range_mv;
 f1 |   f2   
----+------------
 1 | 2017-09-27
 2 | 2017-09-27
 2 | 2017-09-27
 1 | 2017-09-27
 3 | 2017-09-27
(5 rows)
```

### 访问物化视图
```
postgres=# SELECT * FROM t_range_mv;        
 f1 |   f2   
----+------------
 1 | 2017-09-27
 2 | 2017-09-27
 2 | 2017-09-27
 1 | 2017-09-27
 3 | 2017-09-27
(5 rows)

postgres=# INSERT INTO t_range(f1,f3) VALUES(5,10);
INSERT 0 1
postgres=# SELECT * FROM t_range;
 f1 |       f2       | f3 | f4 
----+----------------------------+-----+----
 1 | 2017-09-27 23:17:39.674318 |  1 | 
 2 | 2017-09-27 23:17:39.674318 | 50 | 
 5 | 2017-09-27 23:50:51.576173 | 10 | 
 2 | 2017-09-27 23:17:39.674318 | 110 | 
 1 | 2017-09-27 23:39:45.841093 | 151 | 
 3 | 2017-09-27 23:17:39.674318 | 100 | 
(6 rows)
```

### 增量数据刷新
```
postgres=# SELECT * FROM t_range_mv ;
 f1 |   f2   
----+------------
 1 | 2017-09-27
 2 | 2017-09-27
 2 | 2017-09-27
 1 | 2017-09-27
 3 | 2017-09-27
(5 rows) 

postgres=# REFRESH MATERIALIZED VIEW t_range_mv;
REFRESH MATERIALIZED VIEW
postgres=# SELECT * FROM t_range_mv ;
 f1 |   f2   
----+------------
 1 | 2017-09-27
 2 | 2017-09-27
 5 | 2017-09-27
 2 | 2017-09-27
 1 | 2017-09-27
 3 | 2017-09-27
(6 rows)
```
物化视图数据存储在 CN 节点上面，每个 CN 节点各有一份相同的数据。
