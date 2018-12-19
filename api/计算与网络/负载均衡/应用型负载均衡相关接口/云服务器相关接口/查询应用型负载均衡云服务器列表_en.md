## API Description
This API (DescribeForwardLBBackends) is used to query the list of backend CVMs bound to an application CLB.
 
Domain name for API access: `lb.api.qcloud.com`

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeForwardLBBackends.

| Parameter | Required | Type | Description |	 
|-|-|-|-|
| loadBalancerId | Yes | String | ID of the cloud load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerIds.n | No | String | ID of application-based cloud load balancer listener. It can be queried through API DescribeForwardLBListeners. |
| protocol | No | Int | Protocol type of the listener. 1: HTTP, 2: TCP, 3: UDP, 4: HTTPS. |
| loadBalancerPort | No | Int | Port of the cloud load balancer listener. |

## Output Parameters
 
 
| Parameter | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on APIs. |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| data | Array | Returned array. |

**`data` is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | Listener ID. |
| protocol | Int | Protocol type of the listener. 1: HTTP, 2: TCP, 3: UDP, 4: HTTPS. |
| protocolType | String | Protocol type of listener. For example, HTTP. |
| loadBalancerPort | Int | Listening port of listener. |
| rules | Array | Forwarding rule set of Layer-7 listener. |
| backends | Array | CVM information of Layer-4 listener |

**`rules` is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| locationId | String | ID of forwarding rule. |
| domain| String | Domain name for the forwarding rule. |
| url | String | Path of forwarding rule. |
| backends | Array | Information on backend CVMs. |

**`backends` is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| lanIp | String | Private IP of CVM. |
| wanIpSet | Array | Public IP of CVM. |
| port | Int | Service port of CVM. |
| weight | Int | Weight of CVM. |
| instanceStatus | Int | Status of CVM. |
| unInstanceId | String | CVM ID. |
| instanceName | String| CVM name |
| addTimestamp | String | Time at which the CVM is bound. |





## Example

Request
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeForwardLBBackends
&<Common request parameters>
&loadBalancerId=lb-abcdefgh
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "loadBalancerPort": 80,
            "protocol": 1,
            "protocolType": "http",
            "listenerId": "lbl-fh7o7bgt",
            "rules": [
                {
                    "locationId": "loc-7w5sp6wf",
                    "backends": [
                        {
                            "instanceName": "Cloud automated testing machine. Do not delete",
                            "lanIp": "10.212.199.17",
                            "wanIpSet": [
                                "45.113.71.7"
                            ],
                            "instanceStatus": 0,
                            "port": 80,
                            "weight": 10,
                            "unInstanceId": "ins-42lrdi7x",
                            "addTimestamp": "2016-11-03 11:21:38"
                        },
                        {
                            "instanceName": "Cloud automated testing machine. Do not delete",
                            "lanIp": "10.212.199.17",
                            "wanIpSet": [
                                "45.113.71.7"
                            ],
                            "instanceStatus": 0,
                            "port": 443,
                            "weight": 10,
                            "unInstanceId": "ins-42lrdi7x",
                            "addTimestamp": "2016-11-03 11:21:38"
                        }
                    ],
                    "domain": "www.baidu.com",
                    "url": "/second"
                },
                {
                    "locationId": "loc-3n8v5v5b",
                    "backends": [
                        {
                            "instanceName": "Cloud automated testing machine. Do not delete",
                            "lanIp": "10.212.199.17",
                            "wanIpSet": [
                                "45.113.71.7"
                            ],
                            "instanceStatus": 0,
                            "port": 80,
                            "weight": 10,
                            "unInstanceId": "ins-42lrdi7x",
                            "addTimestamp": "2016-11-03 11:21:38"
                        },
                        {
                            "instanceName": "Cloud automated testing machine. Do not delete",
                            "lanIp": "10.212.199.17",
                            "wanIpSet": [
                                "45.113.71.7"
                            ],
                            "instanceStatus": 0,
                            "port": 443,
                            "weight": 10,
                            "unInstanceId": "ins-42lrdi7x",
                            "addTimestamp": "2016-11-03 11:21:38"
                        }
                    ],
                    "domain": "www.baidu.com",
                    "url": "/first"
                }
            ]
        }
    ]
}
```


