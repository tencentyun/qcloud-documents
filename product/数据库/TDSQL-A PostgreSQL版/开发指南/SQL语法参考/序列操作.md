
## 序列创建
### 建立序列
```
postgres=# CREATE SEQUENCE tdapg_seq;
CREATE SEQUENCE
```

建立序列，不存在时才创建：
```
postgres=# CREATE SEQUENCE IF NOT EXISTS tdapg_seq; 
NOTICE: relation "tdapg_seq" already exists, skipping
CREATE SEQUENCE
```

### 查看序列当前的使用状况
```
postgres=# \x 
Expanded display is on.
postgres=# SELECT * FROM tdapg_seq ;
-[ RECORD 1 ]-
last_value | 1
log_cnt  | 0
is_called | f
```

### 获取序列的下一个值
```
postgres=# SELECT nextval('tdapg_seq');
-[ RECORD 1 ]
nextval | 1
```

### 获取序列的当前值
需要在访问 nextval() 后才能使用：
```
postgres=# SELECT currval('tdapg_seq');
-[ RECORD 1 ]
currval | 1
```

也可以下面的方式来获取序列当前使用到那一个值：
```
postgres=# SELECT last_value FROM tdapg_seq ;
-[ RECORD 1 ]-
last_value | 1
```

### 设置序列当前值
```
postgres=# SELECT setval('tdapg_seq',1);
-[ RECORD 1 ]
setval | 1
postgres=# \x
Expanded display is off.
```

## 序列使用
```
postgres=# CREATE TABLE t (id int, nickname text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO t (id,nickname) VALUES(nextval('tdapg_seq'),'tdapg好');  
INSERT 0 1
postgres=# SELECT * FROM t;
 id | nickname 
----+----------
 2 | tdapg好
(1 row)
```

#### 序列作为字段的默认值使用
```
postgres=# ALTER TABLE t alter column id set default nextval('tdapg_seq');
postgres=# INSERT INTO t (nickname) VALUES('hello tdapg');                     
INSERT 0 1
postgres=# SELECT * FROM t;
 id | nickname  
----+-------------
 3 | hello tdapg
 2 | tdapg好
(2 rows)
```

#### 序列作为字段类型使用
```
postgres=# DROP TABLE t;
DROP TABLE
postgres=# CREATE TABLE t (id serial not null,nickname text);
CREATE TABLE
postgres=# INSERT INTO t (nickname) VALUES('hello tdapg');  
INSERT 0 1
postgres=# SELECT * FROM t;
 id | nickname  
----+-------------
 1 | hello tdapg
(1 row)
```

## 序列删除
```
postgres=# DROP SEQUENCE tdapg_seq;
DROP SEQUENCE
```

删除序列，不存在时跳过：
```
postgres=# DROP SEQUENCE IF EXISTS tdapg_seq;  
NOTICE: sequence "tdapg_seq" does not exist, skipping
DROP SEQUENCE
```
