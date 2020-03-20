## OAuth2.0 概述
OAuth 2.0 是一个开放授权标准，它允许用户让**第三方应用**访问该用户在某服务的**特定私有资源**但是**不提供账号密码信息**给第三方应用。
>?OAuth2.0 是一个授权协议，不是认证协议。

### OAuth2.0 角色说明
OAuth2.0 有以下四个角色： 
- Resource Owner：资源拥有者。
- Resource Server：资源服务器。
- Client：第三方应用客户端，指任何可以消费资源服务器的第三方应用。
- Authorization Server：授权服务器，管理上述三个角色的中间层。

### 授权流程
![](https://main.qcloudimg.com/raw/27814a835f31fd1511ef3247764ee1c7.png)
（A）：客户端请求资源所有者的授权。
（B）：资源所有者同意授权。
（C）：客户端获得了资源所有者的授权之后，向授权服务器申请授权令牌
（D）：授权服务器验证客户端无误后发放授权令牌
（E）：客户端拿到授权令牌之后请求资源服务器发送用户信息
（F）：资源服务器验证令牌无误后将用户信息发放给客户端

### Authorization Grant
- 授权许可是一个代表资源所有者授权（访问受保护资源）的凭据，客户端用它来获取访问令牌。
- Authorization Code：授权码。Client 需要提供 Server 来处理授权码（API 网关授权许可方式）。 

![](https://main.qcloudimg.com/raw/640b58465144331573827f22d997f2af.png)
（A）Client 使用浏览器（用户代理）访问 Authorization Server。
（B）Authorization Server 验证 Client 在（A）中传递的参数信息，如果无误则提供一个页面供 Resource Owner 登录。
（C）在（B）无误后返回一个授权码给 Client。
（D）Client 拿着（C）中获得的授权码和客户端标识、重定向 URL 等信息作为参数，请求 Authorization Server 提供的获取访问令牌的 URL。
（E）Authorization Server 返回访问令牌和可选的刷新令牌以及令牌有效时间等信息给 Client。
- Implicit：隐式许可省掉了授权码，直接返回 Token。适用于没有 Server 服务器来接受处理 Authorization Code 的第三方应用。
- Resource Owner Password Credentials：资源所有者密码凭据，直接使用 Owner 账号密码请求 Token。
- Client Credentials ：客户端凭据，客户端提供自己的身份参数直接获得 Token。

###  OIDC 说明
- OIDC（OpenID Connect） 是在 OOAuth2.0 上构建的一个身份层，是一个基于 OAuth2.0 协议的身份认证标准协议。
- OAuth 2.0 定义了一些机制用于获取和使用访问令牌来访问受保护资源，但未定义用于提供标识信息的标准方法。 
- OIDC 以 id_token 的形式提供有关最终用户的信息，可验证用户的标识，并提供有关用户的基本配置文件信息。

#### id_token
- OIDC 对 OAuth2.0 最主要的扩展就是提供了 ID Token。
- ID Token 是一个安全令牌，是一个授权服务器提供的包含用户信息（由一组 Cliams 构成以及其他辅助的 Cliams）的 JWT 格式的数据结构。
- JWT（JSON Web Token）：是一个定义一种紧凑的，自包含的并且提供防篡改机制的传递数据的方式的标准协议。**API 网关校验的是 JWT 标准生成 id_token。**


| 参数 | 英文全称 | 是否必选 | 说明 | 取值要求 | 
|---------|---------|---------|---------|---------|
| iss | Issuer Identifier | 是 | 提供认证信息者的唯一标识。 | 一般是一个 HTTPS 的 URL（不包含 querystring 和 fragment 部分）
| ѕub | Ѕubjесt ldеntіfіеr | 是 | iss 提供的 EU 的标识，在 iss 范围内唯一。它会被 RP 用来标识唯一 的用户。| 最长为255个 ASCII 字符|
| aud | Audience(s) | 是 | 标识 ID Token 的受众。 | 必须包含 OAuth2 的 client_id |
| exp | Expiration time | 是 | 过期时间，超过此时间的 ID Token 会作废不再被验证通过。 | - |
| iat | Issued At Time | 是 | JWT 构建的时间。 | - |
| auth_ time | AuthenticationTime | 否 | EU 完成认证的时间 。如果 RP 发送 AuthN 请求的时候携带 max_age 的参数，则此 Claim 是必须的。| - |
| nоnсе | - | 否 |RP 发送请求的时候提供的随机字符串，用来减缓重放攻击，也可以来关联  ID Token 和 RP 本身的 Session 信息。 | - |
| асr | Аuthеntісаtіоn Соntехt Сlаѕѕ Rеfеrеnсе | 否 | 表示一个认证上下文引用值，可以用来标识认证上下文类。 | - |
| amr | Authentication Methods References | 否 | 表示一组认证方法。|- |
| azp | Authorized party | 否 | 结合 aud 使用。只有在被认证的一方和受众（sud）不一致时才使用此值，一般情况下很少使用。 | - |


## API 网关 OAuth2.0 操作方法
API 网关已经对外提供了 OAuth 功能，实践一个 Auth 的 Demo 需要一个 Client 和 AS，可能需要 RS。 
功能需求有两个：
- 授权 API 调用：请求 Token、刷新 Token
- 业务 API 调用（需要一个 RS Demo）直接用 Mock：Client 收发请求，postman 等模拟


#### AS 服务
使用 SpringBoot 快速开发
主要功能：处理授权 API 请求、生成 token_id、刷新 token_id

#### 生成 RSA 公私钥
- 公钥：放在 API 网关，用于验证 JWT 签名。
- 私钥： AS 保存。
![](https://main.qcloudimg.com/raw/b660f7e5858232ac083a0b70269a7d24.png)

JSON 格式输出，满足 JWT Header 头部信息包含两部分：
- kty：代表 Token 类型，这里使用的是 RSA。
- alg：使用 Hash 算法，这里使用的是 RS256。

```
{"kty":"RSA","alg":"RS256","e":"","n":"公钥内容"}
```


#### 生成 id_token
![](https://main.qcloudimg.com/raw/14ae49322bf0768c0e0fadf268e3f27c.png)
- 生成 Token 时，需要用户设置 OIDC 协议定义 JWT 的 payload 中的 Claims 属性(iss, aud, iat, exp, sub)。其中，iat 和 exp 必须设置，其他为非必须设置项。

#### 处理请求 Token
![](https://main.qcloudimg.com/raw/c409e2dc368de85df7f0214addf4354c.png)


#### 刷新 id_token
![](https://main.qcloudimg.com/raw/2d22db82e25c6f961d016fd4e914947a.png)
成功授权显示如下：
![](https://main.qcloudimg.com/raw/8f91cc6bf488f8a319f46973208713e3.png)


#### 演示
先将 AS 服务部署到后台服务器并跑起来，注意如果是部署到 CVM，需要在安全组中开放端口。
- 在 API 管理平台创建授权 API
![](https://main.qcloudimg.com/raw/4c84a7cb40d9878c2020f4011ded148c.png)
- 填入公钥等 OAuth 信息
![](https://main.qcloudimg.com/raw/a9c0d2ff616c005466a66b9a79e99a2d.png)
- 在 API 网关平台创建业务 API，关联授权 API
![](https://main.qcloudimg.com/raw/40bde382b2b56c9bdcee812c6aa2848d.png)
- 发布 API
![](https://main.qcloudimg.com/raw/9dc65429e6bbba8096d21826eedebd49.png)
- 调用授权 API 拿到 id_token
![](https://main.qcloudimg.com/raw/85d98d401e6120297eda0f460e3f0eba.png)
- 使用 id_token 访问业务 API
![](https://main.qcloudimg.com/raw/5c8f2a2d901e79e16e8588ffa5519d75.png)

