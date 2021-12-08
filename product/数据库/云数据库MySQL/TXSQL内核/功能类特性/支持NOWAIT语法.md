## 功能介绍
- DDL 支持 NO_WAIT 和 WAIT 选项。对于 DDL 操作，可通过 WAIT 设置等待 MDL LOCK 的秒数，如果在设定时间内未能获取到 MDL LOCK 则直接返回，也可指定 NO_WAIT 选项，未能获取到 MDL LOCK 直接返回。
- SELECT FOR UPDATE 支持 NOWAIT 和 SKIP LOCKED 选项。原有的 SELECT FOR UPDATE 逻辑下，如果目标行数据被另一个事务所加了锁，则需要等待该事务释放锁，但某些场景，如秒杀，并不希望等待锁，通过 SKIP LOCKED 和 NOWAIT 选项提供一种不需要等待锁的功能。SKIP LOCKED 语句会跳过已经被加锁的行，这些行不会出现在结果集中；NOWAIT 语句遇到被加锁的行不会等待，同时会报错。

需要注意的是这两种 NO WAIT 使用的关键字是不一样的。

## 支持版本
- 内核版本 MySQL 5.7 20171130 及以上，DDL 语句支持 NO_WAIT 和 WAIT 选项。
- 内核版本 MySQL 5.7 20200630 及以上（该功能从 MySQL 8.0 移植，因此8.0版本原生支持），SELECT FOR UPDATE 语句支持 NOWAIT 和 SKIP LOCKED 选项。

## 适用场景
DevAPI/XPlugin 暂不支持 SELECT FOR UPDATE/SHARE 语句中使用 SKIP LOCKED 和 NOWAIT 选项。由于历史原因，DDL 的 NO_WAIT 关键字和 SELECT FOR UPDATE 的 NOWAIT 关键字是两个不同的关键字，需要注意区分。

## 使用说明
#### SELECT FOR UPDATE NOWAIT/SKIP LOCKED
```
###############session 1###############
MySQL [test]> create table t1(seat_id int, state int, primary key(seat_id)) engine=innodb;
Query OK, 0 rows affected (0.03 sec)
 
MySQL [test]> INSERT INTO t1 VALUES(1,0), (2,0), (3,0), (4,0);
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0
 
MySQL [test]> begin;
Query OK, 0 rows affected (0.01 sec)
 
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR SHARE;
+---------+-------+
| seat_id | state |
+---------+-------+
|       1 |     0 |
|       2 |     0 |
+---------+-------+
2 rows in set (0.00 sec)
 
###############session 2###############
MySQL [test]> SET SESSION innodb_lock_wait_timeout=1;
Query OK, 0 rows affected (0.00 sec)
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR UPDATE;
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR UPDATE NOWAIT;
ERROR 5010 (HY000): Do not wait for lock.
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR UPDATE SKIP LOCKED;
+---------+-------+
| seat_id | state |
+---------+-------+
|       3 |     0 |
|       4 |     0 |
+---------+-------+
2 rows in set (0.00 sec)
 
MySQL [test]> SELECT * FROM t1 WHERE seat_id > 0 LIMIT 2 FOR UPDATE NOWAIT;
ERROR 5010 (HY000): Do not wait for lock.
MySQL [test]> SELECT * FROM t1 WHERE seat_id > 0 LIMIT 2 FOR UPDATE SKIP LOCKED;
+---------+-------+
| seat_id | state |
+---------+-------+
|       3 |     0 |
|       4 |     0 |
+---------+-------+
2 rows in set (0.00 sec)
 
MySQL [test]> commit;
Query OK, 0 rows affected (0.00 sec)
```

#### SELECT FOR SHARE NOWAIT/SKIP LOCKED
```
###############session 1###############
MySQL [test]> begin;
Query OK, 0 rows affected (0.01 sec)
 
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR UPDATE;
+---------+-------+
| seat_id | state |
+---------+-------+
|       1 |     0 |
|       2 |     0 |
+---------+-------+
2 rows in set (0.00 sec)
 
###############session 2###############
MySQL [test]> SET SESSION innodb_lock_wait_timeout=1;
Query OK, 0 rows affected (0.00 sec)
 
MySQL [test]> begin;
Query OK, 0 rows affected (0.00 sec)
 
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 LOCK IN SHARE MODE;
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR SHARE;
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR SHARE NOWAIT;
ERROR 5010 (HY000): Do not wait for lock.
MySQL [test]> SELECT * FROM t1 WHERE state = 0 LIMIT 2 FOR SHARE SKIP LOCKED;
+---------+-------+
| seat_id | state |
+---------+-------+
|       3 |     0 |
|       4 |     0 |
+---------+-------+
2 rows in set (0.00 sec)
 
MySQL [test]> commit;
Query OK, 0 rows affected (0.00 sec)
```

#### DDL 语句 NO_WAIT 和 WAIT 选项
```
ALTER TABLE `table` [NO_WAIT | WAIT [n]] `command`;
DROP TABLE `table` [NO_WAIT | WAIT [n]];
TRUNCATE TABLE `table` [NO_WAIT | WAIT [n]];
OPTIMIZE TABLE `table` [NO_WAIT | WAIT [n]];
RENAME TABLE `table_src` [NO_WAIT | WAIT [n]] TO `table_dst`;
CREATE INDEX `index` ON `table.columns` [NO_WAIT | WAIT [n]];
CREATE FULLTEXT INDEX `index` ON `table.columns` [NO_WAIT | WAIT [n]];
CREATE SPATIAL INDEX `index` ON `table.columns` [NO_WAIT | WAIT [n]];
DROP INDEX `index` ON `table` [NO_WAIT | WAIT [n]];
```
