### 什么是 HTTPS？
HTTPS，是指超文本传输安全协议（Hypertext Transfer Protocol Secure），是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 CDN 节点，实现全网数据加密传输功能。

### CDN 是否支持 HTTPS 配置？
腾讯云 CDN 目前已经全面支持 HTTPS 配置。您可以上传自有证书进行部署，或前往 [证书管理控制台](https://console.cloud.tencent.com/ssl ) 申请由亚洲诚信免费提供的第三方证书。

### 如何配置 HTTPS 证书？
您可以在 CDN 控制台中配置 HTTPS 证书，详情请参见 [HTTPS 配置](https://cloud.tencent.com/document/product/228/41687)。

### 源站的 HTTPS 证书更新了，CDN 上需要同步更新吗？
由您的回源方式决定：
HTTP 回源：不需要。
HTTPS 回源：源站更新证书，CDN 节点也需要同步更新。客户端到节点，节点到源站证书是需要一致的，否则会导致回源失败。

### CDN 有没有方法让用户控制只允许 HTTPS 访问，禁止 HTTP 访问？
使用强制 HTTPS 功能。证书配置成功后，会出现“强制跳转”开关，开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 进行访问。
![](https://main.qcloudimg.com/raw/c5e8ff7861cc4e00baa0e886d7f783c4.png)


### 配置了 CDN，HTTPS 无法访问？

要把网站的 HTTPS 证书上传到 CDN，操作如下：
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧导航栏的 【域名管理】 进入域名管理页面。单击域名右侧【管理】按钮，进入管理页面。
![图片描述](https://main.qcloudimg.com/raw/9f5202ff57eb14f40dee3b15e4a37cdf.png)
2. 单击【高级配置】，找到 HTTPS 配置模块。单击【前往配置】，跳转至证书管理页面配置证书。配置流程请参阅  [证书管理](https://cloud.tencent.com/document/product/228/41687#.E5.9F.9F.E5.90.8D.E9.85.8D.E7.BD.AE) 。![图片描述](https://main.qcloudimg.com/raw/f8c4570d1a4847aab84c30ff0dc2e22d.png)
3. 证书配置成功后，会出现【强制跳转 HTTPS】开关。开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 请求进行访问：
![图片描述](https://main.qcloudimg.com/raw/da5fb8ee7294231e27d65cd177dfd992.png)



