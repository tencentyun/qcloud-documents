## 1. API Description
 API DescribeForwardLBListeners is used to obtain the list of cloud load balancer listeners by specifying cloud load balancer ID as well as listener's protocol or port as filtering conditions. By default, if you do not specify any filtering conditions, the number of returned listeners will be the default data length under this cloud load balancer (20).

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeForwardLBListeners.
 
| Parameter Name | Required | Type | Description |
|-----|----|----|------------|
| loadBalancerId | Yes | String | Uniform ID of cloud load balancer instance, i.e. unLoadBalancerId. It can be queried by entering 1 or -1 in input parameter "forward" field of API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerIds.n | No | String | ID of application-based cloud load balancer listener. |
| protocol | No | Int | Protocol type of listener. <br>1: HTTP, 4: HTTPS. |
| loadBalancerPort | No | Int | Port of the cloud load balancer listener. |


## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" will be returned. For a failed operation, a message describing the failure will be returned. |
| listenerSet | Array | Returned array of listeners. |

**listenerSet Array Structure:**

There are two types of structures. The structure for layer-4 listener is as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | ID of application-based cloud load balancer listener. |
| protocol | Int | Protocol of application-based cloud load balancer listener. <br>1: HTTP, 4: HTTPS. |
| protocolType | String | Protocol type of the application-based cloud load balancer listener. |
| loadBalancerPort | Int | Listening port of the application-based cloud load balancer listener. |


There are two types of structures. The structure for layer-7 listener is as follows:

| Parameter Name | Type | Description |
|-------|---|---------------|
| listenerId | String | ID of application-based cloud load balancer listener. |
| protocol | Int | Protocol of application-based cloud load balancer listener. 1: HTTP, 4: HTTPS. |
| protocolType | String | Protocol type of the application-based cloud load balancer listener. |
| loadBalancerPort | Int | Listening port of the application-based cloud load balancer listener. |
| SSLMode | String | Authentication mode of HTTPS listener. |
| certId | String | Server certificate ID of HTTPS listener. |
| certCaId | String | Client certificate ID of HTTPS listener. |
| rules | Array | Forwarding rule set of application-based cloud load balancer listener. |

**rules Array Structure:**

| Parameter Name | Type | Description |
|-------|---|---------------|
| locationId | String | ID of forwarding rule. |
| domain| String | Domain for the forwarding rule. |
| url| String | Path of forwarding rule. |
| sessionExpire | Int | Session duration of forwarding rule. |
| healthSwitch | Int | Health check for forwarding rule. 1: Enable; 0: Disable. |
| intervalTime | Int | Time interval by which the check for forwarding rule is made. |
| healthNum |Int | Healthy threshold of forwarding rule. |
| timeOut | Int | Response timeout. This is not applicable currently. |
| unhealthNum |Int | Unhealthy threshold of forwarding rule. |
| httpHash | String | Forwarding method of forwarding rule. wrr refers to polling by weight; ip_hash means delivering the rule based on the accessed source IP by using consistent hashing. |
| httpCode | Int | Status code of health check. For more information about the description of this field, please refer to [Create Listener](/doc/api/244/1255). |
| httpCheckPath | String | Health check path for forwarding rule. |

## 4. Example
 
Input
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeForwardLBListeners
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
```

Output
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



