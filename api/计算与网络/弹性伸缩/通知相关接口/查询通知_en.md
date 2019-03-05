## 1. API Description
This API (ModifyScalingNotification) is used to modify notification configuration.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is ModifyScalingNotification.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID of the notification to be modified. It can be queried by calling <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List </a>(DescribeScalingGroup) API. |
| notificationId | Yes | String | ID of the notification to be modified. It can be queried by calling <a href="/doc/api/372/查询通知" title="Query Notification">Query Notification </a>(DescribeScalingNotification) API. |
| notificationTypes.n | No | String | An array of notification types, which is a collection of scaling activity notifications that need to be subscribed, ranging from 1 to 6. The specific mapping relationship is as follows: <br>1: Scale-up Succeeded<br>2: Scale-up Failed<br>3: Scale-down Succeeded<br>4: Scale-down Failed<br>5: Replacement of Unhealthy Sub-machines Succeeded<br>6: Replacement of Unhealthy Sub-machines Failed |
| receiversIds.n | No | String | ID of the notification group, that is, the user group ID (groupID). The array subscript is started with 0. You can call API <a href="/doc/api/403/4404" title="Obtain User Group List">Obtain User Group List</a> (DescribeUserGroup) to query the parameter. |
## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | It is empty if returned successfully. |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).

| Error Code | Description |
|----|------|
| InvalidParameter.ScallingGroupId | Cannot match to the corresponding scaling group ID |
| InvalidParameter.NotifyType | Invalid notification type number |
| InvalidParameter.NotifyPara | Notification parameter is empty |
| InvalidParameter.NotifyId | Cannot match to the corresponding notification ID |
| InvalidParameter.GroupId | Cannot match to the corresponding notification group ID |


## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common Request Parameters>
&scalingGroupId=xxxx
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
    "data":[]
}
```


