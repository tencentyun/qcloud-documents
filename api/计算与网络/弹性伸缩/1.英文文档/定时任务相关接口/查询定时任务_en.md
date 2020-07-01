## 1. API Description
This API (DescribeScheduledTask) is used to query the scheduled task information. You can specify the scaling group ID to query all the scheduled tasks under this group.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeScheduledTask.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID, which is used for querying scheduled tasks for this scaling group. This parameter can be obtained by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| scalingScheduledTaskIds.n | No | String | An array of scheduled task IDs to be queried. The array subscript starts from 0.  |
| scalingScheduledTaskName | No | String | The scheduled task name to be queried.  |
| offset | No | Int | Offset; default is 0.  |
| limit | No | Int | The maximum number of scheduled tasks allowed to be queried at a time. Default is 20. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | Output result, containing all the scheduled task list information returned for the query. |

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| totalCount | Int | Number of scheduled tasks returned for the query |  |
| scalingConfigurationSet | Array | Set of scheduled task information.  |

scalingScheduleTaskSet contains information about a number of scheduled tasks, and the information about each scheduled task is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingScheduledTaskId | String | Scheduled task ID returned for the query. | 
| scalingScheduledTaskName | String | Scheduled task name returned for the query. | 
| readjustMaxSize | Int | Reset the maximum size of the scaling group when the scheduled task is triggered. | 
| readjustMinSize | Int | Reset the minimum size of the scaling group when the scheduled task is triggered. | 
| startTime | String | Start time of the scheduled task | | 
| endTime | String | End time of the scheduled task | | 
| recurrence | String | The repeated crontab value of the scheduled task. | 
| createTime | String | Creation time of the scheduled task. | 
## 4. Error Codes
For common errors on this API, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=xxxx
```
Example of returned result is as follows. The totalCount is 1, indicating that there is only one scheduled task.
```
{
    "code":"0",
    "codeDesc":"Success",
    "message":"",
    "data":{
        "totalCount":1,
        "scalingScheduleTaskSet":[
            {
                "scalingScheduledTaskId":"xxxx",
                "scalingScheduledTaskName":"xxxx",
                "readjustMaxSize":"20",
                "readjustMinSize":"10",
                "startTime":"2016-03-17 12:00:00",
                "endTime":"2016-03-18 12:00:00",
                "recurrence":"* * * * 1",
                "createTime":"2016-03-14 18:05:03"
            },
        ]
    }
}
```


