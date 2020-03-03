## 1. API Description
This API (AttachInstance) is used to add a CVM instance to a specified scaling group.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) The added CVM instance needs to meet the following conditions:
The added CVM instance must be in the same region as the scaling group.
The specifications of the added CVM instances must be exactly the same as those of the instance bound scaling configuration.
The status of the added CVM instance must be "Running".
The added CVM instance can not be one already added to other scaling groups.

2) This function can be performed when the scaling group is in active status.

3) This function can only be performed when the scaling group is not performing a scaling activity.

4) This function can be performed directly without the cooldown period when the scaling group has no scaling activity being performed.

5) If the number of instances specified by this function plus the number of instances of the current scaling group is greater than the maximum group size specified by the scaling group, the call fails.

6) The manually added CVM instance is not associated with the scaling configuration in effect in scaling group.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is AttachInstance.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID of CVM instance to be bound. It can be queried by calling <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup) API. |
| instanceIds.n  | Yes | String | CVM instance ID to be bound. Please fill in the unInstanceId (unified ID of CVM) field returned in the API <a href="/doc/api/229/831" title="DescribeInstances ">Query Instance List (DescribeInstances)</a>, and a scaling group can bind up to 20 CVM instances. |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

| Error Code | Description |
|----|------|
| IncorrectInstanceStatus.InOtherScalingGroup | The CVM has been bound in other scaling groups |
| InvalidParameter.ScalingGroupIdError | Incorrect scalingGroupId |
| InvalidParameter.InstanceIdError | Incorrect instanceId |
| InvalidInstanceId.ScallingConfigurationMismatch | The bound CVM does not match the scaling group configuration |
| InvalidParameter.InvalidProjectId | The project ID to which the resource belongs is not the default project |


## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=xxx
&instanceIds.0=ins-xxxx
&instanceIds.1=ins-xxxx
```
Example of returned result is as follows. The code is 0, indicating that the bind is successfully.
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"   
}
```


