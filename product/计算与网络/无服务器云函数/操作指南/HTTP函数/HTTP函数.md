## HTTP 函数
### 概述
HTTP 函数（HTTP Function）是云函数的一种。区别于事件函数（Event Function），HTTP函数专门为Web服务场景而优化，自带 URL，并通过发送 HTTP 请求到 URL 触发函数执行。

相较于[API网关触发器](https://cloud.tencent.com/document/product/583/12513)云函数，HTTP 函数有以下优势：

* HTTP Function 天然提供一个 URL 供用户访问和调用，简化学习成本和调试过程，帮助您快速使用函数计算实现 Web 服务和 API；
* 您可以选择自己熟悉的 HTTP 测试工具验证函数计算端的功能和性能；
* 减少请求处理环节，HTTP Function支持更高效的请求/响应格式，不需要 encode/decode 成 json，性能更优；
* 方便对接其他支持 Webhook 回调的服务，例如 CDN 回源，企业微信机器人等；
* HTTP 函数的编写体验更贴近编写原生WEB服务，使用 Node.js 原生接口（使用原生的[HTTP Request/Response数据结构](http://nodejs.cn/api/http.html)）。
* 丰富的框架支持。您可以使用常见的WEB框架（如Nodejs  `Express` ， `Koa` ）编写HTTP函数。WEB框架内置的一些中间件（如`cors`）也会极大的方便您的业务编写。

HTTP 函数当前处于内测发布状态，申请内测请点击xxxx

### 快速入门
请参考xxxx

### 使用限制
* 当前HTTP 函数仅支持 `Nodejs 8.9`，其他Runtime会在后续逐步支持
* 函数类型选定为`HTTP`后不可更改
* HTTP 函数不支持设置触发器
* HTTP 函数暂不支持版本和别名
* Request headers 中的所有 key 和 value 的大小不得超过 4 KB；path（含 query、params）不得超过 4 KB；body 大小不超过 6 MB。
* Response headers 中的所有 key 和 value 的大小不得超过 4 KB；body 的大小不超过 6 MB。

### 问题诊断
HTTP 函数的Response headers会包含`X-Scf-Request-Id`（请求ID）和`X-Scf-Error-Type`（错误类型）来帮助您进行问题诊断。


| 结构名                 | 内容 | 原因分析                                               |
| ---------------------- | ---- | ------------------------------------------------------ |
| ScfCommonError         | 400  | 域名和url格式错误时返回                                |
| ScfCommonError         | 404  | AppId、函数名等不存在                                  |
| ScfCommonError         | 413  | 当请求参数大小超过限制时返回                           |
| ScfCommonError         | 429  | 用户被流控，可减小并发量或者提交工单联系我们提高并发度 |
| ScfSysError            | 500  | 平台系统错误                                           |
| UnhandledInvocationErr | 502  | 响应大小超过限制                                       |
| UnhandledInvocationErr | 502  | 函数错误（如函数代码有语法错误或者异常）               |