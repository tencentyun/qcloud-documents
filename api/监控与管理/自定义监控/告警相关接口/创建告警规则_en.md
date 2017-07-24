## 1. API Description

This API (CreateAlarmRule) is used to create alarm rule.
Alarm is triggered when reported data meets the specified alarm condition.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateAlarmRule.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| namespace | Yes | String | Namespace, which can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName | Yes | String | Metric name, which can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| dimensionNames.n | 	Yes | Array | Group of dimension names. The names can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric). Enter all dimensions under the metric or part of the aggregated dimensions |
| period | Yes | Int | Statistical period, which can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric). Enter the periods of statistical types under the metric |
| statistics | Yes | String | Statistical method, which can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric). Enter the statistical method of the statistical types under the metric |
| operatorType | Yes | String | Operator. Available values are >, < 、>=, <=, !=, ==. This indicates the comparison method of the alarm rule |
| threshold | Yes | Float | Exception triggering threshold |
| constancy | Yes | Int | Number of periods for the exception to persist before alarm is triggered. The alarm is triggered if the exception persists for this number of periods |
| receiversId | No | string | Alarm receiving group ID. No receiving group will be bound with the alarm if this is left empty (in which case no one will receive the alarm). This can be queried by calling the API <a href="https://www.qcloud.com/document/api/378/4404" title="Obtain User Group List">Obtain User Group List</a> |
| isWild | No | Int | Whether the rule is wildcard rule. 1: Wildcard rule. 0: Non-wildcard rule (default) |

A wildcard rule applies to all objects in the metric name group and cannot be bound to specific objects.
In the input example, if isWild=1, all objects with the dimension name "dimensionNames.0=ip&dimensionNames.1=diskname" are automatically bound with this rule.


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message description. Null value indicates success |
| data | Array | This field exists if there is additional returned information |

"data" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| alarmRuleId | string | Alarm rule ID, which is used as an input parameter when you edit or delete an alarm rule | 



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

In the input example, if we expect the average disk utilization to stay above 80% for 4 periods (20 minutes), operatorType is ">", threshold is "80", and constancy is "4" (4 periods).

Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=CreateAlarmRule
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&dimensionNames.1=diskname
&operatorType=>
&threshold=80
&period=300
&statistics=max
&constancy=4
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "alarmRuleId":"policy-ou3kyu2f"
    }
}
```


