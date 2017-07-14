## 1. API Description
 
This API (CreateBmListeners) is used to create BM load balancer layer-4 listeners. BM load balancer layer-4 listener provides specific rules for forwarding user requests, including parameters such as port, protocol, session persistence, health check and so on.

Domain for API request: bmlb.api.qcloud.com

The rules for configuring listeners are as follows:

Use limits for BM load balancers:
1) Layer-7 listener refers to listener with a protocol type of HTTP/HTTPS, while layer-4 listener refers to listener with a protocol type of TCP/UDP.
2) Layer-4 listener with a protocol type of TCP/UDP is supported by both public network BM load balancers (with daily rate) and private network BM load balancers.
3) Public network BM load balancers support layer-7 listeners with protocol type of HTTP/HTTPS, while private network BM load balancers support layer-7 listeners with protocol type of HTTP.
4) Within the same BM load balancer, each BM load balancer port can correspond to a layer-7 listener or a layer-4 listener with TCP protocol, but not both.
5) Within the same BM load balancer, a BM load balancer listener can correspond to multiple CPM ports.
6) Within the same BM load balancer, a CPM port cannot correspond to different layer-4 listeners with the same protocol.


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listeners | Yes | Array | Array containing listener information. You can create multiple listeners. Currently, you can create up to 50 listeners under a BM load balancer |

The listeners array is used to describe specific information of current listeners. "n" is subscript, the array includes the following fields

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| listeners.n.loadBalancerPort | Yes | Int | Listening port of BM load balancer listener. Value range: 1-65535. |
| listeners.n.protocol | Yes | Int | Protocol type of BM load balancer instance listener. Value can be TCP or UDP. |
| listeners.n.listenerName | No | String | Name of BM load balancer listener. |
| listeners.n.sessionExpire | No | Int | Session persistence duration of BM load balancer listener (in sec). Value range: 900 ~ 3600. Session persistence is disabled if you don't pass any value. |
| listeners.n.healthSwitch | No | Int | Indicate whether health check is enabled for BM load balancer instance listener. 1: On; 0: Off. Default value is 0 (off). |
| listeners.n.timeOut | No | Int | Health check response timeout for the BM load balancer listener (in sec). Value range: 2-60. Default is 2. <br>The response timeout must be smaller than health check time interval. |
| listeners.n.intervalTime | No | Int | Health check time interval of BM load balancer listener (in sec). Default: 5; value range: 5-300. |
| listeners.n.healthNum | No | Int | Health threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: count. |
| listeners.n.unhealthNum | No | Int | Unhealth threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10; unit: count. |
| listeners.n.bandwidth | No | Int | Used to specify the maximum bandwidth of the listener with the billing mode is pay-by-fixed bandwidth. Value range: 0-1000 (in Mbps). |




## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| requestId | Int | Task ID. This API is an asynchronous task. You can query task operation result by calling API [DescribeBmLoadBalancersTaskResult](/document/product/386/9308) based on this parameter |


Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |
| 12003 | IncorrectStatus.LBWrongStatus | The operation is impossible due to incorrect status of BM load balancer |
| 12014 | InvalidResource.ListenerNumberOverLimit | The number of listeners of this BM load balancer has exceeded the limit |
| -12013 | InvalidParameter.VportIsDuplicate | Listener for this port already exists in this BM load balancer |

## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=CreateBmListeners
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listeners.1.loadBalancerPort=1234
&listeners.1.protocol=tcp
&listeners.1.listenerName=tcp-test
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
