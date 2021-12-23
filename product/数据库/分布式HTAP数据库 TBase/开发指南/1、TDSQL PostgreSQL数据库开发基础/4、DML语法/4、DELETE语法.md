## delete语句

### 带条件删除

```
postgres=# select * from tdsql_pg;
 id |  nickname  
----+-------------
 2 | tdsql_pg好
 1 | Hello tdsql_pg
 3 | 
 4 | tdsql_pg good
(4 rows)
 
postgres=# delete from tdsql_pg where id=4;
DELETE 1
```

null条件的表达方式

```
postgres=# delete from tdsql_pg where nickname is null;
DELETE 1
postgres=# select * from tdsql_pg;
 id |  nickname  
----+-------------
 2 | tdsql_pg好
 1 | Hello tdsql_pg
(2 rows)
```



### 多表关联删除数据

```
postgres=# select * from tdsql_pg;
 id |  nickname  
----+-------------
 2 | tdsql_pg好
 1 | Hello tdsql_pg
(2 rows)
 
postgres=# set prefer_olap to on;
SET
postgres=# delete from tdsql_pg using t_appoint_col where tdsql_pg.id=t_appoint_col.id;
DELETE 1
postgres=# select * from tdsql_pg;
 id | nickname  
----+-----------
 2 | tdsql_pg好
(1 row)
```



### 返回删除数据

```
postgres=# delete from tdsql_pg returning *;
 id | nickname  
----+-----------
 2 | tdsql_pg好
(1 row)
 
```

returning特性可以返回DML（insert、update、delete）修改的数据，降低应用复杂度。



### 删除所有数据

```
postgres=# insert into tdsql_pg select t,random()::text from generate_series(1,100000) as t;
postgres=# \timing 
Timing is on.
postgres=# delete from tdsql_pg ;
DELETE 100000
Time: 100.808 ms
```

使用truncate方法是全表删除更高效的方法

```
postgres=# insert into tdsql_pg select t,random()::text from generate_series(1,100000) as t;
INSERT 0 100000
Time: 13178.429 ms
postgres=# truncate table tdsql_pg;
TRUNCATE TABLE
Time: 24.242 ms
```

