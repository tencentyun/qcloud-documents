

__功能__

[MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34776#mlvbliveroom) 事件回调。

__介绍__

包括房间关闭、Debug 事件信息和出错说明等。



## 通用事件回调
### onError

错误回调。
```
void onError(int errCode, String errMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errMsg | String | 错误信息。 |
| extraInfo | Bundle | 额外信息，如错误发生的用户，一般不需要关注，默认是本地错误。 |

__介绍__

SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

***

### onWarning

警告回调。
```
void onWarning(int warningCode, String warningMsg, Bundle extraInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| warningCode | int | 错误码 TRTCWarningCode。 |
| warningMsg | String | 警告信息。 |
| extraInfo | Bundle | 额外信息，如警告发生的用户，一般不需要关注，默认是本地错误。 |

***

### onDebugLog
```
void onDebugLog(String log)
```

***


## 房间事件回调
### onRoomDestroy

房间被销毁的回调。
```
void onRoomDestroy(String roomID)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomID | String | 房间 ID。 |

__介绍__

主播退房时，房间内的所有用户都会收到此通知。

***

### onAnchorEnter

收到新主播进房通知。
```
void onAnchorEnter(AnchorInfo anchorInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| anchorInfo | AnchorInfo | 新进房用户信息。 |

__介绍__

房间内的主播（和连麦中的观众）会收到新主播的进房事件，您可以调用 [MLVBLiveRoom#startRemoteView(AnchorInfo， TXCloudVideoView， PlayCallback)](https://cloud.tencent.com/document/product/454/34776#startremoteview) 显示该主播的视频画面。

>?直播间里的普通观众不会收到主播加入和推出的通知。


***

### onAnchorExit

收到主播退房通知。
```
void onAnchorExit(AnchorInfo anchorInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| anchorInfo | AnchorInfo | 退房用户信息。 |

__介绍__

房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 [MLVBLiveRoom#stopRemoteView(AnchorInfo)](https://cloud.tencent.com/document/product/454/34776#stopremoteview) 关闭该主播的视频画面。

>?直播间里的普通观众不会收到主播加入和推出的通知。


***

### onAudienceEnter

收到观众进房通知。
```
void onAudienceEnter(AudienceInfo audienceInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| audienceInfo | AudienceInfo | 进房观众信息。 |

***

### onAudienceExit

收到观众退房通知。
```
void onAudienceExit(AudienceInfo audienceInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| audienceInfo | AudienceInfo | 退房观众信息。 |

***

### onRequestJoinAnchor

主播收到观众连麦请求时的回调。
```
void onRequestJoinAnchor(AnchorInfo anchorInfo, String reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| anchorInfo | AnchorInfo | 观众信息。 |
| reason | String | 连麦原因描述。 |

***

### onKickoutJoinAnchor

连麦观众收到被踢出连麦的通知。
```
void onKickoutJoinAnchor()
```

__介绍__

连麦观众收到被主播踢除连麦的消息，您需要调用 [MLVBLiveRoom#kickoutJoinAnchor(String)](https://cloud.tencent.com/document/product/454/34776#kickoutjoinanchor) 来退出连麦。

***

### onRequestRoomPK

收到请求跨房 PK 通知。
```
void onRequestRoomPK(AnchorInfo anchorInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| anchorInfo | AnchorInfo | 发起跨房连麦的主播信息。 |

__介绍__

主播收到其他房间主播的 PK 请求 如果同意 PK ，您需要调用 MLVBLiveRoom#startRemoteView(AnchorInfo， TXCloudVideoView， PlayCallback) 接口播放邀约主播的流。

***

### onQuitRoomPK

收到断开跨房 PK 通知。
```
void onQuitRoomPK(AnchorInfo anchorInfo)
```

***


## 消息事件回调
### onRecvRoomTextMsg

收到文本消息。
```
void onRecvRoomTextMsg(String roomID, String userID, String userName, String userAvatar, String message)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomID | String | 房间 ID。 |
| userID | String | 发送者 ID。 |
| userName | String | 发送者昵称。 |
| userAvatar | String | 发送者头像。 |
| message | String | 文本消息。 |

***

### onRecvRoomCustomMsg

收到自定义消息。
```
void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomID | String | 房间 ID。 |
| userID | String | 发送者 ID。 |
| userName | String | 发送者昵称。 |
| userAvatar | String | 发送者头像。 |
| cmd | String | 自定义 cmd。 |
| message | String | 自定义消息内容。 |

***


## LoginCallback

__功能__

登录结果回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## GetRoomListCallback

__功能__

获取房间列表回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess(ArrayList< RoomInfo > roomInfoList)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomInfoList | ArrayList< RoomInfo > | 房间列表。 |

***


## GetAudienceListCallback

__功能__

获取观众列表回调接口。

__介绍__

观众进房时，后台会将其信息加入观众列表中，观众列表最大保存30名观众信息。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess(ArrayList< AudienceInfo > audienceInfoList)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| audienceInfoList | ArrayList< AudienceInfo > | 观众列表。 |

***


## CreateRoomCallback

__功能__

创建房间的结果回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess(String RoomID)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| RoomID | String | 房间号标识。 |

***


## EnterRoomCallback

__功能__

创建房间的结果回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## ExitRoomCallback

__功能__

离开房间的结果回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## RequestJoinAnchorCallback

__功能__

观众请求连麦的结果回调接口。



### onAccept

主播接受连麦。
```
void onAccept()
```

***

### onReject

主播拒绝连麦。
```
void onReject(String reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | String | 拒绝原因。 |

***

### onTimeOut

请求超时。
```
void onTimeOut()
```

***

### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***


## JoinAnchorCallback

__功能__

进入连麦的结果回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码 RequestRoomPKCallback。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## QuitAnchorCallback

__功能__

进入连麦的结果回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## RequestRoomPKCallback

__功能__

请求跨房 PK 的结果回调接口。



### onAccept

主播接受连麦。
```
void onAccept(AnchorInfo anchorInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| anchorInfo | AnchorInfo | 被邀请 PK 主播的信息。 |

***

### onReject

拒绝 PK。
```
void onReject(String reason)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | String | 拒绝原因。 |

***

### onTimeOut

请求超时。
```
void onTimeOut()
```

***

### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***


## QuitRoomPKCallback

__功能__

退出跨房 PK 的结果回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## PlayCallback

__功能__

播放器回调接口。



### onBegin

开始回调。
```
void onBegin()
```

***

### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onEvent

其他事件回调。
```
void onEvent(int event, Bundle param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| event | int | 事件 ID。 |
| param | Bundle | 事件附加信息。 |

***


## SendRoomTextMsgCallback

__功能__

发送文本消息回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## SendRoomCustomMsgCallback

__功能__

发送自定义消息回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## SetCustomInfoCallback

__功能__

设置自定义信息回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onSuccess

成功回调。
```
void onSuccess()
```

***


## GetCustomInfoCallback

__功能__

获取自定义信息回调接口。



### onError

错误回调。
```
void onError(int errCode, String errInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。 |
| errInfo | String | 错误信息。 |

***

### onGetCustomInfo

获取自定义信息的回调。
```
void onGetCustomInfo(Map< String, Object > customInfo)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| customInfo | Map< String, Object > | 自定义信息。 |

***
