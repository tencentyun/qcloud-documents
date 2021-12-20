
### 接口描述
应用可以通过此接口获取 OIDC 授权服务器的配置信息。具体的配置信息及其含义请参考[ OpenID Connect Discovery 标准](https://openid.net/specs/openid-connect-discovery-1_0.html)。
>!如果不使用此接口，则需手动在应用本地存储一份配置信息。
### 请求方法
GET
### 请求地址
```
/auth/.well-known/openid-configuration
```

### 返回参数
| 参数                                  | 参数类型        | 描述                                       |
| ------------------------------------- | --------------- | ------------------------------------------ |
| issuer                                | String          | OIDC Issuer                                |
| authorization_endpoint                | String          | OAuth 2.0 获取授权的服务地址               |
| token_endpoint                        | String          | OAuth 2.0 获取 Token 的服务地址            |
| jwks_uri                              | String          | 获取 JWT 公钥的服务地址                    |
| grant_types_supported                 | Array of String | 支持的 OAuth 2.0  Grant Type               |
| response_types_supported              | Array of String | OAuth 2.0 获取授权服务支持的 Response Type |
| token_endpoint_auth_methods_supported | Array of String | OAuth 2.0 获取 Token 服务支持的认证方式    |
| subject_types_supported               | Array of String | 支持的 OIDC  Subject Identifier Type       |
| id_token_signing_alg_values_supported | Array of String | 支持的 JWS 签名算法                        |
| scopes_supported                      | Array of String | 支持的 OAuth 2.0  Scope                    |

### 接口示例
#### 输入示例
```
https://<auth_domain>/auth/.well-known/openid-configuration
```
#### 返回示例
```
{
  "issuer" : "https://xxxTENANT.PORTAL.DOMAIN",
  "authorization_endpoint" : "https://xxxTENANT.PORTAL.DOMAIN/oauth2/authorize",
  "token_endpoint" : "https://xxxTENANT.PORTAL.DOMAIN/oauth2/token",
  "token_endpoint_auth_methods_supported" : [ "client_secret_basic", "client_secret_post" ],
  "jwks_uri" : "https://xxxTENANT.PORTAL.DOMAIN/oauth2/jwks",
  "response_types_supported" : [ "code" ],
  "grant_types_supported" : [ "authorization_code", "client_credentials", "refresh_token" ],
  "subject_types_supported" : [ "public" ],
  "id_token_signing_alg_values_supported" : [ "RS256" ],
  "scopes_supported" : [ "openid" ]
}
```
