## 注意事项
- **前置条件：请合作方确保 Access Token 已经正常获取，获取方式见 [Access Token 获取](https://cloud.tencent.com/document/product/655/13813)。**
- SIGN ticket 是合作方 **后台服务端业务请求** 生成签名鉴权参数之一，用于后台查询验证结果、调用其他业务服务等。
- API ticket 的 SIGN 类型，其有效期最长为 3600S，此处 API ticket 必须缓存在磁盘，并定时刷新，刷新的机制如下：
 - 由于 API ticket 的生命周期依赖于 Access Token。最长为 3600S，故为了简单方便，建议 API ticket 的刷新机制与 Access Token 定时机制原理一致，建议按照每 20 分钟和 Access Token 绑定定时刷新，原 API ticket 1 小时（3600S）失效。获取新的之后立即使用最新的，旧的有一分钟的并存期。

## 请求
**请求 URL：** 
```
https://idasc.webank.com/api/oauth2/api_ticket
```
**请求方法：GET**
**请求参数：**

| 参数           | 说明                                       | 类型   | 长度（字节）    | 是否必填 |
| ------------ | ---------------------------------------- | ---- | --------- | ---- |
| app_id       | 腾讯云线下对接分配的 App ID                        | 字符串  | 腾讯云线下对接决定 | 是    |
| access_token | 根据 [Access Token 获取](https://cloud.tencent.com/document/product/655/13813) 页面中的指引进行获取 | 字符串  | 腾讯云线下对接决定 | 是    |
| type         | ticket 类型，默认值：**SIGN** (必须大写)            | 字符串  | 20        | 是    |
| version      | 版本号，默认值：1.0.0                            | 字符串  | 20        | 是    |

**请求示例：**
```
https://idasc.webank.com/api/oauth2/api_ticket?app_id=xxx&access_token=xxx&type=SIGN&version=1.0.0
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
"expire_in":"3600"，
"expire_time":"20151022044027"}
]
 ｝
```

>**注意**:
> - code 不为 0 则表示获取失败，可以根据 code 和 msg 字段进行定位和调试。
> - expire_in 为 SIGN ticket 的最大生存时间，单位秒，合作伙伴在 **判定有效期时以此为准**。
> - expire_time 为 SIGN ticket 失效的绝对时间，由于各服务器时间差异，不能使用作为有效期的判定依据，只展示使用。
> - access_token 失效时，该 access_token 生成的 ticket 都失效。
> - tickets 只有一个。
