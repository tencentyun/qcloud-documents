## 认证方式
### 企业自建应用（jwt）
腾讯会议面向企业 IT、ISV 系统集成商、SaaS 服务商提供开放接口，实现企业办公平台与腾讯会议的连接。
购买腾讯会议商业版、教育版或企业版，将自动开通企业自建应用的接入能力，创建企业自建应用后可获取调用API的密钥对，具体操作指引请参见：[企业自建应用接入指引](https://cloud.tencent.com/document/product/1095/83667)，密钥对示例如下：
- SecretId：AKID****EXAMPLE
- SecretKey： Gu5t****EXAMPLE

>!SecretId 和 SecretKey 是您调用 API 的重要凭证，请妥善保管，切勿泄漏。


### 第三方应用开发（OAuth2.0 授权）
#### 授权说明
1. OAuth 2.0允许应用程序访问腾讯会议 API 接口。
2. 在用户授权后，开发者可以获取到一个网页授权特有的接口调用凭证（网页授权 access_token），通过网页授权 access_token 可以进行授权后接口调用，例如：获取用户基本信息等。
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/b21d14055ae92035f80d4c1719e6e25e.png" />



#### 授权步骤
1.  用户同意授权，获取 auth_code。
2.  通过 auth_code 换取授权 access_token。
3.  刷新 access_token（如有需要请进行刷新）。
4.  拉取用户信息（检验凭证是否有效）。

具体的接口调用方式请参见：[第三方应用鉴权（OAuth2.0）](https://cloud.tencent.com/document/product/1095/51257)
