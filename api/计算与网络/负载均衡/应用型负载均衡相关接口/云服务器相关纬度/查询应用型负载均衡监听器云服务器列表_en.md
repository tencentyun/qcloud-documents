## 1. API Description
 API DescribeForwardLBBackends is used to query the list of backend CVMs bound to the cloud load balancer.
 
Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeForwardLBBackends.

| Parameter Name | Required | Type | Description |	 
|-|-|-|-|
| loadBalancerId | Yes | String | Uniform ID of cloud load balancer instance, i.e. unLoadBalancerId. It can be queried by entering 1 or -1 in input parameter "forward" field of API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerIds.n | No | String | ID of application-based cloud load balancer listener. It can be queried through API DescribeForwardLBListeners. |
| protocol | No | Int | Protocol type of listener. <br>1: HTTP, 4: HTTPS. |
| loadBalancerPort | No | Int | Port of the cloud load balancer listener. |

## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| data | Array | Returned array. |

**data Array Structure:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | Listener ID. |
| protocol | Int | Protocol of listener. |
| protocolType | Int | Protocol type of listener. For example, http. |
| loadBalancerPort | Int | Listening port of listener. |
| rules | Array | Forwarding rule set of layer-7 listener. |

**rules Array Structure:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| locationId | String | ID of forwarding rule. |
| domain| String | Domain for the forwarding rule. |
| url| String | Path of forwarding rule. |
| backends | Array | Information on backend CVMs. |

**backends Array Structure:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| lanIp | String | Private IP of CVM. |
| wanIpSet | Array | Public IP of CVM. | |
| port | Int | Service port of CVM. |
| weight | Int | Weight of CVM. |
| instanceStatus | Int | Status of CVM. |
| unInstanceId | String | CVM ID. |
| instanceName |String| CVM name | |
| addTimestamp | String | Time at which the CVM is bound. |





## 4. Example

Input:
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeForwardLBBackends
&<Common request parameters>
&loadBalancerId=lb-abcdefgh
```
Output:
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


