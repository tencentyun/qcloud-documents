## API Description
 This API (ModifyLoadBalancerAttributes) is used to modify basic configuration information of load balancer instances based on your input parameters.
 
Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
 The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/product/213/11650) page. The Action field for this API is ModifyLoadBalancerAttributes.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> Unique ID of the load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> loadBalancerName
<td> No
<td> String
<td> Name of the load balancer instance, which can contain 1-50 characters, including letters, numbers, "-" or "_".
<tr>
<td> domainPrefix
<td> No
<td> String
<td> Domain prefix. The domain name of a load balancer instance consists of the domain prefix entered by a user and the domain suffix in the configuration file to ensure the uniqueness.<br> The prefix should be a combination of 1-20 characters comprised of lowercase letters, numbers or "-".<br> This field is not applicable to private network-based load balancer instances.
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
<td> requestId
<td> Int
<td> Request task ID. The API is an asynchronous task.
<a href="https://cloud.tencent.com/document/api/214/4007">DescribeLoadBalancersTaskResult</a> is used to query the result of task execution.
</tbody></table>

 

## Example
 
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyLoadBalancerAttributes
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&loadBalancerName=my-lb-name
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

