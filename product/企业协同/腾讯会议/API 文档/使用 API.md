
## 认证方式
### 企业内部开发
腾讯会议面向企业 IT、ISV 系统集成商、SaaS 服务商提供开放接口，实现企业办公平台与腾讯会议的连接。
购买腾讯会议企业版或者商业版，将自动开通企业 API 接入能力，企业管理员可登录 [腾讯会议官网](https://meeting.tencent.com/)，在高级选项里创建密钥对，密钥对示例如下：
● SecretId：AKID********************EXAMPLE
● SecretKey： Gu5t********************EXAMPLE

>?高级选项里可以同时获取鉴权时所需要的 APPID 和 SDKID。


### 第三方应用开发（OAuth2.0 授权）
**授权说明**
1. OAuth2.0 允许应用程序访问腾讯会议 API 接口。
>!回调域名只需要填写主域名，而不是 URL，因此请勿加 `http:/`/ 等协议头，请严格按照 `meeting.tencent.com` 该格式填写。

2. 在用户授权后，开发者可以获取到一个网页授权特有的接口调用凭证（网页授权 access_token），通过网页授权 access_token 可以进行授权后接口调用，如获取用户基本信息等。
![](https://main.qcloudimg.com/raw/343b7c3122df48926ffae2004b8e53e4.png)

**授权步骤**
1. 用户同意授权，获取 auth_code；
2. 通过 auth_code 换取授权 access_token；
3. 刷新 access_token（如有需要请进行刷新）；
4. 拉取用户信息（检验凭证是否有效）。

