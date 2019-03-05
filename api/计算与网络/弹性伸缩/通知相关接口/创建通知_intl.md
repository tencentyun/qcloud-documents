## 1. API Description
This API (CreateScalingNotification) is used to create notification.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) Each scaling group can create up to 20 notifications. For more information, refer to <a href="/doc/product/377/3120" title="Service Limits">Service Limits</a>.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is CreateScalingNotification.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID of the notification to be created. It can be queried by calling <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List </a>(DescribeScalingGroup) API. |
| notificationTypes.n | Yes | int | Notification types, which is a collection of notification types that need to be subscribed, ranging from 1 to 6. The specific mapping relationship is as follows: <br>1: Scale-up Succeeded<br>2: Scale-up Failed<br>3: Scale-down Succeeded<br>4: Scale-down Failed<br>5: Replacement of Unhealthy Sub-machines Succeeded<br>6: Replacement of Unhealthy Sub-machines Failed |
| receiversIds.n | Yes | String | ID of the notification group, that is, the collection of user group ID (groupID). The array subscript is started with 0. You can call API <a href="/doc/api/403/4404" title="Obtain User Group List">Obtain User Group List</a> (DescribeUserGroup) to query the parameter. |
## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | It contains the notification list information that was created successfully. |

Parameter data is composed of the following parameters, and contains only one element notificationId.

| Parameter Name | Type | Description |
|---------|---------|---------|
| notificationId | String | Notification ID.  |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

| Error Code | Description |
|----|------|
| InvalidParameter.ScallingGroupId | Cannot match to the corresponding scaling group ID |
| InvalidParameter.NotifyType | Invalid notification type number |


## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common Request Parameters>
&scalingGroupId=asg-xxxx
&notificationTypes.0=1
&notificationTypes.1=2
&receiversIds.0=1832
&receiversIds.1=1833
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"
    "data":{
        "notificationId":"asn-xxxxx"
    }
}
```
