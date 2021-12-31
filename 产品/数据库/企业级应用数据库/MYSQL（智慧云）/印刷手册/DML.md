本节主要介绍 DML 语句中常用的Select（查询）、Insert（插入）、Replace（替换）、Update（更新）及Delete（删除）指令。
## SELECT
### 基础查询语法

```
SELECT
    [ALL | DISTINCT | DISTINCTROW ]
    select_expr [, select_expr] ...
    [FROM table_references
      [PARTITION partition_list]]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
    [HAVING where_condition]
    [ORDER BY {col_name | expr | position}
      [ASC | DESC], ... [WITH ROLLUP]]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [FOR {UPDATE | SHARE}
        [OF tbl_name [, tbl_name] ...]
        [NOWAIT | SKIP LOCKED]
      | LOCK IN SHARE MODE]
```
**示例：**
```
drop table if exists test1;
create table test1 ( a int key, b int, c char(20) ) shardkey=a;
drop table if exists test2;
create table test2 ( a int key, d int, e char(20) ) shardkey=a;

insert into test1 (a,b,c) values(1,2,"record1"),(2,3,"record2");
insert into test2 (a,d,e) values(1,3,"test2_record1"),(2,3,"test2_record2");

select t1.a,t1.b,t1.c,t2.a,t2.d,t2.e  from test1 t1 join test2 t2 on t1.b=t2.d;


select t1.a,t1.b,t1.c from test1 t1 where t1.a in (select a from test2);

select t1.a,t1.b,t1.c from test1 t1  where exists (select t2.a,t2.d,t2.e  from test2 t2 where t2.a=t1.b);

select t1.a, count(1) from test1 t1 where exists (select t2.a,t2.d,t2.e from test2 t2 where t2.a=t1.a) group by t1.a;


select distinct count(1) from test1 t1 where exists (select t2.a,t2.d,t2.e from test2 t2 where t2.a=t1.a) group by t1.a;

select count(distinct t1.a) from test1 t1 where exists (select t2.a,t2.d,t2.e from test2 t2 where t2.a=t1.a);
```

### join
TDSQL支持对 SELECT 语句和多表 DELETE 和 UPDATE 操作的join。
#### 分表间join示例
如果分表之间带有分表键相等的条件，则相当于单机Join。
**示例：**
```
--构建两张测试表：
DROP TABLE IF EXISTS `test_join_shard_table1`;
CREATE TABLE `test_join_shard_table1` (
  `id` int(10) NOT NULL,
  `b` varchar(10)  NOT NULL DEFAULT '',
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;
INSERT INTO test_join_shard_table1 (id, b, c) VALUES 
    (1,"test1",1), (2,"test2",2), (3,"test3",3),
    (4,"test4",4), (5,"test5",5), (6,"test6",6),
(7,"test7",7), (8,"test8",8), (9,"testX",11);

DROP TABLE IF EXISTS `test_join_shard_table2`;
CREATE TABLE `test_join_shard_table2` (
  `id` int(10) NOT NULL,
  `d` datetime,
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT  CHARSET=utf8  COLLATE=utf8_bin shardkey=id;
INSERT INTO test_join_shard_table2 (id, d, c) VALUES 
    (1,NOW(),1), (2,NOW(),2), (3,NOW(),3),
    (4,NOW(),4), (5,NOW(),5), (6,NOW(),6),
(7,NOW(),7), (8,NOW(),8), (9,NOW(),10);

--检查分布式测试表的数据分布情况：
/*sets:allsets*/  select * from test_join_shard_table1;
/*sets:allsets*/  select * from test_join_shard_table2;

--执行带INNER JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
INNER JOIN test_join_shard_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带LEFT JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME
FROM test_join_shard_table1 test1
LEFT JOIN test_join_shard_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带RIGHT JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
RIGHT JOIN test_join_shard_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带FULL JOIN的SELECT查询语句，笛卡尔积
SELECT test1.id, test1.b AS NAME, test2.d AS TIME
FROM test_join_shard_table1 test1
CROSS JOIN test_join_shard_table2 test2
ORDER BY NAME;
```
#### 分表和广播表join示例
跨分片的分表与广播表，效果相当于单机 Join。
**示例：**
```
--构建两张测试表：
DROP TABLE IF EXISTS `test_join_shard_table1`;
CREATE TABLE `test_join_shard_table1` (
  `id` int(10) NOT NULL,
  `b` varchar(10)  NOT NULL DEFAULT '',
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;
INSERT INTO test_join_shard_table1 (id, b, c) VALUES
    (1,"test1",1), (2,"test2",2), (3,"test3",3),
    (4,"test4",4), (5,"test5",5), (6,"test6",6),
(7,"test7",7), (8,"test8",8), (9,"testX",11);

DROP TABLE IF EXISTS `test_join_group_table2`;
CREATE TABLE `test_join_group_table2` (
  `id` int(10) NOT NULL,
  `d` datetime,
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT  CHARSET=utf8  COLLATE=utf8_bin shardkey=noshardkey_allset;
INSERT INTO test_join_group_table2 (id, d, c) VALUES
    (1,NOW(),1), (2,NOW(),2), (3,NOW(),3),
    (4,NOW(),4), (5,NOW(),5), (6,NOW(),6),
(7,NOW(),7), (8,NOW(),8), (9,NOW(),10);

--检查分布式测试表的数据分布情况：
/*sets:allsets*/  select * from test_join_shard_table1;
/*sets:allsets*/  select * from test_join_group_table2;

--执行带INNER JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME
FROM test_join_shard_table1 test1 
INNER JOIN test_join_group_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带LEFT JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME
FROM test_join_shard_table1 test1
LEFT JOIN test_join_group_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带RIGHT JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
RIGHT JOIN test_join_group_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带FULL JOIN的SELECT查询语句，笛卡尔积
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
CROSS JOIN test_join_group_table2 test2 
ORDER BY NAME;
```
#### 分表和单表join示例
**示例：**
```
--构建两张测试表：
DROP TABLE IF EXISTS `test_join_shard_table1`;
CREATE TABLE `test_join_shard_table1` (
  `id` int(10) NOT NULL,
  `b` varchar(10)  NOT NULL DEFAULT '',
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;
INSERT INTO test_join_shard_table1 (id, b, c) VALUES 
    (1,"test1",1), (2,"test2",2), (3,"test3",3),
    (4,"test4",4), (5,"test5",5), (6,"test6",6),
(7,"test7",7), (8,"test8",8), (9,"testX",11);

DROP TABLE IF EXISTS `test_join_noshard_table2`;
CREATE TABLE `test_join_noshard_table2` (
  `id` int(10) NOT NULL,
  `d` datetime,
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
INSERT INTO test_join_noshard_table2 (id, d, c) VALUES 
    (1,NOW(),1), (2,NOW(),2), (3,NOW(),3),
    (4,NOW(),4), (5,NOW(),5), (6,NOW(),6),
    (7,NOW(),7), (8,NOW(),8), (9,NOW(),10);

--检查分布式测试表的数据分布情况：
/*sets:allsets*/ select * from test_join_shard_table1;
--检查单片表的数据：
select * from test_join_noshard_table2;

--执行带INNER JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
INNER JOIN test_join_noshard_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带LEFT JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
LEFT JOIN test_join_noshard_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带RIGHT JOIN的SELECT查询语句
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
RIGHT JOIN test_join_noshard_table2 test2 
ON test1.c=test2.c
ORDER BY NAME;

--执行带FULL JOIN的SELECT查询语句，笛卡尔积
SELECT test1.id, test1.b AS NAME, test2.d AS TIME 
FROM test_join_shard_table1 test1 
CROSS JOIN test_join_noshard_table2 test2
ORDER BY NAME;
```
#### 跨分片update/delete join示例
**示例：**
```
--创建测试表：
DROP TABLE IF EXISTS `test_join_shard_table1`;
CREATE TABLE `test_join_shard_table1` (
  `id` int(10) NOT NULL,
  `b` varchar(10)  NOT NULL DEFAULT '',
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;
INSERT INTO test_join_shard_table1 (id, b, c) VALUES
    (1,"test1",1), (2,"test2",2), (3,"test3",3),
    (4,"test4",4), (5,"test5",5), (6,"test6",6),
(7,"test7",7), (8,"test8",8), (9,"testX",11);

DROP TABLE IF EXISTS `test_join_shard_table2`;
CREATE TABLE `test_join_shard_table2` (
  `id` int(10) NOT NULL,
  `d` datetime,
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;
INSERT INTO test_join_shard_table2 (id, d, c) VALUES
    (1,NOW(),1), (2,NOW(),2), (3,NOW(),3),
    (4,NOW(),4), (5,NOW(),5), (6,NOW(),6),
(7,NOW(),7), (8,NOW(),8), (9,NOW(),10);

--检测分布式测试表的数据分布情况
/*sets:allsets*/  select * from test_join_shard_table1;
/*sets:allsets*/  select * from test_join_shard_table2;

--UPDATE…JOIN…ON…SET语句，单字段：
UPDATE test_join_shard_table1 test1 
INNER JOIN test_join_shard_table2 test2 
ON test1.c=test2.c SET test1.b="TEXTXXXXX" 
WHERE test1.id>7;
SELECT * FROM test_join_shard_table1;

--UPDATE…JOIN…ON…SET语句，同一表多字段
UPDATE test_join_shard_table1 test1 
INNER JOIN test_join_shard_table2 test2 
ON test1.c=test2.c 
SET test1.b="TEXTSSSS", test1.c=88
WHERE test1.id>7;
SELECT * FROM test_join_shard_table1;

--DELETE…FROM…JOIN…ON语句
DELETE test1 FROM test_join_shard_table1 test1 
INNER JOIN test_join_shard_table2 test2 
ON test1.c=test2.c 
WHERE test1.id>7;
SELECT * FROM test_join_shard_table1;
```
### union语法
UNION 将来自多个 SELECT 语句的结果组合到一个结果集中。
语法如下：
```
SELECT ...
UNION [ALL | DISTINCT] SELECT ...
[UNION [ALL | DISTINCT] SELECT ...]
```
>!
- 参与UNION的表所select的列的个数需要保持一致。
- UNION 结果集的列名取自第一个 SELECT 语句的列名。

示例：
```
DROP TABLE IF EXISTS t1;
create table t1 (a int primary key, b int) shardkey=a;
DROP TABLE IF EXISTS t2;
create table t2 (a int primary key, b int) shardkey=a;
select * from t1 where t1.a in (select a from t2) union select * from t2 where t2.a>22;
```
各种表的组合场景：
```
分表：
DROP TABLE IF EXISTS s1;
create table s1 (a int primary key, b int) shardkey=a;
DROP TABLE IF EXISTS s2;
create table s2 (a int primary key, b int) shardkey=a;
单表：
DROP TABLE IF EXISTS ns1;
create table ns1 (a int primary key, b int);
DROP TABLE IF EXISTS ns2;
create table ns2 (a int primary key, b int);
广播表：
DROP TABLE IF EXISTS g1;
create table g1 (a int primary key, b int) shardkey=noshardkey_allset;
DROP TABLE IF EXISTS g2;
create table g2 (a int primary key, b int) shardkey=noshardkey_allset;
二级分区表：
DROP TABLE IF EXISTS p1;
create table p1 (a int, b int, PRIMARY KEY(a)) shardkey=a PARTITION BY range (b) (PARTITION p0 values less than (100), PARTITION p1 values less than (200));
DROP TABLE IF EXISTS p2;
create table p2 (a int, b int, PRIMARY KEY(a)) shardkey=a PARTITION BY range (b) (PARTITION p0 values less than (100), PARTITION p1 values less than (200));

各种类型表之间的union
select * from s1 union select * from s2;
select * from ns1 union select * from ns2;
select * from g1 union select * from g2;
select * from s1 union select * from ns1;
select * from p1 union select * from p2;
select * from s1 where not exists (select * from s2 where s2.a=s1.a order by s2.a) or b<10 union select * from s2 where s2.a>22;
select a, sum(b) from s1 group by a union select * from s2;
select a, sum(b) from s1 union select * from s2;
select distinct(a) from s1 union select a from s2;
select distinct(a), b from s1 union select a,b from s2;
```
### 子查询
语法如下：
```
SELECT ...
FROM table
WHERE expr operator
(SELECT select_list FROM table)
```
>!一般情况下，由于子查询效率不高，尽量使用join的代替子查询

示例：
```
DROP TABLE if exists `test_shard_table1`;
CREATE TABLE `test_shard_table1` (
  `id` int(10) NOT NULL,
  `b` varchar(10)  NOT NULL DEFAULT '',
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin shardkey=id;
INSERT INTO test_shard_table1 (id, b, c) VALUES 
    (1,"test1",1), (2,"test2",2), (3,"test3",3),
    (4,"test4",4), (5,"test5",5), (6,"test6",6),
(7,"test7",7), (8,"test8",8), (9,"testX",11);

DROP TABLE if exists `test_shard_table2`;
CREATE TABLE `test_shard_table2` (
  `id` int(10) NOT NULL,
  `d` datetime,
  `c` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT  CHARSET=utf8  COLLATE=utf8_bin shardkey=id;
INSERT INTO test_shard_table2 (id, d, c) VALUES
    (1,NOW(),1), (2,NOW(),2), (3,NOW(),3),
    (4,NOW(),4), (5,NOW(),5), (6,NOW(),6),
(7,NOW(),7), (8,NOW(),8), (9,NOW(),10);

SELECT COUNT(B)
FROM test_shard_table1
WHERE id IN
(SELECT c FROM test_shard_table2 WHERE id>5);

SELECT MAX(c), MIN(c)
FROM test_shard_table1 WHERE c IN
(SELECT c FROM test_shard_table2 WHERE id<8)
AND id>4 ORDER BY c;
```

## INSERT
语法如下：
```
INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {{VALUES | VALUE} (value_list) [, (value_list)] ...
      |
      VALUES row_constructor_list
    }
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {SELECT ... | TABLE table_name}
    [ON DUPLICATE KEY UPDATE assignment_list]

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

row_constructor_list:
    ROW(value_list)[, ROW(value_list)][, ...]

assignment:
    col_name = [row_alias.]value

assignment_list:
    assignment [, assignment] ...
```
>!对于分片表执行insert命令时，字段必须包含Shardkey，否则系统会拒绝执行SQL命令，因为Proxy无法判断SQL语句发送的后端数据库节点位置 

**示例：**
```
--测试不带shardkey字段：
MySQL [test]> DROP TABLE IF EXISTS test1;
Query OK, 0 rows affected (0.12 sec)

MySQL [test]> create table test1(a int not null primary key,b int,c char(10)) shardkey=a;
Query OK, 0 rows affected (2.64 sec)

MySQL [test]> insert into test1 (b,c) values(10,"record3");
ERROR 683 (HY000): Proxy ERROR: Get shardkeys return error: insert/replace must contain shardkey column

MySQL [test]> insert into test1 (a,c) values(40,"records5");
Query OK, 1 row affected (0.03 sec)


--测试不携带ignore，会发生主键冲突
MySQL [test]> drop table if exists t1_1_1;
Query OK, 0 rows affected (0.10 sec)
MySQL [test]> create table t1_1_1 (a int primary key, b int) shardkey=a;
Query OK, 0 rows affected (0.18 sec)
MySQL [test]> drop table if exists t1_1_2;
Query OK, 0 rows affected (0.07 sec)
MySQL [test]> create table t1_1_2 (a int primary key) shardkey=a;
Query OK, 0 rows affected (0.18 sec)

MySQL [test]> insert into t1_1_1 (a,b) values (1,0),(2,0),(3,1);
Query OK, 3 rows affected (0.01 sec)

MySQL [test]> select * from t1_1_1;
+---+------+
| a | b    |
+---+------+
| 1 |    0 |
| 2 |    0 |
| 3 |    1 |
+---+------+
3 rows in set (0.00 sec)

MySQL [test]> insert into t1_1_2 select b from t1_1_1;
ERROR 913 (HY000): Proxy ERROR:Join internal error: Duplicate entry '0' for key 'PRIMARY'

--携带ignore，会写入部分数据，重复的数据只写一次
MySQL [test]> insert ignore into t1_1_2 select b from t1_1_1;
Query OK, 2 rows affected, 1 warning (0.00 sec)

MySQL [test]> select * from t1_1_2 order by a;
+---+
| a |
+---+
| 0 |
| 1 |
+---+
2 rows in set (0.00 sec)
```
## REPLACE
语法如下：

```
REPLACE
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {{VALUES | VALUE} (value_list) [, (value_list)] ...
      |
      VALUES row_constructor_list
    }

REPLACE 
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list

REPLACE
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {SELECT ... | TABLE table_name}

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

row_constructor_list:
    ROW(value_list)[, ROW(value_list)][, ...]

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```
>!对于分片表执行Replace命令时，字段必须包含Shardkey，否则系统会拒绝执行SQL命令，因为Proxy无法判断SQL语句发送的后端数据库节点位置

**示例：**

```
--测试不带shardkey字段：
MySQL [test]> DROP TABLE IF EXISTS test5;
MySQL [test]> create table test5(a int not null primary key,b int,c char(10)) shardkey=a;
Query OK, 0 rows affected (0.27 sec)

MySQL [test]> replace into test5 (b,c) values(10,"record3");
ERROR 683 (HY000): Proxy ERROR: Get shardkeys return error: insert/replace must contain shardkey column

MySQL [test]> replace into test5(a,b,c) values(3,40,"record1");
Query OK, 1 row affected (0.00 sec)

--测试加载多条数据
MySQL [test]> replace into test5(a,b,c) values(4,50,"record2"),(5,60,"record3"),(6,70,"record4"),(7,80,"record5"),(8,90,"record6"),(9,100,"record7");
Query OK, 6 rows affected (0.00 sec)

--测试replace select语句
drop table if exists t1_1_1;
create table t1_1_1 (a int not null primary key, b char(10)) shardkey=a;
drop table if exists t1_1_2;
create table t1_1_2 (a int not null primary key, b char(10)) shardkey=a;

insert into t1_1_1 (a,b) values (1,"t1:1"),(3,"t1:3");
insert into t1_1_2 (a,b) values (2,"t2:2"), (3,"t2:3");
replace into t1_1_1 select * from t1_1_2;
```

## DELETE
语法如下：
```
DELETE [QUICK] [IGNORE] FROM tbl_name [[AS] tbl_alias]
    [PARTITION (partition_name [, partition_name] ...)]
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]
```
>!为了安全考虑，分表和广播表执行delete指令的时候必须带“ where ”条件，否则系统拒绝执行该SQL命令 

**示例：**

```
--测试不带shardkey的delete
MySQL [test]> DROP TABLE IF EXISTS test3;
MySQL [test]> create table test3(a int not null primary key,b int,c char(10)) shardkey=a;

MySQL [test]> insert into test3(a,b,c) values (1,2,'A');
Query OK, 1 row affected (0.00 sec)

MySQL [test]> delete from test3;
ERROR 913 (HY000): Proxy ERROR:Join internal error: delete query has no where clause

MySQL [test]> delete from test3 where a=1;
Query OK, 1 rows affected (0.00 sec)

--测试包含子查询的delete
drop table if exists t1_1;
create table t1_1 (a int primary key, b int) shardkey=a;
drop table if exists t1_2;
create table t1_2 (a int primary key, b int) shardkey=a;
insert into t1_1 (a,b) values (20,20);
insert into t1_2 (a,b) values (20,20);
insert into t1_1 (a,b) values (19,19);
insert into t1_2 (a,b) values (19,19);
insert into t1_1 (a,b) values (18,18);
insert into t1_2 (a,b) values (18,18);
insert into t1_1 (a,b) values (17,17);
insert into t1_2 (a,b) values (17,17);
insert into t1_1 (a,b) values (16,16);
insert into t1_2 (a,b) values (16,16);
insert into t1_1 (a,b) values (15,15);
insert into t1_2 (a,b) values (15,15);
insert into t1_1 (a,b) values (14,14);
insert into t1_2 (a,b) values (14,14);
insert into t1_1 (a,b) values (13,13);
insert into t1_2 (a,b) values (13,13);
insert into t1_1 (a,b) values (12,12);
insert into t1_2 (a,b) values (12,12);
insert into t1_1 (a,b) values (11,11);
insert into t1_2 (a,b) values (11,11);
insert into t1_1 (a,b) values (10,10);
insert into t1_2 (a,b) values (10,10);
insert into t1_1 (a,b) values (9,9);
insert into t1_2 (a,b) values (9,9);
insert into t1_1 (a,b) values (8,8);
insert into t1_2 (a,b) values (8,8);
insert into t1_1 (a,b) values (7,7);
insert into t1_2 (a,b) values (7,7);
insert into t1_1 (a,b) values (6,6);
insert into t1_2 (a,b) values (6,6);
insert into t1_1 (a,b) values (5,5);
insert into t1_2 (a,b) values (5,5);
insert into t1_1 (a,b) values (4,4);
insert into t1_2 (a,b) values (4,4);
insert into t1_1 (a,b) values (3,3);
insert into t1_2 (a,b) values (3,3);
insert into t1_1 (a,b) values (2,2);
insert into t1_2 (a,b) values (2,2);
insert into t1_1 (a,b) values (1,1);
insert into t1_2 (a,b) values (1,1);
delete from t1_1 where a in (select b from t1_2 where a<10);
delete from t1_1 where exists(select 1 from t1_2 where t1_1.a=t1_2.b and t1_2.a>8);

--测试携带和不携带ignore的delete
drop table if exists t8_1;
create table t8_1 (a int NOT NULL, b int, primary key (a));
drop table if exists t8_2;
create table t8_2 (a int NOT NULL, b int, primary key (a));
drop table if exists t8_3;
create table t8_3 (a int NOT NULL, b int, primary key (a));
insert into t8_1 (a,b) values (0, 10),(1, 11),(2, 12);
insert into t8_2 (a,b) values (33, 10),(0, 11),(2, 12);
insert into t8_3 (a,b) values (1, 21),(2, 12),(3, 23);

--不带ignore的情况
MySQL [test]> delete t8_1.*, t8_2.* from t8_1,t8_2 where t8_1.a = t8_2.a and t8_1.b <> (select b from t8_3 where t8_1.a < t8_3.a);
ERROR 1242 (21000): Subquery returns more than 1 row

--携带ignore的情况
MySQL [test]> delete ignore t8_1.*, t8_2.* from t8_1,t8_2 where t8_1.a = t8_2.a and t8_1.b <> (select b from t8_3 where t8_1.a < t8_3.a);
Query OK, 2 rows affected, 2 warnings (0.01 sec)
```
## UPDATE
语法如下：
```
UPDATE [IGNORE] table_reference
    SET assignment_list
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]

value:
    {expr | DEFAULT}

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```
>!
- 分区表不支持更新shardkey，需用显示开启事务，再执行delete和insert替代update
- 分区表不支持update set的值为子查询
- 为了安全考虑，分表和广播表执行update指令的时候必须带“ where ”条件，否则系统拒绝执行该SQL命令 

**示例：**
```
--测试update的累加
DROP TABLE IF EXISTS t1_1;
CREATE TABLE t1_1
(place_id int (10) unsigned NOT NULL,
shows int(10) unsigned DEFAULT '0' NOT NULL,
ishows int(10) unsigned DEFAULT '0' NOT NULL,
ushows int(10) unsigned DEFAULT '0' NOT NULL,
clicks int(10) unsigned DEFAULT '0' NOT NULL,
iclicks int(10) unsigned DEFAULT '0' NOT NULL,
uclicks int(10) unsigned DEFAULT '0' NOT NULL,
ts timestamp,PRIMARY KEY (place_id,ts)) 
shardkey=place_id;

INSERT INTO t1_1 (place_id,shows,ishows,ushows,clicks,iclicks,uclicks,ts)VALUES (1,0,0,0,0,0,0,20000928174434);

UPDATE t1_1 SET shows=shows+1,ishows=ishows+1,ushows=ushows+1,clicks=clicks+1,iclicks=iclicks+1,uclicks=uclicks+1 WHERE place_id=1 AND ts>="2000-09-28 00:00:00";

--测试带有子查询的update
drop table if exists t1_1;
create table t1_1 (a int primary key, b int) shardkey=a;
drop table if exists t1_2;
create table t1_2 (a int primary key, b int) shardkey=a;
drop table if exists t1_3;
create table t1_3 (a int primary key, b int) shardkey=a;
insert into t1_1(a, b) values (10, 10);
insert into t1_1(a, b) values (9, 9);
insert into t1_1(a, b) values (8, 8);
insert into t1_1(a, b) values (7, 7);
insert into t1_1(a, b) values (6, 6);
insert into t1_1(a, b) values (5, 5);
insert into t1_1(a, b) values (4, 4);
insert into t1_1(a, b) values (3, 3);
insert into t1_1(a, b) values (2, 2);
insert into t1_1(a, b) values (1, 1);
insert into t1_2 select * from t1_1;
insert into t1_3 select * from t1_1;
update t1_1 set b=1 where exists(select * from t1_2 where t1_1.a=t1_2.a order by 1) limit 3;
update t1_1 set b=-1 where a in (select b from t1_2 order by 1) order by a limit 3;

--update不支持更新主键
MySQL [test]> update t1_1 set a=b where exists(select 1 from t1_2 where a=t1_1.b);
ERROR 658 (HY000): Proxy ERROR: Join internal error: cannot update primary key

--update不支持更新shardkey
MySQL [test]> update t1_1 set a=200 where b=1;
ERROR 682 (HY000): Proxy ERROR: Something went wrong: can not update the shardkey

--显示开启事务用delete/insert替代update 
begin;
delete from t1_1 where b=1;
insert into t1_1(a,b) values(200,1);
commit;

--不支持update列表中带有sum的子查询
MySQL [test]> update t1_1 set b=(select max(b) from t1_2 where t1_2.a=t1_1.a) where 1;
ERROR 658 (HY000): Proxy ERROR: Join internal error: do not support subquery/sum in update list

--多表更新语法，但只更新一个表
MySQL [test]> update t1_1, t1_2 set t1_1.b=-1 where t1_1.a=t1_2.b and t1_2.a<3;
Query OK, 0 rows affected (0.01 sec)

--不支持order by和limit
MySQL [test]> update t1_1, t1_2 set t1_1.b=-1 where t1_1.a=t1_2.b and t1_2.a<3 order by t1_1.a limit 3;
ERROR 658 (HY000): Proxy ERROR: Join internal error: Incorrect usage of UPDATE and ORDER

--不支持更新多个表
MySQL [test]> update t1_1, t1_2 set t1_1.b=-1, t1_2.b=-1 where t1_1.a=t1_2.b and t1_2.a<3;
ERROR 658 (HY000): Proxy ERROR: Join internal error: multi update is not supported yet.

--更新一个表，但value引用了另外一个表
MySQL [test]> update t1_1, t1_2 set t1_1.b= t1_2.b+1 where t1_1.a=t1_2.b and t1_2.a<3;
Query OK, 2 rows affected (0.01 sec)

--不支持list分区表更新分区键
drop table if exists list_user;
CREATE TABLE list_user 
(id int, name varchar(255), 
city varchar(255), primary key(id)) 
shardkey=id 
PARTITION by list(city) 
(PARTITION p0 values in ('Beijin','Shanghai','Shenzhen'),
 PARTITION p1 values in ('Nanjin', 'Chongqing','Wuhan'));
insert into list_user (id, name,city) values (1,'Rain','Beijin'),(22,'Storm','Beijin'),(103,'wind','Nanjin');

MySQL [test]> update list_user set city='Nanjin' where id in (select id from list_user,t1_1 where t1_1.a=list_user.id and t1_1.a <3 );
ERROR 913 (HY000): Proxy ERROR:Join internal error: sub partitioned table do not support such update yet!

MySQL [test]> update list_user set city='Nanjin' where id=1;
ERROR 682 (HY000): Proxy ERROR: Something went wrong: can not update the subshardkey

--不支持范围分区表更新分区键
drop table if exists range_part;
create table range_part
(a int, b int, PRIMARY KEY(a)) 
shardkey=a 
PARTITION BY range (b) 
(PARTITION p0 values less than (100), 
PARTITION p1 values less than (200));
insert into range_part (a,b) values (1,11),(22,2),(103,1);

MySQL [test]> update range_part set b=11 where a in (select a from range_part,t1_1 where t1_1.a=range_part.id and t1_1.a <3 );
ERROR 913 (HY000): Proxy ERROR:Join internal error: sub partitioned table do not support such update yet!

MySQL [test]> update range_part set b=11 where a=103;
ERROR 682 (HY000): Proxy ERROR: Something went wrong: can not update the subshardkey
```
