## 概述
用户可以编写 SCF 函数来处理自身业务逻辑，并通过 SCF 暴露的管理接口来触发云函数。管理接口在腾讯云中统一称为云 API。通过使用 SCF 云 API 中的 Invoke 接口，用户可以按需触发调用云函数。
详细的云 API 接口调用方法可见 [运行函数 API](https://cloud.tencent.com/document/product/583/17243) 文档。云 API 触发器具有以下特点：
- **调用模式可选**：可根据 InvocationType 参数，自行定义同步或异步触发方法。
- **自定义事件**：可根据 ClientContext 参数，自行定义触发云函数的事件或数据内容，内容需要以 JSON 格式编码。

## 云 API 调用
通过云 API 触发云函数，需要：
1. [按 API 接口进行鉴权](https://cloud.tencent.com/document/product/583/17239)；
2. [填写公共参数](https://cloud.tencent.com/document/product/583/17238)；
3. 根据 [返回结果](https://cloud.tencent.com/document/product/583/17240) 解析返回结果。

另外，为了避免自行构造请求内容及解析内容，用户也可以直接使用云 API SDK 触发云函数。 云 API SDK 提供了 Python，PHP，Java，GO，.NET，Node.js 语言的实现，各语言 SDK 的具体使用方式可见 [腾讯云 SDK 中心](https://cloud.tencent.com/document/sdk)。

