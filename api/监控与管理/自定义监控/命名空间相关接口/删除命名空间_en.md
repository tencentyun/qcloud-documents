## 1. API Description

This API (DeleteNamespace) is used to delete a custom namespace. A namespace with metrics cannot be deleted. Please delete the <a href="https://www.qcloud.com/document/api/397/4241">metrics before deleting the namespace.</a>

Domain name: monitor.api.qcloud.com
 

## 2. Input Parameters
  The following request parameter list only provides API request parameters. Common request parameters are also needed when this API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DeleteNamespace.
​	
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td> Yes
<td> String
<td> Namespace, which can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace)
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
https://monitor.api.qcloud.com/v2/index.php?Action=DeleteNamespace
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
</pre>

Output

```
{
  'code': 0,
  'message': ''
}
```



