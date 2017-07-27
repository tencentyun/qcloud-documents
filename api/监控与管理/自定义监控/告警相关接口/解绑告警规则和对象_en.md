## 1. API Description

This API (UnbindAlarmRuleObjects) is used to unbind alarm rule from object. Once unbound from the object, the alarm rule will no longer analyze the data reported by the object.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| alarmRuleId | Yes | String | Rule ID, which can be queried by calling the API <a href="/doc/api/255/查询告警规则" title="Query Alarm Rule">Query Alarm Rule</a> (DescribeAlarmRuleList) |
| dimensions.n.name | Yes | String | Key of the dimension group, which can be queried by calling the API <a href="/doc/api/255/查询告警规则绑定的对象" title="Query Objects Bound with Alarm Rule">Query Objects Bound with Alarm Rule</a> (DescribeAlarmRuleByObject) |
| dimensions.n.value | Yes | string |	Value of the dimension group, which can be queried by calling the API <a href="/doc/api/255/查询告警规则绑定的对象" title="Query Objects Bound with Alarm Rule">Query Objects Bound with Alarm Rule</a> (DescribeAlarmRuleByObject) |

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
&alarmRuleId = policy-f3h1bxvcsb 
&dimensions.0.name=diskname
&dimensions.1.name=ip
&dimensions.0.value=sda
&dimensions.1.value=172.31.58.160
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```


