## 接口描述
将用户（浏览器）重定向到此接口地址，发起登录。CIAM 会将用户重定向到认证门户进行登录认证。登录成功后，CIAM 将用户重定向到   `redirect_uri` 参数指定的地址。

如果发起登录时用户已经登录，则无需再次登录，CIAM 会直接将用户重定向到 `redirect_uri`。
>?
>- 根据 OAuth 协议的安全最佳实践要求，本接口使用 PKCE 授权码模式。
>- 本节请求示例中使用的应用系统 Redirect URI 为 `https://example.com/callback`。

## 支持的应用类型
Web 应用、单页应用、移动 App。

## 请求方法
```
GET
```

## 请求路径
```
/oauth2/authorize
```

## 请求示例
```
GET /oauth2/authorize?scope=openid&client_id=TENANT_CLIENT_ID&redirect_uri=https%3A%2F%2FTENANT.APP.DOMAIN%2Flogin%2Foauth2%2Fcode%2FTENANT_APP_ID&response_type=code&state=MOCK_STATE&code_challenge_method=S256&code_challenge=MOCK_CODE_CHALLENGE&auth_source_id=MOCK_USERNAME_PASSWORD_AUTH_SOURCE_ID HTTP/1.1
Host: sample.portal.tencentciam.com
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
| code_challenge        | false | PKCE code_challenge ，计算方法请参考 [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)。 |
| auth_source_id       | true | 使用特定的认证源登录。如果此参数为空，则显示默认登录页面。   |


## 正常响应示例
- 用户未登录，显示认证门户的默认登录页面。
```
HTTP/1.1 302 Found
Location: https://sample.portal.tencentciam.com/portal/login?p_state=MOCK_LOGIN_PORTAL_STATE
```
- 用户已登录，携带授权码和 state 参数重定向到应用回调地址。
```
HTTP/1.1 302 Found
Location: https://example.com/callback?code=DVtNBg5XGqeu2IytLi6WOWwfh7pRc5jqI8vUb2K8k_2OryR2OsYN3260DwhlTDqEMtUSD1XN6gNuRDjYQ25nJX6H8MzfpIxJHIoi0tdtkXfRpV1ELhmw7behuwYraTlC&state=MOCK_STATE
```
>?应用回调地址拿到 code 参数后，需要调用 [ PKCE 模式 获取 Token](https://cloud.tencent.com/document/product/1441/64396) 口获取 Access Token 和 ID Token，完成登录。
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
Location: https://example.com/callback?error=invalid_request&error_description=OAuth%202.0%20Parameter:%20code_challenge_method&error_uri=https://datatracker.ietf.org/doc/html/rfc7636%23section-4.4.1&state=MOCK_STATE
```
