本节主要介绍创建、删除、查询和使用Sequence，以及获取显示Sequence的值。Sequence语法和MariaDB兼容，但是需保证分布式全局递增且数值唯一。
>! 目前Sequence为保证分布式全局数值唯一，导致性能较差，主要适用于并发不高的场景。

**示例：**

```
创建Sequence：
create tdsql_sequence test.seq1 start with 12 tdsql_minvalue 10 maxvalue 50000  tdsql_increment by 5  tdsql_nocycle;
create tdsql_sequence test.seq2 start with 12 tdsql_minvalue 10 maxvalue 50000  tdsql_increment by 1  tdsql_cycle;

查询Sequence：
show create tdsql_sequence test.seq2;

使用Sequence获取下一个数值，语句如下：
select tdsql_nextval(test.seq2);
select next value for test.seq2;

删除Sequence：
drop tdsql_sequence test.seq1;
drop tdsql_sequence test.seq2;

nextval命令可以用在insert语句中。使用如下：
MySQL [test]> DROP TABLE IF EXISTS test3;
MySQL [test]> create table test3(a int not null primary key,b int,c char(10)) shardkey=a;
MySQL [test]> insert into test3(a,c) values(1,'A');
Query OK, 1 row affected (0.00 sec)
MySQL [test]> insert into test3(a,c) values(40,'records5');
Query OK, 1 row affected (0.00 sec)

MySQL [test]> select a,c from test3;
+----+----------+
| a  | c        |
+----+----------+
|  1 | A        |
| 40 | records5 |
+----+----------+
2 rows in set (0.00 sec)

MySQL [test]> insert into test3(a,c) values(tdsql_nextval(test.seq2),3);
Query OK, 1 row affected (0.01 sec)

Seq2的初始值为12，此次insert的值为12
MySQL [test]> select a,c from test3;
+----+----------+
| a  | c        |
+----+----------+
| 40 | records5 |
|  1 | A        |
| 12 | 3        |
+----+----------+
3 rows in set (0.00 sec)

如需获取上一次的值：
MySQL [test]> select tdsql_lastval(test.seq2);
+----+
| 12 |
+----+
| 12 |
+----+
1 row in set (0.00 sec)

MySQL [test]> select tdsql_previous value for test.seq2;
+----+
| 12 |
+----+
| 12 |
+----+
1 row in set (0.00 sec)

设置下一个序列数值为2000，tdsql_setval内的第三个参数默认为1，表示2000这个值用过了，下一次不包含2000，如果为0，则下一个从2000开始。
MySQL [test]> select tdsql_setval(test.seq2,2000,1)  
    -> ;
+------+
| 2000 |
+------+
| 2000 |
+------+
1 row in set (0.01 sec)

设置的值只能比当前数值大，否则将返回数值为0。设置下一个序列数值时，如果比当前数值小，则系统将没有反应，例如：
MySQL [test]> select tdsql_nextval(test.seq2);
+------+
| 2001 |
+------+
| 2001 |
+------+
1 row in set (0.01 sec)

seq2设置为10，系统返回0
MySQL [test]> select tdsql_setval(test.seq2,10);
+---+
| 0 |
+---+
| 0 |
+---+
1 row in set (0.03 sec)

如果设置的比当前数值大，成功返回当前设置的值。
MySQL [test]> select tdsql_setval(test.seq2,2010);
+------+
| 2010 |
+------+
| 2010 |
+------+
1 row in set (0.02 sec)

MySQL [test]> select tdsql_nextval(test.seq2);
+------+
| 2011 |
+------+
| 2011 |
+------+
1 row in set (0.01 sec)
```
