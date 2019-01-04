在【WebSocket 原理介绍】章节中，提到需要 3 类云函数来承载与 API 网关之间的交互：
- 注册函数：在 Client 端发起和 API 网关之间建立 websocket 连接时触发该函数，通知 SCF websocket 连接的 secConnectionID。通常会在该函数中记录 secConnectionID 到持久存储中，用于后续数据的反向推送。
- 清理函数：在 Client 端主动发起 websocket 连接中断请求时触发该函数，通知 SCF 准备断开连接的 secConnectionID。通常会在该函数中清理持久存储中记录的该 secConnectionID。
- 传输函数：在 Client 端通过 websocket 连接发送数据时触发该函数，告知 SCF 连接的 secConnectionID 以及发送的数据。通常会在该函数中处理业务数据，如是否把数据推送给持久存储中的其他 secConnectionID。
*注：当需要主动给某个 secConnectionID 推送数据或主动断开某个 secConnectionID 时，均需要用到 API 网关的反向推送地址。*

本章节会以 Python2.7 为例，重点介绍每类函数 main_handler 的示例写法，以及 API 网关的创建及使用。

## 创建云函数

### 注册函数

在云函数控制台上，创建空白函数，函数可以命名为 Register，并使用如下代码，函数可以保持为默认配置。

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
*在本函数中，用户可自行扩充其他业务逻辑，如把 secConnectionID 保存到 CDB 中，创建并关联聊天室等*

### 传输函数
在云函数控制台上，创建空白函数，函数可以命名为 Transmission，并使用如下代码，函数可以保持为默认配置。
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
*在本函数中，用户可自行扩充其他业务逻辑，如把本次获取的数据转发给其他保存在 CDB 中的 secConnectionID；
API 网关的反向推送地址在 API 网关的 API 详情里可以获取，下一步在配置 API 网关时会展示。*

### 清理函数

在云函数控制台上，创建空白函数，函数可以命名为 Delete，并使用如下代码，函数可以保持为默认配置。
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
*在本函数中，用户可自行扩充其他业务逻辑，如把本次断开的 secConnectionID 从 CDB 中移除，或强制某个 secConnectionID的 Client 下线；
API 网关的反向推送地址在 API 网关的 API 详情里可以获取，下一步在配置 API 网关时会展示。*

## 配置 API 网关
### 创建 API
前往 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=8),在与云函数相同的地域下创建 API 服务。然后再新建 API，如下图所示：
- 在前端配置中，前端类型选择 websocket，路径和鉴权方式根据实际需要填写
- 在后端配置中，后端类型选择 cloud function，然后分别对应选择传输函数、注册函数、清理函数。
*超时时间：Client 端在建立 websocket 连接后，如果一直没有消息发送，则会在超时时间到达后，由 API 网关断开连接；
响应集成（建议不要勾选）：当勾选响应集成后，则云函数的返回值需要按照约定的 json 数据结构返回*
![](https://main.qcloudimg.com/raw/af3ab8fb9913ef0f391bb704a9798da7.png)
![](https://main.qcloudimg.com/raw/e350af206f3d6fab77774283d9ea3d40.png)

### 发布服务
创建完 API 后，可以前往【服务信息】里，对服务进行发布，可以选择发布到正式环境，如下图所示：
![](https://main.qcloudimg.com/raw/25cac411f73a735e481d31f965666e6d.png)
发布完成后，前往【API 管理】，查看 API 详情，**并查看 websocket 的反向推送地址，**如下图所示：
*该推送地址，会在 Server 端主动向 Client 端发送消息、或者主动断开与 Client 端的连接时使用*
![](https://main.qcloudimg.com/raw/8a5f79013046f66eba25aa10fc7f7986.png)

### 获取 websocket 连接地址
前往【环境管理】，查看 API 服务地址，如下图所示：
![](https://main.qcloudimg.com/raw/48b5e37072da95df2238ec3cd2eec504.png)
根据服务地址，可知 websocket 的 API 地址为："ws://service-0sua8j6z-1256608914.ap-beijing.apigateway.myqcloud.com/release/websocket"
*websocket 的 API 地址需要带上 API 的路径'/websocket'*