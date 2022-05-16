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
使用 [强制跳转功能](https://cloud.tencent.com/document/product/228/41688)。HTTPS 证书配置成功后，可以开启 Http->Https 功能，开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 进行访问。
![](https://main.qcloudimg.com/raw/7161b36b260f3af2d75931b2e567295d.png)


[](id:q6)
### 配置了 CDN，HTTPS 无法访问？

要使用 HTTPS 访问，操作如下：
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧导航栏的 【域名管理】 进入域名管理页面。单击域名右侧【管理】按钮，进入管理页面。
![](https://main.qcloudimg.com/raw/63c5127bf5c12d7aa0be52e6ba1a2e31.png)
2. 单击【Https 配置】，找到 HTTPS 配置模块。单击【前往配置】，跳转至证书管理页面配置证书。配置流程请参阅 [证书配置](https://cloud.tencent.com/document/product/228/41687#.E8.AF.81.E4.B9.A6.E9.85.8D.E7.BD.AE)。
![](https://main.qcloudimg.com/raw/88bcf378321ca664572f9ecfca3cf6ad.png)
证书配置成功后即可开启 HTTPS 访问。


### CDN 支持哪些 TLS 版本
您好，腾讯云 CDN 默认开启TLS 1.0/1.1/1.2 ，关闭 TLS 1.3，您可按需关闭/开启指定 TLS 版本。

>!
>- 配置前需确保已成功配置 HTTPS 证书。
>- TLS 版本配置暂不支持中国境外。若域名的加速区域为全球，则配置变更后仅生效中国境内。
>- 部分平台正在升级中，暂未开放此配置功能。
>- 只可开启连续或单个版本号。例如，不可仅开启1.0和1.2而关闭1.1。
>- 不可关闭全部版本。如需配置可参考文档 [配置指南](https://cloud.tencent.com/document/product/228/44868)。

###  CDN 如何开启 QUIC？
CDN 支持 QUIC，如何开启请参考  [QUIC](https://cloud.tencent.com/document/product/228/51800)。


###  CDN 是否支持证书证书自动续签？
 自定义上传证书和您于 SSL 控制台申请的免费证书暂不支持自动续签新的证书，若您于 SSL 控制台购买了多年期证书可实现自动签发第二张证书，详情见 [多年期证书方案说明](https://cloud.tencent.com/document/product/400/72804)。

###  CDN 支持 HTTP 2.0吗？
客户端到 CDN 节点已支持 HTTP 2.0，开启 HTTP 2.0 前请先配置 HTTPS 证书，CDN 节点回源到源站不支持 HTTP2.0。

###  如何批量配置 CDN 证书？
若您拥有多域名证书或泛域名证书，可适用于多个 CDN 加速域名，您可以通过批量配置，一次性为多个域名添加配置。

请参考证书管理中的 [批量配置证书](https://cloud.tencent.com/document/product/228/41687#.E6.89.B9.E9.87.8F.E9.85.8D.E7.BD.AE) 。

### 如何查看 HTTPS 请求数的使用情况
您可在控制台通过**实时监控** > **访问监控** ，在 HTTP 协议选择 HTTPS 单击**查询**即可获取到 HTTPS 使用数据。
![](https://qcloudimg.tencent-cloud.cn/raw/60b0948bc41374cafd93fe74c6a8e32c.png)

###  CDN 上的 HTTPS 证书和源站服务器的证书冲突了怎么办？
CDN 上的 HTTPS 证书和源站服务器上的 HTTPS 证书两者是独立存在的，不会影响。


