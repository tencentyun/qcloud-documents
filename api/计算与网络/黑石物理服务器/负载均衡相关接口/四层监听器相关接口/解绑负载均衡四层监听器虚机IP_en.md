## 1. API Description
 
This API (UnbindBmL4ListenerVmIp) is used to unbind VM IP from BM load balancer layer-4 listeners.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the BM load balancer layer-4 listener, which can be queried via API [DescribeBmListeners](/document/product/386/9296). |
| vmList | Yes | Array |   Information of the VM to be unbound. |

"vmList" describes the information of the VM to be unbound. It contains the following fields ("n" is subscript)

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vmList.n.port | Yes | Int | VM port to be unbound. Available value range: 1-65535. |
| vmList.n.vmIp | Yes | String | VM IP to be unbound. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |


Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |
| 12003 | IncorrectStatus.LBWrongStatus | The operation is impossible due to incorrect status of BM load balancer |
| -21001 | InvalidStatus.LBInvalidStatus | The operation is not allowed due to the current status of BM load balancer |
| -12023 | InvalidL4Listener.NotExist | The layer-4 listener does not exist in CCDB |
| 11060 | InternalError.TGWAbnormal | TGW service error |



## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=UnbindBmL4ListenerVmIp
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&vmList.1.port=1234
&vmList.1.vmIp=1.1.1.1
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}

```
