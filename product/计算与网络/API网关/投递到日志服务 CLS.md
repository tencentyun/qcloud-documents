## 操作场景
API 网关支持记录客户端访问日志，通过访问日志可以帮助您了解客户端请求、辅助排查问题、分析梳理用户行为等。
API 网关控制台提供了基础的日志看板，您可以直接在控制台查看、检索日志；API 网关也提供了投递日志到 [日志服务 CLS](https://console.cloud.tencent.com/cls) 的能力，以便于您通过日志服务进行多维度的统计分析。

## 操作步骤
### 步骤1：创建日志集和日志主题[](id:step1)
若您需要配置访问日志到日志服务 CLS 中，则需先创建日志集和日志主题。
若已有日志集和日志主题，则可直接跳转至 [步骤2](#step2) 开始操作。
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)，单击左侧导航栏的**工具-日志投递**。
2. 在“访问日志”页面左上角选择所属地域，在“日志集信息”区域，单击**创建日志集**。
3. 在弹出的“创建日志集”对话框中，设置保存时间，单击**保存**。
>?每个地域仅支持创建一个日志集，日志集名称为“apigw_logset”。
4. 在“访问日志”页面的“日志主题”区域，单击**新建日志主题**。
5. 在弹出的“新增日志主题”对话框，选择左侧的 API 网关专享实例添加至右侧列表中，单击**保存**。
>?
>- API 网关的日志投递是实例级别的，仅专享实例支持投递日志到日志服务 CLS ，共享实例不支持。
>- 在日志主题列表的右侧“操作”列中，单击**管理**可编辑已添加的 API 网关专享实例。
>- 每个 API 网关实例仅限添加至一个日志主题中。
>- 一个日志集中可创建多个日志主题（Topic），您可将不同的 API 网关专享实例日志放在不同的日志主题中。
6. （可选）若需关闭访问日志，在日志主题列表的右侧“操作”列中，单击**停止**停止投递日志即可。

### 步骤2：查看访问日志[](id:step2)
API 网关已自动配置以访问日志的变量为关键值的索引，您无需手动配置索引，可直接通过检索分析来查询访问日志。
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)，单击左侧导航栏的**工具** > **日志投递**。
2. 单击目标日志主题右侧“操作”列的**检索**，跳转至 [日志服务控制台](https://console.cloud.tencent.com/cls/search) 的“检索分析”页面。
3. 在“检索分析”页面的输入框中输入检索分析语句，选择时间范围，单击**检索分析**即可检索 API 网关上报到 CLS 的访问日志。
>?检索语法详情请参见 [语法与规则](https://cloud.tencent.com/document/product/614/47044)。

## 日志格式说明
投递的服务日志格式如下：
```LOG
log_format  
'[$app_id][$env_name][$service_id][$http_host][$api_id][$uri][$scheme][rsp_st:$status][ups_st:$upstream_status]'
'[cip:$remote_addr][uip:$upstream_addr][vip:$server_addr][rsp_len:$bytes_sent][req_len:$request_length]' 
'[req_t:$request_time][ups_rsp_t:$upstream_response_time][ups_conn_t:$upstream_connect_time][ups_head_t:$upstream_header_time]'
'[err_msg:$err_msg][tcp_rtt:$tcpinfo_rtt][$pid][$time_local][req_id:$request_id]';
```
各参数说明如下：

| 参数名称 | 说明 |
|---------|---------|
| app_id | 用户 ID。 | 
| env_name |环境名称。|
| service_id | 服务 ID。|
| http_host | 域名。|
| api_id | API 的 ID。 |
| uri |请求的路径。|
| scheme |  HTTP/HTTPS 协议。|
| rsp_st | 请求响应状态码。 |
| ups_st | 后端业务服务器的响应状态码（如果请求透传到后端，改变量不为空。如果请求在 APIGW 就被拦截了，那么该变量显示为 `-`）。|
| cip |    客户端 IP。|
| uip |     后端业务服务（upstream）的 IP。
| vip |    请求访问的 VIP。|
| rsp_len | 响应长度。 |
| req_len | 请求长度。| 
| req_t | 请求响应的总时间。|
| ups_rsp_t | 后端响应的总时间（APIGW 建立连接到接收到后端响应的时间）。|
| ups_conn_t |与后端业务服务器连接建立成功时间。|
| ups_head_t |后端响应的头部到达时间。|
| err_msg |   错误信息。|
| tcp_rtt |   客户端 TCP 连接信息，RTT（Round Trip Time）由三部分组成：链路的传播时间（propagation delay）、末端系统的处理时间、路由器缓存中的排队和处理时间（queuing delay）。|
| pid | 进程 ID。 |
| time_local | 发生请求的时间。 |
| req_id | 请求 ID。 |

## 注意事项
- API 网关的日志投递是实例级别的，仅专享实例支持投递日志到日志服务 CLS ，共享实例不支持。
- API 网关配置访问日志到 CLS 的功能免费，用户仅需支付日志服务 CLS 的费用。
- 仅支持日志服务 CLS 的地域支持此功能，详情请参见 CLS 的 [可用地域](https://cloud.tencent.com/document/product/614/18940)。
