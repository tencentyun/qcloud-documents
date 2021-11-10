Web 函数目前已经支持通过原生 WebSocket 协议在客户端和函数运行的服务端间建立连接。

## 工作原理

### 服务启动
可以通过在配置支持 WebSocket 协议的 Web 函数的运行环境中，使用启动文件启动 WebSocket 服务器，并在 **指定端口（9000）** 上进行监听，等待客户端连接。

同时，API 网关触发器需要设定为前端协议为 “WS 或 WSS” 支持，后端为当前指定支持 WebSocket 的 Web 函数。 通过 API 网关提供的 ws 路径，可供客户端连接使用。

### 建立 WebSocket 连接

WebSocket 客户端通过使用 API 网关触发器提供的 WS 连接，发起 WebSocket 连接。 API 网关及云函数平台将透传连接至运行环境中的服务进程上。建立连接的协商及通讯过程，均由服务端代码处理。

连接建立后，客户端及服务端按 WebSocket 协议进行正常通讯。


### WebSocket 连接生命周期

在 Web 函数的 WebSocket 支持下， WebSocket 一次连接的生命周期，等同于一次函数调用请求。WS 连接建立过程等同于请求发起阶段，WS 连接断开等同于请求结束。

同时，函数实例与连接一一对应，即同一实例在某一时刻仅处理一个 WS 连接。在有更多客户端的连接请求发起时，将启动对应数量的实例进行处理。
- 当 WS 连接请求时，函数实例启动，并接受连接建立的请求。
- 当 WS 连接建立后，实例持续运行，根据实际业务情况来接受处理客户端的上行数据，或服务端主动推送下行数据。
- 当 WS 连接中断后，实例停止运行。


#### 连接断开

在如下情况中，WS 连接会中断，且由于请求生命周期与连接生命周期相同，也会使得当次请求运行周期结束：

|断开情况|函数表现|函数状态码|
|----------|-----------|-----------|
|客户端或服务端发起连接结束、关闭连接操作，结束状态码为1000、1010（客户端发送）、1011（服务端发送）|函数正常执行结束，运行状态为成功|200|
|客户端或服务端发起连接结束、关闭连接操作，结束状态码非1000、1010、1011|函数异常结束，运行状态为失败|439（服务端关闭）、456（客户端关闭）|
|在 WS 连接上无消息上行或下行发送，达到配置的空闲超时时间的情况下，连接被函数平台断开|函数异常结束，运行状态为失败|455|
|在连接建立后持续使用，函数运行时间达到最大运行时长，连接被函数平台断开|函数异常结束，运行状态失败|433|

- WebSocket 协议的结束码详情可见 [WebSocket Status Codes](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4)。
- 更详细的函数状态码可见 [云函数状态码列表](https://cloud.tencent.com/document/product/583/42611)。

## 使用限制

使用 WebSocket 时有如下限制：

- 空闲超时时间设置：1 - 600秒
- 单次数据包最大体积：1MB


## 操作步骤

### 创建函数

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)。
2. 单击**新建**创建云函数，可以通过选择**自定义创建** > **选择 Web 函数** > **高级配置**来看到协议支持选项。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/02caa24cddfa1b16c95a7ee8255c4586.png)
3. 通过勾选 WebSocket 支持，配置好 WebSocket 空闲超时时间，来完成 WebSocket协议支持。如下图所示：
![](https://main.qcloudimg.com/raw/5e72c2cd51f6a31a0c9f746e8bba8fc3.png)
4. 同时在勾选 WebSocket 支持后，API 网关的协议支持同样将自动切换为 WS&WSS 支持，创建的 API 网关所提供的链接地址，也将是 Websocket 地址。如下图所示：
![](https://main.qcloudimg.com/raw/dd02d4e09577f26eaabbc33cfea4e97d.png)
>?在完成创建后，WebSocket 的协议支持不可取消，但可以根据需求修改空闲超时时间配置。


### 示例代码

目前可以通过如下的 Demo 代码来创建函数，体验 WebSocket 效果：

- [Python 示例](https://github.com/awesome-scf/scf-python-code-snippet/tree/main/ws_python)：使用 [websockets 库](https://github.com/aaugustin/websockets) 实现 WebSocket 服务端。
- [Nodejs 示例](https://github.com/awesome-scf/scf-nodejs-code-snippet/tree/main/ws_node)：使用 [ws 库](https://github.com/websockets/ws) 实现 WebSocket 服务端。
