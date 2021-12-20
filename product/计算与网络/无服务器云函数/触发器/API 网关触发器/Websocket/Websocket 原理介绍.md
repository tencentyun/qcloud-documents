>?本文介绍**事件函数**支持 WebSocket 的解决方案，目前 **Web 函数**已经支持原生 WebSocket 协议，详情请参见 [WebSocket 协议支持](https://cloud.tencent.com/document/product/583/63406)。

## 实现原理

WebSocket 协议是基于 TCP 的一种新的网络协议。它实现了浏览器与服务器全双工（full-duplex）通信，即允许服务器主动发送信息给客户端。WebSocket 在服务端有数据推送需求时，可以主动发送数据至客户端。而原有 HTTP 协议的服务端对于需推送的数据，仅能通过轮询或 long poll 的方式来让客户端获得。

由于云函数是无状态且以触发式运行，即在有事件到来时才会被触发，因此，为了实现 WebSocket，云函数与 API 网关相结合，通过 API 网关承接及保持与客户端的连接。您可以认为 API 网关与 SCF 一起实现了服务端。当客户端有消息发出时，会先传递给 API 网关，再由 API 网关触发云函数执行。当服务端云函数要向客户端发送消息时，会先由云函数将消息 POST 到 API 网关的反向推送链接，再由 API 网关向客户端完成消息的推送。具体的实现架构如下：
![](https://main.qcloudimg.com/raw/d51ee070556d8f6bb3be308f651bcc4b.png)

对于 WebSocket 的整个生命周期，主要由以下几个事件组成：
- 连接建立：客户端向服务端请求建立连接并完成连接建立。
- 数据上行：客户端通过已经建立的连接向服务端发送数据。
- 数据下行：服务端通过已经建立的连接向客户端发送数据。
- 客户端断开：客户端要求断开已经建立的连接。
- 服务端断开：服务端要求断开已经建立的连接。

对于 WebSocket 整个生命周期的事件，云函数和 API 网关的处理过程如下：
- 连接建立：客户端与 API 网关建立 WebSocket 连接，API 网关将连接建立事件发送给 SCF。
- 数据上行：客户端通过 WebSocket 发送数据，API 网关将数据转发送给 SCF。
- 数据下行：SCF 通过向 API 网关指定的推送地址发送请求，API 网关收到后会将数据通过 WebSocket 发送给客户端。
- 客户端断开：客户端请求断开连接，API 网关将连接断开事件发送给 SCF。
- 服务端断开：SCF 通过向 API 网关指定的推送地址发送断开请求，API 网关收到后断开 WebSocket 连接。

因此，API 网关与 SCF 之间的交互，需要由3类云函数来承载：
- 注册函数：在客户端发起和 API 网关之间建立 WebSocket 连接时触发该函数，通知 SCF WebSocket 连接的 secConnectionID。通常会在该函数记录 secConnectionID 到持久存储中，用于后续数据的反向推送。
- 清理函数：在客户端主动发起 WebSocket 连接中断请求时触发该函数，通知 SCF 准备断开连接的 secConnectionID。通常会在该函数清理持久存储中记录的该 secConnectionID。
- 传输函数：在客户端通过 WebSocket 连接发送数据时触发该函数，告知 SCF 连接的 secConnectionID 以及发送的数据。通常会在该函数处理业务数据。例如，是否将数据推送给持久存储中的其他 secConnectionID。

>! 当您需要主动给某个 secConnectionID 推送数据或主动断开某个 secConnectionID 时，均需要用到 API 网关的反向推送地址。

## 数据结构

### 连接建立

1. 当客户端发起 WebSocket 建立连接的请求时，API 网关会将约定好的 JSON 数据结构封装在 Body 中，并以 HTTP POST 方法发送给注册函数。您可以从函数的 event 中获取，请求的 Body 示例如下：
<dx-codeblock>
:::  json
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
:::
</dx-codeblock>
数据结构内容详细说明如下：
<table>
<tr><th>结构名</th><th>内容</th></tr>
<tr>
 <td>requestContext</td>
 <td>请求来源的 API 网关的配置信息、请求标识、认证信息、来源信息。其中包括：
  <ul>
   <li>serviceName，path，httpMethod：指向 API 网关的服务、API 的路径和方法。</li>
	 <li>stage：指向请求来源 API 所在的环境。</li>
	 <li>requestId：标识当前这次请求的唯一 ID。</li>
	 <li>identity：标识用户的认证方法和认证的信息。</li>
	 <li>sourceIp：标识请求来源 IP。</li>
  </ul>
 </td>
</tr>
<tr>
 <td>websocket</td>
 <td>建立连接的详细信息。其中包括：
   <ul>
   <li>action：指本次请求的动作。</li>
	 <li>secConnectionID：字符串，即标识 WebSocket 连接的 ID。原始长度为128Bit，是经过 base64 编码后的字符串，共32个字符。</li>
	 <li>secWebSocketProtocol：字符串，可选字段。</br>代表子协议列表。如果原始请求有该字段内容将传给云函数，否则该字段不出现。</li>
	 <li>secWebSocketExtensions：字符串，可选字段。</br>代表扩展列表。如果原始请求有该字段内容将传给云函数，否则该字段不出现。</li>
  </ul>
 </td>
</tr>
</table>

>! 在 API 网关迭代过程中，requestContext 中的内容可能会大量增加。目前只保证数据结构内容仅增加，不删除，且不对已有结构进行破坏。

2. 当注册函数收到连接建立的请求后，需要在函数处理结束时，将是否同意建立连接的响应消息返回至 API 网关中。响应  Body 要求为 JSON 格式，其示例如下：
<dx-codeblock>
:::  json
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
:::
</dx-codeblock>
数据结构内容详细说明如下：
<table>
<tr><th>结构名</th><th>内容</th></tr>
<tr>
 <td>errNo</td>
 <td>整型，必选项。</br>
 响应错误码。errNo 为0时，表示握手成功，同意连接建立。</td>
</tr>
<tr>
 <td>errMsg</td>
 <td>字符串，必选项。</br>
 错误原因。errNo 为非0时，表示生效。</td>
</tr>
<tr>
 <td>websocket</td>
 <td>连接建立的详细信息。其中：
  <ul>
	 <li>action：指本次请求的动作。</li>
	 <li>secConnectionID：字符串，是标识 WebSocket 连接的 ID，原始长度为128Bit，是经过 base64 编码后的字符串，共32个字符。</li>
	 <li>secWebSocketProtocol：字符串，可选字段。</br>为单个子协议的值。如果原始请求有该字段内容，API 网关会透传到客户端。</li>
	 <li>secWebSocketExtensions：字符串，可选字段。</br>为单个扩展的值。如果原始请求有该字段内容，API 网关会透传到客户端。</li>
	</ul>
 </td>
</tr>
</table>

 >! 
 > - SCF 请求超时默认认为连接建立失败。
 > - 当 API 网关收到云函数的响应消息后，优先判断 HTTP 响应码。如果响应码为200，则解析响应 Body。如果响应码为非200，则认为 SCF 出现故障，拒绝建立连接。

### 数据传输

#### 上行数据传输

##### 传输请求

当客户端通过 WebSocket 发送数据时，API 网关会把约定好的 JSON 数据结构封装在 Body 中，并以 HTTP POST 方法发送给传输函数。您可以从函数的 event 中获取，请求的 Body 示例如下：
```
{
  "websocket":{
    "action":"data send",
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa==",
    "dataType":"text", 
    "data":"xxx"
  }
}
```
数据结构内容详细说明如下：
<table>
<tr><th>参数</th><th>内容</th></tr>
<tr><td>websocket</td><td>数据传输的详细信息。</td></tr>
<tr><td>action</td><td>本次请求的动作，本文以 “data send” 为例。</td></tr>
<tr><td>secConnectionID</td><td>字符串，是标识 WebSocket 连接的 ID。原始长度为128Bit，是经过 base64 编码后的字符串，共32个字符</td></tr>
<tr><td>dataType</td><td>传输数据的类型。<ul><li>“binary”：表示二进制。</li><li>“text”：表示文本。</li></ul></td></tr>
<tr><td>data</td><td>传输的数据。如果 “dataType” 是 “binary”，则为 base64 编码后的二进制流；如果 “dataType” 是 “text”，则为字符串。</td></tr>
<table>

##### 传输响应

在传输函数运行结束后，会向 API 网关返回 HTTP 响应，API 网关会根据响应码做出相应的动作：
- 如果响应码为200，表示函数运行成功。
- 如果响应码为非200，表示系统故障，API 网关会主动给客户端发 FIN 包。

>! API 网关不会处理响应 Body 中的内容。

[](id:DownlinkDataCallback)
#### 下行数据回调

##### 回调请求

当云函数需要向客户端推送数据或主动断开连接时，可以发起 Request 请求，把数据封装在 Body 中，以 POST 方法发送给 API 网关的反向推向地址。请求 Body 要求为 JSON 格式，其示例如下：
```
{
  "websocket":{
    "action":"data send", //向客户端发送数据
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa==",
    "dataType":"text",
    "data":"xxx"
  }
}
```
```
{
  "websocket":{
    "action":"closing", //发送断开连接请求
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa=="
  }
}
```
数据结构内容详细说明如下：

|    字段    | 内容 |
| ---------- | --- |
| websocket | 数据传输的详细信息。 |
|action | 本次请求的动作，支持内容为 “data send”、“closing” 两种：<ul><li>“data send”：为向客户端发送数据。</li><li>“closing”：为向客户端发起连接断开请求，可以不包含 "dataType" 和 "data" 内容。</li></ul> |
|secConnectionID| 字符串，是标识 websocket 连接的 ID，原始长度为 128bit，是经过 base64 编码后的字符串，共32个字符。|
|dataType | 传输数据的类型，一共两种：<ul><li>“binary”：表示二进制。</li> <li>“text”：表示文本。</li></ul> |
|data | 传输的数据：<ul><li>如果 “dataType” 是 “binary”，则为 base64 编码后的二进制流。</li> <li>如果 “dataType” 是 “text”，则为字符串。</li></ul> |

##### 回调响应

在回调结束后，可根据 API 网关的响应码判断回调的结果：
- 如果响应码为200，表示回调成功。
- 如果响应码为非200，表示系统故障，此时 API 网关会主动向客户端发 FIN 包。

同时，在响应结果中可以拿到为 JSON 格式的响应 Body，示例如下：
```
{
   "errNo":0, 
   "errMsg":"ok"
}
```
数据结构内容详细说明如下：

|    字段    | 内容 |
| ---------- | --- |
| errNo | 整数，响应错误码。如果为0表示成功。 |
| errMsg | 字符串，错误原因。 |


### 连接清理

#### 客户端主动断开连接

##### 注销请求

当客户端主动发起 WebSocket 建立断开的请求时，API 网关会把约定好的 JSON 数据结构封装在 Body 中，并以 HTTP POST 方法发送给清理函数。您可以从函数的 event 中获取，请求的 Body 示例如下：
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
| websocket | 连接断开的详细信息。 |
| action | 本次请求的动作，此处为 "closing"。 |
| secConnectionID | 字符串。</br>是标识 WebSocket 连接的 ID。原始长度为128Bit，是经过 base64 编码后的字符串，共32个字符。|
>! 在清理函数中，您可以从 event 中获取 secConnectionID，并在永久存储（如数据库）中删除该 ID。

##### 注销响应

在清理函数运行结束后，会向 API 网关返回 HTTP 响应，API 网关会根据响应码做出相应的动作：
- 如果响应码为200，表示函数运行成功。
- 如果响应码为非200，表示系统故障。

>! API 网关不会处理响应 Body 中的内容。

#### 服务端主动断开连接

参考 **[下行数据回调](#DownlinkDataCallback)**，在函数中发起 Request 请求，将以下数据结构封装在 Body 中，并以 POST 方法发送给 API 网关的反向推向地址。
```
{
  "websocket":{
    "action":"closing", //发送断开连接请求
    "secConnectionID":"xawexasdfewezdfsdfeasdfffa=="
  }
}
```
>! 当主动断开客户端的链接时，您需要先获取客户端 WebSocket 的 secConnectionID，并将其填写在数据结构中；再在永久存储（如数据库）中删除该 ID。



