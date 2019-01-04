## 实现原理

WebSocket 协议是基于TCP的一种新的网络协议。它实现了浏览器与服务器全双工(full-duplex)通信,即允许服务器主动发送信息给客户端。区别于 http，websocket 在服务端有数据推送需求时，一样可以主动发送数据至客户端。而原有 http 协议，服务端由于是被动处理，对于需推送的数据，仅能通过轮询或 long poll 的方式来让客户端获得。

由于云函数是无状态的，且以触发的式运行，即在有事件到来时才会被触发。因此，为了实现 websocket，云函数与 API 网关相结合，通过 API 网关来承接及保持与客户端的连接，可以认为 API 网关与 SCF 一起实现了 Server 端。当客户端有消息发出时，会先传递给 API 网关，再由 API 网关触发云函数执行。当后端云函数要向客户端发送消息时，会先由云函数把消息 post 到 API 网关的反向推送链接，然后由 API 网关向客户端完成消息的推送。具体的实现架构如下：
![](https://main.qcloudimg.com/raw/d51ee070556d8f6bb3be308f651bcc4b.png)

对于 websocket 的整个生命周期，我们可以认为有如下几个事件组成:
- 连接建立：Client 端向 Server 端请求建立连接并完成连接建立
- 数据上行：Client 端通过已经建立的连接向 Server 端发送数据
- 数据下行：Server 端通过已经建立的连接向 Client 端发送数据
- 客户端断开：Client 端要求断开已经建立的连接
- 服务端断开：Server 端要求断开已经建立的连接

对于 websocket 整个生命周期的事件，云函数和 API 网关的处理过程如下：
- 连接建立：Client 端与 API 网关建立 websocket 连接，API 网关把连接建立事件发送给 SCF
- 数据上行：Client 端通过 websocket 发送数据，API 网关将数据转发送给 SCF
- 数据下行：SCF 通过向 API 网关指定的推送地址发送请求，API 网关收到后会把数据通过 websocket 发送给 Client 端
- 客户端断开：Client 端请求断开连接，API 网关把连接断开事件发送给 SCF
- 服务端断开：SCF 通过向 API 网关指定的推送地址发送断开请求，API 网关收到后断开 websocket 连接

因此，API 网关与 SCF 之间的交互，需要由 3 类云函数来承载：
- 注册函数：在 Client 端发起和 API 网关之间建立 websocket 连接时触发该函数，通知 SCF websocket 连接的 secConnectionID。通常会在该函数中记录 secConnectionID 到持久存储中，用于后续数据的反向推送。
- 清理函数：在 Client 端主动发起 websocket 连接中断请求时触发该函数，通知 SCF 准备断开连接的 secConnectionID。通常会在该函数中清理持久存储中记录的该 secConnectionID。
- 传输函数：在 Client 端通过 websocket 连接发送数据时触发该函数，告知 SCF 连接的 secConnectionID 以及发送的数据。通常会在该函数中处理业务数据，如是否把数据推送给持久存储中的其他 secConnectionID。
> **注意：**
> 当需要主动给某个 secConnectionID 推送数据或主动断开某个 secConnectionID 时，均需要用到 API 网关的反向推送地址。



## 数据结构

### 连接建立

1. 当 Client 端发起 websocket 建立连接的请求时，API 网关会把约定好的 json 数据结构封装在 Body 中并以 HTTP POST 方法发送给注册函数，可以从函数的 event 中获取。请求的 Body 样例如下:
```
{
  "requestContext": {
    "serviceName": "testsvc",
    "path": "/test/{testvar}",
    "httpMethod": "GET",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "identity": {
      "secretId": "abdcdxxxxxxxsdfs"
    },
    "sourceIp": "10.0.2.14",
    "stage": "prod",
    "websocketEnable":true
  },
  "websocket":{
    "action":"connecting",
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa==",
    "secWebSocketProtocol":"chat,binary",
    "secWebSocketExtensions":"extension1,extension2"
  }
}
```
数据结构内容详细说明如下：

|    结构名    | 内容 |
| ---------- | --- |
| requestContext |  请求来源的 API 网关的配置信息、请求标识、认证信息、来源信息。其中：<li>serviceName，path，httpMethod 指向 API 网关的服务、API 的路径和方法；<li>stage 指向请求来源 API 所在的环境；<li>requestId 标识当前这次请求的唯一 ID；<li>identity 标识用户的认证方法和认证的信息；<li>sourceIp 标识请求来源 IP。 |
| websocket | 建立连接的详细信息。其中：<li>action 指本次请求的动作；<li>secConnectionID 字符串，是标识 websocket 连接的 ID，原始长度为 128bit,此处是经过 base64 编码后的字符串，共 32 个字符;<li>secWebSocketProtocol 字符串，代表子协议列表。可选字段，如果原始请求有该字段内容则传过来，否则该字段不出现;<li>secWebSocketExtensions 字符串，扩展列表。可选字段，如果原始请求有该字段内容则传过来，否则该字段不出现。|

> **注意：**
> 在 API 网关迭代过程中， requestContext 内的内容可能会增加更多。目前会保证数据结构内容仅增加，不删除，不对已有结构进行破坏。


2. 当注册函数收到连接建立的请求后，需要在函数处理结束时，给 API 网关返回是否同意建立连接的响应消息。响应 Body 也要求为 json 格式,样例如下：
```
{
   "errNo":0, 
   "errMsg":"ok",
   "websocket":{
     "action":"connecting",
     "secConnectionID":"xawexasdfewezdfsdfeasdfffa==",
     "secWebSocketProtocol":"chat,binary",
     "secWebSocketExtensions":"extension1,extension2"
  }
}
```
数据结构内容详细说明如下：

|    结构名    | 内容 |
| ---------- | --- |
| errNo | 响应错误码，整型。必选。如果为 0 表示正常握手成功，同意连接建立 |
| errMsg | 错误原因，字符串。必选。errNo 为非 0 时生效 |
| websocket | 连接建立的详细信息。其中：<li>action 指本次请求的动作；<li>secConnectionID 字符串，是标识 websocket 连接的 ID，原始长度为 128bit,此处是经过 base64 编码后的字符串，共 32 个字符;<li>secWebSocketProtocol 字符串，为单个子协议的值。可选字段，如果有，API 网关会透传到 Client 端;<li>secWebSocketExtensions 字符串，为单个扩展的值。可选字段，如果有，API 网关会透传到 Client 端。|

> **注意：**
>- SCF 请求超时认为连接建立失败。
>- 当 API 网关收到云函数的响应消息后，首先会判断 http 响应码。如果响应码为非200，则认为scf出现故障，拒绝建立连接。如果响应码为200，则解析响应 Body。

### 数据传输
#### 1. 上行数据传输
1.1 传输请求
当 Client 端通过 websocket 发送数据时，API 网关会把约定好的 json 数据结构封装在 Body 中并以 HTTP POST 方法发送给传输函数，可以从函数的 event 中获取。请求的 Body 样例如下:
```
{
  "websocket":{
    "action":"data recv",
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa==",
    "dataType":"text", 
    "data":"xxx"
  }
}
```
数据结构内容详细说明如下：

|    字段    | 内容 |
| ---------- | --- |
| websocket | 数据传输的详细信息 |
|action | 本次请求的动作，此处为 "data recv" |
|secConnectionID| 字符串，是标识 websocket 连接的 ID，原始长度为 128bit,此处是经过 base64 编码后的字符串，共 32 个字符|
|dataType | 传输数据的类型，一共两种："binary" 表示二进制，"text" 表示文本 |
|data | 传输的数据，如果 "dataType" 是 "binary"，则为 base64 编码后的二进制流；如果 "dataType" 是 "text"，则为字符串|

1.2 传输响应
在传输函数运行结束后，会向 API 网关返回 HTTP 响应，API 网关会根据响应码做出相应的动作：
- 如果响应码为 200，表示函数运行成功;
- 如果响应码为非 200，表示系统故障, API 网关会主动给客户端发 FIN 包。
> **注意：**
> API 网关不会处理响应 Body 中的内容。

#### 2. 下行数据回调
2.1 回调请求
当云函数需要向 Client 端推送数据或主动断开连接时，可以发起 request 请求，把数据封装在 Body 中，以 POST 方法发送给 API 网关的反向推向地址，请求 Body 要求为 json 格式。请求body样例:
```
{
  "websocket":{
    "action":"data send",//向客户端发送数据
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa==",
    "dataType":"text",
    "data":"xxx"
  }
}
```
```
{
  "websocket":{
    "action":"closing",//发送断开连接请求
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa=="
  }
}
```
数据结构内容详细说明如下：

|    字段    | 内容 |
| ---------- | --- |
| websocket | 数据传输的详细信息 |
|action | 本次请求的动作，支持内容为"data send"、"closing"两种：<li>"data send"为向客户端发送数据<li>"closing"为向客户端发起连接断开请求，可以不包含"dataType"和"data"内容 |
|secConnectionID| 字符串，是标识 websocket 连接的 ID，原始长度为 128bit,此处是经过 base64 编码后的字符串，共 32 个字符|
|dataType | 传输数据的类型，一共两种：<li>"binary" 表示二进制 <li>"text" 表示文本 |
|data | 传输的数据:<li>如果 "dataType" 是 "binary"，则为 base64 编码后的二进制流 <li>如果 "dataType" 是 "text"，则为字符串|

2.2 回调响应
在回调结束后，可根据 API 网关的响应码判断回调的结果：
- 如果响应码为 200，表示回调成功;
- 如果响应码为非 200，表示系统故障, 此时 API 网关会主动向客户端发 FIN 包。

同时，在响应结果中可以拿到响应 Body，为 json 格式，示例如下：
```
{
   "errNo":0, 
   "errMsg":"ok"
}
```
数据结构内容详细说明如下：

|    字段    | 内容 |
| ---------- | --- |
| errNo | 响应错误码，整数，如果为0表示成功 |
| errMsg | 错误原因，字符串 |


### 连接清理

#### 1.Client 端主动断开连接
1.1 注销请求
当 Client 端主动发起 websocket 建立断开的请求时，API 网关会把约定好的 json 数据结构封装在 Body 中并以 HTTP POST 方法发送给清理函数，可以从函数的 event 中获取。请求的 Body 样例如下:
```
{
  "websocket":{
    "action":"closing",
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa=="
  }
}
```
数据结构内容详细说明如下：

|    字段    | 内容 |
| ---------- | --- |
| websocket | 连接断开的详细信息 |
| action | 本次请求的动作，此处为 "closing" |
| secConnectionID | 字符串，是标识 websocket 连接的 ID，原始长度为 128bit,此处是经过 base64 编码后的字符串，共 32 个字符|
> **注意：**
> 在清理函数中，可以从 event 中获取 secConnectionID，并在永久存储（如数据库）中删除该 ID。

1.2 注销响应
在清理函数运行结束后，会向 API 网关返回 HTTP 响应，API 网关会根据响应码做出相应的动作：
- 如果响应码为 200，表示函数运行成功;
- 如果响应码为非 200，表示系统故障。
> **注意：**
> API 网关不会处理响应 Body 中的内容。

#### 2.Server 端主动断开连接
参考【下行数据回调】小节，在函数中发起 request 请求，把如下数据结构封装在 Body 中，以 POST 方法发送给 API 网关的反向推向地址。
```
{
  "websocket":{
    "action":"closing",//发送断开连接请求
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa=="
  }
}
```
> **注意：**
> 当主动断开 Client 端的链接时，需要获取 Client 端 websocket 的 secConnectionID，填写到数据结构中，并在永久存储（如数据库）中删除该 ID。
