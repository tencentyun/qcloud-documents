## 1. API Description
 
This API (DescribeBmForwardListeners) is used to acquire BM load balancer layer-7 listeners.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerIds.n | No | Array | List of IDs of load balancer layer-7 listeners. The IDs can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| listenerSet | Array | List of returned layer-7 listeners. |

Each sub-item of listensetSet is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| listenerId | String | ID of the load balancer layer-7 listener. |
| listenerName | String | Name of the cloud load balancer layer-7 listener. |
| protocol | String | Protocol type of load balancer layer-7 listener (HTTP, HTTPS). |
| loadBalancerPort | Int | Listening port of the load balancer layer-7 listener. |
| bandwidth | Int | Maximum bandwidth of the listener when the billing mode is pay-by-fixed bandwidth (in Mbps). |
| listenerType | String | Listener type: L4Listener (layer-4 listener) or L7Listener (layer-7 listener). |
| SSLMode | Int | Authentication method of load balancer layer-7 listener. 0: no authentication, used for HTTP; 1: one-way authentication, used for HTTPS; 2: two-way authentication, used for HTTPS. |
| certId | String | ID of the server certificate associated with the load balancer layer-7 listener. |
| certCaId | String | ID of the client certificate associated with the load balancer layer-7 listener. |
| status | Int | Current status of the listener. 0: Creating; 1: Running; 2: Creation failed; 3: Deleting; 4: Deletion failed. |
| addTimestamp | String | Creation time stamp. |

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmForwardListeners
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerIds.1=lbl-abcdefgh
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "listenerSet": [
        {
            "listenerId": "lbl-abcdefgh",
            "listenerName": "xxx",
            "protocol": "http",
            "loadBalancerPort": 1234,
            "bandwidth": 0,
            "listenerType": "L7Listener",
            "SSLMode": 0,
            "certId": "",
            "certCaId": "",
            "status": 1,
            "addTimestamp": "2017-03-09 19:34:45"
        }
    ],
    "totalCount": 1
}

```
