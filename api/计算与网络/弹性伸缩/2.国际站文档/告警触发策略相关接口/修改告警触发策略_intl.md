## 1. API Description
This API (ModifyScalingPolicy) is used to modify alarm trigger policies.
Domain for API request: <font style="color:red">scaling.api.qcloud.com</font>

1) When adjustmentType is TotalCapacity, it means adjusting the number of CVM instances in the current scaling group to the number specified by adjustmentValue. The value of adjustmentValue must be greater than or equal to 0.

2) When adjustmentType is QuantityChangeInCapacity or PercentChangeInCapacity, if the value of adjustmentValue is positive, it means increasing instances, and if negative, it means reducing instances.

3) When adjustmentType is PercentChangeInCapacity, adjustmentValue indicates the percentage of current instances.

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href="/doc/api/372/4153" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is ModifyScalingPolicy.

| Parameter Name | Required  | Type | Description | 
|---------|---------|---------|---------|
| scalingGroupId | Yes | String | ID of the scaling group for which the alarm trigger policy needs to be modified. It can be queried by calling API <a href="/doc/api/372/查询伸缩组列表" title="Query Scaling Group List">Query Scaling Group List</a> (DescribeScalingGroup). |
| scalingPolicyId | Yes | String | ID of the alarm trigger policy; ID of the alarm trigger policy to be modified in this case. This parameter can be queried by calling API <a href="/doc/api/372/查询告警触发策略" title="Query Alarm Trigger Policy">Query Alarm Trigger Policy</a> (DescribeScalingPolicy). |
| scalingPolicyName | No | String | Name of the alarm policy defined by users. |
| metric | No | String | Parameter metric stipulates the specific scaling policy in json format. <br>{"dimensionName":"cpu_usage","comparisonOperator":"Greater","threshold":50}<br>If the CPU utilization is greater than 50%, the scaling behavior will be triggered to increase or decrease corresponding CVMs. <a href="https://cloud.tencent.com/doc/product/377/%E5%BC%B9%E6%80%A7%E4%BC%B8%E7%BC%A9%E7%9B%B8%E5%85%B3%E9%97%AE%E9%A2%98#15.-.E5.91.8A.E8.AD.A6.E7.AD.96.E7.95.A5.E6.98.AF.E5.A6.82.E4.BD.95.E7.BB.9F.E8.AE.A1.E4.BA.91.E7.9B.91.E6.8E.A7.E4.BF.A1.E6.81.AF.E7.9A.84.EF.BC.9F" title="Detailed statistical rules">Click here to view detailed statistical rules</a> |
| adjustmentType | No | String | Adjustment method of the scaling rule. Only 3 values are available:<br>TotalCapacity: Adjusting the number of instances in the current scaling group to the specified number. <br>QuantityChangeInCapacity: Increasing or decreasing the instances by specified number. <br>PercentChangeInCapacity: Increasing or decreasing instances by specified percentage. |
| adjustmentValue | No | Int | Adjustment value for the scaling rule. If it is negative, it means decreasing instances.  The value ranges of adjustmentValue are as follows:<br>TotalCapacity: 0-30<br>QuantityChangeInCapacity: -30-30<br>PercentChangeInCapacity: -100-100.  |
| cooldown | No | Int | Cooldown period (in seconds), a period of time when the corresponding scaling group is locked after a scaling activity is completed. During this period, this scaling group cannot execute other scaling activities. |
| notifyIds.n | No | String | ID of the notification group, that is, the user group ID (groupID). The maximum number is 20, and the array subscript starts from 0. You can call API <a href="/doc/api/403/4404" title="Obtain User Group List">Obtain User Group List</a> (DescribeUserGroup) to query the parameter. |

Parameter metric stipulates the specific scaling policy in json format. Its parameters are as follows:

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| comparisonOperator | No | String | Comparison operator. Available values include:<br>Greater: Greater than<br>EqualOrGreater: Greater than or equal to<br>Less: Less than. <br>EqualOrLess: Less than or equal to. <br>Equal: Equal. <br>NotEqual: Not equal. | 
| dimensionName | No | String | Dimension. Available values include:<br>cpu_usage: CPU utilization. <br>mem_usage: Memory usage.  <br>lan_outtraffic: Outbound bandwidth of the private network. <br>lan_intraffic: Inbound bandwidth of the private network. |
| threshold | No | Int | Alarm threshold:<br>cpu_usage: value range [0, 100], unit: %<br>mem_usage: value range [0, 100], unit: %<br>lan_outtraffic: value range >0, unit: Bps<br>lan_intraffic: value range >0, unit: Bps |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="http://intl.cloud.tencent.com/document/product/377/8946" title="Common Error Codes">Common Error Codes</a> on the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code at business side. If the task succeeds, it will return "Success"; if the task fails, the specific business error reason will be returned. |

## 4. Error Codes
The following error codes only include the business logic error codes for this API. For additional common error codes, refer to [AS Error Code](http://intl.cloud.tencent.com/document/product/377/8946).

| Error Code | Description |
|----|------|
| InvalidParameter.MetricError | METRIC is configured incorrectly |
| InvalidParameter.ScalingPolicyAdjustmenttypeError | Incorrect type of scaling action |
| InvalidParameter.ScalingPolicyNameError | Wrong scaling policy name |
| InvalidParameter.AdjustmentValue | adjustmentValue of scaling policy is beyond the range |
| Conflict.ModifyDefaultScalingPolicyError | Default policy cannot be edited |

## 5. Example
```
https://scaling.api.qcloud.com/v2/index.php?
&<Common request parameters>
&scalingGroupId=xxxx
&scalingPolicyId=xxxx
&scalingPolicyName=xxxx
&adjustmentType=QuantityChangeInCapacity
&adjustmentValue=10
&cooldown=300
&metric={"dimensionName":"cpu_usage","comparisonOperator":"Greater","threshold":50}
&notifyIds.0=1832
&notifyIds.1=1833
```
Example of returned result is as below:
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success"   
}
```


