## 1. API Description
This API (DeleteBmLoadBalancers) is used to delete one or more BM load balancer instances specified by the user.

Domain for API access: lb.api.qcloud.com
 
## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/document/product/386/6718). The Action field for this API is DeleteBmLoadBalancers.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> ID of load balancer instance, which can be queried via API <a href="/document/product/386/9304" title="DescribeLoadBalancers">DescribeBmLoadBalancers</a>.
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
<a href="/document/product/386/9308">You can query the task execution result based on this parameter by calling API DescribeLoadBmBalancersTaskResult</a>
</tbody></table>

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this load balancer does not exist in CCDB |
| 12003 | IncorrectStatus.LBWrongStatus | The operation is impossible due to incorrect status of the load balancer |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DeleteBmLoadBalancers
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-aaaa
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 2376363
}
```
