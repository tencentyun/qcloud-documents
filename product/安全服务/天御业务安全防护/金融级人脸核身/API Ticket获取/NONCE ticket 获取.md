### 1.注意事项
1.**前置条件**：确保Access Token已经正常获取，获取规则见章节4。
2.主要用于合作方**前端包含APP和H5等**生成签名鉴权参数之一，启动H5或SDK人脸验证。
3.api ticket为NONCE类型，有效期为120S,且一次性有效, 即每次启动SDK刷脸都要重新请求NONCE ticket。

### 2.获取NONCE ticket
ticket用于对请求数据签名或加密。
请求URL: https://idasc.webank.com/api/oauth2/api_ticket
请求方法:GET
请求参数：

| 参数 | 说明 |类型 |长度 | 是否必输 |
|---------|---------|---------|---------|---------|
| app_id | 腾讯服务分配的app_id | 字符串 |腾讯服务分配 |必输，腾讯服务分配的app_id |
| access_token | 根据[《整体登录鉴权流程》](https://www.qcloud.com/document/product/295/10117?!preview&lang=cn)获取access token | 字符串 |腾讯服务分配 |根据[《整体登录鉴权流程》](https://www.qcloud.com/document/product/295/10117?!preview&lang=cn)获取access token |
|type | ticket类型 | 字符串 |20 |必输，默认值：**NONCE(必须大写)** |
| version | 版本号 | 字符串 |20 |必输，默认值：1.0.0|
| user_id | 当前使用用户的唯一标识。<br>**注意合作伙伴必须保证user_id的全局唯一。** | 字符串 |20 |必输|

请求示例：
https://idasc.webank.com/api/oauth2/api_ticket?app_id=xxx&access_token=xxx&type=NONCE&version=1.0.0&user_id=xxx

```
响应：
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
 
**注**：
1.code不是0是表示获取失败，可以根据code和msg字段定位和调试。
2.expire_in为access_token的最大生存时间，单位秒，合作伙伴在判定有效期时以此为准。
3.expire_time为access_token失效的绝对时间，由于各服务器时间差异，不能使用作为有效期的判定依据，只展示使用。
4.access_token失效时，该access_token生成的ticket都失效