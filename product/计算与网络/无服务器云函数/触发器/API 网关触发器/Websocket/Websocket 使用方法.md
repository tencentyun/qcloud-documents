>?本文介绍**事件函数**支持 WebSocket 的解决方案，目前 **Web 函数**已经支持原生 WebSocket 协议，详情请参见 [WebSocket 协议支持](https://cloud.tencent.com/document/product/583/63406)。

在 [原理介绍](https://cloud.tencent.com/document/product/583/32553) 章节中，提到需要3类云函数来承载与 API 网关之间的交互：
- 注册函数：在客户端发起和 API 网关之间建立 WebSocket 连接时触发该函数，通知 SCF WebSocket 连接的 secConnectionID。通常会在该函数记录 secConnectionID 到持久存储中，用于后续数据的反向推送。
- 清理函数：在客户端主动发起 WebSocket 连接中断请求时触发该函数，通知 SCF 准备断开连接的 secConnectionID。通常会在该函数清理持久存储中记录的该 secConnectionID。
- 传输函数：在客户端通过 WebSocket 连接发送数据时触发该函数，告知 SCF 连接的 secConnectionID 以及发送的数据。通常会在该函数处理业务数据。例如，是否将数据推送给持久存储中的其他 secConnectionID。

>! 当您需要主动给某个 secConnectionID 推送数据或主动断开某个 secConnectionID 时，均需要用到 API 网关的反向推送地址。

本文档以 Python2.7 为例，介绍各类函数 main_handler 的写法。

## 函数代码示例

### 注册函数
```
# -*- coding: utf8 -*-
import json
import requests
def main_handler(event, context):
    print('Start Register function')
    print("event is %s"%event)
    retmsg = {}
    global connectionID
    if 'requestContext' not in event.keys():
        return {"errNo":101, "errMsg":"not found request context"}
    if 'websocket' not in event.keys():
        return {"errNo":102, "errMsg":"not found websocket"}
    connectionID = event['websocket']['secConnectionID']
    retmsg['errNo'] = 0
    retmsg['errMsg'] = "ok" 
    retmsg['websocket'] = {
            "action":"connecting",
            "secConnectionID":connectionID
        }
    if "secWebSocketProtocol" in event['websocket'].keys():
        retmsg['websocket']['secWebSocketProtocol'] = event['websocket']['secWebSocketProtocol']
    if "secWebSocketExtensions" in event['websocket'].keys():
        ext = event['websocket']['secWebSocketExtensions']
        retext = []
        exts = ext.split(";")
        print(exts)
        for e in exts:
            e = e.strip(" ")
            if e == "permessage-deflate":
                #retext.append(e)
                pass
            if e == "client_max_window_bits":
                #retext.append(e+"=15")
                pass
        retmsg['websocket']['secWebSocketExtensions'] = ";".join(retext)
    print("connecting \n connection id:%s"%event['websocket']['secConnectionID'])
    print(retmsg)
    return retmsg
```
>! 在本函数中，您可以自行扩充其他业务逻辑。例如，将 secConnectionID 保存到 TencentDB 中，创建并关联聊天室等。

### 传输函数
```
# -*- coding: utf8 -*-
import json
import requests
g_connectionID = 'xxxx'  #转发消息到某个特定的 websocket 连接
sendbackHost = "http://set-7og8wn64.cb-beijing.apigateway.tencentyun.com/api-xxxx" #API 网关的反向推送地址，在下一步 API 创建好后才能拿到
#主动向 Client 端推送消息
def send(connectionID,data):
    retmsg = {}
    retmsg['websocket'] = {}
    retmsg['websocket']['action'] = "data send"
    retmsg['websocket']['secConnectionID'] = connectionID
    retmsg['websocket']['dataType'] = 'text'
    retmsg['websocket']['data'] = json.dumps(data)
    print("send msg is %s"%retmsg)
    r = requests.post(sendbackHost, json=retmsg)   
def main_handler(event, context):
    print('Start Transmission function')
    print("event is %s"%event)
    if 'websocket' not in event.keys():
        return {"errNo":102, "errMsg":"not found web socket"}
    for k in event['websocket'].keys():
        print(k+":"+event['websocket'][k])
    # 发送内容给某个客户端
    #connectionID = event['websocket']['secConnectionID']
    data = event['websocket']['data']
    send(g_connectionID,data)
    return event
```
>! 
> - 在本函数中，您可以自行扩充其他业务逻辑。例如，将本次获取的数据转发给其他保存在 TencentDB 中的 secConnectionID。
> - 在 API 网关的 API 详情中，可以获取 API 网关的反向推送地址。具体操作参看 [配置 API 网关](https://cloud.tencent.com/document/product/583/32971#.E9.85.8D.E7.BD.AE-api-.E7.BD.91.E5.85.B3)。

### 清理函数
```
import json
import requests
g_connectionID = 'xxxx'  #转发消息到某个特定的 websocket 连接
sendbackHost = "http://set-7og8wn64.cb-beijing.apigateway.tencentyun.com/api-xxxx" #API 网关的反向推送地址，在下一步 API 创建好后才能拿到
#主动发送断开信息
def close(connectionID):
    retmsg = {}
    retmsg['websocket'] = {}
    retmsg['websocket']['action'] = "closing"
    retmsg['websocket']['secConnectionID'] = connectionID
    r = requests.post(sendbackHost, json=retmsg)
    return retmsg
def main_handler(event, context):
    print('Start Delete function')
    print("event is %s"%event)
    if 'websocket' not in event.keys():
        return {"errNo":102, "errMsg":"not found web socket"}
    for k in event['websocket'].keys():
        print(k+":"+event['websocket'][k])        
    #close(g_connectionID)
    return event
```
>! 
> - 在本函数中，您可以自行扩充其他业务逻辑。例如，将本次断开的 secConnectionID 从 TencentDB 中移除，或强制某个 secConnectionID 的 Client 下线。

您可前往  [基于 Websocket 搭建匿名聊天室 ](https://cloud.tencent.com/document/product/583/32970)，通过实践了解云函数及 API 网关的创建及使用方法。
