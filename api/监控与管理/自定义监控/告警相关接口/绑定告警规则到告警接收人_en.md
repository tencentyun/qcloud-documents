## 1. API Description

This API (BindAlarmRuleReceivers) is used to bind alarm rule to receiving group. For more information about how many receiving groups can be bound with an alarm rule, please see the <a href="https://www.qcloud.com/doc/product/397/4002">Product Limitation</a> page.
When data in the object that is bound with an alarm rule satisfies the alarm conditions, users in the receiving groups will receive the alarm information.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is BindAlarmRuleReceivers.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| alarmRuleId | Yes | String | Alarm rule ID, which can be queried by calling the API <a href="/doc/api/255/查询告警规则" title="Query Alarm Rule">Query Alarm Rule</a> |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |


## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=BindAlarmRuleReceivers
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&alarmRuleId=policy-eqzqq79naz
&receiversId=1001
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


