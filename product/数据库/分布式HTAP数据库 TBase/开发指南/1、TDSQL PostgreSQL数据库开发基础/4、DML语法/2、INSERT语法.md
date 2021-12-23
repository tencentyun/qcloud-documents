## insert语句

### 插入单条记录

指定所有字段

```
postgres=# insert into tdsql_pg(id,nickname) values(1,'hello tdsql_pg');
INSERT 0 1
```

指定某些字段，不指的有默认值的插入时带上默认值

```
postgres=# insert into tdsql_pg(nickname) values('tdsql_pg好');    
INSERT 0 1
```

不指定字段则默认为所有字段与建表时一致

```
postgres=# insert into tdsql_pg values(nextval('t_id_seq'::regclass),'tdsql_pg好');
INSERT 0 1
```

字段顺序可以任意排列

 ```
 postgres=# insert into tdsql_pg(nickname,id) values('tdsql_pg swap',5);         
 INSERT 0 1
 ```

使用default关键字，即值为建表时指定的默认值方式

```
postgres=#  insert into tdsql_pg(id,nickname) values(default,'tdsql_pg default');     
INSERT 0 1
```

上面五次插入记录后产生的数据

```
postgres=# select * from tdsql_pg;
 id |  nickname   
----+---------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
 5 | tdsql_pg swap
 3 | tdsql_pg好
 4 | tdsql_pg default
(5 rows)
```



### 插入多数记录

```
postgres=# insert into tdsql_pg(id,nickname) values(1,'hello tdsql_pg'),(2,'tdsql_pg好');
INSERT 0 2
postgres=# select * from tdsql_pg;
 id |  nickname  
----+-------------
 1 | hello tdsql_pg
 2 | tdsql_pg好
(2 rows)
```



### 使用子查询插入数据

```
postgres=# insert into tdsql_pg(id,nickname) values(1,(select relname from pg_class limit 1));   
INSERT 0 1
postgres=# select * from tdsql_pg;
 id |  nickname  
----+--------------
 1 | pg_statistic
(1 row)
```



### 从另外一个表取数据进行批量插入

```
postgres=# insert into tdsql_pg(nickname) select relname from pg_class limit 3;
INSERT 0 3
postgres=# select * from tdsql_pg;
 id |  nickname   
----+---------------
 5 | pg_type
 6 | pg_toast_2619
 4 | pg_statistic
(3 rows)
```



### 大批量的生成数据

```
postgres=# insert into tdsql_pg select t,md5(random()::text) from generate_series(1,10000) as t;
INSERT 0 10000
postgres=# select count(1) from tdsql_pg;
 count 
-------
 10000
(1 row)
```



### 返回插入数据，轻松获取插入记录的serial值

```
postgres=# insert into tdsql_pg(nickname) values('tdsql_pg好') returning *;     
 id | nickname  
----+-----------
 7 | tdsql_pg好
(1 row)
INSERT 0 1

postgres=# insert into tdsql_pg(nickname) values('hello tdsql_pg') returning id;       
 id 
\----
 8
(1 row)
```

指定返回的字段



### insert..update更新

- **使用ON CONFLICT**

```
postgres=# \d+ t
              Table "public.t"
 Column |  Type  | Modifiers | Storage  | Stats target | Description 
--------+---------+-----------+----------+--------------+-------------
 id   | integer |      | plain   |        | 
 nc   | text   |      | extended |        | 
Indexes:
  "t_id_udx" UNIQUE, btree (id)
Has OIDs: no
Distribute By SHARD(id)
    Location Nodes: ALL DATANODES
 
postgres=# select * from t;
 id |  nc  
----+------
 1 | pgxz
(1 row)
 
postgres=# insert into t values(1,'pgxz') ON CONFLICT (id)  DO UPDATE SET nc = 'tdsql_pg';      
INSERT 0 1
postgres=# select * from t;
 id |  nc  
----+-------
 1 | tdsql_pg
(1 row)
```

