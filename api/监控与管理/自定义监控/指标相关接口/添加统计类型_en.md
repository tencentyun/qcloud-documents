## 1. API Description


This API (CreateMetricStatisticsType) is used to add statistical types for a specified dimension under a metric. A metric may have multiple statistical types.
A metric must have a statistical type, so the analysis result of the reported data can be queried.
You can skip this API if you have entered the information of statistical types when you <a href="/doc/api/255/创建指标" title="Create Metric">Create Metric</a> or <a href="/doc/api/255/创建指标聚合" title="Create Metric Aggregation">Create Metric Aggregation</a>.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters

 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateMetricStatisticsType.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td>Yes
<td> String
<td> Add the statistical types for the metrics under the namespace. This can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace)
<tr>
<td> metricName
<td>Yes
<td> String
<td> Add statistical types for the metric. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric)
<tr>
<td> dimensionNames.n
<td> Yes
<td> Array
<td> Group of all the dimensions or group of aggregated dimensions under the metric. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric)
<tr>
<td> statisticsType.m.period
<td> Yes
<td> Int
<td> Statistical period (in sec). Currently, you must enter 300 seconds, and other values are not supported
<tr>
<td> statisticsType.m.statistics
<td> Yes
<td> String
<td>  Statistical type, including max, min, last, sum, avg, etc.
</tbody></table>

The subscript n in dimensionNames.n is the subscript of the dimension under the metric.
You can enter the original dimensions of the metric (i.e. all the dimensions under the metric) or aggregated dimensions under the metric

statisticsType.m.statistics and statisticsType.m.period always come in pairs. You can add multiple groups of statistical types for the dimension of the metric.
The subscript m is the digit subscript of different statistical types
For example:    statisticsType.0.statistics=max  statisticsType.0.period=300
             statisticsType.1.statistics=min  statisticsType.1.period=300
This means to take the maximum and minimum values of the reported data within the statistical period (5 minutes).					
​							

## 3. Output Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code, 0:  Successful; other values: Failed. For more information, please see Error Codes
<tr>
<td> message
<td> String
<td> Error message
</tbody></table>



## 4. Error Codes

| Error Code | Error Description    | Error Message                                 |
| ---- | ------- | ------------------------------------ |
| -503 | Incorrect request parameter  | InvalidParameter                     |
| -505 | Parameter is missing    | InvalidParameter.MissingParameter    |
| -507 | Limit has been exceeded    | OperationDenied.ExceedLimit          |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |



## 5. Example

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&dimensionNames.1=diskname
&statisticsType.0.period=300
&statisticsType.0.statistics=avg
</pre>

Output
```
{
  'code': 0,
  'message': ''
}
```


