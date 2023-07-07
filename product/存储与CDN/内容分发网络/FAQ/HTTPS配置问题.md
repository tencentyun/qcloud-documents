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
>- 只可开启连续或单个版本号。例如，不可仅开启1.0和1.2而关闭1.1。
>- 不可关闭全部版本。如需配置可参考文档 [配置指南](https://cloud.tencent.com/document/product/228/44868)。

###  CDN 如何开启 QUIC？
CDN 支持 QUIC，如何开启请参考  [QUIC](https://cloud.tencent.com/document/product/228/51800)。


###  CDN 是否支持证书自动续签？
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



### 配置HTTPS后还可以使用HTTP访问吗？

配置 HTTPS 后，可同时支持 HTTP 访问和 HTTPS 访问。

### 如何验证 CDN 证书是否部署成功？

证书安装成功并解析至服务器 IP 后，您可以按照以下步骤检查 HTTPS 证书 生效情况：
1. 打开浏览器（以 Chrome 浏览器为例），在浏览器地址栏中以 HTTPS格式 输入证书已绑定的域名地址。
2. 按回车键，访问域名地址。检查是否具备以下情况：
	- 域名地址可以成功访问网站。
	- 浏览器地址栏左侧显示安全锁标志，则说明您的 HTTPS证书 已生效。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fae9dfb37b57128ee07acf039e777fec.png)

### 网站提示证书风险，如何处理？
如果您在 CDN 节点已配置了 HTTPS 证书，但是验证却未生效，可能的原因有：
- 证书已过期。
证书存在有效期，当证书出现过期后会出现证书失效进而导致网站 HTTPS 访问出现异常的情况。
处理方案：您需要前往控制台更换证书，自定义上传证书和您于 SSL 控制台申请的免费证书暂不支持自动续签新的证书，若您于SSL控制台购买了多年期证书可实现自动签发第二张证书，详情见多年期证书方案说明
- 应用了自签名 HTTPS 证书。
非 CA 机构签发，由自己生成的证书称为自签名证书，此类证书不受各大浏览器信任，容易被伪造，存在安全风险。
处理方案：建议您在腾讯云 SSL 控制台申请由 CA 机构颁发的证书。
- 系统时间不正确。
系统时间不正确会导致证书过期或校验不成功 。
处理方案：将系统时间配置正确
- 网页内有 HTTP 链接资源，即网页使用了 HTTP 协议的链接。
如：网页使用了 HTTP 的图片链接
处理方案：将 HTTP 协议链接调整 HTTPS 协议链接
- 过低的 TLS 版本
低版本的 TLS 存在许多安全漏洞，这些漏洞存在被攻击的去安全风险。
处理方案：腾讯云 CDN 默认开启TLS 1.0/1.1/1.2 ，关闭 TLS 1.3，TLSv1.2 和 TLSv1.3 是目前公认的安全性更高的协议，您可根据您的需要关闭 TLS 1.0/1.1，开启 TLSv1.2 和 TLSv1.3。
- 使用了弱密码加密套件。
弱密码套件存在较多安全漏洞，这些漏洞存在被攻击的安全风险。
处理方案：安全加密和身份验证建议您使用128位的 AEC、GCM 配置；密钥交换机制建议使用 ECDHE_RSA。

### 证书过期后怎么办？
![](https://qcloudimg.tencent-cloud.cn/raw/e870f72db6d3c430c07c9213cf84ca9f.png)
1. 如果您的证书属于自有证书，您可通过单击**编辑**更新证书和私钥内容，完成更新后，单击**提交**。
 ![](https://qcloudimg.tencent-cloud.cn/raw/cf359e9e870bd8f9c90c4880ac1ecb0e.png)
2. 如果您的证书属于已托管证书，您可前往 SSL 控制台更新证书，并更新域名和证书的关联关系。
![](https://qcloudimg.tencent-cloud.cn/raw/ff4e4e677b138df76293e3a5420b38a1.png)
