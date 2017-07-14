## 1. API Description
 
This API (DeleteBmForwardRules) is used to delete BM load balancer layer-7 forwarding rules.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the load balancer's layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| domainId | Yes | String | ID of the load balancer's layer-7 forwarding domain, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| locationIds.n | Yes | Array | List of IDs of the load balancer layer-7 forwarding paths. The IDs can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |


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
| -12003 | InvalidForwardRule.NotExist | The forwarding rule does not exist in CCDB |
| -12011 | IncorrectStatus.ForwardRuleWrongStatus | Incorrect load balancer forwarding rule status |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=DeleteBmForwardRules
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&domainId=dm-abcdefgh
&locationIds.1=loc-abcdefgh
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
