### 常见错误码

| 错误码 | 日志中错误提示                                               | 说明                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 401    | HMAC apikey is invalid for API                               | APIKey没有绑定到该API                                        |
| 401    | HMAC signature cannot be verified, a valid x-date header is required for   HMAC Authentication | Hmac认证时没有在header中带上x-date，或者其值非法             |
| 401    | HMAC signature cannot be verified, the x-date header is out of date for   HMAC Authentication | x-date时间戳超时，默认900s                                   |
| 401    | HMAC signature cannot be verified, a valid date or x-date header is   required | 如果没有x-date, 那么需要header中包含date                     |
| 401    | HMAC id or signature missing                                 | Authorization中id或者signatrue字段缺失                       |
| 401    | HMAC do not support multiple HTTP header                     | 不支持一个header包含多个值的形式                             |
| 401    | HMAC signature cannot be verified, a valid xxx header is required | 请求中缺少xxx header                                         |
| 401    | HMAC algorithm xxx not supported                             | Hmac算法不支持,目前支持hmac-sha1, hmac-sha256，hmac-sha384, hmac-sha512 |
| 401    | HMAC authorization format error                              | Authorization格式错误                                        |
| 401    | HMAC authorization headers is invalidate                     | Authorization缺少足够的参数，请参考说明文档                  |
| 401    | HMAC signature cannot be verified                            | 无法检验签名，可能原因为apikey无法识别      通常是APIKEY没有绑定到这个服务或者没有绑定到这个API |
| 401    | HMAC signature does not match                                | 签名不一致                                                   |
| 401    | Oauth call authentication server fail.                       | 调用认证服务器失败                                           |
| 401    | Oauth found no related Oauth api                             | 没有查到关联的Aouth认证api, 无法认证id_token                 |
| 401    | Oauth miss Oauth id_token                                    | 请求缺少id_token                                             |
| 401    | Oauth signature cannot be verified, a validate authorization header is   required | 认证头部                                                     |
| 401    | Oauth authorization header format error                      | Oauth头部格式错误                                            |
| 401    | Oauth found no authorization header                          | 没有找到认证头部                                             |
| 401    | Oauth found no id_token                                      | 没有找到id_token                                             |
| 401    | Oauth id_token verify error                                  | jwt格式的id_token验证失败                                    |
| 403    | Found no validate usage plan                                 | 没有找到对应的使用计划，禁止访问(开启使用计划时可能出现的错误) |
| 403    | Cannot identify the client IP address, unix domain sockets are not   supported. | 无法识别源IP                                                 |
| 403    | Endpoint IP address is not allowed                           | 禁止访问的后端IP                                             |
| 403    | Get xxx params fail                                          | 从请求中获取参数出错                                         |
| 403    | need header Sec-WebSocket-Key                                | 实际请求缺少header Sec-WebSocket-Key, 配置了websoket的API会检验 |
| 403    | need header Sec-WebSocket-Version                            | 实际请求缺少header Sec-WebSocket-Version, 配置了websoket的API会检验 |
| 403    | header xxx is required                                       | 实际请求缺少header xxx                                       |
| 403    | path variable xxx is required                                | 配置了路径变量 {xxx}，但是实际请求的路径不能匹配上           |
| 403    | querystring xxx is required                                  | 实际请求缺少querystring xxx                                  |
| 403    | req content type need application/x-www-form-urlencoded      | 配置了body参数的请求必须是表单格式                           |
| 403    | body param xxx is required                                   | 实际请求缺少body参数 xxx                                     |
| 404    | Not found micro service with key                             | 没有找到对应的微服务                                         |
| 404    | Not Found Host                                               | 请求携带host字段，该字段值需要填服务器的域名，且为string类型 |
| 404    | Get Host Fail                                                | 请求中携带的Host字段值并不是string类型                       |
| 404    | Could not support method                                     | 并不支持该请求方法类型                                       |
| 404    | There is no api match host[$host]                            | 找不到请求服务器域名/地址                                    |
| 404    | There is no api match env_mapping[$env_mapping]              | 自定义域名后的env_mapping字段错误                            |
| 404    | There is no api match default env_mapping[$env_mapping]      | 默认域名后的env_mapping字段需要是test/prepub/release         |
| 404    | There is no api match uri[$uri]                              | 在该请求地址对应的服务下找不到对应uri匹配的API               |
| 404    | Not allow use HTTPS protocol或者Not allow use HTTP protocol  | 该请求地址对应的服务并不支持对应HTTP协议类型                 |
| 404    | Found no api                                                 | 请求没有匹配到API                                            |
| 426    | Not allow use HTTPS protocol                                 | 不允许用HTTPS协议                                            |
| 426    | Not allow use HTTP protocol                                  | 不允许用HTTP协议                                             |
| 426    | Not allow use xxx protocol                                   | 不允许用xxx协议                                              |
| 429    | API rate limit exceeded                                      | 请求速率超过限速值，当前速率值可以查看请求的Header           |
| 429    | API quota exceeded                                           | 配置超限，剩余的配额可以通过请求的header查看                 |
| 429    | req is cross origin, api $uri need open cors flag on qcloud   apigateway. | 该请求是跨域请求，但对应的API并未打开跨域开关                |
| 481    | API config error                                             | API配置错误                                                  |
| 481    | TSF config error                                             | TSF相关配置错误                                              |
| 481    | Get location of micro service info fail                      | 没有配置微服务名，微服务命名空间获取位置                     |
| 481    | Only support the map_from like method.req.{path}.{}, but     | 配置了微服务名，微服务空间的拉取位置，但是位置格式非法       |
| 481    | Found no valid cors config                                   | CORS配置出错                                                 |
| 481    | Oauth public key error                                       | 配置的公钥证书错误                                           |
| 481    | Oauth id_token location forbidden                            | 不允许的id_token存放位置                                     |
| 481    | Oauth found no oauth config                                  | 没有找到Oauth配置                                            |
| 481    | Oauth found no public key                                    | 没有找到公钥                                                 |
| 481    | Mock config error                                            | mock的配置出错                                               |
| 499    | Client closed connetion                                      | 客户端主动中断连接                                           |
| 500    | Error occurred during query params                           | query参数处理出错                                            |
| 500    | Internal Server Error                                        | 其他APIGW内部逻辑错误      或者若API为proxy类型，访问了没有权限访问的后端地址也会报该错误 |
| 502    | Bad Gateway                                                  | 连接后端服务出错,可能情况: 1. 后端拒绝服务,全部请求都为502 2. 后端高负载, 导致部分请求响应502 |
| 504    | Gateway Time-out                                             | 后端服务器连接超时                                           |