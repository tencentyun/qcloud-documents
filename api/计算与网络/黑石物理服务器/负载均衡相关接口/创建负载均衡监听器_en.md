## 1. API Description
 
This API (CreateBmLoadBalancerListeners) is used to create BM load balancer listeners. A BM load balancer listener provides specific rules for forwarding user requests, including parameters such as port, protocol, session persistence, health check and so on.

Domain for API request: <font style="color:red">lb.api.qcloud.com</font>

The rules for configuring listeners are as follows:

Service limits on public network-based load balancers (with daily rate):
1) Within one BM load balancer, a balancer port can only correspond to one protocol type,
2) Within one BM load balancer, a balancer port can correspond to multiple CVM ports,
3) TCP protocol is supported.

Service limits on private network-based BM load balancers:
1) Within one BM load balancer, a balancer port can only correspond to one protocol type,
2) Within one BM load balancer, a balancer port can correspond to multiple CVM ports,
3) Within one BM load balancer, CVMs must have different ports,
4) TCP protocol is supported.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/doc/api/456/6658). |
| listeners | Yes | Array | Array containing listener information. You can create multiple listeners. Currently, you can create up to 50 listeners under a BM load balancer |

The listeners array is used to describe specific information of current listeners. "n" is subscript, the array includes the following fields

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| listeners.n.loadBalancerPort | Yes | Int | Listening port of BM load balancer listener. Value range: 1-65535. |
| listeners.n.instancePort | Yes | Int | Backend CPM listening port of BM load balancer instance listener. Value range: 1-65535. |
| listeners.n.protocol | Yes | Int | Protocol type of BM load balancer instance listener. 2: TCP |
| listeners.n.listenerName | No | String | Name of BM load balancer listener. |
| listeners.n.sessionExpire | No | Int | Session persistence duration of BM load balancer listener. Unit: second. Value range: 900 ~ 3600. Session persistence is disabled if you don't pass any value. |
| listeners.n.healthSwitch | No | Int | Indicate whether health check is enabled for BM load balancer instance listener. 1: On; 0: Off. Default value is 1 (On). |
| listeners.n.timeOut | No | Int | Health check response timeout for the BM load balancer listener (in second). Value range: 2-60. Default is 2.  <br>The response timeout must be smaller than health check time interval.|
| listeners.n.intervalTime | No | Int | Health check time interval of BM load balancer listener (in second). Default: 5; value range: 5-300. |
| listeners.n.healthNum | No | Int | Health threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: count. |
| listeners.n.unhealthNum | No | Int | Unhealth threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10; unit: count. |
| listeners.n.bandwidth | No | Int | Used to specify the maximum bandwidth of the listener with the billing mode is pay-by-fixed bandwidth. Value range: 0-1000 (in Mbps). |




## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| requestId | Int | Task ID. This API is an asynchronous task. You can query task operation result by calling API [DescribeBmLoadBalancersTaskResult](/doc/api/456/6666) based on this parameter |


Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |
| 12003 | IncorrectStatus.LBWrongStatus | The operation is impossible due to incorrect status of BM load balancer |
| 12014 | InvalidResource.ListenerNumberOverLimit | The number of listeners of this BM load balancer has exceeded the limit |

## 4. Example
 
Input

<pre>
	https://domain/v2/index.php?
	Action=DescribeBmLoadBalancersTaskResult
	&loadBalancerId=lb-abcdefgh
	&listeners.1.loadBalancerPort=1234
	&listeners.1.instancePort=1234
	&listeners.1.protocol=2
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId" : 1234
}

```
