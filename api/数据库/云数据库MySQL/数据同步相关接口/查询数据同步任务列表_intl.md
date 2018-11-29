## 1. API Description
This API (GetCdbDataMigrationTaskList) is used to query data synchronization task list and return the details of data synchronization task.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/doc/api/372/4153' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbDataSyncTaskList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| jobId | No | Int | ID of data synchronization task. Please use API "Query Data Synchronization Task List" to query the task ID |
| jobName | Yes | String | Name of data synchronization task |
| status | No | Array | A set of data synchronization task statuses. Possible values include: < br > 0 - Not configured <br>1 - Configured <br>2 - Verifying <br>3 - Verification Failed <br>4 - Verification Succeeded <br>5 - Ready to Synchronize <br>6 - Synchronizing <br>7 - To be Switched <br>8 - Synchronization Failed <br>9 - Synchronization Succeeded |
| srcUInstanceId | No | String | Master instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained via API [Query List of Instances](/doc/api/253/1266). Its value equals uInstanceId field value in the output parameter.  |
| dstUInstanceId | No | String | Disaster recovery instance ID, such as: cdb-c1nl9rpv. It is identical to the instance ID displayed in the Cloud Database console page and can be obtained via API [Query List of Instances](/doc/api/253/1266). Its value equals to uInstanceId field value in the output parameter.  |
| order | No | String | Sorting field. Values include jobId, status, jobName and submitTime |
| orderSeq | No | String | Sorting mode. ASC indicates an ascending order, and DESC indicates a descending order |
| offset | No | Int | Offset; default is 0 |
| limit | No | Int | Number of returned instances. Default is 20, and valid value range is [1,100] |
| submitTimeStart | No | String | Start time of task submission. Format: yyyy-mm-dd hh: mm: ss |
| submitTimeEnd | No | String | End time of task submission. Format: yyyy-mm-dd hh: mm: ss |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Object | Returned data |
| data.totalCount | Int | Number of data synchronization tasks that satisfy the query criteria |
| data.jobList | Array | Paged list of data synchronization tasks |

Each element in the jobList is an Object, which is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Status code of data synchronization task execution. 0: Succeeded; other values: Failed. |
| message | String | Status information about data synchronization task execution |
| jobId | Int | ID of data synchronization task |
| Type | Int | Data synchronization task type. Available value: < br > 10-Disaster recovery instance synchronization task|
| status | Int | status of data synchronization task execution. Values include: < br > 0 - Not configured <br>1 - Configured <br>2 - Verifying <br>3 - Verification failed <br>4 - Verification succeeded <br>5 - Ready to synchronize <br>6 - Synchronizing <br>7 - To be switched <br>8 - Synchronization failed <br>9 - Synchronization succeeded |
| progress | Int | Execution progress of data synchronization task |
| startTime | String | Start time of data synchronization task. Format: yyyy-mm-dd hh:mm:ss |
| EndTime | String | End time of data synchronization task. Format: yyyy-mm-dd hh:mm:ss |
| detail | Object | Other details of data synchronization task |

Parameter detail is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| jobName | String | Name of data synchronization task |
| runMode | Int | Run mode of task. Values include: 1 - immediate execution; 2 - scheduled execution |
| migrateType | Int |Data synchronization type. Values include: <br>1 - structural synchronization <br>2 - full synchronization <br>3 - full + incremental synchronization |
| extMsg | String | Message on data synchronization task executed at backend|
| srcInfo | Object | Source instance information, which contains region and cdbUInstanceId |
| dstInfo | Object | Destination instance information, which contains region and cdbUInstanceId | 
| jobInput | Object | Information on the stop of task|
| checkInfo | Object | Information on the verification of data synchronization task |
| jobOutput | Object | Information on the synchronization task execution process |
| expectTime | String | Expected execution time of synchronization task. Format: yyyy-mm-dd hh:mm:ss 
| updateTime | String | Update time of synchronization task status. Format: yyyy-mm-dd hh:mm:ss | 
| submitTime | String | Submission time of the synchronization task. Format: yyyy-mm-dd hh:mm:ss |

Parameter JobInput is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| stopStatus | Int | Stop status code of data synchronization task. 100 - Task is being stopped forcibly; 101 - Task has stopped successfully; 102 - Task failed to stop |
| stopMsg | String | Information on the stop of data synchronization task |

Parameter CheckInfo is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| checkFlag | Int | Verification status of data synchronization task. 0 - Not verified; 1 - Verification succeeded; 2 - Verification failed|
| checkResult | Object | Details of verification of data synchronization task, which is shown step by step. Please refer to the example. |

Parameter jobOutput is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Status code of data synchronization task execution. 0: Succeeded; other values: Failed. |
| message | String | Error message returned during the execution of data synchronization task |
| stepAll | Int | Total number of steps for executing data synchronization task |
| stepNow | Int | ID of the current step for executing data synchronization task |
| stepName | Int | Name of the current step for executing data synchronization task |
| stepPercent | String | Percent of the steps that have been taken in the execution of data synchronization task |
| CostTime | Int | Time that has been consumed in the execution of data synchronization task (in seconds) |
| createTime | String | Creation time of the data synchronization task at backend |
| stepInfo | Object | Step information of data synchronization task execution process. Please refer to the example |

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
| 9590 | InternalFailure | Synchronization task database access error |
| 9593 | IncorrectInstanceStatus | Abnormal instance status |

## 5. Example
Input
<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbDataSyncTaskList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&offset=0
&limit=1
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
                "message": "",
                "jobId": 124,
                "type": 10,
                "status": 9,
                "progress": 100,
                "startTime": "2017-02-23 15:04:10",
                "endTime": "2017-02-23 15:06:00",
                "detail": {
                    "jobName": "Synchronization of disaster recovery instance",
                    "runMode": "1",
                    "migrateType": "3",
                    "extMsg": "Instance upgrade succeeded",
                    "srcInfo": {
                        "regionId": 1,
                        "cdbUInstanceId": "cdb-5u7czxdx",
                        "dbInfo": [],
                        "isOverrideRoot": 1
                    },
                    "dstInfo": {
                        "regionId": 4,
                        "cdbUInstanceId": "cdb-ek0t57qd"
                    },
                    "jobInput": [],
                    "checkInfo": {
                        "checkFlag": 1,
                        "checkResult": {
                            "code": 0,
                            "message": "Disaster recovery instance check succeeded",
                            "status": "finished",
                            "isSuccess": 1,
                            "stepInfo": [
                                {
                                    "stepNo": 1,
                                    "stepName": "Check the parameters",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 2,
                                    "stepName": "Check source instance",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 3,
                                    "stepName": "Check destination instance",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 4,
                                    "stepName": "Check instance status",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 5,
                                    "stepName": "Check instance specification",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 6,
                                    "stepName": "Check instance version",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 7,
                                    "stepName": "Check if the destination instance is empty",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 8,
                                    "stepName": "Check database table information of instance synchronization",
                                    "code": 0,
                                    "message": "Verification succeeded"
                                },
                                {
                                    "stepNo": 9,
                                    "stepName": "Check cold backup data of instance",
                                    "code": 0,
                                    "message": "Succeeded"
                                }
                            ]
                        }
                    },
                    "jobOutput": {
                        "code": 0,
                        "message": "Disaster recovery instance synchronization succeeded",
                        "status": "normal_finish",
                        "stepAll": 6,
                        "stepNow": 6,
                        "stepName": "Create cold backup",
                        "stepPercent": "100.00",
                        "costTime": 111,
                        "createTime": "2017-02-23 15:04:09",
                        "stepInfo": [
                            {
                                "stepNo": 1,
                                "stepName": "Check environment",
                                "canStop": 0
                            },
                            {
                                "stepNo": 2,
                                "stepName": "Migrate configurations",
                                "canStop": 0
                            },
                            {
                                "stepNo": 3,
                                "stepName": "Import cold backup",
                                "canStop": 1
                            },
                            {
                                "stepNo": 4,
                                "stepName": "Build master-slave relationship",
                                "canStop": 0
                            },
                            {
                                "stepNo": 5,
                                "stepName": "Waiting for synchronization",
                                "canStop": 1
                            },
                            {
                                "stepNo": 6,
                                "stepName": "Create cold backup",
                                "canStop": 0
                            }
                        ]
                    },
                    "expectTime": "0000-00-00 00:00:00",
                    "updateTime": "2017-02-23 15:06:00",
                    "submitTime": "2017-02-22 22:17:23"
                }
            }
        ]
    }
}
```


