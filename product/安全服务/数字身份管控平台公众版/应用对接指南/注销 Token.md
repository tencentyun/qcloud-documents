## 接口描述
注销 OAuth 2.0 Token 。如果传入的是 access_token ，则仅注销该 access_token；如果传入的是 refresh_token，则该 refresh_token 以及与它相关联的 access_token 都将被注销。


## 请求方法
POST

## 请求路径
```
/oauth2/revoke
```

## 请求示例
```
POST /oauth2/revoke HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
client_id=TENANT_CLIENT_ID&client_secret=TENANT_CLIENT_SECRET&token=MOCK_ACCESS_TOKEN
```


## 请求参数
| 参数          | 可选  | 描述                                                         |
| :------------ | :---- | :----------------------------------------------------------- |
| client_id     | false | 应用的 `client_id`。需要与获取授权和获取 Token 时使用的一致。 |
| client_secret | false | 应用的 `client_secret`。可通过租户管理平台的应用基本信息页面查看。 |
| token         | false | access_token 或 refresh_token 的值。                         |






## 正常响应示例
```
HTTP/1.1 200 OK
```

## 异常响应示例
client_id 与发起登录和获取 Token 时使用的不一致。
```
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_client"
}
```
