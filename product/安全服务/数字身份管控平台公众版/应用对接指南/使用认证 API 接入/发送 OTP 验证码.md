## 接口描述
向用户发送短信或邮箱 OTP 验证码，用于登录、注册或更新用户信息。



## 支持的应用类型
Web 应用、M2M 应用。

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
- 短信 OTP 登录场景，发送短信验证码用于登录。
```
POST /otp/send HTTP/1.1
Content-Type: application/json
Authorization: Basic VEVOQU5UX0NMSUVOVF9JRDpURU5BTlRfQ0xJRU5UX1NFQ1JFVA==
Host: sample.portal.tencentciam.com

{
  "usage" : "login",
  "phone_number" : "13612345678",
  "auth_source_id" : "MOCK_SMS_OTP_AUTH_SOURCE_ID"
}

```
- 邮箱 OTP 登录场景，发送邮箱验证码用于登录。
```
POST /otp/send HTTP/1.1
Content-Type: application/json
Authorization: Basic Q0xJRU5UXzRfSUQ6Q0xJRU5UXzRfU0VDUkVU
Host: sample.portal.tencentciam.com

{
  "usage" : "login",
  "email" : "MOCK_USERNAME@example.com",
  "auth_source_id" : "MOCK_EMAIL_OTP_AUTH_SOURCE_ID"
}
```
- 用户注册场景，发送短信验证码用于绑定手机。
```
POST /otp/send HTTP/1.1
Content-Type: application/json
Authorization: Basic Q0xJRU5UXzRfSUQ6Q0xJRU5UXzRfU0VDUkVU
Host: sample.portal.tencentciam.com

{
  "usage" : "signup",
  "phone_number" : "13612345678"
}
```
- 用户注册场景，发送邮箱验证码用于绑定邮箱。
```
POST /otp/send HTTP/1.1
Content-Type: application/json
Authorization: Basic Q0xJRU5UXzRfSUQ6Q0xJRU5UXzRfU0VDUkVU
Host: sample.portal.tencentciam.com

{
  "usage" : "signup",
  "email" : "MOCK_USERNAME@example.com"
}
```
- 更新用户信息场景，发送短信验证码绑定或更新手机号。
```
POST /otp/send HTTP/1.1
Content-Type: application/json
Authorization: Basic Q0xJRU5UXzRfSUQ6Q0xJRU5UXzRfU0VDUkVU
Host: sample.portal.tencentciam.com

{
  "usage" : "update_userinfo",
  "phone_number" : "13612345678"
}
```

## 请求头
| 名称          | 描述                                                         |
| :------------ | :----------------------------------------------------------- |
| Authorization | HTTP Basic 认证请求头，格式为 `Basic <credentials>`，其中 `Basic` 为固定字符串，`<credentials>` 的计算方式为 `base64(url_encode(client_id) + ":" + url_encode(client_secret))`，`Basic` 和 `<credentials>` 之间用一个空格隔开。 |

## 请求体 JSON 参数
| JSON 路径      | 数据类型 | 描述                                                         |
| :------------- | :------- | :----------------------------------------------------------- |
| usage          | String   | OTP 验证码的使用场景。<li>短信和邮箱 OTP 登录场景输入 `login`</li><li>用户注册场景输入 `signup`</li><li>更新用户信息场景输入 `update_userinfo`</li>如果不填，默认代表登录场景。 |
| phone_number   | String   | 用户的手机号，限国内三大运营商11位手机号。发送短信 OTP 验证码时传递此参数。 |
| email          | String   | 用户的邮箱地址。发送邮箱 OTP 验证码时传递此参数。            |
| auth_source_id | String   | 短信 OTP 或邮箱 OTP 认证源 ID。可在控制台的通用认证源列表页面查看。短信和邮箱 OTP 登录场景传递此参数，系统将使用认证源配置的验证码长度和有效期。其他场景不传递此参数，系统默认使用6位数字验证码，有效期60秒。 |

## 正常响应示例
验证码发送成功
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "otp_token" : "MOCK_OTP_TOKEN"
}
```

## 响应参数
| 字段      | 数据类型 | 描述                                              |
| :-------- | :------- | :------------------------------------------------ |
| otp_token | String   | OTP token，后续验证 OTP 时携带使用。有效期5分钟。 |

## 异常响应示例
- 手机号格式有误。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "malformed_phone_number"
}
```
- 邮箱格式有误。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "malformed_email"
}
```
- 因短信额度不足无法发送短信，一般是由于免费短信额度已用尽，需要到控制台配置 [短信模板](https://cloud.tencent.com/document/product/1441/65102)。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "insufficient_sms_quota"
}
```
- 因邮箱额度不足无法发送邮件，一般是由于免费邮箱额度已用尽，需要到控制台配置 [邮箱模板](https://cloud.tencent.com/document/product/1441/67392)。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "insufficient_email_quota"
}
```
- 验证码发送失败。
```
HTTP/1.1 503 Service Unavailable
Content-Type: application/json;charset=UTF-8

{
  "error" : "temporarily_unavailable",
  "error_description" : "Failed to send OTP. Please try again later."
}
```
