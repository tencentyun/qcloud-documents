Cloud load Balancer enables users to store request logs to COS which can be downloaded for analysis. Now, the log feature is in the process of beta test, for now supporting such regions as Guangzhou and Shanghai. If you need it, please submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB) for application.

### Enabling Log Feature
Enable log access feature on the **Cloud Load Balancer Instance Details** page.

![](https://mc.qcloudimg.com/static/img/17014eeb67628fa78ffe04e2d7a58d8d/log1.png)

Select the appropriate bucket in the COS for the request log to be stored into the lb-id folder automatically created under the bucket. Then click the bucket address to go directly to the log download page.

If no buckets are created for cloud object storage, [Create a Bucket](https://console.cloud.tencent.com/cos4/bucket) and then select the appropriate storage location.

### Product Limitation and Cost Calculation
- Now the log aggregation granularity is one hour

- Load balancer only supports storage and download of Layer-7(HTTP/HTTPS) logs for now

- There will be delay in transmission of log data.

- Now the log service of load balancer is `Free`. According to [Free Quota](https://cloud.tencent.com/document/product/436/6240), the free quota of COS storage is 50 GB. If you have a large log size, please clean up the data in time.

- If you do not enable log access, Tencent Cloud will keep 3 days of logs for you by default; if you enable log access, the storage time depends on COS storage.

### Log Format and Variable Description
#### Log Format

```
[$stgw_request_id] [$time_local] [$protocol_type] [$server_addr:$server_port] [$server_name] [$remote_addr:$remote_port] [$status]  [$upstream_status] [$proxy_host] [$request] [$request_length] [$bytes_sent] [$http_host] [$http_user_agent] [$http_referer]
[$request_time] [$upstream_response_time] [$upstream_connect_time] [$upstream_header_time] [$tcpinfo_rtt] [$connection] [$connection_requests] [$ssl_handshake_time] [$ssl_cipher] [$ssl_protocol] [$ssl_session_reused]
```

#### Log Variable Description

| Number | Variable Name |   Description |
| :-------- | :-------- | :------ |
| 1 | time_local	|  Time stamp |
| 2 | protocol_type |  Protocol type (http/https/spdy/http2/ws/wss) |
| 3 | server_addr:server_port  | Destination IP and port of request |
| 4 | server_name | server_name of rule |
| 5 | remote_addr:remote_port	| client ip: port |
| 6 | status | Status code returned to the client by LB |
| 7 | upstream_status | Status code returned to LB by RS |
| 8 | proxy_host | upstream id |
| 9 | request | Request line |
| 10 | request_length | Bytes of request received from client |
| 11 |bytes_sent | 	Bytes sent to client |
| 12 |http_host	 | Request domain name |
| 13 |http_user_agent | 	user_agent |
| 14 |http_referer	 | http request source |
| 15 | request_time| Request processing time |
| 16 | upstream_response_time | Time for receiving response from rs |
| 17 | upstream_connect_time	 | Time for building tcp connection with rs |
| 18 | upstream_header_time	 | Time for receiving all http headers from rs |
| 19 | tcpinfo_rtt | rtt for tcp connection |
| 20 | connection | Connection id |
| 21 | connection_requests | Number of connection requests |
| 22 | ssl_handshake_time	| Time for ssl handshake |
| 23 | ssl_cipher| Encryption suite |
| 24 | ssl_protocol	| ssl protocol version |
| 25 | ssl_session_reused | ssl session reuse |
