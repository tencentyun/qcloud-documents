### 1. 什么是 HTTPS？
HTTPS，是指超文本传输安全协议（Hypertext Transfer Protocol Secure），是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 CDN 节点，实现全网数据加密传输功能。

### 2. CDN 是否支持 HTTPS 配置？
腾讯云 CDN 目前已经全面支持 HTTPS 配置。您可以上传自有证书进行部署，或前往 [证书管理](https://console.cloud.tencent.com/ssl ) 控制台申请由亚洲诚信免费提供的第三方证书。

### 3. 如何配置 HTTPS 证书？
您可以在 CDN 控制台中配置 HTTPS 证书，详情请参阅 [HTTPS 配置](https://cloud.tencent.com/document/product/228/6295)。

### 4. 源站的 HTTPS 证书更新了，CDN 上需要同步更新吗？
由您的回源方式决定：
HTTP 回源：不需要。
HTTPS 回源：源站更新证书，CDN 节点也需要同步更新。客户端到节点，节点到源站证书是需要一致的，否则会导致回源失败。

### 5. CDN 有没有方法让用户控制只允许 HTTPS 访问，禁止 HTTP 访问？
使用强制 HTTPS 功能。证书配置成功后，会出现【强制跳转】开关，开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 进行访问。
![](https://mc.qcloudimg.com/static/img/8dc758129896bef56c85a8528371e9e7/force_https.png)