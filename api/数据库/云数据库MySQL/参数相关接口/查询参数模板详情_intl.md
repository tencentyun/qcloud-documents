## 1. API Description
This API (GetCdbParamTemplateInfo) is used to query the parameter template list of the Cloud Database instance. You can use the template ID to query the details of the template.
You can also use API [Query List of Parameter Templates](/doc/api/253/7185) to query the details of the list of parameter templates.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbParamTemplateInfo.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| templateId | Yes | Int | Template ID, you can use API [Query List of Parameter Templates](/doc/api/253/7185) to query the parameter template ID |


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
| templateId | Int | Template ID |
| name | String | Template name |
| engineVersion | String | Database version number. Possible returned values include: 5.1, 5.5, and 5.6 |
| desc | String | Template description |
| paramList | Array | Returned parameter list |

Parameter paramList is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| default | String | Default value|
| cur_value | String | Current value |
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
| 9613 | InternalError | Database query error or null |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbParamTemplateInfo
&<<a href="/document/product/236/6921">Common request parameters</a>>
&templateId=1006
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":{
        "templateId":"1006",
        "name":"test",
        "engineVersion":"5.6",
        "desc":"",
        "paramList":[
            {
                "name":"auto_increment_increment",
                "type":"integer",
                "default":"1",
                "min":"1",
                "max":"65535",
                "desc":"Controls the interval between successive column values.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1"
            },
            {
                "name":"auto_increment_offset",
                "type":"integer",
                "default":"1",
                "min":"1",
                "max":"65535",
                "desc":"Determines the starting point for the AUTO_INCREMENT column value.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1"
            },
            {
                "name":"back_log",
                "type":"integer",
                "default":"1",
                "min":"1",
                "max":"65535",
                "desc":"The number of outstanding connection requests MySQL can have.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"1"
            },
            {
                "name":"binlog_checksum",
                "type":"enum",
                "default":"NONE",
                "min":"0",
                "max":"0",
                "desc":"When enabled, this variable causes the master to write a checksum for each event in the binary log.",
                "enum_value":[
                    "NONE",
                    "CRC32"
                ],
                "need_reboot":"0",
                "cur_value":"NONE"
            },
            {
                "name":"character_set_server",
                "type":"enum",
                "default":"latin1",
                "min":"0",
                "max":"0",
                "desc":"Specify default server character set",
                "enum_value":[
                    "latin1",
                    "utf8",
                    "gbk",
                    "utf8mb4"
                ],
                "need_reboot":"1",
                "cur_value":"latin1"
            },
            {
                "name":"connect_timeout",
                "type":"integer",
                "default":"10",
                "min":"2",
                "max":"1800",
                "desc":"The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"10"
            },
            {
                "name":"default_week_format",
                "type":"integer",
                "default":"0",
                "min":"0",
                "max":"7",
                "desc":"The default mode value to use for the WEEK() function",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"0"
            },
            {
                "name":"div_precision_increment",
                "type":"integer",
                "default":"4",
                "min":"0",
                "max":"30",
                "desc":"This variable indicates the number of digits by which to increase the scale of the result of division operations performed with the operator",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"4"
            },
            {
                "name":"event_scheduler",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"This variable indicates the status of the Event Scheduler",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"group_concat_max_len",
                "type":"integer",
                "default":"1024",
                "min":"4",
                "max":"4294967295",
                "desc":"The maximum permitted result length in bytes for the GROUP_CONCAT() function",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1024"
            },
            {
                "name":"innodb_adaptive_hash_index",
                "type":"enum",
                "default":"ON",
                "min":"0",
                "max":"0",
                "desc":"Whether the InnoDB adaptive hash index is enabled or disabled.",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"ON"
            },
            {
                "name":"innodb_autoinc_lock_mode",
                "type":"integer",
                "default":"1",
                "min":"0",
                "max":"2",
                "desc":"The lock mode to use for generating auto-increment values.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"1"
            },
            {
                "name":"innodb_flush_log_at_trx_commit",
                "type":"integer",
                "default":"1",
                "min":"0",
                "max":"2",
                "desc":"Controls the balance between strict ACID compliance for commit operations, and higher performance that is possible when commit-related I/O operations are rearranged and done in batches.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1"
            },
            {
                "name":"innodb_ft_max_token_size",
                "type":"integer",
                "default":"84",
                "min":"10",
                "max":"84",
                "desc":"Maximum character length of words that are stored in an InnoDB FULLTEXT index.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"84"
            },
            {
                "name":"innodb_ft_min_token_size",
                "type":"integer",
                "default":"3",
                "min":"0",
                "max":"16",
                "desc":"Minimum length of words that are stored in an InnoDB FULLTEXT index.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"3"
            },
            {
                "name":"innodb_large_prefix",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"Enable this option to allow index key prefixes longer than 767 bytes (up to 3072 bytes) for InnoDB tables that use the DYNAMIC and COMPRESSED row formats.",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"innodb_lock_wait_timeout",
                "type":"integer",
                "default":"7200",
                "min":"1",
                "max":"1073741824",
                "desc":"The length of time in seconds an InnoDB transaction waits for a row lock before giving up",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"7200"
            },
            {
                "name":"innodb_max_dirty_pages_pct",
                "type":"integer",
                "default":"75",
                "min":"0",
                "max":"99",
                "desc":"InnoDB tries to flush data from the buffer pool so that the percentage of dirty pages does not exceed this value",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"75"
            },
            {
                "name":"innodb_old_blocks_pct",
                "type":"integer",
                "default":"37",
                "min":"5",
                "max":"95",
                "desc":"Specifies the approximate percentage of the InnoDB buffer pool used for the old block sublist",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"37"
            },
            {
                "name":"innodb_old_blocks_time",
                "type":"integer",
                "default":"1000",
                "min":"0",
                "max":"2147483647",
                "desc":"Specifies the approximate percentage of the InnoDB buffer pool used for the old block sublist",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1000"
            },
            {
                "name":"innodb_open_files",
                "type":"integer",
                "default":"300",
                "min":"1",
                "max":"8192",
                "desc":"It specifies the maximum number of .ibd files that MySQL can keep open at one time.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"300"
            },
            {
                "name":"innodb_print_all_deadlocks",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"When this option is enabled, information about all deadlocks in InnoDB user transactions is recorded in the mysqld error log.",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"innodb_purge_batch_size",
                "type":"integer",
                "default":"300",
                "min":"1",
                "max":"5000",
                "desc":"The granularity of changes, expressed in units of redo log records, that trigger a purge operation, flushing the changed buffer pool blocks to disk.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"300"
            },
            {
                "name":"innodb_purge_threads",
                "type":"integer",
                "default":"1",
                "min":"1",
                "max":"32",
                "desc":"The number of background threads devoted to the InnoDB purge operation.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1"
            },
            {
                "name":"innodb_read_ahead_threshold",
                "type":"integer",
                "default":"56",
                "min":"0",
                "max":"64",
                "desc":"Controls the sensitivity of linear read-ahead that InnoDB uses to prefetch pages into the buffer pool",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"56"
            },
            {
                "name":"innodb_read_io_threads",
                "type":"integer",
                "default":"4",
                "min":"1",
                "max":"64",
                "desc":"The number of I/O threads for read operations in InnoDB.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"4"
            },
            {
                "name":"innodb_rollback_on_timeout",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"If innodb_rollback_on_timeout is specified, a transaction timeout causes InnoDB to abort and roll back the entire transaction.",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"innodb_stats_on_metadata",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"When this variable is enabled, InnoDB updates statistics when metadata statements such as SHOW TABLE STATUS or SHOW INDEX are run, or when accessing the INFORMATION_SCHEMA tables TABLES or STATISTICS",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"innodb_strict_mode",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"When innodb_strict_mode is ON, InnoDB returns errors rather than warnings for certain conditions",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"innodb_table_locks",
                "type":"enum",
                "default":"ON",
                "min":"0",
                "max":"0",
                "desc":"If autocommit = 0, InnoDB honors LOCK TABLES; MySQL does not return from LOCK TABLES ... WRITE until all other threads have released all their locks to the table. The default value of innodb_table_locks is 1, which means that LOCK TABLES causes InnoDB to lock a table internally if autocommit = 0.",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"ON"
            },
            {
                "name":"innodb_thread_concurrency",
                "type":"integer",
                "default":"0",
                "min":"0",
                "max":"128",
                "desc":"InnoDB tries to keep the number of operating system threads concurrently inside InnoDB less than or equal to the limit given by this variable.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"0"
            },
            {
                "name":"innodb_thread_sleep_delay",
                "type":"integer",
                "default":"0",
                "min":"0",
                "max":"4294967295",
                "desc":"How long InnoDB threads sleep before joining the InnoDB queue, in microseconds. ",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"0"
            },
            {
                "name":"innodb_write_io_threads",
                "type":"integer",
                "default":"4",
                "min":"1",
                "max":"64",
                "desc":"The number of I/O threads for write operations in InnoDB.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"4"
            },
            {
                "name":"interactive_timeout",
                "type":"integer",
                "default":"3600",
                "min":"1",
                "max":"86400",
                "desc":"The number of seconds the server waits for activity on an interactive connection before closing it",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"3600"
            },
            {
                "name":"log_queries_not_using_indexes",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"Whether queries that do not use indexes are logged to the slow query log",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"long_query_time",
                "type":"float",
                "default":"10",
                "min":"0.1",
                "max":"3600",
                "desc":"If a query takes longer than this many seconds, the server increments the Slow_queries status variable",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"10"
            },
            {
                "name":"low_priority_updates",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"If set to true, all INSERT, UPDATE, DELETE, and LOCK TABLE WRITE statements wait until there is no pending SELECT or LOCK TABLE READ on the affected table",
                "enum_value":[
                    "ON",
                    "OFF"
                ],
                "need_reboot":"0",
                "cur_value":"OFF"
            },
            {
                "name":"lower_case_table_names",
                "type":"integer",
                "default":"0",
                "min":"0",
                "max":"1",
                "desc":"If set to 0, table names are stored as specified and comparisons are case sensitive. If set to 1, they are stored in lowercase on disk and comparisons are not case sensitive.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"0"
            },
            {
                "name":"max_allowed_packet",
                "type":"integer",
                "default":"4194304",
                "min":"1024",
                "max":"1073741824",
                "desc":"The maximum size of one packet or any generated/intermediate string.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"4194304"
            },
            {
                "name":"max_connect_errors",
                "type":"integer",
                "default":"100",
                "min":"1",
                "max":"4294967295",
                "desc":"If more than this many successive connection requests from a host are interrupted without a successful connection, the server blocks that host from further connections.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"100"
            },
            {
                "name":"max_connections",
                "type":"integer",
                "default":"151",
                "min":"1",
                "max":"10000",
                "desc":"The maximum permitted number of simultaneous client connections.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"151"
            },
            {
                "name":"max_length_for_sort_data",
                "type":"integer",
                "default":"1024",
                "min":"4",
                "max":"8388608",
                "desc":"The cutoff on the size of index values that determines which filesort algorithm to use.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1024"
            },
            {
                "name":"max_prepared_stmt_count",
                "type":"integer",
                "default":"16382",
                "min":"0",
                "max":"1048576",
                "desc":"This variable limits the total number of prepared statements in the server.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"16382"
            },
            {
                "name":"net_read_timeout",
                "type":"integer",
                "default":"30",
                "min":"1",
                "max":"4294967295",
                "desc":"The number of seconds to wait for more data from a connection before aborting the read.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"30"
            },
            {
                "name":"net_retry_count",
                "type":"integer",
                "default":"10",
                "min":"1",
                "max":"4294967295",
                "desc":"If a read or write on a communication port is interrupted, retry this many times before giving up.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"10"
            },
            {
                "name":"net_write_timeout",
                "type":"integer",
                "default":"60",
                "min":"1",
                "max":"4294967295",
                "desc":"The number of seconds to wait for a block to be written to a connection before aborting the write.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"60"
            },
            {
                "name":"open_files_limit",
                "type":"integer",
                "default":"5000",
                "min":"4000",
                "max":"102400",
                "desc":"The number of files that the operating system permits mysqld to open.",
                "enum_value":[
                    
                ],
                "need_reboot":"1",
                "cur_value":"5000"
            },
            {
                "name":"query_alloc_block_size",
                "type":"integer",
                "default":"8192",
                "min":"1024",
                "max":"16384",
                "desc":"The allocation size of memory blocks that are allocated for objects created during statement parsing and execution.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"8192"
            },
            {
                "name":"query_cache_limit",
                "type":"integer",
                "default":"1048576",
                "min":"1",
                "max":"1048576",
                "desc":"Do not cache results that are larger than this number of bytes. The default value is 1MB.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"1048576"
            },
            {
                "name":"query_cache_size",
                "type":"integer",
                "default":"0",
                "min":"0",
                "max":"104857600",
                "desc":"The amount of memory allocated for caching query results. By default, the query cache is disabled.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"0"
            },
            {
                "name":"query_cache_type",
                "type":"enum",
                "default":"OFF",
                "min":"0",
                "max":"0",
                "desc":"Set the query cache type.",
                "enum_value":[
                    "OFF",
                    "ON",
                    "DEMAND"
                ],
                "need_reboot":"1",
                "cur_value":"OFF"
            },
            {
                "name":"query_prealloc_size",
                "type":"integer",
                "default":"8192",
                "min":"8192",
                "max":"1048576",
                "desc":"The size of the persistent buffer used for statement parsing and execution. This buffer is not freed between statements.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"8192"
            },
            {
                "name":"slow_launch_time",
                "type":"integer",
                "default":"2",
                "min":"1",
                "max":"10",
                "desc":"If creating a thread takes longer than this many seconds, the server increments the Slow_launch_threads status variable",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"2"
            },
            {
                "name":"sql_mode",
                "type":"enum",
                "default":"NO_ENGINE_SUBSTITUTION",
                "min":"0",
                "max":"0",
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
                "need_reboot":"0",
                "cur_value":"NO_ENGINE_SUBSTITUTION"
            },
            {
                "name":"table_definition_cache",
                "type":"integer",
                "default":"400",
                "min":"400",
                "max":"4048",
                "desc":"The number of table definitions (from .frm files) that can be stored in the definition cache.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"400"
            },
            {
                "name":"table_open_cache",
                "type":"integer",
                "default":"2000",
                "min":"1",
                "max":"524288",
                "desc":"The number of open tables for all threads. Increasing this value increases the number of file descriptors that mysqld requires.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"2000"
            },
            {
                "name":"tmp_table_size",
                "type":"integer",
                "default":"16777216",
                "min":"1024",
                "max":"1073741824",
                "desc":"The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables.",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"16777216"
            },
            {
                "name":"wait_timeout",
                "type":"integer",
                "default":"3600",
                "min":"1",
                "max":"86400",
                "desc":"The number of seconds the server waits for activity on a noninteractive connection before closing it",
                "enum_value":[
                    
                ],
                "need_reboot":"0",
                "cur_value":"3600"
            }
        ]
    }
}
```


