## update语句

### 单表更新

```
postgres=# update tdsql_pg set nickname ='Hello tdsql_pg' where id=1;
UPDATE 1
 
```

null条件的表达方法

```
postgres=# update tdsql_pg set nickname = 'Good tdsql_pg' where nickname is null;
UPDATE 1
postgres=# select * from tdsql_pg;
 id |  nickname  
----+-------------
 2 | tdsql_pg好
 1 | Hello tdsql_pg
 3 | Good tdsql_pg
(3 rows)
```



### 多表关联更新

```
postgres=# update tdsql_pg set nickname ='Good tdsql_pg' from t_appoint_col where t_appoint_col.id=tdsql_pg.id;
UPDATE 1
postgres=# select * from tdsql_pg;
 id |  nickname  
----+------------
 2 | tdsql_pg好
 1 | Good tdsql_pg
(2 rows)
```



### 返回更新的数据

```
postgres=# update tdsql_pg set nickname = nickname where id = (random()*2)::integer returning *;
 id | nickname  
----+-----------
 2 | tdsql_pg好
(1 row)
 
```

上面的语句我们随机更新了一些数据，然后返回更新过的记录，returning机制大在的降低的应用的复杂度



### 多列匹配更新

```
postgres=# update tdsql_pg set ( nickname , age ) = ( 'tdsql_pg好' , (random()*2)::integer );
UPDATE 2
postgres=# select * from tdsql_pg;
 id | nickname  | age 
----+-----------+-----
 1 | tdsql_pg好 |  2
 2 | tdsql_pg好 |  0
(2 rows)
```



### shard key禁止更新操作

```
postgres=# update tdsql_pg set id=8 where id=1;             
ERROR:  Distribute column or partition column can't be updated in current version
```


