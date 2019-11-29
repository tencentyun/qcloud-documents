## 创建 jsonb 类型字段表
```
postgres=# create table t_jsonb(id int,f_jsonb jsonb);
NOTICE:  Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# 
```


## 插入数据
```
postgres=# insert into t_jsonb values(1,'{"col1":1,"col2":"tbase"}');
INSERT 0 1
postgres=# insert into t_jsonb values(2,'{"col1":1,"col2":"tbase","col3":"pgxz"}');
INSERT 0 1

postgres=# select * from t_jsonb;
 id |                   f_jsonb                    
----+----------------------------------------------
  1 | {"col1": 1, "col2": "tbase"}
  2 | {"col1": 1, "col2": "tbase", "col3": "pgxz"}
(2 rows)
```


jsonb 插入时会移除重复的键，如下所示：
```
postgres=# insert into t_jsonb values(3,'{"col1":1,"col2":"tbase","col2":"pgxz"}');
INSERT 0 1
postgres=# select * from t_jsonb;
 id |                   f_jsonb                    
----+----------------------------------------------
  1 | {"col1": 1, "col2": "tbase"}
  3 | {"col1": 1, "col2": "pgxz"}
  2 | {"col1": 1, "col2": "tbase", "col3": "pgxz"}
(3 rows)
```
 
