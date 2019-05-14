## 1. API Description
This API (DescribeScalingPolicy) is used to query the alarm trigger policy.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeScalingConfiguration.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | ID of scaling group. In this case, it represents the scaling group in which the alarm trigger policy to be queried locates. This parameter can be obtained by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| scalingPolicyIds.n | No | String | An array of alarm trigger policy IDs to be queried. Array subscript starts from 0. |
| scalingPolicyName | No | String | Name of the alarm trigger policy to be queried. |
| offset | No | Int | Offset; default is 0.  |
| limit | No | Int | The maximum number of alarm trigger policies allowed to be queried at a time. Default is 20.  |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |
| message | String | Module error message description depending on API. |
| data | Array | Information on the list of alarm trigger policies returned for the query. |
| totalCount | Int | Number of alarm trigger policies returned for the query.  | 

Parameter data is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| scalingPolicyId | String | ID of alarm trigger policy returned for the query. | 
| scalingPolicyName | String | Name of alarm trigger policy returned for the query. | 
| adjustmentType | String | Adjustment method of scaling rules returned for the query. The possible values are: <br>QuantityChangeInCapacity: Increasing or decreasing the instances by specified number. <br>PercentChangeInCapacity: Increasing or decreasing instances by specified percentage. <br>TotalCapacity: Adjusting the number of instances in the current scaling group to the specified number. <br>UnhealthyInstance: Remove unhealthy instances (default policy cannot be modified or deleted). | 
| adjustmentValue | Int | Adjustment value for the scaling policy.  | 
| metric | Array | Scaling rule, the composition of which is shown in the table below.  |  
| notifyIdSet | Array | Notification group ID, or the user group ID (groupId), which indicates the user group where the user is located. | 
| createTime | String | Creation time of the alarm policy | 
| cooldown | Int | Cooldown time, a period of time when the corresponding scaling group is locked after a scaling activity is completed. During this period, this scaling group cannot execute other scaling activities. | 

metric represents the scaling rule and is composed of the following parameters:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dimensionName | String | Dimension. Available values include:<br>cpu_usage: CPU usage. <br>mem_usage: Memory usage.  <br>lan_outtraffic: Outbound bandwidth of the private network. <br>lan_intraffic: Inbound bandwidth of the private network. | 
| comparisonOperator | String | Comparison operator. Available values include:<br>Greater: Greater than<br>EqualOrGreater: Greater than or equal to<br>Less: Less than. <br>EqualOrLess: Less than or equal to. <br>Equal: Equal. <br>NotEqual: Not equal. | 
| threshold | Int | Alarm threshold: <br>cpu_usage: value range [0, 100], unit: %<br>mem_usage: value range [0, 100], unit: %<br>lan_outtraffic: value range >0, unit: Bps<br>lan_intraffic: value range >0, unit: Bps | 
## 4. Error Codes
For common errors on this API, refer to [AS Error Code](https://cloud.tencent.com/doc/api/372/4173).
## 5. Example
If a user wants to show that the scalingGroupId is the alarm trigger policy for asg-d4hmoms6, the request form may be as follows, where the instruction request parameter only sets the scalingGroupId.
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=asg-d4hmoms6
```
The following results will be returned:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",    
    "data":{
        "scalingPolicySet":[
           {
                "scalingPolicyId": "asp-168y1thp",
                "scalingPolicyName": "bono1d24",
                "adjustmentType": "QuantityChangeInCapacity",
                "adjustmentValue": 10,
                "metric": {
                    "dimensionName": "cpu_usage",
                    "comparisonOperator": "EqualOrGreater",
                    "threshold": 50
                },
                "notifyIdSet": [
                    "1832",
                    "1833"
                ],
                "createTime": "2016-03-21 14:07:42",
                "cooldown": 300
            },
        ],
        "totalCount":1
    }
}
```


