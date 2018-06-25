## 1. API Description
This API (ModifyScheduledTask) is used to modify scheduled tasks.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is ModifyScheduledTask.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingScheduledTaskId | Yes | String | ID of scheduled task to be modified. This parameter can be obtained by calling API <a href="/doc/api/372/查询定时任务" title="Query Scheduled Task">Query Scheduled Task</a>(DescribeScheduledTask). |
| scalingScheduledTaskName | No | String | Name of scheduled task to be modified. This parameter can be obtained by calling API <a href="/doc/api/372/查询定时任务" title="Query Scheduled Task">Query Scheduled Task</a>(DescribeScheduledTask). |
| readjustMaxSize | No | Int | Reset the maximum size of the scaling group when the scheduled task is triggered. |
| readjustMinSize | No | Int | Reset the minimum size of the scaling group when the scheduled task is triggered.  |
| startTime | No | datetime | Start time of the scheduled task.  |
| endTime | No | datetime | End time for repeated execution of the scheduled task, which is required if the scheduled task needs to be repeated. If you need to close repeated execution, enter 0000-00-00 00: 00: 00 | 
| recurrence | No | String | Repetition mode of the scheduled task, which is in the standard crontab format ```* * * * *```, where the asterisks denoting minute and hour cannot be specified (the first and the second asterisk). This parameter is required if the scheduled task needs to be executed repeatedly. If you need to close repeated execution, enter ```* * * * *```. |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

| Error Code | Description |
|----|--------|
| NameDuplicate.ScheduledTask | Scheduled task name already exists |
InvalidScheduleTask.TimeConflict | Time conflict between scheduled tasks |
| InvalidScheduledTask.NotExist | The scheduled task does not exist |
## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxxx
&scalingScheduledTaskId=xxxxx
&recurrence=* * * * * 1
```
Example of returned result is as follows. The code is 0, indicating that the scheduled task has been modified successfully.
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[]    
}
```
