TLS 协议版本包括 TLSv1.0、TLSv1.1、TLSv1.2、TLSv1.3 等，您可根据您的实际需求在腾讯云相关产品或服务器 Web 服务上设置证书的 TLS 协议版本。

### 腾讯云相关产品
如果您的证书部署到以下腾讯云产品，请参考以下文档进行配置：
- 负载均衡（CLB）：[HTTPS 转发配置入门指南](https://cloud.tencent.com/document/product/214/6534)
- 内容分发网络（CDN）：[TLS 版本配置](https://cloud.tencent.com/document/product/228/44868)

### 服务器 Web 服务
如果您的证书安装在服务器 Web 服务上，请在 Web 服务的证书配置文件中找到 `ssl_protocols TLSv1 TLSv1.1 TLSv1.2`，并根据实际需求进行修改。
例如：您的证书需要支持 TLSv1.1 和 TLSv1.2 版本，则在 `ssl_protocols TLSv1 TLSv1.1 TLSv1.2` 中去掉 `TLSv1` 即可。


