**功能**

[MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34763?!editLang=zh&!preview) 事件回调。

**介绍**

包括房间关闭、Debug 事件信息及出错说明等。

 ## MLVBLiveRoomDelegate API 概览

### 通用事件回调

| API                       | 描述     |
| ------------------------- | -------- |
| [onError](#onError)       | 错误回调 |
| [onWarning](#onWarning)   | 警告回调 |
| [onDebugLog](#onDebugLog) | Log 回调 |

### 房间事件回调 

| API                             | 描述             |
| ------------------------------- | ---------------- |
| [onRoomDestroy](#onRoomDestroy) | 房间被销毁的回调 |

### 主播和观众的进出事件回调 

| API                                 | 描述               |
| ----------------------------------- | ------------------ |
| [onAnchorEnter](#onAnchorEnter)     | 收到新主播进房通知 |
| [onAnchorExit](#onAnchorExit)       | 收到主播退房通知   |
| [onAudienceEnter](#onAudienceEnter) | 收到观众进房通知   |
| [onAudienceExit](#onAudienceExit)   | 收到观众退房通知   |

### 主播和观众连麦事件回调 

| API                                         | 描述                         |
| ------------------------------------------- | ---------------------------- |
| [onRequestJoinAnchor](#onRequestJoinAnchor) | 主播收到观众连麦请求时的回调 |
| [onKickoutJoinAnchor](#onKickoutJoinAnchor) | 连麦观众收到被踢出连麦的通知 |

### 主播 PK 事件回调 

| API                                 | 描述                 |
| ----------------------------------- | -------------------- |
| [onRequestRoomPK](#onRequestRoomPK) | 收到请求跨房 PK 通知 |
| [onQuitRoomPK](#onQuitRoomPK)       | 收到断开跨房 PK 通知 |

### 消息事件回调 

| API                                         | 描述           |
| ------------------------------------------- | -------------- |
| [onRecvRoomTextMsg](#onRecvRoomTextMsg)     | 收到文本消息   |
| [onRecvRoomCustomMsg](#onRecvRoomCustomMsg) | 收到自定义消息 |



## 通用事件回调

<h3 id="onError">onError</h3>

错误回调。

```
- (void)onError:(int)errCode errMsg:(NSString *)errMsg extraInfo:(NSDictionary *)extraInfo 
```

**参数**

| 参数      | 类型           | 含义                                                         |
| :-------- | :------------- | :----------------------------------------------------------- |
| errCode   | int            | 错误码。                                                     |
| errMsg    | NSString *     | 错误信息。                                                   |
| extraInfo | NSDictionary * | 额外信息，如错误发生的用户，一般不需要关注，默认是本地错误。 |

**介绍**

SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

------

<h3 id="onWarning">onWarning</h3>

警告回调。

```
- (void)onWarning:(int)warningCode warningMsg:(NSString *)warningMsg extraInfo:(NSDictionary *)extraInfo 
```

**参数**

| 参数        | 类型           | 含义                                                         |
| :---------- | :------------- | :----------------------------------------------------------- |
| warningCode | int            | 错误码 TRTCWarningCode。                                     |
| warningMsg  | NSString *     | 警告信息。                                                   |
| extraInfo   | NSDictionary * | 额外信息，如警告发生的用户，一般不需要关注，默认是本地错误。 |

------

<h3 id="onDebugLog">onDebugLog</h3>

Log 回调。

```
- (void)onDebugLog:(NSString *)log 
```

**参数**

| 参数 | 类型       | 含义       |
| :--- | :--------- | :--------- |
| log  | NSString * | LOG 信息。 |

------

## 房间事件回调

<h3 id="onRoomDestroy">onRoomDestroy</h3>

房间被销毁的回调。

```
- (void)onRoomDestroy:(NSString *)roomID 
```

**参数**

| 参数   | 类型       | 含义      |
| :----- | :--------- | :-------- |
| roomID | NSString * | 房间 ID。 |

**介绍**

主播退房时，房间内的所有用户都会收到此通知。

## 主播和观众的进出事件回调

<h3 id="onAnchorEnter">onAnchorEnter</h3>

收到新主播进房通知。

```
- (void)onAnchorEnter:(MLVBAnchorInfo *)anchorInfo 
```

**参数**

| 参数       | 类型             | 含义             |
| :--------- | :--------------- | :--------------- |
| anchorInfo | MLVBAnchorInfo * | 新进房用户信息。 |

**介绍**

房间内的主播和连麦中的观众会收到新主播的进房事件，您可以调用 [MLVBLiveRoom.startRemoteView](https://cloud.tencent.com/document/product/454/34763?!editLang=zh&!preview#startRemoteView) 显示该主播的视频画面。

>? 直播间里的普通观众不会收到主播加入和推出的通知。

------

<h3 id="onAnchorExit">onAnchorExit</h3>

收到主播退房通知。

```
- (void)onAnchorExit:(MLVBAnchorInfo *)anchorInfo 
```

**参数**

| 参数       | 类型             | 含义           |
| :--------- | :--------------- | :------------- |
| anchorInfo | MLVBAnchorInfo * | 退房用户信息。 |

**介绍**

房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 [MLVBLiveRoom.stopRemoteView](https://cloud.tencent.com/document/product/454/34763?!editLang=zh&!preview#stopRemoteView) 关闭该主播的视频画面。

>? 直播间里的普通观众不会收到主播加入和推出的通知。

------

<h3 id="onAudienceEnter">onAudienceEnter</h3>

收到观众进房通知。

```
- (void)onAudienceEnter:(MLVBAudienceInfo *)audienceInfo 
```

**参数**

| 参数         | 类型               | 含义           |
| :----------- | :----------------- | :------------- |
| audienceInfo | MLVBAudienceInfo * | 进房观众信息。 |

------

<h3 id="onAudienceExit">onAudienceExit</h3>

收到观众退房通知。

```
- (void)onAudienceExit:(MLVBAudienceInfo *)audienceInfo 
```

**参数**

| 参数         | 类型               | 含义           |
| :----------- | :----------------- | :------------- |
| audienceInfo | MLVBAudienceInfo * | 退房观众信息。 |

## 主播和观众连麦事件回调

<h3 id="onRequestJoinAnchor">onRequestJoinAnchor</h3>

主播收到观众连麦请求时的回调。

```
- (void)onRequestJoinAnchor:(MLVBAnchorInfo *)anchorInfo reason:(NSString *)reason 

```

**参数**

| 参数       | 类型             | 含义           |
| :--------- | :--------------- | :------------- |
| anchorInfo | MLVBAnchorInfo * | 观众信息。     |
| reason     | NSString *       | 连麦原因描述。 |

------

<h3 id="onKickoutJoinAnchor">onKickoutJoinAnchor</h3>

连麦观众收到被踢出连麦的通知。

```
- (void)onKickoutJoinAnchor

```

**介绍**

连麦观众收到被主播踢除连麦的消息，您需要调用 [MLVBLiveRoom.kickoutJoinAnchor](https://cloud.tencent.com/document/product/454/34763?!editLang=zh&!preview#kickoutJoinAnchor ) 来退出连麦。

## 主播 PK 事件回调

<h3 id="onRequestRoomPK">onRequestRoomPK</h3>

收到请求跨房 PK 通知。

```
- (void)onRequestRoomPK:(MLVBAnchorInfo *)anchorInfo 

```

**参数**

| 参数       | 类型             | 含义                     |
| :--------- | :--------------- | :----------------------- |
| anchorInfo | MLVBAnchorInfo * | 发起跨房连麦的主播信息。 |

**介绍**

主播收到其他房间主播的 PK 请求，如果同意 PK ，您需要调用 [MLVBLiveRoom.startRemoteView](https://cloud.tencent.com/document/product/454/34763?!editLang=zh&!preview#startRemoteView) 接口播放邀约主播的流。

------

<h3 id="onQuitRoomPK">onQuitRoomPK</h3>

收到断开跨房 PK 通知。

```
- (void)onQuitRoomPK

```

## 消息事件回调

<h3 id="onRecvRoomTextMsg">onRecvRoomTextMsg</h3>

收到文本消息。

```
- (void)onRecvRoomTextMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar message:(NSString *)message 

```

**参数**

| 参数       | 类型       | 含义         |
| :--------- | :--------- | :----------- |
| roomID     | NSString * | 房间 ID。    |
| userID     | NSString * | 发送者 ID。  |
| userName   | NSString * | 发送者昵称。 |
| userAvatar | NSString * | 发送者头像。 |
| message    | NSString * | 文本消息。   |

------

<h3 id="onRecvRoomCustomMsg">onRecvRoomCustomMsg</h3>

收到自定义消息。

```
- (void)onRecvRoomCustomMsg:(NSString *)roomID userID:(NSString *)userID userName:(NSString *)userName userAvatar:(NSString *)userAvatar cmd:(NSString *)cmd message:(NSString *)message 
```

**参数**

| 参数       | 类型       | 含义             |
| :--------- | :--------- | :--------------- |
| roomID     | NSString * | 房间 ID。        |
| userID     | NSString * | 发送者 ID。      |
| userName   | NSString * | 发送者昵称。     |
| userAvatar | NSString * | 发送者头像。     |
| cmd        | NSString * | 自定义 cmd。     |
| message    | NSString * | 自定义消息内容。 |
