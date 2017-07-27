## 1. API Description

This API (ModifyAlarmRule) is used to modify alarm rule. You can modify the comparison type, alarm threshold, number of consecutive periods, alarm receiving group ID of the rule.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is ModifyAlarmRule.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| alarmRuleId | Yes | String | Alarm rule ID, which can be queried by calling the API <a href="/doc/api/255/查询告警规则" title="Query Alarm Rule">Query Alarm Rule</a> (DescribeAlarmRuleList) |
| operatorType | No | String | Comparison type (operator), available values are >, < 、>=, <=, !=, ==. This indicates the comparison method of the alarm rule |
| threshold | No | Int | Alarm threshold | 
| constancy | No | Int | Number of consecutive periods. Currently, default period is 300 seconds |
| receiversId | No | Int | Alarm receiving group ID |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |


## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=ModifyAlarmRule
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&alarmRuleId=policy-eqzqq79naz
&receiversId=8888

</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


