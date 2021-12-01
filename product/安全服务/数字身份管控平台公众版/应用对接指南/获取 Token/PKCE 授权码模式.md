## 接口描述
应用系统通过 PKCE 授权码模式获得认证门户返回的 `code` 之后，调用此接口获取 Access Token 和 ID Token，完成登录。




## 请求方法
POST

## 请求路径
```
/oauth2/token
```

## 请求示例
```
POST /oauth2/token HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
client_id=TENANT_CLIENT_ID&grant_type=authorization_code&code=MOCK_CODE&redirect_uri=https%3A%2F%2FTENANT.APP.DOMAIN%2Flogin%2Foauth2%2Fcode%2FTENANT_APP_ID&code_verifier=MOCK_CODE_VERIFIER
```


## 请求参数

| 参数          | 可选  | 描述                                                         |
| :------------ | :---- | :----------------------------------------------------------- |
| client_id     | false | 应用的 `client_id` 。需要与获取授权时使用的一致。              |
| grant_type     | false | 填固定值 `authorization_code`。                              |
| code          | false | 获取授权时返回的授权码。                                     |
| redirect_uri  | false | 授权成功后的重定向地址。需要与获取授权时指定的地址一致。     |
| code_verifier | false | PKCE code_verifier 。需要与获取授权时用于生成 code_challenge 的 code_verifier 一致。 |


## 响应参数
| 参数          | 数据类型 | 描述                                 |
| :------------ | :------- | :----------------------------------- |
| access_token  | String   | OAuth 2.0 Access Token (JWT)。       |
| refresh_token | String   | OAuth 2.0 Refresh Token。            |
| scope         | String   | Access Token 的 Scope。              |
| id_token      | String   | OIDC ID Token (JWT)。                |
| token_type    | String   | Token 类型，目前取固定值 `Bearer` 。 |
| expires_in    | Number   | Access Token 有效期，单位秒。        |


## 正常响应示例
```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "access_token" : "eyJraWQiOiJkNDliYzUwNS01NTcyLTRlZDYtOWU0OC0zODhjM2Q0NGJiNDYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJOQU1FIiwiYXVkIjoiVEVOQU5UX0NMSUVOVF9JRCIsIm5iZiI6MTYzNjQ0OTIzMiwic2NvcGUiOlsib3BlbmlkIl0sImlzcyI6Imh0dHBzOlwvXC9URU5BTlQuUE9SVEFMLkRPTUFJTiIsImV4cCI6MTYzNjQ0OTUzMiwiaWF0IjoxNjM2NDQ5MjMyLCJqdGkiOiI0NjkyNTUxMC1mNjY0LTQzNTktODIyYS1jMTdiNTlmNzNhOGUifQ.mmM6iEiGCLIURqaKaJV_LbddUP1i5wCJMJvuasM8i6Wu_Ynix0W_EeghvMcQ94QvLhNYq2KshGQlkl0N5186KCqpHpG6z2ZXbuP35oY4yRFNvhqWOt8drvyxw13aVfehk1_KPLLDgrKGmHTUgxNDvssQq1u6Xd7QxPz0_d0jnaosl78pIO_tV-auGMhYQo6SHHMbFHgJLYBlPUq81eBknqbu8W9Omr4FuDmzlr9VFI4grJ_guxlUuri8lx-C4mRtSbg6bfUYlH7PuAM8bDfaOZ_qhAQ9-KTYF-ZiShDnuJMlVz0u_97ky5kNm_IUOrH6XzWfGL8MboYLagxOHmzNMQ",
  "refresh_token" : "8FuXWpwMZI9oA8ASvCUrqap61N7RvPON6DjWFk-Saiv4dOR8y2tNf9eKf36woAaWYKwW99bpBAQVNWA7P8yM9jiBiGcix42ttYzvRoeMoEBoqYInBgnNMC8jTRTrKDEq",
  "scope" : "openid",
  "id_token" : "eyJraWQiOiJkNDliYzUwNS01NTcyLTRlZDYtOWU0OC0zODhjM2Q0NGJiNDYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJOQU1FIiwiYXVkIjoiVEVOQU5UX0NMSUVOVF9JRCIsImF6cCI6IlRFTkFOVF9DTElFTlRfSUQiLCJpc3MiOiJodHRwczpcL1wvVEVOQU5ULlBPUlRBTC5ET01BSU4iLCJleHAiOjE2MzY0NTEwMzIsImlhdCI6MTYzNjQ0OTIzMiwianRpIjoiMGMzODNiZTktOGFiNy00YzEwLTg5NWQtMzYwNjgzODg3MmZiIn0.i4Zywl6O5KF7iiivV-8d4Yok7CZr_eQNI8mTS3BkaRCIKiMzXJ55-T55XEonOViUE7s_Z4eMlyInm5-oLmk36NXrkO460LHEwxr8o5BlAnMhC4bd7xX3U3JrQISi6CpJxEn0UXXfJrtHnmR-yxAGNLFkoijM_qV1KWe6Y_OxxKe4FPfM2PwjYACt-XQgs4JsJOQk_UiSnHnvyvbpWTB8ZZriIwwxrNErZxdr09HBWhsQQ5fjJNviSilNLKD5fYYMz0yhl-YxDgMJ7s9tnfpDsNXyX25VpFtjdL4L13d1VAMPs2F5fTFBHX-p9LjoqF2sIJFEBbapgOX5EO-E_v1IFQ",
  "token_type" : "Bearer",
  "expires_in" : 299
}
```
>?CIAM 返回的是 JWT 格式的 Access Token 和 ID Token，使用 Token 前需对 JWT 进行解密与验证。请参考 [RFC 9068 ](https://www.rfc-editor.org/rfc/rfc9068.html)和[ OIDC 官方文档 ](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation)对 JWT 进行解密与验证。也可以直接使用相关的开发库完成解密验证。验证所需的公钥通过调用 [获取 JWT 公钥 ](https://cloud.tencent.com/document/product/1441/64397)接口获得。

## 异常响应示例
- client_id 参数缺失或有误。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
{
  "error" : "invalid_request"
}
```

- client_id 与获取授权和获取 Token 时使用的不一致。
```
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=UTF-8
{
  "error" : "invalid_client"
}
```

- response_type 参数缺失或有误。
```
HTTP/1.1 401 Unauthorized
```
- code_verifier 参数有误。
```
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=UTF-8
{
  "error" : "invalid_client"
}
```
