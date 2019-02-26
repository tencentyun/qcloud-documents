## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeBackupTables) is used to query the backup data tables of a specified database.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeBackupTables |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | Yes | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page. |
| StartTime | Yes | String | Start time, such as 2017-07-12 10:29:20. |
| DatabaseName | Yes | String | Name of the specified database. |
| SearchTable | No | String | The prefix of the data tables to be queried. |
| Offset | No | Integer | Page offset. |
| Limit | No | Integer | Page size. The maximum is 2000. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of returned results. |
| Items | Array of [TableName](/document/api/236/##TableName) | An array of data tables that meet the condition. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalError.DatabaseAccessError | Database's internal error. |
| InvalidParameter | Parameter error. |
| InvalidParameter.InstanceNotFound | The instance does not exist. |

## 5. Example

### Example 1 Query the backup data tables of a specified database

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeBackupTables
&InstanceId=cdb-c1nl9rpv
&StartTime=2017-07-12 10:29:20
&DatabaseName=mysql
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Items": [
      {
        "TableName": "general_log"
      },
      {
        "TableName": "slow_log"
      },
      {
        "TableName": "columns_priv"
      },
      {
        "TableName": "db"
      },
      {
        "TableName": "event"
      },
      {
        "TableName": "func"
      },
      {
        "TableName": "help_category"
      },
      {
        "TableName": "help_keyword"
      },
      {
        "TableName": "help_relation"
      },
      {
        "TableName": "help_topic"
      },
      {
        "TableName": "innodb_index_stats"
      },
      {
        "TableName": "innodb_table_stats"
      },
      {
        "TableName": "ndb_binlog_index"
      },
      {
        "TableName": "plugin"
      },
      {
        "TableName": "proc"
      },
      {
        "TableName": "procs_priv"
      },
      {
        "TableName": "proxies_priv"
      },
      {
        "TableName": "servers"
      },
      {
        "TableName": "slave_master_info"
      },
      {
        "TableName": "slave_relay_log_info"
      },
      {
        "TableName": "slave_worker_info"
      },
      {
        "TableName": "tables_priv"
      },
      {
        "TableName": "time_zone"
      },
      {
        "TableName": "time_zone_leap_second"
      },
      {
        "TableName": "time_zone_name"
      },
      {
        "TableName": "time_zone_transition"
      },
      {
        "TableName": "time_zone_transition_type"
      },
      {
        "TableName": "user"
      }
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "TotalCount": "28"
  }
}
```


## 6. Other Resources

Cloud API 3.0 comes with the following development tools to make it easier to call the API.

* [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
* [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
* [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
* [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
* [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
* [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)
* [Tencent Cloud CLI 3.0](https://cloud.tencent.com/document/product/440/6176)

