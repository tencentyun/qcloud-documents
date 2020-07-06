## 什么是 QUIC
快速 UDP 互联网连接（quick udp internet connection，QUIC）是由 Google 提出的使用 UDP 进行多路并发传输的协议。QUIC 相比现在广泛应用的 TCP+TLS+HTTP2 协议有如下优势：
- 减少了连接建立的时间；
- 改善拥塞控制；
- 避免队头阻塞的多路复用；
- 连接迁移。

使用 QUIC 协议后，APP 访问速度将得到大幅提升，在弱网络、Wi-Fi 和4G 频繁切换等场景下，不需要重连即可实现多路复用。
## 功能概述
当前 CLB 支持的 QUIC 版本是 Q044及以下 。公网负载均衡的七层 HTTPS 监听器支持 QUIC 协议，其他类型监听器暂不支持。CLB 开启 QUIC 后：
- 客户端可以和 CLB 之间建立 QUIC 连接，当二者协商无法建立 QUIC 连接时自动降级到 HTTPS 或 HTTP/2。
- CLB 和后端服务器之间仍然使用 HTTP1.x 协议。

QUIC 使用 UDP协议，会占用 CLB 的 UDP 端口：
- HTTPS 监听器开启 QUIC 协议后，自动占用对用的 UDP 端口。例如当 HTTPS:443 监听器开启 QUIC 协议后，该规则会同时占用 TCP:443 和 UDP:443 端口，您不能再创建 TCP:443 和 UDP:443 监听器。
- 当前在一个 HTTPS 监听器中，只能对一个域名开启 QUIC 协议。
- 创建新的 HTTPS 监听器时，支持开启QUIC；创建完后，QUIC可以自由的开关。创建时没有开启 QUIC 的监听器，不能再开启 QUIC，更不可能关闭 QUIC。
## 前提条件
已 [购买负载均衡实例](https://buy.cloud.tencent.com/lb)。
>? 
> - CLB 支持 QUIC 协议。当前内测中，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/9e084vdqdw)。
> - 当前支持 QUIC 的地域为：孟买。
> - 当前只有公网负载均衡支持 QUIC 协议，内网负载均衡和传统型负载均衡暂不支持。

## 操作步骤
1. 创建 HTTPS 监听器时。
![](https://main.qcloudimg.com/raw/1ac3f012eaafb629fc0e10a8aee2ad57.png)
2. 创建七层规则，并打开 QUIC 协议，单击【下一步】，继续完成健康检查和会话保持的配置。
![](https://main.qcloudimg.com/raw/3c4f93680b2aaf134037e5d80a4c6830.png)
