### 1.注意事项
1.**前置条件**：确保 Access Token 已经正常获取，获取规则见[登录鉴权流程](https://cloud.tencent.com/document/product/295/10117)。
2.主要用于合作方**后台服务端业务请求**生成签名鉴权参数之一，用于后台查询验证结果、调用其他业务服务等。
3.api ticket 为 SIGN 类型，有效期为最长为 3600S, 此处 api ticket 的必须缓存在磁盘，并定时刷新,刷新的机制如下：
- 由于 api ticket 的生命周期依赖于 Access Token。最长为 3600S,故为了简单方便，建议 api ticket 的刷新机制与Access Token 定时机制原理一致，严格按照每50分钟请求新的api ticket,原api ticket 1 小时 (3600S) 失效，期间两个 api ticket 都能使用。
- 在获取新的 api ticket，请注意返回的 expire_in 为此 ticket 的最大生存周期，最大为 3600S,具体以实际返回为准，如果 expire_in 大于 600,那么下次刷新时间为 expire_in – 600S; 如果返回的 expire_in 小于等于 600，那么下次取 ticket时需要立刻刷新。

### 2.获取 SIGN ticket
请求 URL: https://idasc.webank.com/api/oauth2/api_ticket
请求方法:GET
请求参数：

| 参数 | 说明 |类型 |长度 | 是否必填 |
|---------|---------|---------|---------|---------|
| app_id | 腾讯服务分配的 app_id | 字符串 |腾讯服务分配 |必填 ，腾讯服务分配的 app_id |
| access_token | 根据[《整体登录鉴权流程》](https://cloud.tencent.com/document/product/295/10117?=cn)获取 access token | 字符串 |腾讯服务分配 |根据[《整体登录鉴权流程》](https://cloud.tencent.com/document/product/295/10117?=cn)获取 access token |
|type | ticket 类型 | 字符串 |20 |必填 ，默认值：**SIGN** (必须大写) |
| version | 版本号 | 字符串 |20 |必填 ，默认值：1.0.0|

请求示例：
https://idasc.webank.com/api/oauth2/api_ticket?app_id=xxx&access_token=xxx&type=SIGN&version=1.0.0
响应：
```
{
"code":"0",
"msg":"请求成功",
 "transactionTime":"20151022044027", 
 "tickets":[
{"value":"ticket_string",
"expire_in":"3600"，
"expire_time":"20151022044027"}
]
 ｝
 ```
 
>**注**:
1.code不是0是表示获取失败，可以根据code和msg字段定位和调试。
2.expire_in为access_token的最大生存时间，单位秒，合作伙伴在判定有效期时以此为准。
3.expire_time为access_token失效的绝对时间，由于各服务器时间差异，不能使用作为有效期的判定依据，只展示使用。
4.access_token失效时，该access_token生成的ticket都失效
