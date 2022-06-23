## 接口描述
校验短信或邮箱 OTP 验证码，获取 Access Token 和 ID Token，完成登录。调用此接口前，需要先通过 [发送 OTP 验证码](https://cloud.tencent.com/document/product/1441/71640) 接口向用户发送验证码。

>?可以通过传递 `auto_signup=true` 参数来支持自动注册用户。

## 支持的应用类型
Web 应用、单页应用、移动 App。

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
#### 短信 OTP 登录
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
  "otp_token" : "MOCK_OTP_TOKEN",
  "otp" : "123456"
}
```
#### 邮箱 OTP 登录
```
POST /oauth2/token HTTP/1.1
Content-Type: application/json
Host: sample.portal.tencentciam.com

{
  "grant_type" : "https://sample.portal.tencentciam.com/oauth2/grant-type/otp/email",
  "client_id" : "TENANT_CLIENT_ID",
  "client_secret" : "TENANT_CLIENT_SECRET",
  "auth_source_id" : "MOCK_EMAIL_OTP_AUTH_SOURCE_ID",
  "email" : "MOCK_USERNAME@example.com",
  "otp_token" : "MOCK_EMAIL_OTP_TOKEN",
  "otp" : "123456"
}
```

## 请求体 JSON 参数
| JSON 路径      | 数据类型 | 描述                                                         |
| :------------- | :------- | :----------------------------------------------------------- |
| grant_type     | String   | <li>短信 OTP 登录输入： `http://tencentciam.com/oauth2/grant-type/otp/sms`</li><li>邮箱 OTP 登录输入：`http://tencentciam.com/oauth2/grant-type/otp/email` </li>|
| client_id      | String   | 应用的 `client_id`。需要与发送验证码时使用的一致。           |
| client_secret  | String   | 应用的 `client_secret`。Web 应用须传递此参数。单页应用和移动 App 不传递此参数。 |
| auth_source_id | String   | 短信 OTP 或邮箱 OTP 认证源 ID。需要与发送验证码时使用的一致。 |
| phone_number   | String   | 用户的手机号。需要与发送验证码时使用的一致。短信 OTP 登录时传递此参数。 |
| email          | String   | 用户的邮箱地址。需要与发送验证码时使用的一致。邮箱 OTP 登录时传递此参数。 |
| otp_token      | String   | 发送验证码成功后服务端返回的 `otp_token`。                   |
| otp            | String   | 用户手机或邮箱收到的 OTP 验证码。                            |
| auto_signup    | Boolean  | 如需支持自动注册用户，则此参数传 true，否则可以不传。        |

## 正常响应示例
```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "access_token" : "eyJraWQiOiJmZTQ4YTJjYS1lNGU3LTQyMGEtOThjOS01OGM5NmI2NzUwZjIiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJfSUQiLCJhdWQiOiJURU5BTlRfQ0xJRU5UX0lEIiwibmJmIjoxNjQ3NDIwMDM1LCJzY29wZSI6WyJvcGVuaWQiXSwiaXNzIjoiaHR0cHM6XC9cL3NhbXBsZS5wb3J0YWwudGVuY2VudGNpYW0uY29tIiwiZXhwIjoxNjQ3NDIwMzM1LCJpYXQiOjE2NDc0MjAwMzUsImp0aSI6ImMxZmE5Yzk4LThhZjQtNDA1Zi1iOWFhLTdiNTU2MjY1NDljNSJ9.FzvKdLeIgNeYKwQeixIGKX2JPkZ9tJ43fnwuaruLY85RQj9cMedm9eSU4Ft_h7NJkwH-eBTmSybg7174RsQ98yOaW77u2flQwxm0xZCx74kY2dOZOf3YhRJwVLVhocMtLC1NrrP3phJSVfYYzClS_ppTnSHcGZhiVzW57YgolTr0EeuOMucmt1jh_I76kDreo_B5UhV95sRqP_R5FMVBLpGvlAD3TPVCMs3zQETlgHHyq2UE9YBnkNBLK9RzxknRZ0XSnUMxpcPCod4e7Q7S87QqML2S_3AbcmJlPY5q0D-XTqzyjvS2QByUOUQNOX6pEH4Pe7fV6phVrfXh0IenDQ",
  "refresh_token" : "B-72VlkQa3jQNuo9Xbbl-muoh4w7nYu-7Q3Wb-qmPgyftN1CgXPov2aWsOBWeeIOIVHjVxxHxbOa21Oz0CtIgsIz1LMZ_HG7eLxF-qk6hiRcFzPOcSl8PBsCdd3QXaEd",
  "scope" : "openid",
  "id_token" : "eyJraWQiOiJmZTQ4YTJjYS1lNGU3LTQyMGEtOThjOS01OGM5NmI2NzUwZjIiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJfSUQiLCJhdWQiOiJURU5BTlRfQ0xJRU5UX0lEIiwiYXpwIjoiVEVOQU5UX0NMSUVOVF9JRCIsImlzcyI6Imh0dHBzOlwvXC9zYW1wbGUucG9ydGFsLnRlbmNlbnRjaWFtLmNvbSIsImV4cCI6MTY0NzQyMTgzNSwiaWF0IjoxNjQ3NDIwMDM1LCJqdGkiOiI5MGFiMzljMi00NjQzLTQwYTEtODdmOC0yN2Q5ODkzOTExMDQifQ.ZqgRcJae_XEUd1XIbu2_pzdgnJCtEehLoCTTHJhEvewOeEnUlfYkRMrpfZ_hYSVsaWDZy0zdqntWmpmN57eJuw-nfwaUGBUjc1e3KgyvY9jr5vo4zlI5O2NJYYMwP8uwwCFsqWjbNl1cl-dVPu6pIGAvPWBx_Hm1C0vMsPICv61KE7I4bGi_XCSQ--CQjvjzE8ly4I7Z1jCfVl9f4Aybve2HJkuD-m73nZsgluAGOANXvBLcYi1bj4ncXt9Ybk45Gt_vtlCOY9Ab-N6STm4omtKuxyMQUfy7Rv-9RXBuvDFIdDl6tpENxch1N0V027FdtdWk_JOk9mq97rqI-LycPA",
  "token_type" : "Bearer",
  "expires_in" : 299
}
```

## 响应参数
| 字段          | 数据类型 | 描述                                      |
| :------------ | :------- | :---------------------------------------- |
| access_token  | String   | OAuth 2.0 Access Token (JWT)。            |
| token_type    | String   | Token 类型，目前返回的是固定值 'Bearer'。 |
| expires_in    | Number   | Access Token 有效期，单位秒。             |
| scope         | String   | Access Token scope。                      |
| refresh_token | String   | OAuth 2.0 Refresh Token。                 |
| id_token      | String   | OIDC ID Token (JWT)。                     |

## 异常响应示例
- otp_token 错误或已过期。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_grant",
  "error_description" : "Unknown or expired otp_token"
}
```
- otp 错误或已过期。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_grant",
  "error_description" : "Unknown or expired OTP"
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
- 找不到手机号或邮箱对应的用户（不允许自动注册用户的情况下）。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_grant",
  "error_description" : "User not found"
}
```
- 手机号或邮箱对应的用户状态异常（如被锁定或冻结）。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_grant",
  "error_description" : "Abnormal user status"
}
```
- 认证源不是应用的首选认证源或关联认证源。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_auth_source",
  "error_description" : "Auth source and application not associated"
}
```
