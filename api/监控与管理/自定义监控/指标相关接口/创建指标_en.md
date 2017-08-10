## 1. API Description

This API (CreateMetric) is used to create a metric under a namespace for data analysis.
For more information about the number of metrics and dimensions, please see <a href="https://www.qcloud.com/doc/product/397/4002">Product Limitation</a> page
When you use this API to create a metric, you can also add the statistical type under the metric. Add statistical type when you enter statisticsType.m.period and statisticsType.m.statistics.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
  The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateMetric.
​	
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td>Yes
<td> String
<td> Namespace, which can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace)
<tr>
<td> metricName
<td>Yes
<td> String
<td> Metric name, which is comprised of letters, numbers and underscores
<tr>
<td> metricCname
<td>Yes
<td> String
<td> Chinese name of the metric
<tr>
<td>  dimensionNames.n
<td>Yes
<td> Array
<td> Statistical dimension name of the metric
<tr>
<td> unit
<td>No
<td> String
<td> The unit used when user reports data. Default is empty string
<tr>
<td> statisticsType.m.period
<td>No
<td> Int
<td> Statistical period. The time interval for data collection. Currently, default is 300 seconds, which cannot be modified
<tr>
<td> statisticsType.m.statistics
<td>No
<td> String
<td> Analyze the data set within a specified statistical period. Available analytical methods are: max (to take the maximum value in the data set), min (to take the minimum value in the data set), sum (to take the sum of all data in the data set), avg (to take the average value of all data in the data set), last (to take the last value in the data set)
</tbody></table>



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
| -514 | Resource already exists    | OperationDenied.SourceAlreadyExists  |



## 5. Example

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&dimensionNames.1=diskname
&metricCname='Disk utilization'
&statisticsType.0.period=300
&statisticsType.0.statistics=max
</pre>

Output
```
{
  'code': 0,
  'message': ''
}
```


