## 1. API Description
 
This API (GetRedisTaskList) is used to query the task list of a CRS instance.
Domain name for API request: <font style='color:red'>redis.api.qcloud.com </font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href='https://cloud.tencent.com/document/product/213/6976' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetRedisTaskList.

| Parameter Name | Required | Type | Description |
|:---------|---------|---------|---------|
| limit | Yes | Int | Length of a page |
| offset | Yes | Int | Current page number. Default is 0.  For query APIs, a maximum number of returned records is generally set for a single query by default. To traverse all the resources, you need to use "limit" and "offset" for a paged query; For example, to query the 40 records between 110 and 149, you can set offset = 110 and limit = 40.  |
| redisId | No | String | Instance ID, which can be obtained from redisId in the returned values of API [DescribeRedis](/document/product/239/1384). Filtering tasks by instance ID is supported. |
| redisId | No | String | Instance name, which can be obtained from redisName in the returned values of API [DescribeRedis](/document/product/239/1384). Filtering tasks by instance name is supported.  |
| beginTime | No | String | Start time, such as: 2017-02-08 16:46:34.  Query the list of tasks submitted within the time period of [beginTime, endTime].  |
| endTime | No | String | End time, such as: 2017-02-08 19:09:26.  Query the list of tasks submitted within the time period of [beginTime, endTime].  |
| taskStatus | No | Array | Status (statuses) of one or more tasks (n represents the array subscript starting with 0).  Filtering tasks by task status is supported.  Task statuses are defined as follows:<br>0: To be executed;<br>1: Executing;<br>2: Succeeded;<br>3: Failed;<br>-1: Execution Error |
| taskType | No | Array | Type(s) of one or more tasks (n represents the array subscript starting with 0).  Filtering tasks by task type is supported.  Task types are defined as follows:<br>task_importRdb: Import Rdb;<br>task_exportBackup: Export backup;<br>task_restoreBackup: Restore an instance;<br>task_restoreStream: Roll back an instance (cluster instances can be rolled back to any time point within the last three days, but the data for the last 10 minutes cannot be rolled back);<br>task_backupInstance: Back up an instance;<br>task_cleanInstance: Clear an instance;<br>task_resizeInstance: Upgrade an instance |

## 3. Output Parameters

| Parameter Name | Type | Description |
|:---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Codes page. |
| message | String | Error message description. A null value indicates a success |
| codeDesc | String | Description of error code at business side. For a successful operation, "Success" will be returned. In case of an error, a message describing the reason for the error will be returned.  |
| totalCount | Int | Total number of tasks |
| data | Object | Details of task list |


Parameter data indicates the details of task list, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| data.redisTaskSet | Array | Array of task details |

Parameter redisTaskSet indicates the array of task details, and is composed as follows:

| Parameter Name | Type | Description |
|:---------|---------|---------|
| startTime | String | Submission time of the task, such as: 2017-02-10 16:56:18 |
| taskName | String | Task name:<br>newInstance: Create an instance;<br>resizeInstance: Upgrade an instance;<br>closeInstance: Isolate an instance;<br>cleanInstance: Clear an instance;<br>startInstance: Dis-isolate an instance;<br>deleteInstance: Delete an instance;<br>setPassword: Set password for an instance;<br>importRdb: Import Rdb;<br>exportBackup: Export backup;<br>restoreBackup: Restore an instance;<br>restoreStream: Roll back an instance (cluster instances can be rolled back to any time point within the last three days, but the data for the last 10 minutes cannot be rolled back);<br>backupInstance: Back up an instance |
| redisName | String | Instance name |
| redisId | String | Instance ID |
| projectId | Int | ID of project to which the instance belongs |
| status | Int | Task status. 0: To be executed; 1: Executing; 2: Succeeded; 3: Failed; -1: Execution Error |
| progress | Int | Task execution progress. 0: Uncompleted; 1: Completed |

## 4. Error Codes
The following error codes include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 11201 | InvalidParameter | Incorrect business parameter |

## 5. Example
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=GetRedisTaskList
&<<a href="https://cloud.tencent.com/doc/api/229/6976">common request parameters</a>>
&limit=10
&offset=0
&beginTime=2016-12-28 00:03:52
&endTime=2017-02-11 00:03:52
&redisId=crs-izbob1wh
&redisName=for API test&taskStatus.0=2
&taskType.0=task_restoreBackup
&taskType.1=task_backupInstance
&taskType.2=task_cleanInstance
</pre>
The returned results are as below:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 9,
    "data": {
        "redisTaskSet": [
            {
                "startTime": "2017-02-10 16:56:18",
                "taskName": "restoreBackup",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-10 15:02:36",
                "taskName": "backupInstance",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-10 14:59:29",
                "taskName": "backupInstance",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-09 19:00:24",
                "taskName": "backupInstance",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 19:09:26",
                "taskName": "backupInstance",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 17:21:32",
                "taskName": "restoreBackup",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 16:46:34",
                "taskName": "backupInstance",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 15:38:16",
                "taskName": "cleanInstance",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            },
            {
                "startTime": "2017-02-08 15:35:25",
                "taskName": "backupInstance",
                "redisName": "for API test",
                "redisId": "crs-izbob1wh",
                "projectId": 0,
                "status": 2,
                "progress": 1
            }
        ]
    }
}

```
