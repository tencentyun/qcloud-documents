## 1. API Description
This API (AttachLifeCycleHookId) is used to bind a lifecycle hook ID to a scaling group ID and activate the currently bound lifecycle hook.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) A scaling group can only be bound to a lifecycle hook configuration.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is AttachLifeCycleHookId.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup) |
| lifeCycleHookId | Yes | String | Lifecycle hook ID. | 




## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. |
| data | Array | It is empty if returned successfully. |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

| Error Code | Description |
|----|------|
| Conflict.ScalingGroupIdVsLifeCycleHookId | This lifecycle hook does not exist in the scaling group |
| InvalidParameter.ScalingGroupIdError | Incorrect scalingGroupId |

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxxxx
&lifeCycleHookId=lfh-xxxxxx
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc": "Success",
    "data":[]
}
```


