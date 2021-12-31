子查询一般是将查询出来的结果作为其他查询的结果使用。使用子查询可以一次性的完成很多逻辑上需要多个步骤才能完成的SQL操作。但多数情况下，使用join替代子查询效率更高。
## 子查询方式
语句如下：

```
MySQL [test]> SELECT cust_name FROM customerinfo 
WHERE CustomerID NOT in (SELECT CustomerID FROM salesinfo);
```
## 推荐join方式
join方式语句如下：
```
MySQL [test]> create table test1(a int not null primary key,b int,c char(20));
Query OK, 0 rows affected (2.64 sec)

MySQL [test]> create table test2(a int not null primary key,b int,c char(20));
Query OK, 0 rows affected (2.28 sec)

MySQL [test]> insert into test1(a,b,c) values(1,2,'test1_record1');
Query OK, 1 row affected (0.01 sec)

MySQL [test]> insert into test1(a,b,c) values(2,3,'test1_record2');
Query OK, 1 row affected (0.03 sec)

MySQL [test]> insert into test2(a,b,c) values(1,200,'test2_record1');
Query OK, 1 row affected (0.01 sec)

MySQL [test]> insert into test2(a,b,c) values(2,300,'test2_record2');
Query OK, 1 row affected (0.07 sec)

MySQL [test]> select a,b,c from test1;
+---+------+---------------+
| a | b    | c             |
+---+------+---------------+
| 1 |    2 | test1_record1 |
| 2 |    3 | test1_record2 |
+---+------+---------------+
2 rows in set (0.01 sec)

MySQL [test]> select a,b,c from test2;
+---+------+---------------+
| a | b    | c             |
+---+------+---------------+
| 1 |  200 | test2_record1 |
| 2 |  300 | test2_record2 |
+---+------+---------------+
2 rows in set (0.01 sec)

MySQL [test]> select t1.a,t1.b,t1.c,t2.a,t2.b,t2.c from test1 t1 join test2 t2 where t1.a=t2.a;
+---+------+---------------+---+------+---------------+
| a | b    | c             | a | b    | c             |
+---+------+---------------+---+------+---------------+
| 1 |    2 | test1_record1 | 1 |  200 | test2_record1 |
| 2 |    3 | test1_record2 | 2 |  300 | test2_record2 |
+---+------+---------------+---+------+---------------+
2 rows in set (0.01 sec)

MySQL [test]> select t1.a,t1.b,t1.c,t2.a,t2.b,t2.c from test1 t1 left join test2 t2 on t1.a<t2.a where t1.a=1;
+---+------+---------------+------+------+---------------+
| a | b    | c             | a    | b    | c             |
+---+------+---------------+------+------+---------------+
| 1 |    2 | test1_record1 |    2 |  300 | test2_record2 |
+---+------+---------------+------+------+---------------+
1 row in set (0.00 sec)
```
