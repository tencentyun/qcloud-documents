## 1. API Description
 GetCertListWithLoadBalancer API is used to query which listeners of cloud load balancer are associated with the certificate.
 
Domain for API access: lb.api.qcloud.com


## 2. Request Parameters

   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is GetCertListWithLoadBalancer.
 
| Parameter Name | Required | Type | Description |
|-|-|-|-|
| certIds.n | Yes | String | ID of the certificate to be queried. |
| loadBalancerId | Yes | String | The ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of the cloud load balancer listener, which can be listenerId or unListenerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E8%8E%B7%E5%8F%96%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9B%91%E5%90%AC%E5%99%A8%E5%88%97%E8%A1%A8" title=" DescribeLoadBalancerListeners">DescribeLoadBalancerListeners</a>. |
| listenerName | No | String | Listener name. |
| sessionExpire | No | Int | Session duration. 0 means disabled. <br>Value range for listeners with TCP or UDP protocols on public network (with daily rate): 900-3600; <br>Value range for listeners with HTTP protocols on public network (without daily rate): 900-3600; <br>Value range for listeners with HTTP or HTTPS protocols on public network (with daily rate): 30-3600; <br>Not supported for private network cloud load balancers. |
| healthSwitch | No | Int | Indicate whether to enable Health Check: 1 (On) and 0 (Off). |
| timeOut | No | Int | Response timeout. Value range: 2-60 seconds; <br> Currently you cannot configure response timeout for listeners with HTTP or HTTPS protocols on public network (with daily rate). Default is 5 seconds. |
| intervalTime | No | Int | Health check time interval, value range: 5-300, <br> Value range of health check time interval for listeners with HTTP or HTTPS protocols on public network (with daily rate): 30-300. |
| healthNum | No | Int | Healthy threshold. Value range: 2-10. |
| unhealthNum | No | Int | Unhealthy threshold. Value range: 2-10. |
| httpHash | No | Int | Forwarding method of cloud load balancer listeners. This field is only supported for HTTP or HTTPS listeners on the public network with daily rate. Available values: wrr (weighted round robin), <br>ip_hash (IP_HASH). Default is wrr. |
| httpCode | No | Int | For HTTP and HTTPS listeners, this returned code is used to determine health status. Value range: 1-31. Default is 31. <br>1: it is considered healthy if the health check returns `1xx` codes; 2: it is considered healthy if the health check returns `2xx` codes; 4: it is considered healthy if the health check returns `3xx` codes; 8: it is considered healthy if the health check returns `4xx` codes; 16: it is considered healthy if the health check returns `5xx` codes. <br>If there should be multiple types of codes that can indicate healthy status, enter the accumulated value corresponding to such codes. |
| httpCheckPath | No | String | Health check path for HTTP or HTTPS listeners. Default is `/`. Path must start with `/`. |
| SSLMode | No | String | Authentication type of https protocols. <br>unidirectional: unidirectional authentication; mutual: mutual authentication. <br><font color="red">This option is mandatory for HTTPS listeners. </font>|
| certId | No | String | New server certificate ID of HTTPS listeners. |
| certCaId | No | String | New client certificate ID of HTTPS listeners. |
| certCaContent | No | String | New client certificate content of HTTPS listeners. |
| certCaName | No | String | New client certificate name of HTTPS listeners. |
| certContent | No | String | New server certificate content of HTTPS listeners. |
| certKey | No | String | New server certificate key of HTTPS listeners. |
| certName | No | String | New server certificate name of HTTPS listeners. |

## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| certSet | Array | Certificate is key, value is the information of cloud load balancer and listeners associated with the certificate. |

Content of returned certSet array:

| Parameter Name | Type | Description |
|-|-|-|-|
| LBName | String | Name of the cloud load balance service. |
| loadBalancerId | String | ID of the cloud load balancer instance. |
| region | String | The region. |
| listener | Array | Listener information. |


Content of the returned listener array

| Parameter Name | Type | Description |
|-|-|-|-|
| unListenerId | String | Listener ID. |
| listenerName | String | Listener name. |
| loadBalancerPort | Int | Listening port of the listener. |
| instancePort | Int | Service port of the listener backend server. |
| protocol | Int | Listener protocol. |
| sessionExpire | Int | Session duration. |
| healthSwitch | Int | Indicate whether Health Check is enabled. |
| timeOut | Int | Response timeout. |
| intervalTime | Int | Health check time interval. |
| healthNum |Int | Healthy threshold. |
| unhealthNum | Int | Unhealthy threshold. |
| httpHash | Int | Forwarding method of cloud load balancer listeners. |
| httpCode | Int | For HTTP and HTTPS listeners, this returned status code is used to determine health status. |
| SSLMode | String | Authentication type of the HTTPS listener. |
| certId | String | New server certificate ID of the HTTPS listener. |
| certCaId | String | New client certificate ID of the HTTPS listener. |

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=GetCertListWithLoadBalancer
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
certIds.0=4b9fc92b
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "certSet": {
        "4b9fc92b": [
            {
                "LBName": "ad",
                "loadBalancerId": "lb-ltkip4do",
                "region": "gz",
                "listener": [
                    {
                        "unListenerId": "lbl-6hkiqc6c",
                        "listenerName": "teaa",
                        "loadBalancerPort": 80,
                        "instancePort": 80,
                        "protocol": 4,
                        "SSLMode": "unidirectional",
                        "certId": "4b9fc92b",
                        "certCaId": "",
                        "sessionExpire": 0,
                        "healthSwitch": 1,
                        "timeOut": 6,
                        "intervalTime": 6,
                        "healthNum": 3,
                        "unhealthNum": 3,
                        "httpHash": "ip_hash",
                        "httpCode": 15
                    }
                ]
            },
            {
                "LBName": "ad",
                "loadBalancerId": "lb-ltkip4do",
                "region": "sh",
                "listener": [
                    {
                        "unListenerId": "lbl-6hkiqc6c",
                        "listenerName": "teaa",
                        "loadBalancerPort": 80,
                        "instancePort": 80,
                        "protocol": 4,
                        "SSLMode": "unidirectional",
                        "certId": "4b9fc92b",
                        "certCaId": "",
                        "sessionExpire": 0,
                        "healthSwitch": 1,
                        "timeOut": 6,
                        "intervalTime": 6,
                        "healthNum": 3,
                        "unhealthNum": 3,
                        "httpHash": "ip_hash",
                        "httpCode": 15
                    }
                ]
            }
        ]
    }
}

```



