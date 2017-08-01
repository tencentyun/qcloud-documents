## 1. API Description

This API (DescribeAlarmRuleList) is used to query the list of created alarm rules.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeAlarmRuleList.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| namespace | Yes | String | Namespace. This can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName | No | string	| Metric name. All rules under the namespace will be returned if this is left empty. Metric names can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| offset | No | Int | Offset. Default is 0 (i.e. query result is displayed from the first alarm rule) |
| rows | No | Int | Number of rows to be displayed in the result. Default is 30. Starting from offset, this number of alarm rules are displayed |



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |
| data | Array | This field exists if there is additional returned information |

"data" field contains:

| Parameter Name | Type | Description |
|---------|---------|---------|
| ruleList | Array | Details of the alarm rules |
| total | Int | Number of rules |

"ruleList" field contains:

| Parameter Name | Type | Description |
|---------|---------|---------|
| alarmRuleId | String | Alarm rule ID |
| namespace | String | Namespace in which the alarm rule resides |
| metricName | String | Name of the metric in which the alarm rule resides |
| dimensionGroup | String | Group of dimension names |
| operatorType | String | Operator |
| threshold | Int | Threshold |
| constancy | Int | Number of periods for the alarm to persist |
| period | Int | Statistical period (in sec) |
| statistics | String | Statistical method of the alarm rule, which determines how the statistics within specified statistical period shall be taken from a data set. Available analytical methods are: max (to take the maximum value in the data set), min (to take the minimum value in the data set), sum (to take the sum of all data in the data set), avg (to take the average value of all data in the data set), last (to take the last value in the data set) |
| isWild | Int | Whether the rule is a wildcard rule. A wildcard rule applies to all the objects in the metric name group and cannot be bound to specific objects |
| receiversId | Int | Receiving group ID for the alarm. "0" means no receiving group is bound with the alarm rule |

## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=DescribeAlarmRuleList
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "ruleList": [
            {
                "alarmRuleId": "policy-ou3kyu2f",
                "namespace": "cvm",
                "metricName": "diskusage",
                "dimensionGroup": "diskname,ip",
                "operatorType": ">=",
                "threshold": "100",
                "constancy": "4",
                "period": "300",
                "statistics": "max",
                "isWild": "0",
                "receiversId": "0"
            }
        ],
        "total": "1"
    }
}
```


