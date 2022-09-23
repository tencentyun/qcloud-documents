## 操作场景

该任务指导您通过 API 网关控制台创建后端对接云函数 SCF 的 API。

## 前提条件
已完成 [服务创建](https://cloud.tencent.com/document/product/628/11787)。

## 操作步骤
### 步骤1：新建通用 API

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) ，在左侧导航栏单击**服务**。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击**管理 API** 标签页，根据后端业务类型选择创建**通用 API**。
4. 单击**新建**，进行后续配置。

### 步骤2：前端配置

API 的前端配置指提供给外界访问的相关配置，包括 API 名称、前端类型、请求协议、HTTP 方法、URL 路径和入参的定义。

#### 前端基础信息配置

- **API 名称**：您创建的 API 的名称，在当前服务内具有唯一性，支持最长60个字符。
- **前端类型**：API 网关支持 HTTP&HTTPS、WS&WSS 两种前端类型。
- **URL 路径（Path）**：您可以按需求写入合法 URL 路径。如需要在路径中配置动态参数，请使用`{}`符号，并在其中填入参数名，例如`/user/{userid}`路径，申明了路径中的 userid 参数，此参数同时需要在入参中作为 Path 类型参数进行定义。Query 参数可以不用在 URL 路径中定义。
  **路径支持正则表达式方式匹配**，路径输入内容以`/user`为例：
	- `=/user`：代表精确匹配，当存在多个 API 接口都有`/user`时，优先匹配含有`=/user`的配置的 API 接口。
	- `/user/{id}`：代表路径上存在动态参数，当存在多个 API 接口都有`/user`时，优先级第三匹配含有动态参数的配置的 API 接口。
	- `/user`：表示完全匹配或前缀匹配的方式访问，访问时`/user`、`/usertest`、`/user/test/a`都可以访问到`/user`路径的 API 接口。
- **请求方法**：可选择 GET、POST、PUT、DELETE、HEAD 方法。
- **鉴权类型**：支持 [免鉴权](https://cloud.tencent.com/document/product/628/11820)、[密钥对认证](https://cloud.tencent.com/document/product/628/11819)、[OAuth 2.0](https://cloud.tencent.com/document/product/628/38393) 三种鉴权类型。
- **支持 CORS**：用于配置跨域资源共享（CORS），开启后将默认在响应头中添加 `Access-Control-Allow-Origin : *`。

#### 前端参数配置

**入参**：入参包含了来源于 Header、Query、Path 的参数。其中 Path 参数对应于在 URL 路径中定义的动态参数。任一参数，均需要指定参数名，参数类型和参数数据类型；同时可以指明是否必填、默认值、示例数据和描述说明。利用这些配置，API 网关可以协助您完成入参的文档化和初步校验。
![](https://main.qcloudimg.com/raw/0d06c20c35e518d687e5dc46f9db8a43.png)

> ?
> - 请求协议为 HTTPS 时，需要请求中携带 SNI 标识，为了保障请求安全，API 网关会拒绝不携带 SNI 标识的请求。
> - SNI（Server Name Indication）是 TLS 的一个扩展协议，用于解决一个服务器拥有多个域名的情况，在 TLSv1.2 开始得到协议的支持。之前的 SSL 握手信息中没有携带客户端要访问的目标地址，如果一台服务器有多个虚拟主机，且每个主机的域名不一样，使用了不一样的证书，此时会无法判断返回哪一个证书给客户端，SNI 通过在 Client Hello 中补上 Host 信息解决该问题。

### 步骤3：后端配置对接云函数 SCF

API 的后端配置，是指的实际提供真实服务的配置。API 网关会将前端请求，依据后端配置进行转换后，转发调用到实际的服务上。
当您的业务实现在云函数 SCF 中，希望通过 API 网关将服务能力开放出来时，后端选用 SCF 对接。

![](https://main.qcloudimg.com/raw/1db8feaa662dfdc88211bd01bb5f7ba7.png)

后端对接 SCF 时，需要填写的参数如下表：

| 序号 | 参数名称 | 参数含义                               |
| ---- | -------- | -------------------------------------- |
| 1    | 命名空间 | 对接函数所在的命名空间，默认为 default |
| 2    | 名称     | 对接函数的名称                         |
| 3    | 版本     | 对接函数的版本，默认为 $LATEST         |
| 4    | 响应时间 | 响应时间，默认为15秒                   |
| 5    | 响应集成 | 见 [下文](#1)                                 |

响应集成说明：[](id:1)

针对 API 网关发送到云函数的请求处理方式，和云函数响应给 API 网关的返回值处理方式，称为请求方法和响应方法。请求方法和响应方法规划和实现的分别有透传方式和集成方式：

- 不开启集成响应，为透传方式。在 API 网关向 SCF 发送请求时，会以固定的结构体对 request 信息进行组合。SCF 收到的为此固定结构体，返回保持透传不做处理，响应格式仅支持 json。
- 开启响应集成时，为集成方式。API 网关向 SCF 发送请求时会以固定结构体对 request 信息进行组合，SCF 返回的也需要为固定结构体。API 网关再将 SCF 返回的内容映射到 statusCode、header、body 等位置返回给客户端。

如果开启响应集成，用户必须配置SCF，以如下数据格式返回数据给 API 网关，以便 API 网关解析：

```
{ 
        "isBase64Encoded": false, // 是否使用base64编码，值为 true 或者 false 
        "statusCode": 200, // http请求状态码 
        "headers": {"Content-Type":"text/html"}, // Content-Type 只支持字符串，不支持数组
        "body": "<html><body><h1>Heading</h1><p>Paragraph.</p></body></html>" 
}
```

API 网关发往 SCF 的结构体格式为：

```
{
  "requestContext": {
    "serviceId": "service-f94sy04v",
    "path": "/test/{path}",
    "httpMethod": "POST",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs"
    },
    "sourceIp": "10.0.2.14",
    "stage": "release"
  },
  "headers": {
    "Accept-Language": "en-US,en,cn",
    "Accept": "text/html,application/xml,application/json",
    "Host": "service-3ei3tii4-251000691.ap-guangzhou.apigateway.myqloud.com",
    "User-Agent": "User Agent String",
    "x-api-requestid": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef"
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
    "stage": "release"
  },
  "path": "/test/value",
  "queryString": {
    "foo" : "bar",
    "bob" : "alice"
  },
  "httpMethod": "POST",
  "isBase64Encoded": "true"
}
```

> ? 您可以通过编写云函数 SCF 来实现 Web 后端服务，并通过 API 网关对外提供服务。API 网关会将请求内容以参数形式传递给函数，并将函数返回作为响应返回给请求方。详细内容请参考 [API 网关触发器概述](https://cloud.tencent.com/document/product/583/12513)。

### 步骤4：响应配置

API 响应配置：包括 API 响应数据配置和 API 错误码配置。
API 响应数据配置：用于指明返回数据类型，包括成功调用的数据示例和失败调用的数据示例。
API 的错误码定义：用于指明额外的错误码、错误信息和描述。

> ?目前 API 网关对于响应结果不做处理，直接透传给请求者。在生成 SDK 文档时，填写的响应示例也会一并展示在文档中，它将会更好的帮助使用者理解接口含义。
