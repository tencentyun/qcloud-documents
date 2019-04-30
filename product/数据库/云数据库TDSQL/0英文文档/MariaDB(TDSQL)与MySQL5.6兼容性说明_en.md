## Foreword
TDSQL is developed based on MariaDB. We chose MariaDB in consideration of future open source issues regarding MySQL, besides that MariaDB has proved its decent performance, features and reliability to us over all these years.

>**We hope that readers do not consider "incompatibility" as a serious problem when reading this article, because surpassing MySQL is one of the goals for TDSQL (MariaDB). To "surpass" means to have better and more comprehensive performances and features, which means you can use the databases in a more standardized and flexible manner. Therefore, the incompatibility issues between the two engines will always exist.**

> The concepts described in this article have been verified and tested through many practical projects and use cases. Should you find anything amiss or incorrect, feel free to provide feedback to **vitosu@tencent.com**.

## The Compatibility Between MariaDB (TDSQL) and Open-source MariaDB
Fully compatible with MariaDB.

## The Compatibility Between MariaDB (TDSQL) and MySQL 5.6
> MariaDB (TDSQL) is highly compatible with MySQL 5.6, which means existing code, applications, drivers and tools already used in MySQL databases can be used for TDSQL without any modifications (or with minimum modifications).

- Data files and table definition files are binary compatible;
- All client APIs and protocols are compatible;
- All file names, binary files, paths and port numbers are the same;
- All connectors (including those for PHP, Perl, Python, Java, .NET, Ruby, MySQL) can be used on MariaDB without any modifications.
- You can use MySQL clients to connect to TDSQL.

## The Incompatibility Between TDSQL and MySQL 5.6
> MariaDB (TDSQL) is highly compatible with MySQL 5.6 but with several places that aren't compatible. Note that different versions of MySQL are not fully compatible with each other, such as 5.5 and 5.6, 5.6 and 5.7.


### 1. GTID not Compatible
- The GTID of MariaDB (TDSQL) is not compatible with the GTID of MySQL 5.6. In other words, MySQL cannot act as a slave library for TDSQL;

### 2. Different Default Binlog Configuration
- The Binlog of MariaDB (TDSQL) uses row as default format, whereas MySQL and MariaDB use statement as default format.

### 3. Copy CREAT TABLE ... SELECT Command as Line or as Command

- To ensure that the CREAT TABLE ... SELECT command can always function when copied as line or as command, the CREAT TABLE ... SELECT command in TDSQL will be converted into CREAT OR RPLACE in the slave library before it is executed. This ensures that the slave library can continue to function after it recovers from failure.

#### 3.1 Default Value Deduction

When creating tables using the "Create table ... Select from   " statement, the differences of the default values for varchar(N) fields are as follows:

- Mariadb 10.1: No default value,
- mysql 5.7: Default value is NULL, 
- mysql 5.5/5.6: Default value is an empty string ''.

For the default value of decimal column, mysql 5.5/5.6 deducts it as 0.00, while mariadb-10.1 deducts it as NULL.

Example:
```
---------------- mysql 5.5 -----------------------
create table t1
select least(_latin1'a',_latin2'b',_latin5'c' collate latin5_turkish_ci) as f1; 
show create table t1; 
Table   Create Table
t1  CREATE TABLE `t1` (
  `f1` varchar(1) CHARACTER SET latin5 NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=latin1
-------------------- mysql 5.7 ---------------------------------
create table t1
select least(_latin1'a',_latin2'b',_latin5'c' collate latin5_turkish_ci) as f1; 
show create table t1; 
Table   Create Table
t1  CREATE TABLE `t1` (
  `f1` varchar(1) CHARACTER SET latin5 DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1
------------------- mariadb10.1*--------------------------------
create table t1
select least(_latin1'a',_latin2'b',_latin5'c' collate latin5_turkish_ci) as f1; 
show create table t1; 
Table   Create Table
t1  CREATE TABLE `t1` (
  `f1` varchar(1) CHARACTER SET latin5 NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1


```

#### 3.2 Difference when Handling Select Statements in Sub-queries
In this statement: `SELECT a AS x, ROW(11, 12) = (SELECT MAX(x), 12), ROW(11, 12) IN (SELECT MAX(x), 12) FROM t1;`

- In Mysql 5.5/5.6, the sub-query "SELECT MAX(x), 12" is considered as "SELECT MAX(x), 12 from t1" if it is located after "in"; it is considered as "SELECT x, 12" if it is located after "=", where "x" is an alias for "a" in the current line
- In Mysql 5.7 and Mariadb 10.1.*, the sub-query "SELECT MAX(x), 12" always equals to "SELECT x, 12", where "x" is an alias for "a" in the current line

Example:
```
----------------- mysql 5.5/5.6 -----------------------
CREATE TABLE t1 (a INT);
INSERT INTO t1 VALUES (1), (2), (11);
SELECT a AS x, ROW(11, 12) = (SELECT MAX(x), 12), ROW(11, 12) IN (SELECT MAX(x), 12) FROM t1;
x   ROW(11, 12) = (SELECT MAX(x), 12)   ROW(11, 12) IN (SELECT MAX(x), 12)
1   0   1
2   0   1
11  1   1
--------------------------- mariadb-10.1.* or mysql 5.7------------------------------
CREATE TABLE t1 (a INT);
INSERT INTO t1 VALUES (1), (2), (11);
SELECT a AS x, ROW(11, 12) = (SELECT MAX(x), 12), ROW(11, 12) IN (SELECT MAX(x), 12) FROM t1;
x   ROW(11, 12) = (SELECT MAX(x), 12)   ROW(11, 12) IN (SELECT MAX(x), 12)
1   0   0
2   0   0
11  1   1


```

#### 3.3 Handling NULL in ALL/SOME
In Mysql 5.5, the "NULL" in "10 >=  ALL (NULL, 1, 10)" or "1 <= ALL (NULL, 1, 10)" is skipped (considered as non-existent), because NULL is incomparable.
In Mysql 5.7 and MariaDB, "NULL" is an unknown value, thus the comparisons above return "NULL"(unknown result)

#### 3.4 "alter table inplace" operation

When using "alter table" to change the sequence of columns only, the "inplace" algorithm is allowed in MariaDB but is not allowed in MySQL.

When "inplace alter table" is executed in MariaDB, the result of "show create table t1" is the same with executing "ALGORITHM=COPY" in MySQL


### 4. Undefined Behaviors in MySQL/MariaDB (TDSQL)

>**Undefined behavior** refers to feature or behavior that can be realized by any means in MySQL/MariaDB. These behaviors may change in different versions, and the changes are not shown to users or pointed out. In MySQL and MariaDB, these behaviors may either yield the same results or different results.

>TDSQL does not guarantee the results for such differences or similarities in current or future versions, and does not guarantee to provide kernel optimizations to keep the results consistent. Official description for undefined behaviors: https://mariadb.com/kb/en/mariadb/mariadb-vs-mysql-compatibility/


#### 4.1 Character Type Column and Case Insensitive Sorting

For character type columns, the sorting operation (order by <clause>) is usually case insensitive, which means the sorted sequence for fields that contain the same content with different letter cases is not defined. You can use the BINARY keyword to enforce case-sensitive sorting operation: ORDER BY BINARY <column name>.

Example:
```
In MySQL and MariaDB, sorting the following example may yield random results
mysql> SELECT email FROM t2 LEFT JOIN t1  ON kid = t2.id WHERE t1.id IS NULL order by email;

+-------+
| email |
+-------+
| email |
| eMail |
| EMail |
+-------+
3 rows in set (0.00 sec)
```

#### 4.2 Handling Auto_increment Field Overflow
Undefined behavior specific to INNODB

1. In all auto increment lock modes (0, 1, 2), the auto increment behavior is considered undefined if you specify negative value for auto increment field;

2. In all auto increment lock modes (0, 1, 2), the auto increment behavior is considered undefined if the value of auto increment field is bigger than the max value allowed for the integer type of this field.

> Note: Do not insert incorrect values into auto increment columns.

#### 4.3 Statistical Method for FOUND ROWS

The returned value of FOUND_ROWS() is only accurate if "UNION ALL" is used in the query statement.

If **"UNION" is used but without "ALL", then duplicates will be removed in the statistics in MariaDB, and will not be removed in statistics in MySQL**. If the LIMIT clause is not used in UNION query statement, the SQL_CALC_FOUND_ROWS keyword will be ignored and FOUND_ROWS() will return the number of rows of the temporary table that is created when UNION is executed.

#### 4.4 Locking Sequence of LOCK TABLES Statement
The LOCK TABLES statement will lock tables in the following way: First, sort all tables to be locked using an internal-defined method. From the user's perspective, this sequence in MySQL/MariaDB is undefined. For example, if you execute "LOCK TABLES t1, t2, t3", MySQL/MariaDB will not lock tables with the sequence t1, t2, then t3.
This behavior is undefined in MySQL/MariaDB, thus they may use a different method to sort t1, t2, t3, then lock them using the sequence after the sorting operation.

For this reason, users should not rely on locking sequence to ensure accuracy when coding storage procedures or queries, as this may cause deadlock.

#### 4.5 The Timing for Executing RESET MASTER

You cannot execute RESET MASTER when any backup slave is running, otherwise the behaviors of master and slave are not defined (and not supported) for MariaDB and MySQL. Various errors may occur during the execution of RESET MASTER. These errors are not predictable (it's even possible that no error would occur at all). The official development teams of MariaDB and MySQL do not consider these errors as bugs and are not responsible for any errors that may occur in this way. 

#### 4.6 Convert "date" and "time" into "year" Type
In MySQL 5.5, when comparing variables for "year" and "date" types, the "date" type is converted into "year" type for comparison. For example, "2011-01-01" is converted into "2011".

In MySQL 5.7 and MariaDB, the variable of "date" type is still "date", thus it is not the same with the variable of "year" when compared.

Similarly, MariaDB cannot convert "time" type into "year", while mysql 5.6 uses the value of "YEAR" in the timestamp of the current session as the "year" value for every "time", which means the "year" in the timestamp of the current session is used every time a "time" type value needs to be converted into "year" type.

#### 4.7 Handling Unknown Characters
- Character encoding conversion is done in different ways in different versions of MySQL and MariaDB. For example: if an encoding byte string is not recognized by unhex, then an empty string ("") will be returned in mysql 5.5/5.6/5.7, while a question mark character (?) will be returned in mariadb 10.1.

- The `UPDATE t1 SET a=unhex(code) ORDER BY code` statement assigns values to field "a" in table "t1". However, some of the assignment will fail, since unhex can only recognize and convert byte strings within a certain range:

 - The default storage engine in mysql 5.5 is MyISAM, so the transaction is not supported. The statement is exited when it fails to assign value to "a" in any row in t1. Those already assigned are still stored in t1
 - The default storage engine in mysql 5.7 is InnoDB, thus the transaction will be rolled back when the statement fails to assign value to "a" in any row in t1, which means all values already assigned will be rolled back as well.
 - The default storage engine in MariaDB is InnoDB. When unhex is unable to find a corresponding character for a byte string, a question mark ("?", 0x3F) is returned, thus the operation will always succeed regardless of the storage engine (InnoDB or myisan)

- When inserting a hexadecimal string using "insert into" statement, if the corresponding utf8mb4 character is not found:
 - In mysql 5.5/5.6, if storage engine is heap, the unknown character is ignored
 - In mariadb 10.1 and mysql 5.7, the character is replaced with 0x3F (question mark).

- For string fields of invalid encoding, an error is returned in MySQL with InnoDB as storage engine. While in MariaDB, it is replaced with 3F before it's inserted

#### 4.8 Precision of time Type
``` 
SELECT CAST(CAST('10:11:12.098700' AS TIME) AS DECIMAL(20,6));
CAST(CAST('10:11:12.098700' AS TIME) AS DECIMAL(20,6))
``` 	
Similar statements are handled in different ways in MySQ 5.5/5.6 and MariaDB 10.1/MySQL 5.7:

- In MySQL 5.5/5.6, time precision is retained, which means "101112.098700" will be returned.
- In MySQL 5.7 and MariaDB 10.1, "101112.000000" will be returned. This is because the statement does not specify a precision for TIME, in which case the default precision is 0, thus the values after the decimal point for "CAST('10:11:12.098700' AS TIME)" are lost

You can use the following statement to keep the time precision;
```
SELECT CAST(CAST('10:11:12.098700' (6)) AS DECIMAL(20,6));
+-----------------------------------------------------------+
| CAST(CAST('10:11:12.098700' AS TIME(6)) AS DECIMAL(20,6)) |
+-----------------------------------------------------------+
| 101112.098700 |
+-----------------------------------------------------------+
```
> The default precision for TIME is not consistent. If there is requirement for time precision, you should explicitly specify a precision for "time" for operations such as upgrading or migrating.

```
CREATE TABLE t1(f1 TIME);
INSERT INTO t1 VALUES ('23:38:57');
SELECT TIMESTAMP(f1,'1') FROM t1;
```
"NULL" is returned in Mysql 5.5/5.6, while "2016-08-03 23:38:58" is returned in Mariadb 10.1 and Mysql 5.7
- If the type of the first parameter of TIMESTAMP() is "time", then the returned value will be "NULL", because mysql 5.5 is not able to automatically convert it into timestamp type
- While mysql 5.7 is able to automatically convert "time" into timestamp type, that is, in the format of "<current date> + <time variable entered by user>"







### 5. Appendix: MariaDB Parameters and MySQL Parameters

#### 5.1 Different Parameter with the Same Variable Name
>Parameters with the same variable name have the same main feature

| Parameter Name | TDSQL (MariaDB 10.1) | MySQL 5.6 |
|:--:|:--:|:--:|
|old_passwords|OFF|0|
|tmpdir|/tmp/5cXm2hHsWi/mysqld.1|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/tmp/mysqld.1|
|version|10.1.9-MariaDB-log|5.6.31-log|
|slow_query_log_file|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/mysqld-slow.log|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/mysqld.1/mysqld-slow.log|
|table_definition_cache|400|1400|
|datadir|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/data/|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/mysqld.1/data/|
|pid_file|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/run/mysqld.1.pid|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/run/mysqld.1.pid|
|max_seeks_for_key|4294967295|18446744073709500000|
|slave_load_tmpdir|/tmp/5cXm2hHsWi/mysqld.1|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/tmp/mysqld.1|
|secure_file_priv|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/|
|sql_mode|NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION|NO_ENGINE_SUBSTITUTION|
|ssl_cert|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/mysql-test/std_data/server-cert.pem|/data/home/tdengine/dongzhi/src/mysql-server-5.6/mysql-test/std_data/server-cert.pem|
|ssl_ca|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/mysql-test/std_data/cacert.pem|/data/home/tdengine/dongzhi/src/mysql-server-5.6/mysql-test/std_data/cacert.pem|
|open_files_limit|1024|4161|
|binlog_checksum|NONE|CRC32|
|basedir|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1|/data/home/tdengine/dongzhi/src/mysql-server-5.6|
|query_alloc_block_size|16384|8192|
|innodb_max_dirty_pages_pct|75.000000|75|
|ssl_key|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/mysql-test/std_data/server-key.pem|/data/home/tdengine/dongzhi/src/mysql-server-5.6/mysql-test/std_data/server-key.pem|
|myisam_sort_buffer_size|134216704|8388608|
|skip_name_resolve|ON|OFF|
|pseudo_thread_id|3|2|
|character_sets_dir|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/sql/share/charsets/|/data/home/tdengine/dongzhi/src/mysql-server-5.6/sql/share/charsets/|
|innodb_adaptive_flushing_lwm|10|10|
|myisam_recover_options|DEFAULT|OFF|
|performance_schema_max_statement_classes|179|168|
|innodb_version|5.6.26-74.0|5.6.31|
|max_write_lock_count|4294967295|18446744073709500000|
|thread_cache_size|0|9|
|innodb_checksum_algorithm|INNODB|innodb|
<<<<<<< HEAD
|optimizer_switch|index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,index_merge_sort_intersection=off,engine_condition_pushdown=off,index_condition_pushdown=on,derived_merge=on,derived_with_keys=on,firstmatch=on,loosescan=on,materialization=on,in_to_exists=on,semijoin=on,partial_match_rowid_merge=on,partial_match_table_scan=on,subquery_cache=on,mrr=off,mrr_cost_based=off,mrr_sort_keys=off,outer_joinwith_cache=on,semijoin_with_cache=on,join_cache_incremental=on,join_cache_hashed=on,join_cache_bka=on,optimize_join_buffer_size=off,table_elimination=on,extended_keys=on,exists_to_in=on|index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,subquery_materialization_cost_based=on,use_index_extensions=on|
=======
|optimizer_switch|index_merge=on,<br>index_merge_union=on,<br>index_merge_sort_union=on,<br>index_merge_intersection=on,<br>index_merge_sort_intersection=off,<br>engine_condition_pushdown=off,<br>index_condition_pushdown=on,<br>derived_merge=on,<br>derived_with_keys=on,<br>firstmatch=on,<br>loosescan=on,<br>materialization=on,<br>in_to_exists=on,<br>semijoin=on,<br>partial_match_rowid_merge=on,<br>partial_match_table_scan=on,<br>subquery_cache=on,<br>mrr=off,<br>mrr_cost_based=off,<br>mrr_sort_keys=off,<br>outer_join_with_cache=on,<br>semijoin_with_cache=on,<br>join_cache_incremental=on,<br>join_cache_hashed=on,<br>join_cache_bka=on,<br>optimize_join_buffer_size=off,<br>table_elimination=on,<br>extended_keys=on,<br>exists_to_in=on|index_merge=on,<br>index_merge_union=on,<br>index_merge_sort_union=on,<br>index_merge_intersection=on,<br>engine_condition_pushdown=on,<br>index_condition_pushdown=on,<br>mrr=on,<br>mrr_cost_based=on,<br>block_nested_loop=on,<br>batched_key_access=off,<br>materialization=on,<br>semijoin=on,<br>loosescan=on,<br>firstmatch=on,<br>subquery_materialization_cost_based=on,<br>use_index_extensions=on|
>>>>>>> origin/master
|timestamp|1471938276|1471937901|
|general_log_file|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/mysqld.log|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/mysqld.1/mysqld.log|
|myisam_stats_method|NULLS_UNEQUAL|nulls_unequal|
|innodb_log_compressed_pages|OFF|ON|
|query_prealloc_size|24576|8192|
|rand_seed2|297895171|0|
|rand_seed1|605568929|0|
|socket|/tmp/5cXm2hHsWi/mysqld.1.sock|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/mysql-test/var/tmp/mysqld.1.sock|
|innodb_max_dirty_pages_pct_lwm|0.001|0|
|lc_messages_dir|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/sql/share/|/data/home/tdengine/dongzhi/src/mysql-server-5.6/build_dongzhi/sql/share/|
|max_relay_log_size|1073741824|0|
|plugin_dir|/data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/lib/plugin/|/data/home/tdengine/dongzhi/src/mysql-server-5.6/lib/plugin/|
|thread_stack|294912|262144|


#### 5.2 TDSQL (MariaDB)-only Variables
--------------------------------------------------
- aria_block_size     8192
- aria_checkpoint_interval     30
- aria_checkpoint_log_activity     1048576
- aria_encrypt_tables     OFF
- aria_force_start_after_recovery_failures     0
- aria_group_commit     none
- aria_group_commit_interval     0
- aria_log_file_size     1073741824
- aria_log_purge_type     immediate
- aria_max_sort_file_size     9223372036853727232
- aria_page_checksum     ON
- aria_pagecache_age_threshold     300
- aria_pagecache_buffer_size     134217728
- aria_pagecache_division_limit     100
- aria_pagecache_file_hash_size     512
- aria_recover     NORMAL
- aria_repair_threads     1
- aria_sort_buffer_size     268434432
- aria_stats_method     nulls_unequal
- aria_sync_log_dir     NEWFILE
- aria_used_for_temp_tables     ON
- autoremoverelaylog     ON
- binlog_annotate_row_events     OFF
- binlog_commit_wait_count     0
- binlog_commit_wait_usec     100000
- binlog_optimize_thread_scheduling     ON
- deadlock_search_depth_long     15
- deadlock_search_depth_short     4
- deadlock_timeout_long     50000000
- deadlock_timeout_short     10000
- debug_no_thread_alarm     OFF
- default_master_connection      
- default_regex_flags      
- encrypt_binlog     OFF
- encrypt_tmp_disk_tables     OFF
- encrypt_tmp_files     OFF
- enforce_storage_engine      
- expensive_subquery_limit     100
- extra_max_connections     20
- extra_port     0
- flush_relay_logs_for_strong_consistency     ON
- gtid_binlog_pos      
- gtid_binlog_state      
- gtid_current_pos      
- gtid_domain_id     0
- gtid_ignore_duplicates     OFF
- gtid_seq_no     0
- gtid_slave_pos      
- gtid_strict_mode     OFF
- histogram_size     0
- histogram_type     SINGLE_PREC_HB
- in_transaction     0
- innodb_adaptive_hash_index_partitions     1
- innodb_background_scrub_data_check_interval     3600
- innodb_background_scrub_data_compressed     OFF
- innodb_background_scrub_data_interval     604800
- innodb_background_scrub_data_uncompressed     OFF
- innodb_buf_dump_status_frequency     0
- innodb_buffer_pool_populate     OFF
- innodb_cleaner_lsn_age_factor     HIGH_CHECKPOINT
- innodb_compression_algorithm     none
- innodb_corrupt_table_action     assert
- innodb_default_encryption_key_id     1
- innodb_defragment     OFF
- innodb_defragment_fill_factor     0.900000
- innodb_defragment_fill_factor_n_recs     20
- innodb_defragment_frequency     40
- innodb_defragment_n_pages     7
- innodb_defragment_stats_accuracy     0
- innodb_disallow_writes     OFF
- innodb_empty_free_list_algorithm     BACKOFF
- innodb_encrypt_log     OFF
- innodb_encrypt_tables     OFF
- innodb_encryption_rotate_key_age     1
- innodb_encryption_rotation_iops     100
- innodb_encryption_threads     0
- innodb_fake_changes     OFF
- innodb_fatal_semaphore_wait_threshold     600
- innodb_force_primary_key     OFF
- innodb_foreground_preflush     EXPONENTIAL_BACKOFF
- innodb_idle_flush_pct     100
- innodb_immediate_scrub_data_uncompressed     OFF
- innodb_instrument_semaphores     OFF
- innodb_kill_idle_transaction     0
- innodb_locking_fake_changes     ON
- innodb_log_arch_dir     ./
- innodb_log_arch_expire_sec     0
- innodb_log_archive     OFF
- innodb_log_block_size     512
- innodb_log_checksum_algorithm     INNODB
- innodb_max_bitmap_file_size     104857600
- innodb_max_changed_pages     1000000
- innodb_mtflush_threads     8
- innodb_prefix_index_cluster_optimization     OFF
- innodb_sched_priority_cleaner     19
- innodb_scrub_log     OFF
- innodb_scrub_log_speed     256
- innodb_show_locks_held     10
- innodb_show_verbose_locks     0
- innodb_simulate_comp_failures     0
- innodb_stats_modified_counter     0
- innodb_stats_traditional     ON
- innodb_track_changed_pages     OFF
- innodb_use_atomic_writes     OFF
- innodb_use_fallocate     OFF
- innodb_use_global_flush_log_at_trx_commit     ON
- innodb_use_mtflush     OFF
- innodb_use_stacktrace     OFF
- innodb_use_trim     OFF
- join_buffer_space_limit     2097152
- join_cache_level     2
- key_cache_file_hash_size     512
- key_cache_segments     0
- last_gtid      
- log_slow_filter     admin,filesort,filesort_on_disk,full_join,full_scan,query_cache,query_cache_miss,tmp_table,tmp_table_on_disk
- log_slow_rate_limit     1
- log_slow_verbosity      
- log_tc_size     24576
- loglevel     3
- max_long_data_size     4194304
- max_statement_time     0.000000
- mrr_buffer_size     262144
- myisam_block_size     1024
- mysql56_temporal_format     ON
- old_mode      
- optimizer_selectivity_sampling_limit     100
- optimizer_use_condition_selectivity     1
- plugin_maturity     unknown
- progress_report_time     5
- query_cache_strip_comments     OFF
- relay_log_sync_threshold     134217728
- relay_log_sync_timeout     200
- relay_log_sync_txn_count     5
- replicate_annotate_row_events     OFF
- replicate_do_db      
- replicate_do_table      
- replicate_events_marked_for_skip     REPLICATE
- replicate_ignore_db      
- replicate_ignore_table      
- replicate_wild_do_table      
- replicate_wild_ignore_table      
- rowid_merge_buff_size     8388608
- rpl_semi_sync_master_enabled     OFF
- rpl_semi_sync_master_timeout     10000
- rpl_semi_sync_master_trace_level     32
- rpl_semi_sync_master_wait_no_slave     ON
- rpl_semi_sync_master_wait_point     AFTER_COMMIT
- rpl_semi_sync_slave_enabled     OFF
- rpl_semi_sync_slave_trace_level     32
- skip_parallel_replication     OFF
- skip_replication     OFF
- slave_current_parallel_transactions     0
- slave_ddl_exec_mode     IDEMPOTENT
- slave_domain_parallel_threads     0
- slave_max_parallel_transactions     0
- slave_parallel_max_queued     131072
- slave_parallel_mode     conservative
- slave_parallel_threads     0
- slave_run_triggers_for_rbr     NO
- sqlasyn     OFF
- sqlasyntimeout     10
- sqlasynwarntimeout     3
- strict_password_validation     ON
- thread_pool_high_prio_mode     transactions
- thread_pool_high_prio_tickets     4294967295
- thread_pool_idle_timeout     60
- thread_pool_max_threads     1000
- thread_pool_oversubscribe     3
- thread_pool_oversubscribe_parall     1
- thread_pool_size     8
- thread_pool_stall_limit     500
- use_stat_tables     NEVER
- userstat     OFF
- version_malloc_library     system
- version_ssl_library     OpenSSL 1.0.2d 9 Jul 2015
- wsrep_auto_increment_control     ON
- wsrep_causal_reads     OFF
- wsrep_certify_nonpk     ON
- wsrep_cluster_address      
- wsrep_cluster_name     my_wsrep_cluster
- wsrep_convert_lock_to_trx     OFF
- wsrep_data_home_dir     /data/home/tdengine/dongzhi/src/tdsql-mariadb-10.1.9-release1/build_dongzhi/mysql-test/var/mysqld.1/data/
- wsrep_dbug_option      
- wsrep_debug     OFF
- wsrep_desync     OFF
- wsrep_dirty_reads     OFF
- wsrep_drupal_282555_workaround     OFF
- wsrep_forced_binlog_format     NONE
- wsrep_gtid_domain_id     0
- wsrep_gtid_mode     OFF
- wsrep_load_data_splitting     ON
- wsrep_log_conflicts     OFF
- wsrep_max_ws_rows     131072
- wsrep_max_ws_size     1073741824
- wsrep_mysql_replication_bundle     0
- wsrep_node_address      
- wsrep_node_incoming_address     AUTO
- wsrep_node_name      
- wsrep_notify_cmd      
- wsrep_on     OFF
- wsrep_osu_method     TOI
- wsrep_patch_version     wsrep_25.11
- wsrep_provider     none
- wsrep_provider_options      
- wsrep_recover     OFF
- wsrep_replicate_myisam     OFF
- wsrep_restart_slave     OFF
- wsrep_retry_autocommit     1
- wsrep_slave_fk_checks     ON
- wsrep_slave_threads     1
- wsrep_slave_uk_checks     OFF
- wsrep_sst_auth      
- wsrep_sst_donor      
- wsrep_sst_donor_rejects_queries     OFF
- wsrep_sst_method     rsync
- wsrep_sst_receive_address     AUTO
- wsrep_start_position     00000000-0000-0000-0000-000000000000:-1
- wsrep_sync_wait     0

#### 5.3 Mysql 5.6-only Variables

- avoid_temporal_upgrade     OFF
- bind_address     *
- binlog_error_action     IGNORE_ERROR
- binlog_gtid_simple_recovery     OFF
- binlog_max_flush_queue_time     0
- binlog_order_commits     ON
- binlog_rows_query_log_events     OFF
- binlogging_impossible_mode     IGNORE_ERROR
- block_encryption_mode     aes-128-ecb
- core_file     ON
- disconnect_on_expired_password     ON
- end_markers_in_json     OFF
- enforce_gtid_consistency     OFF
- eq_range_index_dive_limit     1
- gtid_executed      
- gtid_mode     OFF
- gtid_next     AUTOMATIC
- gtid_owned      
- gtid_purged      
- innodb_tmpdir      
- log_bin_use_v1_row_events     OFF
- log_slow_admin_statements     OFF
- log_slow_slave_statements     OFF
- log_throttle_queries_not_using_indexes     0
- master_info_repository     FILE
- new     OFF
- optimizer_trace     enabled=off,one_line=off
- optimizer_trace_features     greedy_search=on,range_optimizer=on,dynamic_range=on,repeated_subselect=on
- optimizer_trace_limit     1
- optimizer_trace_max_mem_size     16384
- optimizer_trace_offset     -1
- relay_log_info_repository     FILE
- rpl_stop_slave_timeout     31536000
- server_id_bits     32
- server_uuid     9078a55d-6904-11e6-bfa9-ecf4bbcdc829
- sha256_password_private_key_path     private_key.pem
- sha256_password_public_key_path     public_key.pem
- show_old_temporals     OFF
- simplified_binlog_gtid_recovery     OFF
- slave_allow_batching     OFF
- slave_checkpoint_group     512
- slave_checkpoint_period     300
- slave_parallel_workers     0
- slave_pending_jobs_size_max     16777216
- slave_rows_search_algorithms     TABLE_SCAN,INDEX_SCAN
- table_open_cache_instances     1
- transaction_allow_batching     OFF


