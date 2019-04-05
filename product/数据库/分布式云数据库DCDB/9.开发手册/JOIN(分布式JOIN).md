
> 如果您期望阅读或下载全量开发文档，请参考 [《TDSQL 开发指南》](https://cloud.tencent.com/document/product/557/7714)


## JOIN(分布式 JOIN)
由于 TDSQL 存在多个物理节点，部分 join 操作可能涉及到多个物理节点的数据，这种跨物理节点数据的 JOIN，一般叫做分布式 JOIN。

- 如果 join 相关的表有 shardkey 相等条件（如下示例），由于分表的一致性原则，会让这部分数据自动存储到同一物理节点，此时相当于单机 JOIN，性能最好。此处涉及到分表 shardkey 的选择，可以参考 [常见问题](https://cloud.tencent.com/document/product/557/10572)，帮助您更好的判断。
- 如果涉及到跨物理节点数据，此时 proxy 会先从其他节点拉取数据并缓存，由于涉及到网络数据传输，性能会损失。

### shardkey 相等条件（性能无损失）
```
	mysql> create table test1 ( a int key, b int, c char(20) ) shardkey=a;
	Query OK, 0 rows affected (1.56 sec)

	mysql> create table test2 ( a int key, d int, e char(20) ) shardkey=a;
	Query OK, 0 rows affected (1.46 sec)

	mysql> insert into test1 (a,b,c) values(1,2,"record1"),(2,3,"record2");
	Query OK, 2 rows affected (0.02 sec)

	mysql> insert into test2 (a,d,e) values(1,3,"test2_record1"),(2,3,"test2_record2");
	Query OK, 2 rows affected (0.02 sec)

	mysql>  select * from test1 left join test2 on test1.a=test2.a where test1.a=1;
	+---+------+---------+---+------+---------------+
	| a | b    | c       | a | d    | e             |
	+---+------+---------+---+------+---------------+
	| 1 |    2 | record1 | 1 |    3 | test2_record1 |
	+---+------+---------+---+------+---------------+
	1 row in set (0.00 sec)

	mysql>  select * from test1 join test2 on test1.a=test2.a;
	+---+------+---------+---+------+---------------+
	| a | b    | c       | a | d    | e             |
	+---+------+---------+---+------+---------------+
	| 1 |    2 | record1 | 1 |    3 | test2_record1 |
	| 2 |    3 | record2 | 2 |    3 | test2_record2 |
	+---+------+---------+---+------+---------------+
	2 rows in set (0.03 sec)
```
### shardkey 不等条件（性能有损失）
```

        mysql>  select * from test1  join test2;
        +---+------+---------+---+------+---------------+
        | a | b    | c       | a | d    | e             |
        +---+------+---------+---+------+---------------+
        | 1 |    2 | record1 | 1 |    3 | test2_record1 |
        | 2 |    3 | record2 | 1 |    3 | test2_record1 |
        | 1 |    2 | record1 | 2 |    3 | test2_record2 |
        | 2 |    3 | record2 | 2 |    3 | test2_record2 |
        +---+------+---------+---+------+---------------+
        4 rows in set (0.06 sec)

```
### 对于广播表和单表（普通表）相关的 join

如果是单表（普通表）与单表（普通表）JOIN，相当于单机 JOIN，性能无损失。
如果是广播表与分表 JOIN，相当于单机 JOIN，性能无损失。
广播表与广播表 JOIN，相当于单机 JOIN，性能无损失。

>**目前暂不支持“单表（普通表）”和“分表”进行 join 操作；**

```
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
