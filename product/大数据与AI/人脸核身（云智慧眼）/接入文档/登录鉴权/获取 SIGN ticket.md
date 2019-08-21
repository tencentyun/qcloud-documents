## 注意事项
- **前置条件：**请合作方确保 Access Token 已经正常获取，获取方式请参见 [Access Token 获取](https://cloud.tencent.com/document/product/655/31946)。
- SIGN ticket 是合作方**后台服务端业务请求**生成签名鉴权参数之一，用于后台查询验证结果、调用其他业务服务等。
- API ticket 的 SIGN 类型，其有效期最长为3600秒，此处 API ticket 必须缓存在磁盘，并定时刷新，刷新的机制如下：
 - 因为 API ticket 依赖于 Access Token，所以生命周期最长为 3600秒。为了简单方便，建议将 API ticket 与 Access Token 绑定，每20分钟定时刷新，原 API ticket 1 小时（3600秒）失效。
 - 获取新的之后请立即使用最新的，旧的有一分钟的并存期。

## 请求
- **请求 URL：**`https://idasc.webank.com/api/oauth2/api_ticket`
- **请求方法**：GET
- **请求参数：**
<table><tbody>
<tr><th >参数</th><th >说明</th><th >类型</th><th >长度（字节）</th><th >是否必填</th></tr>
<tr><td >app_id</td><td >请参考 <a href="https://cloud.tencent.com/document/product/655/31892">接入前须知</a>，按照指引进入链接在线申请</td><td >String</td><td >腾讯云线下对接决定</td><td >是</td></tr>
<tr><td>access_token</td><td >请根据 <a href='https://cloud.tencent.com/document/product/655/31946'>Access Token 获取</a> 指引进行获取</td><td>String</td><td >腾讯云线下对接决定</td><td>是</td></tr>
<tr><td >type</td><td >ticket 类型，默认值：SIGN（必须大写）</td><td >String</td><td >20</td><td >是</td></tr>
<tr><td >version</td><td >版本号，默认值：1.0.0</td><td >String</td><td >20</td><td >是</td></tr>
</tbody></table>
- **请求示例：**
```
https://idasc.webank.com/api/oauth2/api_ticket?app_id=xxx&access_token=xxx&type=SIGN&version=1.0.0
```

## 响应
**响应示例：**
```
{
	"code": "0",
	"msg": "请求成功",
	"transactionTime": "20151022044027",
	"tickets": [{
		"value": "ticket_string",
		"expire_in": "3600",
		"expire_time": "20151022044027"
	}]
}
```
>!
>- code 不为0则表示获取失败，可以根据 code 和 msg 字段进行定位和调试。code 详情请参见 [错误码](https://cloud.tencent.com/document/product/1007/31082)。
>- expire_in 为 SIGN ticket 的最大生存时间，单位：秒，合作伙伴在**判定有效期时以此为准**。
>- expire_time 为 SIGN ticket 失效的绝对时间，由于各服务器时间差异，不能以此作为有效期的判定依据，只作为展示使用。
>- access_token 失效时，该 access_token 生成的 ticket 都失效。
>- tickets只有一个。
