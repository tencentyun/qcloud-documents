## 注意事项
- 所有场景默认采用 UTF-8 编码。
- Access Token 必须缓存在磁盘并定时刷新，建议每20分钟请求新的 Access Token，原 Access Token 2小时（7200秒）失效，获取之后立即请使用最新的 Access Token。旧的 Access Token 只有一分钟的并存期 。
- 每次用户登录时必须重新获取 ticket。

## 请求
- **请求 URL：**`https://idasc.webank.com/api/oauth2/access_token`
- **请求方法**：`GET`
- **请求参数：**
<table><tbody>
<tr><th>参数</th><th>说明</th><th>类型</th><th>长度（字节）</th><th>是否必填</th></tr>
<tr>
<td>app_id</td>
<td>请添加小助手微信 faceid001，进行线下对接获取</td>
<td>String</td>
<td>腾讯云线下对接决定</td>
<td>是</td>
</tr>
<tr>
<td>secret</td>
<td>请添加小助手微信 faceid001，进行线下对接获取</td>
<td>String</td>
<td>腾讯云线下对接决定</td>
<td>是</td>
</tr>
<tr>
<td>grant_type</td>
<td>授权类型，默认值为：client_credential（必须小写）</td>
<td>String</td>
<td>20</td>
<td>是</td>
</tr>
<tr>
<td>version</td>
<td>版本号，默认值为：1.0.0</td>
<td>String</td>
<td>20</td>
<td>是</td>
</tr>
</tbody></table>
- **请求示例：**
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
>!
>- code 不为0则表示获取失败，可以根据 code 和 msg 字段进行定位和调试。code 详情请参见 [错误码](https://cloud.tencent.com/document/product/1007/31082)。
>- expire_in 为 access_token 的最大生存时间，单位：秒，合作伙伴在**判定有效期时以此为准**。
>- expire_time 为 access_token 失效的绝对时间，由于各服务器时间差异，不能以此作为有效期的判定依据，只作为展示使用。
>- 修改 secret 之后，该 app_id 生成的 access_token 和 ticket 都失效。
