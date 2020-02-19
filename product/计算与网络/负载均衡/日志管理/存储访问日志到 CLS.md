负载均衡支持配置七层（HTTP/HTTPS）访问日志（Access Log），访问日志可以帮助您了解客户端请求、辅助排查问题、分析梳理用户行为等。当前访问日志支持存储到 CLS 中，支持分钟粒度的日志上报，在线多规则检索。
- 当前负载均衡仅支持公网七层（HTTP/HTTPS）日志的存储和下载，不支持四层（TCP/UDP）和内网七层日志的存储和下载。
- 负载均衡访问日志无需额外付费，您仅需要支付日志服务的费用。
- 当前访问日志存入 CLS 支持的地域包括：广州、成都、多伦多，可直接在控制台使用或通过 API 配置；北京和上海灰度中，如有需求，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)。

>?CLB 的访问日志主要用于故障排查，帮助业务快速定位问题。访问日志功能包括日志上报、日志存储和查询：
- 日志上报，提供尽力而为服务（Best Effor Service），优先保障业务转发，再保障日志上报。
- 日志存储和查询，按当前使用的存储服务来提供服务保障 SLA。

## 开启访问日志
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)。
2. 单击需进行配置的负载均衡 ID，进入“负载均衡基本信息”页面。
3. 在“日志访问”模块，编辑日志服务 CLS。
![](https://main.qcloudimg.com/raw/163c20ca7cb4326005c9ecf9fb43a39f.png)
4. 在弹出框中，启用并选择访问日志将存入的日志集和日志主题。
>?如您没有创建日志集或日志主题，请 [新建相关资源](https://console.cloud.tencent.com/cls/logset) 后，再选取具体的存储位置。
>
![](https://main.qcloudimg.com/raw/ad6a8f33dbec8eec9ce0e84de859a845.png)
5. 单击【提交】，访问日志会被收集在对应的主题中。
6. 配置完成后单击日志集或日志主题将跳转到 CLS 的日志检索页面。

## 查询访问日志
### 配置 CLS 日志主题索引
>?日志主题必须配置索引，否则检索不到日志。

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航中，选择【日志集管理】，进入“日志集管理”列表页。
3. 单击日志集 ID，进入日志集详情页。
4. 在日志集详情页，单击日志主题 ID，进入日志主题详情页。
![](https://main.qcloudimg.com/raw/2ac7b3725bf4a598a4f9668ed3c80c1c.png)
5. 在日志主题详情页，选择【索引配置】选项卡，您可以在日志变量中选取部分变量，按需配置索引字段，配置说明请参见 [开启索引](https://cloud.tencent.com/document/product/614/16981)。
![](https://main.qcloudimg.com/raw/aff66a76b27f5ec0366028e1e9a6ed08.png)
6. 索引配置完成后结果如下图所示。
![](https://main.qcloudimg.com/raw/a5c1dfd312827c8fd3945cb0945616fb.png)

### 检索访问日志
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航中，选择【日志检索】，进入“检索分析 ”页面。
3. 在“检索分析 ”页面中，选择日志集和日志主题，即可检索 CLB 上报到 CLS 的访问日志。检索语法详情请参见 [语法与规则](https://cloud.tencent.com/document/product/614/16982)。
![](https://main.qcloudimg.com/raw/8fc64241fd239212f101aaa9b0e7729d.png)

## 日志变量说明
<table class="table"><thead><tr><th>变量名</th><th>说明</th></tr></thead>
<tbody><tr><td>stgw_request_id</td><td> 请求 ID，内部使用 </td></tr>
<tr><td>time_local</td><td> 访问的时间与时区，例如，“01/Jul/2019:11:11:00 +0800”，最后的“+0800”表示所处时区为 UTC 之后的8小时，即为北京时间</td></tr>
<tr><td>protocol_type</td><td> 协议类型（HTTP/HTTPS/SPDY/HTTP2/WS/WSS）</td></tr>
<tr><td>server_addr</td><td> 请求的目的 IP </td></tr>
<tr><td>server_port</td><td>请求的目的端口</td></tr>
<tr><td>server_name</td><td> 规则的 server_name，即服务器名称</td></tr>
<tr><td>remote_addr</td><td> client IP</td></tr>
<tr><td>remote_port</td><td> client port</td></tr>
<tr><td>status</td><td> CLB 返回给 client 的状态码 </td></tr>
<tr><td>upstream_addr</td><td> RS 地址</td></tr>
<tr><td>upstream_status</td><td> RS 返回给 CLB 的状态码 </td></tr>
<tr><td>proxy_host</td><td> upstream ID </td></tr>
<tr><td>request</td><td> 请求行 </td></tr>
<tr><td>request_length</td><td> 从客户端收到的请求字节数 </td></tr>
<tr><td>bytes_sent</td><td> 发送客户端的字节数 </td></tr>
<tr><td>http_host</td><td> 请求域名 </td></tr>
<tr><td>http_user_agent</td><td> user_agent </td></tr>
<tr><td>http_referer</td><td> HTTP 请求来源 </td></tr>
<tr><td>request_time</td><td> 请求处理时间（从收到客户端的第一个字节开始，到给客户端发送的最后一个字节为止，包括客户端请求到 CLB、CLB 转发请求到 RS、RS 响应数据到 CLB、CLB 转发数据到客户端的总时间）</td></tr>
<tr><td>upstream_response_time</td><td> 整个后端请求所花费时间（从开始 CONNECT RS 到从 RS 接收完应答的时间）</td></tr>
<tr><td>upstream_connect_time</td><td> 和 RS 建立 TCP 连接所花费时间（从开始 CONNECT RS 到开始发送 HTTP 请求的时间）</td></tr>
<tr><td>upstream_header_time</td><td> 从 RS 接收完 HTTP 头部所花费时间（从开始 CONNECT RS 到从 RS 接收完 HTTP 应答头部的时间）</td></tr>
<tr><td>tcpinfo_rtt</td><td> TCP 连接的 RTT </td></tr>
<tr><td>connection</td><td> 连接 ID </td></tr>
<tr><td>connection_requests</td><td> 连接上的请求个数 </td></tr>
<tr><td>ssl_handshake_time</td><td> SSL 握手所花费时间 </td></tr>
<tr><td>ssl_cipher</td><td> 加密套件</td></tr>
<tr><td>ssl_protocol</td><td> SSL 协议版本</td></tr>
<tr><td>vip_vpcid</td><td>负载均衡 VIP 的 vpcId </td></tr></tbody></table>
