## 1. API Description
This API (CreateScheduledTask) is used to create a new scheduled task.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) Up to 10 scheduled tasks can be created in each scaling group.

2) If the scheduled task triggering execution of the scaling rule fails, it will automatically re-trigger during recurrence.

3) If multiple scheduled tasks trigger execution of a scaling rule of the same scaling group within a similar period of time, the earliest triggering scheduled task will perform the scaling activity first. Since there should be only one scaling activity under the same scaling group at the same time, the subsequent scheduled task will automatically retry the scheduled trigger during recurrence. Where after the completion of the previous scaling activity, the subsequent scheduled task is still retrying in recurrence, the scaling rule of the scheduled task is executed and the corresponding scaling activity is triggered.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is CreateScheduledTask.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID of the scheduled task to be created. It can be queried by calling <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup) API.
| scalingScheduledTaskName | Yes | String | Name defined by the user for the scheduled task to be created. | 
| readjustMaxSize | Yes | Int | Reset the maximum size of the scaling group when the scheduled task is triggered. | 
| readjustMinSize| Yes | Int | Reset the minimum size of the scaling group when the scheduled task is triggered.  | 
| startTime | Yes | datetime | Start time of the scheduled task.  | 
| endTime | No | datetime | End time for repeated execution of the scheduled task, which is required if the scheduled task needs to be repeated. | 
| recurrence | No | String | Repetition mode of the scheduled task, which is in the standard crontab format ```* * * * *```, where the asterisks denoting minute and hour cannot be specified (the first and the second asterisk). This parameter is required if the scheduled task needs to be executed repeatedly.|


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | It contains the list information of the scheduled tasks that were created successfully. |

Parameter data is composed of only one element: scalingScheduleTaskId.

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingScheduleTaskId | Array | It contains the ID of each scheduled task created.  |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

| Error Code | Description |
|----|--------|
| QuotaExceeded.ScheduledTask | Number of scheduled tasks allowed to be added has been exceeded |
| NameDuplicate.ScheduledTask | Scheduled task name already exists |
InvalidScheduleTask.TimeConflict | Time conflict between scheduled tasks |
| InvalidParameter.EndtimeAndRecurrence | endtime and recurrence must be passed at the same time |

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxxxx
&scalingScheduledTaskName=xxxxx
&readjustMaxSize=10
&readjustMinSize=1
&startTime=2016-03-16 12:00:00
&recurrence= * * 1 * *
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",    
    "data":{
        "scalingScheduleTaskId":[
            "xxxxxx"
        ]
    }
}
```


