The unique global digital sequence of DCDB for Percona and MariaDB (hereinafter the "sequence", with a type of "unsigned long" and length of 8 bytes) is used in the same way with AUTO_INCREMENT of MySQL. Currently, DCDB for Percona and MariaDB can ensure the global uniqueness and orderly increment of this field, but not the continuity. Details are shown below:

## Creating "sequence"
DCDB for Percona and MariaDB creates sequence using the same syntax as auto-increment field of mysql. Example:

```
	mysql> create table auto_inc (a int,b int,c int auto_increment,d int,key auto(c),primary key p(a,d)) shardkey=d;
	Query OK, 0 rows affected (0.12 sec)
```

## Inserting "sequence"
DCDB for Percona and MariaDB inserts sequence using the same syntax as auto-increment field of mysql. DCDB for Percona and MariaDB can automatically assign a unique global value without the need to pass the field value or 0/NULL. Example:

```
	mysql> insert into shard.auto_inc ( a,b,d,c) values(1,2,3,0),(1,2,4,0);
	Query OK, 2 rows affected (0.05 sec)
	Records: 2 Duplicates: 0 Warnings: 0
	
	mysql> select last_insert_id();
	+------------------+
	| last_insert_id() |
	+------------------+
	| 1                |
	+------------------+
	1 row in set (0.00 sec)
	
	mysql> select * from shard.auto_inc;
	+---+------+---+---+
	| a | b    | c | d |
	+---+------+---+---+
	| 1 |    2 | 2 | 4 |
	| 1 |    2 | 1 | 3 |
	+---+------+---+---+
	2 rows in set (0.03 sec)

	mysql> insert into shard.auto_inc ( a,b,d,c) values(2,2,3,NULL),(2,2,4,NULL);
	mysql> insert into shard.auto_inc ( a,b,d) values(3,2,3),(3,2,4);

	mysql> select * from shard.auto_inc;
	+---+------+---+---+
	| a | b    | c | d |
	+---+------+---+---+
	| 1 |    2 | 2 | 4 |
	| 2 |    2 | 4 | 4 |
	| 3 |    2 | 6 | 4 |
	| 1 |    2 | 1 | 3 |
	| 2 |    2 | 3 | 3 |
	| 3 |    2 | 5 | 3 |
	+---+------+---+---+
	6 rows in set (0.03 sec)
```	
    
## Modifying the Current "sequence" Value
Example:

```
	alter table auto auto_increment=100
```

## Note
Due to the special architecture of distributed database, the continuity (but not global uniqueness) of sequence cannot be ensured when the proxy is scheduled, switched over, and restarted upon exception. Example:

```
    mysql> insert into shard.auto_inc ( a,b,d,c) values(11,12,13,0),(21,22,23,0);
    Query OK, 2 rows affected (0.03 sec)

	mysql> select * from shard.auto_inc;
	+----+------+------+----+
	| a  | b    | c    | d  |
	+----+------+------+----+
	| 21 |   22 | 2002 | 23 |
	|  1 |    2 |    2 |  4 |
	|  2 |    2 |    4 |  4 |
	|  3 |    2 |    6 |  4 |
	|  1 |    2 |    1 |  3 |
	|  2 |    2 |    3 |  3 |
	|  3 |    2 |    5 |  3 |
	| 11 |   12 | 2001 | 13 |
	+----+------+------+----+
	8 rows in set (0.03 sec)

	mysql> select last_insert_id();
	+------------------+
	| last_insert_id() |
	+------------------+
	| 2001             |
	+------------------+
```



