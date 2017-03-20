## 1. API Description

API DescribeLoadBalancersTaskResult is used to query the result of a request task with the task's ID as an input parameter. You can judge the execution status of the asynchronous API based on returned result.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeLoadBalancersTaskResult.
	 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> requestId
<td> Yes
<td> Int
<td> ID of request task. This is provided by specific asynchronous operation API.
</tbody></table>


## 3. Response Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> msg
<td> string
<td> Module error message description depending on API.
<tr>
<td> data
<td> array
<td> Returned array
</tbody></table>

<b></th>Data structure:</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> status
<td> Int
<td> Current status of task.
0: Succeeded; 1: Failed; 2: In progress.
</tbody></table>


## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancersTaskResult
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&requestId=6356081
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "status": 0
    }
}
```
