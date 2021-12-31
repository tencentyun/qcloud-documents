QUIC 协议能帮您大幅提升 App 访问速度，在弱网络、Wi-Fi 和4G频繁切换等场景下，无需重连即可实现多路复用。本文档将为您介绍，如何在负载均衡控制台中，配置 QUIC 协议。
## QUIC 概述
[QUIC](https://www.chromium.org/quic)（Quick UDP Internet Connection），又称为快速 UDP 互联网连接，是由 Google 提出的使用 UDP 进行多路并发传输的协议，QUIC 相比现在广泛应用的 TCP+TLS+HTTP2 协议有如下优势：
- 减少连接建立时间。
- 改善拥塞控制。
- 避免队头阻塞的多路复用。
- 连接迁移。

CLB 开启 QUIC 后，客户端可以和 CLB 之间建立 QUIC 连接，当二者协商无法建立 QUIC 连接时自动降级到 HTTPS 或 HTTP/2，但 CLB 和后端服务器之间仍然使用 HTTP1.x 协议。


## 使用限制
- 目前 CLB 中的 QUIC 协议正在内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/9e084vdqdw) 进行使用。
- 仅广州、上海、北京及孟买地域支持 QUIC。
- 仅负载均衡实例类型支持，传统型负载均衡实例类型不支持。
- 仅公网负载均衡支持，内网负载均衡暂不支持。
- 仅 IPv4、IPv6 NAT64 版本的负载均衡支持，IPv6 版本的暂不支持。
- 仅公网负载均衡的七层 HTTPS 监听器支持 QUIC 协议。
- QUIC 仅支持单可用区 CLB 实例，不支持多可用区。
- 当前 CLB 支持的 QUIC 版本有：Q050、Q046、Q043、h3-29 和 h3-27。

## 操作步骤[](id:making)
1. 根据需求创建负载均衡实例，详情请参见 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)。
>?在创建负载均衡实例时，创建地域选择“北京”、“上海”或“孟买”，网络类型选择“公网”。
>
2. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，在左侧导航栏，单击**实例管理**。
2. 在“实例管理”页面中，单击**负载均衡**。
3. 在“负载均衡”标签页中，找到创建地域为“北京”、“上海”或“孟买”的公网负载均衡实例，在右侧操作栏，单击**配置监听器**。
![](https://main.qcloudimg.com/raw/75be8dabe196036bd401a3f874fbf194.png)
4. 在“监听器管理”页面的 "HTTP/HTTPS 监听器" 下，单击**新建**。
![](https://main.qcloudimg.com/raw/c84fbc4b37c063b8c13625d87e332df0.png)
5. 在“创建监听器”页面，切换监听协议端口为 HTTPS，根据需要填写完后，单击**提交**。
![](https://main.qcloudimg.com/raw/c1e32add2ab92d9f7866934784179923.png)
6. 在**监听器管理**标签页，单击该新建监听器的**+**符号。
![](https://main.qcloudimg.com/raw/9fdb02a7a98cddbf6eafa1c95c36b93a.png)
7. 在“创建转发规则”页面，打开 QUIC 协议，创建七层规则，并填写相关字段后，单击**下一步**，即可完成基本配置。
>?
>- 创建新的 HTTPS 转发规则时，支持开启 QUIC 协议。创建完成后，QUIC 协议可以自由开启或关闭。若创建 HTTPS 转发规则时未开启 QUIC 协议，则创建后不支持开启。
>- QUIC 使用 UDP 协议，会占用 CLB 的 UDP 端口，即 HTTPS 监听器开启 QUIC 协议后，自动占用对应的 UDP 端口和 TCP 端口。例如，当 HTTPS:443 监听器开启 QUIC 协议后，该规则会同时占用 TCP:443 和 UDP:443 端口，因此您不能再创建 TCP:443 和 UDP:443 监听器。
>
![](https://main.qcloudimg.com/raw/53dae3e54d774586d7e3ac31d7431b6c.png)

## 后续操作
填写完基本配置后，可继续完成 [健康检查](https://cloud.tencent.com/document/product/214/6097) 和 [会话保持](https://cloud.tencent.com/document/product/214/6154) 的相关操作。

