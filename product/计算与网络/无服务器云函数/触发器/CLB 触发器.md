您可以通过编写云函数 SCF 来实现 Web 后端服务，并通过负载均衡 CLB 对外提供服务。负载均衡 CLB 触发器会将请求内容以参数形式传递给函数，并将函数返回作为响应返回给请求方。

CLB 触发器具有以下特点：
- **Push 模型**
负载均衡 CLB 监听器在接受到 CLB 侧发出的请求后，如果 CLB 在后端配置了对接的云函数，该函数将会被触发运行。同时 CLB 会将请求的相关信息以 event 入参的形式发送给被触发的函数。相关信息包含了具体接受到请求的方法、请求的 path、header、query 等内容。
- **同步调用**
CLB 触发器通过同步调用的方式来调用函数。有关调用类型的更多信息，请参阅 [调用类型](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B)。

>?
- CLB 触发器目前处于灰度测试阶段，您可点击 [申请链接](https://cloud.tencent.com/apply/p/h2r3ix3s5vs) 进行申请。
- CLB 账户分为标准账户类型和传统账户类型。传统账户类型不支持绑定 SCF，建议升级为标准账户类型。详情可参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。 
>

## CLB 触发器配置

CLB 触发器支持在  **[云函数控制台](https://console.cloud.tencent.com/scf/index)** 或在  **[负载均衡控制台](https://console.cloud.tencent.com/clb/index)** 中进行配置。
<dx-tabs>
::: 云函数控制台
在**云函数控制台**中，支持 [在触发方式中添加 CLB 负载均衡触发器](https://cloud.tencent.com/document/product/583/30230#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.AE.8C.E6.88.90.E8.A7.A6.E5.8F.91.E5.99.A8.E5.88.9B.E5.BB.BA)、支持选取已有 CLB 负载均衡或新建主机路由规则、支持配置 URL 请求路径。
:::
::: 负载均衡控制台
在**负载均衡控制台**中配置路由规则时，后端配置可选 Cloud Function，且在选择 Cloud Function 后，即可选择与 CLB 负载均衡相同地域的云函数。在负载均衡控制台上，可以配置及管理更高阶的 CLB 负载均衡服务，例如 WAF 防护、SNI 多域名证书，弹性网卡等能力。
:::
</dx-tabs>



## CLB 触发器绑定限制

- CLB 负载均衡中，一条 CLB 负载均衡路径规则仅能绑定一个云函数，但一个云函数可以被多个 CLB 负载均衡规则绑定为后端。相同路径、相同监听器及主机被视为同一个规则，无法重复绑定。
- 目前 CLB 负载均衡触发器仅支持同地域云函数绑定。例如，广州地区创建的云函数，仅支持被广州地区创建的 CLB 负载均衡中规则所绑定和触发。


## 请求与响应
CLB 负载均衡发送到云函数的请求处理方式，和云函数响应给 CLB 负载均衡的返回值处理方式，称为请求方法和响应方法。请求方法和响应方法都为 CLB 触发器自动处理。CLB 触发器触发云函数时，必须按照响应方法返回数据结构。
>! `X-Vip`、`X-Vport`、`X-Uri`、`X-Method`、`X-Real-Port` 字段必须先在 CLB 控制台进行自定义配置后才可以进行传递，自定义配置可参考 [CLB 产品文档](https://cloud.tencent.com/document/product/214/15171)。


#### CLB 触发器的集成请求事件消息结构[](id:datastructures)
在  CLB 负载均衡触发器接收到请求时，会将类似以下 JSON 格式的事件数据发送给绑定的云函数。

>! 在 CLB 触发场景下，所有的请求和响应由于需要以 JSON 方式传递，对于一些图片、文件等数据，直接放入 JSON 会导致不可见字符丢失，需要进行 Base64 编码，此处规定如下：
> - 如果 Content-type 为 text/*、application/json、application/javascript、application/xml，CLB 不会对 body 内容进行转码。
> - 其他类型一律进行 Base64 转码再转发。


```
{  
  "headers": { 
    "Content-type": "application/json",  
    "Host": "test.clb-scf.com",  
    "User-Agent": "Chrome",  

    "X-Stgw-Time": "1591692977.774",  
    "X-Client-Proto": "http",  
    "X-Forwarded-Proto": "http",  
    "X-Client-Proto-Ver": "HTTP/1.1",  
    "X-Real-IP": "9.43.175.219",
    "X-Forwarded-For": "9.43.175.xx"  
 
    "X-Vip": "121.23.21.xx",  
    "X-Vport": "xx",  
    "X-Uri": "/scf_location",  
    "X-Method": "POST"    
    "X-Real-Port": "44347",  
  },  
  "payload": {  
    "key1": "123",  
    "key2": "abc"  
  },
}  
```

数据结构内容详细说明如下：

|    结构名    | 内容 |
| ---------- | --- |
| X-Stgw-Time |  请求发起的时间戳 |
| X-Forwarded-Proto | 请求的 scheme 结构体|
| X-Client-Proto-Ver | 协议类型 |
| X-Real-IP | 客户端IP地址 |   
| X-Forward-For | 经过的代理IP地址 |
| X-Real-Port | 记录在 API 网关中配置过的 Path 参数以及实际取值。（可选，CLB 个性化配置） |
| X-Vip | CLB 负载均衡的 VIP 地址（可选，CLB 个性化配置） |
| X-Vport | CLB 负载均衡的 Vport（可选，CLB 个性化配置）  |
| X-Url | 请求 CLB 负载均衡的 PATH（可选，CLB 个性化配置） |
| X-Method |请求  CLB 负载均衡的 method（可选，CLB 个性化配置） |

>! 
> - 在 CLB 负载均衡迭代过程中，内容可能会增加更多。目前会保证数据结构内容仅增加，不删除，不对已有结构进行破坏。
> - 实际请求时的参数数据可能会在多个位置出现，可根据业务需求选择使用。

### 集成响应
集成响应，是指 CLB 负载均衡会将云函数的返回内容进行解析，并根据解析内容构造 HTTP 响应。通过使用集成响应，可以通过代码自主控制响应的状态码、headers、body 内容，可以实现自定义格式的内容响应，例如响应 XML、HTML、JSON 甚至 JS 内容。在使用集成响应时，需要按照 [CLB 负载均衡触发器的集成响应返回数据结构](#clbStructure)，才可以被成功解析，否则会出现  `{"errno":403,"error":"Analyse scf response failed."}` 错误信息。


#### CLB 触发器的集成响应返回数据结构[](id:clbStructure)
在 CLB 负载均衡设置为集成响应时，需要返回类似如下内容的数据结构。

```
{
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {"Content-Type":"text/html"},
    "body": "<html><body><h1>Heading</h1><p>Paragraph.</p></body></html>"
}
```
数据结构内容详细说明如下：

|    结构名    | 内容 |
| ---------- | --- |
| isBase64Encoded |  指明 body 内的内容是否为 Base64 编码后的二进制内容，取值需要为 JSON 格式的 true 或 false。 |
| statusCode | HTTP 返回的状态码，取值需要为 Integer 值。 |
| headers | HTTP 返回的头部内容，取值需要为多个 key-value 对象，或 `key:[value,value]` 对象。其中 key、value 均为字符串。 |
| body | HTTP 返回的 body 内容。 |

在需要返回 key 相同的多个 headers 时，可以使用字符串数组的方式描述不同 value，例如：
```
{
    "isBase64Encoded": false,
    "statusCode": 200,
    "headers": {"Content-Type":"text/html","Key":["value1","value2","value3"]},
    "body": "<html><body><h1>Heading</h1><p>Paragraph.</p></body></html>"
}
```

