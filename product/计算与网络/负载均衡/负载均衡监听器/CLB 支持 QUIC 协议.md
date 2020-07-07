用户在使用 QUIC 协议后，APP 访问速度将得到大幅提升，在弱网络、Wi-Fi 和4G频繁切换等场景下，不需要重连即可实现多路复用。本文档将为您介绍，如何在负载均衡控制台中，配置 QUIC 协议。
## 什么是 QUIC
快速 UDP 互联网连接（quick udp internet connection，QUIC）是由 Google 提出的使用 UDP 进行多路并发传输的协议。QUIC 相比现在广泛应用的 TCP+TLS+HTTP2 协议有如下优势：
- 减少了连接建立的时间。
- 改善拥塞控制。
- 避免队头阻塞的多路复用。
- 连接迁移。  

## 功能概述
当前 CLB 支持的 QUIC 版本是 Q044 及以下 。公网负载均衡的七层 HTTPS 监听器支持 QUIC 协议，其他类型监听器暂不支持 QUIC 协议。CLB 开启 QUIC 后：
- 客户端可以和 CLB 之间建立 QUIC 连接，当二者协商无法建立 QUIC 连接时自动降级到 HTTPS 或 HTTP/2。
- CLB 和后端服务器之间仍然使用 HTTP1.x 协议。

QUIC 使用 UDP 协议，会占用 CLB 的 UDP 端口：
- HTTPS 监听器开启 QUIC 协议后，自动占用对用的 UDP 端口。例如当 HTTPS:443 监听器开启 QUIC 协议后，该规则会同时占用 TCP:443 和 UDP:443 端口，您不能再创建 TCP:443 和 UDP:443 监听器。
- 当前在一个 HTTPS 监听器中，只能对一个域名开启 QUIC 协议。
- 创建新的 HTTPS 监听器时，支持开启 QUIC。创建完后，QUIC 可以自由开关。若创建时没有开启 QUIC 的监听器，不能再开启 QUIC，更不可能关闭 QUIC。

## 前提条件
- 当前 CLB 中的 QUIC 协议正在内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/9e084vdqdw) 进行使用。
- 在使用 CLB 中的 QUIC 协议前，需已 [购买负载均衡实例](https://buy.cloud.tencent.com/lb)。
>? 购买的负载均衡实例应满足：
> - 当前支持 QUIC 的地域为：孟买。
> - 当前只有公网负载均衡支持 QUIC 协议，内网负载均衡和传统型负载均衡暂不支持。

<span id="making"></span>
## 操作步骤
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，在左侧导航栏，单击【实例管理】，进入“实例管理”页面。
2. 在“实例管理”页面中，单击【负载均衡】，进入“负载均衡”标签页。
3. 在“负载均衡”标签页中，找到创建地域为“孟买”的公网负载均衡实例，在右侧操作栏，单击【配置监听器】，进入“监听器管理”页面。
![](https://main.qcloudimg.com/raw/75be8dabe196036bd401a3f874fbf194.png)

4. 在“监听器管理”页面的 "HTTP/HTTPS 监听器" 下，单击【新建】，进入“创建监听器”页面。
![](https://main.qcloudimg.com/raw/c84fbc4b37c063b8c13625d87e332df0.png)

5. 在“创建监听器”页面，切换监听协议端口为 HTTPS，根据需要填写完后，单击【提交】，如下图所示。
![](https://main.qcloudimg.com/raw/c1e32add2ab92d9f7866934784179923.png)

6. 在【监听器管理】标签页，单击该新建监听器的【+】符号，如下图所示。
![](https://main.qcloudimg.com/raw/9fdb02a7a98cddbf6eafa1c95c36b93a.png)

7. 进入“创建转发规则”页面，打开 QUIC 协议，创建七层规则，单击【下一步】，继续完成健康检查和会话保持的配置。
![](https://main.qcloudimg.com/raw/53dae3e54d774586d7e3ac31d7431b6c.png)
