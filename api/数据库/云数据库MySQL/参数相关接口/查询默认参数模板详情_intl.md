## 1. API Description
This API (GetCdbDefaultParamInfo) is used to query the default parameter template of the Cloud Database instance. You can use the database version number to query the default parameter information of the instance.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbDefaultParamInfo.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| engineVersion | Yes | String | Database version number. Possible returned values include: 5.1, 5.5, and 5.6 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Returned data |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| default | String | Default value|
| desc | String | Parameter description |
| enum_value | Array | Available enumerated value of the parameter. If it is not an enumerated value, leave the parameter empty|
| max | Int | Maximum permissible value |
| min | Int | Minimum permissible value |
| name | String | Parameter name |
| need_reboot | Int | Whether to reboot the Cloud Database to validate the modified parameter. Possible returned values include: 0-Not Reboot; 1-Reboot |
| type | String | Parameter type. Possible returned values include: integer-integer; enum-enumeration; string-string; boolean-Boolean; float-floating point |


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Description |
|---------|---------|---------|
| 9013 | InternalError | System internal error |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbDefaultParamInfo
&<<a href="/document/product/236/6921">Common request parameters</a>>
&engineVersion=5.6
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "default":"1",
            "desc":"Controls the interval between successive column values.",
            "enum_value":[
                
            ],
            "max":"65535",
            "min":"1",
            "name":"auto_increment_increment",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"1",
            "desc":"Determines the starting point for the AUTO_INCREMENT column value.",
            "enum_value":[
                
            ],
            "max":"65535",
            "min":"1",
            "name":"auto_increment_offset",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"1",
            "desc":"The number of outstanding connection requests MySQL can have.",
            "enum_value":[
                
            ],
            "max":"65535",
            "min":"1",
            "name":"back_log",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"NONE",
            "desc":"When enabled, this variable causes the master to write a checksum for each event in the binary log.",
            "enum_value":[
                "NONE",
                "CRC32"
            ],
            "max":"0",
            "min":"0",
            "name":"binlog_checksum",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"latin1",
            "desc":"Specify default server character set",
            "enum_value":[
                "latin1",
                "utf8",
                "gbk",
                "utf8mb4"
            ],
            "max":"0",
            "min":"0",
            "name":"character_set_server",
            "need_reboot":"1",
            "type":"enum"
        },
        {
            "default":"10",
            "desc":"The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake",
            "enum_value":[
                
            ],
            "max":"1800",
            "min":"2",
            "name":"connect_timeout",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"0",
            "desc":"The default mode value to use for the WEEK() function",
            "enum_value":[
                
            ],
            "max":"7",
            "min":"0",
            "name":"default_week_format",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"4",
            "desc":"This variable indicates the number of digits by which to increase the scale of the result of division operations performed with the operator",
            "enum_value":[
                
            ],
            "max":"30",
            "min":"0",
            "name":"div_precision_increment",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"OFF",
            "desc":"This variable indicates the status of the Event Scheduler",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"event_scheduler",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"1024",
            "desc":"The maximum permitted result length in bytes for the GROUP_CONCAT() function",
            "enum_value":[
                
            ],
            "max":"4294967295",
            "min":"4",
            "name":"group_concat_max_len",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"ON",
            "desc":"Whether the InnoDB adaptive hash index is enabled or disabled.",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"innodb_adaptive_hash_index",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"1",
            "desc":"The lock mode to use for generating auto-increment values.",
            "enum_value":[
                
            ],
            "max":"2",
            "min":"0",
            "name":"innodb_autoinc_lock_mode",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"1",
            "desc":"Controls the balance between strict ACID compliance for commit operations, and higher performance that is possible when commit-related I/O operations are rearranged and done in batches.",
            "enum_value":[
                
            ],
            "max":"2",
            "min":"0",
            "name":"innodb_flush_log_at_trx_commit",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"84",
            "desc":"Maximum character length of words that are stored in an InnoDB FULLTEXT index.",
            "enum_value":[
                
            ],
            "max":"84",
            "min":"10",
            "name":"innodb_ft_max_token_size",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"3",
            "desc":"Minimum length of words that are stored in an InnoDB FULLTEXT index.",
            "enum_value":[
                
            ],
            "max":"16",
            "min":"0",
            "name":"innodb_ft_min_token_size",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"OFF",
            "desc":"Enable this option to allow index key prefixes longer than 767 bytes (up to 3072 bytes) for InnoDB tables that use the DYNAMIC and COMPRESSED row formats.",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"innodb_large_prefix",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"7200",
            "desc":"The length of time in seconds an InnoDB transaction waits for a row lock before giving up",
            "enum_value":[
                
            ],
            "max":"1073741824",
            "min":"1",
            "name":"innodb_lock_wait_timeout",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"75",
            "desc":"InnoDB tries to flush data from the buffer pool so that the percentage of dirty pages does not exceed this value",
            "enum_value":[
                
            ],
            "max":"99",
            "min":"0",
            "name":"innodb_max_dirty_pages_pct",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"37",
            "desc":"Specifies the approximate percentage of the InnoDB buffer pool used for the old block sublist",
            "enum_value":[
                
            ],
            "max":"95",
            "min":"5",
            "name":"innodb_old_blocks_pct",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"1000",
            "desc":"Specifies the approximate percentage of the InnoDB buffer pool used for the old block sublist",
            "enum_value":[
                
            ],
            "max":"2147483647",
            "min":"0",
            "name":"innodb_old_blocks_time",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"300",
            "desc":"It specifies the maximum number of .ibd files that MySQL can keep open at one time.",
            "enum_value":[
                
            ],
            "max":"8192",
            "min":"1",
            "name":"innodb_open_files",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"OFF",
            "desc":"When this option is enabled, information about all deadlocks in InnoDB user transactions is recorded in the mysqld error log.",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"innodb_print_all_deadlocks",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"300",
            "desc":"The granularity of changes, expressed in units of redo log records, that trigger a purge operation, flushing the changed buffer pool blocks to disk.",
            "enum_value":[
                
            ],
            "max":"5000",
            "min":"1",
            "name":"innodb_purge_batch_size",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"1",
            "desc":"The number of background threads devoted to the InnoDB purge operation.",
            "enum_value":[
                
            ],
            "max":"32",
            "min":"1",
            "name":"innodb_purge_threads",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"56",
            "desc":"Controls the sensitivity of linear read-ahead that InnoDB uses to prefetch pages into the buffer pool",
            "enum_value":[
                
            ],
            "max":"64",
            "min":"0",
            "name":"innodb_read_ahead_threshold",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"4",
            "desc":"The number of I/O threads for read operations in InnoDB.",
            "enum_value":[
                
            ],
            "max":"64",
            "min":"1",
            "name":"innodb_read_io_threads",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"OFF",
            "desc":"If innodb_rollback_on_timeout is specified, a transaction timeout causes InnoDB to abort and roll back the entire transaction.",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"innodb_rollback_on_timeout",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"OFF",
            "desc":"When this variable is enabled, InnoDB updates statistics when metadata statements such as SHOW TABLE STATUS or SHOW INDEX are run, or when accessing the INFORMATION_SCHEMA tables TABLES or STATISTICS",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"innodb_stats_on_metadata",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"OFF",
            "desc":"When innodb_strict_mode is ON, InnoDB returns errors rather than warnings for certain conditions",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"innodb_strict_mode",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"ON",
            "desc":"If autocommit = 0, InnoDB honors LOCK TABLES; MySQL does not return from LOCK TABLES ... WRITE until all other threads have released all their locks to the table. The default value of innodb_table_locks is 1, which means that LOCK TABLES causes InnoDB to lock a table internally if autocommit = 0.",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"innodb_table_locks",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"0",
            "desc":"InnoDB tries to keep the number of operating system threads concurrently inside InnoDB less than or equal to the limit given by this variable.",
            "enum_value":[
                
            ],
            "max":"128",
            "min":"0",
            "name":"innodb_thread_concurrency",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"0",
            "desc":"How long InnoDB threads sleep before joining the InnoDB queue, in microseconds. ",
            "enum_value":[
                
            ],
            "max":"4294967295",
            "min":"0",
            "name":"innodb_thread_sleep_delay",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"4",
            "desc":"The number of I/O threads for write operations in InnoDB.",
            "enum_value":[
                
            ],
            "max":"64",
            "min":"1",
            "name":"innodb_write_io_threads",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"3600",
            "desc":"The number of seconds the server waits for activity on an interactive connection before closing it",
            "enum_value":[
                
            ],
            "max":"86400",
            "min":"1",
            "name":"interactive_timeout",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"OFF",
            "desc":"Whether queries that do not use indexes are logged to the slow query log",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"log_queries_not_using_indexes",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"10",
            "desc":"If a query takes longer than this many seconds, the server increments the Slow_queries status variable",
            "enum_value":[
                
            ],
            "max":"3600",
            "min":"0.1",
            "name":"long_query_time",
            "need_reboot":"0",
            "type":"float"
        },
        {
            "default":"OFF",
            "desc":"If set to true, all INSERT, UPDATE, DELETE, and LOCK TABLE WRITE statements wait until there is no pending SELECT or LOCK TABLE READ on the affected table",
            "enum_value":[
                "ON",
                "OFF"
            ],
            "max":"0",
            "min":"0",
            "name":"low_priority_updates",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"0",
            "desc":"If set to 0, table names are stored as specified and comparisons are case sensitive. If set to 1, they are stored in lowercase on disk and comparisons are not case sensitive.",
            "enum_value":[
                
            ],
            "max":"1",
            "min":"0",
            "name":"lower_case_table_names",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"4194304",
            "desc":"The maximum size of one packet or any generated/intermediate string.",
            "enum_value":[
                
            ],
            "max":"1073741824",
            "min":"1024",
            "name":"max_allowed_packet",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"100",
            "desc":"If more than this many successive connection requests from a host are interrupted without a successful connection, the server blocks that host from further connections.",
            "enum_value":[
                
            ],
            "max":"4294967295",
            "min":"1",
            "name":"max_connect_errors",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"151",
            "desc":"The maximum permitted number of simultaneous client connections.",
            "enum_value":[
                
            ],
            "max":"10000",
            "min":"1",
            "name":"max_connections",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"1024",
            "desc":"The cutoff on the size of index values that determines which filesort algorithm to use.",
            "enum_value":[
                
            ],
            "max":"8388608",
            "min":"4",
            "name":"max_length_for_sort_data",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"16382",
            "desc":"This variable limits the total number of prepared statements in the server.",
            "enum_value":[
                
            ],
            "max":"1048576",
            "min":"0",
            "name":"max_prepared_stmt_count",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"30",
            "desc":"The number of seconds to wait for more data from a connection before aborting the read.",
            "enum_value":[
                
            ],
            "max":"4294967295",
            "min":"1",
            "name":"net_read_timeout",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"10",
            "desc":"If a read or write on a communication port is interrupted, retry this many times before giving up.",
            "enum_value":[
                
            ],
            "max":"4294967295",
            "min":"1",
            "name":"net_retry_count",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"60",
            "desc":"The number of seconds to wait for a block to be written to a connection before aborting the write.",
            "enum_value":[
                
            ],
            "max":"4294967295",
            "min":"1",
            "name":"net_write_timeout",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"5000",
            "desc":"The number of files that the operating system permits mysqld to open.",
            "enum_value":[
                
            ],
            "max":"102400",
            "min":"4000",
            "name":"open_files_limit",
            "need_reboot":"1",
            "type":"integer"
        },
        {
            "default":"8192",
            "desc":"The allocation size of memory blocks that are allocated for objects created during statement parsing and execution.",
            "enum_value":[
                
            ],
            "max":"16384",
            "min":"1024",
            "name":"query_alloc_block_size",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"1048576",
            "desc":"Do not cache results that are larger than this number of bytes. The default value is 1MB.",
            "enum_value":[
                
            ],
            "max":"1048576",
            "min":"1",
            "name":"query_cache_limit",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"0",
            "desc":"The amount of memory allocated for caching query results. By default, the query cache is disabled.",
            "enum_value":[
                
            ],
            "max":"104857600",
            "min":"0",
            "name":"query_cache_size",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"OFF",
            "desc":"Set the query cache type.",
            "enum_value":[
                "OFF",
                "ON",
                "DEMAND"
            ],
            "max":"0",
            "min":"0",
            "name":"query_cache_type",
            "need_reboot":"1",
            "type":"enum"
        },
        {
            "default":"8192",
            "desc":"The size of the persistent buffer used for statement parsing and execution. This buffer is not freed between statements.",
            "enum_value":[
                
            ],
            "max":"1048576",
            "min":"8192",
            "name":"query_prealloc_size",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"2",
            "desc":"If creating a thread takes longer than this many seconds, the server increments the Slow_launch_threads status variable",
            "enum_value":[
                
            ],
            "max":"10",
            "min":"1",
            "name":"slow_launch_time",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"NO_ENGINE_SUBSTITUTION",
            "desc":"The current server SQL mode.",
            "enum_value":[
                "NO_ENGINE_SUBSTITUTION",
                "ALLOW_INVALID_DATES",
                "ANSI_QUOTES",
                "ERROR_FOR_DIVISION_BY_ZERO",
                "HIGH_NOT_PRECEDENCE",
                "IGNORE_SPACE",
                "NO_AUTO_CREATE_USER",
                "NO_AUTO_VALUE_ON_ZERO",
                "NO_BACKSLASH_ESCAPES",
                "NO_DIR_IN_CREATE",
                "NO_ENGINE_SUBSTITUTION",
                "NO_FIELD_OPTIONS",
                "NO_KEY_OPTIONS",
                "NO_TABLE_OPTIONS",
                "NO_UNSIGNED_SUBTRACTION",
                "NO_ZERO_DATE",
                "NO_ZERO_IN_DATE",
                "ONLY_FULL_GROUP_BY",
                "PAD_CHAR_TO_FULL_LENGTH",
                "PIPES_AS_CONCAT",
                "REAL_AS_FLOAT",
                "STRICT_ALL_TABLES",
                "STRICT_TRANS_TABLES"
            ],
            "max":"0",
            "min":"0",
            "name":"sql_mode",
            "need_reboot":"0",
            "type":"enum"
        },
        {
            "default":"400",
            "desc":"The number of table definitions (from .frm files) that can be stored in the definition cache.",
            "enum_value":[
                
            ],
            "max":"4048",
            "min":"400",
            "name":"table_definition_cache",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"2000",
            "desc":"The number of open tables for all threads. Increasing this value increases the number of file descriptors that mysqld requires.",
            "enum_value":[
                
            ],
            "max":"524288",
            "min":"1",
            "name":"table_open_cache",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"16777216",
            "desc":"The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables.",
            "enum_value":[
                
            ],
            "max":"1073741824",
            "min":"1024",
            "name":"tmp_table_size",
            "need_reboot":"0",
            "type":"integer"
        },
        {
            "default":"3600",
            "desc":"The number of seconds the server waits for activity on a noninteractive connection before closing it",
            "enum_value":[
                
            ],
            "max":"86400",
            "min":"1",
            "name":"wait_timeout",
            "need_reboot":"0",
            "type":"integer"
        }
    ]
}
```


