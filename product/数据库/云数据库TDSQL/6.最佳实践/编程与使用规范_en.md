

> If you have any suggestions on the specifications, contact Tencent Cloud staff or directly send mails to benhu@tencent.com


## 1. Introduction


### 1.1. Document Purpose

This document is intended to clarify key technical criteria and guidelines for various stages of entire lifecycle of CDB for MariaDB (TDSQL) technology and application, including planning, designing, installation, deployment, management and OPS, to facilitate the unified construction and management of CDB for MariaDB (TDSQL) application projects, and to improve normalization, performance support and maintainability of CDB for MariaDB (TDSQL) technology applications.


### 1.2. Intended Audience

CDB for MariaDB (TDSQL) projects-related designers, developers, managers and OPS staff.


## 2. Design Specifications

### 2.1. Database Design Principles

- CDB for MariaDB (TDSQL) is designed for OLTP application scenarios, and does not apply to most complex OLAP.
- Anti-normal form design:
  - It is unnecessary to meet the third normal form, and foreign keys are not recommended.
    - Foreign keys are used to protect referential integrity and can be achieved on the business end
    - Proper redundancy design reduces multiple tables Join query, and helps adapt to the scaling out of MPP architecture
    - Optimization is directly based on I/O and queries
- Fully consider separation of business logic and data. The database is only used as a persistent storage system of relational data that ensures ACID characteristics. It is recommended to avoid using custom functions, storage procedures, triggers and views
- Fully consider the overall security design of the database, and separate database management permission from use permission
- Fully consider access frequency and performance needs of the specific data object, and design good database performance in combination with the server, storage and other needs
- Fully consider data growth model to determine whether to use "distributed (horizontal sharding)" mode
- Fully consider the security level of business data to design proper backup and recovery policies


### 2.2. Design Specifications of Database Model
#### 2.2.1. Basic Specifications

- Only use InnoDB instead of MyISAM as the storage engine because InnoDB has the following characteristics compared with MyISAM:
  - Fully supports ACID
  - Features crash self-test and recovery
  - Features row-level locking, ensuring high concurrency
  - Better exerts performance of multi-core CPU
  - Comes with a cache pool to better use memory
- Use a unified character set for all tables. It is strongly recommended to use UTF8 or UTF8MB4 character set.
- Do not store big data such as pictures and binary files in the database
- Design the specifications of a single table in advance, including the number of rows and size
- Control the total length of a single-row field, set innodb\_page\_size reasonably, and use COMPACT row format to avoid row overflow.

#### 2.2.2. Naming Specifications of Database Object

Naming specifications of database object apply to designers, managers, developers of CDB for MariaDB (TDSQL). System database tables and other objects coming with CDB for MariaDB (TDSQL) products are not within the constraint of the specifications.

Database objects are named based on the following specifications:

- Use meaningful English words to name an object, and avoid abbreviations unless established by popular usage
- When naming an object such as index and constraint, the involved tables, fields and so on also need to be named. At this point, you can use abbreviations to name them, and abbreviation rules and the number of characters should be consistent.
- Use only a combination of lowercase letters, numbers, and underscores
- Name length should not exceed 32 characters
- Do not use SQL keywords
- An object name includes at least: object type, parent object name and object name

The table below lists naming rules of different database objects:

| Database Object | Format | Sample | Description |
| --- | --- | --- | --- |
| Database (SCHEMA) | db\_&lt;database name&gt; | db\_user | Database that stores user data |
| Table | tbl\_&lt;table name&gt; | tbl\_employees | Table that stores employee information |
|Primary key | pk\_&lt;table name&gt;\_&lt;field name&gt;[\_field name] | pk\_emlo\_id\_name | ID and name fields of the tbl\_employees table constitute the primary key. However, in CDB for MariaDB (TDSQL), the primary key name is meaningless so that the system ignores the name and names the object as PRIMARY |
| Unique index | uidx\_&lt;table name&gt;\_&lt;field name&gt;[\_field name]\_&lt;number&gt; | uidx\_empl\_name\_age\_1 | The first unique index created for name and age fields of the tbl\_employees table|
| Index | idx\_&lt;abbreviation of table name;abbreviation of column name&gt;[\_abbreviation of column name]\_&lt;number&gt; | idx\_empl\_name\_age\_1 | The first index created for name and age fields of the tbl\_employees table |
| Foreign key | fk\_&lt;table name&gt;\_&lt;name of associated table&gt;\_&lt;field name&gt;[\_field name] \_&lt;name of associated field&gt;[\_name of associated field] | fk\_empl\_user\_uid\_id | The ID field that the foreign key of uid field of tbl\_employees table constrains to the tbl\_user |
| View | v\_&lt;view name&gt; | v\_female | - |
| Storage procedure | sp\_&lt;name of storage procedure&gt; | sp\_add\_empl |  - |
| Custom function | f\_&lt;function name&gt; | f\_count\_empl | -  |
| Trigger | trg\_&lt;Trigger name&gt; | trg\_update\_empl | -  |
| Temporary table | tmp\_&lt;table name&gt; | tmp\_latecomer | - |

Table 1
#### 2.2.3. Instance Configuration

After applying for a CDB for MariaDB (TDSQL) instance, you need to initialize it, during which you should specify two important metrics:

- Character set: Specify the default character set for the database table
-`innodb_page_size`: The size of the page stored in the InnoDB table file. Page is the smallest unit stored in the file by InnoDB engine, and the default value is 16K in the original MySQL. To configure the value, you need to consider the following:
  - The single-row data size of the primary table in the instance
  - InnoDB table's `ROW_FORMA`T configuration
  - Whether to use SSD

After initialization, you can set the following parameters:

- Based on business needs, you can set `STRICT_ALL_TABLES` or`STRICT_TRANS_TABLES` flags through the SQL MODE to enable the STRICT mode. Never write data that do not meet the definition of field type. The differences between the two flags are as follows:
  - `STRICT_ALL_TABLES`: For a storage engine that does not support transactions, if multi-row data are updated simultaneously, and the data in the non-first row do not meet the definition, the data above this row will be updated while the data in and below this row will not
  - `STRICT_TRANS_TABLES`: For a storage engine that does not support transactions, if the data in the first row do not meet the definition, the request will be rejected, or else, the request will operate in normal mode
- CDB for MariaDB (TDSQL) starts automatic transaction submission (AUTOCOMMIT) by default. It is recommended to keep the feature enabled.
- CDB for MariaDB (TDSQL) sets REPEATABLE-READ as the default transaction isolation level. You can adjust it to READ-COMMITED (default level of Oracle) based on your needs

#### 2.2.4. Database

Database in CDB for MariaDB (TDSQL) has different concepts from that in ORACLE, and can be considered as a SCHEMA similar to a folder of a table to help DBAs with classified management. When creating a database, besides database name, you are strongly recommended to specify parameters of the default character set for the database. For example:

```
 CREATE DATABASE `db_user` CHARSET ='utf8'  COLLATE='utf8_bin' 
```

#### 2.2.5 Table
##### 2.2.5.1. Table Parameter Settings

- The default `ROW_FORMAT` of the InnoDB table is COMPACT. You can specify a proper value based on your needs:
  - COMPACT: In the case of no row overflow, a row of data is stored in one data page, and data read efficiency is the highest
  - DYNAMIC: A row of data is stored at least two pages, with the data page only storing the pointer of the overflow page and the overflow page storing the data. Such structure brings the most concentrated index storage and the highest index access efficiency
  - REDUNDANT: Old format. Do not use it
  - COMPRESSED: Data is stored after compression to get the highest space utilization. However, using this format increases CPU and memory consumption, and system response time, and reduces throughput, so please use it with caution.
- You are strongly recommended to specify parameters of the default character set for the table
- File storage path and other physically-related parameters are not allowed to specify


##### 2.2.5.2. Primary Foreign Key and Constraint Design

- A primary key must be specified for InnoDB table
- It is not recommended to use a meaningful field as the primary key, but if the situation cannot be avoided, make sure that the field is unique and invariant in the real world (for example, the bank transaction serial number) to avoid modification to the primary key
- It is not recommended to use foreign keys, especially when database and tables are split automatically in the "distributed (horizontal sharding)" mode
- The shorter the fields constituting the primary key are, the higher the efficiency is The optimum fields for primary key is integer type
- If there are multiple unique keys, use the most common one as the primary key
- It is recommended to use auto increment fields as the primary key
- For field attributes, it is recommended to add NOT NULL constraint and use the default value, because using NULL value can cause the following negative effects:
  - NULL value does not work for many operators because it is ambiguous, increasing the complexity. For example, for a! = 5, the row of "a" being NULL cannot be matched
  - It is difficult to optimize queries
  - The composite index including NULL becomes invalid
- Use ENUM type instead of CHECK constraint because CDB for MariaDB (TDSQL) ignores CHECK constraint although no error occurs.

##### 2.2.5.3. Field Type Design

- For integer type, select a proper type based on the range of the stored value
- For unsigned integer type, add UNSIGNED keyword
- For string type, select a fixed-length type or a variable-length type based on the stored value
- Minimize the length of string type fields based on the stored value
- Avoid using TEXT/BLOB type, and do not store data such as pictures and binary files in the database
- For non-integers, it is recommended to use the accurate DECIMAL type instead of floating point type

The following table provides the main recommended data types, value ranges and storage requirements:

| Type | Value Range | Storage Requirements |
| --- | --- | --- |
| TINYINT[(M)] | -128-127 or 0-255 | 1 byte |
| SMALLINT[(M)] | -32768-32767 or 0-65535 | 2 bytes |
| INT[(M)] | -2147483648-214748364 or 0-4294967295 | 4 bytes |
| BIGINT[(M)] | -9223372036854775808-9223372036854775807 or 0-18446744073709551615 | 8 bytes |
| DECIMAL[(M[,D])] | Integer digits (M) is no more than 65 and decimal places (D) is no more than 30 | Variable-length |
|   |
| DATE | &#39;1000-01-01&#39;-&#39;9999-12-31&#39; | 3 bytes |
| TIME[(&lt;microsecond precision&gt;)] | &#39;-838:59:59.999999&#39;-&#39;838:59:59.999999&#39; | 5 bytes |
| DATETIME[(microsecond precision)] | &#39;1000-01-01 00:00:00.000000&#39;-&#39;9999-12-31 23:59:59.999999&#39; | 8 bytes |
| TIMESTAMP[(&lt;microsecond precision)] | &#39;1970-01-01 00:00:01&#39; (UTC)-&#39;2038-01-19 05:14:07&#39; (UTC) | 4 bytes |
|   |
| CHAR[(M)] | 0&lt;M&lt;=255 | Integer multiple of M. The value of M depends on string set settings |
| VARCHAR[(M)] | 0&lt;M&lt;65532/N | The value of N depends on string set settings |
| TEXT[(M)] | 0&lt;M&lt;65535/N | The value of N depends on string set settings |

Table 2

#### 2.2.6. Index

- Do not index low-selectivity columns, such as sex column
- For the combined index, put common or high-selectivity fields in the front
- For fields that need to be sorted frequently, you can add them to an index according to the most common sorting order
- For longer string type fields, you are recommended to use a prefix index
- Combine indexes when needed to avoid redundancy. For example, for (a, b) and (a) indexes, (a)should be removed
- The indexes of a single table should be within 5
- The fields for a single index should not exceed 5
- InnoDB engine of CDB for MariaDB (TDSQL) supports full-text index, but only in English currently

#### 2.2.7. Paging Design

Paging is the most common access model in applications. We can learn how to design a reasonable paging model through the following tests for several paging methods:

```
/*
 * ID is the primary key of the table post
*/
MySQL> SELECT sql_no_cache * FROM post LIMIT 20000,10; 
10 row in set (0.13 sec) 

MySQL> SELECT sql_no_cache * FROM post LIMIT 80000,10; 
10 rows in set (0.58 sec) 

MySQL> SELECT sql_no_cache id FROM post LIMIT 80000,10; 
10 rows in set (0.02 sec) 

MySQL> SELECT sql_no_cache * FROM post WHERE id>=323423 LIMIT 10; 
10 rows in set (0.01 sec) 

MySQL> SELECT * FROM post WHERE id >= ( SELECT sql_no_cache id FROM post LIMIT 80000,1 ) LIMIT 10 ; 
10 rows in set (0.02 sec)

```

It can be seen from the above results that we should not directly use the LIMIT m, n paging method

### 2.3. Database Security Design

- Design Principles for Database User Security
  - Database user permission is authorized according to the principle of minimum assignment
  - Database users includes managers, end users, maintenance staff, and backup staff
- Design specifications for database user permission
  - Except core maintenance staff of CDB for MariaDB (TDSQL), other users can not have SUPER permission account
  - Avoid simple passwords
  - CDB for MariaDB (TDSQL) supports field-level permission. Control permission subject and object according to the minimum principle
  - User permission settings should be consistent in development, test and production environments
- Never store cleartext passwords of any form in the database

1.
# 3. Development Specifications

  3.1.SQL Coding Specifications

- Characters in per line should not exceed 80. You can perform line feed and indent to avoid it
- Use two spaces to indent codes
- Capitalize keywords, such as SELECT
- Capitalize constant symbols, such as NULL
- Use notes when needed
  - Make a detailed note about the table use in front of the table creation statement
  - Use COMMNET clause to add notes at the end of each field
  - Use COMMENT clause to add a note to the table at the end of table creation statement
- Remove the redundant parentheses, for example:
```
((a AND b) AND c OR (((a AND b) AND (c AND d))))
```

- It should be optimized as follows:
```
(a AND b AND c) OR (a AND b AND c AND d)
```

- Remove repeated conditions, for example:
```
(B>=5 AND B=5) OR (B=6 AND 5=5) OR (B=7 AND 5=6)
```

- It should be optimized as follows:
```
B=5 OR B=6
```

### 3.2. SQL Statement Specifications
#### 3.2.1. Index and Partition

- Use USE INDEX or IGNORE INDEX reasonably for index selection
- It is recommended to use indexes for query conditions
- Note the field type and avoid type conversion because type conversion increases the CPU consumption, and even causes invalid index if the conversion fails
- To use a composite index, the query condition must include all the prefix fields. For example, for index (a, b, c), the query condition must be a, a and b, or a, b and c

#### 3.2.2. SELECT Column and WHERE Condition

- It is recommended to perform arithmetic operations at application-level instead of in database, for example:
```
SELECT a FROM tbl WHERE id*10=100;
```
- It is recommended to directly list the fields to be queried instead of directly using SELECT \*
- It is recommended to use UNION ALL instead of UNION because UNION removes duplicate records and perform sort
- The principle of using WHERE clause: Use indexes, simplify the clause, and make it match less rows
- In WHERE clause, use equivalence operators and avoid non-equivalence operators because the latter often cause invalid index (MySQL does not support range index)
- Even if an index is used, rows that WHERE clause match should not exceed 30% of the total rows of the table, or else the efficiency is still low, and InnoDB engine may stopping using index to scan the full table
- In LIKE clause, do not use % as the first character Use the full-text index for more complex needs
- If OR conditions are more than 3:
  - For OR conditions of different fields, replace them with UNION ALL
  - For OR conditions of the same field, replace them with IN
- Replace WHERE clause with HAVING clause if possible. For example:
```
SELECT id,COUNT(*) FROM tbl GROUP BY id HAVING age>=30;
```
- It should be replaced with:
```
SELECT id,COUNT(*) FROM tbl WHERE age>30 GROUP BY id;
```

- The combinations of ORDER BY and GROUP BY in a table should not exceed 3, or else you should perform optimization from the business logic perspective and split the table into multiple ones
- If you need no sorting, the GROUP BY clause should be GROUP BY NULL
- Use the primary key in WHERE clause
- In InnoDB table, avoid full table scan query through functions such as COUNT(\*). You can store this count value in another table
- Avoid subqueries

#### 3.2.3.DML Statements

- For statements such as UPDATE and DELETE, it is recommended to use WHERE clause, index fields, and the primary key
- Use INSERT ... ON DUPLICATE KEY update (INSERT IGNORE) to avoid unnecessary queries
- In INSERT, UPDATE and DELETE statements, do not use uncertain functions, such as RAND () and NOW ()
- Merge multiple INSERT statements into one for batch submission, and the data submitted at a time should no more than 500 rows.
- In UPDATE statement, never write &quot;,&quot; into AND because it is very dangerous. For example:
```
UPDATE tbl SET fid=fid+1000, gid=gid+1000 WHERE id > 2;
```
If it is written into

```
UPDATE tbl SET fid=fid+1000 AND gid=gid+1000 WHERE id > 2;
```
At this point, `fid+1000 AND gid=gid+1000` is assigned to fid and no warning occurs

- Use TRUNCATE instead of DELETE to delete a table

#### 3.2.4. Multiple Tables Join 

- In multiple tables Join, tables are sorted in ascending order based on the number of rows returned by WHERE clause, and table with the least number of rows returned is on the far left
- Avoid joining large tables. Generally, it is recommended to use Join when the records in the table do not exceed 10

 #### 3.2.5. Other Statements

- Use PREPARE statement when needed to provide performance and prevent SQL injection
- Split load SQL data into multiple SQL data to avoid big transactions
- To perform DDL operation on the table, you are recommended to use one SQL statement to complete DDL operation on one table. For example, to add a field b to table t, and then to create an index for an existing field a, you can use the following statement:
```
ALTER TABLE t ADD COLUMN b VARCHAR(10), ADD INDEX idx_a(a);
```
## 4. Database Management Specifications

### 4.1. Basic Requirements

Before CDB MariaDB (TDSQL) is installed, its installation programs checks system environment, including the following items:

| Check Items | Expected Results |
| --- | --- |
| Operating system version | Linux series |
| File handler | More than 100K |
| Time synchronization | NTP configuration is correct |
| User | Check whether the user specified for the installation exists |
| Installation directory | Check whether the installation directory exists and has write permission |
| Data directory | Check whether the specified data directory exists and has write permission |

Table 3

### 4.2. Selection of "Regular (No Sharding)" and "Distributed (Horizontal Sharding)"

You can select "distributed (horizontal sharding)" when the following conditions are met:

- The data in the table increase continuously, and will exceed the maximum storage capacity of stand-alone in the foreseeable future
- High volume of read and write is performed on the table, exceeding the maximum throughput of stand-alone
- Fully considered various limits to table design and use caused by database and table splitting

For information about service limits on "distributed (horizontal sharding)" version, please see  [Distributed Version Development Instruction](https://cloud.tencent.com/document/product/557)

### 4.3. Master/Slave Configuration and Disaster Recovery
> Currently, CDB for MariaDB (TDSQL) features the following:


- It supports the configuration of one master and multiple slaves and can automatically select one slave as the master when the master crashes
- You can customize the number of slaves. Multiple slaves provide read-only capability for load balancer, so increasing slaves can expand read capability (a latency occurs to the slave data)
- It supports two master-slave synchronization modes: strongsync and async
  - Strongsync prevents data loss when the master crashes. It is recommended to configure at least two slaves because if there is only one slave, when the master crashes, the slave can provide only read-only service to prevent data loss
  - Strongsync brings lower performance than async does, and the performance loss depends on the network quality between the master and the slaves Generally, it is recommended to use strongsync only in the same data center, or multiple data centers in the same city
- You can set two logical instances as the master and the slave, generally used for remote data disaster recovery

### 4.4. Backup and Recovery

> Currently, CDB for MariaDB (TDSQL) features the following:


- You can configure an HDFS cluster for CDB for MariaDB (TDSQL) cluster to store cold backups and Binlog backups
- It supports the configuration of regular cold backup to HDFS
- It can backs up Binlog to HDFS in real time
- It supports timed rollback through cold backups and Binlog backups

### 4.5. Users and Permission

CDB for MariaDB (TDSQL) users include cluster managers, database instance managers and database users:

- Cluster managers mainly perform the following work through the OPS management platform:
  - Manage resource pools of the entire cluster, and launch, deactivate and assign resources
  - Assign database instances to instance managers
  - Help instance managers manage instances
  - Manage cold backup and Binlog backup data of all instances
  - Focus on operation metrics of clusters and instances to ensure the normal operation of clusters and instances
- Database instance managers mainly perform the following work through the database management platform:
  - Submit applications for instance creation, capacity expansion and deletion
  - Maintain individual parameters of instances
  - Manage accounts and passwords of database instances
  - Focus on operation metrics of instances to manage database performance
  - Optimize and analyze database performance by viewing information such as slow log, slow log analysis and error log
- Database users connect the SQL client to the database to submit SQL statements and access data
- 
### 4.6. Log Management

Logs of CDB for MariaDB (TDSQL) cluster mainly include:

- Operation log of each component in the cluster
- Instance gateway log
- Operation log, slow log and error log of database of the instance
- Binlog file of database of the instance
- Various log backups stored in HDFS

You need to configure all the logs with reasonable cleanup policies based on your needs


## 5. Suggestions on Performance Optimization

### 5.1. Performance Optimization Principles

Database performance optimization generally involves methodology, characteristics and tools The methodology consists of three parts:

- Performance planning: Deeply understand the interaction between the application and the database characteristics, establish a good procedure of design, development and test iteration, and eliminate performance bottlenecks before the database is launched
- Instance tuning: Establish a performance benchmark to compare and adjust the configuration of database, operating system, storage, network and so on, perform active monitoring, and eliminate bottlenecks
- SQL tuning: Write efficient SQL statements, optimize database objects, and fully use optimizers to determine the best execution plan

### 5.2. Performance Optimization Steps

- First, perform the following initial checks:
  - Obtain feedback from direct users to determine performance goal and range.
  - Obtain statistics on operating system, database and application when performance is good and bad
  - Perform an overall health check on the database
- Collect database statistics regularly
- Based on the collected statistics and your understanding of application characteristics, establish a performance conceptual model, and identify performance bottlenecks and corresponding reasons
- Propose targeted optimization measures, sort them based on their improvement to performance, and then implement the measures one by one Do not implement them once for all, and you must make comparison step by step
- Verify whether the optimization has produced the desired effect by obtaining feedback from direct users. If not, re-establish performance conceptual models until you have accurate understanding of application characteristics
- Repeat the above steps until the performance reaches the goal or can not be further optimized due to objective constraints

### 5.3. Common Optimization Techniques

- View `long_query` and `long_query_rate` metrics of the instance to analyze slow log frequencies and rules
- Analyze SQL statements that have the highest frequencies and spend longest time to execute via the slow log analysis tool, and solve the problem by optimizing the SQL statements, adding indexes and so on
- View `mem_hit_rate` and `mem_available` metrics to analyze if InnoDB's cache pool is sufficient or bottlenecks exist in the memory
- View `cpu_usage_rate`, and in combination with slow log, analyze if CPU consumption is reasonable or bottlenecks exist in CPU
- Adjust `innodb_page_size` parameter, and find the optimum configuration by comparing performance tests
- Use EXPLAIN for query analysis of common statements to find potential design problems
- According to the business scenarios, design the proper use cases, and make performance tests for instances of different specifications

