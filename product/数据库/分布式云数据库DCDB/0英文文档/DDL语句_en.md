DCDB for Percona, MariaDB supports common DDL statements, such as CREATE DATABASE, CREATE TABLE, ALTER TABLE, etc.


## Create Table

DCDB for Percona, MariaDB can create three types of tables: sub-table, small table and single table. Sub-tables are used when a single database cannot accommodate all tables, in which case there will be certain restrictions for SQL. For more information, please see <SQL Compatibility>. Single tables are mainly used when data can be stored in a single database and SQL is relatively more complex.

### Sub-table: Please see <sub-table>

See Sub-tables for details.

### Broadcast Table
Broadcast table works as the broadcast feature of a small table. If a table is set as broadcast table, all operations made to this table will be broadcast to all physical shards (sets), and each set possesses all data of the table.

```
	mysql> create table test.global_table ( a int, b int,primary key(b)) shardkey=noshardkey_allset
```
> The broadcast feature of small table can simplify join operations and complex calculations across physical shards (sets). It is often used in tables that are frequently used but seldom modified, for example, configuration tables.
> If a broadcast table needs to be updated, then response in given to transaction only if all sets are updated. Hence, there is no need to worry about data inconsistency between sets.

### Single Table
Single table is used to store tables that do not need sharding. All data of this table is stored in the first physical shard (set), and all tables of this type are placed in the first physical shard (set), with exactly the same syntax and usage methods as MySQL. You can consider it as a non-distributed table.
```
	mysql> create table test.noshard_table ( a int, b int,primary key(b)) 
```

> The system automatically balances storage capacity of the first physical shard (set) in order to prevent it from being overloaded by multiple single tables.



## Alter Table

The syntax used to alter table is the same as MySQL. Currently, you cannot modify the shardkey column:

### Add Column
	mysql> alter table test.test1 add column d varchar(20);
	Query OK, 0 rows affected (0.10 sec)
	
### Add Index
	mysql> alter table test.test1 add index index_c(c);
	Query OK, 0 rows affected (0.06 sec)

### Delete Column
	mysql> alter table test.test1 drop column b;
	Query OK, 0 rows affected (0.10 sec)

### Delete Index
	mysql> alter table test.test1 drop index index_c;
	Query OK, 0 rows affected (0.06 sec)

### Modify Field
	mysql> alter table test.test1 modify column b varchar(20);
	Query OK, 0 rows affected (0.16 sec)

### Clear Table Data
	mysql> truncate table test.test1;
	Query OK, 0 rows affected (0.16 sec)	

## Delete Table

The syntax used to delete a table is exactly the same as MySQL. DCDB for Percona, MariaDB automatically goes to one or more back-end databases to delete table, based on table type.

	mysql> drop table test.ff;
	Query OK, 0 rows affected (0.07 sec)
	

