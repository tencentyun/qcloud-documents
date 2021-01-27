## 操作场景

客户端请求 API 网关，API 网关会将客户端请求内容处理后再传递给后端，此时 API 网关传递给后端的结构体一般是固定的。
本文记录了对接不同后端类型时 API 网关传递给后端的结构体，以便您开发排障使用。

## 后端对接公网 URL/IP 和对接 VPC 内资源的结构体

```
GET / HTTP/1.1
Host: 10.0.0.0
Connection: keep-alive
X-Client-Proto: http
X-Client-Proto-Ver: HTTP/1.1
X-Forwarded-For: 100.100.10.1
X-Real-IP: 100.100.10.1
User-Agent: curl/7.29.0
Accept: /
x-b3-traceid: 12345678906f******7cd8db0fe843dc
X-Api-RequestId: 12345678906f******7cd8db0fe843dc
X-Api-Scheme: http
```

数据结构内容详细说明如下：

| 名称               | 内容                                                         |
| ------------------ | ------------------------------------------------------------ |
| Host               | 用于指定虚拟主机                                             |
| Connection         | 用于决定当前的事务完成后，是否会关闭网络连接                 |
| X-Client-Proto     | 记录客户端请求协议                                           |
| X-Client-Proto-Ver | 记录客户端请求协议版本                                       |
| X-Forwarded-For    | 记录从客户端发起请求后访问过的每一个 IP 地址                 |
| X-Real-IP          | 记录客户端请求的真实 IP 地址                                 |
| User-Agent         | 记录客户端请求工具                                           |
| Accept             | 代表客户端希望接受的数据类型                                 |
| x-b3-traceid       | 记录本次请求的 RequestId，等值于 X-Api-RequestId，用于适配 API 网关内部模块 |
| X-Api-RequestId    | 记录本次请求的 RequestId                                      |
| X-Api-Scheme       | 记录客户端请求协议，等值于 X-Client-Proto，用于适配 API 网关内部模块 |

>!由于不同 Content-Type 的请求 body 结构不同，且客户端请求可能添加自定义 Header，本文仅列出了经过 API 网关后的固定请求 Header。

## 后端对接 SCF 的结构体

```
{
	"body": "{key:value}",
	"requestContext": {
		"httpMethod": "ANY",
		"serviceId": "service-dlhbuxqh",
		"path": "/scf/{pathParam}",
		"sourceIp": "14.17.22.36",
		"identity": {},
		"stage": "release"
	},
	"queryStringParameters": {
		"queryParam": ""
	},
	"headers": {
		"content-length": "11",
		"x-b3-traceid": "12345678906f******7cd8db0fe843dc",
		"x-qualifier": "$DEFAULT",
		"accept": "/",
		"user-agent": "curl/7.69.1",
		"host": "service-abcdefgh-1234567890.gz.apigw.tencentcs.com",
		"requestsource": "APIGW",
		"x-api-scheme": "http",
		"x-api-requestid": " 12345678906f******7cd8db0fe843dc",
		"content-type": "application/x-www-form-urlencoded"
	},
	"pathParameters": {
		"pathParam": "mypath"
	},
	"queryString": {
		"a": "1",
		"b": "2"
	},
	"httpMethod": "POST",
	"headerParameters": {
		"headerparam": ""
	},
	"path": "/scf/mypath",
	"isBase64Encoded": "true",
}
```

数据结构内容详细说明如下：

| 名称                  | 内容                                                         |
| --------------------- | ------------------------------------------------------------ |
| requestContext        | 请求来源的 API 网关的配置信息、请求标识、认证信息、来源信息。其中：<li>serviceId，path，httpMethod 指向 API 网关的服务 ID、API 的路径和方法。<li>stage 指向请求来源 API 所在的环境。<li>requestId 标识当前这次请求的唯一 ID。<li>identity 标识用户的认证方法和认证的信息。<li>sourceIp 标识请求来源 IP。 |
| path                  | 记录实际请求的完整 Path 信息。                               |
| httpMethod            | 记录实际请求的 HTTP 方法。                                   |
| queryString           | 记录实际请求的完整 Query 内容。                              |
| body                  | 记录实际请求转换为 String 字符串后的内容。                   |
| headers               | 记录实际请求的完整 Header 内容。                             |
| pathParameters        | 记录在 API 网关中配置过的 Path 参数以及实际取值。            |
| queryStringParameters | 记录在 API 网关中配置过的 Query 参数以及实际取值。           |
| headerParameters      | 记录在 API 网关中配置过的 Header 参数以及实际取值。          |
| isBase64Encoded       | 记录在请求体是否被进行了 Base64 编码，取值为 true 或 false。  | 


