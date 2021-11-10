
腾讯云图支持 Pull & Push 两种方式动态更新大屏。
- Pull 的方式有：
 - CSV
 - API
 - 数据库
 - 腾讯云监控
- Push 的方式有：
 - WebSocket

Push 的方式是实时的，如果您需要实时更新大屏，可以选择将数据源设置为 WebSocket。下面将介绍 WebSocket 的使用。

## 快速搭建 WebSocket 服务端
以 NodeJs 举例，使用到了 ws 这个 WebSocket 库，同时配合 HTTP 框架 express 进行使用。使用 NodeJs 运行以下代码，便启动了一个 WebSocket。访问地址是：`ws://127.0.0.1:3000`，代码如下：
```
const http = require('http')
const WebSocket = require('ws')
const express = require('express')
const app = express()
const server = http.createServer(app)
const wss = new WebSocket.Server({
  server
})
wss.on('connection', (ws) => {
  console.log('client connected')
})
server.listen(3000)
```

## 使用 WebSocket 更新大屏图表
在大屏中添加一个柱状图，然后选择数据源为 **WebSocket**，设置 WebSocket 的 URL 地址。
![](https://main.qcloudimg.com/raw/91f7c98fe4cb424a8fa7c4d4be3b317a.png)
单击**数据示例**，即可看到 WebSocket 服务器刷新此图标组件的消息格式。
![](https://main.qcloudimg.com/raw/d8a92bf1389263126b041cf23ceb77d6.png)
格式示例如下：
![](https://main.qcloudimg.com/raw/95bea557d0ddf1c134c6a42e52461d11.png)
复制并修改“WebSocket 发送数据格式示例”中的内容，然后使用示例中的代码实现一个消息发送接口。当浏览器访问`http://127.0.0.1:3000/refresh-chart`时，将会向 WebSocket 客户端发送数据刷新组件。

```
const BAR_DATA_MAX = 120
function randomNumber(max) {
  return parseInt(Math.random() * max, 10)
}
// 实现接口 http://127.0.0.1:3000/refresh-chart
// 访问这个接口，将会向 WebSocket 客户端发送刷新组件的消息
app.get('/refresh-chart', (req, res, next) => {
  wss.clients.forEach(ws => {
    ws.send(JSON.stringify({
      version: 1,
      action: 'UpdateComponentData',
      // body 是数组，这里可以传入多个图表组件的数据
      body: [
        {
          id: 'ChartColumnBasic_1_0_0_2_1583478813519',
          data: [
            {
              x: '一月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '二月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '三月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '四月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '五月',
              y: randomNumber(BAR_DATA_MAX)
            }
          ]
        }
      ]
    }))
  })
  res.json({
    code: 0,
    msg: 'ok'
  })
})
```
浏览器每访问一次`http://127.0.0.1:3000/refresh-chart`便会实时刷新柱状图。因为消息中的 body 是数组，因此可以同时发送多个图表组件的数据，刷新多个图表组件。
>!大屏中只用设置一个图表组件的 WebSocket 数据源，便可以控制大屏中所有的图表组件。图表组件的 ID 可以右键编辑界面中的图表组件，单击菜单中的**复制 ID** 获取。

## 使用 WebSocket 控制联动
WebSocket 也可以用来控制联动，只需要发送更新全局变量的消息。
![](https://main.qcloudimg.com/raw/f8369158229bee0732a45a93071c2630.png)
如上图，这里需要更改全局变量 tabValue 的值为 tab2，向客户端发送以下消息即可（同样，这里可以传入多个字段）：
```
{
  "version": 1,
  "action": "UpdateGlobalField",
  "body": {
    "tabValue": "tab2"
  }
}
```

## WebSocket 服务端实现访问密钥鉴权
WebSocket 服务端搭建完成后，此时，服务是暴露在公网的，可能被任何人连接。云图提供了访问密钥功能，在 WebSocket 连接建立后会发送带签名的 Connect 消息。

如果在一定时间之内没有收到 Connect 消息或收到 Connect 消息的签名不正确，即认为连接的客户端不合法。

以下面的 SecretId、SecretKey 为例：
- SecretId：zUYUtjPu2Kob9jarBhTGxrbxxxxxxxxxxxxxx
- SecretKey：xrck1Mgi0IxVjS08B3xxxxxxxxxxxxxx

当访问大屏，大屏连接服务端成功后，服务端将收到带签名的 Connect 消息：
```
{
  "version": 1,
  "from": "tcv-editor",
  "timestamp": 1583487814678,
  "clientId": "980b05e0-ca11-4536-91dd-3795c5b11b88",
  "action": "Connect",
  "body": {
    "TcvSignature": "vIwmPQ3yUD8WsXKOA/ABq1jl/iyHVyZnVoWF561hjVU=",
    "TcvSecretId": "zUYUtjPu2Kob9jarBhTGxrbxxxxxxxxxxxxxx",
    "TcvTimestamp": 1583487814,
    "TcvNonce": 357963
  }
}
```
服务端使用记录下来的 secretKey 与传入的参数计算签名，将计算结果与接收到的签名做对比，判断是否相同，相同则为合法。NodeJs 计算签名方法：
```
function isSignatureOK(body) {
  const secretKey = 'xrck1Mgi0IxVjS08B3xxxxxxxxxxxxxx'
  const receivedSignature = body.TcvSignature
  // TcvSignature 不参与签名
  delete body.TcvSignature
  const params = Object.entries(body)
  // 升序排列字段
  params.sort(([key1], [key2]) => {
    if (key1 > key2) {
      return 1
    }
    if (key1 < key2) {
      return -1
    }
    return 0
  })
  // 生成签名字符串
  const signStr = params.map(kv => kv.join('=')).join('&')
  console.log(signStr)
  // 计算签名
  const signature = crypto.createHmac('sha256', secretKey).update(signStr).digest().toString('base64')
  console.log(`signature=${signature}, receivedSignature=${receivedSignature}`)
  // 比较签名结果是否相同
  return signature === receivedSignature
}
```

## WebSocket 服务端实现心跳保活
当大屏 WebSocket 客户端和服务端连接后，客户端和服务端的连接稳定性面临很多问题：
- 无线网络信号突然变差
- 网络发生切换
- 路由器断网
- 网线断了

而服务端和客户端都不知道连接变慢或已经的断开状态。此时可勾选**需要心跳包**。
![](https://main.qcloudimg.com/raw/5cdc265c3a74435e9b72a943ca518480.png)
当大屏客户端没有收到服务器的消息时，将每隔设定时间发起 Ping 消息，服务端收到后需要响应 Pong 消息以完成心跳检测。

如果大屏客户端在发送 Ping 消息10秒后没有收到服务回应的 Pong 消息，便认为网络不通，将尝试进行重连。

Ping 消息：
```
{
  "version": 1,
  "from": "tcv-editor",
  "timestamp": 1583490098004,
  "clientId": "5ca85aad-102a-4468-95fe-e608b5b46b36",
  "action": "Ping"
}
```
Pong 消息：
```
{
  "version": 1,
  "action": "Pong"
}
```
服务端添加定时器，如果超过31秒（上图心跳包 Ping 间隔时间）+ 10秒（Ping 消息在网络上传递的最大时间）的时间没有收到消息，则认为客户端已经断开连接，将主动断开该客户端的连接。

## 完整服务端代码示例
NodeJs 完整示例代码（支持 node 8 及以上版本运行）：
```
const http = require('http')
const WebSocket = require('ws')
const express = require('express')
const crypto = require('crypto')
const BAR_DATA_MAX = 120
function randomNumber(max) {
  return parseInt(Math.random() * max, 10)
}
function isSignatureOK(body) {
  const secretKey = 'xrck1Mgi0IxVjS08B3xxxxxxxxxxxxxx'
  const receivedSignature = body.TcvSignature
  // TcvSignature 不参与签名
  delete body.TcvSignature
  const params = Object.entries(body)
  // 升序排列字段
  params.sort(([key1], [key2]) => {
    if (key1 > key2) {
      return 1
    }
    if (key1 < key2) {
      return -1
    }
    return 0
  })
  // 生成签名字符串
  const signStr = params.map(kv => kv.join('=')).join('&')
  console.log(signStr)
  // 计算签名
  const signature = crypto.createHmac('sha256', secretKey).update(signStr).digest().toString('base64')
  console.log(`signature=${signature}, receivedSignature=${receivedSignature}`)
  // 比较签名结果是否相同
  return signature === receivedSignature
}
const app = express()
const server = http.createServer(app)
const wss = new WebSocket.Server({
  server
})
wss.on('connection', (ws) => {
  console.log('client connected')
  let heartbeatTimer
  const heartbeat = () => {
    clearTimeout(heartbeatTimer)
    heartbeatTimer = setTimeout(() => {
      ws.terminate()
    }, (31 + 10) * 1000)
  }
  // 连接一建立则设置心跳检测
  heartbeat()
  // 10秒内没有收到 Connect 消息，强制关闭连接
  const connectTimer = setTimeout(() => {
    if (!ws.receivedConnectMsg) {
      ws.terminate()
    }
  }, 10 * 1000)
  ws.on('message', (msg) => {
    console.log('received msg', msg)
    // 收到消息，则更新心跳计时器，因为如果没有消息，将会在设定时间内收到心跳包
    heartbeat()
    const data = JSON.parse(msg)
    // 在没有收到 Connect 消息之前，丢弃任何消息
    if (!ws.receivedConnectMsg & data.action !== 'Connect') {
      return
    }
    // 处理来自客户端的消息
    switch (data.action) {
      case 'Connect': {
        ws.receivedConnectMsg = true
        clearTimeout(connectTimer)
        // 签名校验失败，断开连接
        if (!isSignatureOK(data.body)) {
          ws.terminate()
        }
        break
      }
      // 来自客户端的心跳包 Ping 消息，回应 Pong 消息
      case 'Ping': {
        ws.send(JSON.stringify({
          version: 1,
          action: 'Pong'
        }))
        break
      }
      default:
        break
    }
  })
})
// 更新大屏联动变量
app.get('/change-tab', (req, res, next) => {
  wss.clients.forEach(ws => {
    ws.send(JSON.stringify({
      version: 1,
      action: 'UpdateGlobalField',
      body: {
        tabValue: 'tab2'
      }
    }))
  })
  res.json({
    code: 0,
    msg: 'ok'
  })
})
// 更新大屏图表
app.get('/refresh-chart', (req, res, next) => {
  wss.clients.forEach(ws => {
    ws.send(JSON.stringify({
      version: 1,
      action: 'UpdateComponentData',
      body: [
        {
          id: 'component/ChartColumnBasic_1_0_0_2_1583478813519',
          data: [
            {
              x: '一月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '二月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '三月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '四月',
              y: randomNumber(BAR_DATA_MAX)
            },
            {
              x: '五月',
              y: randomNumber(BAR_DATA_MAX)
            }
          ]
        }
      ]
    }))
  })
  res.json({
    code: 0,
    msg: 'ok'
  })
})
server.listen(3000)
```



