## API Description
 This API (ModifyLoadBalancerListener) is used to modify the attributes of load balancer listeners.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is ModifyLoadBalancerListener.
 
| Parameter Name | Required | Type | Description |
|-----|------|--------|-----------|
| loadBalancerId | Yes | String | ID of the load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of the load balancer listener, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1260" title=" DescribeLoadBalancerListeners">DescribeLoadBalancerListeners</a>. |
| listenerName | No | String | Listener name. |
| sessionExpire | No | Int | Session persistence duration. 0 means disabled. Value range: 30-3600. |
| healthSwitch | No | Int | Whether to enable health check: 1 (Enable) and 0 (Disable). |
| timeOut | No | Int | Response timeout. Value range: 2-60 seconds; <br>Response timeout of the public network-based load balancer listener with HTTP or HTTPS protocol cannot be set. |
| intervalTime | No | Int | Check interval. Value range: 5-300. Default is 5. |
| healthNum | No | Int | Healthy threshold. Value range: 2-10. |
| unhealthNum | No | Int | Unhealthy threshold. Value range: 2-10. |
| scheduler | No | String | Forwarding method of the load balancer listener. This value cannot be passed along with httpHash at the same time. This field is only supported for public network-based load balancers with TCP or UDP listeners. Available values: wrr (polling by weight),  least_conn (minimum number of connections). |
| httpHash | No | String | Forwarding method of the load balancer listener. This field is only supported for public network-based load balancers with HTTP or HTTPS listeners. Available values: wrr (polling by weight), ip_hash (hashing a value based on the source IP and forwarding the value to the backend server), least_conn <br>(minimum number of connections). Default is wrr. |
| httpCode | No | Int | This returned code is used to determine the health status of HTTP and HTTPS listeners. Value range: 1-31. Default is 31.<br> 1: It is considered healthy if the health check returns 1xx code; 2: It is considered healthy if the health check returns 2xx code; 4: It is considered healthy if the health check returns 3xx code; 8: It is considered healthy if the health check returns 4xx code; 16: It is considered healthy if the health check returns 5xx code. If there are multiple codes that can show the health status, enter the accumulated value corresponding to such codes. |
| httpCheckPath | No | String | Health check path for the public network-based load balancer listener with HTTP or HTTPS protocol. Default is /. It must start with /. |
| SSLMode | No | String | Verification mode of the public network-based load balancer listener with HTTPS protocol. unidirectional: Unidirectional verification; mutual: Mutual verification. |
| certId | No | String | New server certificate ID of HTTPS listener of public network-based load balancer. |
| certCaId | No | String | New client certificate ID of HTTPS listener of public network-based load balancer. |
| certCaContent | No | String | New client certificate content of HTTPS listener of public network-based load balancer. |
| certCaName | No | String | New client certificate name of HTTPS listener of public network-based load balancer. |
| certContent | No | String | New server certificate content of HTTPS listener of public network-based load balancer. |
| certKey | No | String | New server certificate key of HTTPS listener of public network-based load balancer. |
| certName | No | String | New server certificate name of HTTPS listener of public network-based load balancer. |


## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| requestId | Int | Request task ID. The operation status can be queried via the API [DescribeLoadBalancersTaskResult](https://cloud.tencent.com/document/api/214/4007). |

## Example
 
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyLoadBalancerListener
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
loadBalancerId=lb-ltkip4do
&listenerId=lbl-6hkiqc6c
&SSLMode=unidirectional
</pre>
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 18642
}

```


