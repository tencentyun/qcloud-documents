## 1. API Description
 
This API (ModifyBmListener) is used to modify BM load balancer layer-4 listeners.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | Layer-4 listener ID, which can be queried via API [DescribeBmListeners](/document/product/386/9296). |
| listenerName | No | String | Name of new BM load balancer layer-4 listener. |
| sessionExpire | No | Int | Session persistence duration of new BM load balancer listener (in sec). Value range: 900-3600. |
| healthSwitch | No | Int | Indicate whether health check is enabled for new BM load balancer instance listener. 1: On; 0: Off. Default value is 0 (off). |
| timeOut | No | Int | Health check response timeout for new BM load balancer listener (in sec). Value range: 2-60. Default is 2. <br><font color="red">The response timeout must be smaller than health check time interval. </font>|
| intervalTime | No | Int | Health check time interval of new BM load balancer listener (in sec). Default: 5; value range: 5-300. |
| healthNum | No | Int | Health threshold of new BM load balancer listener. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: count. |
| unhealthNum | No | Int | Health threshold of new BM load balancer listener. Default value is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10; unit: count. |
| bandwidth | No | Int | Used to specify the maximum bandwidth of new listener with the billing mode is pay-by-fixed bandwidth. Value range: 0-1000 (in Mbps). |


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
| -21001 | InvalidStatus.LBInvalidStatus | The operation is not allowed due to the current status of BM load balancer |
| -12023 | InvalidL4Listener.NotExist | The layer-4 listener does not exist in CCDB |
| -12021 | IncorrectStatus.L4ListenerWrongStatus | The operation is impossible due to incorrect status of BM load balancer layer-4 listener |


## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=ModifyBmListener
&<<a href="https://www.qcloud.com/document/product/386/6718">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&listenerName=tcp-listener
&healthSwitch=1
&timeOut=6
&intervalTime=10
&healthNum=8
&unhealthNum=8
&sessionExpire=1000
&bandwidth=5
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

