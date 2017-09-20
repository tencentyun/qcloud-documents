## 事件通知简介

在某些事件发生，或者异步任务执行完毕之后，点播服务端可以将此类事件通知到APP的服务端。目前点播系统支持的事件通知包括：

| 事件类型 | eventType |
|---------|---------|
| 任务流状态变更通知 | [ProcedureStateChanged](/document/product/266/9636) |
| 视频上传完成 | [NewFileUpload](/document/product/266/7830) |
| URL转拉完成 | [PullComplete](/document/product/266/7831) |
| 视频转码完成 | [TranscodeComplete](/document/product/266/7832) |
| 视频拼接完成 | [ConcatComplete](/document/product/266/7834) |
| 视频剪辑完成 | [ClipComplete](/document/product/266/10157) |
| 视频截取雪碧图完成 | [CreateImageSpriteComplete](/document/product/266/8104) |
| 视频按时间点截图完成 | [CreateSnapshotByTimeOffsetComplete](/document/product/266/8105) |

点播支持APP通过两种方式来获取事件通知：

- HTTP回调；
- 基于消息队列的可靠通知。

两种方式相比：前者配置简单；后者安全性高、可靠性强，但配置略为复杂。

## HTTP回调

HTTP回调的基本流程是：APP后台搭建一个HTTP服务来接收回调，并在点播控制台上配置回调URL；当事件发生时，点播服务端会向该URL发起HTTP POST请求，具体事件内容将通过HTTP Body送达APP后台。

### 配置方法
在"控制台" -> "全局设置" -> "回调配置"页面中进行设置："回调URL"设置为APP后台接收回调的地址；"回调模式"选择为"普通回调"；同时选择您需要开启的事件回调类型。

如下图所示：

![](//mc.qcloudimg.com/static/img/349c36d65d5c42163ec131e1689db5a4/image.png)

### 回调协议
请求：HTTP POST请求，包体内容为JSON，每一种回调的具体包体内容参见各自文档。
应答：点播服务端忽略应答包内容。

### 公共参数说明

| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| version | String | 回调版本号，固定为4.0 |
| eventType | String | 事件类型，APP后台可以根据该字段区分不同的回调 |
| data | Object | 具体回调数据 |
| data.status | Integer | 错误码, 0: 成功, 其他值: 失败 |
| data.message | String | 错误信息  |

### 回调请求示例

如下为视频拼接成功回调示例（完整HTTP请求），此处假定回调URL为`https://www.example.com/path/to/your/service`。

```
POST /path/to/your/service
HOST: www.example.com

{
    "version": "4.0",
    "eventType": "ConcatComplete",
    "data": {
        "vodTaskId": "concat-1edb7eb88a599d05abe451cfc541cfbd",
        "fileInfo": [
            {
                "fileType": "m3u8",
                "status": 0,
                "message": "",
                "fileId": "14508071098244931831",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244931831/playlist.f6.m3u8"
            },
            {
                "fileType": "mp4",
                "status": 0,
                "message": "",
                "fileId": "14508071098244929440",
                "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4"
            }
        ]
    }
}
```

### 回调应答示例

对于HTTP回调，APP后台需要对回调请求进行应答，点播后台会忽略HTTP返回码与包体。示例如下：

```
HTTP/1.1 200 OK
Server: nginx/1.7.10
Date: Fri, 09 Oct 2015 02:59:55 GMT
Content-Length: 4

{
}
```

### 回调超时时间与重试
点播服务端发起HTTP回调的超时时间为5秒；如果回调超时，点播后台会重试两次（即：总共最多发送三次）。如果您对回调的可靠性十分敏感，建议使用基于消息队列的可靠通知。

### 安全考虑
为确保安全，APP可以将回调URL设置为HTTPS。此种方案的安全性可以达到：
- 点播服务端能够认证APP回调URL的合法性；
- 回调数据无法被人监听。

安全性无法达到：
- APP后台服务器无法认证请求方是否为点播服务端。

如果您需要更高的安全强度，建议使用基于消息队列的可靠通知。

## 基于消息队列的可靠通知

APP服务端可能会遭遇网络问题或者宕机等故障。简单HTTP回调，即时增加重试，也无法确保可靠性。为确保回调的可靠性，点播提供了第二种回调方式：基于消息队列的可靠通知。另外，此种方案的安全性更高。

### 配置方法
在"控制台" -> "全局设置" -> "回调配置"页面中进行设置："回调模式"选择为"可靠回调"；同时选择您需要开启的事件回调类型。注意：在可靠回调模式下，"回调URL"将不起作用。

如下图所示：

![](//mc.qcloudimg.com/static/img/e448c807e093ecae7651c9c94987137c/image.png)

### 基本原理介绍

- 点播后台会为APP维护一个消息队列，并扮演生产者的角色；
- 当新的事件产生时，点播后台会将该消息放入消息队列中；
- APP后台扮演消费者的角色，需要通过长轮询的方式来获取消息队列中的内容。所谓长轮询，即：APP后台必须循环调用[PullEvent](/document/product/266/7818)接口来拉取事件通知。如果当前消息队列中存在消息，则该接口会立即返回；如果当前没有未消费事件通知，则点播后台会把该请求挂起，直到有新事件产生为止；每个请求最多挂起5秒。
- APP后台通过[PullEvent](/document/product/266/7818)拉取到消息之后，必须调用[ConfirmEvent](/document/product/266/7819)接口来确认该事件通知已经消费到，否则该消息可能会被再次消费。

如下图所示：第一个虚线框描述了一次事件通知的的完整消费流程；第二个虚线框表示PullEvent没有获取到新的事件通知，APP后台需要继续发起PullEvent调用。

![](//mc.qcloudimg.com/static/img/740ef842285aef44ff4911cc702ee178/image.png)

### 相关接口
基于消息队列的可靠回调通过两个服务端API实现，参见：
- 拉取事件通知（[PullEvent](/document/product/266/7818)）；
- 确认事件通知（[ConfirmEvent](/document/product/266/7819)）。

### 示例

1，APP后台调用[PullEvent](/document/product/266/7818)，来获取未消费事件通知，请求URL为：

```
https://vod.api.qcloud.com/v2/index.php?Action=PullEvent
&COMMON_PARAMS
```

2，假设当前存在未消费事件通知，服务端应答包体如下。eventList中的msgHandle字段比较关键，后续会用到。

```javascript
{
    "code": 0,
    "message": "",
    "eventList": [  // 拉取到的服务端事件通知列表，总共两个事件通知
        {
            "msgHandle": "MsgHandle1",  // 第一个事件通知的句柄
            "eventContent": { // 第一个事件通知的内容
                "version": "4.0",
                "eventType": "NewFileUpload", // 该字段表明事件通知的类型为“视频上传完成”
                "data": {
                    "fileId": "14508071098244959037",
                    "fileUrl": "http://251000330.vod2.myqcloud.com/vod251000330/14508071098244959037/f0.flv",
                    "transcodeTaskId": "transcode-0bee89b07a248e27c83fc3d5951213c1",
                    "porncheckTaskId": "porncheck-f5ac8127b3b6b85cdc13f237c6005d80"
                }
            }
        },
        {
            "msgHandle": "MsgHandle2", // 第二个事件通知的句柄
            "eventContent": { // 第二个事件通知的内容
                "version": 4,
                "eventType": "ConcatComplete", // 该字段表明事件通知的类型为“视频拼接完成”
                "data": {
                    "status": 0,
                    "message": "",
                    "vodTaskId": "concat-1edb7eb88a599d05abe451cfc541cfbd",
                    "fileInfo": [
                        {
                            "fileId": "14508071098244931831",
                            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244931831/playlist.f6.m3u8",
                            "fileType": "m3u8"
                        },
                        {
                            "fileId": "14508071098244929440",
                            "fileUrl": "http://125xx.vod2.myqcloud.com/vod125xx/14508071098244929440/f0.mp4",
                            "fileType": "mp4"
                        }
                    ]
                }
            }
        }
    ]
}
```

3，APP后台在消费到事件通知后，调用[ConfirmEvent](/document/product/266/7819)接口来确认该事件通知已经收到。需要将PullEvent所返回eventList.msgHandle作为参数。

```
https://vod.api.qcloud.com/v2/index.php?Action=ConfirmEvent
&msgHandle.1=MsgHandle1
&msgHandle.2=MsgHandle2
&COMMON_PARAMS
```

4，点播服务端应答如下：

```javascript
{
    "code": 0,
    "message": ""
}
```

至此，两条服务端事件通知接收完毕。APP后台需要再次调用[PullEvent](/document/product/266/7818)来轮询服务端事件通知。