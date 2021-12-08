## 接口描述
用户在应用系统的登录页面，单击**登录**或访问受保护资源时，应用系统将用户（浏览器）重定向到此接口地址，发起登录认证。用户将在 CIAM 的认证门户上完成登录认证。登录成功后，认证门户把用户重定向到应用的 `redirect_uri` 地址。
>?根据 OAuth 协议的安全最佳实践要求，本接口使用 PKCE 授权码模式。


## 请求方法
GET

## 请求路径
```
/oauth2/authorize
```

## 请求示例
```
GET /oauth2/authorize?scope=openid&client_id=TENANT_CLIENT_ID&redirect_uri=https%3A%2F%2FTENANT.APP.DOMAIN%2Flogin%2Foauth2%2Fcode%2FTENANT_APP_ID&response_type=code&state=MOCK_STATE&code_challenge_method=S256&code_challenge=MOCK_CODE_CHALLENGE&auth_source_id=MOCK_USERNAME_PASSWORD_AUTH_SOURCE_ID HTTP/1.1
Host: localhost:8080
```


## 请求参数

| 参数                    | 可选    | 描述                                                         |
| :---------------------- | :------ | :----------------------------------------------------------- |
| scope                 | false | 填固定值 `openid`。 |
| client_id            | false | 应用的 `client_id`。可参考 **[应用管理页面](https://console.cloud.tencent.com/ciam/app-management)** > **选定指定应用** > 单击**应用配置** > 对应的“Client Id”。 |
| redirect_uri         | false | 授权成功后的重定向地址。需要与控制台配置的地址一致。         |
| response_type        | false| 填固定值 `code`。                                              |
| state               | true  | 应用随机生成的一个字符串，服务器会以 HTTP 响应参数的形式原样返回给应用。为防止 CSRF 攻击，建议携带此参数。 |
| code_challenge_method | false | 计算 PKCE code_challenge 的算法。目前仅支持固定值 `S256` 。  |
| code_challenge        | false | PKCE code_challenge ，计算方法请参考 RFC 7636，或直接使用开发库来生成。 |
| auth_source_id       | true | 使用特定的认证源登录。如果此参数为空，则显示默认登录页面。   |


## 正常响应示例
- 用户未登录，显示认证门户的默认登录页面。
```
HTTP/1.1 302 Found
Location: http://localhost:8080/portal/login?p_state=MOCK_LOGIN_PORTAL_STATE
```
- 用户已登录，携带授权码和 state 参数重定向到应用回调地址。
```
HTTP/1.1 302 Found
Location: https://TENANT.APP.DOMAIN/login/oauth2/code/TENANT_APP_ID?code=rGdq86P6LQaHb-QA25DTcZKgi_TtGefDDjKNReM_nYtxExn0Nh-46TYGWlIlYXjxo1bDR07kUZQSgzHj_emwbnq5YajUSmBthaXZMCu2QsPBGd4p8t6nc471Wp22kcvp&state=MOCK_STATE
```
>?用户登录成功后，认证门户将把用户重定向到应用的 `redirect_uri` 地址，并在参数中携带授权码 `code`。应用系统获取到 `code` 参数后，调用 [ PKCE 模式 获取 Token](https://cloud.tencent.com/document/product/1441/64396) 接口获取 Access Token 和 ID Token，完成登录。
>

## 异常响应示例
- client_id 参数缺失或有误。
```
HTTP/1.1 400 Bad Request
```

- redirect_uri 参数与注册信息不匹配。
```
HTTP/1.1 400 Bad Request
```

- response_type 参数缺失或有误。
```
HTTP/1.1 400 Bad Request
```
- 不支持的 code_challenge_method。
```
HTTP/1.1 302 Found
Location: https://TENANT.APP.DOMAIN/login/oauth2/code/TENANT_APP_ID?error=invalid_request&error_description=OAuth%202.0%20Parameter:%20code_challenge_method&error_uri=https://datatracker.ietf.org/doc/html/rfc7636%23section-4.4.1&state=MOCK_STATE
```
