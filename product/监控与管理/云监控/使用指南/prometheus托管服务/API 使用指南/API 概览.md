## HTTP API

Prometheus 所有稳定的 HTTP API 都在 `/api/v1` 路径下。当我们有数据查询需求时，可以通过查询 API 请求监控数据，提交数据可以使用 [remote write](https://prometheus.io/docs/practices/remote_write/) 协议或者 [Pushgateway](https://prometheus.io/docs/practices/pushing/) 的方式。

## 支持的 API

| API                               |         说明          | 需要认证 | 方法         |
| --------------------------------- | :-------------------: | -------- | ------------ |
| /api/v1/query                     |       查询接口        | 是       | GET/POST     |
| /api/v1/query_range               |       范围查询        | 是       | GET/POST     |
| /api/v1/series                    |      series 查询      | 是       | GET/POST     |
| /api/v1/labels                    |      labels 查询      | 是       | GET/POST     |
| /api/v1/label/&lt;label_name>/values |   label value 查询    | 是       | GET          |
| /api/v1/prom/write                | remote write 数据提交 | 是       | remote write |
| Pushgateway                       | pushgateway 数据提交  | 是       | SDK          |

## 认证方法

默认开启认证，因此所有的接口都需要认证，且所有的认证方式都支持 Bearer Token和 Basic Auth。

### Bearer Token

Bearer Token 随着实例产生而生成，可以通过控制台进行查询。了解 Bearer Token 更多信息，请参见 [Bearer Authentication](https://swagger.io/docs/specification/authentication/bearer-authentication/)。

### Basic Auth

Basic Auth 兼容原生 Prometheus Query 的认证方式，用户名为用户的 APPID，密码为 bearer token（实例产生时生成），可以通过控制台进行查询。了解 Basic Auth 更多信息，请参见 [Basic Authentication](https://swagger.io/docs/specification/authentication/basic-authentication/)。   


## 数据返回格式

所有 API 的响应数据格式都为 JSON。每一次成功的请求会返回 `2xx` 状态码。

无效的请求会返回一个包含错误对象的 JSON 格式数据，同时也将包含一个如下表格的状态码：

| 状态码 | 含义                                         |
| ------ | -------------------------------------------- |
| 401    | 认证失败                                     |
| 400    | 当参数缺失或错误时返回无效的请求状态码       |
| 422    | 当一个无效的表达式无法被指定时 (RFC4918)     |
| 503    | 当查询不可用或者被取消时返回服务不可用状态码 |

无效请求响应返回模板如下：

```
{
  "status": "success" | "error",
  "data": <data>,

  // 当 status 状态为 error 时，下面的数据将被返回
  "errorType": "<string>",
  "error": "<string>",

  // 当执行请求时有警告信息时，该字段将被填充返回
  "warnings": ["<string>"]
}
```
