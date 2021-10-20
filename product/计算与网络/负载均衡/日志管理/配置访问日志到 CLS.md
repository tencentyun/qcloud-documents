负载均衡支持配置七层（HTTP/HTTPS）访问日志（Access Log），访问日志可以帮助您了解客户端请求、辅助排查问题、分析梳理用户行为等。当前访问日志支持存储到 CLS 中，支持分钟粒度的日志上报，在线多规则检索。

负载均衡的访问日志主要用于故障排查，帮助业务快速定位问题。访问日志功能包括日志上报、日志存储和查询：
- 日志上报，提供尽力而为服务（Best-Effort Service），优先保障业务转发，再保障日志上报。
- 日志存储和查询，按当前使用的存储服务来提供服务保障 SLA。

>?
>- 当前负载均衡仅七层协议（HTTP/HTTPS）支持配置访问日志到 CLS，四层协议（TCP/UDP/TCP SSL）不支持配置访问日志到 CLS。
- 负载均衡配置访问日志到 CLS 的功能免费，用户仅需支付日志服务 CLS 的费用。
- 仅支持日志服务 CLS 的地域支持此功能，详情请参见 CLS 的 [可用地域](https://cloud.tencent.com/document/product/614/18940)。



## 方式一：为单实例配置访问日志
### 步骤一：开启访问日志存入 CLS
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)，单击左侧导航栏的**实例管理**。
2. 在“实例管理”页面，单击目标负载均衡 ID。
3. 在“基本信息”页面的“访问日志（七层）”模块，单击铅笔图标。
![](https://main.qcloudimg.com/raw/5c6ff27e1e5f4d839ea61def06457ae3.png)
4. 在弹出的“修改 CLS 日志存放位置”对话框中，开启“启用日志”，并选择存储访问日志的日志集和日志主题，单击**提交**。若您没有创建日志集或日志主题，请 [新建相关资源](https://console.cloud.tencent.com/cls/logset) 后，再选取具体的存储位置。
![](https://main.qcloudimg.com/raw/33ccb8c1bcf3b200716a4a2f1751f0c1.png)
>?建议选择 clb_logset 日志集下带“CLB”标识的日志主题。带“CLB”标识的日志主题和普通日志主题的差异在于：
>- 带“CLB”标识的日志主题默认自动创建索引；普通日志主题需手动创建索引，否则不支持检索。
>- 带“CLB”标识的日志主题默认支持仪表盘；普通日志主题需手动配置仪表盘。
6. 配置完成后单击日志集或日志主题即可跳转到 CLS 控制台的检索分析页面。
7. （可选）若想关闭访问日志，可再次单击铅笔图标，在弹出的“修改 CLS 日志存放位置”对话框中进行关闭并提交即可。

### 步骤二：配置日志主题的索引
>?为单实例配置的访问日志的日志主题必须配置索引，否则检索不到日志。
>
建议配置的索引如下：

| 键值索引    | 字段类型 | 分词符 |
| :---------- | :------- | :----- |
| server_addr | text     | 无需配置分词符     |
| server_name | text     | 无需配置分词符     |
| http_host   | text     | 无需配置分词符     |
| status      | long     | -     |
| vip_vpcid   | long     | -     |

具体操作如下：
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，在左侧导航栏单击**日志主题**。
2. 在“日志主题”页面，单击目标日志主题 ID。
3. 在日志主题详情页，单击**索引配置**页签，单击右上角的**编辑**，即可添加索引。索引字段配置说明请参见 [开启索引](https://cloud.tencent.com/document/product/614/16981)。
![](https://main.qcloudimg.com/raw/59262eff6c7f55929aa2b6ad652ec60c.png)
4. 索引配置完成后结果如下图所示。
![](https://main.qcloudimg.com/raw/c87991c34235f0ce38c2da72f1e0214d.png)

### 步骤三：查看访问日志
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)，单击左侧导航栏的**检索分析**。
3. 在“检索分析 ”页面中，选择日志集、日志主题和时间范围，单击**检索分析**，即可检索 CLB 上报到 CLS 的访问日志。检索语法详情请参见 [语法与规则](https://cloud.tencent.com/document/product/614/16982)。
![](https://main.qcloudimg.com/raw/1be3bc335e74f30538453133c34349db.png)

## 方式二：批量配置访问日志

### 步骤一：创建日志集和日志主题[](id:step2)
若您需要配置访问日志到日志服务 CLS 中，则需先创建日志集和日志主题。
若已有日志集和日志主题，则可直接跳转至 [步骤二](#step3) 开始操作。
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，单击左侧导航栏的**访问日志**。
2. 在“访问日志”页面左上角选择所属地域，在“日志集信息”区域，单击**创建日志集**。
3. 在弹出的“创建日志集”对话框中，设置保存时间，单击**保存**。
>?每个地域仅支持创建一个日志集，日志集名称为“clb_logset”。
4. 在“访问日志”页面的“日志主题”区域，单击**新建日志主题**。
5. 在弹出的“新增日志主题”对话框，选择左侧的负载均衡实例添加至右侧列表中，单击**保存**。
>?
>- 新建日志主题时，可选择添加、或不添加负载均衡实例。在日志主题列表的右侧“操作”列中，单击**管理**可重新添加负载均衡实例。每个负载均衡实例仅限添加至一个日志主题中。
>- 一个日志集中可创建多个日志主题（Topic），您可将不同的 CLB 日志放在不同的日志主题中，这些日志主题默认会带“CLB”标识。
>
![](https://main.qcloudimg.com/raw/375049a83cf4d1b734058fab4ee7755a.png)
6. （可选）若需关闭访问日志，在日志主题列表的右侧“操作”列中，单击**停止**停止投递日志即可。

### 步骤二：查看访问日志[](id:step3)
负载均衡已自动配置以访问日志的变量为关键值的索引，您无需手动配置索引，可直接通过检索分析来查询访问日志。
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，单击左侧导航栏的**访问日志**。
2. 单击目标日志主题右侧“操作”列的**检索**，跳转至 [日志服务控制台](https://console.cloud.tencent.com/cls/search) 的“检索分析”页面。
3. 在“检索分析”页面的输入框中输入检索分析语句，选择时间范围，单击**检索分析**即可检索 CLB 上报到 CLS 的访问日志。
>?检索语法详情请参见 [语法与规则](https://cloud.tencent.com/document/product/614/47044)。
>


## 日志格式及变量说明
### 日志格式
```
[$stgw_request_id] [$time_local] [$protocol_type] [$server_addr:$server_port]  [$server_name] [$remote_addr:$remote_port] [$status] [$upstream_addr] [$upstream_status] [$proxy_host] [$request] [$request_length] [$bytes_sent] [$http_host] [$http_user_agent] [$http_referer] [$request_time] [$upstream_response_time] [$upstream_connect_time] [$upstream_header_time] [$tcpinfo_rtt] [$connection] [$connection_requests] [$ssl_handshake_time] [$ssl_cipher] [$ssl_protocol] [$vip_vpcid] [$uri] [$server_protocol]
```

### 字段类型
目前日志服务支持如下三种字段类型：

| 名称   | 类型描述                 |
| :----- | :----------------------- |
| text   | 文本类型                 |
| long   | 整型数值类型（Int 64）   |
| double | 浮点数数值类型（64 bit） |

### 日志变量说明
<table class="table"><thead><tr><th>变量名</th><th>说明</th><th>字段类型</th></tr></thead>
<tbody><tr><td>stgw_request_id</td><td> 请求 ID。 </td><td>text</td></tr>
<tr><td>time_local</td><td> 访问的时间与时区，例如，“01/Jul/2019:11:11:00 +0800”，最后的“+0800”表示所处时区为 UTC 之后的8小时，即为北京时间。</td><td>text</td></tr>
<tr><td>protocol_type</td><td> 协议类型（HTTP/HTTPS/SPDY/HTTP2/WS/WSS）。</td><td>text</td></tr>
<tr><td>server_addr</td><td>CLB 的 VIP。 </td><td>text</td></tr>
<tr><td>server_port</td><td>CLB 的 VPort，即监听端口。</td><td>long</td></tr>
<tr><td>server_name</td><td> 规则的 server_name，CLB 的监听器中配置的域名。</td><td>text</td></tr>
<tr><td>remote_addr</td><td> 客户端 IP。</td><td>text</td></tr>
<tr><td>remote_port</td><td> 客户端端口。</td><td>long</td></tr>
<tr><td>status</td><td> CLB 返回给客户端的状态码。 </td><td>long</td></tr>
<tr><td>upstream_addr</td><td> RS 地址。</td><td>text</td></tr>
<tr><td>upstream_status</td><td> RS 返回给 CLB 的状态码。 </td><td>text</td></tr>
<tr><td>proxy_host</td><td> stream ID。 </td><td>text</td></tr>
<tr><td>request</td><td> 请求行。 </td><td>text</td></tr>
<tr><td>request_length</td><td> 从客户端收到的请求字节数。 </td><td>long</td></tr>
<tr><td>bytes_sent</td><td> 发送到客户端的字节数。 </td><td>long</td></tr>
<tr><td>http_host</td><td> 请求域名，即 HTTP 头部中的 Host。</td><td>text</td></tr>
<tr><td>http_user_agent</td><td> HTTP 协议头的 user_agent 字段。</td><td>text</td></tr>
<tr><td>http_referer</td><td> HTTP 请求来源。 </td><td>text</td></tr>
<tr><td>request_time</td><td> 请求处理时间：从收到客户端的第一个字节开始，直到给客户端发送的最后一个字节为止，包括客户端请求到 CLB、CLB 转发请求到 RS、RS 响应数据到 CLB、CLB 转发数据到客户端的总时间。</td><td>double</td></tr>
<tr><td>upstream_response_time</td><td> 整个后端请求所花费时间：从开始 CONNECT RS 到从 RS 接收完应答的时间。</td><td>double</td></tr>
<tr><td>upstream_connect_time</td><td> 和 RS 建立 TCP 连接所花费时间：从开始 CONNECT RS 到开始发送 HTTP 请求的时间。</td><td>double</td></tr>
<tr><td>upstream_header_time</td><td> 从 RS 接收完 HTTP 头部所花费时间：从开始 CONNECT RS 到从 RS 接收完 HTTP 应答头部的时间。</td><td>double</td></tr>
<tr><td>tcpinfo_rtt</td><td> TCP 连接的 RTT。 </td><td>long</td></tr>
<tr><td>connection</td><td> 连接 ID。 </td><td>long</td></tr>
<tr><td>connection_requests</td><td> 连接上的请求个数。 </td><td>long</td></tr>
<tr><td>ssl_handshake_time</td><td> SSL 握手所花费时间。 </td><td>double</td></tr>
<tr><td>ssl_cipher</td><td> SSL 加密套件。</td><td>text</td></tr>
<tr><td>ssl_protocol</td><td> SSL 协议版本。</td><td>text</td></tr>
<tr><td>vip_vpcid</td><td>负载均衡 VIP 的所属私有网络 ID，公网 CLB 的 vip_vpcid 为-1。</td><td>long</td></tr>
<tr><td>request</td><td> 请求方式，支持 POST 和 GET 请求。</td><td>text</td></tr>
<tr><td>uri</td><td> 资源标识符。</td><td>text</td></tr>
<tr><td>server_protocol</td><td>CLB 的协议。</td><td>text</td></tr>
</tbody></table>

### 默认支持检索的日志变量
带“CLB”标识的日志集默认支持检索的字段如下所示：
<table class="table"><thead><tr><th>索引字段</th><th>说明</th><th>字段类型</th></tr></thead>
<tbody>
<tr><td>time_local</td><td> 访问的时间与时区，例如，“01/Jul/2019:11:11:00 +0800”，最后的“+0800”表示所处时区为 UTC 之后的8小时，即为北京时间。</td><td>text</td></tr>
<tr><td>protocol_type</td><td> 协议类型（HTTP/HTTPS/SPDY/HTTP2/WS/WSS）。</td><td>text</td></tr>
<tr><td>server_addr</td><td>CLB 的 VIP。 </td><td>text</td></tr>
<tr><td>server_name</td><td> 规则的 server_name，CLB 的监听器中配置的域名。</td><td>text</td></tr>
<tr><td>remote_addr</td><td> 客户端 IP。</td><td>text</td></tr>
<tr><td>status</td><td> CLB 返回给客户端的状态码。 </td><td>long</td></tr>
<tr><td>upstream_addr</td><td> RS 地址。</td><td>text</td></tr>
<tr><td>upstream_status</td><td> RS 返回给 CLB 的状态码。 </td><td>text</td></tr>
<tr><td>request_length</td><td> 从客户端收到的请求字节数。 </td><td>long</td></tr>
<tr><td>bytes_sent</td><td> 发送到客户端的字节数。 </td><td>long</td></tr>
<tr><td>http_host</td><td> 请求域名，即 HTTP 头部中的 Host。</td><td>text</td></tr>
<tr><td>request_time</td><td> 请求处理时间：从收到客户端的第一个字节开始，直到给客户端发送的最后一个字节为止，包括客户端请求到 CLB、CLB 转发请求到 RS、RS 响应数据到 CLB、CLB 转发数据到客户端的总时间。</td><td>double</td></tr>
<tr><td>upstream_response_time</td><td> 整个后端请求所花费时间：从开始 CONNECT RS 到从 RS 接收完应答的时间。</td><td>double</td></tr>
</tbody></table>
