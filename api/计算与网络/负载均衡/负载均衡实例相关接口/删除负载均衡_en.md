## 1. API Description
 API DeleteLoadBalancers is used to delete one or more cloud load balancer instances specified by users.
Domain for API access: lb.api.qcloud.com

 
## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DeleteLoadBalancers.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerIds.n
<td> Yes
<td> String
<td>  Uniform ID of cloud load balancer instance, i.e. unLoadBalancerId. It can be queried through API <a href="/doc/api/244/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
</tbody></table>

 

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> requestId
<td> Int
<td>Request task ID. The API is an asynchronous task, and can be called based on this parameter
<a href="/doc/api/244/4007">DescribeLoadBalancersTaskResult</a> is used to query the result of task execution.
</tbody></table>

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DeleteLoadBalancers
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerIds.1=lb-abcdefgh
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "requestId": 6356502
}
```

