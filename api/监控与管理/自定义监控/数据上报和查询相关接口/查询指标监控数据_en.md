## 1. API Description

This API (GetMonitorData) is used to analyze the data you reported, and obtain the analysis result within each statistical period (300 seconds).
For example, if statistical type contains period": "300", "statistics": "max" under the metric, the API will obtain the maximum value within 5 minutes from the data you reported.
You can use this API to acquire multiple sets of data (between startTime and endTime) of the specified dimension under the metric.

Domain name: monitor.api.qcloud.com

For more information about how many days the data can be retained, please see <a href="https://www.qcloud.com/doc/product/397/4002">Product Limitation</a> page

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| namespace | Yes | String | Namespace. This can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName | Yes | String | Metric name. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| dimensions.n.name| Yes | Array | Array of dimension names. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric). Enter all the dimensions or part of the aggregated dimensions under the metric |
| dimensions.n.value | Yes | Array | Array of dimension values. This can be queried by calling the API <a href="/doc/api/255/查询指标对象列表" title="Query Metric Object List">Query Metric Object List</a> (DescribeObjects). Enter the dimension values corresponding to the dimension names |
| statistics  | Yes | String | Statistical method when an object exists. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| period | No | Int | Statistical granularity of monitoring data. Currently, you can only enter 300 |
| startTime | No | datetime | Start time. Format is Y-m-d H:M:S. If left empty, it will be 00:00:00 of the day by default |
| endTime | No | datetime | End time. If left empty, it will be the current time by default |



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |
| data | Array | Data information |

"data" should be the metricName and the statistical values of dimensions.

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
&startTime=2016-06-21 22:00:00
&endTime=2016-06-21 22:30:00
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "metricName": "diskusage",
    "startTime": "2016-06-21 22:00:00",
    "endTime": "2016-06-21 22:15:00",
    "period": "300",
    "dataPoints": {
        "diskname=sda&ip=172.31.58.160": [
            0.8,
            0.7,
            0.5,
            0.6
        ]
    }
}
```
Four data points in the output data are the maximum values obtained from four time periods: 21:55-22:00, 22:00-22:05, 22:05-22:10, 22:10-22:15.


