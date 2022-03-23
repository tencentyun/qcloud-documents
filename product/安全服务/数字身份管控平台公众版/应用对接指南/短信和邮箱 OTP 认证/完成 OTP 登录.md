## 接口描述
校验短信或邮箱 OTP 验证码，获取 Access Token 和 ID Token，完成登录。

## 支持的应用类型
Web 应用。

## 请求方法
```
POST
```

## 请求路径
```
/oauth2/token
```

## 请求 Content-Type
```
application/json
```

## 请求示例
```
POST /oauth2/token HTTP/1.1
Content-Type: application/json
Host: sample.portal.tencentciam.com

{
  "grant_type" : "https://sample.portal.tencentciam.com/oauth2/grant-type/otp/sms",
  "client_id" : "TENANT_CLIENT_ID",
  "client_secret" : "TENANT_CLIENT_SECRET",
  "auth_source_id" : "MOCK_SMS_OTP_AUTH_SOURCE_ID",
  "phone_number" : "13612345678",
  "otp" : "MOCK_OTP",
  "otp_token" : "MOCK_OTP_TOKEN"
}
```


## 请求体 JSON 参数

| JSON 路径      | 数据类型 | 描述                                                         |
| :------------- | :------- | :----------------------------------------------------------- |
| grant_type     | String   | <li>短信 OTP 登录填写： `http://tencentciam.com/oauth2/grant-type/otp/sms`</li><li>邮箱 OTP 登录填写：`http://tencentciam.com/oauth2/grant-type/otp/email` </li> |
| client_id      | String   | 应用的 client_id。需要与 [发送验证码](https://cloud.tencent.com/document/product/1441/67151) 时使用的一致 。 |
| client_secret  | String   | 应用的 client_secret。                                       |
| auth_source_id | String   | 短信 OTP 或邮箱 OTP 认证源 ID。需要与 [发送验证码](https://cloud.tencent.com/document/product/1441/67151) 时使用的一致。 |
| phone_number   | String   | 用户的手机号。需要与  [发送验证码](https://cloud.tencent.com/document/product/1441/67151) 时使用的一致。短信 OTP 登录时传递此参数。 |
| email          | String   | 用户的邮箱地址。需要与 [发送验证码](https://cloud.tencent.com/document/product/1441/67151) 时使用的一致。邮箱 OTP 登录时传递此参数。 |
| otp            | String   | 用户手机或邮箱收到的 OTP 验证码。                            |
| otp_token      | String   | 发送验证码成功后服务端返回的 otp_token。                     |





## 正常响应示例
```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "access_token" : "eyJraWQiOiI1MzQyOGU3ZS1kOTJiLTQ3OTAtOGIwMC0wMmEyZjc4NjUxNzMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJfSUQiLCJhdWQiOiJURU5BTlRfQ0xJRU5UX0lEIiwibmJmIjoxNjQwNTg4ODI3LCJzY29wZSI6WyJvcGVuaWQiXSwiaXNzIjoiaHR0cHM6XC9cL3NhbXBsZS5wb3J0YWwudGVuY2VudGNpYW0uY29tIiwiZXhwIjoxNjQwNTg5MTI3LCJpYXQiOjE2NDA1ODg4MjcsImp0aSI6IjRmMzhhMjc0LWY4YTQtNDdhNi04YmUyLTZlMDUxZDE5ZmQ3ZiJ9.nnTFLenQ0t_h-RfVCd4b6C-CtSgjKl-A0J_4nUyjs921Q7IlWe5uzIG7hEFAq8yqbvIDa3Ua3cepiZJQhBSrVY2mo0nDlXMUNvFqYp7jAaFyeOHf9V2-FKJ3lhm5n92pO_Jo2dI0kJXaGDidFsQkP_XMUhpeO6UgzZJHmoCDrF0sz3lmrHPXThWQZY89WlyTea3bOcZUZ2YKndCCiDC6y6gSjagV2Bnedc6htp2FQijRG_rS8PglOeEDtiYIQMuGsvRR1H4Lb320BB2SpZLbIdUt6ovM6TGYxCdORYhNfCtCP76cLipE5CwuCul_bmwhOGV5SAVpPwvkENXKFyJyDg",
  "refresh_token" : "DDAfEd98Hm9MUOs7BSeZNGKzf4Xl2X6W0keTh7FbmK8_X-Imc-JJvWqaZZCgOJKAHxEwEEhIVuiMEO8gVfGCSbILmGlGPh5KCGExVWTZShcjQ8cCfvUDMcuy5BEon4Rm",
  "scope" : "openid",
  "id_token" : "eyJraWQiOiI1MzQyOGU3ZS1kOTJiLTQ3OTAtOGIwMC0wMmEyZjc4NjUxNzMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJfSUQiLCJhdWQiOiJURU5BTlRfQ0xJRU5UX0lEIiwiYXpwIjoiVEVOQU5UX0NMSUVOVF9JRCIsImlzcyI6Imh0dHBzOlwvXC9zYW1wbGUucG9ydGFsLnRlbmNlbnRjaWFtLmNvbSIsImV4cCI6MTY0MDU5MDYyNywiaWF0IjoxNjQwNTg4ODI3LCJqdGkiOiIwMDhhNzBiNC1hOTc4LTRlZDEtYmZkNC1mMDM1Nzc5NTEzMjYifQ.OObTWSeYTnEMKuwKlDjYtnrS6CBoTzbmlpDV1IdLh_C-pdlaMxHWLMuGoYEJhSGtLlWc6zwX7IAsf56o2YSJY5YBXDThWAb9IidrV8YrRRR-SGjI7ZZh-w2Q_tvqVXzT_n7fXeuZ40vJUirpR7nGy1XApLHbxYII9RXmTTn7B6R1IrSXIoadAc_Vp7zMVZVRh-LLIGSVLgGNC5PMYjYfmwA0RmH1p0fhvc2DHc-KnjGnM4YvtptrQ1EZwEOaemelQIQFR-ISHNaqPWpej_Iw0huI9owyntiI0APEaogVTqA6xd_2pBwLXZOgGy9IATnQwYJF1Ogo1eLHm6TtaZHsww",
  "token_type" : "Bearer",
  "expires_in" : 299
}
```


## 异常响应示例
- OTP 错误或已过期。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_grant",
  "error_description" : "Unknown or expired OTP"
}
```

- otp_token 错误已过期。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_grant",
  "error_description" : "Unknown or expired otp_token"
}
```

- 使用的参数与发送验证码时不一致（例如：手机号不同）。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_request",
  "error_description" : "Mismatched OTP token and OTP sending parameters"
}
```
