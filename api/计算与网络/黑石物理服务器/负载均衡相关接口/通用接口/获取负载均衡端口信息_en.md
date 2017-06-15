## 1. API Description
 
This API (DescribeBmVportInfo) is used to acquire the information on the BM load balancer ports.

Domain for API request: <font style="color:red">bmlb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of the load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| listenerSet | Array | List of returned listeners (4-layer and 7-layer). |

Each sub-item of listensetSet is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| listenerId | String | ID of the load balancer listener. |
| listenerName | String | Name of the load balancer listener. |
| protocol | String | Protocol type of load balancer listener (HTTP, HTTPS, TCP, UDP) |
| loadBalancerPort | Int | Listening port of the load balancer listener. |
| bandwidth | Int | Maximum bandwidth of the listener when the billing mode is pay-by-fixed bandwidth (in Mbps). |
| status | Int | Current status of the listener. 0: Creating; 1: Running; 2: Creation failed; 3: Deleting; 4: Deletion failed. |

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this load balancer does not exist in CCDB |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmVportInfo
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
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
            "status": 1,
        }
    ],
    "totalCount": 1
}

```
