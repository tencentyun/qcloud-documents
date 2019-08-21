## 1. API Description
This API (GetCdbDataMigrationTaskList) is used to query the data migration task list and return the details of the data migration task.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbDataMigrationTaskList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobId | No | Int | Data migration task ID, through which the task execution details can be obtained |
| jobName | No | String | Name of data migration task |
| status | No | Array | A set of data migration task statuses. Possible values include: < br > 0 - Not configured <br>1 - Configured <br>2 - Verifying <br>3 - Verification failed <br>4 - Verification succeeded <br>5 - Ready to migrate<br>6 - Migrating <br>7 - To be switched <br>8 - Migration failed <br>9 - Migration succeeded |
| migrateType | No | Int |Data migration type. Possible values include: <br>1 - structural migration <br>2 - full migration <br>3 - full + incremental migration |
| dstUInstanceId | No | String | Destination instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained using API [Query List of Instances](/doc/api/253/1266). Its value equals the uInstanceId field value in the output parameter.  |
| type | No | Array | Task type. Values include: < br > 1 - Source instance is self-built MySQL in public network; <br>2 - Source instance is self-built MySQL in basic network; <br>3 - Source instance is self-built MySQL in VPC; <br>4 - Source instance is connected through Direct Connect; <br>5 - Source instance is connected through Cloud VPN; <br>6 - Source instance is connected through self-built VPN |
| runMode | No | Int | Task run mode. Values include: 1 - Immediate execution; 2 - scheduled execution |
| order | No | String | Sorting field, which can be jobId, status, jobName, migrateType, type, runMode, submitTime |
| orderSeq | No | String | Sorting mode. ASC indicates an ascending order, and DESC indicates a descending order |
| offset | No | Int | Offset; default is 0 |
| limit | No | Int | Number of returned instances. Default is 20, and valid value range is [1,100] |
| submitTimeStart | No | String | Start time of task submission. Format: yyyy-mm-dd hh: mm: ss |
| submitTimeEnd | No | String | End time of task submission. Format: yyyy-mm-dd hh: mm: ss |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Object | Returned data |
| data.totalCount | Int | Number of data migration tasks that satisfy the query criteria |
| data.jobList | Array | Paged list of data migration tasks |

Each element in the jobList is an Object, which is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Execution status code of data migration task. 0: Succeed; other values: Failed. |
| message | String | Message indicating the execution status of data migration task |
| jobId | Int | ID of data migration task |
| type | Int | Data migration task type. Values include: <br>0 - Not configured; <br>1 - Source instance is self-built MySQL in public network; <br>2 - Source instance is self-built MySQL in basic network; <br>3 - Source instance is self-built MySQL in VPC; <br>4 - Source instance is connected through Direct Connect; <br>5 - Source instance is connected through Cloud VPN; <br>6 - Source instance is connected through self-built VPN |
| status | Int | Execution status of data migration task. Values include: < br > 0 - Not configured <br>1 - Configured <br>2 - Verifying <br>3 - Verification failed <br>4 - Verification succeeded <br>5 - Ready to migrate <br>6 - Migrating <br>7 - To be switched <br>8 - Migration failed <br>9 - Migration succeeded |
| progress | Int | Execution progress of data migration task |
| startTime | String | Start time of data migration task. Format: yyyy-mm-dd hh:mm:ss |
| EndTime | String | End time of data migration task. Format: yyyy-mm-dd hh:mm:ss |
| detail | Object | Other details of data migration task |

Parameter detail is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobName | String | Name of data migration task |
| runMode | Int | Run mode of task. Values include: 1 - Immediate execution; 2 - Scheduled execution |
| migrateType | Int |Data migration type. Values include: <br>1 - Structural migration <br>2 - Full migration <br>3 - Full + Incremental migration|
| extMsg | String | Error message returned during the execution of data migration task |
| srcInfo | Object | Source instance information depending on the migration task type. Please refer to the description in "Creating Migration Task". |
| dstInfo | Object | Destination instance information that contains cdbUInstanceId | 
| jobInput | Object | Information on the stop of task |
| checkInfo | Object | Information on the verification of data migration task |
| jobOutput | Object | Information on the migration task execution process |
| expectTime | String | Expected execution time of migration task. Format: yyyy-mm-dd hh:mm:ss |
| updateTime | String | Update time of migration task status. Format: yyyy-mm-dd hh:mm:ss | 
| submitTime | String | Submission time of migration task. Format: yyyy-mm-dd hh:mm:ss |

Parameter JobInput is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| stopStatus | Int | Stop status code of data migration task. 100 - Task is being stopped forcibly; 101 - Task has stopped successfully; 102 - Task failed to stop |
| stopMsg | String | Information on the stop of data migration task |

Parameter CheckInfo is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| checkFlag | Int | Verification status of data migration task. 0 - Not verified; 1 - Passed verification; 2 - Failed verification |
| checkResult | Object | Details of verification of data migration task, which is shown step by step. Please refer to the example. |

Parameter jobOutput is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Status code of data migration task. 0: Succeeded; other values: Failed |
| message | String | Error message returned during the execution of data migration task |
| stepAll | Int | Total number of steps for executing data migration task | 
| stepNow | Int | ID of the current step for executing data migration task |
| stepName | Int | Name of the current step for executing data migration task |
| stepPercent | Int | Percent of the steps that have been taken in the execution of data migration task |
| CostTime | Int | Time that has been consumed in the execution of data migration task (in seconds) |
| createTime | String | Creation time of the data migration task at backend |
| masterSlaveDistance | Int | Synchronization distance between master and slave instances (in megabytes) |
| secondsBehindMaster | Int | Master Slave Sync Delay, in S |
| stepInfo | Object | Step information of data migration task execution process. Please refer to the example |

## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9006 | InternalError | Database internal error |
| 9013 | InternalError | System internal error |
| 9016 | InternalError | System internal error |
| 9544 | OperationDenied | Instance does not exist |
| 9572 | InstanceNotExists | Instance does not exist |
| 9590 | InternalFailure | Migration task database access error |
| 9593 | IncorrectInstanceStatus | Abnormal instance status|

## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbDataMigrationTaskList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&jobId=121
&jobName=The source instance is connected through a self-built VPN
&status.0=1
&migrateType=3
&dstUInstanceId=cdb-eg60tvyu
&type.0=6
&runMode=1
&order=jobId
&orderSeq=ASC
&offset=0
&limit=1
&submitTimeStart=2017-02-22 11:35:04
&submitTimeEnd=2017-02-22 11:35:06
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "totalCount": 1,
        "jobList": [
            {
                "code": 0,
                "message": "The task has been terminated",
                "jobId": 121,
                "type": 6,
                "status": 1,
                "progress": 14,
                "startTime": "2017-02-22 12:47:37",
                "endTime": "2017-02-22 13:00:13",
                "detail": {
                    "jobName": "The source instance is connected through a self-built VPN",
                    "runMode": "1",
                    "migrateType": "3",
                    "extMsg": "ok",
                    "srcInfo": {
                        "cvmUInstanceId": "ins-qjzk0p8m",
                        "mysqlIp": "10.104.62.7",
                        "mysqlPort": 3306,
                        "mysqlUser": "root",
                        "dbInfo": [],
                        "vpcId": 725,
                        "subnetId": 25961,
                        "unVpcId": "vpc-f7xkdzdv",
                        "unSubnetId": "subnet-b54d3t3w",
                        "vpnSelfBuildIP": "10.0.0.116",
                        "isOverrideRoot": 0
                    },
                    "dstInfo": {
                        "cdbUInstanceId": "cdb-eg60tvyu"
                    },
                    "jobInput": {
                        "stopStatus": 100,
                        "stopMsg": "The task is being terminated"
                    },
                    "checkInfo": {
                        "checkFlag": 2
                        "checkResult": {
                            "code": 0,
                            "message": "ok",
                            "status": "finished",
                            "isSuccess": 0,
                            "stepInfo": [
                                {
                                    "stepNo": 1,
                                    "stepName": "Check the parameters",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 2,
                                    "stepName": "Query the destination instance information",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 3,
                                    "stepName": "Request for dfw permission",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 4,
                                    "stepName": "Attempt to connect to the source instance",
                                    "code": -1,
                                    "message": "Source instance permission verification failed [ SQL ERROR[errno:2013, errors:Lost connection to MySQL server at 'reading initial communication packet', system error: 110]]"
                                },
                                {
                                    "stepNo": 5,
                                    "stepName": "Check source instance permission",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 6,
                                    "stepName": "Check source instance configuration",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 7,
                                    "stepName": "Check compatibility",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 8,
                                    "stepName": "Obtain the size of the source instance data to be migrated",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 9,
                                    "stepName": "Check the remaining space of destination machine",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 10,
                                    "stepName": "Check if the destination instance is empty",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 11,
                                    "stepName": "Check if the destination instance has enough space",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 12,
                                    "stepName": "Check whether the database table to be migrated has a duplicate",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 13,
                                    "stepName": "Check log filtering for destination instance",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 14,
                                    "stepName": "Check the foreign key engine and so on",
                                    "code": -3,
                                    "message": "To be checked"
                                },
                                {
                                    "stepNo": 15,
                                    "stepName": " Release dfw permission",
                                    "code": -3,
                                    "message": "To be checked"
                                }
                            ]
                        }
                    },
                    "jobOutput": {
                        "code": 0,
                        "message": "The migration task has stopped"
                        "stepAll": 7,
                        "stepNow": 1,
                        "stepName": "Check the parameters",
                        "stepPercent": "0.00",
                        "costTime": 756,
                        "createTime": "2017-02-22 12:47:37",
                        "masterSlaveDistance": 0,
                        "secondsBehindMaster": 0,
                        "stepInfo": [
                            {
                                "stepNo": 1,
                                "stepName": "Check the parameters",
                                "stepRemark": ""
                            },
                            {
                                "stepNo": 2,
                                "stepName": "Migrate configurations",
                                "stepRemark": ""
                            },
                            {
                                "stepNo": 3,
                                "stepName": "Export cold backup",
                                "stepRemark": ""
                            },
                            {
                                "stepNo": 4,
                                "stepName": "Import cold backup",
                                "stepRemark": ""
                            },
                            {
                                "stepNo": 5,
                                "stepName": "Build master and slave log synchronization",
                                "stepRemark": ""
                            },
                            {
                                "stepNo": 6,
                                "stepName": "Data comparison",
                                "stepRemark": ""
                            },
                            {
                                "stepNo": 7,
                                "stepName": "Stop master and slave instances",
                                "stepRemark": ""
                            }
                        ]
                    },
                    "expectTime": "0000-00-00 00:00:00",
                    "updateTime": "2017-02-22 13:27:01",
                    "submitTime": "2017-02-22 11:35:05"
                }
            }
        ]
    }
}
```


