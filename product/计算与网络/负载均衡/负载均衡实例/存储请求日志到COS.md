负载均衡支持用户存储请求日志的能力，您可以将请求日志存储到 COS 中，并下载分析。当前七层（HTTP/HTTPS）的日志功能已经全量发布，支持广州、上海、北京、中国香港、上海金融和北京金融，欢迎开通使用。CLB 暂不支持四层（TCP/UDP）日志的存储和下载。

## 开启日志功能
1. 在**负载均衡实例详情**页面，开启日志访问功能。
![](https://main.qcloudimg.com/raw/8e00f8590d3fdf64278389cd019864a8.png)
2. 选取相应的 COS 中 bucket，则请求日志会自动在 bucket 下创建 lb-id 为名称的文件夹进行存储。选取完成后，单击 bucket 地址可以直接跳转到日志下载页面。
![](https://main.qcloudimg.com/raw/f1f6d287dba415df1c832223cbdac11b.png)
>!如您没有创建对象存储的 bucket，请 [新建 bucket](https://console.cloud.tencent.com/cos4/bucket) 后，选取相应的存储位置。

## 产品限制和费用计算
- 当前日志聚合粒度为1小时。
- 当前负载均衡仅支持七层（HTTP/HTTPS）日志的存储和下载，暂不支持四层（TCP/UDP）日志的存储和下载。
- 日志数据的传输会有一定的延迟。
- 当前负载均衡日志服务**免费**，COS 存储的免费额度按照文档 [免费额度](https://cloud.tencent.com/document/product/436/6240) 中所示，提供50G免费存储空间。如您的日志量级较大，请及时清理数据。
- 若您不开启日志访问，腾讯云默认为您保留3天的日志；若您开启日志访问，存储时间则依 COS 存储而定。

## 日志格式及变量说明
### 日志格式
```
[$stgw_request_id] [$time_local] [$protocol_type] [$server_addr:$server_port] [$server_name] [$remote_addr:$remote_port] [$status]  [$upstream_status] [$proxy_host] [$request] [$request_length] [$bytes_sent] [$http_host] [$http_user_agent] [$http_referer]
[$request_time] [$upstream_response_time] [$upstream_connect_time] [$upstream_header_time] [$tcpinfo_rtt] [$connection] [$connection_requests] [$ssl_handshake_time] [$ssl_cipher] [$ssl_protocol] [$ssl_session_reused]
```

### 日志变量说明

| 序号 | 变量名 | 说明 |
| :-------- | :-------- | :------ |
| 1 | time_local	|  访问的时间与时区，例如“01/Jul/2019:11:11:00 +0800”，最后的“+0800”表示所处时区为 UTC 之后的8小时，即为北京时间。 |
| 2 | protocol_type |  协议类型（HTTP/HTTPS/SPDY/HTTP2/WS/WSS）。 |
| 3 | server_addr:server_port  | 请求的目的 IP 和目的端口。 |
| 4 | server_name | 规则的 server_name，即服务器名称。 |
| 5 | remote_addr:remote_port	| client IP：port。 |
| 6 | status | LB 返回给 client 的状态码。 |
| 7 | upstream_status | RS 返回给 LB 的状态码。 |
| 8 | proxy_host | upstream ID。 |
| 9 | request | 请求行。 |
| 10 | request_length | 从客户端收到的请求字节数。 |
| 11 |bytes_sent | 	发送客户端的字节数。 |
| 12 |http_host	 | 请求域名。 |
| 13 |http_user_agent | 	user_agent。 |
| 14 |http_referer	 | HTTP 请求来源。 |
| 15 | request_time|请求处理时间（从收到客户端的第一个字节开始，到给客户端发送的最后一个字节为止，包括客户端请求到 CLB、CLB 转发请求到 RS、RS 响应数据到 CLB、CLB 转发数据到客户端的总时间）。|
| 16 | upstream_response_time |整个后端请求所花费时间（从开始 CONNECT RS 到从 RS 接收完应答的时间）。|
| 17 | upstream_connect_time	|和 RS 建立 TCP 连接所花费时间（从开始 CONNECT RS 到开始发送 HTTP 请求的时间）。|
| 18 | upstream_header_time	|  从 RS 接收完 HTTP 头部所花费时间（从开始 CONNECT RS  到从 RS 接收完 HTTP 应答头部的时间）。|
| 19 | tcpinfo_rtt | TCP 连接的 RTT。 |
| 20 | connection | 连接 ID。 |
| 21 | connection_requests | 连接上的请求个数。 |
| 22 | ssl_handshake_time	|SSL 握手所花费时间。 |
| 23 | ssl_cipher| 加密套件。|
| 24 | ssl_protocol	| SSL 协议版本。 |
| 25 | ssl_session_reused |SSL SESSION 复用。|	 
