## API Description
This API (ModifyLoadBalancerBackends) is used to modify the weight of CVMs bound to a load balancer instance. You can adjust request forwarding rules by modifying weight of CVMs. For more information on weight configuration, please see [Weight Configuration](https://cloud.tencent.com/document/product/214/527#1.3.-.E5.90.8E.E7.AB.AF.E6.9C.8D.E5.8A.A1.E5.99.A8.E6.9D.83.E9.87.8D.E9.85.8D.E7.BD.AE).
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is ModifyLoadBalancerBackends.
	 
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
<td> backends.n.instanceId
<td> Yes
<td> String
<td> Unique ID of the CVM, which can be obtained from "unInstanceId" in the returned fields of API <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a>. <br>This API allows entering instance IDs of multiple CVMs at a time. For example, if you want to enter two CVMs, enter: backends.0.instanceId&backends.1.instanceId.
<tr>
<td> backends.n.weight
<td> Yes
<td> Int
<td> Weight of the bound CVM. Value range is 0-100. Default is 10.
</tbody></table>

 

## Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> codeDesc
<td> String
<td> Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned.
<tr>
<td> requestId
<td> Int
<td> Request task ID. The API is an asynchronous task. 
<a href="https://cloud.tencent.com/document/api/214/4007">DescribeLoadBalancersTaskResult</a> is used to query the result of task execution.
</tbody></table>

 

## Example
 
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyLoadBalancerBackends
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&backends.0.instanceId=ins-6789test
&backends.0.weight=10
&backends.1.instanceId=ins-1234test
&backends.1.weight=6
</pre>
Response
```

{
  "code" : 0,
  "message" : "",
  "codeDesc": "Success",
  "requestId" : 1234
}

```


