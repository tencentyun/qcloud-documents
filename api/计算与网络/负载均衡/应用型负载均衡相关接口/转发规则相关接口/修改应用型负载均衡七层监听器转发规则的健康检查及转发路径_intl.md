## API Description
 This API (ModifyLoadBalancerRulesProbe) is used to modify the health check and forwarding path for the forwarding rules of an application-based load balancer layer-7 listener.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is ModifyLoadBalancerRulesProbe.
 
| Parameter Name | Required | Type | Description |
|-----|------|--------|-----------|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based load balancer listener, which can be queried via the API DescribeForwardLBListeners. |
| locationId | Yes | String | ID for the forwarding rules of application-based load balancer listener. It can be queried via the API DescribeForwardLBListeners. |
| url | No | String | Path for the forwarding rules of application-based load balancer listener with a length limited to 1-80. Two formats can be used: one with modifiers and one without modifiers. Modifiers can be "~", "~\*", "^~", and "=". "~" indicates a case-sensitive regular expression, and "~*" indicates a case-insensitive regular expression. "^~" means that if the expression is determined to be the best match, the subsequent search match is not performed. "=" means exact match. The forwarding path is matched only when the request path is exactly the same as that in the expression. Characters supported in a non-regular expression include letters, numbers, `_`, `.`, `-`, `?`, `=` and `/`. |
| sessionExpire | No | Int | Session persistence duration for the forwarding rules of application-based load balancer listener. 0 means disabled. Value range: 30-3600. |
| healthSwitch | No | Int | Health check for the forwarding rules of application-based load balancer listener. 1: Enable; 0: Disable. |
| intervalTime | No | Int | Interval between health checks for the forwarding rules of application-based load balancer listener. Value range: 5-300. |
| healthNum | No | Int | Healthy threshold for the forwarding rules of application-based load balancer listener. Value range: 2-10. |
| unhealthNum | No | Int | Unhealthy threshold for the forwarding rules of application-based load balancer listener. Value range: 2-10. |
| httpHash | No | Int | Forwarding method for the forwarding rules of application-based load balancer listener. Value range: wrr, ip_hash and least_conn. |
| httpCode | No | Int | Health status code for the forwarding rules of application-based load balancer listener. Value range: 1-31. Default is 31.<br> 1: It is considered healthy if the health check returns 1xx code; 2: It is considered healthy if the health check returns 2xx code; 4: It is considered healthy if the health check returns 3xx code; 8: It is considered healthy if the health check returns 4xx code; 16: It is considered healthy if the health check returns 5xx code. If you need multiple types of codes that can indicate healthy status, enter the accumulated value corresponding to such codes. |
| httpCheckPath | No | String | Check path for the forwarding rules of application-based load balancer listener, which is / by default and must begin with /. It should be a combination of 1-80 characters comprised of `a-z`, `0-9`, `_`, `.`, `-`, `?`, `=` and `/`. |
| httpCheckMethod | No | String | HTTP request method, including "HEAD" and "GET". |
| httpCheckDomain | No | String | Standard domain name for health check. Supported character sets: `a-z`, `0-9`, `_`, `.` and `-`. |


## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| requestId | Int | Request task ID. The operation status can be queried via the API [DescribeLoadBalancersTaskResult](https://cloud.tencent.com/document/api/214/4007). |

## Example
 
Request
```
https://lb.api.qcloud.com/v2/index.php?Action=ModifyLoadBalancerRulesProbe
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
&listenerId=lbl-20cxbf40
&locationId=loc-mpoupana
&url=/zero
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 28078
}
```


