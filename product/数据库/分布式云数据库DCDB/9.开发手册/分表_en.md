DCDB for Percona, MariaDB supports sub-tables, which means horizontally dividing a big table into multiple databases by using shardkeys. This document will explain how to create sub-tables:


## How to Select shardkey

A shardkey cannot be easily changed once it is determined, so it is necessary for developers to evaluate the selected shardkey beforehand. Consider two points when selecting a shardkey:

- Whether the shardkey is helpful to achieve balanced data storage and access;
- Whether the shardkey can be used by multiple associated tables. (Data with the same shardkey is stored in the same physical set. Most business logics can directly perform join operation in single node without going through distributed transaction logic, which greatly improves efficiency)

>Suppose a business contains two tables, one is used to store basic user information, the other stores user order information. If user ID is selected as shardkey, theoretically, data distribution and access will be balanced. In this case, basic information and order information of an individual user will be stored in the same backend database, making subsequent operations easier (such as join).

## Restrictions When Selecting shardkey

The value of shardkey is specified in the last step when creating a common sub-table. The value is the name of a field in the table, and is later used for selecting SQL route:

Restrictions on shardkey:

	1. If there is a primary key or unique index, the shardkey field must be a part of the primary key and all unique indexes.
	2. The type of shardkey field must be int, bigint, smallint/char/varchar.
	3. Try to use ascii code as the value of shardkey field, because gateway does not convert character set and different character sets will be routed to different partitions.
	4. Do not update the value of shardkey field. If this is necessary, delete it first, then insert new value.
	5. `shardkey=` should be placed at the end of the create statement as shown in the following example.
	6. The shardkey field should always be included when accessing data, if possible.

## Create Sub-table
```
	mysql> create table test.right ( a int not null,b int not null, c char(20) not null,primary key(a,b) ,unique key(a,c)) shardkey=a;
	Query OK, 0 rows affected (0.12 sec)
```

>`shardkey'` is a keyword for the system to identify a shard field and should not be occupied.
>`Shardkey=noshardkey_allset` is the keyword to specify a table as a broadcast table. This indicates the table is not divided, but will be stored in every physical shard.

## Common DML Operations

When using a sub-table, there are certain requirements on DML as shown below ("a" is the shardkey):

### Include shardkey in SELECT Statement
Include the shardkey field in SELECT statement if possible, because distributed routing uses "hash" mode by default.

- If `=` or `in` is used, the routing automatically jumps to the corresponding shard. Such cases have the highest efficiency.
- If no `=` or `in` is used, the distributed system automatically scans the whole table, then gathers the result set at the gateway. Such cases have the lowest efficiency:

Example: the following two SQL statements are directly sent to the corresponding database based on the value of shardkey, and are usually processed within 5 ms.
```
	mysql> select a,b,c from test.test1 where a=2 order by b;
	mysql> select a,b,c from test.test1 where a in (2) order by b;
```
Example: the following SQL statements are sent to all backend databases, then additional data collection and sorting are required, which usually takes 5 to 20 ms.
```
	mysql> select a,b,c from test.test1 where a>2 order by b;
	mysql> select a,b,c from test.test1 where c=2 order by b;
```
### insert/replace Fields Must Include shardkey

Insert/replace fields must include shardkey, otherwise the routing will not know which physical shard to insert data into and the system will refuse to execute the SQL statement;
```
	mysql> insert into test.test1 (b,c) values(4,"record3");
	ERROR 1105 (07000): Proxy Warning - sql have no shardkey

	mysql> insert into test.test1 (a,c) values(4,"record3");
	Query OK, 1 row affected (0.01 sec)
```
>This is not required when using broadcast tables or single tables.


### delete/update Fields Must Include shardkey

For security, "where" condition must be included in SQL statements such as delete/update, or the system will refuse to execute them. Also, shardkey should be included in the "where" condition, just as in the select statement:
```
	mysql> delete from test.test1;
	ERROR 1005 (07000): Proxy Warning - sql is not legal,tokenizer_gram went wrong
	mysql> delete from test.test1 where a=1;
	Query OK, 1 row affected (0.01 sec)
```
>This is not required when using broadcast tables or single tables.

### Modify the Value of shardkey Field
Likewise, you cannot modify the value of shardkey field using "update". If necessary, insert the value first, then delete it.
```
	mysql> update test.test1 set a=10 where d=1;
	ERROR 7013 (HY000): Proxy ERROR:combine_sql_key return null,something went wrong
	mysql> update test.test1 set d=1 where a=1;
	Query OK, 0 rows affected (0.00 sec)
```
>You cannot change the type of shardkey field, modify field name, delete or replace the shardkey field, unless you create a new table.


## FAQs:

There is no primary key in the table:
```
	mysql> create table test.e1 ( a int ,b int) shardkey=a;
	ERROR 1105 (HY000): This table type requires a primary key
```

Primary key or unique key does not contain shardkey:
```
	mysql> create table test.e2 ( a int not null,b int not null, c char(20) not null,primary key(a,b) ) shardkey=c;
	ERROR 1105 (HY000): A PRIMARY KEY must include all columns in the table's partitioning function
```

Spelling error in "shardkey" or in the column name:
```
	mysql> create table test.e3 ( a int key,b int,c char(20)) shardkey1=d;
	ERROR 1911 (HY000): Unknown option 'shardkey1'
	mysql> create table test.e4 ( a int key,b int,c char(20)) shardkey=d;
	ERROR 7008 (HY000): Proxy ERROR:shardkey must be one of the column
```
