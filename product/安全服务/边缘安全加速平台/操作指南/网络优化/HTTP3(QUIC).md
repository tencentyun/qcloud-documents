## 功能简介
支持 HTTP/3 (QUIC) 请求，使用 HTTP/3 (QUIC) 加速站点请求，提升数据传输效率及安全性。

#### 什么是 QUIC ？
QUIC（Quick UDP Internet Connections）是一个通用的网络协议，提供几乎等同于 TCP 连接的可靠性，但大大减少传输和连接时的延时，避免网络拥塞，同时能够保障网络安全性。

EdgeOne 当前支持的 QUIC 版本有：h3-29、h3-Q050、h3-Q046、h3-Q043、Q046、Q043。

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **网络优化**。
>?目前边缘安全加速平台控制台仅对部分用户开放，如需访问控制台，请 [联系我们](https://cloud.tencent.com/online-service) 开通权限。
>
3. 在网络优化页面，选择所需站点，单击 HTTP/3 (QUIC) 模块的“开关”，开启或关闭 HTTP/3 (QUIC) 功能。
![](https://qcloudimg.tencent-cloud.cn/raw/8091a9a754ea261a20135ed4cb202c5d.png)
**参数说明：**
 - 关闭状态（默认）：不支持 HTTP/3 (QUIC) 请求。
 - 开启状态：支持 HTTP/3 (QUIC)  请求，使用 HTTP/3 (QUIC) 加速站点请求。
>!
>- 仅配置 HTTPS 证书后才生效，请先配置 HTTPS 证书。
>- 超出套餐内额度的 HTTP/3 (QUIC) 请求数将单独按量后付费。

## 注意事项
1. 若同时开启 HTTP/2 和 HTTP/3 (QUIC) ，则根据实际客户端请求使用 HTTP/2 或 HTTP/3 (QUIC)。
2. 此处仅支持请求访问，不支持 HTTP/3 (QUIC) 回源。
