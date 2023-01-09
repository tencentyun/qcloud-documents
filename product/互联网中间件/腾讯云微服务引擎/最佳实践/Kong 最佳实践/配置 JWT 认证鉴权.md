

## 操作场景
JWT（JSON Web Token） 是现代 Web 服务中经常用到的认证和授权方式。Kong 能够验证使用 HS256 或 RS256 签名的 JWT 的请求。您可以为消费者配置 JWT 凭据（公钥和私钥），并用这些凭据签署他们的 JWT。 Kong 支持通过 Query、Cookie、Header 传递 JWT Token。如果 JWT 的签名通过验证，Kong 将把请求代理到上游服务，否则将丢弃请求。
JWT 常见的三种签名算法为 HS256、RS256 和 ES256，区别在于消息签名与签名验证需要的 key 不同。
- HS256 使用同一个 secret_key 进行签名和验证，适用于集中式认证场景，签名和验证都必须由可信方进行。
- RS256 是使用 RSA 私钥进行签名，使用 RSA 公钥进行验证，因此可以将验证委托给其他应用。
- ES256 使用私钥签名，公钥验证，但是拥有更短的签名长度。

本文介绍如何在 Kong 云原生 API 网关上通过 JWT 插件实现下述常见 JWT 认证鉴权场景：
- 对使用 HS256 签名的请求进行认证鉴权。
- 对使用 RS256 签名的请求进行认证鉴权。

## 前置条件
- 已购买 Kong 网关实例，详情请参见 [实例管理](https://cloud.tencent.com/document/product/1364/72495)。
- 配置了后端（Service）以及路由（Route）。

## 插件配置

| 字段名称 | 字段说明 |
|---------|---------|
| uri param names | 用于获取 JWT Token 的 Query 参数列表，当 JWT Token 配置在 URI 时，设置此属性。 |
| cookies names | 用于获取 JWT Token 的 Cookie 参数列表，当 JWT Token 配置在Cookie时，设置此属性。 |
| key claim name | Credential 的 key 值，对应的 JWT Claim 的内容，默认为 iss。 |
| secret is base64 | Credential 的 secret 是否进行 base64 编码。 |
| claims to verify | Kong 进行校验的 Claims，支持 exp 或 nbf。 |
| anonymous | 认证失败时，判断是否作为匿名Consumer。默认为空，表明请求失败时返回4xx。 |
| run on preflight | 插件是否应在 OPTIONS 预检请求上运行（并尝试进行身份验证）。 如果设置为 false，则将始终允许 OPTIONS 请求。 |
| maximum expiration | JWT Token 过期时间，支持0-31536000（365天）。当设置该值时，需要在 claims to verify 中指定 exp。默认值为0，表示无限期。当 Token 过期时请求将被拒绝，返回 HTTP 403。请注意，配置该值时应考虑潜在的时钟偏差。 |
| header names | 用于获取 JWT Token 的 Header 参数列表。当 JWT Token 配置在 URI 时，设置此属性。 |


## 操作步骤
### 场景一：对使用 HS256 签名的请求进行认证鉴权
#### 步骤1：创建 Consumer
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要配置限流插件的 Kong 网关实例详情页，在配置管理页查看管理控制台登录方式。
2. 登录到 Konga 控制台，进入 Consumer 详情页，选择需要配置访问控制的用户（如clare），单击 **Credentials Tab**，选择 JWT，单击 **创建 JWT**，为该用户创建一个 JWT Token 作为访问凭证。
![](https://qcloudimg.tencent-cloud.cn/raw/c3be32d6c35e3fe3f156c144cb80b2a0.png)
3. 配置 JWT 相关参数。
<table>
<thead>
<tr>
<th>配置项</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td>对应 JWT Claims 的 issuer，即签发人。留空则自动生成。</td>
</tr>
<tr>
<td>algorithm</td>
<td>JWT Token 签名所使用的加密算法，支持 HS256 和 RS256。本场景设置为 HS256。</td>
</tr>
<tr>
<td>secret</td>
<td>当签名算法为 HS256 时，设置 secret，用于验证签名，留空则自动生成。</td>
</tr>
</tbody></table>
<img src="https://qcloudimg.tencent-cloud.cn/raw/20e73acd66af23dfea71d643e7f1432a.png" alt=""> 
4. 查看生成的用户凭证。
![](https://qcloudimg.tencent-cloud.cn/raw/ae256cccc834f833d610cd5df8dd6b8e.png)
5. 生成对应的 JWT Token。
![](https://qcloudimg.tencent-cloud.cn/raw/b891967c0a9825eaeeb898909c4b9c6c.png)

#### 步骤2：绑定JWT插件
1. 进入需要认证的 Service，单击 **ADD PLUGIN**，在插件市场的 Authentication 分组中选择 Jwt 插件，单击 **Add Plugin**。
![](https://qcloudimg.tencent-cloud.cn/raw/add3016d6a75f02531f38ff0457198bf.png)
2. 填写 JWT Token 校验的信息，单击 **ADD PLUGIN**。
![](https://qcloudimg.tencent-cloud.cn/raw/8f54d926f016a5243e7e2ed3b8b873a9.png)

#### 步骤3：测试请求
1. 不携带 JWT Token 请求服务，该请求被拒绝，返回401。
<dx-codeblock>
:::  http
curl -i xxxxxxx/test

HTTP/1.1 401 Unauthorized
Connection: keep-alive
Content-Length: 26
Content-Type: application/json; charset=utf-8
Date: Tue, 29 Nov 2022 12:55:33 GMT
Server: kong/2.5.1
X-Kong-Response-Latency: 23

{"message":"Unauthorized"}
:::
</dx-codeblock>
2. 携带 JWT Token 请求服务，请求成功。
<dx-codeblock>
:::  http
curl -i 'http://xxxxxx/test' \
--header 'Authorization: Bearer eyJhbGciOixxxxxxxxxxI6IkpXVCJ9.eyJpc3MiOiJoUXY4eGRtWxxxxxxxxxxxzFoQ0VUQnNySiJ9.APz7Kx9eIiV1CxAJUVt4i4-gvsJ56TtPxxxxxxK67VQ'

HTTP/1.1 200 OK
Connection: keep-alive
Content-Type: application/json; charset=utf-8
Date: Tue, 29 Nov 2022 12:57:38 GMT
Server: apigw/1.0.15
Vary: Accept-Encoding
Via: kong/2.5.1
X-Api-Id: api-1nxxxxkuc
X-Api-Requestid: ab873xxxxd68cac394ddc208
X-Kong-Proxy-Latency: 7
X-Kong-Upstream-Latency: 6
Content-Length: 11

hello Kong
:::
</dx-codeblock>


### 场景二：对使用 RS256 签名的请求进行认证鉴权

#### 步骤1：创建 Consumer
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，进入需要配置限流插件的 Kong 网关实例详情页，在配置管理页查看管理控制台登录方式。
2. 登录到 Konga 控制台，进入 Consumer 详情页，选择需要配置访问控制的用户（如clarersa），单击 **Credentials Tab**，选择 JWT，单击 **创建 JWT**，为该用户创建一个 JWT Token 作为访问凭证。
![](https://qcloudimg.tencent-cloud.cn/raw/181c16023b5683d3be69ab8dced6415f.png)
3. 配置JWT相关参数。
<table>
<thead>
<tr>
<th>配置项</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>key</td>
<td>对应 JWT Claims 的 issuer，即签发人。留空则自动生成。</td>
</tr>
<tr>
<td>algorithm</td>
<td>JWT Token 签名所使用的加密算法，支持 HS256 和 RS256。本场景设置为 RS256。</td>
</tr>
<tr>
<td>rsa_public_key</td>
<td>当签名算法为 RS256 时，设置公钥（PEM 格式），用于验证签名。</td>
</tr>
<tr>
<td>secret</td>
<td>当签名算法为 RS256 时，设置私钥（PEM 格式），用于验证签名。</td>
</tr>
</tbody></table>
<img src="https://qcloudimg.tencent-cloud.cn/raw/ce3c38fe6879c21f805605a7b31daa43.png" alt=""> 
4. 查看生成的用户凭证。
![](https://qcloudimg.tencent-cloud.cn/raw/1ae3d8c0f730c4c50dee38843036f051.png)
5. 生成对应的 JWT Token。
![](https://qcloudimg.tencent-cloud.cn/raw/617abd63861669aab23d50412b65fe28.png)

#### 步骤2：绑定 JWT 插件
1. 进入需要认证的 Service，单击 **ADD PLUGIN**，在插件市场的 Authentication 分组中选择 Jwt 插件，单击 **Add Plugin**。
![](https://qcloudimg.tencent-cloud.cn/raw/bcb9bdc47d8a9375964910e52e35ad94.png)
2. 填写 JWT Token 校验的信息，单击 **ADD PLUGIN**。
![](https://qcloudimg.tencent-cloud.cn/raw/1d2ea80c8a94c8475d324d0a70ae8919.png)

#### 步骤3：测试请求
1. 不携带 JWT Token 请求服务，该请求被拒绝，返回401。
<dx-codeblock>
:::  HTTP
curl -i xxxxxxx/testrsa

HTTP/1.1 401 Unauthorized
Connection: keep-alive
Content-Length: 26
Content-Type: application/json; charset=utf-8
Date: Tue, 29 Nov 2022 12:55:33 GMT
Server: kong/2.5.1
X-Kong-Response-Latency: 23

{"message":"Unauthorized"}
:::
</dx-codeblock>
2. 携带 JWT Token 请求服务，请求成功。
<dx-codeblock>
:::  HTTP
curl -i 'http://xxxxxx/testrsa' \
--header 'Authorization: Bearer eyJhbGciOixxxxxxxxxxI6IkpXVCJ9.eyJpc3MiOiJoUXY4eGRtWxxxxxxxxxxxzFoQ0VUQnNySiJ9.APz7Kx9eIiV1CxAJUVt4i4-gvsJ56TtPxxxxxxK67VQ'

HTTP/1.1 200 OK
Connection: keep-alive
Content-Type: application/json; charset=utf-8
Date: Tue, 29 Nov 2022 12:57:38 GMT
Server: apigw/1.0.15
Vary: Accept-Encoding
Via: kong/2.5.1
X-Api-Id: api-1nxxxxkuc
X-Api-Requestid: ab873xxxxd68cac394ddc208
X-Kong-Proxy-Latency: 7
X-Kong-Upstream-Latency: 6
Content-Length: 11

hello Kong
:::
</dx-codeblock>

## 参考
更多相关说明请参见 [Kong JWT 插件官方文章](https://docs.konghq.com/hub/kong-inc/jwt/)。

