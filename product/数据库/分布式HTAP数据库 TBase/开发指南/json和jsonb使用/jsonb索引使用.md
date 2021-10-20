TDSQL PostgreSQL版 为文档 jsonb 提供了 GIN 索引，GIN 索引在大量 jsonb 文档（数据）中，可有效地用来搜索出现的键或者键值对。

## 创建 jsonb 索引
```
postgres=# create index t_jsonb_f_jsonb_idx on t_jsonb using gin(f_jsonb);
CREATE INDEX

postgres=# \d+ t_jsonb
                                   Table "public.t_jsonb"
 Column  |  Type   | Collation | Nullable | Default | Storage  | Stats target | Description 
---------+---------+-----------+----------+---------+----------+--------------+-------------
 id      | integer |           |          |         | plain    |              | 
 f_jsonb | jsonb   |           |          |         | extended |              | 
Indexes:
    "t_jsonb_f_jsonb_idx" gin (f_jsonb)
Distribute By: SHARD(id)
Location Nodes: ALL DATANODES
```


## 测试查询的性能
```
postgres=# select count(1) from t_jsonb;
  count   
\----------
 10000000
(1 row)

postgres=# analyze t_jsonb;
ANALYZE
```

 
**没有索引开销**
```
postgres=# select * from t_jsonb where f_jsonb @> '{"col1":9999}';
  id  |            f_jsonb             
------+--------------------------------
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
(5 rows)

Time: 2473.488 ms (00:02.473)
```
 

**有索引开销**
```
postgres=# select * from t_jsonb where f_jsonb @> '{"col1":9999}';
  id  |            f_jsonb             
------+--------------------------------
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
 9999 | {"col1": 9999, "col2": "9999"}
(5 rows)

Time: 217.968 ms
```
 
