在 [原理介绍](https://cloud.tencent.com/document/product/583/32553) 章节中，提到需要3类云函数来承载与 API 网关之间的交互：
- 注册函数：在客户端发起和 API 网关之间建立 WebSocket 连接时触发该函数，通知 SCF WebSocket 连接的 secConnectionID。通常会在该函数记录 secConnectionID 到持久存储中，用于后续数据的反向推送。
- 清理函数：在客户端主动发起 WebSocket 连接中断请求时触发该函数，通知 SCF 准备断开连接的 secConnectionID。通常会在该函数清理持久存储中记录的该 secConnectionID。
- 传输函数：在客户端通过 WebSocket 连接发送数据时触发该函数，告知 SCF 连接的 secConnectionID 以及发送的数据。通常会在该函数处理业务数据。例如，是否将数据推送给持久存储中的其他 secConnectionID。

>! 当您需要主动给某个 secConnectionID 推送数据或主动断开某个 secConnectionID 时，均需要用到 API 网关的反向推送地址。

本文档以 Python2.7 为例，介绍各类函数 main_handler 的写法，以及 API 网关的创建及使用。

## 创建云函数

### 注册函数

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)。
2. 在左侧导航栏中，选择【[函数服务](https://console.cloud.tencent.com/scf/list)】，进入函数服务管理页面。
3. 单击【新建】按钮，选择 “空白函数”，定义函数名称，创建函数。例如，创建了一个名称为 Register 的空白函数。
4. 在 Register 的空白函数中，选择 “函数代码” 页签，并将以下代码拷贝至在线编辑框中。以下函数代码可以保持为默认配置。
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

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)。
2. 在左侧导航栏中，选择【[函数服务](https://console.cloud.tencent.com/scf/list)】，进入函数服务管理页面。
3. 单击【新建】按钮，选择 “空白函数”，定义函数名称，创建函数。例如，创建了一个名称为 Transmission 的空白函数。
4. 在 Transmission 的空白函数中，选择 “函数代码” 页签，并将以下代码拷贝至在线编辑框中。以下函数代码可以保持为默认配置。
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
> - 在 API 网关的 API 详情中，可以获取 API 网关的反向推送地址。具体操作参看 [配置 API 网关](#ConfigureAPIGateway)。

### 清理函数

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)。
2. 在左侧导航栏中，选择【[函数服务](https://console.cloud.tencent.com/scf/list)】，进入函数服务管理页面。
3. 单击【新建】按钮，选择 “空白函数”，定义函数名称，创建函数。例如，创建了一个名称为 Delete 的空白函数。
4. 在 Delete 的空白函数中，选择 “函数代码” 页签，并将以下代码拷贝至在线编辑框中。以下函数代码可以保持为默认配置。
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
> - 在 API 网关的 API 详情中，可以获取 API 网关的反向推送地址。具体操作参看 [配置 API 网关](#ConfigureAPIGateway)。

<span id="ConfigureAPIGateway"></span>
## 配置 API 网关

### 创建 API

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=8)。
2. 选择与云函数相同的地域，并单击【新建】，创建服务。
3. 单击【API配置】，进入 “API管理” 页面。
4. 单击【新建】，进入 “新建API” 页面。
5. 在 “前端配置” 中，将 “前端类型” 设置为 “WEBSOCKET”，并根据实际需求填写 “路径” 和 “鉴权类型”。如下图所示：
![](https://main.qcloudimg.com/raw/255e351bf7926e1a984e2735877bbb80.png)
6. 单击【下一步】。
7. 在 “后端配置” 中，将 “后端类型” 设置为 “cloud function”，并根据实际需求设置 “传输函数”、“注册函数” 和 “清理函数” 等参数。如下图所示：
>! 
> - 后端超时：Client 端在建立 WebSocket 连接后，如果一直没有消息发送，将会在超时时间到达后，由 API 网关断开连接。
> - 响应集成（建议不要勾选）：当勾选响应集成后，云函数的返回值需要按照约定的 JSON 数据结构返回。

 ![](https://main.qcloudimg.com/raw/ed7baa101cbd407f6d046b51a9ebb57b.png)

8. 根据页面提示，逐步完成操作。

### 发布服务

1. 切换至【服务信息】页签，单击【发布】。如下图所示：
![](https://main.qcloudimg.com/raw/25cac411f73a735e481d31f965666e6d.png)
2. 在弹出的 “发布服务” 窗口中，选择 “发布环境”，单击【提交】。
3. 单击【确认】。
4. 切换至【API管理】页签，单击 API 的 ID/名称，查看 API 详情以及 WebSocket 的反向推送地址。如下图所示：
![](https://main.qcloudimg.com/raw/8a5f79013046f66eba25aa10fc7f7986.png)
>! 该推送地址会在 Server 端主动向 Client 端发送消息，或者在主动断开与 Client 端的连接时使用。


### 获取 WebSocket 连接地址

切换至【环境管理】页签，查看 API 服务地址。如下图所示：
![](https://main.qcloudimg.com/raw/48b5e37072da95df2238ec3cd2eec504.png)
根据服务地址，可知 WebSocket 的 API 地址为："ws://service-0sua8j6z-1256608914.ap-beijing.apigateway.myqcloud.com/release/websocket"
>! WebSocket 的 API 地址需要带上 API 的路径 “/websocket”。
