## 1. API Description
This API (DeleteScheduledTask) is used to delete a specific scheduled task.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DeleteScheduledTask.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID, indicating that the scheduled task to be deleted belongs to the scaling group. This parameter can be obtained by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| scalingScheduledTaskId | Yes | String | ID of scheduled task to be deleted. This parameter can be obtained by calling API <a href="/doc/api/372/查询定时任务" title="Query Scheduled Task">Query Scheduled Task</a>(DescribeScheduledTask). |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |

## 4. Error Codes
For common errors on this API, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).
## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxx
&scalingScheduleTaskId=xxxx
```
Example of returned result is as follows. The code is 0, indicating that the scheduled task has been deleted successfully.
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",  
    "data":[]    
}
```


