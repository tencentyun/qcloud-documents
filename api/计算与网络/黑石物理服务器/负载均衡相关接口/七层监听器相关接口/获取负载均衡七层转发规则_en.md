## 1. API Description
 
This API (DescribeBmForwardRules) is used to acquire BM load balancer layer-7 forwarding rules.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerId | Yes | String | ID of the load balancer's layer-7 listener, which can be queried via API [DescribeBmForwardListeners](/document/product/386/9283). |
| domainIds.n | No | Array | List of IDs of the load balancer layer-7 forwarding domains. The IDs can be queried via API [DescribeBmForwardRules](/document/product/386/9285). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| ruleSet | Array | List of returned forwarding rules. |

Each sub-item of ruleSet contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| domain | String | layer-7 forwarding domain name of the load balancer. |
| domainId | String | ID of layer-7 forwarding domain of the load balancer. |
| status | Int | Current status of the forwarding domain. 0: Creating; 1: Running; 2: Creation failed; 3: Deleting; 4: Deletion failed. |
| addTimestamp | String | Creation time stamp. |
| locations | Array | List of forwarding paths under the forwarding domain. |

Each sub-item of locations contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| url | String | Forwarding path of the layer-7 forwarding rules for the load balancer. |
| locationId | String | ID of layer-7 forwarding path of the load balancer. |
| sessionExpire | Int | Session duration. |
| healthSwitch | Int | Indicates whether Health Check is enabled. |
| httpCheckPath | String | Path to be checked in health check. |
| httpCheckDomain | String | Domain to be checked in health check. |
| intervalTime | Int | Time interval between health checks. |
| healthNum | Int | Healthy threshold for health checks. |
| unhealthNum | Int | Unhealthy threshold for health checks. |
| httpCode | Int | This determines which combination of HTTP return codes are considered as healthy in health checks. |
| balanceMode | String | Balance mode. |
| status | Int | Current status of the forwarding path. 0: Creating; 1: Running; 2: Creation failed; 3: Deleting; 4: Deletion failed. |
| addTimestamp | String | Creation time stamp. |


Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmForwardRules
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&domainIds.1=dm-abcdefgh
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "ruleSet": [
        {
            "domain": "a.com",
            "domainId": "dm-abcdefgh",
            "status": 1,
            "addTimestamp": "2017-04-25 21:03:40",
            "locations": [
                {
                    "url": "/",
                    "locationId": "loc-abcdefgh",
                    "sessionExpire": 0,
                    "healthSwitch": 1,
                    "httpCheckPath": "/",
                    "httpCheckDomain": "a.com",
                    "intervalTime": 30,
                    "healthNum": 3,
                    "unhealthNum": 5,
                    "httpCode": 7,
                    "balanceMode": "wrr",
                    "status": 1,
                    "addTimestamp": "2017-04-25 21:03:40"
                }
            ]
        }
    ],
    "totalCount": 1
}

```
