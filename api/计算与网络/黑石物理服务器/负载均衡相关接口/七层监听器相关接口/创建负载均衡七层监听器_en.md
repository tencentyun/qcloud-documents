## 1. API Description
 
This API (CreateBmForwardListeners) is used to create BM load balancer layer-7 listeners. A BM load balancer layer-7 listener provides specific rules for forwarding user requests, including parameters such as port, protocol and so on.

Domain for API request: <font style="color:red">bmlb.api.qcloud.com</font>

The rules for configuring listeners are as follows:

Use limits for BM load balancers:
1) Layer-7 listener refers to listener with a protocol type of HTTP/HTTPS, while layer-4 listener refers to listener with a protocol type of TCP/UDP.
2) Layer-4 listener with a protocol type of TCP/UDP is supported by both public network-based load balancers (with daily rate) and private network load balancers.
3) Public network load balancers support layer-7 listeners with protocol type of HTTP/HTTPS, while private network load balancers support layer-7 listeners with protocol type of HTTP.
4) Within the same load balancer, each load balancer port can correspond to a layer-7 listener or a layer-4 listener with TCP protocol, but not both.
5) Within the same load balancer, a load balancer listener can correspond to multiple CPM ports.
6) Within the same load balancer, a CPM port cannot correspond to different layer-4 listeners with the same protocol.


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listeners | Yes | Array | Array containing layer-7 listener information. You can create multiple layer-7 listeners. Currently, you can create up to 50 layer-7 listeners under a load balancer. |

The listeners array is used to describe specific information of current listeners. "n" is subscript, the array includes the following fields

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| listeners.n.loadBalancerPort | Yes | Int | Listening port of load balancer layer-7 listener. Value range: 1-65535. |
| listeners.n.protocol | Yes | String | Protocol type of load balancer layer-7 listener. Available values: http, https. |
| listeners.n.listenerName | Yes | String | Name of load balancer layer-7 listener. |
| listeners.n.SSLMode | No | Int | Authentication method of load balancer layer-7 listener. 0: no authentication, used for HTTP; 1: one-way authentication, used for HTTPS; 2: two-way authentication, used for HTTPS. |
| listeners.n.certId | No | String | Server certificate ID of load balancer layer-7 listener. |
| listeners.n.certName | No | String | Server certificate name of load balancer layer-7 listener. |
| listeners.n.certContent | No | String | Server certificate content of load balancer layer-7 listener. |
| listeners.n.certKey | No | String | Server certificate key of load balancer layer-7 listener. |
| listeners.n.certCaId | No | String | Client certificate ID of load balancer layer-7 listener. |
| listeners.n.certCaName | No | String | Client certificate name of load balancer layer-7 listener. |
| listeners.n.certCaContent | No | String | Client certificate content of load balancer layer-7 listener. |
| listeners.n.bandwidth | No | Int | Used to specify the maximum bandwidth of the listener when billing mode is "bill by fixed bandwidth". Value range: 0-1000 (in Mbps). |



## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| listenerIds | Array | List of unique IDs of the newly created load balancer layer-7 listeners. |


Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |
| 12003 | IncorrectStatus.LBWrongStatus | The operation is impossible due to incorrect status of BM load balancer |
| 12014 | InvalidResource.ListenerNumberOverLimit | The number of layer-7 listeners of this BM load balancer has exceeded the limit |
| -12013 | InvalidParameter.VportIsDuplicate | Listener for this port already exists in this load balancer |
| -20002 | InvalidParameter.InvalidCertContent | Invalid certificate content |
| -20000 | InvalidResource.CertPlatformErr | An error occurred while accessing the certificate platform |
| -12020 | InvalidParameter.certNotInValidTime | Certificate is not within the valid time period |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=CreateBmForwardListeners
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listeners.1.loadBalancerPort=1234
&listeners.1.protocol=http
&listeners.1.listenerName=http-listener
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "listenerIds" : ["lbl-abcdefg"]
}

```
