## 1. API Description
This API (DeleteScalingGroup) is used to delete a specific scaling group. You can delete the corresponding scaling group based on scalingGroupId.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) You can delete a scaling group only when the following two conditions are satisfied.
i. The scaling group is not performing a scaling activity.
ii. The number of CVM instances currently in the scaling group is 0.

2) The information on the associated scaling configuration, scaling rule, scaling activity and scaling request will be deleted when a scaling group is deleted.

3) When a scaling group is deleted, the following tasks or instances will not be deleted: scheduled task, cloud monitor alarm task and cloud load balancer instance.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DeleteScalingGroup.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | Scaling group ID. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |


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

## 5. Example

```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=xxxx
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"      
}
```


