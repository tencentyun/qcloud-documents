## API Description
Domain name: `lb.api.qcloud.com`
API name: `AutoRewrite`

Automatic redirect only supports HTTPS port 443. It automatically generates an HTTP port 80 and redirects it to HTTPS port 443.

## Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of load balancer instance. It can be queried by entering 1 or -1 in input parameter "forward" field through the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of load balancer listener, which can be queried via the API DescribeForwardLBListeners. |
| domains | No | Array | Domain name to be redirected. Batch operations are supported. |

## Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed. |
| message | String | Error message. |
| codeDesc | String | Error code at business side. For a successful operation, "Success" is returned. In case of an error, a message describing the reason for the error is returned. |
| requestId | Int | ID of asynchronous task of automatic redirect. The execution result can be queried using the API for querying asynchronous task. |

## Example

Input
```
https://lb.api.qcloud.com/v2/index.php?Action=AutoRewrite
&<Common request parameters>
&loadBalancerId=lb-6efswuxa
&listenerId=lbl-20cxbf40
&domains.0=www.xxx.com
```
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 28078
}
```

