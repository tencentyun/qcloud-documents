## 1. API Description
This API (CdbTdsqlGetConfigList) is used to acquire the current parameter configurations of the database.

Domain for API request: tdsql.api.qcloud.com

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976
). The Action field for this API is CdbTdsqlGetConfigList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | Int | Instance ID |
| dbMode | No | Int | 0: Standalone; 1: Distributed (currently only Standalone is available, thus the parameter is not applicable) |

## 3. Output Parameters

The composition of returned values for common parameters can be found in [Returned Values](https://cloud.tencent.com/document/api/213/6976). The following only provides the formats of returned values for the "data" field.

| Parameter Name | Type | Description |
|---------|---------|---------|
| id | Int | Instance ID |
| config | Array | Parameters and related values. See example |
| config.param | String | Parameter name |
| config.value | String | Parameter value |
| config.set_value | String | The value set by the user last time |
| config.default | String | System default value |
| config.constraint.type | String | Constraint type, such as enum, section |
| config.constraint.min | String | Minimum value when constraint type is "section" |
| config.constraint.max | String |Maximum value when constraint type is "section" |
| config.constraint.enum | String | List of available values when constraint type is "enum" |
## 4. Error Codes

The following are the common error codes for this API. Other error codes not listed here can be found in [TDSQL Error Codes](/doc/api/309/7150).

| Error Code | Description |
|---------|---------|
| DbOperationFailed | DB internal failure |
| EINSTANCEDELETED | Instance has been deleted |
| InstanceStatusAbnormal | Operation is impossible due to instance status exception (not deleted) |
| OssOpertaionFailed | OSS internal failure|
| GetDbconfigFailed | Failed to acquire parameter |
## 5. Example
Input
<pre>
https://tdsql.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&Action=CdbTdsqlGetConfigList
&cdbInstanceId=40732
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "id": 40732,
        "config": [
            {
                "param": "auto_increment_increment",
                "value": "1",
                "set_value": "",
                "default": "1",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "65535"
                    }
                }
            },
            {
                "param": "auto_increment_offset",
                "value": "1",
                "set_value": "",
                "default": "1",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "65535"
                    }
                }
            },
            {
                "param": "autocommit",
                "value": "ON",
                "set_value": "",
                "default": "ON",
                "constraint": {
                    "type": "enum",
                    "enum": "ON,OFF"
                }
            },
            {
                "param": "character_set_server",
                "value": "utf8",
                "set_value": "",
                "default": "utf8",
                "constraint": {
                    "type": "enum",
                    "enum": "utf8,latin1,gbk,utf8mb4"
                }
            },
            {
                "param": "connect_timeout",
                "value": "10",
                "set_value": "",
                "default": "10",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "3600"
                    }
                }
            },
            {
                "param": "default_week_format",
                "value": "0",
                "set_value": "",
                "default": "0",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "0",
                        "max": "7"
                    }
                }
            },
            {
                "param": "delay_key_write",
                "value": "ON",
                "set_value": "",
                "default": "ON",
                "constraint": {
                    "type": "enum",
                    "enum": "ON,OFF,ALL"
                }
            },
            {
                "param": "delayed_insert_limit",
                "value": "100",
                "set_value": "",
                "default": "100",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "4294967295"
                    }
                }
            },
            {
                "param": "delayed_insert_timeout",
                "value": "300",
                "set_value": "",
                "default": "300",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "3600"
                    }
                }
            },
            {
                "param": "delayed_queue_size",
                "value": "1000",
                "set_value": "",
                "default": "1000",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "4294967295"
                    }
                }
            },
            {
                "param": "div_precision_increment",
                "value": "4",
                "set_value": "",
                "default": "4",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "0",
                        "max": "30"
                    }
                }
            },
            {
                "param": "group_concat_max_len",
                "value": "1024",
                "set_value": "",
                "default": "1024",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "4",
                        "max": "1844674407370954752"
                    }
                }
            },
            {
                "param": "innodb_concurrency_tickets",
                "value": "5000",
                "set_value": "",
                "default": "5000",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "100",
                        "max": "10000"
                    }
                }
            },
            {
                "param": "innodb_large_prefix",
                "value": "OFF",
                "set_value": "",
                "default": "OFF",
                "constraint": {
                    "type": "enum",
                    "enum": "OFF,ON"
                }
            },
            {
                "param": "innodb_lock_wait_timeout",
                "value": "50",
                "set_value": "",
                "default": "50",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "1073741824"
                    }
                }
            },
            {
                "param": "innodb_max_dirty_pages_pct",
                "value": "10",
                "set_value": "",
                "default": "10",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "10",
                        "max": "90"
                    }
                }
            },
            {
                "param": "innodb_old_blocks_pct",
                "value": "37",
                "set_value": "",
                "default": "37",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "5",
                        "max": "95"
                    }
                }
            },
            {
                "param": "innodb_old_blocks_time",
                "value": "1000",
                "set_value": "",
                "default": "1000",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "0",
                        "max": "1000"
                    }
                }
            },
            {
                "param": "innodb_page_size",
                "value": "4096",
                "set_value": "",
                "default": "4096",
                "constraint": {
                    "type": "enum",
                    "enum": "4096,8192,16384,32768,65536"
                }
            },
            {
                "param": "innodb_purge_batch_size",
                "value": "300",
                "set_value": "",
                "default": "300",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "1024"
                    }
                }
            },
            {
                "param": "innodb_read_ahead_threshold",
                "value": "56",
                "set_value": "",
                "default": "56",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "0",
                        "max": "64"
                    }
                }
            },
            {
                "param": "innodb_stats_method",
                "value": "nulls_equal",
                "set_value": "",
                "default": "nulls_equal",
                "constraint": {
                    "type": "enum",
                    "enum": "nulls_equal,nulls_unequal,nulls_ignored"
                }
            },
            {
                "param": "innodb_stats_on_metadata",
                "value": "OFF",
                "set_value": "",
                "default": "OFF",
                "constraint": {
                    "type": "enum",
                    "enum": "ON,OFF"
                }
            },
            {
                "param": "innodb_stats_sample_pages",
                "value": "8",
                "set_value": "",
                "default": "8",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "4294967296"
                    }
                }
            },
            {
                "param": "innodb_strict_mode",
                "value": "OFF",
                "set_value": "",
                "default": "OFF",
                "constraint": {
                    "type": "enum",
                    "enum": "ON,OFF"
                }
            },
            {
                "param": "innodb_table_locks",
                "value": "ON",
                "set_value": "",
                "default": "ON",
                "constraint": {
                    "type": "enum",
                    "enum": "ON,OFF"
                }
            },
            {
                "param": "innodb_thread_concurrency",
                "value": "0",
                "set_value": "",
                "default": "0",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "0",
                        "max": "128"
                    }
                }
            },
            {
                "param": "innodb_thread_sleep_delay",
                "value": "10000",
                "set_value": "",
                "default": "10000",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "3600000"
                    }
                }
            },
            {
                "param": "interactive_timeout",
                "value": "28800",
                "set_value": "",
                "default": "28800",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "10",
                        "max": "86400"
                    }
                }
            },
            {
                "param": "key_cache_block_size",
                "value": "1024",
                "set_value": "",
                "default": "1024",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "512",
                        "max": "16384"
                    }
                }
            },
            {
                "param": "key_cache_division_limit",
                "value": "100",
                "set_value": "",
                "default": "100",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "100"
                    }
                }
            },
            {
                "param": "lock_wait_timeout",
                "value": "5",
                "set_value": "",
                "default": "5",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "31536000"
                    }
                }
            },
            {
                "param": "log_queries_not_using_indexes",
                "value": "OFF",
                "set_value": "",
                "default": "OFF",
                "constraint": {
                    "type": "enum",
                    "enum": "ON,OFF"
                }
            },
            {
                "param": "long_query_time",
                "value": "1.000000",
                "set_value": "",
                "default": "1.000000",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "0.5",
                        "max": "10"
                    }
                }
            },
            {
                "param": "low_priority_updates",
                "value": "OFF",
                "set_value": "",
                "default": "OFF",
                "constraint": {
                    "type": "enum",
                    "enum": "OFF,ON"
                }
            },
            {
                "param": "lower_case_table_names",
                "value": "0",
                "set_value": "",
                "default": "1",
                "constraint": {
                    "type": "enum",
                    "enum": "0,1"
                }
            },
            {
                "param": "max_allowed_packet",
                "value": "134217728",
                "set_value": "",
                "default": "134217728",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "16384",
                        "max": "1073741824"
                    }
                }
            },
            {
                "param": "max_connect_errors",
                "value": "2000",
                "set_value": "",
                "default": "2000",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "4096"
                    }
                }
            },
            {
                "param": "myisam_sort_buffer_size",
                "value": "4194304",
                "set_value": "",
                "default": "4194304",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "262144",
                        "max": "16777216"
                    }
                }
            },
            {
                "param": "net_read_timeout",
                "value": "30",
                "set_value": "",
                "default": "30",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "3153600"
                    }
                }
            },
            {
                "param": "net_retry_count",
                "value": "10",
                "set_value": "",
                "default": "10",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "4294967295"
                    }
                }
            },
            {
                "param": "net_write_timeout",
                "value": "60",
                "set_value": "",
                "default": "60",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "3153600"
                    }
                }
            },
            {
                "param": "query_alloc_block_size",
                "value": "8192",
                "set_value": "",
                "default": "8192",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1024",
                        "max": "16384"
                    }
                }
            },
            {
                "param": "query_cache_limit",
                "value": "1048576",
                "set_value": "",
                "default": "1048576",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "1048576"
                    }
                }
            },
            {
                "param": "query_cache_size",
                "value": "0",
                "set_value": "",
                "default": "0",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "0",
                        "max": "104857600"
                    }
                }
            },
            {
                "param": "query_cache_type",
                "value": "OFF",
                "set_value": "",
                "default": "OFF",
                "constraint": {
                    "type": "enum",
                    "enum": "OFF,ON,DEMAND"
                }
            },
            {
                "param": "query_prealloc_size",
                "value": "8192",
                "set_value": "",
                "default": "8192",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "8192",
                        "max": "1048576"
                    }
                }
            },
            {
                "param": "slow_launch_time",
                "value": "2",
                "set_value": "",
                "default": "2",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "1",
                        "max": "1024"
                    }
                }
            },
            {
                "param": "table_definition_cache",
                "value": "400",
                "set_value": "",
                "default": "400",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "400",
                        "max": "2048"
                    }
                }
            },
            {
                "param": "table_open_cache",
                "value": "1024",
                "set_value": "",
                "default": "1024",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "400",
                        "max": "524288"
                    }
                }
            },
            {
                "param": "tmp_table_size",
                "value": "33554432",
                "set_value": "",
                "default": "33554432",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "262144",
                        "max": "67108864"
                    }
                }
            },
            {
                "param": "tx_isolation",
                "value": "REPEATABLE-READ",
                "set_value": "",
                "default": "REPEATABLE-READ",
                "constraint": {
                    "type": "enum",
                    "enum": "REPEATABLE-READ,SERIALIZABLE,READ-COMMITTED,READ-UNCOMMITTED"
                }
            },
            {
                "param": "wait_timeout",
                "value": "28800",
                "set_value": "",
                "default": "28800",
                "constraint": {
                    "type": "section",
                    "range": {
                        "min": "60",
                        "max": "259200"
                    }
                }
            }
        ]
    }
}
```


