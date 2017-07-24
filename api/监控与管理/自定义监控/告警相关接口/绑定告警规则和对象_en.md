## 1. API Description

This API (BindAlarmRuleObjects) is used to bind an alarm rule to objects. Once objects are bound with alarm rule, data reported by corresponding objects is analyzed according to the alarm rule, and alarm will be triggered when the trigger conditions of the alarm rule are met.
Objects refer to the entities whose statistics are being collected. For example, when disk utilization information is collected, the disk is the object, which is determined by the dimension names and values: dimensions.0.name=ip, dimensions.1.name=diskname,
dimensions.0.value=172.31.58.160, dimensions.1.value=sda.
An alarm rule can be bound to different objects. An object can also be bound with different alarm rules.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is BindAlarmRuleObjects.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| alarmRuleId | Yes | String | Alarm rule ID, which can be queried by calling the API <a href="/doc/api/255/查询告警规则" title="Query Alarm Rule">Query Alarm Rule</a> (DescribeAlarmRuleList) |
| dimensions.n.name | Yes | String | An array containing the names of the dimension groups, which can be queried by calling the API <a href="/doc/api/255/查询告警规则" title="Query Alarm Rule">Query Alarm Rule</a> (DescribeAlarmRuleList). Enter the fields that correspond to dimensionGroup in the returned values |
| dimensions.n.value | Yes | string | An array containing the values of the dimension groups, which is customized by the user. These values are the values of dimensions.n.name |



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |


## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&alarmRuleId = policy-ou3kyu2f 
&dimensions.0.name=ip
&dimensions.1.name=diskname
&dimensions.0.value=172.31.58.160
&dimensions.1.value=sda
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


