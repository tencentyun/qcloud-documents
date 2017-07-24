## 1. API Description

This API (DescribeAlarmRuleByObject) is used to query alarm rules bound to the specified object.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| namespace | Yes | string | Namespace, which can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName | Yes | String | Metric name. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| dimensions.n.name | Yes | array | Key of the dimension group. This can be queried by calling the API <a href="/doc/api/255/查询指标对象列表" title="Query Metric Object List">Query Metric Object List</a> (DescribeObjects) |
| dimensions.n.value | Yes | array | Value of the dimension group. This can be queried by calling the API <a href="/doc/api/255/查询指标对象列表" title="Query Metric Object List">Query Metric Object List</a> (DescribeObjects) |
| offset | No | int | Offset. Default is 0 (i.e. query result is displayed from the first alarm rule) |
| limit	 | No | int | Number of rows to be displayed in the result. Default is 30. Starting from offset, this number of alarm rules are displayed |

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |
| data | Array | Returned Result |

"data" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| ruleList | Array | List of objects bound with the alarm rule | 
| total | Int | Number of returned ruleLists |

"ruleList" contains:

| Parameter Name | Type | Description |
|---------|---------|---------|
| alarmRuleId | String | Alarm rule ID |
| namespace | String | Namespace |
| metricName | String | Metric name |
| dimensionGroup | String | Dimension group name |
| operatorType | String | Operator | 
| threshold | Int | Exception triggering threshold |
| constancy | Int | Number of periods for the exception to persist before alarm is triggered | 
| period | Int | Statistical period. Currently you can only enter "300s" |
| statistics | String | Statistical method. Available values are: sum, last, avg, min, max |
| receiversId | String | Alarm receiving group ID |

## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&dimensions.0.name=ip
&dimensions.0.value=172.31.58.160
&dimensions.1.name=diskname
&dimensions.1.value=sda
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


