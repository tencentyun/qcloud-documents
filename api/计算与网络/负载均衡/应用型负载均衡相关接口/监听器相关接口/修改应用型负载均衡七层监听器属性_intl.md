## API Description
This API (ModifyForwardLBSeventhListener) is used to modify the attributes of application-based load balancer layer-7 listener.
 
Domain name for API access: `lb.api.qcloud.com`


## Request Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is ModifyForwardLBSeventhListener.
 
| Parameter Name | Required | Type | Description |
|-----|------|--------|-----------|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of application-based load balancer listener, which can be queried via the API DescribeForwardLBListeners. |
| listenerName | No | String | Name of application-based load balancer listener. |
| SSLMode | No | String | Verification mode of HTTPS listeners. unidirectional: Unidirectional verification; mutual: Mutual verification. |
| certId | No | String | New server certificate ID of HTTPS listener. |
| certCaId | No | String | New client certificate ID of HTTPS listener. |
| certCaContent | No | String | New client certificate content of HTTPS listener. |
| certCaName | No | String | New client certificate name of HTTPS listener. |
| certContent | No | String | New server certificate content of HTTPS listener. |
| certKey | No | String | New server certificate key of HTTPS listener. |
| certName | No | String | New server certificate name of HTTPS listener. |

## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| requestId | Int | Request task ID. The operation status can be queried via the API [DescribeLoadBalancersTaskResult](https://cloud.tencent.com/document/api/214/4007). |

## Example
 
Request
```
https://lb.api.qcloud.com/v2/index.php?Action=ModifyForwardLBSeventhListener
&<Common request parameters>
&loadBalancerId=lb-ltkip4do
&listenerId=lbl-6hkiqc6c
&SSLMode=unidirectional
```
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 18642
}

```


