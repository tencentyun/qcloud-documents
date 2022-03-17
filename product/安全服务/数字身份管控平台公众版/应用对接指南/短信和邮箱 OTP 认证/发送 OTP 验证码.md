## 接口描述
向用户发送短信或邮箱 OTP 验证码。

## 支持的应用类型
Web 应用。

## 请求方法
```
POST
```

## 请求路径
```
/otp/send
```

## 请求 Content-Type
```
application/json
```

## 请求示例
```
POST /otp/send HTTP/1.1
Content-Type: application/json
Host: sample.portal.tencentciam.com

{
  "client_id" : "TENANT_CLIENT_ID",
  "client_secret" : "TENANT_CLIENT_SECRET",
  "auth_source_id" : "MOCK_SMS_OTP_AUTH_SOURCE_ID",
  "phone_number" : "13612345678"
}
```


## 请求体 JSON 参数

| JSON 路径      | 数据类型 | 描述                                                         |
| :------------- | :------- | :----------------------------------------------------------- |
| client_id      | String   | 应用的 `client_id`。可参考 **[应用管理页面](https://console.cloud.tencent.com/ciam/app-management)** > **选定指定应用** > 单击**应用配置** > 对应的“Client Id”。 |
| client_secret  | String   | 应用的 `client_secret`。可参考 **[应用管理页面](https://console.cloud.tencent.com/ciam/app-management)** > **选定指定应用** > 单击**应用配置** > 对应的“client_secret”。 |
| auth_source_id | String   | 短信 OTP 或邮箱 OTP 认证源 ID。可在控制台的 [通用认证源页面](https://console.cloud.tencent.com/ciam/general-auth-source) 查看。 |
| phone_number   | String   | 用户的手机号，限国内三大运营商11位手机号。发送短信 OTP 验证码时传递此参数。 |
| email          | String   | 用户的邮箱地址。发送短信 OTP 验证码时传递此参数。            |




## 正常响应示例
#### 验证码发送成功
```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "otp_token" : "MOCK_OTP_TOKEN"
}
```

#### 响应参数
| 参数      | 数据类型 | 描述                                                        |
| :-------- | :------- | :---------------------------------------------------------- |
| otp_token | String   | OTP token，用于在后续调用 [OTP 登录](https://cloud.tencent.com/document/product/1441/67153) 接口时携带，有效期5分钟。 |
