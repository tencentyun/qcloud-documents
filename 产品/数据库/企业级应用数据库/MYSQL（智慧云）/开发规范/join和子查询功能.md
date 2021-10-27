对于分布式实例，数据水平拆分在各个节点上。为了提高性能，应用层应优先优化表结构和SQL语句，使数据尽量采用不跨节点的方式存储。
- 如果Join 相关的表有分表键相等条件（如下示例），由于分表的一致性原则，会让这部分数据自动存储到同一物理节点，此时相当于单机Join，数据处理效率将更高，因此我们推荐使用join方式替代子查询。
- 如果涉及到跨物理节点数据，此时 Proxy 会先从其他节点拉取数据并缓存，由于涉及到网络数据传输，将降低数据处理效率。

## 推荐join方式
### 分表之间
如果分表之间带有分表键相等的条件，则相当于单机Join。语句如下：
```
MySQL [test]> create table test1(a int not null primary key,b int,c char(20)) shardkey=a;

Query OK, 0 rows affected (2.64 sec)

MySQL [test]> create table test2(a int not null primary key,b int,c char(20)) shardkey=a;
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

### 分表和广播表
跨分片的分表与广播表，效果相当于单机 Join。语句如下：
```
MySQL [test]> create table global_test(a int key, b int) shardkey=noshardkey_allset;
Query OK, 0 rows affected (0.07 sec)

MySQL [test]> insert into global_test(a, b) values(1,1),(2,2);
Query OK, 2 rows affected (0.05 sec)

MySQL [test]> select a,b from global_test;
+---+------+
| a | b    |
+---+------+
| 1 |    1 |
| 2 |    2 |
+---+------+
2 rows in set (0.02 sec)

MySQL [test]> select * from test1;
+---+------+---------------+
| a | b    | c             |
+---+------+---------------+
| 1 |    2 | test1_record1 |
| 2 |    3 | test1_record2 |
+---+------+---------------+
2 rows in set (0.00 sec)

MySQL [test]> select t1.a,t1.b,t1.c,tg.a,tg.b from test1 t1,global_test tg where t1.a=tg.a;
+---+------+---------------+---+------+
| a | b    | c             | a | b    |
+---+------+---------------+---+------+
| 1 |    2 | test1_record1 | 1 |    1 |
| 2 |    3 | test1_record2 | 2 |    2 |
+---+------+---------------+---+------+
2 rows in set (0.00 sec)
```

## 复杂SQL查询
对于不满足推荐方式的SQL语句，因需要做跨节点的数据交互，将会导致性能变差，可能影响以下查询活动：
- 包含子查询的查询。
- 带有Having条件的查询。
- 需要进行多个排序/分组/去重的查询，例如：Count (Distinct ID)。
- 多表的Join查询，且参与查询的各表的分区字段(Shardkey)不相等，或者同时涉及不同类型的表（例如，单表和分表）。
对于此类复杂查询，可以通过条件下推，将从后端数据库中抽取出参与查询的数据，并存放在本地临时表中，通过临时表中的数据进行计算。

因此用户需要指定参与查询的表的条件，避免因抽取大量数据而导致性能受损。相关语句如下：

```
mysql> create table test1 ( a int key, b int, c char(20) ) shardkey=a;
Query OK, 0 rows affected (1.56 sec)

mysql> create table test2 ( a int key, d int, e char(20) ) shardkey=a;
Query OK, 0 rows affected (1.46 sec)

mysql> insert into test1 (a,b,c) values(1,2,"record1"),(2,3,"record2");
Query OK, 2 rows affected (0.02 sec)

mysql> insert into test2 (a,d,e) values(1,3,"test2_record1"),(2,3,"test2_record2");
Query OK, 2 rows affected (0.02 sec)

MySQL [test]> select t1.a,t1.b,t1.c,t2.a,t2.d,t2.e  from test1 t1 join test2 t2 on t1.b=t2.d;
+---+------+---------+---+------+---------------+
| a | b    | c       | a | d    | e             |
+---+------+---------+---+------+---------------+
| 2 |    3 | record2 | 1 |    3 | test2_record1 |
| 2 |    3 | record2 | 2 |    3 | test2_record2 |
+---+------+---------+---+------+---------------+
2 rows in set (0.00 sec)

MySQL [test]> select t1.a,t1.b,t1.c from test1 t1 where t1.a in (select a from test2);
+---+------+---------+
| a | b    | c       |
+---+------+---------+
| 1 |    2 | record1 |
| 2 |    3 | record2 |
+---+------+---------+
2 rows in set (0.01 sec)

MySQL [test]> select t1.a,t1.b,t1.c from test1 t1  where exists (select t2.a,t2.d,t2.e  from test2 t2 where t2.a=t1.b);
+---+------+---------+
| a | b    | c       |
+---+------+---------+
| 1 |    2 | record1 |
+---+------+---------+
1 row in set (0.00 sec)

MySQL [test]> select t1.a, count(1) from test1 t1 where exists (select t2.a,t2.d,t2.e from test2 t2 where t2.a=t1.a) group by t1.a;
+---+----------+
| a | count(1) |
+---+----------+
| 1 |        1 |
| 2 |        1 |
+---+----------+
2 rows in set (0.03 sec)

MySQL [test]> select distinct count(1) from test1 t1 where exists (select t2.a,t2.d,t2.e from test2 t2 where t2.a=t1.a) group by t1.a;
+----------+
| count(1) |
+----------+
|        1 |
+----------+
1 row in set (0.02 sec)

MySQL [test]> select count(distinct t1.a) from test1 t1 where exists (select t2.a,t2.d,t2.e from test2 t2 where t2.a=t1.a);
+----------------------+
| count(distinct t1.a) |
+----------------------+
|                    2 |
+----------------------+
1 row in set (0.00 sec)


```
