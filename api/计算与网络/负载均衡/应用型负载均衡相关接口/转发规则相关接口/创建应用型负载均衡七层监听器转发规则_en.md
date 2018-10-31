## 1. API Description
 API CreateForwardLBListenerRules provides the ability to create forwarding rules of application-based cloud load balancer listener.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is CreateForwardLBListenerRules.


| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| loadBalancerId | Yes | String | ID of cloud load balancer instance, i.e. unLoadBalancerId, which can be queried by entering 1 or -1 in input parameter "forward" field through API <a href="https://cloud.tencent.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based cloud load balancer listener, which can be queried through API DescribeForwardLBListeners. |
| rules.n.domain | Yes | String | Domain for the forwarding rules of application-based cloud load balancer listener. The length range is between 1 and 80 characters. Three formats can be used: non-regular expression, wildcard and regular expression. With the non-regular expression format, only letters, numbers, "-", and "." can be contained. With the wildcard format, "*" can only be placed at the beginning or the end. Regular expressions must start with "~", and those native from nginx are supported. |
| rules.n.url | Yes | String | Path for the forwarding rules of application-based cloud load balancer listener. The length range is between 1 and 80 characters. Two formats can be used: one with modifiers and one without modifiers. Modifiers can be "~", "~\*", "^~" and "=". "~" means that the expression that follows is a case-sensitive one, and "~*" means that the expression that follows is not case-sensitive. The modifier "^~" means that if the expression is determined to be the best match, the subsequent search match will not be performed. "=" means exact match. The forwarding can be satisfied only when the request is exactly the same as the expression. Characters that can be used in a non-regular expression include letters, numbers, "_", "-", ".", "&", "#", "？",  "%", and "/". |
| rules.n.sessionExpire | No |Int| Session duration of forwarding rules of application-based cloud load balancer listener. 0 means Off. Value range: 30-3600. |
| rules.n.healthSwitch | No | Int | Health check on the forwarding rules of application-based cloud load balancer listener. 1: On; 0: Off. Default value: 1, which means On. |
| rules.n.intervalTime | No | Int | The time interval between health checks on the forwarding rules of application-based cloud load balancer listener. Default value: 5; value range: 5-300; unit: second. |
| rules.n.healthNum | No | Int | Healthy threshold for the forwarding rules of application-based cloud load balancer listener. Default value: 3, which means the forwarding is normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: time. |
| rules.n.unhealthNum | No | Int | Unhealthy threshold for the forwarding rules of application-based cloud load balancer listener. Default value: 3, which means the forwarding is abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10; unit: time. |
| rules.n.httpHash | No | String | Forward method of the forwarding rules of application-based cloud load balancer listener. Available values: wrr (weighted round robin), ip_hash (IP_HASH)<br>. Default is wrr. |
| rules.n.httpCode | No | Int | Health status code for the forwarding rules of application-based cloud load balancer listener. Value range: 1-31. The default is 31. <br>1: it is considered healthy if the health check returns 1xx code; 2: it is considered healthy if the health check returns 2xx code; 4: it is considered healthy if the health check returns 3xx code; 8: it is considered healthy if the health check returns 4xx code; 16: it is considered healthy if the health check returns 5xx code. If there should be multiple types of codes that can indicate healthy status, enter the accumulated value corresponding to such codes. |
| rules.n.httpCheckPath | No | String | Check path for forwarding rules of application-based cloud load balancer listener, which is / by default and must start with /.  The length range is between 1 and 80 characters. Characters that can be used include letters, numbers, "_", "-", ".", "&", "#", "？", "%", and "/". |



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
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 28182
}
```
