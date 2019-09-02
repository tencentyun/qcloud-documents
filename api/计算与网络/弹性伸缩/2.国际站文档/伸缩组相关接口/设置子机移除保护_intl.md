
## 1. API Description
This API (SetCvmProtectedDetach) is used to set the sub-machine removal protection.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

When the submachine is protected from removal, it will not be scaled down when replacement of unhealthy sub-machines, alarm policy and expected change trigger the scale-down.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is ModifyScalingGroup.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|------|
| scalingGroupId | Yes | String | ID of the scaling group of the submachine to be protected from removal. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| instanceIds.n | Yes | String | An array containing the IDs of submachine to be protected from removal. Array subscript starts from 0. |
| protectedFromDetach | Yes | Int | Flag bit of removal protection, 1: to set sub-machine removal protection; 0: to cancel sub-machine removal protection. |



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
| InvalidParameter.ScalingGroupIdError | Incorrect scalingGroupId |
| InvalidParameter.ProtectedFromDetach | Error in setting flag bit of removal protection. 0: to cancel removal protection; 1: to set removal protection |
| InvalidParameter.InstanceIdError | Invalid submachine ID |

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxx
&instanceIds.0=ins-xxx
&protectedFromDetach=1
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"         
}
```


