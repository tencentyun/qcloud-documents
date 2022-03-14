__功能__

[MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34763) 事件回调。

__介绍__

包括房间关闭、Debug 事件信息及出错说明等。 



## 通用事件回调

### onError

错误回调。

```
- (void)onError:(int)errCode errMsg:(NSString *)errMsg extraInfo:(NSDictionary *)extraInfo 
```

__参数__

| 参数      | 类型           | 含义                                                         |
| --------- | -------------- | ------------------------------------------------------------ |
| errCode   | int            | 错误码。                                                     |
| errMsg    | NSString *     | 错误信息。                                                   |
| extraInfo | NSDictionary * | 额外信息，如错误发生的用户，一般不需要关注，默认是本地错误。 |

__介绍__

SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

***

### onWarning

警告回调。

```
- (void)onWarning:(int)warningCode warningMsg:(NSString *)warningMsg extraInfo:(NSDictionary *)extraInfo 
```

__参数__

| 参数        | 类型           | 含义                                                         |
| ----------- | -------------- | ------------------------------------------------------------ |
| warningCode | int            | 错误码 TRTCWarningCode。                                     |
| warningMsg  | NSString *     | 警告信息。                                                   |
| extraInfo   | NSDictionary * | 额外信息，如警告发生的用户，一般不需要关注，默认是本地错误。 |

***

### onDebugLog

Log 回调。

```
- (void)onDebugLog:(NSString *)log 
```

__参数__

| 参数 | 类型       | 含义       |
| ---- | ---------- | ---------- |
| log  | NSString * | LOG 信息。 |

***


## 房间事件回调

### onRoomDestroy

房间被销毁的回调。

```
- (void)onRoomDestroy:(NSString *)roomID 
```

__参数__

| 参数   | 类型       | 含义      |
| ------ | ---------- | --------- |
| roomID | NSString * | 房间 ID。 |

__介绍__

主播退房时，房间内的所有用户都会收到此通知。

***


## 主播和观众的进出事件回调

### onAnchorEnter

收到新主播进房通知。

```
- (void)onAnchorEnter:(MLVBAnchorInfo *)anchorInfo 
```

__参数__

| 参数       | 类型             | 含义             |
| ---------- | ---------------- | ---------------- |
| anchorInfo | MLVBAnchorInfo * | 新进房用户信息。 |

__介绍__

房间内的主播和连麦中的观众会收到新主播的进房事件，您可以调用 [MLVBLiveRoom startRemoteView](https://cloud.tencent.com/document/product/454/34763#startremoteview)  显示该主播的视频画面。

>?直播间里的普通观众不会收到主播加入和推出的通知。

***

### onAnchorExit

收到主播退房通知。

```
- (void)onAnchorExit:(MLVBAnchorInfo *)anchorInfo 
```

__参数__

| 参数       | 类型             | 含义           |
| ---------- | ---------------- | -------------- |
| anchorInfo | MLVBAnchorInfo * | 退房用户信息。 |

__介绍__

房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 [MLVBLiveRoom stopRemoteView](https://cloud.tencent.com/document/product/454/34763#stopremoteview) 关闭该主播的视频画面。

>?直播间里的普通观众不会收到主播加入和推出的通知。

***

### onAudienceEnter

收到观众进房通知。

```
- (void)onAudienceEnter:(MLVBAudienceInfo *)audienceInfo 
```

__参数__

| 参数         | 类型               | 含义           |
| ------------ | ------------------ | -------------- |
| audienceInfo | MLVBAudienceInfo * | 进房观众信息。 |

***

### onAudienceExit

收到观众退房通知。

```
- (void)onAudienceExit:(MLVBAudienceInfo *)audienceInfo 
```

__参数__

| 参数         | 类型               | 含义           |
| ------------ | ------------------ | -------------- |
| audienceInfo | MLVBAudienceInfo * | 退房观众信息。 |

***


## 主播和观众连麦事件回调

### onRequestJoinAnchor

主播收到观众连麦请求时的回调。

```
- (void)onRequestJoinAnchor:(MLVBAnchorInfo *)anchorInfo reason:(NSString *)reason 
```

__参数__

| 参数       | 类型             | 含义           |
| ---------- | ---------------- | -------------- |
| anchorInfo | MLVBAnchorInfo * | 观众信息。     |
| reason     | NSString *       | 连麦原因描述。 |

***

### onKickoutJoinAnchor

连麦观众收到被踢出连麦的通知。

```
- (void)onKickoutJoinAnchor
```

__介绍__

连麦观众收到被主播踢除连麦的消息，您需要调用 [MLVBLiveRoom kickoutJoinAnchor](https://cloud.tencent.com/document/product/454/34763#kickoutjoinanchor) 来退出连麦。

***


## 主播 PK 事件回调

### onRequestRoomPK

收到请求跨房 PK 通知。

```
- (void)onRequestRoomPK:(MLVBAnchorInfo *)anchorInfo 
```

__参数__

| 参数       | 类型             | 含义                     |
| ---------- | ---------------- | ------------------------ |
| anchorInfo | MLVBAnchorInfo * | 发起跨房连麦的主播信息。 |

__介绍__

主播收到其他房间主播的 PK 请求，如果同意 PK ，您需要调用 [MLVBLiveRoom startRemoteView](https://cloud.tencent.com/document/product/454/34763#startremoteview)  接口播放邀约主播的流。

***

### onQuitRoomPK

收到断开跨房 PK 通知。

```
- (void)onQuitRoomPK
```

***


## 消息事件回调

### onRecvRoomTextMsg

收到文本消息。

```
- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar message:(NSString *)message 
```

__参数__

| 参数       | 类型       | 含义         |
| ---------- | ---------- | ------------ |
| roomID     | NSString * | 房间 ID。    |
| userID     | NSString * | 发送者 ID。  |
| userName   | NSString * | 发送者昵称。 |
| userAvatar | NSString * | 发送者头像。 |
| message    | NSString * | 文本消息。   |

***

### onRecvRoomCustomMsg

收到自定义消息。

```
- (void)onRecvRoomCustomMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar cmd:(NSString *)cmd message:(NSString *)message 
```

__参数__

| 参数       | 类型       | 含义             |
| ---------- | ---------- | ---------------- |
| roomID     | NSString * | 房间 ID。        |
| userID     | NSString * | 发送者 ID。      |
| userName   | NSString * | 发送者昵称。     |
| userAvatar | NSString * | 发送者头像。     |
| cmd        | NSString * | 自定义 cmd。     |
| message    | NSString * | 自定义消息内容。 |


