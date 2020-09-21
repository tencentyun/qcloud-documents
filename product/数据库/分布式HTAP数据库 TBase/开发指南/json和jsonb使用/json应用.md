
## 创建 json 类型字段表
```
postgres=# create table t_json(id int,f_json json);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
```


## 插入数据
```
postgres=# insert into t_json values(1,'{"col1":1,"col2":"tbase"}');
INSERT 0 1
postgres=# insert into t_json values(2,'{"col1":1,"col2":"tbase","col3":"pgxz"}');
INSERT 0 1
postgres=# select * from t_json;
 id |                 f_json                  
----+-----------------------------------------
  1 | {"col1":1,"col2":"tbase"}
  2 | {"col1":1,"col2":"tbase","col3":"pgxz"}
(2 rows)
```


## 通过键获得 json 对象域

```
postgres=# select f_json ->'col2' as col2 ,f_json -> 'col3' as col3 from t_json;  
  col2   |  col3  
---------+--------
 "tbase" | 
 "tbase" | "pgxz"
(2 rows)
```


## 以文本形式获取对象值

```
postgres=# select f_json ->>'col2' as col2 ,f_json ->> 'col3' as col3 from t_json;
 col2  | col3 
-------+------
 tbase | 
 tbase | pgxz
(2 rows)

postgres=# select f_json ->>'col2' as col2 ,f_json ->> 'col3' as col3 from t_json where f_json ->> 'col3' is not null;
 col2  | col3 
-------+------
 tbase | pgxz
(1 row)
```
