### 调用 API 网关有哪些常见错误？
用户调用 API 网关时，常见的 HTTP 错误码及说明如下：

**前台错误**：

| 错误码 | 日志中错误提示                                               | 说明                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 401    | HMAC apikey is invalid for API.                               | APIKey 没有绑定到该 API。                                        |
| 401    | HMAC signature cannot be verified, a valid x-date header is required for   HMAC Authentication. | HMAC 认证时没有在 header 中带上  x-date，或者 HMAC 值非法。             |
| 401    | HMAC signature cannot be verified, the x-date header is out of date for   HMAC Authentication. | x-date 时间戳超时，默认为900s。                                   |
| 401    | HMAC signature cannot be verified, a valid date or x-date header is   required. | 如果没有 x-date，则 header 中包含 date。        |
| 401    | HMAC id or signature missing.                                 | Authorization 中 ID 或者 signatrue 字段缺失。                       |
| 401    | HMAC do not support multiple HTTP header.                     | 不支持一个 header 包含多个值的形式。                             |
| 401    | HMAC signature cannot be verified, a valid xxx header is required. | 请求中缺少 xxx header。                                         |
| 401    | HMAC algorithm xxx not supported.                             | HMAC 算法不支持 xxx，目前支持 hmac-sha1、hmac-sha256、hmac-sha384、hmac-sha512。 |
| 401    | HMAC authorization format error.                              | Authorization 格式错误。                                        |
| 401    | HMAC authorization headers is invalidate.                     | Authorization 缺少足够的参数，请参考 [密钥对认证-最终发送内容](https://cloud.tencent.com/document/product/628/11819#.E6.9C.80.E7.BB.88.E5.8F.91.E9.80.81.E5.86.85.E5.AE.B9)。                  |
| 401    | HMAC signature cannot be verified.                            | 无法检验签名，可能原因为 APIKey 无法识别，通常是 APIKey 没有绑定到这个服务或者没有绑定到这个 API。 |
| 401    | HMAC signature does not match.                                | 签名不一致。                                                   |
| 401    | Oauth call authentication server fail.                       | 调用认证服务器失败。                                           |
| 401    | Oauth found no related Oauth api.                             | 没有查到关联的 Oauth 认证 API，无法认证 id_token。                 |
| 401    | Oauth miss Oauth id_token.                                    | 请求缺少 id_token。                                             |
| 401    | Oauth signature cannot be verified, a validate authorization header is   required. | 没有认证头部。                                                     |
| 401    | Oauth authorization header format error.                      | Oauth 头部格式错误。                                            |
| 401    | Oauth found no authorization header.                          | 没有找到认证头部。                                             |
| 401    | Oauth found no id_token.                                      | 没有找到 id_token。                                             |
| 401    | Oauth id_token verify error.                                  | JWT 格式的 id_token 验证失败。                                    |
| 403    | Found no validate usage plan.                                 | 没有找到对应的使用计划，禁止访问（开启使用计划时可能出现的错误）。 |
| 403    | Cannot identify the client IP address, unix domain sockets are not   supported. | 无法识别源 IP。                                                 |
| 403    | Endpoint IP address is not allowed.                           | 禁止访问的后端 IP。                                             |
| 403    | Get xxx params fail.                                          | 从请求中获取参数出错。                                         |
| 403    | need header Sec-WebSocket-Key.                                | 实际请求缺少 header Sec-WebSocket-Key，配置了 websoket 的 API 会检验。 |
| 403    | need header Sec-WebSocket-Version.                            | 实际请求缺少 header Sec-WebSocket-Version，配置了 websoket 的 API 会检验。 |
| 403    | header xxx is required.                                       | 实际请求缺少 header xxx。                                       |
| 403    | path variable xxx is required.                                | 配置了路径变量`{xxx}`，但是与实际请求的路径不能匹配。           |
| 403    | querystring xxx is required.                                  | 实际请求缺少 querystring xxx。                                  |
| 403    | req content type need application/x-www-form-urlencoded.      | 配置了 body 参数的请求必须是表单格式。                           |
| 403    | body param xxx is required.                                   | 实际请求缺少 body 参数 xxx。                                     |
| 404    | Not found micro service with key.                             | 没有找到对应的微服务。                                         |
| 404    | Not Found Host.                                               | 请求携带 host 字段，该字段值需要填服务器的域名，且为 String 类型。  |
| 404    | Get Host Fail.                                                | 请求中携带的 host 字段值不是 String 类型。                       |
| 404    | Could not support method.                                     | 并不支持该请求方法类型。                                       |
| 404    | There is no api match host[$host].                            | 找不到请求服务器域名/地址。                                    |
| 404    | There is no api match env_mapping[$env_mapping].              | 自定义域名后的 env_mapping 字段错误。                            |
| 404    | There is no api match default env_mapping[$env_mapping].      | 默认域名后的 env_mapping 字段需要是 test/prepub/release。         |
| 404    | There is no api match uri[$uri].                              | 在该请求地址对应的服务下找不到对应 URI 匹配的 API。               |
| 404    | Not allow use HTTPS protocol或者Not allow use HTTP protocol.  | 该请求地址对应的服务并不支持对应 HTTP 协议类型。                 |
| 404    | Found no api.                                                 | 请求没有匹配到 API。                                            |
| 405    | Method Not Allowed.                                           | 不允许的 HTTP 请求方法。                                        |
| 426    | Not allow use HTTPS protocol.                                 | 不允许用 HTTPS 协议。                                            |
| 426    | Not allow use HTTP protocol.                                  | 不允许用 HTTP 协议。                                             |
| 426    | Not allow use xxx protocol.                                   | 不允许用 xxx 协议。                                              |
| 429    | API rate limit exceeded.                                      | 请求速率超过限速值，当前速率值可以查看请求的 header。           |
| 429    | API quota exceeded.                                           | 配置超限，剩余的配额可以通过请求的 header 查看。                 |
| 429    | req is cross origin, api $uri need open cors flag on qcloud   apigateway. | 该请求是跨域请求，但对应的 API 并未打开跨域开关。                |
| 481    | API config error.                                             | API 配置错误。                                                  |
| 481    | TSF config error.                                             | TSF 相关配置错误。                                              |
| 481    | Get location of micro service info fail.                      | 没有配置微服务名、微服务命名空间获取位置。                     |
| 481    | Only support the map_from like method.req.{path}.{}.     | 配置了微服务名、微服务空间的拉取位置，但是位置格式非法。       |
| 481    | Found no valid cors config.                                   | CORS 配置出错。                                                 |
| 481    | Oauth public key error.                                       | 配置的公钥证书错误。                                           |
| 481    | Oauth id_token location forbidden.                            | 不允许的 id_token 存放位置。                                     |
| 481    | Oauth found no oauth config.                                  | 没有找到 Oauth 配置。                                            |
| 481    | Oauth found no public key.                                    | 没有找到公钥。                                                 |
| 481    | Mock config error.                                            | mock 的配置出错。                                               |
| 499    | Client closed connetion.                                      | 客户端主动中断连接。                                           |

**后台错误**：

| 错误码 | 日志中错误提示                                               | 说明                                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 500    | Error occurred during query params.                           | query 参数处理出错。                                            |
| 500    | Internal Server Error.                                        | 1. 其他 APIGW 内部逻辑错误。<br>2. 若 API 为 proxy 类型，访问了没有权限访问的后端地址也会报该错误。 |
| 502    | Bad Gateway.                                                  | 连接后端服务出错，可能情况：<br>1. 后端拒绝服务，全部请求都为502。 <br>2. 后端高负载，导致部分请求响应为502。 |
| 504    | Gateway Time-out.                                             | 后端服务器连接超时。                                           |

