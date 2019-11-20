>? HTTP 函数功能在全新升级中，后期会开放申请使用，您可以前往 [云函数介绍页](https://cloud.tencent.com/product/scf) 来了解最新进展。
>
## 简介
HTTP 函数（HTTP Function）是云函数的一种，区别于事件函数（Event Function）。HTTP 函数专注于优化 Web 服务场景，例如自带 URL 并通过发送 HTTP 请求到 URL 触发函数执行。


## 功能与优势
相较于 [API 网关触发器](https://cloud.tencent.com/document/product/583/12513) 云函数，HTTP 函数具备以下优势：
- HTTP 函数提供一个 URL 供用户访问和调用，简化了学习成本和调试过程，帮助您快速使用函数计算实现 Web 服务和 API。
- 您可以选择自己熟悉的 HTTP 测试工具验证函数计算端的功能和性能。
- 减少请求处理环节，HTTP 函数支持更高效的请求/响应格式，不需要 encode/decode 生成 json，性能更优。
- 方便对接其他支持 Webhook 回调的服务，例如 CDN 回源，企业微信机器人等。
- HTTP 函数的编写体验更贴近编写原生 Web 服务，使用 Node.js 原生接口（[HTTP Request/Response 数据结构](http://nodejs.cn/api/http.html)）。
- 丰富的框架支持，您可以使用常见的 Web 框架（如 Nodejs Web 框架：`Express`、`Koa`）编写 HTTP 函数。而 Web 框架内置的一些中间件（如 `cors`）也会极大的方便您的业务编写。



## 使用限制
- 当前 HTTP 函数目前仅支持 `Nodejs 8.9`，后续会支持多个 Runtime。
- 函数类型选定为 `HTTP` 后不可更改。
- HTTP 函数不支持设置触发器。
- HTTP 函数暂不支持版本和别名。
- 在 `Request headers` 中有以下限制：
 - 所有 key 和 value 的大小不得超过4KB。
 - path（含 query、params）不得超过4KB。
 - body 大小不超过6MB。
- 在 `Response headers` 中有以下限制：
 - 所有 key 和 value 的大小不得超过4KB。
 - body 的大小不超过6MB。

## 问题分析
当 HTTP 函数出现问题时，Response headers 会包含请求 ID（`X-Scf-Request-Id`）和错误类型（`X-Scf-Error-Type`）信息，来帮助您分析问题原因。您可参考以下信息查看错误原因：


| 结构名                 | 内容 | 原因分析                                               |
| ---------------------- | ---- | ------------------------------------------------------ |
| ScfCommonError         | 400  | 域名和 url 格式错误时返回                                |
| ScfCommonError         | 404  | AppId、函数名等不存在                                  |
| ScfCommonError         | 413  | 当请求参数大小超过限制时返回                           |
| ScfCommonError         | 429  | 用户被流控，可减小并发量或者 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=668&source=0&data_title=%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BA%91%E5%87%BD%E6%95%B0%20SCF&level3_id=671&radio_title=%E4%BD%BF%E7%94%A8%E9%99%90%E5%88%B6%E6%8F%90%E5%8D%87%E7%94%B3%E8%AF%B7&queue=81&scene_code=17230&step=2) 联系我们提高并发度 |
| ScfSysError            | 500  | 平台系统错误                                           |
| UnhandledInvocationErr | 502  | 响应大小超过限制                                       |
| UnhandledInvocationErr | 502  | 函数错误（如函数代码有语法错误或者异常）               |

## 快速入门
请参考 [HTTP 函数快速入门](https://cloud.tencent.com/document/product/583/37894) 通过快速创建一个 HTTP 函数，了解 HTTP 函数使用流程。
