## 1. API Description
 
This API (ModifyBmForwardLocation) is used to modify BM load balancer layer-7 forwarding paths.

Domain for API request: bmlb.api.qcloud.com

The rules for configuring forwarding rules are as follows:

Forwarding rules created for the same forwarding domain name are merged under the same forwarding domain name

Use limits for forwarding domain names:
1) The domain name may contain 1-80 printable ASCII characters.
2) You can use four formats: default domain name format, generic domain name format, wildcard format and regular expression format.
3) Default domain name is represented with "_".
4) You can only use letters, numbers, "-", and "." in a generic domain name.
5) For wildcard format, it must start or end with wildcard "\*".
6) Regular expression starts with "~". Regular expression cannot contain spaces and these symbols: " ' ; ` ~ {}
7) Matching priority for forwarding domain names: Generic domain name format > Wildcard format starting with wildcard > Wildcard format ending with wildcard > Regular expression > Default domain name format.


Use limits for forwarding paths:
1) The path may contain 1-80 printable ASCII characters.
2) You can use two formats: paths with modifiers and paths without modifiers.
3) A path without modifiers can only contain letters, numbers, "-", ".", "?", "%", "#", "&", "=".
4) A path with modifiers can contain these modifiers: "~", "~\*", "^~", "=". "~" indicates that the following expression is a case-sensitive regular expression; "~\*" indicates that the following expression is a case-insensitive regular expression; "^~" means if the expression is considered as the best match, then no further matching search will be performed; "=" indicates exact match, which means the request is only forwarded if it is exactly the same with the expression.
5) Regular expression cannot contain spaces and these symbols: " ' ; ` ~ {}
6) Matching priority for forwarding domain names: Exact match with the modifier "=" > Prefix match with the modifier "^~" > Regular expressions with the modifier "~" or "~\*" > Formats without modifiers.

Use limits for health check forwarding domain names:
1) The format for a health check domain name must be a generic one
2) A health check domain name must match the forwarding domain name

Use limits for health check forwarding paths:
The format for a health check path must be a generic format

## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| rules | Yes | Array | Array containing the layer-7 forwarding rule information to be updated. |

The "rules" array is used to describe specific information of current listeners. "n" is subscript, the array includes the following fields

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| rules.n.domainId | Yes | String | ID of the load balancer's layer-7 forwarding domain name, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| rules.n.locationId | Yes | String | ID of the load balancer's layer-7 forwarding path, which can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |
| rules.n.url | No | String | New forwarding path. |
| rules.n.sessionExpire | No | Int | New session persistence duration (in seconds). Available value range: 30-3600. Default value is 0 (disable session persistence). |
| rules.n.healthSwitch | No | Int | Health check switch: 1 (On) and 0 (Off). Default value is 0 (off). |
| rules.n.intervalTime | No | Int | New time interval between health checks. Default value: 30; value range: 30-300 (in seconds). |
| rules.n.healthNum | No | Int | New healthy threshold for health checks. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: count. |
| rules.n.unhealthNum | No | Int | New unhealthy threshold for health checks. Default value is 5, which means the forwarding is considered abnormal if it is detected to be unhealthy for five times consecutively. Value range: 2-10; unit: count. |
| rules.n.httpCode | No | Int | New healthy HTTP code combination. This determines which combination of HTTP return codes are considered as healthy in health checks. Value range: 0-31. For example, the value 7 means the health check result is considered healthy if HTTP return code is 1xx, 2xx or 3xx. |
| rules.n.httpCheckPath | No | String | New path to be checked in health check. |
| rules.n.httpCheckDomain | No | String | New domain to be checked in health check. |
| rules.n.balanceMode | No | String | New balance mode: ip_hash, wrr. Default is wrr. |



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
| -12015 | InvalidParameter.ForwardLocationIsDuplicate | The forwarding path already exists for this load balancer |
| -12017 | InvalidParameter.ForwardLocationNotComplianceWithRule | Incorrect forwarding path format |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=ModifyBmForwardLocation
&<<a href="https://www.qcloud.com/document/product/386/6718">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&rules.1.domainId=dm-abcdefgh
&rules.1.locationId=loc-abcdefgh
&rules.1.url=/a
&rules.1.sessionExpire=1000
&rules.1.healthSwitch=0
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
