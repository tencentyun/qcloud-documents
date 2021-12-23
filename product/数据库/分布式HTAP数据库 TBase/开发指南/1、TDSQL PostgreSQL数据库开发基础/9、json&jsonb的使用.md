## json/jsonb的使用

TDSQL PostgreSQL不只是一个分布式关系型数据库系统，同时它还支持非关系数据类型json。JSON 数据类型是用来存储 JSON（JavaScript Object Notation） 数据的。这种数据也可以被存储为text，但是 JSON 数据类型的 优势在于能强制要求每个被存储的值符合 JSON 规则。 也有很多 JSON 相关的函数和操作符可以用于存储在这些数据类型中的数据。JSON 数据类型有json 和 jsonb。它们接受完全相同的值集合作为输入。主要的实际区别是效率。json数据类型存储输入文本的精准拷贝，处理函数必须在每次执行时必须重新解析该数据。而jsonb数据被存储在一种分解好的二进制格式中，它在输入时要稍慢一些，因为需要做附加的转换。但是 jsonb在处理时要快很多，因为不需要解析。jsonb也支持索引，这也是一个令人瞩目的优势。 

### json应用

#### 创建json类型字段表

```
postgres=# create table t_json(id int,f_json json);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
```



#### 插入数据

```
postgres=# insert into t_json values(1,'{"col1":1,"col2":"tdsql_pg"}');
INSERT 0 1
postgres=# insert into t_json values(2,'{"col1":1,"col2":"tdsql_pg","col3":"pgxz"}');
INSERT 0 1
postgres=# select * from t_json;
 id |         f_json          
----+-----------------------------------------
 1 | {"col1":1,"col2":"tdsql_pg"}
 2 | {"col1":1,"col2":"tdsql_pg","col3":"pgxz"}
(2 rows)
```



#### 通过键获得 JSON 对象域

```
postgres=# select f_json ->'col2' as col2 ,f_json -> 'col3' as col3 from t_json;  
 col2  |  col3  
---------+--------
 "tdsql_pg" | 
 "tdsql_pg" | "pgxz"
(2 rows)
```



#### 以文本形式获取对象值

```
postgres=# select f_json ->>'col2' as col2 ,f_json ->> 'col3' as col3 from t_json;
 col2  | col3 
-------+------
 tdsql_pg | 
 tdsql_pg | pgxz
(2 rows)
 
postgres=# select f_json ->>'col2' as col2 ,f_json ->> 'col3' as col3 from t_json where f_json ->> 'col3' is not null;
 col2  | col3 
-------+------
 tdsql_pg | pgxz
(1 row)
```



### jsonb应用

#### 创建jsonb类型字段表

```
postgres=# create table t_jsonb(id int,f_jsonb jsonb);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# 
```



#### 插入数据

```
postgres=# insert into t_jsonb values(1,'{"col1":1,"col2":"tdsql_pg"}');
INSERT 0 1
postgres=# insert into t_jsonb values(2,'{"col1":1,"col2":"tdsql_pg","col3":"pgxz"}');
INSERT 0 1
 
postgres=# select * from t_jsonb;
 id |          f_jsonb           
----+----------------------------------------------
 1 | {"col1": 1, "col2": "tdsql_pg"}
 2 | {"col1": 1, "col2": "tdsql_pg", "col3": "pgxz"}
(2 rows)
 
```



jsonb插入时会移除重复的键，如下所示

```
postgres=# insert into t_jsonb values(3,'{"col1":1,"col2":"tdsql_pg","col2":"pgxz"}');
INSERT 0 1
postgres=# select * from t_jsonb;
 id |          f_jsonb           
----+----------------------------------------------
 1 | {"col1": 1, "col2": "tdsql_pg"}
 3 | {"col1": 1, "col2": "pgxz"}
 2 | {"col1": 1, "col2": "tdsql_pg", "col3": "pgxz"}
(3 rows)
```



#### 更新数据

增加元素

```
postgres=# update t_jsonb set f_jsonb = f_jsonb || '{"col3":"pgxz"}'::jsonb where id=1;  
UPDATE 1
 
```

更新原来的元素

```
postgres=# update t_jsonb set f_jsonb = f_jsonb || '{"col2":"tdsql_pg"}'::jsonb where id=3;   
UPDATE 1
 
postgres=# select * from t_jsonb;
 id |          f_jsonb           
----+----------------------------------------------
 2 | {"col1": 1, "col2": "tdsql_pg", "col3": "pgxz"}
 1 | {"col1": 1, "col2": "tdsql_pg", "col3": "pgxz"}
 3 | {"col1": 1, "col2": "tdsql_pg"}
(3 rows)
```

删除某个键

```
postgres=# update t_jsonb set f_jsonb = f_jsonb - 'col3';   
UPDATE 3
 
postgres=# select * from t_jsonb;
 id |      f_jsonb       
----+------------------------------
 2 | {"col1": 1, "col2": "tdsql_pg"}
 1 | {"col1": 1, "col2": "tdsql_pg"}
 3 | {"col1": 1, "col2": "tdsql_pg"}
(3 rows)
```



#### jsonb_set()函数更新数据

jsonb_set(target jsonb, path text[], new_value jsonb, [create_missing boolean]) 说明：target指要更新的数据源，path指路径，new_value指更新后的键值，create_missing值为true表示如果键不存在则添加，create_missing值为false表示如果键不存在则不添加。

```
postgres=# update t_jsonb set f_jsonb = jsonb_set( f_jsonb , '{col}' , '"pgxz"' , true ) where id=1;
UPDATE 1
postgres=# update t_jsonb set f_jsonb = jsonb_set( f_jsonb , '{col}' , '"pgxz"' , false ) where id=2;     
UPDATE 1
postgres=# update t_jsonb set f_jsonb = jsonb_set( f_jsonb , '{col2}' , '"pgxz"' , false ) where id=3;      
UPDATE 1
postgres=# select * from t_jsonb;
 id |          f_jsonb          
----+---------------------------------------------
 1 | {"col": "pgxz", "col1": 1, "col2": "tdsql_pg"}
 2 | {"col1": 1, "col2": "tdsql_pg"}
 3 | {"col1": 1, "col2": "pgxz"}
(3 rows)
```





### jsonb函数应用

#### jsonb_each()将json对象转变键和值

```
postgres=# select  f_jsonb  from t_jsonb where id=1;
          f_jsonb          
---------------------------------------------
 {"col": "pgxz", "col1": 1, "col2": "tdsql_pg"}
(1 row)
 
postgres=#  select * from  jsonb_each((select  f_jsonb  from t_jsonb where id=1)); 
 key  |  value  
------+---------
 col  | "pgxz"
 col1 | 1
 col2 | "tdsql_pg"
(3 rows)
```



#### jsonb_each_text()将json对象转变文本类型的键和值

```
postgres=#  select * from  jsonb_each_text((select  f_jsonb  from t_jsonb where id=1)); 
 key  | value 
------+-------
 col  | pgxz
 col1 | 1
 col2 | tdsql_pg
(3 rows)
```



#### row_to_json()将一行记录变成一个json对象

```
postgres=# \d+ tdsql_pg
                  Table "public.tdsql_pg"
 Column  |  Type  | Collation | Nullable | Default | Storage  | Stats target | Description 
----------+---------+-----------+----------+---------+----------+--------------+-------------
 id    | integer |      | not null |     | plain   |        | 
 nickname | text   |      |      |     | extended |        | 
Indexes:
  "tdsql_pg_pkey" PRIMARY KEY, btree (id)
Distribute By: SHARD(id)
Location Nodes: ALL DATANODES
 
postgres=# select * from tdsql_pg;
 id | nickname 
----+----------
 1 | tdsql_pg
 2 | pgxz
(2 rows)
 
postgres=# select row_to_json(tdsql_pg) from tdsql_pg;
     row_to_json     
-----------------------------
 {"id":1,"nickname":"tdsql_pg"}
 {"id":2,"nickname":"pgxz"}
(2 rows)
```



#### json_object_keys()返回一个对象中所有的键

```
postgres=#  select * from json_object_keys((select  f_jsonb  from t_jsonb where id=1)::json); 
 json_object_keys 
------------------
 col
 col1
 col2
(3 rows)
```



### jsonb索引使用

tdsql_pg为文档jsonb提供了GIN索引，GIN 索引可以被用来有效地搜索在大量jsonb文档（数据）中出现 的键或者键值对。

#### 创建立jsonb索引

```
postgres=# create index t_jsonb_f_jsonb_idx on t_jsonb using gin(f_jsonb);
CREATE INDEX
 
postgres=# \d+ t_jsonb
                  Table "public.t_jsonb"
 Column  |  Type  | Collation | Nullable | Default | Storage  | Stats target | Description 
---------+---------+-----------+----------+---------+----------+--------------+-------------
 id    | integer |      |      |     | plain   |        | 
 f_jsonb | jsonb  |      |      |     | extended |        | 
Indexes:
  "t_jsonb_f_jsonb_idx" gin (f_jsonb)
Distribute By: SHARD(id)
Location Nodes: ALL DATANODES
```



#### 测试查询的性能

```
postgres=# select count(1) from t_jsonb;
 count  
----------
 10000000
(1 row)
 
postgres=# analyze t_jsonb;
ANALYZE
```

没有索引开销

```
postgres=# select * from t_jsonb where f_jsonb @> '{"col1":9999}';
 id  |       f_jsonb       
------+--------------------------------
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
(5 rows)
Time: 2473.488 ms (00:02.473)
```

有索引开销

```
postgres=# select * from t_jsonb where f_jsonb @> '{"col1":9999}';
 id  |       f_jsonb       
------+--------------------------------
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
(5 rows)
 
Time: 217.968 ms
```



