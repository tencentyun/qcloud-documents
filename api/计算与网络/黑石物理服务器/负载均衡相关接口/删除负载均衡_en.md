## 1. API Description
This API (DeleteBmLoadBalancers) is used to delete one or more BM load balancer instances specified by the user.

Domain for API access: lb.api.qcloud.com
 
## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is DeleteBmLoadBalancers.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerIds.n
<td> Yes
<td> Array
<td> ID of BM load balancer instance, which can be queried via API <a href="/doc/api/456/6658" title="DescribeLoadBalancers">DescribeBmLoadBalancers</a>.
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
<a href="/doc/api/456/6666">You can query task operation result by calling API DescribeLoadBmBalancersTaskResult</a> based on this parameter.
</tbody></table>

Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |
| 12003 | IncorrectStatus.LBWrongStatus | The operation is impossible due to incorrect status of BM load balancer |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DeleteBmLoadBalancers
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerIds.0=lb-aaaa
&loadBalancerIds.1=lb-bbbb
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
