DCDB supports common DDL statements, such as CREATE DATABASE, CREATE TABLE, and ALTER TABLE.

## Create Table

DCDB can create three types of tables: sub-table, broadcast table and single table. Sub-tables are used when a single database cannot accommodate all tables. Each broadcast table possesses all data in all physical multiparts and is suitable for the "join" operation across physical multiparts. Single tables are used when data can be stored in a single database and the SQL is relatively more complex.

### Sub-table
DCDB supports sub-tables. With the table key (shardkey), big tables can be horizontally split into multiple databases to form a "separate" database "multipart". Several multiparts together form a logically complete database instance. For more information on how to create sub-tables, please see [Create Sub-table](https://cloud.tencent.com/document/product/557/8767).

### Broadcast Table
Broadcast table works as the broadcast feature of a small table. If a table is set as broadcast table, all operations made to this table will be broadcast to all physical multiparts (sets), and each set possesses all data of the table.
```
mysql> create table test.global_table ( a int, b  int,primary key(b)) shardkey=noshardkey_allset
```
The broadcast function of the small table can simplify join operations and complex calculations across physical multiparts (sets). It is often used in tables that are frequently used but seldom modified, for example, configuration tables.
If a broadcast table needs to be updated, then response in given to transaction only if all sets are updated. Therefore, there is no need to worry about the data inconsistency between sets;

### Single Table
Single table is used to store tables that do not need multiparts. All data of this table is stored in the first physical multipart (set), and all tables of this type are placed in the first physical multipart (set), with exact the same syntax and usage methods as MySQL. You can consider it as a non-distributed table.
```
mysql> create table test.noshard_table ( a int, b  int,primary key(b)) 
```

> **Note:**
> The system automatically balances the storage capacity of the first physical multipart (set) to prevent it from being overloaded by multiple single tables.

## Alter Table
The syntax used to alter table is the same as MySQL. Currently, you cannot modify the shardkey column.

### Add Column
```
	mysql> alter table test.test1 add column d varchar(20);
	Query OK, 0 rows affected (0.10 sec)
```	
### Add Index
```
mysql> alter table test.test1 add index index_c(c);
Query OK, 0 rows affected (0.06 sec)
```
### Delete Column
```
	mysql> alter table test.test1 drop column b;
	Query OK, 0 rows affected (0.10 sec)
```
### Delete Index
```
	mysql> alter table test.test1 drop index index_c;
	Query OK, 0 rows affected (0.06 sec)
```
### Modify Field
```
	mysql> alter table test.test1 modify column b varchar(20);
	Query OK, 0 rows affected (0.16 sec)
```
### Clear Table Data
```	
	mysql> truncate table test.test1;
	Query OK, 0 rows affected (0.16 sec)	
```
## Delete Table
The syntax used to delete a table is exactly the same as MySQL. Based on the table type, DCDB deletes the table automatically in one or more backend databases.
```
	mysql> drop table test.ff;
	Query OK, 0 rows affected (0.07 sec)
```

