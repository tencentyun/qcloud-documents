## API Description
This API (ModifyForwardLBFourthListener) is used to modify the attributes of application-based load balancer layer-4 listener.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is ModifyForwardLBFourthListener.
 
| Parameter Name | Required | Type | Description |
|-----|------|--------|-----------|
| loadBalancerId | Yes | String | ID of load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based load balancer listener, which can be queried via the API DescribeForwardLBListeners. |
| listenerName | No | String | Listener name. |
| sessionExpire | No | Int | Session persistence duration. 0 means disabled. Value range: 30-3600 seconds. |
| healthSwitch | No | Int | Whether to enable health check: 1 (Enable) and 0 (Disable). |
| timeOut | No | Int | Response timeout. Value range: 2-60 seconds. |
| intervalTime | No | Int | Interval between health checks. Value range: 5-300. |
| healthNum | No | Int | Healthy threshold. Value range: 2-10. |
| unhealthNum | No | Int | Unhealthy threshold. Value range: 2-10. |
| scheduler | No | String | Forwarding method of the load balancer listener. <br>Available values: wrr (polling by weight), least_conn (minimum number of connections). |

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
https://lb.api.qcloud.com/v2/index.php?Action=ModifyForwardLBFourthListener
&<Common request parameters>
&loadBalancerId=lb-ltkip4do
&listenerId=lbl-6hkiqc6c
&SSLMode=unidirectional
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 18642
}

```

