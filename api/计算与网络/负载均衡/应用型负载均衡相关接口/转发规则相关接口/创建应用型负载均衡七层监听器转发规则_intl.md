## API Description
This API (CreateForwardLBListenerRules) is used to create forwarding rules of an application-based load balancer layer-7 listener.

Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is CreateForwardLBListenerRules.


| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based load balancer listener, which can be queried via the API DescribeForwardLBListeners. |
| rules.n.domain | Yes | String | Domain name for the forwarding rules of application-based load balancer listener. Length limit: 1-80. Three formats are supported: non-regular expression, wildcard and regular expression. Non-regular expressions can only contain letters, numbers, "-", and ".". For wildcard format, "*" can only be placed at the beginning or the end. Regular expressions must start with "~". Native regular expression from nginx is supported. |
| rules.n.url | Yes | String | Path for the forwarding rules of application-based load balancer listener. Length limit: 1-80. Two formats are supported: one with modifiers and one without modifiers. Modifiers can be "~", "~\*", "^~" and "=". "~" indicates a case-sensitive regular expression, and "~*" indicates a case-insensitive regular expression. "^~" means that if the expression is determined to be the best match, the subsequent search match is not performed. "=" means exact match. The forwarding path is matched only when the request path is exactly the same as that in the expression. Characters supported in a non-regular expression include letters, numbers, "_", "-", ".", "=", "?" and "/". |
| rules.n.sessionExpire | No | Int | Session persistence duration for the forwarding rules of application-based load balancer listener. 0 means disabled. Value range: 30-3600. |
| rules.n.healthSwitch | No | Int | Health check for the forwarding rules of application-based load balancer listener. 1: Enable; 0: Disable. Default is 1 (Enable). |
| rules.n.intervalTime | No | Int | Time interval between health checks on the forwarding rules of application-based load balancer listener (in sec). Default value: 5. Value range: 5-300. |
| rules.n.healthNum | No | Int | Healthy threshold for the forwarding rules of application-based load balancer listener (in count). Default value: 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10. |
| rules.n.unhealthNum | No | Int | Unhealthy threshold for the forwarding rules of application-based load balancer listener (in count). Default value: 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10. |
| rules.n.httpHash | No | String | Forward method for the forwarding rules of application-based load balancer listener. <br>Available values: wrr (polling by weight), ip_hash (hashing a value based on the source IP and forwarding the value to the backend server), least_conn (minimum number of connections). Default is wrr. |
| rules.n.httpCode | No | Int | Health status code for the forwarding rules of application-based load balancer listener. Value range: 1-31. Default is 31.<br> 1: It is considered healthy if the health check returns 1xx code; 2: It is considered healthy if the health check returns 2xx code; 4: It is considered healthy if the health check returns 3xx code; 8: It is considered healthy if the health check returns 4xx code; 16: It is considered healthy if the health check returns 5xx code. If you need multiple types of codes that can indicate healthy status, enter the accumulated value corresponding to such codes. |
| rules.n.httpCheckPath | No | String | Check path for the forwarding rules of application-based load balancer listener, which is / by default and must begin with /. It must be a combination of 1-80 characters comprised of letters, numbers, "_", "-", ".", "=", "?" and "/". |



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
https://lb.api.qcloud.com/v2/index.php?Action=CreateForwardLBListenerRules
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
&listenerId=lbl-20cxbf40
&rules.0.domain=www.tencent.com
&rules.0.url=fourth
&rules.0.sessionExpire=211
&rules.0.healthSwitch=0
&rules.0.httpHash=ip_hash
&rules.1.domain=www.ali.com
&rules.1.url=/second
&rules.1.sessionExpire=321
&rules.1.healthSwitch=1
&rules.1.httpHash=ip_hash

```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 28182
}
```
