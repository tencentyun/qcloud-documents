## 1. API Description
 
This API (ModifyBmLocationBackendPort) is used to modify the backend instance port of BM load balancer layer-7 forwarding path.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the load balancer's layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| domainId | Yes | String | ID of the load balancer's layer-7 forwarding domain, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| locationId | Yes | String | ID of the load balancer's layer-7 forwarding path, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| instanceId | Yes | String | ID of the CPM. |
| port | Yes | Int | Bound CPM port. |
| newPort | Yes | Int | New CPM port. Value range: 1-65535. |


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
| -21000 | InvalidStatus.DeviceInvalidStatus | The operation is not allowed due to the current device status |
| 11060 | InternalError.TGWAbnormal | TGW service error |
| 28000 | InternalError.VPCAbnormal | VPC service error |
| 14100 | InternalError.BmApiAbnormal | bmApi service error |
| 30011 | InvalidRs.NotExist | CPM information does not exist |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=ModifyBmLocationBackendPort
&<<a href="https://www.qcloud.com/document/product/386/6718">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&domainId=dm-abcdefgh
&locationId=loc-abcdefgh
&instanceId=cpm-abcdefgh
&port=1234
&newPort=12345
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}

```
