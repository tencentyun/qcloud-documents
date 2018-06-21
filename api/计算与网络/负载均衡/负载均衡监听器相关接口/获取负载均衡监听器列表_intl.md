## 1. API Description
 This API (DescribeLoadBalancerListeners) is used to query the list of listeners by load balancer ID, listener protocol or port. If you do not specify any filter conditions, the default number (20) of listeners is returned for the load balancer.

Domain name for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](/doc/api/244/4183) page. The Action field for this API is DescribeLoadBalancerListeners.
 
| Parameter Name | Required | Type | Description |
|-----|----|----|------------|
| loadBalancerId | Yes | String | ID of the load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://cloud.tencent.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. | |
| listenerIds.n | No | String | ID of the load balancer listener. |
| protocol | No | Int | Protocol type of the listener. <br>1: HTTP, 2: TCP, 3: UDP, 4: HTTPS. |
| loadBalancerPort | No | Int | Port of the load balancer listener. |
| status | No | Int | Status of the load balancer listener. This field will be ignored if you enter the listener ID for your query. |


## 3. Response Parameters
 
| Parameter Name | Type | Description |
|------|-----|-------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| totalCount | Int | The total number of load balancer instances meeting the filter criteria |
| listenerSet | Array | Returned array of listeners. |

listenerSet is composed as follows:

| Parameter Name | Type | Description |
|--------|-------|-------|
| unListenerId | String | ID of the load balancer listener. |
| loadBalancerPort | Int | Listening port of the load balancer. |
| instancePort | Int | Forwarding port of the listener backend. |
| listenerName | String | Listener name. |
| protocol | Int | Protocol type of the listener. <br>1: HTTP, 2: TCP, 3: UDP, 4: HTTPS. |
| sessionExpire | Int | Session persistence duration. |
| healthSwitch | Int | Indicate whether Health Check is enabled: 1 (On) and 0 (Off). |
| timeOut | Int | Response timeout. |
| intervalTime | Int | Interval between health checks. |
| healthNum | Int | Healthy threshold. |
| unhealthNum | Int | Unhealthy threshold. |  
| httpHash | String | Polling method of public network-based HTTP or HTTPS listeners with static IP. wrr refers to polling by weight; ip_hash means delivering the rule based on the accessed source IP by using consistent hashing. |
| httpCode | Int | Health check return code of public network-based HTTP or HTTPS listeners with static IP. For more information, please see [Create Listener](/doc/api/244/1255). |
| httpCheckPath | String | Health check path of public network-based HTTP or HTTPS listeners with static IP. |
| SSLMode | String | Verification method of public network-based HTTPS listeners with static IP. |
| certId | String | Server certificate ID of public network-based HTTPS listeners with static IP. |
| certCaId | String | Client certificate ID of public network-based HTTPS listeners with static IP. |
| status | Int | Listener status. 0: Creating. 1: Running. |

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancerListeners
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-abcdefgh
&listenerIds.0=lbl-6hkiqc6c
&listenerIds.1=lbl-6wv071ba
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "listenerSet": [
        {
            "loadBalancerPort": 80,
            "instancePort": 80,
            "protocol": 4,
            "status": 1,
            "listenerName": "teaa",
            "unListenerId": "lbl-6hkiqc6c",
            "sessionExpire": 1000,
            "healthSwitch": 1,
            "timeOut": 6,
            "intervalTime": 6,
            "healthNum": 3,
            "unhealthNum": 3,
            "httpCode": 15,
            "httpCheckPath": "/",
            "httpHash": "ip_hash",
            "SSLMode": "mutual",
            "certId": "4b9fc92b",
            "certCaId": "ee4c5590"
        },
        {
            "loadBalancerPort": 777,
            "instancePort": 798,
            "protocol": 4,
            "status": 1,
            "listenerName": "",
            "unListenerId": "lbl-6wv071ba",
            "sessionExpire": 0,
            "healthSwitch": 1,
            "timeOut": 2,
            "intervalTime": 5,
            "healthNum": 3,
            "unhealthNum": 3,
            "httpCode": 31,
            "httpCheckPath": "/",
            "httpHash": "wrr",
            "SSLMode": "mutual",
            "certId": "e2b6d555",
            "certCaId": "dcda0a22"
        }
    ],
    "totalCount": 2
}

```



