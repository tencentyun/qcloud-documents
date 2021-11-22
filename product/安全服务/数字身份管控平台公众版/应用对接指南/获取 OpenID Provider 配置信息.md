## 接口描述
应用可以通过此接口获取 OIDC 授权服务器的配置信息，从而简化本地配置。具体的配置信息及其含义请参考 [OpenID Connect Discovery 标准](https://openid.net/specs/openid-connect-discovery-1_0.html)。

## 请求方法
GET

## 请求路径
```
/.well-known/openid-configuration
```

## 请求示例
```
GET /.well-known/openid-configuration HTTP/1.1
Host: localhost:8080
```


## 响应参数
| 参数                                  | 数据类型 | 描述                                         |
| :------------------------------------ | :------- | :------------------------------------------- |
| issuer                                | String   | OIDC Issuer。                                |
| authorization_endpoint                | String   | OAuth 2.0 获取授权的服务地址。               |
| token_endpoint                        | String   | OAuth 2.0 获取 Token 的服务地址。            |
| jwks_uri                              | String   | 获取 JWT 公钥的服务地址。                    |
| grant_types_supported                 | Array    | 支持的 OAuth 2.0 Grant Type。                |
| response_types_supported              | Array    | OAuth 2.0 获取授权服务支持的 Response Type。 |
| token_endpoint_auth_methods_supported | Array    | OAuth 2.0 获取 Token 服务支持的认证方式。    |
| subject_types_supported               | Array    | 支持的 OIDC Subject Identifier Type。        |
| id_token_signing_alg_values_supported | Array    | 支持的 JWS 签名算法。                        |
| scopes_supported                      | Array    | 支持的 OAuth 2.0 Scope。                     |





## 正常响应示例
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "issuer" : "https://TENANT.PORTAL.DOMAIN",
  "authorization_endpoint" : "https://TENANT.PORTAL.DOMAIN/oauth2/authorize",
  "token_endpoint" : "https://TENANT.PORTAL.DOMAIN/oauth2/token",
  "token_endpoint_auth_methods_supported" : [ "client_secret_basic", "client_secret_post" ],
  "jwks_uri" : "https://TENANT.PORTAL.DOMAIN/oauth2/jwks",
  "response_types_supported" : [ "code" ],
  "grant_types_supported" : [ "authorization_code", "client_credentials", "refresh_token" ],
  "subject_types_supported" : [ "public" ],
  "id_token_signing_alg_values_supported" : [ "RS256" ],
  "scopes_supported" : [ "openid" ]
}
```


