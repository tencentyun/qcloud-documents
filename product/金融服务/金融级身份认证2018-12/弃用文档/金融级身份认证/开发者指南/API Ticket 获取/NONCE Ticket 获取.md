## 注意事项
- **前置条件：确保 Access Token 已经正常获取，获取方式见 [Access Token 获取](https://cloud.tencent.com/document/product/655/13813)**。
- NONCE ticket 是合作方 **前端包含 App 和 H5 等** 生成签名鉴权参数之一，启动 H5 或 SDK 人脸验证。
- API ticket 的 NONCE 类型，其有效期为 120s，且一次性有效, 即每次启动 SDK 刷脸都要重新请求 NONCE ticket。

## 请求
**请求 URL：**
```
 https://idasc.webank.com/api/oauth2/api_ticket
```
**请求方法**：GET
**请求参数**：

| 参数           | 说明                                       | 类型   | 长度（字节）    | 是否必填 |
| ------------ | ---------------------------------------- | ---- | --------- | ---- |
| app_id       | 腾讯云线下对接分配的 AppID                        | 字符串  | 腾讯云线下对接决定 | 是    |
| access_token | 根据 [Access Token 获取](https://cloud.tencent.com/document/product/655/13813) 页面中的指引进行获取 | 字符串  | 腾讯云线下对接决定 | 是    |
| type         | ticket 类型，默认值：**NONCE (必须大写)**           | 字符串  | 20        | 是    |
| version      | 版本号                                      | 字符串  | 20        | 是    |
| user_id      | 当前使用用户的唯一标识<br>**注意：合作伙伴必须保证 user_id 的全局唯一** | 字符串  | 30        | 是    |

**请求示例**：

```
https://idasc.webank.com/api/oauth2/api_ticket?app_id=xxx&access_token=xxx&type=NONCE&version=1.0.0&user_id=xxx
```

## 响应
**响应示例：**
```
{
"code":"0",
"msg":"请求成功",
 "transactionTime":"20151022044027", 
 "tickets":[
{"value":"ticket_string",
"expire_in":"120"，
"expire_time":"20151022044027"}
]
 ｝
```

>**注意**：
> - code 不为 0 则表示获取失败，可以根据 code 和 msg 字段定位和调试。
> - expire_in 为 access_token 的最大生存时间，单位秒，合作伙伴在 **判定有效期时以此为准**。
> - expire_time 为 access_token 失效的绝对时间，由于各服务器时间差异，不能使用作为有效期的判定依据，只展示使用。
> - access_token 失效时，该 access_token 生成的 ticket 都失效
