## 1. API Description
 
This API (BindBmL7LocationVmIp) is used to bind VM IP to BM load balancer layer-7 forwarding path.

Domain for API request: <font style="color:red">bmlb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the load balancer's layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| domainId | Yes | String |   ID of the load balancer's layer-7 forwarding domain, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| locationId | Yes | String |   ID of the load balancer's layer-7 forwarding path, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| vmList | Yes | Array |   Information of the VM to be bound. You can bind multiple VM ports. Currently, you can bind up to 255 VM ports under a layer-7 forwarding path. |

"vmList" describes the information of the VM to be bound. It contains the following fields ("n" is subscript)

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vmList.n.port | Yes | Int | VM port to be bound. Available value range: 1-65535. |
| vmList.n.vmIp | Yes | String | VM IP to be bound. |
| vmList.n.weight | Yes | Int | Weight. Available value range: 0-100. |


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
| 12013 | InvalidResource.BindCPMNumberOverLimit | The number of CPM ports bound to this BM load balancer has exceeded the limit |
| 11060 | InternalError.TGWAbnormal | TGW service error |
| 28000 | InternalError.VPCAbnormal | VPC service error |
| 14100 | InternalError.BmApiAbnormal | bmApi service error |
| -12024 | InvalidVmIp.NotExist | The VM IP does not exist |
| -12025 | InvalidVmIp.AlreadyExist | The VM IP port has already been bound to layer-7 forwarding path |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=BindBmL7LocationVmIp
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&domainId=dm-abcdefgh
&locationId=loc-abcdefgh
&vmList.1.port=1234
&vmList.1.vmIp=1.1.1.1
&vmList.1.weight=10
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}

```
