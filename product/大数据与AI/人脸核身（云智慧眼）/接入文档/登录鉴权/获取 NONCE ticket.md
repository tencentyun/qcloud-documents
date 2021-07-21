## 注意事项
- **前置条件：**请合作方确保 Access Token 已经正常获取，获取方式请参见 [Access Token 获取](https://cloud.tencent.com/document/product/1007/37304)。
- **用途：**NONCE ticket 是合作方**前端包含 App 和 H5 等**生成签名鉴权参数之一，启动 H5 或 SDK 人脸核身。
- API ticket 的 NONCE 类型，其有效期为120秒，且一次性有效，即每次启动 SDK 刷脸都要重新请求 NONCE ticket。

## 请求
- **请求 URL：**`https://miniprogram-kyc.tencentcloudapi.com/api/oauth2/api_ticket`
- **请求方法**：GET
- **请求参数：**
<table><tbody>
<tr><th >参数</th><th >说明</th><th >类型</th><th >长度（字节）</th><th >是否必填</th></tr>
<tr><td >app_id</td><td>业务流程唯一标识，即 wbappid，可参考<a href="https://cloud.tencent.com/document/product/1007/49634"> 获取 WBappid</a>  指引在人脸核身控制台内申请</td><td >String</td><td >8</td><td >是</td></tr>
<tr><td >access_token</td><td >请根据 <a href='https://cloud.tencent.com/document/product/1007/37304'>Access Token 获取</a> 指引进行获取</td><td >String</td><td>64</td><td >是</td></tr>
<tr><td >type</td><td >ticket 类型，默认值：NONCE（必须大写）</td><td >String</td><td >20</td><td >是</td></tr>
<tr><td >version</td><td >版本号</td><td >String</td><td >20</td><td >是</td></tr>
<tr><td>user_id</td><td >当前使用用户的唯一标识，需合作伙伴自行定义<br/>注意：合作伙伴必须保证 user_id 的全局唯一性，不要带有特殊字符</td><td>String</td><td>30</td><td>是</td></tr>
</tbody></table>
- **请求示例：**
```
https://miniprogram-kyc.tencentcloudapi.com/api/oauth2/api_ticket?app_id=xxx&access_token=xxx&type=NONCE&version=1.0.0&user_id=xxx
```

## 响应

**响应参数：**

| 参数            | 类型   | 说明                                                         |
| --------------- | ------ | ------------------------------------------------------------ |
| code            | String | 0：成功 <br>非0：失败 <br>详情请参见 [SaaS 服务错误码](https://cloud.tencent.com/document/product/1007/47912) |
| msg             | String | 请求结果描述                                                 |
| transactionTime | String | 调用接口的时间                                               |
| tickets         | list   | ticket 返回数组                                               |
| value           | String | ticket 的值                                                   |
| expire_time     | String | ticket 失效的绝对时间                                         |
| expire_in       | int    | ticket 的最大生存时间                                         |

**响应示例：**
```
{
	  "code": "0",
	  "msg": "请求成功",
	  "transactionTime": "20151022044027",
	  "tickets": [
		{
			  "value": "ticket_string",
			  "expire_in": "120",
			  "expire_time": "20151022044027"
		}
	]
}
```
>!
>- code 不为0则表示获取失败，可以根据 code 和 msg 字段进行定位和调试。code 详情请参见 [SaaS 服务错误码](https://cloud.tencent.com/document/product/1007/47912)。
>- expire_in 为 access_token 的最大生存时间，单位：秒，合作伙伴在**判定有效期时以此为准**。
>- expire_time 为 access_token 失效的绝对时间，由于各服务器时间差异，不能以此作为有效期的判定依据，只作为展示使用。
>- access_token 失效时，该 access_token 生成的 ticket 都失效。
