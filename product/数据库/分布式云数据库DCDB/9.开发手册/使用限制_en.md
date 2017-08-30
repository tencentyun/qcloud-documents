
### Restriction on User Permission

For the current version, you cannot configure user permission through command lines. You need to log in to Tencent Cloud console to configure.
```
	mysql> grant all on *.* to 'test'@'%' identified by 'test123';
	ERROR 7009 (HY000): Proxy ERROR:proxy do not support such use yet
```	

### Unsupported Features

	1: Custom data type, custom function
	2: View, storage procedure, trigger, cursor
	3: Foreign key, self-built partition
	4: Compound statement, such as "BEGIN END", "LOOP", etc.
	4: Sub-query, "having" statement ("derived table" with "shardkey" is supported)

### Restrictions on Database Status Information

	1: Since the SQL for querying the database status information is randomly sent to a physical shard, the statistics may be inaccurate.
	2: The SQL for querying system table is also randomly sent to a physical shard.

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
The following syntax is not supported for "insert":
```
	INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
	    [INTO] tbl_name [(col_name,...)]
	    SELECT ...
	    [ ON DUPLICATE KEY UPDATE
	      col_name=expr
	        [, col_name=expr] ... ]
```
The following syntax is not supported for "select":
```
	SELECT
	    [INTO OUTFILE 'file_name'
	        [CHARACTER SET charset_name]
	        export_options
	      | INTO DUMPFILE 'file_name'
	      | INTO var_name [, var_name]]
```
KILL is not supported


### Supported Type of SQL

DDL syntax is compatible, please see < DDL statement>
```
	CREATE TABLE Syntax
	CREATE INDEX Syntax
	DROP TABLE Syntax
	DROP INDEX Syntax
	ALTER TABLE Syntax
	TRUNCATE TABLE Syntax
```
DML syntax is compatible, please see < sub-table>
```
	INSERT Syntax
	REPLACE Syntax
	UPDATE Syntax
	DELETE Syntax
	SELECT Syntax
```
"prepare" syntax is compatible
```
	PREPARE Syntax
	EXECUTE Syntax
	DEALLOCATE PREPARE Syntax
```

Example:
```
	mysql> prepare ff from 'select * from test.test1 where a=?';
	
	mysql> set @a=1;

	mysql> execute ff using @a;

	mysql> deallocate prepare ff;
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

Example:
```
	mysql> show columns from test.test1;
	mysql> show index from test.test1;
	mysql> show table status;	
	mysql> show tables from test;	
	mysql> show variables like "%char%";	
```
"proxy" randomly sends other SHOW commands to a physical shard (SET)

Database tool commands
```
	DESCRIBE Syntax
	EXPLAIN Syntax
	USE Syntax
```	



