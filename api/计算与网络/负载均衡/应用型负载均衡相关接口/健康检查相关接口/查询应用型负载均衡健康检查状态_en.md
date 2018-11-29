## 1. API Description
 API DescribeForwardLBHealthStatus is used to query the health check result of application-based cloud load balancer instances.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeForwardLBHealthStatus.

| Parameter Name | Required | Type | Description |	 
|-|-|-|-|
| loadBalancerIds.n | Yes | String | Uniform ID of application-based cloud load balancer instance, i.e. unLoadBalancerId. It can be queried by entering 1 or -1 in input parameter "forward" field of API <a href="https://cloud.tencent.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |


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
| loadBalancerName | String | Name of cloud load balancer. |
| unLoadBalancerId | String | Uniform ID of the cloud load balancer. |
| listener | Array | Listener array. |

**listener Array Structure:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | ID of application-based cloud load balancer listener. |
| protocol | Int | Protocol type of application-based cloud load balancer listener. 1: HTTP, 4: HTTPS. |
| loadBalancerPort | Int | Listening port of the application-based cloud load balancer listener. |
| listenerName | String | Name of application-based cloud load balancer listener. |
| rules | Array | Forwarding rule set of application-based cloud load balancer listener. |

**rules Array Structure:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| locationId | String | ID of forwarding rule of application-based cloud load balancer listener. |
| domain | String | Domain for the forwarding rule of application-based cloud load balancer listener. |
| url | String | Path of the forwarding rule of application-based cloud load balancer listener. |
| backends | Array | Backend CVM array. |

**backends Array Structure:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| ip | String | Private IP of CVM. |
| port | Int | Service port of CVM. |
| healthStatus | Int | Health check result. 1: healthy; 0: unhealthy |


## 4. Example

Input:
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeForwardLBHealthStatus
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
```
Output:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "loadBalancerName": "123",
            "unLoadBalancerId": "lb-6efswuxa",
            "listener": [
                {
                    "listenerId": "lbl-fh7o7b9o",
                    "listenerName": "lna",
                    "protocol": 1,
                    "loadBalancerPort": 9090,
                    "rules": [
                        {
                            "locationId": "loc-3n8v5uy6",
                            "domain": "*.alibaba.com",
                            "url": "/second",
                            "backends": [
                                {
                                    "ip": "172.17.8.4",
                                    "port": 80,
                                    "healthStatus": 1
                                }
                            ]
                        },
                        {
                            "locationId": "loc-7h3nl8dc",
                            "domain": "*.alibaba.com",
                            "url": "/first",
                            "backends": [
                                {
                                    "ip": "172.17.8.4",
                                    "port": 80,
                                    "healthStatus": 1
                                }
                            ]
                        },
                        {
                            "locationId": "loc-3mkbad8s",
                            "domain": "~^.baidu.com",
                            "url": "/second",
                            "backends": [
                                {
                                    "ip": "172.17.8.4",
                                    "port": 80,
                                    "healthStatus": 1
                                }
                            ]
                        },
                        {
                            "locationId": "loc-pt6nsy2q",
                            "domain": "~^.domain.edu.cn$",
                            "url": "/1234&#",
                            "backends": [
                                {
                                    "ip": "172.17.8.4",
                                    "port": 80,
                                    "healthStatus": 1
                                }
                            ]
                        },
                        {
                            "locationId": "loc-h3wu30tc",
                            "domain": ".emaoe.com",
                            "url": "/1234&#",
                            "backends": [
                                {
                                    "ip": "172.17.8.4",
                                    "port": 80,
                                    "healthStatus": 1
                                }
                            ]
                        },
                        {
                            "locationId": "loc-78ifmow4",
                            "domain": ".example.com",
                            "url": "/1234&#",
                            "backends": [
                                {
                                    "ip": "172.17.8.4",
                                    "port": 80,
                                    "healthStatus": 1
                                }
                            ]
                        },
                    ]
                }
            ]
        }
    ]
}
```
