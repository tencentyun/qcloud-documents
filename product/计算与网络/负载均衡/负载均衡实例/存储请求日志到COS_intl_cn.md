负载均衡支持用户存储请求日志的能力，您可以将请求日志存储到COS中，并下载分析。当前日志功能在灰度中，支持广州、上海等地域，如您有需要，请提[工单](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB)申请。

### 开启日志功能
在**负载均衡实例详情**页面，开启日志访问功能。

![](https://mc.qcloudimg.com/static/img/17014eeb67628fa78ffe04e2d7a58d8d/log1.png)

选取相应的COS中bucket，则请求日志会自动在bucket下创建lb-id为名称的文件夹进行存储。选取完成后，点击bucket地址可以直接跳转到日志下载页面。

如您没有创建对象存储的bucket，请在[新建bucket](https://console.cloud.tencent.com/cos4/bucket)后选取相应的存储位置。

### 产品限制和费用计算
- 当前日志聚合粒度为1小时。

- 当前负载均衡仅支持七层（HTTP/HTTPS）日志的存储和下载。

- 日志数据的传输会有一定的延迟。

- 当前负载均衡日志服务`免费`，COS存储的免费额度按照[文档](https://cloud.tencent.com/document/product/436/6240)中所示，提供50G免费存储空间。如您的日志量级较大，请及时清理数据。

- 若您不开启日志访问，腾讯云默认为您保留3天的日志；若您开启日志访问，存储时间则依COS存储而定。

### 日志格式及变量说明
#### 日志格式

```
[$stgw_request_id] [$time_local] [$protocol_type] [$server_addr:$server_port] [$server_name] [$remote_addr:$remote_port] [$status]  [$upstream_status] [$proxy_host] [$request] [$request_length] [$bytes_sent] [$http_host] [$http_user_agent] [$http_referer]
[$request_time] [$upstream_response_time] [$upstream_connect_time] [$upstream_header_time] [$tcpinfo_rtt] [$connection] [$connection_requests] [$ssl_handshake_time] [$ssl_cipher] [$ssl_protocol] [$ssl_session_reused]
```

#### 日志变量说明

| 序号 | 变量名 |   说明 |
| :-------- | :-------- | :------ |
| 1 | time_local	|  时间戳 |
| 2 | protocol_type |  协议类型（http/https/spdy/http2/ws/wss） |
| 3 | server_addr:server_port  | 请求的目的ip和目的端口 |
| 4 | server_name | 规则的server_name |
| 5 | remote_addr:remote_port	| client ip：port |
| 6 | status | LB返回给client的状态码 |
| 7 | upstream_status | RS返回给LB的状态码 |
| 8 | proxy_host | upstream id |
| 9 | request | 请求行 |
| 10 | request_length | 从客户端收到的请求字节数 |
| 11 | request_time| 请求处理时间 |
| 12 | upstream_response_time | 从rs接收应答所花费时间 |
| 13 | upstream_connect_time	 | 和rs建立tcp连接所花费时间 |
| 14 | upstream_header_time	 | 从rs接收完http头部所花费时间 |
| 15 | tcpinfo_rtt | tcp连接的rtt |
| 16 | connection | 连接id |
| 17 | connection_requests | 连接上的请求个数 |
| 18 | ssl_handshake_time	|ssl握手所花费时间 |
| 19 | ssl_cipher| 加密套件|
| 20 | ssl_protocol	| ssl协议版本 |
| 21 | ssl_session_reused | ssl session复用|
