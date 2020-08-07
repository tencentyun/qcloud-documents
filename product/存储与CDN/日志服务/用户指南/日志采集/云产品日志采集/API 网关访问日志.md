
## 简介

在微服务架构中，API 网关扮演着重要的角色，封装后端各类小的服务系统，实现前后端分离，对外提供统一的调用接口，方便用户调用服务集成应用。作为系统的统一出入口管理模块，每一次请求的日志访问记录的信息就显得尤为重要，包括客户端 IP、请求路径、状态码等信息。

API 网关访问日志接入日志服务后，API 管理员可以根据日志中任意关键字进行快速的精确或模糊检索，可用于问题定位或者统计查询，同时也能方便检索 API 调用的详细日志。

![](https://main.qcloudimg.com/raw/29747a0d2ad0268e4cfc418232b02a11.png)





## 接入步骤


>?API 日志管理功能目前为灰度测试阶段，如需使用请联系您的客户经理或 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开启。

#### 创建日志规则

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)，在左侧导航中单击【日志管理】。
2. 在日志管理页面，单击左上角的【新建】，开始新建日志收集规则。
第一次使用时，您需要对 API 网关采集日志服务进行授权，步骤如下：
   1. 在创建服务角色的对话框中，单击前往【访问管理】。
   2. 在访问管理的角色管理页面，单击【同意授权】，完成后自动跳转至 API 网关的日志管理页面。
3. 在添加日志规则的对话框中，填写日志规则名称、采集数据和投递的目标日志集。
   - 名称：API 网关的日志管理能力使用了腾讯云平台的日志服务，在新建日志规则时，可对日志规则进行命名。
   - 采集数据：选择所需收集的通账户下的日志服务及服务中的具体环境。
   - 投递到日志集：通过选择日志集，确定将这些信息投递到日志服务的哪个日志集中。若您还没有创建日志集，则需要在日志服务页面先进行创建。
4. 创建成功后，即可在日志管理页面查看并编辑日志规则。
![img](https://main.qcloudimg.com/raw/09803844784ceaa5f038354c658896c2.png)



## 查看日志

API 网关的日志收集到日志服务中后，您可在日志服务页面对应的日志集下，进行查看对应的日志集和日志主题，也可以在检索页面查看 API 网关访问日志的详情信息，检索前必须预先在日志服务的控制台 [开启索引配置](https://cloud.tencent.com/document/product/614/16981)。


在日志服务控制台操作日志主题索引配置，将全文索引开启并保存。
![](https://main.qcloudimg.com/raw/3dc8a71867d6744f854fffb494a1ede5.png)

在日志服务控制台检索页面查看日志。
![](https://main.qcloudimg.com/raw/4e6c2819ed69fc9a4ef9018e21bb2434.png)



## API 访问日志格式
```shell
log_format  
'[$app_id][$env_name][$service_id][$http_host][$api_id][$uri][$scheme][rsp_st:$status][ups_st:$upstream_status]'
'[cip:$remote_addr][uip:$upstream_addr][vip:$server_addr][rsp_len:$bytes_sent][req_len:$request_length]' 
'[req_t:$request_time][ups_rsp_t:$upstream_response_time][ups_conn_t:$upstream_connect_time][ups_head_t:$upstream_header_time]'
'[err_msg:$err_msg][tcp_rtt:$tcpinfo_rtt][$pid][$time_local]';
```

| 序号 | 字段名     | 说明                                                         |
| ---- | ---------- | ------------------------------------------------------------ |
| 1    | app_id     | 用户 ID                                                      |
| 2    | env_name   | 环境名称                                                     |
| 3    | service_id | 服务 ID                                                      |
| 4    | http_host  | 域名                                                         |
| 5    | api_id     | API 的 ID                                                    |
| 6    | uri        | 请求的路径                                                   |
| 7    | scheme     | HTTP/HTTPS 协议                                              |
| 8    | rsp_st     | 请求响应状态码                                               |
| 9    | ups_st     | 后端业务服务器的响应状态码（如果请求透传到后端，改变量不为空。如果请求在 APIGW 就被拦截了，那么该变量显示为`-`） |
| 10   | cip        | 客户端 IP                                                    |
| 11   | uip        | 后端业务服务（upstream）的 IP                                |
| 12   | vip        | 请求访问的 VIP                                               |
| 13   | rsp_len    | 响应长度                                                     |
| 14   | req_len    | 请求长度                                                     |
| 15   | req_t      | 请求响应的总时间                                             |
| 16   | ups_rsp_t  | 后端响应的总时间（APIGW 建立连接到接收到后端响应的时间）     |
| 17   | ups_conn_t | 与后端业务服务器连接建立成功时间                             |
| 18   | ups_head_t | 后端响应的头部到达时间                                       |
| 19   | err_msg    | 错误信息                                                     |
| 20   | tcp_rtt    | 客户端 TCP 连接信息，RTT（Round Trip Time）由三部分组成：链路的传播时间（propagation delay）、末端系统的处理时间、路由器缓存中的排队和处理时间（queuing delay） |


