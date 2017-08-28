## 1. API Description

This API (GetMonitorRealtimeData) is used to obtain real-time monitoring data of the metric. The statistical result of the data you reported that is analyzed using specified statistical method within the most recent period (300 seconds) will be returned.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is GetMonitorRealtimeData.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| namespace | Yes | String | Namespace. This can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName | Yes | String | Metric name. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| dimensions.N.name | Yes  | String | Group of dimension names. You can call the API <a href="/doc/api/255/查询指标对象列表" title="Query Metric Object List">Query Metric Object List</a> (DescribeMetric) to query all the dimensions or part of the aggregated dimensions under the metric |
| dimensions.N.value | Yes  | String | Group of dimension values. You can call the API <a href="/doc/api/255/查询指标对象列表" title="Query Metric Object List">Query Metric Object List</a> (DescribeObjects) to query the dimension values corresponding to the dimension names |
| statistics | Yes | String | Statistical method. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric). Enter the statistical method of the metric |
| period	| Yes |	Int | Statistical period. Currently you can only enter 300 |



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |
| data | array | Specific information of object |

"data" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| dimensions.name&dimensions.value | String | The string comprised of dimension and its value with & in between |
| value | Int | Statistical result |
| updateTime | datetime | End time of data analysis |




## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&dimensions.0.name=ip
&dimensions.1.name=diskname
&dimensions.0.value=172.31.58.160
&dimensions.1.value=sda
&period=300
&statistics=max
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "diskname=sda&ip=172.31.58.160": {
            "value": 0.8,
            "updateTime": "2016-06-21 22:40:00"
        }
    }
}

```
Note: If the queried object exists, "data" field in the returned result is null.
In the returned result, 0.8 is the maximum value analyzed within the time period from 22:35 to 22:40.



