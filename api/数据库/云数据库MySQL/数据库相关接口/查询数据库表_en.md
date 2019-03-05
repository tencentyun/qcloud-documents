## 1. API Description
This API (QueryCdbDatabaseTables) is used to query the database table information of Cloud Database instance.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is QueryCdbDatabaseTables.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cdbInstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals the uInstanceId field value in the output parameter.  |
| databases.n | Yes | String | One or more database names (n represents the array subscript starting from 0, which can be obtained using API [Query Database](/doc/api/253/7167) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error description |
| data | Array | Data of database table |
Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code returned for database query |
| message | String | Error message returned for database query |
| database | String | Database name |  
| TableList | Array | Information of database table list | 


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |


## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=QueryCdbDatabaseTables
&<<a href="/document/product/236/6921">Common request parameters</a>>
&cdbInstanceId=cdb-c1nl9rpv
&databases.0=mysql
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[
        {
            "database":"mysql",
            "code":"0",
            "message":"ok",
            "tableList":[
                "columns_priv",
                "db",
                "event",
                "func",
                "general_log",
                "help_category",
                "help_keyword",
                "help_relation",
                "help_topic",
                "innodb_index_stats",
                "innodb_table_stats",
                "ndb_binlog_index",
                "plugin",
                "proc",
                "procs_priv",
                "proxies_priv",
                "servers",
                "slave_master_info",
                "slave_relay_log_info",
                "slave_worker_info",
                "slow_log",
                "tables_priv",
                "time_zone",
                "time_zone_leap_second",
                "time_zone_name",
                "time_zone_transition",
                "time_zone_transition_type",
                "user"
            ]
        }
    ]
}
```


