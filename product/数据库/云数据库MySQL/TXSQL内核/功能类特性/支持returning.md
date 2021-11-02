## 功能介绍
在某些使用场景下，需要在 DML 操作后返回刚操作的数据行。实现这个需求一般有两种办法：
- 一是在开启事务的后在 DML 语句后紧跟一条 SELECT 语句。
- 二是使用触发器等较为复杂的操作实现。

前者主要会增加一条 SELECT 语句的开销，后者则会令 SQL 的实现变得更加复杂并且不够灵活（需要创建触发器）。
因此，RETURNING 语法的设计主要针对该场景的优化，通过在 DML 语句后增加 RETURNING 关键字可以灵活高效地实现上述的需求。

## 支持版本
内核版本 MySQL 5.7 20210330 及以上

## 适用场景
在目前 MySQL 5.7 20210330 及以上的内核版本中，分别支持：INSERT ... RETURNING、REPLACE ... RETURNING、DELETE ... RETURNING。该语法允许返回所有被 INSERT/REPLACE/DELETE 语句操作过的行（statment 为单位）。同时，RETURNING 也支持在 prepared statements，存储过程中使用。

在使用该功能时，需要注意以下几点：
1. 在使用 RETURNING 时，DELETE...RETURNING 语句返回前镜像数据，INSERT/REPLACE...RETURNING 返回后镜像数据。
2. 暂不支持 UPDATE...RETURNING 语句。
3. INSERT/REPLACE 场景下，外层表的列对 returning 中的子查询语句，暂不具有可见性。
4. INSERT/REPLACE的RETURNING 语句若需要返回 last_insert_id()，则该 last_insert_id() 的值为该语句执行成功之前的值。若需要获得精确的 last_insert_id() 值，建议使用 RETURNING 直接返回该表的自增列 ID。

## 使用说明
#### INSERT... RETURNING
```
MySQL [test]> CREATE TABLE `t1` (id1 INT);
Query OK, 0 rows affected (0.04 sec)

MySQL [test]> CREATE TABLE `t2` (id2 INT);
Query OK, 0 rows affected (0.03 sec)

MySQL [test]> INSERT INTO  t2 (id2) values (1);
Query OK, 1 row affected (0.00 sec)

MySQL [test]> INSERT INTO t1 (id1) values (1) returning *, id1 * 2, id1 + 1, id1 * id1 as alias, (select * from t2); 
+------+---------+---------+-------+--------------------+
| id1  | id1 * 2 | id1 + 1 | alias | (select * from t2) |
+------+---------+---------+-------+--------------------+
|    1 |       2 |       2 |     1 |                  1 |
+------+---------+---------+-------+--------------------+
1 row in set (0.01 sec)

MySQL [test]> INSERT INTO t1 (id1) SELECT id2 from t2 returning id1;
+------+
| id1  |
+------+
|    1 |
+------+
1 row in set (0.01 sec)
```

#### REPLACE ... RETURNING
```
MySQL [test]> CREATE TABLE t1(id1 INT PRIMARY KEY, val1 VARCHAR(1));
Query OK, 0 rows affected (0.04 sec)

MySQL [test]> CREATE TABLE t2(id2 INT PRIMARY KEY, val2 VARCHAR(1));
Query OK, 0 rows affected (0.03 sec)

MySQL [test]> INSERT INTO t2 VALUES (1,'a'),(2,'b'),(3,'c');
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

MySQL [test]> REPLACE INTO t1 (id1, val1) VALUES (1, 'a');
Query OK, 1 row affected (0.00 sec)

MySQL [test]> REPLACE INTO t1 (id1, val1) VALUES (1, 'b') RETURNING *;
+-----+------+
| id1 | val1 |
+-----+------+
|   1 | b    |
+-----+------+
1 row in set (0.01 sec)
```

#### DELETE ... RETURNING
```
MySQL [test]> CREATE TABLE t1 (a int, b varchar(32));
Query OK, 0 rows affected (0.04 sec)

MySQL [test]> INSERT INTO t1 VALUES
    ->   (7,'ggggggg'), (1,'a'), (3,'ccc'),
    ->   (4,'dddd'), (1,'A'), (2,'BB'), (4,'DDDD'),
    ->   (5,'EEEEE'), (7,'GGGGGGG'), (2,'bb');
Query OK, 10 rows affected (0.03 sec)
Records: 10  Duplicates: 0  Warnings: 0

MySQL [test]> DELETE FROM t1 WHERE a=2 RETURNING *;
+------+------+
| a    | b    |
+------+------+
|    2 | BB   |
|    2 | bb   |
+------+------+
2 rows in set (0.01 sec)

MySQL [test]> DELETE FROM t1 RETURNING *;
+------+---------+
| a    | b       |
+------+---------+
|    7 | ggggggg |
|    1 | a       |
|    3 | ccc     |
|    4 | dddd    |
|    1 | A       |
|    4 | DDDD    |
|    5 | EEEEE   |
|    7 | GGGGGGG |
+------+---------+
8 rows in set (0.01 sec)
```

#### 存储过程
```
MySQL [test]> CREATE TABLE `t` (id INT);
Query OK, 0 rows affected (0.03 sec)

MySQL [test]> delimiter $$
MySQL [test]> CREATE PROCEDURE test(in param INT)
    -> BEGIN
    ->     INSERT INTO t (id) values (param) returning *;
    -> END$$
Query OK, 0 rows affected (0.00 sec)
MySQL [test]> delimiter ;

MySQL [test]> CALL test(100);
+------+
| id   |
+------+
|  100 |
+------+
1 row in set (0.01 sec)

Query OK, 0 rows affected (0.01 sec)
```

