> TDSQL kernel is modified based on MariaDB 10.0, so it is basically the same with MariaDB 10.0 in terms of compatibility. Details are as follows:

## Compatibility Between TDSQL and MySQL
### Updated: Dec 31, 2015
- Data files and table definition files are binary compatible.
- All client APIs and protocols are compatible.
- All file names, binary files, paths and port numbers are the same.
- All connectors (including those for PHP, Perl, Python, Java, .NET, Ruby and MySQL) can be used on MariaDB without any modifications.
- You can use MySQL clients to connect to TDSQL.

## Incompatibility Between TDSQL and MySQL 5.6
### Updated: Dec 31, 2015
- The GTID of TDSQL is not compatible with the GTID of MySQL 5.6. In other words, MySQL cannot act as a slave database for TDSQL;
- MySQL can send alarms and TDSQL can work normally if only the prefix of the option is provided, for example, replace "--big-tables" with "--big-table". That is, MySQL and TDSQL are compatible if only the prefix provided can uniquely identify the option.
- To ensure that the CREAT TABLE ... SELECT command can always function when copied as line or as command, the CREAT TABLE ... SELECT command in TDSQL will be converted into CREAT OR RPLACE in the slave database before it is executed. The advantage is that the slave database can work normally even if it crashes while executing "CREAT TABLE ... SELECT" command.

### Updated: Jan 12, 2016
- By default, the **innodb_page_size** of TDSQL and MySQL is set to *4 KB* and 16 KB respectively, so that the length of single index is limited to 768 Bytes.

### Updated: Jan 22, 2016
- Under the JDBC application, if **mysql-connector-java.jar** is used, an error may occur while executing the following sub-query SQL:
```
For example:
select * from (select col_a , col_b , from tbl_a where col_b=1) tx where tx.col_a = '01';
Error: Table db.tx' doesn't exist
```

- If **mariadb-java-client-1.2.x.jar** is used, an exception may occur while executing the following sub-query SQL:

```
For example:
select col_a as a from tbl;
Even though the query is successful, you can obtain the result from the result set using only the original column name, rather than alias.
For example, an error may occur while obtaining the column data using the alias "a". So the value can only be obtained using "col_a".
```

- When **mariadb-java-client-1.3.x.jar** is used, if the "autocommit" is set as "global" or "session", an error may occur while implement "commit" method.
- Test shows that in the framework Hibernate or Entityframework, if you configure the parameter ** useAffectedRows = false ** and request the update statement to return **matched rows**, since Mariadb ignores the field **CLIENT_FOUND_ROWS** pushed by the client while establishing connection, the configuration of parameter **useAffectedRows=false** is invalid and the update statement actually returns "affected rows".

```
For example:
	Execute: update tal_a set col_a="value";
	If "col_a" is "value", the update operation is not be performed at the moment. affected rows=0 and matched rows=1.
	At this point, if the framework requests server to return 1, but 0 is actually returned, the judgment of the framework may fail.
```

