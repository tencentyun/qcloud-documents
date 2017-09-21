### 1.注意事项
1.所有场景默认采用UTF-8编码。
2.access token必须缓存在磁盘，并定时刷新,建议每1小时50分钟请新的access token,原access token 2小时(7200S)失效，期间两个token都能使用。
3.每次用户登录时必须重新获取ticket。

### 2.Access Token获取
请求URL：**https://idasc.webank.com/api/oauth2/access_token**
请求方法:GET
请求参数：

| 参数 | 说明 |类型 |长度 | 是否必输 |
|---------|---------|---------|---------|---------|
| app_id | 腾讯服务分配的app_id | 字符串 |腾讯服务分配 |必输，腾讯服务分配的app_id |
| secret | 腾讯服务app_id的密钥 | 字符串 |腾讯服务分配 |必输，腾讯服务分配的secret |
|grant_type | 授权类型 | 字符串 |20 |必输，默认值：client_credential (必须小写) |
| version | 版本号 | 字符串 |20 |必输，默认值：1.0.0|

请求示例：
https://idasc.webank.com/api/oauth2/access_token?app_id=xxx&secret=xxx&grant_type=client_credential&version=1.0.0

响应：
```
{
"code":"0","msg":"请求成功",
"transactionTime":"20151022043831",
"access_token":"accessToken_string",
"expire_time":"20151022043831",
"expire_in":"7200"
}
```

注：
1．code不是0是表示获取失败，可以根据code和msg字段定位和调试。
2．expire_in为access_token的最大生存时间，单位秒，合作伙伴在判定**有效期时以此为准**。
3．expire_time为access_token失效的绝对时间，由于各服务器时间差异，不能使用作为有效期的判定依据，只展示使用。
4．修改secret之后，该app_id生成的access_token和ticket都失效。