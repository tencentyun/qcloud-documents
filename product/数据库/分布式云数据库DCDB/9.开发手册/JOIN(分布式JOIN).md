
对于分布式实例，数据水平拆分在各个节点，为提高性能，建议优先优化表结构和 SQL，尽量使用不跨节点的方式。

## 推荐方式
### 多个分表，带有分表键相等的条件
```sql
MySQL > select * from test1 join test2 where test1.a=test2.a;     
+---+------+---------+---+------+---------------+
| a | b    | c       | a | d    | e             |
+---+------+---------+---+------+---------------+
| 1 |    2 | record1 | 1 |    3 | test2_record1 |
| 2 |    3 | record2 | 2 |    3 | test2_record2 |
+---+------+---------+---+------+---------------+
2 rows in set (0.00 sec)

MySQL > select * from test1 left join test2 on test1.a<test2.a where test1.a=1;
+---+------+---------+------+------+---------------+
| a | b    | c       | a    | d    | e             |
+---+------+---------+------+------+---------------+
| 1 |    2 | record1 |    2 |    3 | test2_record2 |
+---+------+---------+------+------+---------------+
1 row in set (0.00 sec)

MySQL> select * from test1 where test1.a in (select a from test2);        
+---+------+---------+
| a | b    | c       |
+---+------+---------+
| 1 |    2 | record1 |
| 2 |    3 | record2 |
+---+------+---------+
2 rows in set (0.00 sec)

MySQL> select a, count(1) from test1 where exists (select * from test2 where test2.a=test1.a) group by a;        
+---+----------+
| a | count(1) |
+---+----------+
| 1 |        1 |
| 2 |        1 |
+---+----------+
2 rows in set (0.00 sec)

MySQL> select distinct count(1) from test1 where exists (select * from test2 where test2.a=test1.a) group by a;   
+----------+
| count(1) |
+----------+
|        1 |
+----------+
1 row in set (0.00 sec)

MySQL> select count(distinct a) from test1 where exists (select * from test2 where test2.a=test1.a);        
+-------------------+
| count(distinct a) |
+-------------------+
|                 2 |
+-------------------+
1 row in set (0.00 sec)
```

### 均为单表
```sql
mysql> create table noshard_table ( a int, b int key);
Query OK, 0 rows affected (0.02 sec)

mysql> create table noshard_table_2 ( a int, b int key);
Query OK, 0 rows affected (0.00 sec)

mysql> select * from noshard_table,noshard_table_2;
Empty set (0.00 sec)

mysql> insert into noshard_table (a,b) values(1,2),(3,4);
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> insert into noshard_table_2 (a,b) values(10,20),(30,40);
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from noshard_table,noshard_table_2;
+------+---+------+----+
| a    | b | a    | b  |
+------+---+------+----+
|    1 | 2 |   10 | 20 |
|    3 | 4 |   10 | 20 |
|    1 | 2 |   30 | 40 |
|    3 | 4 |   30 | 40 |
+------+---+------+----+
4 rows in set (0.00 sec)
```

### 广播表
```sql
 MySQL> create table global_test(a int key, b int)shardkey=noshardkey_allset;
Query OK, 0 rows affected (0.00 sec)

MySQL> insert into global_test(a, b) values(1,1),(2,2);
Query OK, 2 rows affected (0.00 sec)

MySQL> select * from test1, global_test;
+---+------+---------+---+------+
| a | b    | c       | a | b    |
+---+------+---------+---+------+
| 1 |    2 | record1 | 1 |    1 |
| 2 |    3 | record2 | 1 |    1 |
| 1 |    2 | record1 | 2 |    2 |
| 2 |    3 | record2 | 2 |    2 |
+---+------+---------+---+------+
4 rows in set (0.00 sec)
```

### 子查询带有 shardkey 的 derived table
```
mysql> select a from (select * from test1 where a=1) as t;
+---+
| a |
+---+
| 1 |
+---+
1 row in set (0.00 sec)
```
>?子查询时不指定 shardkey，即可查询结果。

## 复杂 SQL
对于不能满足推荐方式的 SQL，由于需要做跨节点的数据交互，所以性能会差一些。
包括：
- 包含子查询的查询。
- 多表的 join 查询，且参与查询的各表的分区字段（shardkey）不相等，或者同时涉及不同类型的表，例如单表和分表。

对于这类复杂查询，通过条件下推，将真正参与查询的数据从后端数据库中抽取出来，存放在本地的临时表中，然后对临时表中的数据进行计算。

因此用户需要明确指定参与查询的表的条件，避免因为抽取大量数据而性能受损。
```sql
mysql> create table test1 ( a int key, b int, c char(20) ) shardkey=a;
Query OK, 0 rows affected (1.56 sec)

mysql> create table test2 ( a int key, d int, e char(20) ) shardkey=a;
Query OK, 0 rows affected (1.46 sec)

mysql> insert into test1 (a,b,c) values(1,2,"record1"),(2,3,"record2");
Query OK, 2 rows affected (0.02 sec)

mysql> insert into test2 (a,d,e) values(1,3,"test2_record1"),(2,3,"test2_record2");
Query OK, 2 rows affected (0.02 sec)

mysql> select * from test1 join test2 on test1.b=test2.d;
+---+------+---------+---+------+---------------+
| a | b    | c       | a | d    | e             |
+---+------+---------+---+------+---------------+
| 2 |    3 | record2 | 1 |    3 | test2_record1 |
| 2 |    3 | record2 | 2 |    3 | test2_record2 |
+---+------+---------+---+------+---------------+
2 rows in set (0.00 sec)

MySQL> select * from test1 where exists (select * from test2 where test2.a=test1.b);
+---+------+---------+
| a | b    | c       |
+---+------+---------+
| 1 |    2 | record1 |
+---+------+---------+
1 row in set (0.00 sec)
```

分布式实例还支持丰富的复杂 update/delete/insert 操作。

需要注意的是，这类查询是在与之对应的 select 基础上实现的，因此也需要将数据加载至网关临时表，建议用户尽量在查询中指定明确的查询条件，避免大量数据的加载带来性能损耗。
另外，网关在加载数据时默认不会对加载的数据进行上锁，这与官方的 MySQL 行为存在略微的差异；如需加锁可以通过修改 proxy 配置来实现。

```sql
MySQL [th]> update test1 set test1.c="record" where exists(select 1 from test2 where test1.b=test2.d);
Query OK, 1 row affected (0.00 sec)

MySQL [th]> update test1, test2 set test1.b=2 where test1.b=test2.d;
Query OK, 1 row affected (0.00 sec)

MySQL [th]> insert into test1 select cast(rand()*1024 as unsigned), d, e from test2;
Query OK, 2 rows affected (0.00 sec)

MySQL [th]> delete from test1 where b in (select b from test2);
Query OK, 6 rows affected (0.00 sec)

MySQL [th]> delete from test2.* using test1 right join test2 on test1.a=test2.a where test1.a is null;
Query OK, 2 rows affected (0.00 sec)
```
