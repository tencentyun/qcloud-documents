## 1. API Description
 DeleteLoadBalancerListeners is used to delete one or more listeners of cloud load balancer instances.
 
Domain for API access: lb.api.qcloud.com

## 2. Request Parameter
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DeleteLoadBalancerListeners.
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> The ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> listenerIds.n
<td> Yes
<td> String
<td> You can query the ID of the cloud load balancer listener to be deleted via the API<a href="http://www.qcloud.com/doc/api/244/%E8%8E%B7%E5%8F%96%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9B%91%E5%90%AC%E5%99%A8%E5%88%97%E8%A1%A8" title=" DescribeLoadBalancerListeners"> DescribeLoadBalancerListeners</a>.

</tbody></table>

 

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on Error Code page.
<tr>
<td> message
<td> String
<td>  Module error message description depending on API.
<tr>
<td> requestId
<td> int
<td> Request task ID. The API is a asynchronous task, and can be called based on this parameter
<a href="/doc/api/244/4007">DescribeLoadBalancersTaskResult</a> is used to query the result of task operation.
</tbody></table>

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DeleteLoadBalancerListeners
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalanceId=lb-abcdefgh
&listenerIds.1=lbl-name1
</pre>
Output
```
{
    "code" : 0,
    "message" : "",
    "requestId" : 1234
}
```


