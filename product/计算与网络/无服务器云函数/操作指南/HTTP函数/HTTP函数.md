## 简介
HTTP 函数（HTTP Function）是云函数的一种，区别于事件函数（Event Function）。HTTP 函数专门优化 Web 服务场景，例如自带 URL，通过发送 HTTP 请求到 URL 触发函数执行。


## 功能与优势
相较于 [API 网关触发器](https://cloud.tencent.com/document/product/583/12513) 云函数，HTTP 函数具备以下优势：
- HTTP Function 天然提供一个 URL 供用户访问和调用，简化了学习成本和调试过程，帮助您快速使用函数计算实现 Web 服务和 API。
- 您可以选择自己熟悉的 HTTP 测试工具验证函数计算端的功能和性能。
- 减少请求处理环节，HTTP Function 支持更高效的请求/响应格式，不需要 encode/decode 生成 json，性能更优。
- 方便对接其他支持 Webhook 回调的服务，例如 CDN 回源，企业微信机器人等。
- HTTP 函数的编写体验更贴近编写原生 WEB 服务，使用原生的 [HTTP Request/Response数据结构](http://nodejs.cn/api/http.html)。
- 丰富的框架支持，您可以使用常见的 WEB 框架（如 Nodejs Web 框架：`Express`、`Koa`）编写 HTTP 函数。WEB框架内置的一些中间件（如 `cors`）也会极大的方便您的业务编写。

HTTP 函数当前处于内测发布状态，请通过 [内测申请](https://cloud.tencent.com/apply/p/1zimo1hbjpu) 获得此功能。

## 使用限制
- 当前 HTTP 函数目前仅支持 `Nodejs 8.9`，后续会支持多个 Runtime。
- 函数类型选定为 `HTTP` 后不可更改。
- HTTP 函数不支持设置触发器。
- HTTP 函数暂不支持版本和别名。
- 在 `Request headers` 中有以下限制：
 - 所有 key 和 value 的大小不得超过 4 KB。
 - path（含 query、params）不得超过 4 KB。
 - body 大小不超过 6 MB。
- 在 `Response headers` 中有以下限制：
 - 所有 key 和 value 的大小不得超过 4 KB。
 - body 的大小不超过 6 MB。

## 问题分析
HTTP 函数的 Response headers 会包含请求 ID（`X-Scf-Request-Id`）和错误类型（`X-Scf-Error-Type`）来帮助您进行问题诊断。您可参考以下信息分析错误原因：


| 结构名                 | 内容 | 原因分析                                               |
| ---------------------- | ---- | ------------------------------------------------------ |
| ScfCommonError         | 400  | 域名和 url 格式错误时返回                                |
| ScfCommonError         | 404  | AppId、函数名等不存在                                  |
| ScfCommonError         | 413  | 当请求参数大小超过限制时返回                           |
| ScfCommonError         | 429  | 用户被流控，可减小并发量或者提交工单联系我们提高并发度 |
| ScfSysError            | 500  | 平台系统错误                                           |
| UnhandledInvocationErr | 502  | 响应大小超过限制                                       |
| UnhandledInvocationErr | 502  | 函数错误（如函数代码有语法错误或者异常）               |

## 快速入门
请参考 [HTTP 函数](https://cloud.tencent.com/document/product/583/37894) 通过快速创建一个 HTTP 函数，了解 HTTP 函数使用流程。
