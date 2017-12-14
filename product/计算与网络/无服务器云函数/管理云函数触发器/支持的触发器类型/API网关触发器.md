用户可以编写 SCF 云函数来实现 Web 后端服务，并通过 API 网关对外提供服务。API 网关会将 API 请求内容以参数形式传递给函数，并将函数返回作为 API 响应返回给请求方。

API 网关触发器具有以下特点：

- **Push 模型**：API 网关在接受到 API 请求后，如果 API 在网关上的后端配置了对接云函数，函数将会被触发运行，同时 API 网关会将 API 请求的相关信息，例如具体接受到请求的服务和 API 规则，请求的实际路径，方法，请求的path，header，query等参数，全部封装为请求入参，以 event 入参的形式发送给触发的函数。
- **同步调用**：API 网关以同步调用的方式来调用函数，会在 API 网关中配置的超时时间未到前等待函数返回。有关调用类型的更多信息，请参阅[调用类型](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B)。

## API 网关触发器配置

API 网关触发器配置并**不在云函数中进行配置**，而是在 API 网关中进行。在 API 网关中配置 API 规则时，后端配置可选 Cloud Function，在选择 Cloud Function 后，即可选择与 API 服务相同地域的云函数。

在 API 网关配置对接云函数时，同样会配置超时时间。API 网关中的请求超时时间，和云函数的运行超时时间，两者分别生效。超时规则如下：
* API 网关超时时间 > 云函数超时时间：云函数超时先生效，API 请求响应为 200 http code，但返回内容为云函数超时报错内容。
* API 网关超时时间 < 云函数超时时间：API网关超时先生效，API 请求返回 5xx http code，标识请求超时。

## API 网关触发器绑定限制
 
API 网关中，一条 API 规则仅能绑定一个云函数，但一个云函数可以被多个 API 规则绑定为后端。同时，目前 API 网关触发器仅支持同地域云函数绑定，即广州区创建的云函数，仅支持被广州区创建的 API 服务中规则所绑定和触发。如果您想要使用特定地域的 API 网关配置来触发云函数，可以通过在对应地域下创建函数来实现。

## API 网关触发器的事件消息结构

在API网关接收到请求时，会将类似以下的 JSON 格式事件数据发送给绑定的云函数。

```
{
  "requestContext": {
    "serviceName": "testsvc",
    "path": "/test/{path}",
    "httpMethod": "POST",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs"
    },
    "sourceIp": "10.0.2.14",
    "stage": "prod"
  },
  "headers": {
    "Accept-Language": "en-US,en,cn",
    "Accept": "text/html,application/xml,application/json",
    "Host": "service-3ei3tii4-251000691.ap-guangzhou.apigateway.myqloud.com",
    "User-Agent": "User Agent String"
  },
  "body": "{\"test\":\"body\"}",
  "pathParameters": {
    "path": "value"
  },
  "queryStringParameters": {
    "foo": "bar"
  },
  "headerParameters":{
    "Refer": "10.0.2.14"
  },
  "stageVariables": {
    "stage": "test"
  },
  "path": "/test/value",
  "query": "foo=bar&bob=alice",
  "httpMethod": "POST"
}
```

其中，`requestContext` 结构标识了 API 请求来源服务和 API 规则、所生效的环境、请求id、认证信息等内容。`pathParameters`,`queryStringParameters`,`headerParameters`等内容包含了 API 规则中所配置入参的参数名称和实际值，`httpMethod`、`path`、`body`、`headers`等内容包含了实际请求内容。

## API 网关触发器对云函数返回内容的处理

由于使用的是同步调用，API 网关会触发云函数后等待函数执行完成，并将函数返回，作为 API 请求的响应内容返回给 API 请求的发起方，因此，此特性可以用来使用云函数实现 API 后端服务，将 API 请求进行处理后，返回处理结果并被传递至 API 请求者。