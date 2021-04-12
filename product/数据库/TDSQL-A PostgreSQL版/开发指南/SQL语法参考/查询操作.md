**按某一列排序**
```
postgres=# DROP TABLE if exists tdapg;
DROP TABLE
postgres=#  CREATE TABLE tdapg (id int, nickname text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO tdapg (nickname) VALUES('tdapg数据库好');              
INSERT 0 1
postgres=# INSERT INTO tdapg (id,nickname) VALUES(1,'tdapg数据库的时代来了');       
INSERT 0 1
postgres=# INSERT INTO tdapg (id,nickname) VALUES(2,'hello tdapg '); 
INSERT 0 1
postgres=# SELECT * FROM tdapg ORDER BY id;
 id |    nickname    
----+-----------------------
 1 | tdapg 数据库的时代来了
 2 | hello tdapg 
  | tdapg 数据库好
(3 rows)
```

**随机排序**
```
postgres=# SELECT * FROM tdapg ORDER BY random();
 id |    nickname    
----+-----------------------
 1 | tdapg 数据库的时代来了
  | tdapg 数据库好
 2 | hello tdapg 
(3 rows)
```

**计算排序**
```
postgres=# SELECT * FROM tdapg ORDER BY md5(nickname);
 id |    nickname    
----+-----------------------
 2 | hello tdapg 
  | tdapg数据库好
 1 | tdapg数据库的时代来了
(3 rows)
```

**子查询排序**
```
postgres=# SELECT * FROM tdapg ORDER BY (SELECT id FROM tdapg ORDER BY random() limit 1);
 id |    nickname    
----+-----------------------
 1 | tdapg 数据库的时代来了
 2 | hello tdapg 
  | tdapg 数据库好
(3 rows)
```

**null 值排序结果处理**
```
postgres=# INSERT INTO tdapg VALUES(4,null);
INSERT 0 1
```

null 值记录排在最前面：
```
postgres=# SELECT * FROM tdapg ORDER BY nickname nulls first;
 id |    nickname    
----+-----------------------
 4 | 
 2 | hello tdapg 
 1 | tdapg 数据库的时代来了
  | tdapg 数据库好
(4 rows)
```

null 值记录排在最后：
```
postgres=# SELECT * FROM tdapg ORDER BY nickname nulls last; 
 id |    nickname    
----+-----------------------
 2 | hello tdapg 
 1 | tdapg 数据库的时代来了
  | tdapg 数据库好
 4 | 
(4 rows)
```

**按拼音排序**
```
postgres=# SELECT * FROM (VALUES ('张三'), ('李四'),('陈五')) t(myname) ORDER BY myname;               
 myname 
--------
 张三
 李四
 陈五
(3 rows)
```

如果不加处理，则按汉字的 utf8 编码进行排序，不符合使用习惯：
```
postgres=# SELECT * FROM (VALUES ('张三'), ('李四'),('陈五')) t(myname) ORDER BY convert(myname::bytea,'UTF-8','GBK');
 myname 
--------
 陈五
 李四
 张三
(3 rows)
```

使用 convert 函数实现汉字按拼音进行排序：
```
postgres=# SELECT * FROM (VALUES ('张三'), ('李四'),('陈五')) t(myname) ORDER BY convert_to(myname,'GBK');      
 myname 
--------
 陈五
 李四
 张三
(3 rows)
```

使用 convert_to 函数实现汉字按拼音进行排序：
```
postgres=# SELECT * FROM (VALUES ('张三'), ('李四'),('陈五')) t(myname) ORDER BY myname  collate "zh_CN.utf8";
 myname 
--------
 陈五
 李四
 张三
(3 rows)
```
通过指定排序规则 collact 来实现汉字按拼音进行排序。

## WHERE 条件使用
#### 单条件查询
```
postgres=# SELECT * FROM tdapg WHERE id=1;
 id |    nickname    
----+-----------------------
 1 | tdapg 数据库的时代来了
(1 row)
```

#### 多条件 and
```
postgres=# SELECT * FROM tdapg WHERE id=2 and nickname like '%h%';
 id | nickname  
----+-------------
 1 | hello tdapg
(1 row)
```

#### 多条件 or
```
postgres=# SELECT * FROM tdapg WHERE id=1 or nickname like '%h%';
 id |    nickname    
----+-----------------------
 1 | tdapg 数据库的时代来了
 2 | hello tdapg 
(2 rows)
```

#### ilike 不区分大小写匹配
```
postgres=# CREATE TABLE t_ilike(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO t_ilike VALUES(1,'tdapg'),(2,'tdapg');
COPY 2
postgres=# SELECT * FROM t_ilike WHERE mc ilike '%tb%';
 id | mc  
----+-------
 1 | tdapg
 2 | tdapg
(2 rows)
```

#### WHERE 条件也能支持子查询
```
postgres=# SELECT * FROM tdapg WHERE id=(SELECT (random()*2)::integer FROM tdapg ORDER BY random() limit 1); 
 id |    nickname    
----+-----------------------
 1 | tdapg数据库的时代来了
(1 row)

postgres=# SELECT * FROM tdapg WHERE id=(SELECT (random()*2)::integer FROM tdapg ORDER BY random() limit 1); 
 id | nickname 
----+----------
(0 rows)
```

#### null 值查询方法
```
postgres=# SELECT * FROM tdapg WHERE nickname is null;
 id | nickname 
----+----------
 4 | 
(1 row)

postgres=# SELECT * FROM tdapg WHERE nickname is not null;
 id |    nickname    
----+-----------------------
  | tdapg 数据库好
 1 | tdapg 数据库的时代来了
 2 | hello tdapg 
(3 rows)
```

#### exists 只要有记录返回就为真
```
postgres=# CREATE TABLE t_exists1(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE

postgres=# INSERT INTO t_exists1 VALUES(1,'tdapg'),(2,'tdapg'); 
COPY 2

postgres=# CREATE TABLE t_exists2(id int,mc text); 
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE

postgres=# INSERT INTO t_exists2 VALUES(1,'tdapg'),(1,'tdapg');
COPY 2

postgres=# SELECT * FROM t_exists1 WHERE exists(SELECT 1 FROM t_exists2 WHERE t_exists1.id=t_exists2.id) ;
 id | mc  
----+-------
 1 | tdapg
(1 row)
```

#### exists 等价写法
```
postgres=# SELECT t_exists1.* FROM t_exists1,(SELECT distinct id FROM t_exists2) as t WHERE t_exists1.id=t.id;
 id | mc  
----+-------
 1 | tdapg
(1 row)
```

## 分页查询
默认从第一条开始，返回一条记录：
```
postgres=# SELECT * FROM tdapg limit 1;
 id |  nickname  
----+---------------
  | tdapg 数据库好
(1 row)
```

使用 offset 指定从第几条开始，0表示第一条开如，返回1条记录：
```
postgres=# SELECT * FROM tdapg limit 1 offset 0; 
 id | nickname  
----+-------------
 1 | hello tdapg
(1 row)
```

从第3条开始，返回二条记录：
```
postgres=# SELECT * FROM tdapg limit 1 offset 2;
 id |  nickname  
----+--------------
 2 | hello tdapg 
(1 row)
```

ORDER BY 可以获得一个有序的结果：
```
postgres=# SELECT * FROM tdapg ORDER BY id limit 1 offset 2;
 id | nickname 
----+----------
 4 | 
(1 row)
```

## 合并多个查询结果
#### 不过滤重复的记录
```
postgres=# create table u1(a int,b varchar)with(orientation=column);
CREATE TABLE
postgres=# create table u2(a int,b varchar)with(orientation=column);
CREATE TABLE
postgres=# insert into u1 values(1,'hi'),(2,'hello');
COPY 2
postgres=# insert into u2 values(1,'hi'),(2,'hello'),(3,'nihao');
COPY 3
postgres=# select * from u1 union all select * from u2 order by 1;
 a |  b  
---+-------
 1 | hi
 1 | hi
 2 | hello
 2 | hello
 3 | nihao
(5 rows)
```

#### 过滤重复的记录
```
postgres=# select * from u1 union select * from u2 order by 1;
 a |  b  
---+-------
 1 | hi
 2 | hello
 3 | nihao
(3 rows)
```

#### 每个子查询分布在合并结果中的使用
```
postgres=# SELECT * FROM ( SELECT * FROM tdapg limit 1) as t union all SELECT * FROM (SELECT * FROM t_appoint_col limit 1) as t ; 
 id |  nickname  
----+---------------
  | tdapg 数据库好
 2 | hello tdapg
(2 rows)
```

## 返回两个结果的交集
```
postgres=# CREATE TABLE t_intersect1(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO t_intersect1 VALUES(1,'tdapg'),(2,'tdapg');
COPY 2
postgres=# CREATE TABLE t_intersect2(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO t_intersect2 VALUES(1,'tdapg'),(3,'tdapg');
COPY 2
postgres=# SELECT * FROM t_intersect1 INTERSECT SELECT * FROM t_intersect2;
 id | mc  
----+-------
 1 | tdapg
(1 row)
```

## 返回两个结果的差集
```
postgres=# CREATE TABLE t_except1(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO t_except1 VALUES(1,'tdapg'),(2,'tdapg');
COPY 2
postgres=# CREATE TABLE t_except2(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO t_except2 VALUES(1,'tdapg'),(3,'tdapg');
COPY 2
postgres=# SELECT * FROM t_except1 except SELECT * FROM t_except2;
 id | mc  
----+-------
 2 | tdapg
(1 row)
```

## 多表关联
#### 内连接
```
postgres=# SELECT * FROM tdapg inner join t_appoint_col on tdapg.id=t_appoint_col.id;
 id |  nickname  | id | nickname 
----+--------------+----+-------------
 2 | hello tdapg | 2 | hello tdapg
(1 row)
```

#### 左外连接
```
postgres=# SELECT * FROM tdapg left join t_appoint_col on tdapg.id=t_appoint_col.id;
 id |    nickname    | id |  nickname 
----+-----------------------+----+-------------
  | tdapg 数据库好     |  | 
 1 | tdapg 数据库的时代来了 |  | 
 2 | hello tdapg      | 2 | hello tdapg
 4 |            |  | 
(4 rows)
```

#### 右外连接
```
postgres=# SELECT * FROM tdapg right join t_appoint_col on tdapg.id=t_appoint_col.id; 
 id |  nickname  | id | nickname 
----+--------------+----+-------------
 2 | hello tdapg | 2 | hello tdapg
(1 row)
```

#### 全连接
```
postgres=# SELECT * FROM tdapg full join t_appoint_col on tdapg.id=t_appoint_col.id;
 id |    nickname    | id | nickname 
----+-----------------------+----+-------------
  | tdapg 数据库好     |  | 
 1 | tdapg 数据库的时代来了 |  | 
 2 | hello tdapg      | 2 | hello tdapg
 4 |            |  | 
(4 rows)
```
