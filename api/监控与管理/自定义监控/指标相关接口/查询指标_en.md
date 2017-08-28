## 1. API Description

This API (DescribeMetric) is used to view the metrics created under a namespace.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is DescribeMetric.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td>Yes
<td> String
<td> Query the metrics under the namespace. This can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace)
<tr>
<td> metricName
<td>No
<td> String
<td> Filtering by metric name. Information of all the metrics under the namespace will be returned if this is left empty.
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
<tr>
<td> data
<td> Array
<td> Returned array
<tr>
</tbody></table>

Each metric returned by "data" is defined as follows:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td> String
<td> Namespace where the metric resides in
<tr>
<td> metricName
<td> String
<td> Metric name
<tr>
<td> metricCname
<td> String
<td> Chinese name of the metric
<tr>
<td> dimension
<td> String
<td> Metric dimension name
<tr>
<td> unit
<td> String
<td>Unit of the reported data
<tr>
<td> statisticsType
<td> Array
<td> Statistical type
<tr>
<td> aggeration
<td> Array
<td> Aggregation dimension. You can view aggregation information using API <a href="/doc/api/255/创建指标聚合" title="Create Metric Aggregation">Create Metric Aggregation</a>
</tbody></table>

"statisticsType" is composed as follows:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> period
<td> Int
<td> Statistical period. The time interval for data collection. Currently, default is 300 seconds, which cannot be modified
<tr>
<td> statistics
<td> String
<td> Statistical method function, which analyzes the data set within a specified statistical period. Available analytic methods are: max (to take the maximum value in the data set), min (to take the minimum value in the data set), sum (to take the sum of all data in the data set), avg (to take the average value of all data in the data set), last (to take the last value in the data set)
</tbody></table>

For the array of aggregation, key is the group of aggregated dimension names, and value is statistical type



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
 https://domain/v2/index.php?Action=DescribeMetric
 &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
 &namespace=cvm
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "cvm": {
            "diskusage": {
                "namespace": "cvm",
                "metricName": "diskusage",
                "unit": "'%'",
                "metricCname": ""Machine disk utilization"",
                "dimension": "diskname,ip",
                "statisticsType": [
                    {
                        "period": "300",
                        "statistics": "max"
                    },
                    {
                        "period": "300",
                        "statistics": "avg"
                    }
                ],
                "aggeration": {
                    "ip": [
                        {
                            "period": "300",
                            "statistics": "max"
                        }
                    ]
                }
            }
        }
    }
}
```


