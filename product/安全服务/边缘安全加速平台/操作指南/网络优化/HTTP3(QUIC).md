## 功能简介
支持 HTTP/3 (QUIC) 请求，使用 QUIC 加速站点请求，提升数据传输效率及安全性。

#### 什么是 QUIC ？
QUIC（Quick UDP Internet Connections）是一个通用的网络协议，提供几乎等同于 TCP 连接的可靠性，但大大减少传输和连接时的延时，避免网络拥塞，同时能够保障网络安全性。



## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/teo) ，在左侧菜单栏中，单击**站点加速** > **网络优化**。
2. 在网络优化页面，选择所需站点，单击 HTTP/3 (QUIC) 模块的![](https://qcloudimg.tencent-cloud.cn/raw/bf52db8b606a923a3520e4b745e8e467.png)，开启 HTTP/3 (QUIC) 功能。
 - 关闭状态（默认）：不支持 QUIC 请求。
 - 开启状态：支持 HTTP/3 (QUIC)  请求，使用 QUIC 加速站点请求。
>!仅配置 HTTPS 证书后才生效，请先配置 HTTPS 证书。

## 注意事项
- 若同时开启 HTTP/2 和 HTTP/3 (QUIC) ，则根据实际客户端请求使用 HTTP/2 或 QUIC。
- 此处仅支持请求访问，不支持 HTTP/3 (QUIC) 回源。
