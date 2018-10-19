## 注意事项
- 所有场景默认采用 UTF-8 编码。
- Access Token 必须缓存在磁盘，并定时刷新，建议每 20 分钟请求新的 Access Token，原 Access Token 2 小时（7200S） 失效，获取之后立即使用最新的 Access Token。旧的只有一分钟的并存期 。
- 每次用户登录时必须重新获取 ticket。

## 请求
**请求 URL：**

```
https://idasc.webank.com/api/oauth2/access_token 
```
**请求方法：GET**
**请求参数：**

| 参数         | 说明                                 | 类型   | 长度（字节）    | 是否必填 |
| ---------- | ---------------------------------- | ---- | --------- | ---- |
| app_id     | 腾讯云线下对接分配的 App ID                  | 字符串  | 腾讯云线下对接决定 | 是    |
| secret     | 腾讯云线下对接分配的 App ID 的密钥              | 字符串  | 腾讯云线下对接决定 | 是    |
| grant_type | 授权类型，默认值为：client_credential (必须小写) | 字符串  | 20        | 是    |
| version    | 版本号，默认值为：1.0.0                     | 字符串  | 20        | 是    |

**请求示例：**
```
https://idasc.webank.com/api/oauth2/access_token?app_id=xxx&secret=xxx&grant_type=client_credential&version=1.0.0
```

## 响应

**响应示例：**

```
{
"code":"0","msg":"请求成功",
"transactionTime":"20151022043831",
"access_token":"accessToken_string",
"expire_time":"20151022043831",
"expire_in":"7200"
}
```

> **注意：**
> - code 不为 0 则表示获取失败，可以根据 code 和 msg 字段进行定位和调试。
> - expire_in 为 access_token 的最大生存时间，单位秒，合作伙伴在 **判定有效期时以此为准**。
> - expire_time 为 access_token 失效的绝对时间，由于各服务器时间差异，不能使用作为有效期的判定依据，只展示使用。
> - 修改 secret 之后，该 app_id 生成的 access_token 和 ticket 都失效。
