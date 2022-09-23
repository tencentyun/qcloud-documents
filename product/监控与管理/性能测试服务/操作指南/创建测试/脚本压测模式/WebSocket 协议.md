
本介绍基于 WebSocket 协议的压测脚本的编写方法。

>?详细的 API 文档请参见 [PTS API](https://cloud.tencent.com/document/product/1484/75805)。

 

## 概述
- [WebSocket](https://baike.baidu.com/item/WebSocket/1953845?fr=aladdin) 是一种应用层通信协议，可在单个 TCP 连接上进行全双工通信。
- 不同于 HTTP 请求的客户端发起、服务端响应的一问一答模式，WebSocket 连接一旦建立，直到连接关闭之前，客户端、服务器之间都可源源不断地、双向地交换数据。因此，在压测场景中，基于 WebSocket 请求的脚本与基于 HTTP 请求的脚本，其结构和作用机制有所不同：
	- 执行 HTTP 脚本的每个 VU 会持续不断地迭代主函数（`export default function() { ... }`），直到压测结束。
	- 执行 WebSocket 脚本的每个 VU 不会持续迭代主函数，因为主函数会被建立连接的 `ws.connect` 方法阻塞，直到连接关闭。而在连接建立后的回调函数里（`function (socket) {...}`），会持续不断地监听和处理异步事件，直到压测结束。

## 脚本编写

PTS API 的 ws 模块提供了 WebSocket 协议的相关接口，请参见 [pts/ws API](https://cloud.tencent.com/document/product/1484/75829)。

**基本用法**
- 用 `ws.connect` 方法建立连接，并在其回调函数里定义您的业务逻辑：
  - `ws.connect` 的必传参数为 URL 和回调函数。
  - 若连接建立成功，PTS 会将创建好的 `ws.Socket` 对象传入回调函数。您可在回调函数里，定义您的 WebSocket 请求逻辑。
  - 执行完回调函数，`ws.connect` 会返回 `ws.Response` 对象。
- `ws.Socket` 对象的常用方法：
  - `send`：发送文本消息。
  - `close`：关闭连接。
  - `on`：监听事件，并用回调函数处理事件。当前 PTS 支持的事件列表如下：

|    事件名     |    事件用途    |
   | :-----------: | :------------: |
   |     open      |    建立连接    |
    |     close     |    关闭连接    |
    |     error     |    发生错误    |
    |    message    |  接收文本消息  |
    | binaryMessage | 接收二进制消息 |
    |     pong      | 接收 pong 消息 |
    |     ping      | 接收 ping 消息 |

    

**代码示例如下：**

```javascript
import ws from 'pts/ws';
import { check, sleep } from 'pts';
export default function () {
    const res = ws.connect("ws://localhost:8080/echo", function (socket) {
        socket.on('open', () => console.log('connected'));
        socket.on('message', (data) => console.log('Message received: ', data));
        socket.on('close', () => console.log('disconnected'));
        socket.send("message");
        socket.setTimeout(function () {
            console.log('3 seconds passed, closing the socket');
            socket.close();
        }, 3000);
        socket.setInterval(function () {
            socket.ping();
        }, 500);
        socket.setLoop(function () {
            sleep(0.1)
            socket.send("loop message")
        });
    });
    check("status is 101", () => res.status === 101);
}
```

## 文件依赖

在压测场景里，您可上传以下几种类型的文件，提供压测执行时的状态数据：

- 参数文件：以 csv 文件的形式，动态提供测试数据。场景被每个并发用户（VU）执行时，会获取参数文件里的每行数据，作为测试数据的值，供脚本里的变量引用。具体使用方法请参见 [使用参数文件](https://cloud.tencent.com/document/product/1484/74046)。
- 请求文件：构建您的请求所需的文件，如需要上传的文件。
