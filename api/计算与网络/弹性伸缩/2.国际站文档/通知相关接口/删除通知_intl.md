## 1. API Description
This API (DeleteScalingNotification) is used to delete notification.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DeleteScalingNotification.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID of the notification to be deleted. It can be queried by calling <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List </a>(DescribeScalingGroup) API. |
| notificationIds.n | Yes | String | Notification ID, which is a collection of notification IDs that need to be deleted |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | It is empty if returned successfully. |


## 4. Error Codes
For common errors on this API, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-xxxx
&notificationIds.0=asn-xxx
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"
    "data":[]
}
```
