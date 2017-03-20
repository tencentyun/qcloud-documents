## 1. API Description
 RegisterInstancesWithLoadBalancer API is used to bind one or more CVMs to cloud load balancer instance.
 
Domain for API access: lb.api.qcloud.com


## 2. Request Parameters
 
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is RegisterInstancesWithLoadBalancer.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td>  ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> backends.n.instanceId
<td> Yes
<td> String
<td> Unique ID of the CVM. You can acquire this from the unInstanceId field in the returned content of <a href="http://www.qcloud.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a> API.<br> You may enter instance IDs of multiple hosts. For example, if you wish to enter two hosts, enter: backends.1.instanceId&backends.2.instanceId.
<tr>
<td> backends.n.weight
<td> No
<td> Int
<td> Weight of the CVM. Value range is 0-100, default is 10.
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
<td> Request task ID. The API is an asynchronous task, and can be called based on this parameter
<a href="/doc/api/244/4007">API DescribeLoadBalancersTaskResult</a> is used to query the result of task operation.
</tbody></table>

 

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&backends.1.instanceId=ins-1234test
&backends.1.weight=10
&backends.2.instanceId=ins-5678test
&backends.2.weight=6
</pre>
Output
```
{
  "code" : 0,
  "message" : "",
  "requestId" : 1234
}
```


