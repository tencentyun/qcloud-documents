### 接口描述
获取 MFA 要素，例如短信验证码、一次密码（OTP）等。

### 请求方法
POST
### 请求地址
```
/auth/mfa/challenge
```

### 请求参数
| 参数           | 参数位置 | 类型   | 是否必选 | 描述                                                         |
| -------------- | -------- | ------ | -------- | ------------------------------------------------------------ |
| client_id      | Query    | String | 是       | 客户端 ID                                                    |
| client_secret  | Query    | String | 否       | 客户端 Secret                                                |
| mfa_token      | Query    | String | 是       | mfa 令牌，密码模式的 token 接口返回mfa_required 错误时会同时返回mfa_token |
| challenge_type | Query    | String | 是       | MFA 认证类型，目前固定为 oob                                 |
| oob_channel    | Query    | String | 否       | MFA 认证方式，固定为 sms                                     |

### 返回参数
| 参数           | 参数位置 | 类型   | 是否必选 | 描述                    |
| -------------- | -------- | ------ | -------- | ----------------------- |
| challenge_type | Body     | String | 是       | 用户支持的 MFA 认证类型 |
| oob_code       | Body     | String | 是       | oob 授权码              |

### 接口示例
#### 输入示例
```
https://<auth_domain>/auth/mfa/challenge?client_id=ODQyNGJlYm****mNDZiYWE4YjkwNjU4MzMxOThkMGU&client_secret=oG412Uk6EdbfXtgU****WUdJht1j%2bq&mfa_token=7138d426f2fb5****e152a4710720b39&challenge_type=oob&oob_channel=sms
```
#### 返回示例
```
{
    "challenge_type": "oob",
    "oob_code": "6275684b3e****12ac40c3db148906ae"
}
```

### 错误码
| httpStatus | Response                                                     |
| ---------- | ------------------------------------------------------------ |
| 403        | {"error":  "unauthorized_client", "error_description": "invalid  client"} |




