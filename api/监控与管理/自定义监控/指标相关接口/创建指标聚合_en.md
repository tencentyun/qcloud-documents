## 1. API Description

This API (CreateMetricAggeration) is used to add metric aggregation. To aggregate the specified dimensions under the metric to achieve features that can collect or query information of a certain group of dimensions under the metric.
For example: The metric diskusage has the dimension dimensionNames.0=ip  dimensionNames.1=diskname
You can specify dimension IP only when you aggregate the dimension dimensionNames.0=ip and call the API "Add Statistical Type". Here, the disk utilization is calculated using machine IP dimension.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
| Parameter Name                        | Required   | Type     | Description                                       |
| --------------------------- | ---- | ------ | ---------------------------------------- |
| namespace                   | Yes    | String | Namespace, which can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName                  | Yes    | String | Metric name, which can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| dimensionNames.n            | Yes    | String | Name of dimension to be aggregated. It can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| statisticsType.m.period     | No    | Int    | Statistical period. Currently you can only enter 300 seconds                           |
| statisticsType.m.statistics | No    | String | Statistical type added for the aggregation dimension, such as max, min, last, sum, avg, etc     |


Add statistical types for all dimensions under the aggregation when you enter statisticsType.m.statistics and statisticsType.m.period



## 3. Output Parameters

| Parameter Name    | Type     | Description                         |
| ------- | ------ | -------------------------- |
| code    | Int    | Error code, 0:  Successful; other values: Failed. For more information, please see Error Codes |
| message | String | Error message                       |



## 4. Error Codes
| Error Code | Error Description    | Error Message                                 |
| ---- | ------- | ------------------------------------ |
| -503 | Incorrect request parameter  | InvalidParameter                     |
| -505 | Parameter is missing    | InvalidParameter.MissingParameter    |
| -507 | Limit has been exceeded    | OperationDenied.ExceedLimit          |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |
| -514 | Resource already exists    | OperationDenied.SourceAlreadyExists  |



## 5. Example

Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetricAggeration
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&statisticsType.0.period=300
&statisticsType.0.statistics=max
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```
