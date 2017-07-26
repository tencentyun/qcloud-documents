## 1. API Description

This API (ModifyMetric) is used to modify a metric. Only unit or metricCname of the metric can be modified.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is ModifyMetric.


| Parameter Name        | Required   | Type     | Description                                       |
| ----------- | ---- | ------ | ---------------------------------------- |
| namespace   | Yes    | String | Namespace, which can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName  | Yes    | String | Metric name, which can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| metricCname | Yes     | String | Metric name                                    |
| unit        | No    | String | Display unit of the reported data                               |



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



## 5. Example

Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=ModifyMetric
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&metricCname='Machine disk utilization'
&unit='%'
</pre>
Output
```
{
    "code":"0",
    "message":""
}
```



