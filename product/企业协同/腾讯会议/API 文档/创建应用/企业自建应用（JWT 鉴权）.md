企业自建应用使用 JSON Web Token 鉴权方式。JSON Web Token，是为了在网络应用环境间传递声明而执行的一种基于 JSON 的开放标准（RFC 7519）。该 token 被设计为紧凑且安全的，特别适用于分布式站点的单点登录（SSO）场景。JWT 的声明一般被用来在身份提供者和服务提供者间传递被认证的用户身份信息，以便于从资源服务器获取资源，也可以增加一些额外的其它业务逻辑所必须的声明信息，该 token 也可直接被用于认证，也可被加密。

>!JWT 只能用于内部应用程序的创建和使用，如果您想创建第三方使用的应用，则必须使用 OAuth 类型。

开发人员使用 JSON Web Token 来获取账户级应用的数据权限，允许管理员管理自己的账户和用户信息。


## 创建企业自建应用
- 企业自建应用需账户管理员管理使用，如果您是账户管理员，则可以通过腾讯会议官网 [开放平台](https://meeting.tencent.com/open-api.html) 中的“API” 创建或查看密钥，创建 JWT 验证密钥进行鉴权。
![](https://main.qcloudimg.com/raw/4e5eaacf58f144143b6af66c8dc4426b.png)
- 您也可以登录 [腾讯会议官网](https://meeting.tencent.com/index.html)，在**用户中心 > 高级 > RestAPI**进行应用创建和 JWT 密钥获取。
![](https://main.qcloudimg.com/raw/653073ef3f6cd8ca5f34458320f1eeab.png)

**企业自建应用类型**
企业自建应用分为企业级和应用级类型。
- 企业级类型：企业级可以获取到您企业账户下的所有数据，包括通过腾讯会议 App、腾讯会议 API 接口等不同途径创建的用户数据，也可跨应用获取。
- 应用级类型：应用级则仅能获取该应用所对应的相关数据，无法跨应用获取。

应用创建完成后，您可以通过 AppID、SDKID、SecretKey、SecretID 进行鉴权，完成接口调用。详细鉴权方式请参考 [企业内部应用鉴权](https://cloud.tencent.com/document/product/1095/42413)。

## 事件订阅
1. 启用通知状态，单击**消息通知**后进行事件配置。
![](https://main.qcloudimg.com/raw/df9198bf3ae1f4c08112219097e9945c.png)
2. 单击右上角**添加消息通知**，填写消息通知名称、接收消息通知的 URL 地址、选择需要订阅的事件类型，即可完成消息事件订阅。
![](https://main.qcloudimg.com/raw/629c457fc6a75b1362cd036f23840f3b.png)



