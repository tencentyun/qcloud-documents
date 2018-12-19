## API Description

This API (DescribeLoadBalancersTaskResult) is used to query the execution result of a task with request task ID as the input parameter for traditional and application-based load balancers.

Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeLoadBalancersTaskResult.
	 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> requestId
<td> Yes
<td> Int
<td> Request task ID, which is obtained from the returned value of asynchronous API.
</tbody></table>


## Response Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> codeDesc
<td> String
<td> Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned.
<tr>
<td> data
<td> Array
<td> Returned array
</tbody></table>

<b></th>"data" is composed as follows:</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> status
<td> Int
<td> Current task status.
0: Successful; 1: Failed; 2: In progress.
</tbody></table>


## Example
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancersTaskResult
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&requestId=6356081
</pre>
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "status": 0
    }
}
```

