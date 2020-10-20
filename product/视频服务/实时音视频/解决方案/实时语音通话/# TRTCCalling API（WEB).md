# TRTCCalling API（WEB)

## 简介
[TRTCCalling](https://www.npmjs.com/package/trtc-calling-js)组件，是基于[腾讯云实时音视频 TRTC](https://cloud.tencent.com/product/trtc/)、[腾讯云信令 TSignalling](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tsignaling/TSignaling.html) 组合而成，支持1v1、多人场景下的语音、视频通话，并封装了简单易用的 [API](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/trtc-calling-js-doc/TRTCCalling.html)，接入后可快速实现服务线上客服、医疗问诊、跨端实时通话等应用场景。

## TRTCCalling API 概览

#### 事件订阅/取消订阅相关接口函数 

本组件基于事件分发进行管理，应用层可以根据组件下发的事件进行交互的改变。

| API                                       | 描述         |
| ----------------------------------------- | ------------ |
| [on(eventName, callback, context)](#on)   | 订阅事件     |
| [off(eventName, callback, context)](#off) | 取消事件订阅 |
#### SDK 基础函数
| API                         | 描述                                         |
| --------------------------- | -------------------------------------------- |
| [login(params)](#login)     | 登录IM接口，所有功能需要先进行登录后才能使用 |
| [logout(callback)](#logout) | 登出接口，登出后无法再进行拨打操作           |

#### 通话操作相关接口函数
| API                             | 描述                                |
| ------------------------------- | ----------------------------------- |
| [call(params))](#off)           | 单人通话邀请                        |
| [groupCall(params)](#groupCall) | 群聊通话邀请（请先创建IM群组）      |
| [accept(params)](#accept)       | 接受通话邀请                        |
| [reject(params)](#reject)       | 拒绝通话邀请                        |
| [hangup(params)](#hangup)       | 1、结束当前通话 2、未拨通时取消通话 |

#### 音视频控制相关接口函数 
| API                                         | 描述             |
| ------------------------------------------- | ---------------- |
| [startRemoteView(params)](#startRemoteView) | 开启远端画面渲染 |
| [stopRemoteView(params)](#stopRemoteView)   | 关闭远端画面渲染 |
| [startLocalView(params)](#startLocalView)   | 开启本地画面渲染 |
| [stopLocalView(params)](#stopLocalView)     | 关闭本地画面渲染 |
| [openCamera()](#openCamera)                 | 开启摄像头       |
| [closeCamera()](#closeCamera)               | 关闭摄像头       |
| [setMicMute(isMute)](#setMicMute)           | 麦克风是否静音   |


#
腾讯云 TRTCCalling SDK 入口类。
接入前，您需要在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 中创建一个云通信应用，并取得 SDKAppID。

#### 参数类型
| 参数     | 类型   | 含义                                                                                                                  |
| -------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| sdkAppID | Number | 您可以在实时音视频控制台 >[应用管理](https://console.cloud.tencent.com/trtc/app)> 应用信息中查看 SDKAppID             |
| userID   | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）                    |
| userSig  | String | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275) |

#### TRTCCalling

您可以通过组件提供的 TRTCCalling.create() 方法获取 SDK 实例。

```javascript
let options = {
  SDKAppID: 0 // 接入时需要将0替换为您的云通信应用的 SDKAppID
};
let trtcCalling = TRTCCalling.create(options);
```
### 事件订阅/取消订阅相关接口函数 

<span id="on"></span>
#### on(eventName, callback, context)

用于监听组件派发的事件，详细事件请参考 [事件表](#event)。


<span id="off"></span>

#### off(eventName, callback, context)

用于取消事件监听。

### SDK 基础函数

<span id="login"></span>
#### login(params)
登录接口

```javascript
trtcCalling.login({sdkAppID, userID, userSig, callback})
```
<span id="logout"></span>
#### logout()
 登出接口
```javascript
trtcCalling.logout(callback)
```


### 通话操作相关接口函数

<span id="call"></span>

#### call(params)

C2C邀请通话，其中type为通话类型，1-语音通话，2-视频通话

```javascript
trtcCalling.call({userID, type, timeout})
```
<span id="groupCall"></span>

#### groupCall(params)

在调用该接口前需要使用IM创建群组，并将groupID作为参数传入

```javascript
trtcCalling.groupCall({userIDList, type, groupID})
```
<span id="accept"></span>

#### accept(params)

当收到邀请后，调用该接口将接受当前的邀请。

> 当上一个invitation未处理完成时，组件会默认占线，之后的邀请都会回复忙线。

```javascript
trtcCalling.on(EVENT.INVITED, () => {
  trtcCalling.accept({inviteID, roomID, callType})
})
```
<span id="reject"></span>

#### reject()

当收到邀请后，调用该接口将拒绝当前的邀请。

```javascript
trtcCalling.on(EVENT.INVITED, () => {
  trtcCalling.reject({inviteID, isBusy})
})
```

<span id="hangup"></span>

#### hangup(params)  

1、当您处于通话中，可以调用该函数结束通话

2、当未拨通时, 可用来取消通话
```javascript
trtcCalling.hangup(status)
```

### 音视频控制相关接口函数 

<span id="startRemoteView"></span>

#### startRemoteView(params) 

调用该函数将远端用户的摄像头数据渲染到指定的 dom id 节点里
```javascript
trtcCalling.startRemoteView({userID, videoViewDomID})
```

<span id="stopRemoteView"></span>

#### stopRemoteView(params) 

调用该函数将远端用户的摄像头数据渲染的 dom 节点删除
```javascript
trtcCalling.stopRemoteView({userID, videoViewDomID})
```

<span id="startLocalView"></span>

#### startLocalView(params) 

调用该函数将本地用户的摄像头数据渲染到指定的 dom id 节点里
```javascript
trtcCalling.startLocalView({userID, videoViewDomID})
```

<span id="stopLocalView"></span>

#### stopLocalView(params) 

调用该函数将本地用户的摄像头数据渲染的 dom 节点删除
```javascript
trtcCalling.stopLocalView({userID, videoViewDomID})
```

<span id="openCamera"></span>

#### openCamera()

开启本地摄像头
```javascript
trtcCalling.openCamera()
```
<span id="closeCamera"></span>

####  closeCamera()

关闭摄像头
```javascript
trtcCalling.closeCamera()
```
<span id="setMicMute"></span>

####  setMicMute(isMute) 

isMute true:麦克风关闭 false:麦克风打开  
```javascript
trtcCalling.setMicMute(true) // 开启麦克风
```

<span id="event"></span>

## 事件表

### 邀请方事件
| CODE      | 说明                     |
| --------- | ------------------------ |
| REJECT    | 用户拒绝通话             |
| NO_RESP   | 邀请用户无应答           |
| LINE_BUSY | 被邀请方正在通话中，忙线 |

### 被邀请方事件

| CODE            | 说明               |
| --------------- | ------------------ |
| INVITED         | 收到邀请通知       |
| CALLING_CANCEL  | 本次通话被取消了   |
| CALLING_TIMEOUT | 本次通话超时未应答 |

### 通用事件
| CODE                           | 说明                                                   |
| ------------------------------ | ------------------------------------------------------ |
| USER_ENTER                     | 用户进房                                               |
| USER_LEAVE                     | 用户退出房间                                           |
| CALL_END                       | 本次通话结束                                           |
| KICKED_OUT                     | 重复登录，被踢出房间                                   |
| USER_VOICE_VOLUME              | 远端用户音量调整                                       |
| USER_VIDEO_AVAILABLE           | 远端用户开启/关闭了摄像头                              |
| USER_AUDIO_AVAILABLE           | 远端用户开启/关闭了麦克风                              |
| GROUP_CALL_INVITEE_LIST_UPDATE | 正在IM群组通话时，如果其他与会者邀请他人，会收到此回调 |

## 错误表

通过监听EVENT里的ERROR字段，对组件抛出的错误进行处理。

```javascript
let onError = function(error) {
  console.log(error)
};
trtcCalling.on(TRTCCalling.EVENT.ERROR, onError);
```




## 常见问题
1、为什么拨打不通，或者被踢下线？
组件暂不支持多实例登入，不支持**离线推送信令**功能，请您确认账号登入的唯一性。

> 多实例：一个userID重复登入，或在不同端登入，将会引起信令的混乱。
> 
> 离线推送：实例在线才能接收消息，实例离线时接收到的信令不会在上线后重新推送。