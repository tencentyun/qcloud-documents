
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
 
## 更新数据
### 增加元素
```
postgres=# update t_jsonb set f_jsonb = f_jsonb || '{"col3":"pgxz"}'::jsonb where id=1;  
UPDATE 1
```

### 更新原来的元素
```
postgres=# update t_jsonb set f_jsonb = f_jsonb || '{"col2":"tbase"}'::jsonb where id=3;     
UPDATE 1

postgres=# select * from t_jsonb;
 id |                   f_jsonb                    
----+----------------------------------------------
  2 | {"col1": 1, "col2": "tbase", "col3": "pgxz"}
  1 | {"col1": 1, "col2": "tbase", "col3": "pgxz"}
  3 | {"col1": 1, "col2": "tbase"}
(3 rows)
```
 
### 删除某个键
```
postgres=# update t_jsonb set f_jsonb = f_jsonb - 'col3';    
UPDATE 3

postgres=# select * from t_jsonb;
 id |           f_jsonb            
----+------------------------------
  2 | {"col1": 1, "col2": "tbase"}
  1 | {"col1": 1, "col2": "tbase"}
  3 | {"col1": 1, "col2": "tbase"}
(3 rows)
```

## jsonb_set() 函数更新数据
jsonb_set(target jsonb, path text[], new_value jsonb, [create_missing boolean]) 
说明：target 指要更新的数据源；path 指路径；new_value 指更新后的键值；create_missing 值为 true 表示如果键不存在则添加；create_missing 值为 false 表示如果键不存在则不添加。
```
postgres=# update t_jsonb set f_jsonb = jsonb_set( f_jsonb , '{col}' , '"pgxz"' , true ) where id=1;
UPDATE 1
postgres=# update t_jsonb set f_jsonb = jsonb_set( f_jsonb , '{col}' , '"pgxz"' , false ) where id=2;         
UPDATE 1
postgres=# update t_jsonb set f_jsonb = jsonb_set( f_jsonb , '{col2}' , '"pgxz"' , false ) where id=3;          
UPDATE 1
postgres=# select * from t_jsonb;
 id |                   f_jsonb                   
----+---------------------------------------------
  1 | {"col": "pgxz", "col1": 1, "col2": "tbase"}
  2 | {"col1": 1, "col2": "tbase"}
  3 | {"col1": 1, "col2": "pgxz"}
(3 rows)
```
 
