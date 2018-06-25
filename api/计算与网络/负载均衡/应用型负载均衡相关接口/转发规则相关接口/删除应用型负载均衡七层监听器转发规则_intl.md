## API Description
 This API (DeleteForwardLBListenerRules) is used to delete forwarding rules of an application-based load balancer instance layer-7 listener.
 
Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DeleteForwardLBListenerRules.
 
| Parameter Name | Required | Type | Description |
|-|-|-|-|-|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based load balancer listener, which can be queried via the API DescribeForwardLBListeners. |
| locationIds.n | No | String | ID for the forwarding rules of application-based load balancer listener. It can be queried via the API DescribeForwardLBListeners. |
| domain | No | String | Domain name for the forwarding rules of application-based load balancer listener. |
| url | No | String | Path for the forwarding rules of application-based load balancer listener. |

 
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
https://lb.api.qcloud.com/v2/index.php?Action=DeleteForwardLBListenerRules
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
&listenerId=lbl-20cxbf40
&locationIds.0=loc-mpoupana
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 28502
}
```



