## API Description
 This API (DescribeLBHealthStatus) is used to query the related parameters of health check for load balancer instances.
 
Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeLBHealthStatus.
	 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> ID of the load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> listenerId
<td> No
<td> String
<td> ID of the load balancer listener, which can be queried via the API <a href="https://cloud.tencent.com/doc/api/244/%E8%8E%B7%E5%8F%96%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9B%91%E5%90%AC%E5%99%A8%E5%88%97%E8%A1%A8" title=" DescribeLoadBalancerListeners">DescribeLoadBalancerListeners</a>.
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
<td> Returned array.
</tbody></table>

**Data is composed as follows:**

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
<td> Listening port of the load balancer.
<tr>
<td> healthStatus
<td> Int
<td> Health check result. 1: healthy; 0: unhealthy.
</tbody></table>
 

## Example

Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLBHealthStatus
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
</pre>
Response
```
{
  "code":0,
  "message" : "",
  "codeDesc": "Success",
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

