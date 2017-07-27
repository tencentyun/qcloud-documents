## 1. API Description

Namespace is a container of metrics. Metrics in different namespaces are independent from each other. So the metrics from different applications will not be mistakenly aggregated into the same statistical information. CCM allows you to customize namespace and store data across multiple regions. For example, proc_monitor, i.e. monitoring A process in Guangzhou region. This API provides capacity to create a custom namespace.

This API (CreateNamespace) is used to create a custom namespace.
For more information on how many namespaces a user can create, please see <a href="https://www.qcloud.com/doc/product/397/4002">Product Limitation</a> page. 

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is CreateNamespace.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td> Yes
<td> String
<td>Namespace: It contains 32 characters, including letters, numbers and underscores.
</tbody></table>

 

## 3. Output Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page
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
https://monitor.api.qcloud.com/v2/index.php?Action=CreateNamespace
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
​	
</pre>

Output

```
{
  'code': 0,
  'message': ''
}·
```

