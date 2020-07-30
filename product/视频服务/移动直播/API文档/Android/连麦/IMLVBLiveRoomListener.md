**功能**

[MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34776?!preview&!editLang=zh) 事件回调。

**介绍**

包括房间关闭、Debug 事件信息和出错说明等。

##  IMLVBLiveRoomListener API 概览

###  **通用事件回调** 

| API                     | 描述       |
| ----------------------- | ---------- |
| [onError](#onError)     | 错误回调。 |
| [onWarning](#onWarning) | 警告回调。 |

###  **通用事件回调** 

| API                             | 描述               |
| ------------------------------- | ------------------ |
| [onRoomDestroy](#onRoomDestroy) | 房间被销毁的回调。 |

###  **主播与观众的进出事件回调** 

| API                                 | 描述                 |
| ----------------------------------- | -------------------- |
| [onAnchorEnter](#onAnchorEnter)     | 收到新主播进房通知。 |
| [onAnchorExit](#onAnchorExit)       | 收到主播退房通知。   |
| [onAudienceEnter](#onAudienceEnter) | 收到观众进房通知。   |
| [onAudienceExit](#onAudienceExit)   | 收到观众退房通知。   |

###   **主播和观众连麦事件回调** 

| API                                         | 描述                           |
| ------------------------------------------- | ------------------------------ |
| [onRequestJoinAnchor](#onRequestJoinAnchor) | 主播收到观众连麦请求时的回调。 |
| [onKickoutJoinAnchor](#onKickoutJoinAnchor) | 连麦观众收到被踢出连麦的通知。 |

###   **主播 PK 事件回调** 

| API                                 | 描述                   |
| ----------------------------------- | ---------------------- |
| [onRequestRoomPK](#onRequestRoomPK) | 收到请求跨房 PK 通知。 |
| [onQuitRoomPK](#onQuitRoomPK)       | 收到断开跨房 PK 通知。 |

###   **消息事件回调** 

| API                                         | 描述             |
| ------------------------------------------- | ---------------- |
| [onRecvRoomTextMsg](#onRecvRoomTextMsg)     | 收到文本消息。   |
| [onRecvRoomCustomMsg](#onRecvRoomCustomMsg) | 收到自定义消息。 |

###   **登录结果回调接口** 

| API                                   | 描述       |
| ------------------------------------- | ---------- |
| [onError](#LoginCallback_onError)     | 错误回调。 |
| [onSuccess](#LoginCallback_onSuccess) | 成功回调。 |

###   **获取房间列表回调接口** 

| API                                         | 描述       |
| ------------------------------------------- | ---------- |
| [onError](#GetRoomListCallback_onError)     | 错误回调。 |
| [onSuccess](#GetRoomListCallback_onSuccess) | 成功回调。 |

###   **获取观众列表回调接口** 

| API                                             | 描述       |
| ----------------------------------------------- | ---------- |
| [onError](#GetAudienceListCallback_onError)     | 错误回调。 |
| [onSuccess](#GetAudienceListCallback_onSuccess) | 成功回调。 |

###   **创建房间的结果回调接口** 

| API                                        | 描述       |
| ------------------------------------------ | ---------- |
| [onError](#CreateRoomCallback_onError)     | 错误回调。 |
| [onSuccess](#CreateRoomCallback_onSuccess) | 成功回调。 |

###   **进入房间的结果回调接口** 

| API                                       | 描述       |
| ----------------------------------------- | ---------- |
| [onError](#EnterRoomCallback_onError)     | 错误回调。 |
| [onSuccess](#EnterRoomCallback_onSuccess) | 成功回调。 |

###   **离开房间的结果回调接口** 

| API                                      | 描述       |
| ---------------------------------------- | ---------- |
| [onError](#ExitRoomCallback_onError)     | 错误回调。 |
| [onSuccess](#ExitRoomCallback_onSuccess) | 成功回调。 |

###   **观众请求连麦的结果回调接口** 

| API                                               | 描述           |
| ------------------------------------------------- | -------------- |
| [onAccept](#RequestJoinAnchorCallback_onAccept)   | 主播接受连麦。 |
| [onReject](#RequestJoinAnchorCallback_onReject)   | 主播拒绝连麦。 |
| [onTimeOut](#RequestJoinAnchorCallback_onTimeOut) | 请求超时。     |
| [onError](#RequestJoinAnchorCallback_onError)     | 错误回调。     |

###   **进入连麦的结果回调接口** 

| API                                        | 描述       |
| ------------------------------------------ | ---------- |
| [onError](#JoinAnchorCallback_onError)     | 错误回调。 |
| [onSuccess](#JoinAnchorCallback_onSuccess) | 成功回调。 |

###   **退出连麦的结果调用接口** 

| API                                        | 描述       |
| ------------------------------------------ | ---------- |
| [onError](#QuitAnchorCallback_onError)     | 错误回调。 |
| [onSuccess](#QuitAnchorCallback_onSuccess) | 成功回调。 |

###   **请求跨房 PK 的结果回调接口** 

| API                                           | 描述           |
| --------------------------------------------- | -------------- |
| [onAccept](#RequestRoomPKCallback_onAccept)   | 主播接受连麦。 |
| [onReject](#RequestRoomPKCallback_onReject)   | 主播拒绝连麦。 |
| [onTimeOut](#RequestRoomPKCallback_onTimeOut) | 请求超时。     |
| [onError](#RequestRoomPKCallback_onError)     | 错误回调。     |

###  **退出跨房 PK 的结果回调接口** 

| API                                        | 描述       |
| ------------------------------------------ | ---------- |
| [onError](#QuitRoomPKCallback_onError)     | 错误回调。 |
| [onSuccess](#QuitRoomPKCallback_onSuccess) | 成功回调。 |

###  **播放器回调接口** 

| API                              | 描述           |
| -------------------------------- | -------------- |
| [onBegin](#PlayCallback_onBegin) | 开始回调。     |
| [onError](#PlayCallback_onError) | 错误回调。     |
| [onEvent](#PlayCallback_onEvent) | 其他事件回调。 |

###   **发送文本消息回调接口** 

| API                                             | 描述       |
| ----------------------------------------------- | ---------- |
| [onError](#SendRoomTextMsgCallback_onError)     | 错误回调。 |
| [onSuccess](#SendRoomTextMsgCallback_onSuccess) | 成功回调。 |

###   **发送自定义消息回调接口** 

| API                                               | 描述       |
| ------------------------------------------------- | ---------- |
| [onError](#SendRoomCustomMsgCallback_onError)     | 错误回调。 |
| [onSuccess](#SendRoomCustomMsgCallback_onSuccess) | 成功回调。 |

###   **设置自定义信息回调接口** 

| API                                           | 描述       |
| --------------------------------------------- | ---------- |
| [onError](#SetCustomInfoCallback_onError)     | 错误回调。 |
| [onSuccess](#SetCustomInfoCallback_onSuccess) | 成功回调。 |

###   **获取自定义信息回调接口** 

| API                                       | 描述                   |
| ----------------------------------------- | ---------------------- |
| [onError](#GetCustomInfoCallback_onError) | 错误回调。             |
| [onGetCustomInfo](#onGetCustomInfo)       | 获取自定义信息的回调。 |



## 通用事件回调

<h3 id="onError">onError</h3>

错误回调。

```
void onError(int errCode, String errMsg, Bundle extraInfo)
```

**参数**

| 参数      | 类型   | 含义                                                         |
| :-------- | :----- | :----------------------------------------------------------- |
| errCode   | int    | 错误码。                                                     |
| errMsg    | String | 错误信息。                                                   |
| extraInfo | Bundle | 额外信息，如错误发生的用户，一般不需要关注，默认是本地错误。 |

**介绍**

SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

------

<h3 id="onWarning">onWarning</h3>

警告回调。

```
void onWarning(int warningCode, String warningMsg, Bundle extraInfo)
```

**参数**

| 参数        | 类型   | 含义                                                         |
| :---------- | :----- | :----------------------------------------------------------- |
| warningCode | int    | 错误码 TRTCWarningCode。                                     |
| warningMsg  | String | 警告信息。                                                   |
| extraInfo   | Bundle | 额外信息，如警告发生的用户，一般不需要关注，默认是本地错误。 |

## 房间事件回调

<h3 id="onRoomDestroy">onRoomDestroy</h3>

房间被销毁的回调。

```
void onRoomDestroy(String roomID)
```

**参数**

| 参数   | 类型   | 含义      |
| :----- | :----- | :-------- |
| roomID | String | 房间 ID。 |

**介绍**

主播退房时，房间内的所有用户都会收到此通知。

## 主播与观众的进出事件回调

<h3 id="onAnchorEnter">onAnchorEnter</h3>

收到新主播进房通知。

```
void onAnchorEnter(AnchorInfo anchorInfo)
```

**参数**

| 参数       | 类型       | 含义             |
| :--------- | :--------- | :--------------- |
| anchorInfo | AnchorInfo | 新进房用户信息。 |

**介绍**

房间内的主播（和连麦中的观众）会收到新主播的进房事件，您可以调用 [MLVBLiveRoom.startRemoteView(AnchorInfo， TXCloudVideoView， PlayCallback)](https://cloud.tencent.com/document/product/454/34776?!preview&!editLang=zh#startRemoteView) 显示该主播的视频画面。
>? 直播间里的普通观众不会收到主播加入和退出的通知。

------

<h3 id="onAnchorExit">onAnchorExit</h3>

收到主播退房通知。

```
void onAnchorExit(AnchorInfo anchorInfo)
```

**参数**

| 参数       | 类型       | 含义           |
| :--------- | :--------- | :------------- |
| anchorInfo | AnchorInfo | 退房用户信息。 |

**介绍**

房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 [MLVBLiveRoom.stopRemoteView(AnchorInfo)](https://cloud.tencent.com/document/product/454/34776?!preview&!editLang=zh#stopremoteview) 关闭该主播的视频画面。

>? 直播间里的普通观众不会收到主播加入和退出的通知。

------

<h3 id="onAudienceEnter">onAudienceEnter</h3>

收到观众进房通知。

```
void onAudienceEnter(AudienceInfo audienceInfo)
```

**参数**

| 参数         | 类型         | 含义           |
| :----------- | :----------- | :------------- |
| audienceInfo | AudienceInfo | 进房观众信息。 |

------

<h3 id="onAudienceExit">onAudienceExit</h3>

收到观众退房通知。

```
void onAudienceExit(AudienceInfo audienceInfo)
```

**参数**

| 参数         | 类型         | 含义           |
| :----------- | :----------- | :------------- |
| audienceInfo | AudienceInfo | 退房观众信息。 |

------

## 主播和观众连麦事件回调

<h3 id="onRequestJoinAnchor">onRequestJoinAnchor</h3>

主播收到观众连麦请求时的回调。

```
void onRequestJoinAnchor(AnchorInfo anchorInfo, String reason)
```

**参数**

| 参数       | 类型       | 含义           |
| :--------- | :--------- | :------------- |
| anchorInfo | AnchorInfo | 观众信息。     |
| reason     | String     | 连麦原因描述。 |

------

<h3 id="onKickoutJoinAnchor">onKickoutJoinAnchor</h3>

连麦观众收到被踢出连麦的通知。

```
void onKickoutJoinAnchor()
```

**介绍**

连麦观众收到被主播踢除连麦的消息，您需要调用 [MLVBLiveRoom.kickoutJoinAnchor(String)](https://cloud.tencent.com/document/product/454/34776?!preview&!editLang=zh#kickoutJoinAnchor) 来退出连麦。

## 主播 PK 事件回调

<h3 id="onRequestRoomPK">onRequestRoomPK</h3>

收到请求跨房 PK 通知。

```
void onRequestRoomPK(AnchorInfo anchorInfo)
```

**参数**

| 参数       | 类型       | 含义                     |
| :--------- | :--------- | :----------------------- |
| anchorInfo | AnchorInfo | 发起跨房连麦的主播信息。 |

**介绍**

主播收到其他房间主播的 PK 请求，如果同意 PK ，您需要调用 [MLVBLiveRoom.startRemoteView(AnchorInfo , TXCloudVideoView , PlayCallback)](https://cloud.tencent.com/document/product/454/34776?!preview&!editLang=zh#startRemoteView) 接口播放邀约主播的流。

------

<h3 id="onQuitRoomPK">onQuitRoomPK</h3>

收到断开跨房 PK 通知。

```
void onQuitRoomPK(AnchorInfo anchorInfo)
```

------

## 消息事件回调

<h3 id="onRecvRoomTextMsg">onRecvRoomTextMsg</h3>

收到文本消息。

```
void onRecvRoomTextMsg(String roomID, String userID, String userName, String userAvatar, String message)
```

**参数**

| 参数       | 类型   | 含义         |
| :--------- | :----- | :----------- |
| roomID     | String | 房间 ID。    |
| userID     | String | 发送者 ID。  |
| userName   | String | 发送者昵称。 |
| userAvatar | String | 发送者头像。 |
| message    | String | 文本消息。   |

------

<h3 id="onRecvRoomCustomMsg">onRecvRoomCustomMsg</h3>

收到自定义消息。

```
void onRecvRoomCustomMsg(String roomID, String userID, String userName, String userAvatar, String cmd, String message)
```

**参数**

| 参数       | 类型   | 含义             |
| :--------- | :----- | :--------------- |
| roomID     | String | 房间 ID。        |
| userID     | String | 发送者 ID。      |
| userName   | String | 发送者昵称。     |
| userAvatar | String | 发送者头像。     |
| cmd        | String | 自定义 cmd。     |
| message    | String | 自定义消息内容。 |

------

<h2 id="LoginCallback">LoginCallback</h2>

**功能**

登录结果回调接口。

<h3 id="LoginCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="LoginCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="GetRoomListCallback">GetRoomListCallback</h2>

**功能**

获取房间列表回调接口。

<h3 id="GetRoomListCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="GetRoomListCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess(ArrayList< RoomInfo > roomInfoList)
```

**参数**

| 参数         | 类型                  | 含义       |
| :----------- | :-------------------- | :--------- |
| roomInfoList | ArrayList< RoomInfo > | 房间列表。 |



<h2 id="GetAudienceListCallback">GetAudienceListCallback</h2>

**功能**

获取观众列表回调接口。

**介绍**

观众进房时，后台会将其信息加入观众列表中，观众列表最大保存30名观众信息。

<h3 id="GetAudienceListCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="GetAudienceListCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess(ArrayList< AudienceInfo > audienceInfoList)
```

**参数**

| 参数             | 类型                      | 含义       |
| :--------------- | :------------------------ | :--------- |
| audienceInfoList | ArrayList< AudienceInfo > | 观众列表。 |

------

<h2 id="CreateRoomCallback">CreateRoomCallback</h2>

**功能**

创建房间的结果回调接口。

<h3 id="CreateRoomCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="CreateRoomCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess(String RoomID)
```

**参数**

| 参数   | 类型   | 含义         |
| :----- | :----- | :----------- |
| RoomID | String | 房间号标识。 |

------

<h2 id="EnterRoomCallback">EnterRoomCallback</h2>

**功能**

进入房间的结果回调接口。

<h3 id="EnterRoomCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="EnterRoomCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="ExitRoomCallback">ExitRoomCallback</h2>

**功能**

离开房间的结果回调接口。

<h3 id="ExitRoomCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="ExitRoomCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="RequestJoinAnchorCallback">RequestJoinAnchorCallback</h2>

**功能**

观众请求连麦的结果回调接口。

<h3 id="RequestJoinAnchorCallback_onAccept">onAccept</h3>

主播接受连麦。

```
void onAccept()
```

------

<h3 id="RequestJoinAnchorCallback_onReject">onReject</h3>

主播拒绝连麦。

```
void onReject(String reason)
```

**参数**

| 参数   | 类型   | 含义       |
| :----- | :----- | :--------- |
| reason | String | 拒绝原因。 |

------

<h3 id="RequestJoinAnchorCallback_onTimeOut">onTimeOut</h3>

请求超时。

```
void onTimeOut()
```

------

<h3 id="RequestJoinAnchorCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h2 id="JoinAnchorCallback">JoinAnchorCallback</h2>

**功能**

进入连麦的结果回调接口。

<h3 id="JoinAnchorCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义                           |
| :------ | :----- | :----------------------------- |
| errCode | int    | 错误码 RequestRoomPKCallback。 |
| errInfo | String | 错误信息。                     |

------

<h3 id="JoinAnchorCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="QuitAnchorCallback">QuitAnchorCallback</h2>

**功能**

退出连麦的结果调用接口。

<h3 id="QuitAnchorCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="QuitAnchorCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="RequestRoomPKCallback">RequestRoomPKCallback</h2>

**功能**

请求跨房 PK 的结果回调接口。

<h3 id="RequestRoomPKCallback_onAccept">onAccept</h3>

主播接受连麦。

```
void onAccept(AnchorInfo anchorInfo)
```

**参数**

| 参数       | 类型       | 含义                   |
| :--------- | :--------- | :--------------------- |
| anchorInfo | AnchorInfo | 被邀请 PK 主播的信息。 |

------

<h3 id="RequestRoomPKCallback_onReject">onReject</h3>

拒绝 PK。

```
void onReject(String reason)
```

**参数**

| 参数   | 类型   | 含义       |
| :----- | :----- | :--------- |
| reason | String | 拒绝原因。 |

------

<h3 id="RequestRoomPKCallback_onTimeOut">onTimeOut</h3>

请求超时。

```
void onTimeOut()
```

------

<h3 id="RequestRoomPKCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h2 id="QuitRoomPKCallback">QuitRoomPKCallback</h2>

**功能**

退出跨房 PK 的结果回调接口。

<h3 id="QuitRoomPKCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)

```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="QuitRoomPKCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="PlayCallback">PlayCallback</h2>

**功能**

播放器回调接口。

<h3 id="PlayCallback_onBegin">onBegin</h3>

开始回调。

```
void onBegin()

```

------

<h3 id="PlayCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="PlayCallback_onEvent">onEvent</h3>

其他事件回调。

```
void onEvent(int event, Bundle param)
```

**参数**

| 参数  | 类型   | 含义           |
| :---- | :----- | :------------- |
| event | int    | 事件 ID。      |
| param | Bundle | 事件附加信息。 |

------

<h2 id="SendRoomTextMsgCallback">SendRoomTextMsgCallback</h2>

**功能**

发送文本消息回调接口。

<h3 id="SendRoomTextMsgCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="SendRoomTextMsgCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="SendRoomCustomMsgCallback">SendRoomCustomMsgCallback</h2>

**功能**

发送自定义消息回调接口。

<h3 id="SendRoomCustomMsgCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="SendRoomCustomMsgCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="SetCustomInfoCallback">SetCustomInfoCallback</h2>

**功能**

设置自定义信息回调接口。

<h3 id="SetCustomInfoCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

------

<h3 id="SetCustomInfoCallback_onSuccess">onSuccess</h3>

成功回调。

```
void onSuccess()
```

------

<h2 id="GetCustomInfoCallback">GetCustomInfoCallback</h2>

**功能**

获取自定义信息回调接口。

<h3 id="GetCustomInfoCallback_onError">onError</h3>

错误回调。

```
void onError(int errCode, String errInfo)
```

**参数**

| 参数    | 类型   | 含义       |
| :------ | :----- | :--------- |
| errCode | int    | 错误码。   |
| errInfo | String | 错误信息。 |

<h3 id="onGetCustomInfo">onGetCustomInfo</h3>

错误回调。

```
void onGetCustomInfo(Map<String, Object> customInfo)
```

