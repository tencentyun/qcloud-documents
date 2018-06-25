## API Description
Domain name: `lb.api.qcloud.com`
API name: `ManualRewrite`

## Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| rewriteInfo | Yes | Array | Forwarding rules of redirect relationship. Batch operations are supported. |
| sourceuListenerId | Yes | String | ID of source listener, which can be queried via the API DescribeForwardLBListeners. |
| targetuListenerId | Yes | String | ID of target listener, which can be queried via the API DescribeForwardLBListeners. |

rewriteInfo is a list and each element is a redirect configuration that is composed of the following fields:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| sourceLocation | Yes | String | Unique ID of source forwarding rule. |
| targetLocation | Yes | String | Unique ID of target forwarding rule. |

## Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed. |
| message | String | Error message. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| requestId | Int | ID of asynchronous task of automatic redirect. The execution result can be queried using the API for querying asynchronous task. |

## Example

Input
```
https://lb.api.qcloud.com/v2/index.php?Action=ManualRewrite
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
&rewriteInfo.0.sourceLocation=loc-asdmamd
&rewriteInfo.0.targetLocation=loc-eewqfqw
&sourceuListenerId=lbl-xxasaads
&targetuListenerId=lbl-xxasaads
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




