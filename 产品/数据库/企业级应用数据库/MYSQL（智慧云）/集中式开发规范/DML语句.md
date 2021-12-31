本节主要介绍 DML 语句中常用的Select（查询）、Insert（插入）、Replace（替换）、Update（更新）及Delete（删除）指令。
## SELECT指令
执行Select指令时，建议增加where子句，语句如下：

```
MySQL [test]> create table test1(a int not null primary key,b int,c char(10));
Query OK, 0 rows affected (0.05 sec)

MySQL [test]> insert into test1(a,b,c) values(2,3,'record2');
Query OK, 1 row affected (0.00 sec)

MySQL [test]> insert into test1(a,b,c) values(3,4,'record3');
Query OK, 1 row affected (0.01 sec)

MySQL [test]> select b,c from test1 where a=3;
+------+---------+
| b    | c       |
+------+---------+
|    4 | record3 |
+------+---------+
1 row in set (0.00 sec)
INSERT/REPLACE指令
MySQL [test]> insert into test1 (a,c) values(40,"records5");
Query OK, 1 row affected (0.03 sec)

MySQL [test]> select a,b,c from test1;
+----+------+----------+
| a  | b    | c        |
+----+------+----------+
|  2 |    3 | record2  |
|  3 |    4 | record3  |
|  4 |   10 | record3  |
| 40 | NULL | records5 |
+----+------+----------+
4 rows in set (0.00 sec)


MySQL [test]> replace into test1(a,b,c) values(3,40,"record1");
Query OK, 2 rows affected (0.03 sec)

MySQL [test]> select a,b,c from test1;
+----+------+----------+
| a  | b    | c        |
+----+------+----------+
|  2 |    3 | record2  |
|  3 |   40 | record1  |
|  4 |   10 | record3  |
| 40 | NULL | records5 |
+----+------+----------+
4 rows in set (0.00 sec)
```
## DELETE/UPDATE指令
执行Delete/Update命令时，为了安全考虑，建议加上where子句，语句如下：

```
MySQL [test]> delete from test1 where a=2;
Query OK, 1 row affected (0.01 sec)
```
【建议】：为了防止用户误操作，建议尽量不要使用全表的Update/Delete指令；
