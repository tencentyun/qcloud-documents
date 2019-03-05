## 1. API Description
 DescribeLBHealthStatus is used to query the related parameters of default health check for cloud load balancer instances.
 
Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeLBHealthStatus.
	 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalanceId
<td>Yes
<td> String
<td> ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://cloud.tencent.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> listenerId
<td> No
<td> String
<td> ID of the cloud load balancer listener, which can be listenerId or unListenerId (recommended). You can query it via the API <a href="https://cloud.tencent.com/doc/api/244/%E8%8E%B7%E5%8F%96%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9B%91%E5%90%AC%E5%99%A8%E5%88%97%E8%A1%A8" title=" DescribeLoadBalancerListeners">DescribeLoadBalancerListeners</a>.
</tbody></table>
 

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> msg
<td> string
<td> Module error message description depending on API.
<tr>
<td> data
<td> array
<td> Returned array
</tbody></table>

**Data array structure:**

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> ip
<td> String
<td> Private IP of the CVM.
<tr>
<td> protocol
<td> String
<td> Protocol.
<tr>
<td> port
<td> Int
<td> CVM port.
<tr>
<td> vport
<td> Int
<td> Listening port of the cloud load balancer.
<tr>
<td> healthStatus
<td> Int
<td> Health check result. 1: healthy; 0: unhealthy.
</tbody></table>
 

## 4. Example

Input:
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLBHealthStatus
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalanceId=lb-abcdefgh
</pre>
Output:
```
{
"code":0,
"msg":"ok",
"data":[
	     {
			"ip":"10.2.3.0",
			"protocol":"TCP",
			"port":8001,
			"vport":8001,
			"healthStatus":0
	     }
	]
}
```


