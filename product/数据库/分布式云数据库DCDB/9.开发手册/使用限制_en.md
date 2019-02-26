### Restriction on User Permission
For the current version, you cannot configure user permission through command lines. You need to log in to Tencent Cloud console to configure.
```
	mysql> grant all on *.* to 'test'@'%' identified by 'test123';
	ERROR 7009 (HY000): Proxy ERROR:proxy do not support such use yet
```	

### Unsupported Features
1. Custom data type and functions.
2. View, storage procedure, trigger and cursor.
3. Foreign key and self-built partition.
4. Compound statements such as BEGIN END and LOOP.
5. For now, only "derived table" with "shardkey" is supported for sub-query.

### Restrictions on Database Status Information
1. Since the SQL for querying the database status information is randomly sent to a physical shard, the statistics may be inaccurate.
2. The SQL for querying system table is also randomly sent to a physical shard.

### Restrictions on Aggregate Functions
1. If you aggregate after `distinct`, "where" condition must contain "shardkey".
```
select count(distinct a),sum(distinct a),avg(distinct a) from table where sk=\*\*
```
2. If `distinct`, `order by` and `group by` are followed by a function, the function must appear in the `select` field and must be defined by an alias which is used after corresponding `distinct`, `order by` and `group by`.
```
select concat(...) as substr from table where ... order by substr
```

3. The `group by` field must be contained in the `select` field. For example, the `select` field below must contain the "b" field.
```
select count(a),b from test group by b
```

### Restrictions on JOIN
For now, DCDB only supports the join operation in a single shard. This means all SQLs in a transaction must be based on the same shard, so the shardkey field must be specified.
```
mysql> create table test1 ( a int , b int, c char(20) ) shardkey=a;
Query OK, 0 rows affected (1.56 sec)
mysql> create table test2 ( a int , d int, e char(20) ) shardkey=a;
Query OK, 0 rows affected (1.46 sec)
mysql> insert into test1 (a,b,c) values(1,2,"record1"),(2,3,"record2");
Query OK, 2 rows affected (0.02 sec)
mysql> insert into test2 (a,d,e) values(1,3,"test2_record1"),(2,3,"test2_record2");
Query OK, 2 rows affected (0.02 sec)
mysql> select * from test1 join test2 on test1.a=test2.a;
ERROR 1105 (07000): Proxy Warning - join shardkey error
mysql> select * from test1 join test2 on test1.a=test2.a where test1.a=1;
+------+------+---------+------+------+---------------+
| a     | b     | c        | a     | d     | e                |
+------+------+---------+------+------+---------------+
| 1     | 2     | record1 | 1    | 3      | test2_record1 |
+------+------+---------+------+------+---------------+
1 row in set (0.00 sec)
```
>**Note:**
>`mysql> select * from test1 join test2 on test1.a=test2.a;` will be supported in subsequent versions, but it should be inner join and the "where" condition of inner join must be that the "shardkey" fields of two tables are equal.

### Restrictions on Preprocessing
SQL type supports:
```
PREPARE Syntax
EXECUTE Syntax
```
Binary protocol supports:
```
COM_STMT_PREPARE
COM_STMT_EXECUTE
```
The code example is shown as below:
```
	mysql> select * from test1;
	+---+------+
	| a | b    |
	+---+------+
	| 5 |    6 |
	| 3 |    4 |
	| 1 |    2 |
	+---+------+
	3 rows in set (0.03 sec)
	
	mysql> prepare ff from "select * from test1 where a=?";
	Query OK, 0 rows affected (0.00 sec)
	Statement prepared
	
	mysql> set @aa=3;
	Query OK, 0 rows affected (0.00 sec)
	
	mysql> execute ff using @aa;
	+---+------+
	| a | b    |
	+---+------+
	| 3 |    4 |
	+---+------+
	1 row in set (0.06 sec)
```

### Restrictions on SQL
The following syntax is not supported for the creation of tables:
```
	CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
	    [(create_definition,...)]
	    [table_options]
	    [partition_options]
	    select_statement
	Or:
	CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
	    { LIKE old_tbl_name | (LIKE old_tbl_name) }
```
The following syntax is not supported for INSERT:
```
	INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
	    [INTO] tbl_name [(col_name,...)]
	    SELECT ...
	    [ ON DUPLICATE KEY UPDATE
	      col_name=expr
	        [, col_name=expr] ... ]
```
The following syntax is not supported for SELECT:
```
	SELECT
	    [INTO OUTFILE 'file_name'
	        [CHARACTER SET charset_name]
	        export_options
	      | INTO DUMPFILE 'file_name'
	      | INTO var_name [, var_name]]
```
KILL is not supported.

### Supported SQL Types
DDL syntax is compatible, please see [DDL Statements](https://cloud.tencent.com/document/product/557/8764).
```
	CREATE TABLE Syntax
	CREATE INDEX Syntax
	DROP TABLE Syntax
	DROP INDEX Syntax
	ALTER TABLE Syntax
	TRUNCATE TABLE Syntax
```
DML syntax is compatible, please see [Create a Sub-Table](https://cloud.tencent.com/document/product/557/8767)
```
	INSERT Syntax
	REPLACE Syntax
	UPDATE Syntax
	DELETE Syntax
	SELECT Syntax
```
Prepare syntax is compatible
```
	PREPARE Syntax
	EXECUTE Syntax
	DEALLOCATE PREPARE Syntax
```
Prepare syntax example:
```
	mysql> prepare ff from 'select * from test.test1 where a=?';
	mysql> set @a=1;
	mysql> execute ff using @a;
	mysql> deallocate prepare ff;
```
Database tool commands
```
	DESCRIBE Syntax
	EXPLAIN Syntax
	USE Syntax
```	
Database management syntax is compatible
```
	SET Syntax, modification of global variables is not supported
	SHOW Syntax
	SHOW COLUMNS Syntax
	SHOW CREATE TABLE Syntax
	SHOW INDEX
	SHOW TABLES Syntax
	SHOW TABLE STATUS Syntax
	SHOW TABLES Syntax
	SHOW VARIABLES Syntax
```
Example of database management syntax:
```
	mysql> show columns from test.test1;
	mysql> show index from test.test1;
	mysql> show table status;	
	mysql> show tables from test;	
	mysql> show variables like "%char%";	
```
"proxy" randomly sends other SHOW commands to a physical shard (set).
