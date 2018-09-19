## 1. API Description
This API (DetachInstance) is used to detach a CVM instance from a specified scaling group.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DetachInstance.

1) If the removed CVM instance is manually created by the user, the instance will not be stopped and released.

2) This function can be performed only when the scaling group is in active status.

3) This API can be called only when the scaling group is not performing a scaling activity.

4) This function can be performed directly without the cooldown period when the scaling group has no scaling activity being performed.

5) If the number of instances of the current scaling group minus the number of instances specified by this API is less than the minimum group size specified by the scaling group, the call fails.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | ID of the scaling group to be removed from the CVM instance. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| instanceIds.n  | Yes | String | ID of the CVM instance to be removed from the scaling group. Please fill in the instanceId (unified ID of CVM) field returned in API <a href="/doc/api/372/查询伸缩组绑定的云服务器" title="DescribeScalingInstance">Query CVM Bound to Scaling Group</a> (DescribeScalingInstance). |
| keepInstance | No | Int | Whether to keep the detached instance. Value range:<br><li>0: stop and release the detached instances.<br><li>1: keep the detached instances. <br><br>default value: 0|

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

| Error Code | Description |
|----|------|
| InvalidParameter.ScalingGroupIdError | Incorrect scalingGroupId |
| InvalidParameter.InstanceIdError | Incorrect instanceId |

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=xxx
&instanceIds.0=ins-xxxx
&instanceIds.1=ins-xxxx
```
Example of returned result is as follows. If the code is 0, it is unbound successfully.
```
{
    "code":"0",
    "message":"", 
    "codeDesc":"Success"   
}
```


