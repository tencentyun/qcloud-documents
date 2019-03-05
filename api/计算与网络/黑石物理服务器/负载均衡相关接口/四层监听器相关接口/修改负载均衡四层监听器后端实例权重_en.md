## 1. API Description
 
This API (ModifyBmL4ListenerBackendWeight) is used to modify the backend instance weight of BM load balancer layer-4 listeners.

Domain for API request: bmlb.api.qcloud.com 


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the BM load balancer layer-4 listener, which can be queried via API [DescribeBmListeners](/document/product/386/9296). |
| instanceId | Yes | String |   ID of the CPM. |
| weight | Yes | Int | Weight. Available value range: 0-100. |
| port | Yes | Int | Bound CPM port. |


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
| 11060 | InternalError.TGWAbnormal | TGW service error |
| 14100 | InternalError.BmApiAbnormal | bmApi service error |
| 30011 | InvalidRs.NotExist | CPM information does not exist |

## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=ModifyBmL4ListenerBackendWeight
&<<a href="https://cloud.tencent.com/document/product/386/6718">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&instanceId=cpm-abcdefgh
&weight=100
&port=1234
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}

```
