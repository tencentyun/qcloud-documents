## API Description
This API (GetCertListWithLoadBalancer) is used to query the information of the load balancer associated with certificate.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is GetCertListWithLoadBalancer.
 
| Parameter Name | Required | Type | Description |
|-|-|-|-|
| certIds.n | Yes | String | ID of the certificate to be queried. |


## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| certSet | Array | Certificate is the key, and the value is the information of load balancer and listeners associated with the certificate. |

The returned array certSet is composed as follows:

| Parameter Name | Type | Description |
|-|-|-|-|
| LBName | String | Name of the load balance service. |
| loadBalancerId | String | ID of the load balancer instance. |
| region | String | Region. |
| listener | Array | Listener information. |


The returned array listener is composed as follows:

| Parameter Name | Type | Description |
|-|-|-|-|
| unListenerId | String | Listener ID. |
| listenerName | String | Listener name. |
| loadBalancerPort | Int | Listening port of the listener. |
| instancePort | Int | Service port of the listener's RS. |
| protocol | Int | Protocol of listener. |
| sessionExpire | Int | Session persistence duration. |
| healthSwitch | Int | Whether to enable health check. |
| timeOut | Int | Response timeout. |
| intervalTime | Int | Interval between health checks. |
| healthNum | Int | Healthy threshold. |
| unhealthNum | Int | Unhealthy threshold. |
| httpHash | No | String | Forwarding method of the load balancer layer-7 listener. |
| scheduler | String | Forwarding method of the load balancer layer-4 listener. |
| httpCode | Int | This returned code is used to determine the health status of HTTP and HTTPS listeners. |
| SSLMode | String | Verification mode of the HTTPS listener. |
| certId | String | New server certificate ID of the HTTPS listener. |
| certCaId | String | New client certificate ID of the HTTPS listener. |

## Example
 
Request
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancers
&<Common request parameters>
certIds.0=4b9fc92b
```

Response
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


