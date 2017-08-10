## 1. API Description

This API (DescribeAlarmRuleObjects) is used to query information of the objects that are bound with the alarm rule using the alarm rule ID.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeAlarmRuleObjects.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| alarmRuleId | Yes | String | Rule ID, which can be queried by calling the API <a href="/doc/api/255/查询告警规则" title="Query Alarm Rule">Query Alarm Rule</a> (DescribeAlarmRuleList) |
| offset | No | Int | Offset. Default is 0 (i.e. query result is displayed from the first alarm rule) |
| limit | No | Int	 | Number of rows to be displayed in the result. Default is 30. Starting from offset, this number of alarm rules are displayed |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |
| data | Array | This field exists if there is additional returned information |


"data" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| ruleBindList | Array | List of objects that are bound with the alarm rule (each element in the array is the detailed description of an object. For more information, please see example) |
| total | Int | Number of objects bound with the alarm rule |




## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&alarmRuleId=policy-ou3kyu2f
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "ruleBindList": [
            {
                "diskname": "sda",
                "ip": "172.31.58.160"
            }
        ],
        "total": "1"
    }
}
```


