## API Description
This API (DescribeForwardLBListeners) is used to query the list of listeners by load balancer ID, listener protocol or port. If you do not specify any filter conditions, the default number (20) of listeners is returned for the load balancer.

Domain name for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeForwardLBListeners.
 
| Parameter Name | Required | Type | Description |
|-----|----|----|------------|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers" target="_blank">DescribeLoadBalancers</a>. |
| listenerIds.n | No | String | ID of application-based cloud load balancer listener. |
| protocol | No | Int | Protocol type of the listener. <br  />1: HTTP, 2: TCP, 3: UDP, 4: HTTPS. |
| loadBalancerPort | No | Int | Port of the load balancer listener. |


## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| listenerSet | Array | Returned array of listeners. |

**"listenerSet" is composed as follows:**

There are two types of structures. The structure for layer-4 listener is as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | ID of application-based load balancer listener. |
| protocol | Int | Protocol of application-based load balancer listener.<br  />1: HTTP, 4: HTTPS. |
| protocolType | String | Protocol type of application-based load balancer listener. |
| loadBalancerPort | Int | Listening port of application-based load balancer listener. |


There are two types of structures. The structure for layer-7 listener is as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | ID of application-based load balancer listener. |
| protocol | Int | Protocol of application-based load balancer listener. 1: HTTP, 2: TCP, 3: UDP, 4: HTTPS. |
| protocolType | String | Protocol type of application-based load balancer listener. |
| loadBalancerPort | Int | Listening port of application-based load balancer listener. |
| SSLMode | String | Verification mode of HTTPS listener. |
| certId | String | Server certificate ID of HTTPS listener. |
| certCaId | String | Client certificate ID of HTTPS listener. |
| rules | Array | Forwarding rule set of application-based load balancer listener. Leave it empty for layer-4 listeners. |

**"rules" is composed as follows:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| locationId | String | Forwarding rule ID. |
| domain | String | Domain name for the forwarding rule. |
| url | String | Path of forwarding rule. |
| sessionExpire | Int | Session persistence duration of forwarding rule. |
| healthSwitch | Int | Health check for forwarding rule. 1: Enable; 0: Disable. |
| intervalTime | Int | Interval between health checks on the forwarding rule. |
| healthNum | Int | Healthy threshold of the forwarding rule. |
| timeOut | Int | Response timeout. This is not applicable for now. |
| unhealthNum | Int | Unhealthy threshold of the forwarding rule. |
| httpHash | String | Forward method of forwarding rule of the application-based load balancer.<br>Available values: wrr (polling by weight), ip_hash (hashing based on the source IP) and least_conn (minimum number of connections). |
| scheduler | String | Forwarding method of the load balancer layer-4 listener. <br>Available values: wrr (polling by weight), least_conn (minimum number of connections). |
| httpCode | Int | Status code of health check. For more information, please see [Create Listener](https://cloud.tencent.com/document/api/214/1255). |
| httpCheckPath | String | Health check path for forwarding rule. |

## Example
 
Request
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeForwardLBListeners
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "listenerSet": [
        {
            "loadBalancerPort": 7,
            "protocol": 1,
            "protocolType": "http",
            "listenerId": "lbl-20cxbf40",
            "rules": [
                {
                    "locationId": "loc-mpoupana",
                    "domain": "www.tencent.com",
                    "url": "/good",
                    "httpHash": "wrr",
                    "sessionExpire": 982,
                    "healthSwitch": 0,
                    "timeOut": 2,
                    "intervalTime": 35,
                    "healthNum": 3,
                    "unhealthNum": 3,
                    "httpCode": 31,
                    "httpCheckPath": "/"
                },
                {
                    "locationId": "loc-fcr98aw2",
                    "domain": "www.tencent.com",
                    "url": "/first",
                    "httpHash": "ip_hash",
                    "sessionExpire": 211,
                    "healthSwitch": 1,
                    "timeOut": 2,
                    "intervalTime": 5,
                    "healthNum": 3,
                    "unhealthNum": 3,
                    "httpCode": 31,
                    "httpCheckPath": "/"
                },
                {
                    "locationId": "loc-hvzwsyqq",
                    "domain": "www.tencent.com",
                    "url": "/third",
                    "httpHash": "ip_hash",
                    "sessionExpire": 211,
                    "healthSwitch": 1,
                    "timeOut": 2,
                    "intervalTime": 5,
                    "healthNum": 3,
                    "unhealthNum": 3,
                    "httpCode": 31,
                    "httpCheckPath": "/"
                },
                {
                    "locationId": "loc-lertoiuk",
                    "domain": "www.zhifubao.com",
                    "url": "/first",
                    "httpHash": "ip_hash",
                    "sessionExpire": 321,
                    "healthSwitch": 1,
                    "timeOut": 2,
                    "intervalTime": 5,
                    "healthNum": 3,
                    "unhealthNum": 3,
                    "httpCode": 31,
                    "httpCheckPath": "/"
                },
                {
                    "locationId": "loc-5mr4zzym",
                    "domain": "www.tencent.com",
                    "url": "/fourth",
                    "httpHash": "ip_hash",
                    "sessionExpire": 211,
                    "healthSwitch": 0,
                    "timeOut": 2,
                    "intervalTime": 5,
                    "healthNum": 3,
                    "unhealthNum": 3,
                    "httpCode": 31,
                    "httpCheckPath": "/"
                },
                {
                    "locationId": "loc-fi5or8js",
                    "domain": "www.zhifubao.com",
                    "url": "/second",
                    "httpHash": "ip_hash",
                    "sessionExpire": 321,
                    "healthSwitch": 1,
                    "timeOut": 2,
                    "intervalTime": 5,
                    "healthNum": 3,
                    "unhealthNum": 3,
                    "httpCode": 31,
                    "httpCheckPath": "/"
                },
                {
                    "locationId": "loc-buq7xfa8",
                    "domain": "www.aws.com",
                    "url": "/second",
                    "httpHash": "ip_hash",
                    "sessionExpire": 321,
                    "healthSwitch": 1,
                    "timeOut": 2,
                    "intervalTime": 5,
                    "healthNum": 3,
                    "unhealthNum": 3,
                    "httpCode": 31,
                    "httpCheckPath": "/"
                }
            ]
        },
        {
            "loadBalancerPort": 9999,
            "protocol": 4,
            "protocolType": "https",
            "listenerId": "lbl-7honivdy",
            "SSLMode": "unidirectional",
            "certId": "cb5fb6cd"
        },
        {
            "loadBalancerPort": 80,
            "protocol": 4,
            "protocolType": "https",
            "listenerId": "lbl-qbmhv8a4",
            "SSLMode": "unidirectional",
            "certId": "c5db1460"
        },
        {
            "loadBalancerPort": 90,
            "protocol": 4,
            "protocolType": "https",
            "listenerId": "lbl-gdbnbl5a",
            "SSLMode": "unidirectional",
            "certId": "c5db1460"
        },
        {
            "loadBalancerPort": 100,
            "protocol": 4,
            "protocolType": "https",
            "listenerId": "lbl-3m99yc3u",
            "SSLMode": "unidirectional",
            "certId": "c5db1460"
        }
    ]
}

```





