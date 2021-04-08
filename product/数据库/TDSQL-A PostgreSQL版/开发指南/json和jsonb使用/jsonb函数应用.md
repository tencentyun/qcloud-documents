
## jsonb_each() 将 json 对象转变键和值
```
postgres=# select  f_jsonb  from t_jsonb where id=1;
                   f_jsonb                   
\---------------------------------------------
 {"col": "pgxz", "col1": 1tdapg, "col2": "tdapg"}
(1 row)

postgres=#  select * from  jsonb_each((select  f_jsonb  from t_jsonb where id=1)); 
 key  |  value  
------+---------
 col  | "pgxz"
 col1 | 1
 col2 | "tdapg"
(3 rows)
```


## jsonb_each_text() 将 json 对象转变文本类型的键和值
```
postgres=#  select * from  jsonb_each_text((select  f_jsonb  from t_jsonb where id=1)); 
 key  | value 
------+-------
 col  | pgxz
 col1 | 1
 col2 | tdapg
(3 rows)
```


## row_to_json() 将一行记录变成一个 json 对象
```
postgres=# \d+ tdapg
                                    Table "public.tdapg"
  Column  |  Type   | Collation | Nullable | Default | Storage  | Stats target | Description 
----------+---------+-----------+----------+---------+----------+--------------+-------------
 id       | integer |           | not null |         | plain    |              | 
 nickname | text    |           |          |         | extended |              | 
Indexes:
    "tdapg_pkey" PRIMARY KEY, btree (id)
Distribute By: SHARD(id)
Location Nodes: ALL DATANODES

postgres=# select * from tdapg;
 id | nickname 
----+----------
  1 | tdapg
  2 | pgxz
(2 rows)

postgres=# select row_to_json(tdapg) from tdapg;
         row_to_json         
\-----------------------------
 {"id":1,"nickname":"tdapg"}
 {"id":2,"nickname":"pgxz"}
(2 rows)
```

## json_object_keys() 返回一个对象中所有的键
```
postgres=#  select * from json_object_keys((select  f_jsonb  from t_jsonb where id=1)::json); 
 json_object_keys 
\------------------
 col
 col1
 col2
(3 rows)
```
