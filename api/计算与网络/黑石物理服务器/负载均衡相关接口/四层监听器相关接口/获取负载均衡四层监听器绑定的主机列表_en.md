## 1. API Description
 
This API (DescribeBmL4ListenerBackends) is used to acquire the list of CPMs bound with BM load balancer layer-4 listeners.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the BM load balancer layer-4 listener, which can be queried via API [DescribeBmListeners](/document/product/386/9296). |
| backends | No | Array |   Information of the CPM to be queried. |

"backends" describes the information of the CPM to be queried. It contains the following fields ("n" is subscript)

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| backends.n.port | Yes | Int | CPM port to be bound. Available value range: 1-65535. |
| backends.n.instanceId | Yes | String | ID of the CPM instance to be bound. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| data | Array | Returned list of binding relationships. |

Each sub-item of data contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| bindType | Int | Type of the bind. 0: CPM; 1: VM IP. |
| rsPort | Int | CPM port. |
| weight | Int | Weight. |
| status | String | Current health status of the binding relationship. "Dead" indicates unhealthy, while "Alive" indicates healthy. |

The following fields are included when bindType is 0

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | ID of the CPM. |
| alias | String | Alias of the CPM. |
| lanIp | String | Private IP of the CPM. |
| operates | Array | Currently available operations for the CPM. |

The following fields are included when bindType is 1

| Parameter Name | Type | Description |
|---------|---------|---------|
| lanIp | String | VM IP. |



Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |
| 11060 | InternalError.TGWAbnormal | TGW service error |
| 14100 | InternalError.BmApiAbnormal | bmApi service error |


## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmL4ListenerBackends
&<<a href="https://cloud.tencent.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "bindType": 0,
            "lanIp": "1.1.1.1",
            "rsPort": 1234,
            "weight": 10,
            "status": "Dead",
            "instanceId": "cpm-abcdefgh",
            "alias": "XXX",
            "operates": [
                "modifyDeviceAlias",
                "renewDevice",
                "shutdownDevice",
                "rebootDevice",
                "reloadDeviceOs",
                "resetPasswd",
                "bindEip",
                "unbindEip",
                "isolateDevice",
                "offlineDevice",
                "bindLb",
                "unbindLb"
            ]
        }
    ]
}

```
