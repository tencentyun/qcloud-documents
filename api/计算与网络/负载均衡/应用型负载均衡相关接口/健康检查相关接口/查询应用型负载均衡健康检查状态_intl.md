## API Description
This API (DescribeForwardLBHealthStatus) is used to query the health check result of application-based load balancer instances.

Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeForwardLBHealthStatus.

| Parameter Name | Required | Type | Description |	 
|-|-|-|-|
| loadBalancerIds.n | Yes | String | ID of application-based load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. The maximum number of load balancers is limited to 30 for this API. |



## Response Parameters


| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| data | Array | Returned array. |

**"data" is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| loadBalancerName | String | Name of load balancer. |
| loadBalancerId | String | ID of load balancer. |
| unLoadBalancerId | String | ID of load balancer, which is the same as loadBalancerId. |
| listener | Array | Listener array. |

**"listener" is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | ID of application-based load balancer listener. |
| protocol | Int | Protocol type of application-based load balancer listener. 1: HTTP, 4: HTTPS. |
| loadBalancerPort | Int | Listening port of application-based load balancer listener. |
| listenerName | String | Name of application-based load balancer listener. |
| rules | Array | Forwarding rule set of application-based load balancer listener. |

**"rules" is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| locationId | String | ID of forwarding rule of the application-based load balancer listener. |
| domain | String | Domain name of forwarding rule of the application-based load balancer listener. |
| url | String | Path of forwarding rule of the application-based load balancer listener. |
| backends | Array | Backend CVM array. |

**"backends" is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| ip | String | Private IP of CVM. |
| port | Int | Service port of CVM. |
| healthStatus | Int | Health check result. 1: Healthy; 0: Unhealthy. |


## Example

Request
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeForwardLBHealthStatus
&<Common request parameters>
&loadBalancerIds.0=lb-6efswuxa
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "loadBalancerName": "123",
			"loadBalancerId": "lb-6efswuxa",
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
