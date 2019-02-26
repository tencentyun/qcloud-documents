## 1. API Description
This API (DeleteScalingPolicy) is used to delete alarm trigger policies according to the user's input.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DeleteScalingGroup.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | ID of scaling group. In this case, it represents the scaling group in which the alarm policy to be deleted locates. This parameter can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| scalingPolicyId | Yes | String | ID of the alarm trigger policy; ID of the alarm trigger policy to be deleted in this case. This parameter can be queried by calling API <a href="/doc/api/372/查询告警触发策略" title="Query Alarm Trigger Policy">Query Alarm Trigger Policy</a> (DescribeScalingPolicy). |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |

## 4. Error Codes

| Error | Error Code |
|----|------|
| Default policy cannot be deleted | Conflict.DeleteDefaultScalingPolicyError|

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-93a83x8x
&scalingPolicyId=sp-iir70sxv
```
Example of returned result is as follows. The code is 0, indicating that the alarm trigger policy has been deleted successfully.
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data":[]
}
```


