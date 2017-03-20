## 1. API Description
 API ModifyLoadBalancerAttributes is used to modify basic configuration information of load balancer instances based on your input parameters. You can modify such information as the name of load balancer instance, domain prefix, and session persistence feature. Currently, the session persistence attribute belongs to listener, so any modification to this attribute will overwrite the session persistence attributes of all the listeners.
 
Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is ModifyLoadBalancerAttributes.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> The unique ID of cloud load balancer instance. This can be loadBalancerId or unLoadBalancerId (the latter is recommended). You can query it through API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> loadBalancerName
<td> No
<td> String
<td> The name of cloud load balancer instance. The name can contain 1-20 characters, including English letters, Chinese characters, numbers, "-" or "_".
<tr>
<td> domainPrefix
<td> No
<td> String
<td> Domain prefix. The domain name of cloud load balancer instance consists of domain prefix entered by user and the domain suffix in configuration file to ensure the uniqueness. <br>Naming rule: 1-20 characters, including English letters (in lowercase), numbers or "-" <br>This field is not applicable to the cloud load balancer instances of private network.
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
https://lb.api.qcloud.com/v2/index.php?Action=ModifyLoadBalancerAttributes
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&loadBalancerName=my-lb-name
</pre>
Output
```
{
    "code" : 0,
    "message" : "",
    "requestId" : 1234
}
```


