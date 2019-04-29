## API Description
This API (DescribeLoadBalancerLog) is used to query the application-level log of a load balancer, which is applicable to the public network-based load balancers with HTTP and HTTPS listeners.
 
Domain name for API access: `lb.api.qcloud.com`

API description: The API can be used to query the forwarding logs of a load balancer over the last three days, including logs forwarded to the RS and those directly returned from the load balancer due to RS exception. Interval between requests does not exceed one day.

## Request Parameters

 The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeLoadBalancerLog.
 
| Parameter Name | Required | Type | Description |
|-|-|-|-|
| loadBalancerId | Yes | String | ID of load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| order | No | String | Order of logs sorted by timestamp. Values range: desc and asc. Default is desc. |
| startTime | No | Int | Start time of log query (Unix timestamp). Default is 5 minutes prior to endTime. |
| endTime | No | Int | End time of log query (Unix timestamp). Default is the current timestamp. |
| offset | No | Int | Log offset. Value range: [0,10000]. |
| limit | No | Int | Number of logs. Value range: [0,500]. |
| filter | No | Array | Filter condition for logs in key-value pairs. Specific fields are shown as follows. |


Available values for the key of filter array:

| Parameter Name | Required | Type | Description |
|-|-|-|-|
| status | No | Int | The status code returned to the client is value. |
| status_not | No | Int | The status code returned to the client is not value. |
| server_name | No | String | The requested matching host is value. |
| server_name_not | No | String | The requested matching host is not value. |
| http_host | No | String | The requested host is value. |
| http_host | No | String | The requested host is not value. |
| remote_addr | No | String | The requested client IP is value. |
| remote_addr_not | No | String | The requested client IP is not value. |
| request_time_less_than | No | String | Time of processing request is less than value, which is valid when it is passed along with request_time_greater_than. |
| request_time_greater_than | No | String | Time taken to process request is greater than value, which is valid when it is passed along with request_time_less_than. |




## Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code. 0: Successful; other values: Failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/api/214/1530) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned. |
| logInfo | Json | Information of the returned log. |

logInfo format:

| Parameter Name | Type | Description |
|-|-|-|
| logList | Array | Log array. |
| total | Int | Total number of logs. |

"logList" is composed as follows:

| No. | Parameter Name | Type | Description |
|-|-------|---|---------------|
| 1 | server_name | String | The server_name of rule. |
| 2 | request | String | Request line. |
| 3 | remote_addr | String | Client IP. |
| 4 | upstream_addr | String | RS information. |
| 5 | upstream_header_time | String | Time taken to receive all HTTP headers from RS. |
| 6 | connection_requests | Int | The current number of requests made through a connection. |
| 7 | ssl_handshake_time | String | Time for SSL handshake. |
| 8 | ssl_cipher | String | Encryption suite. |
| 9 | ssl_protocol | String | SSL protocol version. |
| 10 | ssl_session_reused | String | SSL session reuse. |	
| 11 | time_local | String | Local time. |
| 12 | http_host | String | Domain name for request. |
| 13 | server_addr | String | Destination IP for request. |
| 14 | bytes_sent | Int | Bytes sent to the client. |
| 15 | upstream_status | String | RS status. |
| 16 | protocol_type | String | Protocol type (http/https/spdy/http2/ws/wss). |
| 17 | request_time | Int | Time taken to process request. |
| 18 | upstream_connect_time | Int | Time taken to establish TCP connection with RS (in sec). |
| 19 | request_length | Int | Length of the request received from client (in Bytes). |
| 20 | tcpinfo_rtt | Int | RTT for TCP connection (in ms). |
| 21 | upstream_response_time | Int | Time taken to receive response from RS (in sec). |
| 22 | status | String | Status code returned for a request. Status code is 200 if no RS exists. |
| 23 | http_user_agent | String | user_agent. |



## Example
 
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancerLog
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-7wdcqme9
&filter.0.key=status
&filter.0.value=200
&filter.1.key=server_name
&filter.1.value=www.qq.com
</pre>
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "logInfo": {
        "logList": [
            {
                "server_name": "www.qq.com",
                "request": "GET / HTTP/1.1",
                "remote_addr": "119.28.138.187",
                "upstream_addr": "-",
                "upstream_header_time": "-",
                "connection_requests": 1,
                "ssl_cipher": "-",
                "remote_port": "40554",
                "time_local": "02/Nov/2017:12:03:13 +0800",
                "http_host": "115.159.132.241",
                "server_addr": "115.159.132.241",
                "bytes_sent": 239,
                "upstream_status": "-",
                "protocol_type": "http",
                "ssl_handshake_time": "-",
                "request_time": 0,
                "upstream_connect_time": "-",
                "request_length": 79,
                "ssl_session_reused": "-",
                "tcpinfo_rtt": 38000,
                "upstream_response_time": "-",
                "ssl_protocol": "-",
                "status": "200"
            }
        ],
        "total": 3918
    }
}

```

