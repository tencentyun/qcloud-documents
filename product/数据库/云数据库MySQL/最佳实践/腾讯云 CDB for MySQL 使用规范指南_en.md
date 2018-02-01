### Purposes
1. Standardize the management and maintenance of CDB for MySQL to avoid unavailability and other issues caused by improper operations;
2. Provide a guidance for database developers on how to write SQL to ensure the best performance of CDB for MySQL.

### Audience
CDB for MySQL users.

### Permission Management Specifications
1. To ensure the stability and security, restrictions are imposed on the super, shutdown and file permissions for CDB for MySQL. The following error can occur when you execute the set statement on CDB for MySQL:  
```
#1227-Access denied;you need(at least one of)the SUPER privilege (s) for this operation
```
      
 Solution: If you need to modify the relevant parameters using set, use the "Parameter Modification" feature on the console. If the parameters to be modified are not included, you can submit a ticket for evaluation and modification to ensure the stability of instances.
2. On-demand authorization. For general applications, only the DML (SELECT, UPDATE, INSERT, DELETE) permissions are granted.
3. Minimum permissions. For general applications, users are granted permissions based on database levels.
4. Authorized users can only access CDB for MySQL from specific IPs or IP range. This can be achieved by configuring security groups on the console as instructed by the console. To set a security group for public network access, be sure to allow all the egress IPs involved.
5. Use different accounts for management and development.

### Operation Specifications

1. Avoid performing online ddl operations during peak hours. You can use the tools such as `pt-online-sche-machange`.
2. Avoid performing batch operations during peak hours. It is recommended to perform batch operations during off-peak hours.
3. Avoid running an instance for multiple businesses so as to minimize the risk of interaction between businesses due to too high coupling.
4. Do not use weak passwords so as to enhance the security of database instances.
5. It is recommended to disable the automatic committing of transactions and develop a habit of using `begin;` for online operations to minimize the risk of data loss caused by misoperation. In case of a misoperation, you can use the rollback feature of CDB for data recovery (rollback to any time point for the last 5 days is supported). For tables without cross-database and cross-table logics, you can use quick rollback or instant rollback for a faster data recovery. The name of the new database table generated through rollback is `original table name_bak` by default.
6. For promotional activities, make an estimate of the resources required in advance and optimize the instances. In case of a great demand for resources, contact your service manager in a timely manner.
7. For login by connecting private network, make sure that the CVM on the client side and CDB are in the same region and under the same account.
8. If the binlog downloaded from the console needs to be parsed locally, make sure that the client's MySQL version is same as that of CDB for MySQL. Otherwise, unreadable characters will occur during parsing. It is recommended to use mysqlbinlog 3.4 or above.
9. When downloading cold backup files to a CVM on console via private network, enclose the URL with quotation marks to avoid 404 error.

### Database Table Design Specifications
1. Plan the resources used by database reasonably based on business scenario analysis and estimation of data access (including database read/write QPS, TPS, storage, etc.). You can also configure various monitoring metrics for CDB for MySQL in Cloud Monitor in the console. 
2. When building a database, put the tables for the same business type into one database and do not put the tables for different business types into one database. Do not perform cross-database associated operations in the program, which will affect the subsequent quick rollbacks.
3. Each table must have a primary key. Even if no column is suitable for use as the primary key, you must add a meaningless column to use as the primary key. According to MySQL Paradigm 1, a primary key value is saved on the standard InnoDB secondary index's leaf nodes. It is recommended to use a short autoincrement column as the primary key to reduce the disk space occupied by indexes and improve the efficiency. When binbin_format is row, deleting the data in batch without a primary key can cause serious master-slave delay.
4. Use CDB products supporting InnoDB engine. MyISAM is no longer supported in CDB for MySQL 5.6 or above (nor is it supported in official MySQL 8.0 or above). If memory engine is required, it is recommended to migrate the self-built redis or memcached database to CDB, and then MyISAM will be automatically converted into InnoDB. Therefore, the following two requirements must be met, otherwise the task will fail.
5. For a table containing an auto-increment column, a separate index must exist on the column. If composite index is used, the auto-increment column must be put in the first place.
6. `row_format` must be non-fixed.
7. Always use the character set utf8mb4 to minimize the risk of unreadable characters. Some complex characters and emoji stickers can be displayed normally only by using utf8mb4. If character set is modified, new character set only takes effect on the tables created after the modification. Therefore, it is recommended to select utf8mb4 as early as the initialization of a new CDB instance.
8. For decimal fields, decimal type is recommended. Float and double types have not enough precision, especially for business involving money, in which case decimal type must be used.
9. Do not use text/blob to store a large volume of text, binary data, pictures, files and other contents in a database. Instead, save such data as local disk files and only store their index information in the database.
10. Avoid using foreign keys. It is recommended to implement the foreign key logic at the application layer. Foreign key and cascade update are not suitable for high-concurrency scenarios, because they can reduce insertion performance and lead to deadlock in case of a high concurrency.
11. Define fields as NOT NULL and set default values. NULL fields will cause the unavailability of indexes, thus bringing problems to SQL development. NULL calculation can only be implemented based on IS NULL and IS NOT NULL.
12. Reduce the coupling of business logic and data storage; use database mainly for storing data and implement business logic via the application layer as can as possible; minimize the use of stored procedures, triggers, functions, events, views and other advanced features because of their poor portability and scalability. If such objects exist in the instance, it is not recommended to set definer by default, so as to avoid migration failure caused by the consistency between migration account and definer.
13. If you won't have a substantial business volume in a short term, do not use partition tables, which are mainly used for archive management in the courier and e-commerce industries. Do not rely on partition tables for performance enhancement, unless over 80% of queries in your business involve partition fields.
14. For business scenarios with a high read load and low requirement for consistency (data delay within seconds is allowed), it is recommended to purchase read-only instances to implement read/write separation at the database level.

### Index Design Specifications

1. It is recommended to use not more than 5 indexes in a single table, and not more than 5 fields in a single index. Too much indexes can affect the filtering, occupy much more space, and consume more resources for management.
2. Create indexes on the columns that are used for SQL filtering most frequently with a high cardinality value. There is no point to create indexes on a column not involved in SQL filtering. The higher the uniqueness of a field, the higher the cardinality value, and the better the index filtering result is. Generally, an index column with a cardinality below 10% is considered an inefficient index, such as the gender field.
3. When creating an index on the varchar field, it is recommended to specify an index length, and do not index the entire column. This is because the varchar column is often long and the specified index length can provide sufficient differentiation. Indexing the entire column will increase the maintenance cost. You can use "count (distinct left (column name, index length))/count (*)" to check index differentiation.
4. Avoid using redundant indexes. If both the indexes (a, b) and (a) exist, (a) is considered a redundant index. If the query filtering is based on column a, the index (a, b) is enough.
5. When creating a composite index, the index with the highest differentiation is placed on the far left. For example, in `select xxx where a = x and b = x;`, a and b are used together to create a composite index, and a has higher differentiation. In this case, the composite index is created as `idx_ab (a, b)`. If None-Equal To and Equal To conditions are used at the same time, the column with the Equal To condition must be put first. For example, for `where a xxx and b = xxx`, b must be placed at the forefront even if a has a higher differentiation. This because index a will not be used in the query.
6. Do not create indexes on the columns that are updated frequently and have a lower differentiation. Record updates will change the B+ tree, so creating indexes for the fields that are updated frequently can greatly reduce the database performance.
7. Use covering indexes reasonably to reduce IO overhead. In InnoDB, leaf nodes of a secondary index only save their own key values and primary key values. If an SQL statement does not query such an index column or primary key, the query on the index locates the corresponding primary key first, and then locates the desired column based on the primary key. This is TABLE ACCESS BY INDEX ROWID, which will bring extra IO overhead. We can use covering indexes to solve this problem. For example, in `select a, b from xxx where a = xxx`, if a is not the primary key, we can create a composite index on the a and b columns to prevent the problem. 

### Specifications on Writing SQL

1. Ensure on-demand query and reject `select *` to avoid the following problems:       
    The covering index does not work and the problem of TABLE ACCESS BY INDEX ROWID occurs, which causes extra IO overhead.      
    Additional memory load; a large amount of cold data is put in the `innodb_buufer_pool_size` to cause a lower query hit rate.      
    More overhead in network transmission.
2. Do not use LIMIT for UPDATE and DELETE operations, because LIMIT is random and can cause data errors. You must use WHERE for such operations for a precise matching.
3. Do not use `INSERT INTO t_xxx VALUES(xxx)`, and the column attributes to be inserted must be displayed to prevent data errors caused by table structure changes.
4. Avoid using a large transaction. It is recommended to split a large transaction into multiple small transactions to avoid master-slave delay.
5. Commit transactions in the business code in a timely manner to avoid unnecessary lock wait.
6. Minimize the use of join operation for multiple tables and do not perform join operation on a large table. When performing a join operation on two tables, the smaller one must be used as the driving table, and the columns to be joined must have the same character set and all have been indexed.
7. Use LIMIT for paging optimization. The operation LIMIT 80000, 10 is to filter out 80,010 records, and then return the last 10. This can cause a high load on database. It is recommended to locate the first record before paging, such as `SELECT * FROM test WHERE id = ( SELECT sql_no_cache id FROM test order by id LIMIT 80000,1 ) LIMIT 10 ;`.
8. Avoid using an SQL statement with multi-level nested sub-queries. The query optimizer prior to MySQL5.5 can convert "in" into "exists" and does not go through the indexes. In this case, a large outer table can result in a poor performance.
9. The following are the common reasons for invalid indexes in SQL statements:
 - Implicit type conversion. For example, if the type of index a is varchar, and the SQL statement is where a = 1;, then varchar is changed to int.
 - Math calculations and functions were performed on the index columns, for example, date column was formatted using a function.
 - Inconsistency of character sets between the columns on which joint operation is performed.
 - Inconsistent sorting order between multiple columns. For example, the index is (a, b), but the SQL statement is "order by a b desclike".
 - When performing a fuzzy query, some indexes can be queried for characters with a format of `xxx%`. But in other cases, indexes will not be used.
 - Queries in reverse direction (such as not, !=, not in) are used.

**TIPS:**
1. It is difficult to totally avoid the above problems. The solution is not to use the conditions mentioned above as the primary filtering conditions and set them as the conditions secondary to the primary filtering conditions for indexes.
2. If a large number of full table scans is found in monitor, set `log_queries_not_using_indexes` in the parameter settings on console, and download the slow logs for analysis later. Do not keep it enabled for too long to avoid a surge of slow logs.
3. Perform the SQL audit necessary for a business goes live. In daily OPS work, download slow logs regularly for a targeted optimization.

