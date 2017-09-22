## 1. API Description
 GetCertListWithLoadBalancer API is used to query which listeners of cloud load balancer are associated with the certificate.
 
Domain for API access: lb.api.qcloud.com


## 2. Request Parameters

   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is GetCertListWithLoadBalancer.
 
| Parameter Name | Required | Type | Description |
|-|-|-|-|
| certIds.n | Yes | String | ID of the certificate to be queried. |

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



