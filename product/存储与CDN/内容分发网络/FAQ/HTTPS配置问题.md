[](id:q1)
### 什么是 HTTPS？
HTTPS，是指超文本传输安全协议（Hypertext Transfer Protocol Secure），是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 CDN 节点，实现全网数据加密传输功能。

[](id:q2)
### CDN 是否支持 HTTPS 配置？
腾讯云 CDN 目前已经全面支持 HTTPS 配置。您可以上传自有证书进行部署，或前往 [证书管理控制台](https://console.cloud.tencent.com/ssl ) 申请由亚洲诚信免费提供的第三方证书。

[](id:q3)
### 如何配置 HTTPS 证书？
您可以在 [CDN 控制台](https://console.cloud.tencent.com/cdn) 中配置 HTTPS 证书，详情请参见 [HTTPS 配置](https://cloud.tencent.com/document/product/228/41687)。

[](id:q4)
### 源站的 HTTPS 证书更新了，CDN 上需要同步更新吗？
不需要。源站的 HTTPS 证书更新后不会影响 CDN 上的 HTTPS 证书，当您在 CDN 上配置的 HTTPS 证书将要到期或者已经到期时，您才需要在 CDN 上更新 HTTPS 证书。


[](id:q5)
### CDN 有没有方法让用户控制只允许 HTTPS 访问，禁止 HTTP 访问？
使用 [强制扭转功能](https://cloud.tencent.com/document/product/228/41688)。HTTPS 证书配置成功后，可以开启 Http->Https 功能，开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 进行访问。
![](https://main.qcloudimg.com/raw/7161b36b260f3af2d75931b2e567295d.png)


[](id:q6)
### 配置了 CDN，HTTPS 无法访问？

要使用 HTTPS 访问，操作如下：
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧导航栏的 【域名管理】 进入域名管理页面。单击域名右侧【管理】按钮，进入管理页面。
![](https://main.qcloudimg.com/raw/63c5127bf5c12d7aa0be52e6ba1a2e31.png)
2. 单击【Https 配置】，找到 HTTPS 配置模块。单击【前往配置】，跳转至证书管理页面配置证书。配置流程请参阅 [证书配置](https://cloud.tencent.com/document/product/228/41687#.E8.AF.81.E4.B9.A6.E9.85.8D.E7.BD.AE)。
![](https://main.qcloudimg.com/raw/88bcf378321ca664572f9ecfca3cf6ad.png)
证书配置成功后即可开启 HTTPS 访问。



