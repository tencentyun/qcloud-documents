## 1. API Description
 API ModifyLoadBalancerRulesProbe is used to modify the attributes of the forwarding rules of application-based cloud load balancer listener and the path for forwarding.
 
Domain for API access: lb.api.qcloud.com


## 2. Request Parameters

   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is ModifyLoadBalancerRulesProbe.
 
| Parameter Name | Required | Type | Description |
|-----|------|--------|-----------|
| loadBalancerId | Yes | String | ID of cloud load balancer instance, i.e. unLoadBalancerId, which can be queried by entering 1 or -1 in input parameter "forward" field through API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based cloud load balancer listener, which can be queried through API DescribeForwardLBListeners. |
| locationId | Yes | String | ID for the forwarding rules of application-based cloud load balancer listener. It can be queried through API DescribeForwardLBListeners. |
| url | No | String | Path for the forwarding rules of application-based cloud load balancer listener. The length range is between 1 and 80 characters. Two formats can be used: one with modifiers and one without modifiers. Modifiers can be "~", "~\*", "^~", and "=". "~" means that the expression that follows is a case-sensitive one, and "~*" means that the expression that follows is not case-sensitive. The modifier "^~" means that if the expression is determined to be the best match, the subsequent search match will not be performed. "=" means exact match. The forwarding can be satisfied only when the request is exactly the same as the expression. Characters that can be used in a non-regular expression include letters, numbers, "_", "-", ".", "&", "#", "？", "%", and "/". |
| sessionExpire | No |Int| Session duration of forwarding rules of application-based cloud load balancer listener. 0 means Off. Value range: 30-3600. |
| healthSwitch | No | Int | Health check on the forwarding rules of application-based cloud load balancer listener. 1: On; 0: Off. |
| intervalTime | No | Int | The time interval between health checks on the forwarding rules of application-based cloud load balancer listener. Value range: 5-300. |
| healthNum | No | Int | Healthy threshold for the forwarding rules of application-based cloud load balancer listener. Value range: 2-10. |
| unhealthNum | No | Int | Unhealthy threshold for the forwarding rules of application-based cloud load balancer listener. Value range: 2-10. |
| httpHash | No | Int | Forward method of the forwarding rules of application-based cloud load balancer listener. Available values: wrr, ip_hash. |
| httpCode | No | Int | Health status code for the forwarding rules of application-based cloud load balancer listener. Value range: 1-31. The default is 31. <br>1: it is considered healthy if the health check returns 1xx code; 2: it is considered healthy if the health check returns 2xx code; 4: it is considered healthy if the health check returns 3xx code; 8: it is considered healthy if the health check returns 4xx code; 16: it is considered healthy if the health check returns 5xx code. If there should be multiple types of codes that can indicate healthy status, enter the accumulated value corresponding to such codes. |
| httpCheckPath | No | String | Check path for forwarding rules of application-based cloud load balancer listener, which is / by default and must start with /. The length range is between 1 and 80 characters. Characters that can be used include letters, numbers, "_", "-", ".", "&", "#", "？", "%", and "/". |


## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| requestId | Int | Request task ID. The operation status can be queried through API [DescribeLoadBalancersTaskResult](/doc/api/244/4007). |

## 4. Example
 
Input
```
https://lb.api.qcloud.com/v2/index.php?Action=ModifyLoadBalancerRulesProbe
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
&listenerId=lbl-20cxbf40
&locationId=loc-mpoupana
&url=/zero
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 28078
}
```



