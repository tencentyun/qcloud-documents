## 1. API Description
 
This API (DescribeBmLocationBackends) is used to acquire the list of CPMs to which the BM load balancer layer-7 forwarding paths are bound.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the load balancer's layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| domainId | Yes | String | ID of the load balancer's layer-7 forwarding domain name, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| locationId | Yes | String | ID of the load balancer's layer-7 forwarding path, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| offset | No | Int | Offset. |
| limit | No | Int | Number of results to be returned. |


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
| mgtIp | String | Management IP of the CPM. |
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


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmLocationBackends
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&domainId=dm-abcdefgh
&locationId=loc-abcdefgh
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
            "rsPort": 1234,
            "weight": 10,
            "instanceId": "cpm-abcdefgh",
            "alias": "XXX Test",
            "lanIp": "1.1.1.1",
            "mgtIp": "2.2.2.2",
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
            ],
            "status": "Dead"
        }
    ]
}

```
