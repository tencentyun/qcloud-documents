 >!配置访问日志到 COS 将于2020-05-15 00:00:00关闭新增（其中广州地域将于2020-04-26 00:00:00关闭新增），所有地域将于2020-06-30 00:00:00正式下线该功能，详情请参见 [CLB 配置访问日志到 COS 功能下线公告](https://cloud.tencent.com/document/product/214/43659)，请使用升级版功能：[配置访问日志到 CLS](https://cloud.tencent.com/document/product/214/41379)。

负载均衡支持配置七层（HTTP/HTTPS）访问日志（Access Log），访问日志可以帮助您了解客户端请求、辅助排查问题、分析梳理访问数据等。当前访问日志支持存储到 COS 中下载分析，支持的地域包括广州、上海、北京、香港、上海金融和深圳金融。

负载均衡的访问日志主要用于故障排查，帮助业务快速定位问题。访问日志功能包括日志上报、日志存储和查询：
- 日志上报，提供尽力而为服务（Best-Effort Service），优先保障业务转发，再保障日志上报。
- 日志存储和查询，按当前使用的存储服务来提供服务保障 SLA。

>?
- 当前日志聚合粒度为1小时，日志数据的传输会有一定的延迟。
- 当前负载均衡仅支持公网七层（HTTP/HTTPS）日志的存储和下载，不支持四层（TCP/UDP）和内网七层日志的存储和下载。
- 负载均衡配置访问日志到 COS 的功能免费，用户仅需支付对象存储 COS 的费用， COS 面向所有新用户有一定量的免费额度，详情请参见 [免费额度](https://cloud.tencent.com/document/product/436/6240) 。
- 在支持配置访问日志到 COS 的地域中，若您不开启访问日志，腾讯云默认为您保留3天的日志；若您开启访问日志，存储时间则依 COS 存储而定。其他地域暂不支持配置访问日志。


## 开启访问日志存入 COS
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)。
2. 在"负载均衡"列表页面，单击想要配置的负载均衡 ID，进入“负载均衡基本信息”页面。
3. 在“访问日志”模块，编辑日志存入 COS。
![](https://main.qcloudimg.com/raw/948ca531935af6a102885d3a941852e0.png)
4. 在弹出框中，开启访问日志，并选择相应 COS 中的存放 bucket。如您没有创建COS 的 bucket，请 [新建 bucket](https://console.cloud.tencent.com/cos4/bucket) 后，选取相应的存储位置。
![](https://main.qcloudimg.com/raw/e8f3506ade5fe73c2267c3f294c957b4.png)
5. 点击【提交】，请求日志会自动在 bucket 下，创建以 lb-id 为名称的文件夹进行存储。
6. 配置完成后，单击 bucket 地址可以直接跳转到日志下载页面。

## 关闭访问日志存入 COS
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)。
2. 在"负载均衡"列表页面，单击想要配置的负载均衡 ID，进入“负载均衡基本信息”页面。
3. 在“访问日志”模块，编辑日志存入 COS。
![](https://main.qcloudimg.com/raw/948ca531935af6a102885d3a941852e0.png)
4. 在弹出框中，关闭访问日志， 点击【提交】 即可 。
![](https://main.qcloudimg.com/raw/86dbea54d3b697a03ed449b398679461.png)   
 配置完成如下，关闭后将不支持再开启 COS 日志， 详见 [关于CLB配置访问日志到COS下线的公告](https://cloud.tencent.com/document/product/214/43659)。
![](https://main.qcloudimg.com/raw/43a489e82953e4b27acca5a541912704.png)

## 日志格式及变量说明
### 日志格式
```
[$stgw_request_id] [$time_local] [$protocol_type] [$server_addr:$server_port] [$server_name] [$remote_addr:$remote_port] [$status]  [$upstream_status] [$proxy_host] [$request] [$request_length] [$bytes_sent] [$http_host] [$http_user_agent] [$http_referer]
[$request_time] [$upstream_response_time] [$upstream_connect_time] [$upstream_header_time] [$tcpinfo_rtt] [$connection] [$connection_requests] [$ssl_handshake_time] [$ssl_cipher] [$ssl_protocol] [$ssl_session_reused]
```

### 日志变量说明

| 变量名 | 说明 |
| :-------- | :------ |
|stgw_request_id  |	请求 ID。 |
| time_local	|  访问的时间与时区，例如“01/Jul/2019:11:11:00 +0800”，最后的“+0800”表示所处时区为 UTC 之后的8小时，即为北京时间。 |
| protocol_type |  协议类型（HTTP/HTTPS/SPDY/HTTP2/WS/WSS）。 |
| server_addr:server_port  | 请求的目的 IP 和目的端口。 |
| server_name | 规则的 server_name，即服务器名称。 |
| remote_addr:remote_port	| 客户端 IP和客户端端口。 |
| status | CLB 返回给客户端的状态码。 |
| upstream_status | RS 返回给 CLB 的状态码。 |
| proxy_host | stream ID。 |
| request | 请求行。 |
| request_length | 从客户端收到的请求字节数。 |
|bytes_sent | 	发送到客户端的字节数。 |
|http_host	 | 请求域名。 |
|http_user_agent | 	HTTP 协议头的 user_agent 字段。 |
|http_referer	 | HTTP 请求来源。 |
| request_time|请求处理时间：从收到客户端的第一个字节开始，直到给客户端发送的最后一个字节为止，包括客户端请求到 CLB、CLB 转发请求到 RS、RS 响应数据到 CLB、CLB 转发数据到客户端的总时间。|
| upstream_response_time |整个后端请求所花费时间：从开始 CONNECT RS 到从 RS 接收完应答的时间。|
| upstream_connect_time	|和 RS 建立 TCP 连接所花费时间：从开始 CONNECT RS 到开始发送 HTTP 请求的时间。|
| upstream_header_time	|  从 RS 接收完 HTTP 头部所花费时间：从开始 CONNECT RS  到从 RS 接收完 HTTP 应答头部的时间。|
| tcpinfo_rtt | TCP 连接的 RTT。 |
| connection | 连接 ID。 |
| connection_requests | 连接上的请求个数。 |
| ssl_handshake_time	|SSL 握手所花费时间。 |
| ssl_cipher| SSL 加密套件。|
| ssl_protocol	| SSL 协议版本。 |
| ssl_session_reused |SSL SESSION 复用。|	 



