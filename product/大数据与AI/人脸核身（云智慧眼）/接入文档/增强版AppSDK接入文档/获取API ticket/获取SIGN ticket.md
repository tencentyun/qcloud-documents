## 注意事项
- **前置条件：**请合作方确保 Access Token 已经正常获取，获取方式见 [Access Token 获取](https://cloud.tencent.com/document/product/1007/57603)。
- **用途：**SIGN ticket 是合作方**后台服务端业务请求**生成签名鉴权参数之一，用于后台查询验证结果、调用其他业务服务等。
- API ticket 的 SIGN 类型，必须缓存在磁盘，并定时刷新，刷新的机制如下：
 - **由于 API ticket 的生命周期依赖于 Access Token 为了简单方便，建议 API ticket 的刷新机制与 Access Token 定时机制原理一致，建议按照每20分钟和 Access Token 绑定定时刷新，且不能并发刷新。**
 - **获取新的之后立即使用最新的，旧的有一分钟的并存期。**
 - **如果未按照上述做定时刷新，可能导致鉴权不通过，影响人脸服务正常调用。**

## 请求
- 请求 URL：`https://miniprogram-kyc.tencentcloudapi.com/api/oauth2/api_ticket`
- 请求方法：`GET`
- 请求参数：
<table><tbody>
<tr><th >参数</th><th >说明</th><th >类型</th><th><nobr>长度（字节）</nobr></th><th >是否必填</th></tr>
<tr><td >app_id</td><td >业务流程唯一标识，即 wbappid，可参考<a href="https://cloud.tencent.com/document/product/1007/49634"> 获取 WBappid</a>  指引在人脸核身控制台内申请</td><td >String</td><td >8</td><td >是</td></tr>
<tr><td>access_token</td><td >请根据 <a href='https://cloud.tencent.com/document/product/1007/57603'>获取 Access Token</a> 指引进行获取</td><td>String</td><td>64</td><td>是</td></tr>
<tr><td >type</td><td >ticket 类型，默认值：SIGN（必须大写）</td><td >String</td><td >20</td><td >是</td></tr>
<tr><td >version</td><td>版本号，默认值：1.0.0</td><td >String</td><td >20</td><td >是</td></tr>
</tbody></table>

- **请求示例：**
```
https://miniprogram-kyc.tencentcloudapi.com/api/oauth2/api_ticket?app_id=xxx&access_token=xxx&type=SIGN&version=1.0.0
```

## 响应
**响应示例：**

```
{
  "code":"0",
  "msg":" 请求成功 ", 
  "transactionTime":"20151022044027", 
  "tickets":[
{
  "value":"ticket_string", 
  "expire_in":"3600"， 
  "expire_time":"20151022044027"}
]
｝
```

>!
1. code 不为 0 则表示获取失败，可以根据 code 和 msg 字段进行定位和调试。code 详情请参见 [SaaS 服务错误码](https://cloud.tencent.com/document/product/1007/47912)。
2. expire_in 为 SIGN ticket 的最大生存时间，单位秒，合作伙伴在 判定有效期时以此为准。
3. expire_time 为 SIGN ticket 失效的绝对时间，由于各服务器时间差异，不能使用作为有效期的判定依据，只展示使用。
4. access_token 失效时，该 access_token 生成的 ticket 都失效。
5. tickets 只有一个。
