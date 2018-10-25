## 1. API Description
 API DeleteLoadBalancers is used to delete one or more cloud load balancer instances specified by users.
Domain for API access: lb.api.qcloud.com

 
## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DeleteLoadBalancers.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerIds.n
<td> Yes
<td> String
<td>  Uniform ID of cloud load balancer instance, i.e. unLoadBalancerId. It can be queried through API <a href="/doc/api/244/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
</tbody></table>

 

## 3. Response Parameters
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| requestId | Int | Request task ID. The operation status can be queried through API [DescribeLoadBalancersTaskResult](/doc/api/244/4007). |


## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DeleteLoadBalancers
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerIds.0=lb-abcdefgh
</pre>
Output
```
{
    "code": 0,
    "message": "",
	"codeDesc": "Success",
    "requestId": 6356502
}
```

