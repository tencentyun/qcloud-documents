## API Description
 This API (RegisterInstancesWithForwardLBSeventhListener) is used to associate one or more CVMs to the forwarding rules of application-based load balancer listener.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters
 
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is RegisterInstancesWithForwardLBSeventhListener.

| Parameter Name | Required | Type | Description |
|-|-|-|-|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based load balancer listener, which can be queried via the API DescribeForwardLBListeners. |
| locationIds.n | No | String | ID for the forwarding rules of application-based load balancer listener. |
| domain | No | String | Domain name for the forwarding rules of application-based load balancer listener. |
| url | No | String | Path of forwarding rule of the application-based load balancer listener. |
| backends.n.instanceId | Yes | String | Unique ID of the CVM, which can be obtained from "unInstanceId" in the returned fields of API <a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a>. <br>This API allows entering instance IDs of multiple CVMs at a time. For example, if you want to enter two CVMs, enter: backends.1.instanceId&backends.2.instanceId. |
| backends.n.port | Yes | Int | Listening port of backend CVM of load balancer listener. Value range: 1-65535. |
| backends.n.weight | No | Int | Weight of CVM. Value range is 0-100. Default is 10. |

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
https://lb.api.qcloud.com/v2/index.php?Action=RegisterInstancesWithForwardLBSeventhListener
&<Common request parameters>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&locationIds.0=loc-aaa
&backends.0.instanceId=ins-1234test
&backends.0.port=80
&backends.0.weight=10
&backends.1.instanceId=ins-5678test
&backends.1.port=80
&backends.1.weight=6
```
Response
```
{
  "code" : 0,
  "message" : "",
  "codeDesc": "Success"
  "requestId" : 1234
}
```

