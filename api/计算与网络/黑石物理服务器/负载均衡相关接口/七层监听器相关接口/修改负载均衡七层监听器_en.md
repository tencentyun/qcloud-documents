## 1. API Description
 
This API (ModifyBmForwardListener) is used to modify BM load balancer layer-7 listeners.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| listenerName | No | String | New name of the load balancer layer-7 listener. |
| SSLMode | No | Int | Authentication method of load balancer layer-7 listener. 0: no authentication, used for HTTP; 1: one-way authentication, used for HTTPS; 2: two-way authentication, used for HTTPS. |
| certId | No | String | New server certificate ID of the load balancer layer-7 listener. |
| certName | No | String | New server certificate name of the load balancer layer-7 listener. |
| certContent | No | String | New server certificate content of the load balancer layer-7 listener. |
| certKey | No | String | New server certificate key of the load balancer layer-7 listener. |
| certCaId | No | String | New client certificate ID of the load balancer layer-7 listener. |
| certCaName | No | String | New client certificate name of the load balancer layer-7 listener. |
| certCaContent | No | String | New client certificate content of the load balancer layer-7 listener. |
| bandwidth| No | Int | New maximum bandwidth of the listener. Available value range: 0-1000 (in Mbps). |


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
| -12000 | InvalidL7Listener.NotExist | The layer-7 listener does not exist in CCDB |
| -12010 | IncorrectStatus.ListenerWrongStatus | Incorrect load balancer listener status |
| -20002 | InvalidParameter.InvalidCertContent | Invalid certificate content |
| -20000 | InvalidResource.CertPlatformErr | An error occurred while accessing the certificate platform |
| -12020 | InvalidParameter.certNotInValidTime | Certificate is not within the valid time period |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=ModifyBmForwardListener
&<<a href="https://www.qcloud.com/document/product/386/6718">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&listenerName=https-listener
&SSLMode=1
&certId=abcdefgh
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
