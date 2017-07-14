## 1. API Description
 
This API (DescribeBmForwardListenerInfo) is used to acquire BM load balancer layer-7 listeners that are bound to a certain CPM or have a certain forwarding domain.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |   ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| searchKey | No | String | Search key, which is used to search for listeners with this forwarding domain using fuzzy search method. |
| instanceIds.n | No | Array | List of CPM IDs or VM IPs, used to acquire listeners that are bound to these CPMs. |
| ifGetRsInfo | No | Int | Indicates whether to acquire information of CPMs under the forwarding rules. Default is 0 (do not acquire). |


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
| listenerName | String | Name of the cloud load balancer layer- listener. |
| protocol | String | Protocol type of load balancer layer-7 listener (HTTP, HTTPS). |
| loadBalancerPort | Int | Listening port of the load balancer layer-7 listener. |
| bandwidth | Int | Maximum bandwidth of the listener when the billing mode is pay-by-fixed bandwidth (in Mbps). |
| listenerType | String | Listener type: L4Listener (layer-4 listener) or L7Listener (layer-7 listener). |
| SSLMode | Int | Authentication method of load balancer layer-7 listener. 0: no authentication, used for HTTP; 1: one-way authentication, used for HTTPS; 2: two-way authentication, used for HTTPS. |
| certId | String | ID of the server certificate associated with the load balancer layer-7 listener. |
| certCaId | String | ID of the client certificate associated with the load balancer layer-7 listener. |
| status | Int | Current status of the listener. 0: Creating; 1: Running; 2: Creation failed; 3: Deleting; 4: Deletion failed. |
| addTimestamp | String | Creation time stamp. |
| ruleSet | Array | List of returned forwarding rules. |

Each sub-item of ruleSet is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| domain | String | Layer-7 forwarding domain name of the load balancer. |
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
| healthSwitch | Int | Indicate whether Health Check is enabled. |
| httpCheckPath | String | Path to be checked in health check. |
| httpCheckDomain | String | Domain to be checked in health check. |
| intervalTime | Int | Time interval between health checks. |
| healthNum | Int | Healthy threshold for health checks. |
| unhealthNum | Int | Unhealthy threshold for health checks. |
| httpCode | Int | This determines which combination of HTTP return codes are considered as healthy in health checks. |
| balanceMode | String | Balance mode. |
| status | Int | Current status of the forwarding path. 0: Creating; 1: Running; 2: Creation failed; 3: Deleting; 4: Deletion failed. |
| addTimestamp | String | Creation time stamp. |
| rsList | Array | List of CPMs bound to the forwarding path. |

Each sub-item of rsList contains the following fields

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


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmForwardListenerInfo
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerId=lb-abcdefgh
&searchKey=a
&ifGetRsInfo=1
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
            "listenerName": "test-http",
            "protocol": "http",
            "loadBalancerPort": 80,
            "bandwidth": 0,
            "listenerType": "L7Listener",
            "SSLMode": 0,
            "certId": "",
            "certCaId": "",
            "status": 1,
            "addTimestamp": "2017-03-09 19:34:45",
            "ruleSet": [
                {
                    "domain": "www.a.com",
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
                            "intervalTime": 30,
                            "healthNum": 3,
                            "unhealthNum": 5,
                            "httpCode": 7,
                            "balanceMode": "wrr",
                            "status": 1,
                            "addTimestamp": "2017-04-25 21:03:40",
                            "rsList": [
                                {
                                    "instanceId": "cpm-abcdefgh",
                                    "alias": "xxx",
                                    "lanIp": "1.1.1.1",
                                    "rsPort": 80,
                                    "weight": 10,
                                    "status": "Dead"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    "totalCount": 1
}

```
