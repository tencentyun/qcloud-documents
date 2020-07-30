### 什么是 HTTPS？
HTTPS（Hypertext Transfer Protocol Secure）指超文本传输安全协议，是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 GCD 节点，实现全网数据加密传输功能。

### GCD 是否支持 HTTPS 配置？
腾讯云 GCD 已全面支持 HTTPS 配置。您可以前往 [证书管理](https://console.cloud.tencent.com/ssl ) 控制台申请由亚洲诚信免费提供的第三方证书，或上传自有证书进行部署。

### 如何配置 HTTPS 证书？
您可以在 GCD 控制台中证书管理页面配置 HTTPS 证书。

### 源站的 HTTPS 证书更新了，GCD 上需要同步更新吗？
- HTTP 回源：不需要。
- HTTPS 回源：源站更新证书，GCD 节点也需要同步更新。您需要保持客户端 - 节点 - 源站证书一致，否则会导致回源失败。
