## 1. API Description
 This API (ModifyBmLoadBalancerAttributes) is used to modify the basic configuration information of BM load balancer instances based on your input parameters. Information that can be modified includes the name of load balancer instance and domain name prefix.

Domain name: lb.api.qcloud.com

## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/document/product/386/6718). The Action field for this API is ModifyBmLoadBalancerAttributes.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>

<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td>  ID of load balancer instance, which can be queried via API <a href="/document/product/386/9306" title="DescribeLoadBalancers">DescribeBmLoadBalancers</a>.

<tr>
<td> loadBalancerName
<td> No
<td> String
<td> Name of load balancer. The name should be a combination of 1-20 characters comprised of letters, numbers, "-" or "_".

<tr>
<td> domainPrefix
<td> No
<td> String
<td> Prefix of domain name. The domain name of load balancer consists of domain name prefix entered by user and the domain suffix in the configuration file to ensure its uniqueness. The prefix should be a combination of 1-20 characters comprised of lowercase letters, numbers or "-". This field is not applicable to private network-based load balancers.

</tbody></table>


## 3. Response Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Successful; other values: Failed. For more information, please see <a href="/document/product/386/6725" title="Common Error Codes">Common Error Codes</a> on Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> requestId
<td> Int
<td>Request task ID. The API is an asynchronous task.
<a href="/document/product/386/9308">You can query the task execution result based on this parameter by calling API DescribeBmLoadBalancersTaskResult</a>.
</tbody></table>

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyBmLoadBalancerAttributes
&<<a href="https://www.qcloud.com/document/product/386/6718">Common request parameters</a>>
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

