## 表创建
创建一个表，要用到 CREATE TABLE 命令。在这个命令中需要为新表至少指定一个名字、列的名字及数据类型。例如：
```
CREATE TABLE datatypetest (
  col1 integer,
  col2 character varying(20),
  col3 date,
  col4 jsonb,
  col5 smallint
) WITH (orientation='row');
```

### 指定表的储存方式
表的储存方式支持行存储和列存储。
ROW 行存储适合于 OLTP 业务，此类型的表上交互事务比较多，一次交互会涉及表中的多个列，用行存查询效率较高。
COLUMN 表示表的数据将以列式存储。列存储适合于数据仓库业务，此类型的表上会做大量的汇聚计算，且涉及的列操作较少。

#### 指定行存创建表
```
CREATE TABLE coltest1 (
  id integer NOT NULL,
   name character(16) NOT NULL,
  start_date date,
  subject character(1)
) WITH (orientation = 'row');
```

#### 指定列存创建表
```
CREATE TABLE coltest1 (
  id integer NOT NULL,
  name character(16) NOT NULL,
  start_date date,
  subject character(1)
) WITH (orientation = 'column');
```


### 指定资源组创建表
```
CREATE TABLE t3(id integer,nc text) with (orientation ='column') DISTRIBUTE BY shard (id) TO GROUP default_group;
```

#### 指定 schema 创建表
```
CREATE SCHEMA myschema;
CREATE TABLE myschema.t4(
  col1 integer,
  col2 char,
  col3 bigint,
  clo4 varchar(10)
) WITH (orientation ='column');
```

### 指定表列字段的压缩方式及压缩等级创建表
目前支持压缩方式 compress_method 包括（delta、zstd、zlib、rle、bitpack），compress_level 表示缩级别，压缩级别越大，压缩比越大，压缩时间越长，压缩级别越高越消耗 CPU。

轻量压缩为自研实现算法，包括 rle、delta、bitpack，他们均只有一种压缩级别，且只能压缩数值类型。
- rle 主要针对大量重复的数据，如11111122222333111111进行压缩。
- delta 主要针对递增或者递减的数据，如，固定的时间类型(今天明天后天)，或者数值类型12345678进行压缩。
- bitpack 针对数值比较小的数据，如，创建表的时候是 integer，但实际存储的数值只是1-100。

创建表的时候指定压缩类型，但是实际存储的时候有没有用到指定的压缩类型是会自动适应调整的，有写场景可能导致最终存储没有使用压缩，如压缩算法使用不当，如针对 text 类型使用 delta。

原表大小15GB：
```
CREATE TABLE coltest2 (
c1 int encoding(compress_method='delta'), 
c2 char(30), 
c3 float4 ENCODING(compress_method='zstd', compress_level=19), 
c4 date encoding(compress_method='zlib', compress_level=9),
c5 int encoding(compress_method='rle'),
c6 int encoding(compress_method='bitpack')
) WITH (orientation = 'column');
```
说明：
- delta 压缩，无压缩级别限制，压缩后大小14GB。
- zlib 压缩，压缩级别1-9，压缩级别为9时，压缩后大小4234MB。
- zstd 压缩，压缩级别1-19，压缩级别为19时，压缩后大小3691MB。
- rle 压缩，无压缩级别，压缩后大小14GB。
- bitpack 压缩，无压缩级别，压缩后大小14GB。

### 表的分布方式
复制表：表的每一行存在所有数据节点 DN 中，即每个数据节点都有完整的表数据。 
```
CREATE TABLE t_rep (id int,mc text) DISTRIBUTE BY REPLICATION TO GROUP default_group;
INSERT INTO t_rep(id,mc) VALUES 
(1,'ReplicationTableTest1'),(2,'ReplicationTableTest2'),(3,'ReplicationTableTest3');
```

shard 表：对指定的列进行 shard，把数据分布到指定 DN。不指定 shard key 建表方式，默认使用主键作为 shardkey，如果没有主键，则系统默认使用第一个字段作为表的 shard key。
```
CREATE TABLE t_shard(
  f1 bigserial not null,
  f2 integer,
  f3 text,
  f4 text, 
f5 date) WITH (orientation = 'column') 
DISTRIBUTE BY SHARD(f1) TO GROUP default_group;
```


### 继承表
#### 单表继承
```
CREATE TABLE cities(
  name      text,
  population   float,
  altitude    int
) WITH (orientation ='column');
CREATE TABLE capitals(
  state char(2)
) INHERITS (cities) WITH (orientation = 'column');
```

#### 插入数据
```
INSERT INTO cities VALUES('Las Vegas', 1.53, 2174);
INSERT INTO cities VALUES('Mariposa',3.30,1953);
INSERT INTO capitals VALUES('Madison',4.34,845,'WI');
```

#### 查询
```
SELECT name, altitude FROM cities WHERE altitude > 500;
SELECT name, altitude FROM capitals WHERE altitude > 500;
SELECT name,altitude FROM ONLY cities WHERE altitude > 500;
SELECT * FROM capitals;
```

### 多表继承
```
CREATE TABLE parent1 (FirstCol integer) WITH (orientation = 'column');
 CREATE TABLE parent2 (FirstCol integer, SecondCol varchar(20)) WITH (orientation = 'column');
 CREATE TABLE parent3 (FirstCol varchar(200)) WITH (orientation = 'column');
 --子表 child1 将同时继承自 parent1 和 parent2 表，而这两个父表中均包含 integer 类型的 FirstCol 字段，因此 child1 可以创建成功
 CREATE TABLE child1 (MyCol timestamp) INHERITS (parent1,parent2) WITH (orientation = 'column');
 --子表 child2 将不会创建成功，因为其两个父表中均包含 FirstCol 字段，但是它们的类型不相同
 CREATE TABLE child2 (MyCol timestamp) INHERITS (parent1,parent3) WITH (orientation = 'column');
 --子表 child3 同样不会创建成功，因为它和其父表均包含 FirstCol 字段，但是它们的类型不相同
 CREATE TABLE child3 (FirstCol varchar(20)) INHERITS(parent1) WITH (orientation = 'column');
```

### 使用IF NOT EXISTS
如果已经存在相同名称的表，不会抛出一个错误，而会发出一个通知，告知表关系已存在：
```
postgres=# CREATE TABLE t(id int,mc text);       
CREATE TABLE
postgres=# CREATE TABLE t(id int,mc text);
ERROR: relation "t" already exists
postgres=# CREATE TABLE IF NOT EXISTS t(id int,mc text);
NOTICE: relation "t" already exists, skipping
CREATE TABLE
postgres=# 
```

#### 指定模式创建表
```
postgres=# CREATE TABLE public.t1(id int,mc text);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE 
```

#### 使用查询结果创建数据表
```
postgres=# CREATE TABLE t(id int,mc text) DISTRIBUTE BY shard(mc);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# INSERT INTO t VALUES(1,'tdapg');
INSERT 0 1
postgres=# CREATE TABLE t_as as SELECT * FROM t;
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
INSERT 0 1
postgres=# SELECT * FROM t_as;
 id | mc  
----+-------
 1 | tdapg
(1 row)

postgres=# \d+ t
                   Table "tdapg.t"
 Column | Type  | Collation | Nullable | Default | Storage | Stats target | Description 
--------+---------+-----------+----------+---------+----------+--------------+-------------
 id   | integer |      |     |     | plain  |       | 
 mc   | text  |      |     |     | extended |       | 
DISTRIBUTE BY: SHARD(mc)
Location Nodes: ALL DATANODES

postgres=# \d+ t_as

                   Table "tdapg.t_as"
 Column | Type  | Collation | Nullable | Default | Storage | Stats target | Description 
--------+---------+-----------+----------+---------+----------+--------------+-------------
 id   | integer |      |      |     | plain  |       | 
 mc   | text  |      |     |     | extended |       | 
Distribute By: SHARD(id)
Location Nodes: ALL DATANODES
```

## 表修改
#### 创建表
```
CREATE TABLE t(
  col1 bigint,
  col2 char,
  col3 text,
  col4 varchar(5)
) WITH(ORIENTATION=column);

```

#### 增加列
```
ALTER TABLE t ADD column_name varchar(20);
```

#### 删除列
```
ALTER TABLE t DROP column_name;
```

#### 修改列名
```
ALTER TABLE t RENAME col2 TO col5;
```

#### 修改列的默认值
```
ALTER TABLE t ALTER col3 SET DEFAULT 'test';
```

#### 修改表名
```
ALTER TABLE t RENAME TO t1;
```

#### 修改列字段数据类型
```
ALTER TABLE t1 ALTER COLUMN col5 type TEXT;
```
目前列存模式下不支持修改列字段数据类型。

#### 添加主键
```
ALTER TABLE t1 ADD CONSTRAINT t_id_pkey PRIMARY KEY (col1) ;
```

#### 添加唯一约束
```
ALTER TABLE t1 ADD CONSTRAINT unique_t1_clo1 UNIQUE(col1);
```

#### 添加检查约束
```
ALTER TABLE t1 ADD CONSTRAINT t1_CONSTR_clo3 CHECK (col3 IS NOT NULL);
```


#### 外键创建
```
postgres=# CREATE TABLE t_p(f1 int not null,f2 int ,primary key(f1));
CREATE TABLE t_f(f1 int not null,f2 int );NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# CREATE TABLE t_f(f1 int not null,f2 int );
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# ALTER TABLE t_f ADD CONSTRAINT t_f_f1_fkey FOREIGN KEY (f1) REFERENCES t_p (f1);
ALTER TABLE
```
目前列存表不支持创建外键。

#### 删除外键
```
ALTER TABLE t_f DROP CONSTRAINT t_f_f1_fkey; 
```
外键只是同一个节点内约束有效果，所以外键字段和对应主键字段必需都是表的分布键，否则由于数据分布于不同的节点内会导致更新失败。

## 表删除
#### 删除当前模式下的数据表
```
CREATE TABLE t(
  col1 bigint
);

postgres=# DROP TABLE t;
DROP TABLE
```

#### 删除某个模式下数据表
```
postgres=# DROP TABLE public.t;
DROP TABLE
```

#### 删除数据表，不存在时不执行，不报错
```
postgres=# DROP TABLE IF EXISTS t;  
NOTICE: table "t" does not exist, skipping
DROP TABLE
```

#### 使用 CASCADE 无条件删除数据表
```
postgres=# CREATE SCHEMA if not exists tdapg_schema;
CREATE SCHEMA
postgres=# CREATE TABLE tdapg_schema.t1( col1 bigint);
NOTICE: Replica identity is needed for shard table, please add to this table through "alter table" command.
CREATE TABLE
postgres=# CREATE VIEW tdapg_schema.t1_view AS SELECT * FROM tdapg_schema.t1 ;
CREATE VIEW
postgres=# DROP TABLE tdapg_schema.t1 ;
ERROR: cannot DROP TABLE tdapg_schema.t1 because other objects depend on it
DETAIL: view tdapg_schema.t1_view depends on table tdapg_schema.t1
HINT: Use DROP ... CASCADE to drop the dependent objects too.

postgres=# DROP TABLE tdapg_schema.t1 CASCADE;
NOTICE: drop cascades to view tdapg_schema.t1_view
DROP TABLE
```

## 数据插入
#### 单条插入
```
postgres=# DROP TABLE IF EXISTS t6;
DROP TABLE
postgres=# CREATE TABLE t6(id int,mc text) WITH (ORIENTATION='column');
CREATE TABLE
postgres=# INSERT INTO t6 VALUES(1,'tdapg01');
INSERT 0 1
```

#### 批量插入
```
postgres=# INSERT INTO t6 VALUES(1,'tdapg01'),(1,'tdapg02');
COPY 2
```

#### 插入返回
```
postgres=# INSERT INTO t6 VALUES(1,'tdapg03') RETURNING id ;
 id 
----
 1
(1 row)

INSERT 0 1
```

## 数据更新
#### 更新语句
```
postgres=# DROP TABLE IF EXISTS t1;
DROP TABLE
postgres=# CREATE TABLE t1(name text, price integer, id serial) WITH (ORIENTATION ='column');
CREATE TABLE
postgres=# INSERT INTO t1(name, price) VALUES ('potato',4),('tomato',5),('chicken',20),('beef',50);
COPY 4
postgres=# UPDATE t1 SET price = price * 1.10 WHERE price <= 99.99;
UPDATE 4
```

#### 更新返回
```
postgres=# DROP TABLE IF EXISTS t1;
DROP TABLE
postgres=# CREATE TABLE t1(name text, price integer, id serial) WITH (ORIENTATION ='column');
CREATE TABLE
postgres=# insert into t1(name, price) values ('potato',4),('tomato',5),('chicken',20),('beef',50);
COPY 4
postgres=# UPDATE t1 SET price = price * 1.10 WHERE price <= 99.99 RETURNING name, price AS new_price;
 name  | new_price 
---------+-----------
 potato |     4
 tomato |     6
 beef  |    55
 chicken |    22
(4 rows)

UPDATE 4
```

## 数据删除
删除数据 delete 操作：
```
postgres=# DROP TABLE IF EXISTS t1;
DROP TABLE
CREATE TABLE t1(
  id integer,
  nickname text
) WITH (ORIENTATION ='column');
INSERT INTO t1(id,nickname) 
VALUES(1,'tdapgCTest1'),(2,'tdapgCTest2'),(3,'tdapgCTest3'),(33,'tdapgCTest3');
postgres=# DELETE FROM t1 WHERE id=1;
DELETE 1
```

## 数据清空
TRUNCATE 功能用于对表数据进行快速清除，TRUNCAT E属于 DDL 级别，会给 TRUNCATE 表加上 ACCESS EXCLUSIVE 最高级别的锁。

### truncate 普通表
```
postgres=# TRUNCATE TABLE t1;
TRUNCATE TABLE
\#也可以一次truncate多个数据表
postgres=# TRUNCATE TABLE t1,t6;
TRUNCATE TABLE
postgres=# 
```

### truncate 分区表
truncate 一个时间分区表：
```
CREATE TABLE t_time_range(
 f1 bigint, 
f2 timestamp,f3 varchar(20))
PARTITION BY range (f2) begin (timestamp without time zone '2017-09-01 0:0:0') 
step (interval '1 month') 
PARTITIONS (12)
 WITH (orientation = 'column') ;
postgres=# INSERT INTO t_time_range VALUES(1,'2017-09-01','tdapg');
INSERT 0 1
postgres=# INSERT INTO t_time_range VALUES(2,'2017-10-01','pgxz');
INSERT 0 1
postgres=# \d+ t_time_range
                           Column oriented table "public.t_time_range"
 Column |      Type       | TC method | TC level | LWC method | Collation | Nullable | Default | Storage | Stats target | Description 
--------+-----------------------------+-------------+----------+-------------+-----------+----------+---------+----------+--------------+-------------
 f1   | bigint           | no compress |     | no compress |      |     |     | plain  |       | 
 f2   | timestamp without time zone | no compress |     | no compress |      |     |     | plain  |       | 
 f3   | character varying(20)    | no compress |     | no compress |      |     |     | extended |       | 
Distribute By: SHARD(f1)
Location Nodes: ALL DATANODES
PARTITION BY: RANGE(f2)
     \# Of Partitions: 12
     Start With: 2017-09-01
     Interval Of Partition: 1 MONTH
Options: orientation=column

postgres=# SELECT * FROM t_time_range;
 f1 |     f2     | f3  
----+---------------------+-------
 1 | 2017-09-01 00:00:00 | tdapg
 2 | 2017-10-01 00:00:00 | pgxz
(2 rows)

postgres=# TRUNCATE t_time_range partition for ('2017-09-01' ::timestamp without time zone);
TRUNCATE TABLE
postgres=# SELECT * FROM t_time_range;
 f1 |     f2     | f3 
----+---------------------+------
 2 | 2017-10-01 00:00:00 | pgxz
(1 row)
```

truncate 一个数值范围分区表：
```
CREATE TABLE t_range(
   f1 bigint,
   f2 timestamp default now(),
   f3 integer
 ) PARTITION BY range (f3) begin (1) step (50) partitions (3) WITH (orientation = 'column') DISTRIBUTE BY shard(f1) TO GROUP default_group;
INSERT INTO t_range(f1,f3) VALUES (1,1);
 INSERT INTO t_range(f1,f3) VALUES(2,50);
 INSERT INTO t_range(f1,f3) VALUES(2,110);
 INSERT INTO t_range(f1,f3) VALUES(3,100);

postgres=# \d+ t_range
                            Column oriented table "public.t_range"
 Column |      Type       | TC method | TC level | LWC method | Collation | Nullable | Default | Storage | Stats target | Description 
--------+-----------------------------+-------------+----------+-------------+-----------+----------+---------+---------+--------------+-------------
 f1   | bigint           | no compress |     | no compress |      |     |     | plain  |       | 
 f2   | timestamp without time zone | no compress |     | no compress |      |     | now()  | plain  |       | 
 f3   | integer           | no compress |     | no compress |      |     |     | plain  |       | 
Distribute By: SHARD(f1)
Location Nodes: ALL DATANODES
PARTITION BY: RANGE(f3)
     \# Of Partitions: 3
     Start With: 1
     Interval Of Partition: 50
Options: orientation=column

postgres=# SELECT * FROM t_range ;
 f1 |       f2       | f3 
----+----------------------------+-----
 3 | 2021-01-19 19:47:31.060817 | 100
 1 | 2021-01-19 19:47:30.258023 |  1
 2 | 2021-01-19 19:47:30.37273 | 50
 2 | 2021-01-19 19:47:30.387583 | 110
(4 rows)

postgres=# TRUNCATE t_range partition for (1);  
TRUNCATE TABLE
postgres=# SELECT * FROM t_range ;
 f1 |       f2       | f3 
----+----------------------------+-----
 3 | 2021-01-19 19:47:31.060817 | 100
 2 | 2021-01-19 19:47:30.387583 | 110
(2 rows)
postgres=#
```

## 空间回收
数据库操作中，那些已经被 DELETE 的行并没有做物理删除，在完成 VACUUM 之前，这部分垃圾数据依然存在，所以如果对表进行了大量的更新或删除行，会产生大量磁盘页面碎片，降低查询效率，此时应运行 VACUUM FULL 命令来清理垃圾数据回收空间。

示例：
建表导数后，并对全表数据做delete删除，此时表大小不变，垃圾数据只是逻辑上做了删除：
```
postgres=# CREATE TABLE vacuum_test(a INT,b VARCHAR) WITH(ORIENTATION=column);
CREATE TABLE
postgres=# INSERT INTO vacuum_test VALUES(generate_series(1,10000),'hello world');
INSERT 0 10000
postgres=# DELETE FROM vacuum_test;
DELETE 10000
postgres=# \dt+ vacuum_test
               List of relations
 Schema |  Name   | Type | Owner | Size | Allocated Size | Description 
--------+-------------+-------+-------+--------+----------------+-------------
 public | vacuum_test | table | dbadmin | 144 MB | 144 MB     | 
(1 row)
```

列存表需要连接各个 DN 来执行 VACUUM 操作：
```
postgres=# EXECUTE DIRECT ON(dn001) 'VACUUM FULL vacuum_test;';
EXECUTE DIRECT
postgres=# EXECUTE DIRECT ON(dn002) 'VACUUM FULL vacuum_test;';
EXECUTE DIRECT
postgres=# EXECUTE DIRECT ON(dn003) 'VACUUM FULL vacuum_test;';
EXECUTE DIRECT
postgres=# EXECUTE DIRECT ON(dn004) 'VACUUM FULL vacuum_test;';
EXECUTE DIRECT
postgres=# EXECUTE DIRECT ON(dn005) 'VACUUM FULL vacuum_test;';
EXECUTE DIRECT
postgres=# EXECUTE DIRECT ON(dn006) 'VACUUM FULL vacuum_test;';
EXECUTE DIRECT
postgres=# \dt+ vacuum_test
                List of relations
 Schema |  Name   | Type | Owner | Size  | Allocated Size | Description 
--------+-------------+-------+-------+---------+----------------+-------------
 public | vacuum_test | table | dbadmin | 0 bytes | 0 bytes    | 
(1 row)
```
VACUUM FULL 操作完成后，表中垃圾数据被清理，空间回收。
除 VACUUM 之外，系统自动清理进程（autovacuum）会自动执行 VACUUM 命令，回收被标识为删除状态的记录空间。
