
## 1. API Description
This API (ModifyScalingGroup) is used to modify the attributes of a specific scaling group.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) You can modify the corresponding scaling group attributes based on scalingGroupId. Only the following attributes can be modified:
 maxSize: The maximum group size, that is, the maximum number of the CVM instances in the scaling group
minSize: The minimum group size, that is, the minimum number of the CVM instances in the scaling group
removePolicy: Remove policy. It specifies whether to first remove the oldest or newest instance in the scaling group if necessary
scalingGroupName: Scaling group name
desiredCapacity: The desired instance number
scalingConfigurationId: Scaling configuration
Other attributes cannot be modified.

2) You can only call this API when the scaling group is in active or inactive status.

3) When the number of CVM instances in the scaling group does not satisfy the modified maxSize, minSize, desiredCapacity, CVM instances will be automatically added or removed by the auto scaling service to make the number of CVM instances in the scaling group between maxSize and minSize and equal to desiredCapacity.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is ModifyScalingGroup.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|------|
| scalingGroupId | Yes | String | Scaling group ID to be modified. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| minSize | Yes | Int | The minimum group size of the scaling group after modification, that is, the minimum number of CVM instances in the scaling group, with the range of 0-30, no greater than maxSize. When the number of CVM instances in the scaling group is less than minSize, AS will automatically add CVM instance to make the current instance number in the scaling group equal to minSize. |
| maxSize | Yes | Int | The maximum group size of the scaling group after modification, that is, the maximum number of CVM instances in the scaling group, with the range of 0-30, no less than minSize. When the number of CVM instances in the scaling group is larger than maxSize, AS will automatically remove CVM instance to make the current instance number in the scaling group equal to maxSize. |
| removePolicy | Yes | String | Remove policy for the scaling group. Only two values are available: RemoveOldestInstance means removing the oldest instance in the scaling group, that is, the oldest CVM instance in the scaling group will be first removed if necessary; RemoveNewestInstance means removing the newest instance in the scaling group, that is, the newest CVM instance in the scaling group will be first removed if necessary. |  
| scalingGroupName | No | String | Scaling group name defined by the user. If left empty, the name will be not modified. |
| scalingConfigurationId | No | String | The scaling configuration currently bound to the scaling group. After the modification, the margin sub-machine adopts the configuration before replacement, and the incremental sub-machine adopts the modified configuration. If left empty, the original scaling configuration will not be modified. |
| desiredCapacity | No | Int | The desired instance number. It refers to the number of currently reasonable instances in the scaling group with the value between the minimum and the maximum number of instances. Its value can be adjusted manually. When the timed task and alarm scaling task are triggered, it will also be adjusted. The scaling group will automatically adjust the actual number of instances to make it equal to the desired instance number. |


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
| Conflict.MaxsizeLessMinsize | maxsize must be greater than minsize |
| InvalidParameter.DesiredCapacity | Invalid desired instance number |

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&minSize=3
&maxSize=20
&scalingGroupId=xxx
&removePolicy=RemoveOldestInstance
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"         
}
```


