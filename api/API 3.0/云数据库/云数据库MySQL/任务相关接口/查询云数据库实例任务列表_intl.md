## 1. API Description

Domain name for API request: cdb.tencentcloudapi.com.

This API (DescribeTasks) is used to query the list of database instance tasks.

A maximum of 100 requests can be initiated per second for this API.

Note: This API supports Finance regions. Since Finance regions and non-Finance regions are isolated and not interconnected. If the common parameter Region is a Finance region (such as ap-shanghai-fsi), you need to specify a domain name containing the Finance region that should be identical to the value of Region field, for example: cdb.ap-shanghai-fsi.tencentcloudapi.com.



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/236/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: DescribeTasks |
| Version | Yes | String | Common parameter. The value used for this API: 2017-03-20 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/236/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceId | No | String | Instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the database console page and can be obtained via API [Query Instance List](https://cloud.tencent.com/document/api/236/15872). Its value equals the InstanceId field value in the output parameters. |
| AsyncRequestId | No | String | ID of an async task request, which is returned as a result of a database-related operation |
| TaskTypes.N | No |  Array of Integer | Task type. All task types are queried if no value is passed. Possible values include: 1 - database rollback; 2 - SQL operation; 3 - data import; 5 - parameter configuration; 6 - initialization; 7 - restart; 8 - enable GTID; 9 - read-only instance upgrade; 10 - batch rollback of databases; 11 - master instance upgrade; 12 - delete database list; 13 - switch to master instance. |
| TaskStatus.N | No | Array of Integer | Task status. All task statuses are queried if no value is passed. Possible values include: -1 - Undefined; 0 - Initializing; 1 - Running; 2 - Execution succeeded; 3 - Execution failed; 4 - Terminated; 5 - Deleted; 6 - Suspended. |
| StartTimeBegin | No | String | Start time of the first task, which is used for range query. Format example: 2017-12-31 10:40:01 |
| StartTimeEnd | No | String | Start time of the last task, which is used for range query. Format example: 2017-12-31 10:40:01 |
| Offset | No | Integer | Record offset. Default is 0. |
| Limit | No | Integer | Number of results returned for a single request. Default is 20, and maximum is 100. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| TotalCount | Integer | Number of instances that meet the condition |
| Items | Array of String | Returned instance task information |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/236/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| CdbError | Backend error or process error. |
| InternalError.DatabaseAccessError | Database's internal error. |
| InternalError.DesError | System's internal error. |
| InvalidParameter | Parameter error. |
| InvalidParameter.InstanceNotFound | The instance does not exist. |
| OperationDenied | The operation is not allowed. |
| OperationDenied.WrongStatus | The backend task status is invalid. |

## 5. Example

### Example 1 Query the list of database instance tasks

#### Input example

```
https://cdb.tencentcloudapi.com/?Action=DescribeTasks
&InstanceIds.0=cdb-eb2w7dto
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "Items": [
      {
        "Code": 0,
        "Data": [
          {
            "Character_set_server": "utf8",
            "InstanceId": "cdb-gt70m8aa",
            "Lower_case_table_names": "0",
            "Vport": 3306
          }
        ],
        "EndTime": "2017-06-27 15:06:36",
        "JobId": 15964,
        "Message": "Instance initialized successfully",
        "Progress": 100,
        "StartTime": "2017-06-27 15:05:33",
        "Status": 2,
        "Type": 6
      },
      {
        "Code": -5003,
        "Data": [
          {
            "Code": 3,
            "Databases": [
              {
                "Code": 3,
                "Database": "clear_test",
                "Message": "dial tcp :0: connection refused"
              }
            ],
            "EndTime": "2017-07-21 17:19:31",
            "InstanceId": "cdb-atjl8gns",
            "Message": "dial tcp :0: connection refused",
            "StartTime": "2017-07-21 17:19:30"
          }
        ],
        "EndTime": "2017-07-21 17:19:31",
        "JobId": 51788,
        "Message": "",
        "Progress": 0,
        "StartTime": "2017-07-21 17:19:30",
        "Status": 3,
        "Type": 2
      },
      {
        "Code": 0,
        "Data": [
          {
            "After": {
              "CdbType": "CUSTOM",
              "DeployMode": "",
              "EngineVersion": "5.6",
              "MasterZone": 160002,
              "Memory": 2000,
              "ProtectMode": "",
              "SlaveZoneFirst": 160002,
              "SlaveZoneSecond": "",
              "Volume": 100
            },
            "Before": {
              "CdbType": "CUSTOM",
              "DeployMode": "",
              "EngineVersion": "5.6",
              "MasterZone": 160002,
              "Memory": 1000,
              "ProtectMode": "",
              "SlaveZoneFirst": 160002,
              "SlaveZoneSecond": "",
              "Volume": 50
            },
            "DealName": "20170627160000060843141595228010",
            "InstanceId": "cdb-gt70m8aa"
          }
        ],
        "EndTime": "2017-06-27 15:16:57",
        "JobId": 15967,
        "Message": "Instance upgrade completed",
        "Progress": 100,
        "StartTime": "2017-06-27 15:13:52",
        "Status": 2,
        "Type": 11
      },
      {
        "Code": 0,
        "Data": [
          {
            "InstanceId": "",
            "Parameters": [
              {
                "Code": 0,
                "CurrentValue": "2",
                "Message": "ok",
                "Name": "back_log",
                "OldValue": "210"
              }
            ]
          }
        ],
        "EndTime": "2017-06-27 16:34:25",
        "JobId": 15969,
        "Message": "Parameter set successfully",
        "Progress": 100,
        "StartTime": "2017-06-27 16:33:40",
        "Status": 2,
        "Type": 5
      },
      {
        "Code": 3,
        "Data": [
          {
            "CostTime": 0,
            "Database": "test",
            "FileName": "skyler.sql",
            "FileSize": "12",
            "InstanceId": ""
          }
        ],
        "EndTime": "2017-06-27 16:47:23",
        "JobId": 15970,
        "Message": "Warning: Using a password on the command line interface can be insecure.?ERROR 1064 (42000) at line 1: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'joell=skyler' at line 1?dumper err?",
        "Progress": 5,
        "StartTime": "2017-06-27 16:46:52",
        "Status": 3,
        "Type": 3
      },
      {
        "Code": 3,
        "Data": [
          {
            "CostTime": 0,
            "Database": "test",
            "FileName": "joellwang_1_4.sql",
            "FileSize": "5857113",
            "InstanceId": ""
          }
        ],
        "EndTime": "2017-06-27 16:49:44",
        "JobId": 15971,
        "Message": "Warning: Using a password on the command line interface can be insecure.?ERROR 2006 (HY000) at line 1: MySQL server has gone away?dumper err?",
        "Progress": 5,
        "StartTime": "2017-06-27 16:49:13",
        "Status": 3,
        "Type": 3
      },
      {
        "Code": 0,
        "Data": [
          {
            "CostTime": 19,
            "Database": "test",
            "FileName": "LearningSQLExample.sql",
            "FileSize": "28384",
            "InstanceId": ""
          }
        ],
        "EndTime": "2017-06-27 17:03:00",
        "JobId": 15972,
        "Message": "success",
        "Progress": 100,
        "StartTime": "2017-06-27 17:02:29",
        "Status": 2,
        "Type": 3
      },
      {
        "Code": 0,
        "Data": [
          {
            "After": {
              "CdbType": "CUSTOM",
              "DeployMode": "",
              "EngineVersion": "5.6",
              "MasterZone": 160002,
              "Memory": 8000,
              "ProtectMode": "",
              "SlaveZoneFirst": 160002,
              "SlaveZoneSecond": "",
              "Volume": 100
            },
            "Before": {
              "CdbType": "CUSTOM",
              "DeployMode": "",
              "EngineVersion": "5.6",
              "MasterZone": 160002,
              "Memory": 8000,
              "ProtectMode": "",
              "SlaveZoneFirst": 160002,
              "SlaveZoneSecond": "",
              "Volume": 50
            },
            "DealName": "20170627160000060849699827143219",
            "InstanceId": "cdb-o8cacfkg"
          }
        ],
        "EndTime": "2017-06-27 18:08:25",
        "JobId": 15974,
        "Message": "Instance upgrade completed",
        "Progress": 100,
        "StartTime": "2017-06-27 18:04:19",
        "Status": 2,
        "Type": 11
      },
      {
        "Code": 0,
        "Data": [
          {
            "Character_set_server": "utf8",
            "InstanceId": "cdb-7262qp3q",
            "Lower_case_table_names": "0",
            "Vport": 3306
          }
        ],
        "EndTime": "2017-06-27 19:19:34",
        "JobId": 15976,
        "Message": "Instance initialized successfully",
        "Progress": 100,
        "StartTime": "2017-06-27 19:18:31",
        "Status": 2,
        "Type": 6
      },
      {
        "Code": 0,
        "Data": [
          {
            "Code": 0,
            "DatabaseTables": [
              {
                "Database": "monitor_master",
                "Tables": [
                  {
                    "NewTableName": "monitor_alarm_bak_1",
                    "TableName": "monitor_alarm"
                  }
                ]
              }
            ],
            "Databases": [
              {
                "DatabaseName": "test",
                "NewDatabaseName": "test_bak"
              }
            ],
            "InstanceId": "cdb-ewgjla5w",
            "Message": "Rollback succeeded",
            "Progress": 100,
            "RollbackTime": "2017-04-06 16:00:00",
            "Status": 2
          }
        ],
        "EndTime": "2017-04-06 20:45:03",
        "JobId": 51695,
        "Message": "Rollback of all instances succeeded",
        "Progress": 100,
        "StartTime": "2017-04-06 20:42:59",
        "Status": 2,
        "Type": 10
      }
    ],
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
    "TotalCount": 13
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

