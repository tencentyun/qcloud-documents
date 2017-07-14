## 1. API Description
 
This API (CreateBmForwardRules) is used to create BM load balancer layer-7 forwarding rules.

Domain for API request: bmlb.api.qcloud.com

The rules for configuring forwarding rules are as follows:

Forwarding rules created for the same forwarding domain name are merged under the same forwarding domain name

Limits for forwarding domain names:
1) The domain name may contain 1-80 printable ASCII characters.
2) You can use four formats: default domain name format, generic domain name format, wildcard format and regular expression format.
3) Default domain name is represented with "_".
4) You can only use letters, numbers, "-", and "." in a generic domain name.
5) For wildcard format, it must start or end with wildcard "\*".
6) Regular expression starts with "~". Regular expression cannot contain spaces and these symbols: " ' ; ` ~ {}
7) Matching priority for forwarding domain names: Generic domain name > Wildcard format starting with wildcard > Wildcard format ending with wildcard > Regular expression > Default domain name format.


Limits for forwarding paths:
1) The path may contain 1-80 printable ASCII characters.
2) You can use two formats: paths with modifiers and paths without modifiers.
3) A path without modifiers can only contain letters, numbers, "-", ".", "?", "%", "#", "&", "=".
4) A path with modifiers can contain these modifiers: "~", "~\*", "^~", "=". "~" indicates that the following expression is a case-sensitive regular expression; "~\*" indicates that the following expression is a case-insensitive regular expression; "^~" means if the expression is considered as the best match, then no further matching search will be performed; "=" indicates exact match, which means the request is only forwarded if it is exactly the same with the expression.
5) Regular expression cannot contain spaces and these symbols: " ' ; ` ~ {}
6) Matching priority for forwarding domain names: Exact match with the modifier "=" > Prefix match with the modifier "^~" > Regular expressions with the modifier "~" or "~\*" > Formats without modifiers.

Limits for health check forwarding domain names:
1) The format for a health check domain name must be in a generic format
2) A health check domain name must match with forwarding domain name

Use limits for health check forwarding paths:
The format for a health check path must be normal format

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| rules | Yes | Array | Array containing layer-7 forwarding rule information. You can create multiple layer-7 forwarding rules. You can create up to 50 layer-7 forwarding domain names under a layer-7 listener, and up to 100 forwarding rules under a forwarding domain name. |

The "rules" array is used to describe specific information of current listeners. "n" is subscript, the array includes the following fields

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| rules.n.domain | Yes | String | Forwarding domain name of the layer-7 forwarding rules for the load balancer. |
| rules.n.url | Yes | String | Forwarding path of the layer-7 forwarding rules for the load balancer. |
| rules.n.sessionExpire | No | Int | Session persistence duration (in seconds). Available value range: 30-3600. Default value is 0 (disable session persistence). |
| rules.n.healthSwitch | No | Int | Indicate whether to enable health check: 1 (On) and 0 (Off). Default value is 0 (off). |
| rules.n.intervalTime | No | Int | Time interval between health checks. Default value: 30; value range: 30-300 (in seconds). |
| rules.n.healthNum | No | Int | Healthy threshold for health checks. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: count. |
| rules.n.unhealthNum | No | Int | Unhealthy threshold for health checks. Default value is 5, which means the forwarding is considered abnormal if it is detected to be unhealthy for five times consecutively. Value range: 2-10; unit: count. |
| rules.n.httpCode | No | Int | This determines which combination of HTTP return codes are considered as healthy in health checks. Value range: 0-31. For example, the value 7 means the health check result is considered healthy if HTTP return code is 1xx, 2xx or 3xx. |
| rules.n.httpCheckPath | No | String | Path to be checked in the health check. |
| rules.n.httpCheckDomain | No | String | Domain name to be checked in the health check. |
| rules.n.balanceMode | No | String | Balance mode: ip_hash, wrr. Default is wrr. |



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
| -12011 | IncorrectStatus.ForwardRuleWrongStatus | Incorrect load balancer forwarding rule status |
| -12007 | InvalidResource.ForwardDomainNumberOverLimit | The number of forwarding domain names of the load balancer listener has exceeded the limit |
| -12008 | InvalidResource.ForwardLocationNumberOverLimit | The number of forwarding paths under the forwarding domain for the load balancer listener has exceeded the limit |
| -12015 | InvalidParameter.ForwardLocationIsDuplicate | The forwarding path already exists for this load balancer |
| -12016 | InvalidParameter.ForwardDomainNotComplianceWithRule | Incorrect forwarding domain format |
| -12017 | InvalidParameter.ForwardLocationNotComplianceWithRule | Incorrect forwarding path format |
| -12019 | InvalidParameter.httpCheckDomainNotMatch | The health check domain name does not match with the forwarding domain name |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=CreateBmForwardListeners
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&rules.1.domain=a.com
&rules.1.url=/
&rules.1.sessionExpire=900
&rules.1.healthSwitch=1
&rules.1.intervalTime=30
&rules.1.healthNum=3
&rules.1.unhealthNum=5
&rules.1.httpCode=7
&rules.1.httpCheckPath=/
&rules.1.httpCheckDomain=a.com
&rules.1.balanceMode=wrr
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
