## API Description
This API (CreateForwardLBFourthLayerListeners) is used to create load balancer layer-4 listener. A load balancer layer-4 listener provides specific rules for forwarding user requests, including parameters such as port, protocol, session persistence, health check and so on.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is CreateForwardLBFourthLayerListeners.


| Parameter Name | Required | Type | Description |
|-----------|--------|----------|----------|
| loadBalancerId | Yes | String | ID of load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listeners.n.loadBalancerPort | Yes | Int | Listening port of the load balancer listener. Value range: 1-65535. listeners is an array. You can create multiple listeners. n is subscript. |
| listeners.n.protocol | Yes | Int | Protocol type of load the balancer instance listener. 2: TCP, 3:UDP. |
| listeners.n.listenerName | No | String | Name of the load balancer listener. |
| listeners.n.sessionExpire | No | Int | Session persistence duration of load balancer listener (in sec). Value range: 30-3600. Default is 0 (Disable). |
| listeners.n.healthSwitch | No | Int | Whether to enable health check for load balancer instance listeners: 1 (Enable) and 0 (Disable). Default is 1 (Enable). |
| listeners.n.timeOut | No | Int | Health check response timeout for the load balancer listener (in sec). Value range: 2-60. Default is 2. The response timeout must be smaller than the time interval between health checks. |
| listeners.n.intervalTime | No | Int | Time interval between health checks on the load balancer listener (in sec). Default: 5. Value range: 5-300. |
| listeners.n.healthNum | No | Int | Healthy threshold of the load balancer listener (in count). Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10. |
| listeners.n.unhealthNum | No | Int | Unhealthy threshold of the load balance listener (in count). Default is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10. |
| listeners.n.scheduler | No | String | Forwarding method of the load balancer listener. <br>Available values: wrr (polling by weight), least_conn (minimum number of connections). Default is wwr. |


## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| requestId | Int | Request task ID. The operation status can be queried via the API [DescribeLoadBalancersTaskResult](https://cloud.tencent.com/document/api/214/4007). |
| listenerIds | Array | Listener ID array. |

## Example
 
Request
```
https://lb.api.qcloud.com/v2/index.php?Action=CreateForwardLBFourthLayerListeners
&<Common request parameters>
&loadBalancerId=lb-abcdefgh
&listeners.0.loadBalancerPort=80
&listeners.0.protocol=2
&listeners.0.listenerName=2
```
Response
```
{
  "code" : 0,
  "message" : "",
  "codeDesc": "Success",
  "requestId" : 123,
  "listenerIds": [
        "lbl-3jt7mido"
      ]
}
```




