
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).


## JOIN (Distributed JOIN)
Because there are multiple physical nodes in DCDB, some join operations may involve data of multiple physical nodes. This JOIN of data across multiple physical nodes is generally called distributed JOIN.

- If a JOIN-related table has equal conditions of a shardkey (as shown below), such data will be automatically stored on the same physical node due to the consistency principle of sub-tables. In this case, this works as a stand-alone JOIN with the best performance. For more information about how to choose the sub-table shardkey, please see [FAQ](https://cloud.tencent.com/document/product/557/10572).
- If it involves data across physical nodes, the proxy will pull data from other nodes and cache it first. Due to the network data transmission, the performance will be affected.

### Equal condition of shardkey (no performance loss)
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
### Unequal condition of shardkey (performance loss)
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
### JOIN related to broadcast tables and single tables (regular tables)

If it is a JOIN between single tables (regular tables), it works as a stand-alone JOIN with no performance loss.
If it is a JOIN between a broadcast table and a sub-table, it works as a stand-alone JOIN with no performance loss.
If it is a JOIN between broadcast tables, it works as a stand-alone JOIN with no performance loss.

>**Currently, the JOIN operation is not supported for "single table (regular table)" and "sub-table";**

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

