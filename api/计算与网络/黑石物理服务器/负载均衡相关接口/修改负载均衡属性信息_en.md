## 1. API Description
 This API (ModifyBmLoadBalancerAttributes) is used to modify the basic configuration information of BM load balancer instances based on your input parameters. Information that can be modified includes the name of BM load balancer instance and domain prefix.

Domain: lb.api.qcloud.com

## 2. Request Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is ModifyBmLoadBalancerAttributes.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>

<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> ID of BM load balancer instance, which can be queried via API <a href="/doc/api/456/6658" title="DescribeLoadBalancers">DescribeBmLoadBalancers</a>.

<tr>
<td> loadBalancerName
<td> No
<td> String
<td> Name of BM load balancer. The name can contain 1-20 characters, including letters, numbers, "-" or "_".

<tr>
<td> domainPrefix
<td> No
<td> String
<td> Domain prefix. The domain name of BM load balancer consists of domain prefix entered by user and the domain suffix in the configuration file, to ensure its uniqueness. The prefix can contain 1-20 characters, including letters (in lowercase), numbers or "-". This field is not applicable to private network-based BM load balancers.

</tbody></table>


## 3. Response Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> requestId
<td> Int
<td>Request task ID. The API is an asynchronous task.
<a href="/doc/api/456/6666">You can query task operation result by calling API DescribeBmLoadBalancersTaskResult</a> based on this parameter.
</tbody></table>

Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyBmLoadBalancerAttributes
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-aaaa
&loadBalancerName=my-test
&domainPrefix=aaaa
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 2376362
}
```

