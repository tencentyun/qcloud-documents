
> If you need to view or download the full development documents, please see [Development Guide for DCDB](https://cloud.tencent.com/document/product/557/7714).

### Globally Unique Digital Sequence
The globally unique digital sequence (auto_increment) is supported. Currently, it can ensure the global uniqueness and increment of the auto-increment field, but not the monotonic increment (the absolute increment in chronological order). The auto_increment is 8 bytes in length with the maximum of 18446744073709551616. You do not need to worry about the value overflow. Specific usage is shown below:

Creating:
```
	mysql> create table auto_inc (a int,b int,c int auto_increment,d int,key auto(c),primary key p(a,d)) shardkey=d;
	Query OK, 0 rows affected (0.12 sec)
```
Inserting:
```
	mysql>  insert into shard.auto_inc ( a,b,d,c) values(1,2,3,0),(1,2,4,0);
	Query OK, 2 rows affected (0.05 sec)
	Records: 2  Duplicates: 0  Warnings: 0

	mysql> select * from shard.auto_inc;
	+---+------+---+---+
	| a | b    | c | d |
	+---+------+---+---+
	| 1 |    2 | 2 | 4 |
	| 1 |    2 | 1 | 3 |
	+---+------+---+---+
	2 rows in set (0.03 sec)
```
Note: Since only the global uniqueness and increment of the auto-increment field are ensured, there could be void in the auto-increment field when the node is scheduling the processes of switching, restarting. For example:
```
    mysql> insert into shard.auto_inc ( a,b,d,c) values(11,12,13,0),(21,22,23,0);
    Query OK, 2 rows affected (0.03 sec)
    mysql> select * from shard.auto_inc;
    +‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
    | a | b | c | d |
    +‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
    | 21 | 22 | 2002 | 23 |
    | 1 | 2 | 2 | 4 |
    | 1 | 2 | 1 | 3 |
    | 11 | 12 | 2001 | 13 |
    +‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+‐‐‐‐‐‐+
    4 rows in set (0.01 sec)
```
Modify the current value
```
	alter table auto_inc auto_increment=100
```

If the auto increment is not specified, it can be obtained via "select last_insert_id()".
```
	mysql> insert into auto_inc ( a,b,d,c) values(1,2,3,0),(1,2,4,0);
	Query OK, 2 rows affected (0.73 sec)

	mysql> select * from auto_inc;
	+---+------+------+---+
	| a | b    | c    | d |
	+---+------+------+---+
	| 1 |    2 | 4001 | 3 |
	| 1 |    2 | 4002 | 4 |
	+---+------+------+---+
	2 rows in set (0.00 sec)

	mysql> select last_insert_id();
	+------------------+
	| last_insert_id() |
	+------------------+
	| 4001             |
	+------------------+
	1 row in set (0.00 sec)
```
> Note: Currently, "select last_insert_id()" can only be used with auto-increment field of the shard table. Single table (regular table) and broadcast table are not supported;

