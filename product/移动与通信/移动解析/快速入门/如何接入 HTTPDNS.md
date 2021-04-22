>!如果您不使用 SDK，在接入过程中需要**保留 LocalDNS 的解析方式作为备选**，具体可以参考接入 [最佳实践](/doc/product/379/最佳实践)。

## 1. 开通帐号
首先需要开通移动解析 HTTPDNS 服务，请前往 [控制台](https://console.cloud.tencent.com/httpdns) 开通。具体操作请参见 [开通移动解析 HTTPDNS](https://cloud.tencent.com/document/product/379/54577)。

## 2. 使用 HTTPDNS API 接口解析域名
开通服务后，授权 ID 和加密密钥及 HTTPS Token 将发送至您在腾讯云 [账号中心](https://console.cloud.tencent.com/developer/security) 设置的安全邮箱。
获取授权 ID 和加密密钥及 HTTPS Token 后，可以使用以下方式请求解析：
- HTTPS 加密方式：
` https://119.29.29.99/d?dn=[域名]&token=[HTTPS Token]&ttl=1`
- AES/DES 加密方式：
 `http://119.29.29.98/d?dn=[域名加密后的字符串]&id=[授权ID]&ttl=1`
- 具体加密方式请参见 [加密指引](https://cloud.tencent.com/document/product/379/3530)。
- 具体请求格式请参见 [API 说明](https://cloud.tencent.com/document/product/379/54976)。

## 3. 客户端改造
将客户端的解析方式改为 HTTPDNS 解析，注意在接入过程中需要**保留 LocalDNS 的解析方式作为备选**，具体可以参见接入 [最佳实践](/doc/product/379/最佳实践)。

## 4. 申请 SDK 使用（可选）
使用 HTTPDNS 服务还可以申请 [使用 SDK 接入](https://cloud.tencent.com/document/product/379/12544)，HTTPDNS 服务提供腾讯云自研的 **智营 SDK**，高度定制化、可直接嵌入 App 内调用，已经广泛应用于腾讯各类游戏客户端，功能成熟稳定。

具体可参见以下文档：
[iOS 版本 SDK >>](https://cloud.tencent.com/document/product/379/17669)
[Android 版本 SDK >>](https://cloud.tencent.com/document/product/379/17655)


