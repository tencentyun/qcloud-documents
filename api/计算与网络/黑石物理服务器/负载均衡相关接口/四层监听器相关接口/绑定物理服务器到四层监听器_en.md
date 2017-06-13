## 1. API Description
 
This API (BindBmL4ListenerRs) is used to bind CPM to layer-4 listeners.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the BM load balancer layer-4 listener, which can be queried via API [DescribeBmListeners](/document/product/386/9296). |
| backends | Yes | Array |   Information of the CPM to be bound. You can bind multiple CPM ports. Currently, you can bind up to 255 CPM ports under a layer-4 listener. |

"backends" describes the information of the CPM to be bound. It contains the following fields ("n" is subscript)

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| backends.n.port | Yes | Int | CPM port to be bound. Available value range: 1-65535. |
| backends.n.instanceId | Yes | String | ID of the CPM instance to be bound. |
| backends.n.weight | Yes | Int | Weight. Available value range: 0-100. |


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
| -21000 | InvalidStatus.DeviceInvalidStatus | The operation is not allowed due to the current device status |
| 12013 | InvalidResource.BindCPMNumberOverLimit | The number of CPM ports bound to this BM load balancer has exceeded the limit |
| 14100 | InternalError.BmApiAbnormal | bmApi service error |
| 30011 | InvalidRs.NotExist | CPM information does not exist |
| -12022 | InvalidParameter.InvalidMultiL4VportToRsport | This CPM port has been bound to layer-4 listener |


## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=BindBmL4ListenerRs
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&backends.1.port=1234
&backends.1.instanceId=cpm-abcdefgh
&backends.1.weight=10
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}

```
