## 支持的 API

 Prometheus 监控服务所有支持的 API 与开源 Prometheus 提供的 API 有相同的参数输入和响应数据格式，未在此列出的 API 默认都不支持，或者部分 API 不是所有的版本都支持，以当前文档为准，所有 API 均为 HTTP 协议：

| API                               |          说明       | 使用方式 |
|-----------------------------------|:-------------------:|----------|
| /api/v1/query                     | [查询某一时刻的数据](https://prometheus.io/docs/prometheus/latest/querying/api/#instant-queries) | 推荐使用 Grafana，可使用 HTTP 相关工具，部分 SDK 提供实现 |
| /api/v1/query_range               | [查询时间范围类的数据](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries) | 推荐使用 Grafana，可使用 HTTP 相关工具，部分 SDK 提供实现 |
| /api/v1/series                    | [查询 series](https://prometheus.io/docs/prometheus/latest/querying/api/#finding-series-by-label-matchers) | 推荐使用 Grafana，可使用 HTTP 相关工具，部分 SDK 提供实现 |
| /api/v1/labels                    | [查询标签名](https://prometheus.io/docs/prometheus/latest/querying/api/#getting-label-names) | 推荐使用 Grafana，可使用 HTTP 相关工具，部分 SDK 提供实现 |
| /api/v1/label/{label_name}/values | [查询标签名多对应的值](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-label-values) | 推荐使用 Grafana，可使用 HTTP 相关工具，部分 SDK 提供实现 |
| /api/v1/prom/write                | [remote write](https://prometheus.io/docs/practices/remote_write/) 上报数据 | 常用方式为使用相关 Agent，比如 Prometheus|
| /metrics/{job}/{label-pairs*}     | [Pushgateway](https://prometheus.io/docs/instrumenting/pushing/) 上报数据 | 开源 SDK |

>? Prometheus 监控服务不直接提供 SDK 实现，需使用开源 Prometheus 实现，各语言的实现请参见：[开源指引](https://prometheus.io/docs/instrumenting/clientlibs/) 。
 [Pushgateway](https://prometheus.io/docs/practices/pushing/) 协议在这里仅作为 [remote write](https://prometheus.io/docs/practices/remote_write/) 协议的补充，不支持删除操作，可以理解为我们提供的删除接口是空的不执行任何逻辑，特殊需求可自行部署 [PushGateway](https://github.com/prometheus/pushgateway)。

## 认证方法

以上提供的所有的 API 都需要认证，且所有的认证方式都支持下面两种。

### Basic Auth （推荐）

Basic Auth 兼容原生 Prometheus Query 的认证方式，用户名为用户的 APPID，进入控制台基本信息里面的 Token 即为密码。

了解更多：https://swagger.io/docs/specification/authentication/basic-authentication/

### Bearer Token

Bearer Token 随着实例创建而生成，进入控制台查看基本信息里面的 Token。

了解更多：https://swagger.io/docs/specification/authentication/bearer-authentication/


## API 响应及相关状态码

数据上报请求无固定的响应格式，程序只需关注状态码即可，错误响应最好记录详细的响应信息。

查询请求的响应格式为 JSON，基本结构如下：
```
{
  "status": "success" | "error",
  "data": <data>,

  // 当 status 状态为 error 时，下面的数据将被返回。
  "errorType": "<string>",
  "error": "<string>",

  // 当执行请求时有警告信息时，该字段将被填充返回。
  "warnings": ["<string>"]
}
```

相关状态码注解，错误相关的详细信息会包含在 HTTP 响应体内：

| 状态码 | 请求类型 | 概述 |
|--------|----------|------|
| 400    | 查询 / 数据上报 | 请求参数错误 / 数据上报时如果 series 达到上限可能会出现此错误 |
| 401    | 查询 / 数据上报 | 认证失败 |
| 404    | 查询 / 数据上报 | API 不存在 |
| 422    | 查询 | 查询请求的表达式无法执行([RFC4918](https://datatracker.ietf.org/doc/html/rfc4918#page-78)) |
| 429    | 数据上报 | 数据上报时 samples 速率达到上限（对于基础版，如果自监控上体现出余量还较多，Agent 会自动重试上报数据，这种情况理论上不会丢失数据，平均下来不超过限制）|
| 500    | 查询 / 数据上报 | 内部错误，频繁出现请联系我们 |
| 503    | 查询 / 数据上报 | 服务在启动、重建或升级中 / 查询请求被中止或者超时 |
