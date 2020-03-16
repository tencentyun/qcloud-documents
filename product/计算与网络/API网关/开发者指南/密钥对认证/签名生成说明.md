## 注意事项

- 若创建 API 时选择密钥对鉴权，则该 API 所在的服务需要发布、该发布环境需要绑定使用计划、而且该使用计划需要绑定密钥对，然后使用对应的密钥对生成签名内容来访问该 API。
- 含有中文和空格的 query，请求体 Body 需要对值进行 urlencode 编码，编码方式为 UTF-8。
- 通过参数计算签名时，必须使用编码前的值进行签名，不支持使用 urlencode 编码后的字符串进行签名。请您在签名之后再对 query、body 的值做 urlencode 编码。

## 客户端错误码
|错误码|状态码|语义|解决方案|
|--|---|---|---|
|HMAC signature cannot be verified, a validate authorization header is required|401|请求并未携带 Authorization 字段|请参照各语言签名 demo 构造该字段|
|authorization headers is invalidate|403|请求 Authorization 字段格式不正确|请参照各语言签名 demo 构造该字段|
|id or signature missing|403|请求 Authorization 字段无 ID 或者 signature 字段|请参照各语言签名 demo 构造该字段|
|HMAC signature cannot be verified, a valid $header header is required|403|请求 Authorization 字段中的 headers 字段在请求 header 中找不到对应字段	|请参照各语言签名 demo 构造该字段|
|HMAC signature cannot be verified, a valid date header is required|403|请求 Authorization 必须需要使用 date 字段作为鉴权字段之一|请参照各语言签名 demo 构造该字段|
|Found no validate usage plan|403|请求鉴权失败，API 需要鉴权，但该 API 并没有绑定使用计划|关闭该 API 的鉴权或者给该 API 所在的发布环境绑定使用计划，给该使用计划绑定密钥对|
|HMAC signature cannot be verified|403|请求鉴权失败，Authorization 字段中携带的 Key ID 并未绑定该 API 所在的发布环境，或者 Key ID 非法，或者该 Key 被禁用|请检查该密钥对是否可用，另外，检查该密钥对是否绑定对应使用计划/发布环境|
|HMAC signature does not match|403|请求鉴权失败，计算出来的 HMAC 值并不一致，请重新检查并计算 |计算的 HMAC 值错误，请参照各语言签名 demo 构造该字段|
|Not Found Host|404	|请求中没有携带 Host 字段	|请求携带 Host 字段，该字段值需要填服务器的域名，且为 String 类型|
|Get Host Fail|404|请求中携带的 Host 字段值并不是 String 类型|将 Host 字段值改为 String 类型|
|Could not support method|404|并不支持该请求方法类型|检查请求方法是否合法|
|There is no api match host[$host]|404|找不到请求服务器域名/地址|检查请求地址是否正确|
|There is no api match env_mapping[$env_mapping]|404|自定义域名后的 env_mapping 字段错误|检查绑定的自定义域名配置的 env_mapping 是否与自己填写的一致|
|There is no api match default env_mapping[$env_mapping]|404|默认域名后的 env_mapping 字段需要是 test/prepub/release|默认域名后的 env_mapping 字段需要是 test/prepub/release|
|There is no api match uri[$uri]|404|在该请求地址对应的服务下找不到对应 URI 匹配的 API|请检查 URI 填写是否正确|
|There is no api match method[$method]|404|在该请求地址+URI 对应的 API 并不支持该请求方法|请检查请求方法是否正确|
|"Not allow use HTTPS protocol或者Not allow use HTTP protocol"|404|该请求地址对应的服务并不支持对应 HTTP 协议类型|请检查请求协议类型是否正确|
|req is cross origin, api $uri need open cors flag on qcloud apigateway.|429|该请求是跨域请求，但对应的 API 并未打开跨域开关|请打开该 API 的跨域开关|
