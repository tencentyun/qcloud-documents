## TRTCCalling 简介

[TRTCCalling](https://www.npmjs.com/package/trtc-calling-js) 组件是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1和多人视频/语音通话。具体的实现过程请参见 [实时语音通话（Web）](https://cloud.tencent.com/document/product/647/49795)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。

## TRTCCalling API 

#### 事件订阅/取消订阅相关接口函数 
本组件基于事件分发进行管理，应用层可以根据组件下发的事件进行交互的改变。

| API                                                                         | 描述         |
| --------------------------------------------------------------------------- | ------------ |
| [on(eventName, callback, context)](#on(eventname.2C-callback.2C-context))   | 订阅事件     |
| [off(eventName, callback, context)](#off(eventname.2C-callback.2C-context)) | 取消事件订阅 |

#### SDK 基础函数

| API                                                         | 描述                                           |
| ----------------------------------------------------------- | ---------------------------------------------- |
| [login({userID, userSig})](#login(.7Buserid.2C-usersig.7D)) | 登录 IM 接口，所有功能需要先进行登录后才能使用 |
| [logout()](#logout())                                       | 登出接口，登出后无法再进行拨打操作             |

#### 通话操作相关接口函数
| API                                                                                       | 描述         |
| ----------------------------------------------------------------------------------------- | ------------ |
| [call({userID, type, timeout}))](#call(.7Buserid.2C-type.2C-timeout.7D))                  | 单人通话邀请 |
| [groupCall({userIDList, type, groupID})](#groupcall(.7Buseridlist.2C-type.2C-groupid.7D)) | 群聊通话邀请 |
| [accept({inviteID, roomID, callType})](#accept(.7Binviteid.2C-roomid.2C-calltype.7D))     | 接受通话邀请 |
| [reject({inviteID, isBusy, callType})](#reject(.7Binviteid.2C-isbusy.2C-calltype.7D))     | 拒绝通话邀请 |
| [hangup()](#hangup())                                                                     | 挂断当前通话 |

#### 视频控制相关接口函数
| API                                                                                           | 描述               |
| --------------------------------------------------------------------------------------------- | ------------------ |
| [startRemoteView({userID, videoViewDomID})](#startremoteview(.7Buserid.2C-videoviewdomid.7D)) | 启动远端画面渲染   |
| [stopRemoteView({userID, videoViewDomID})](#stopremoteview(.7Buserid.2C-videoviewdomid.7D))   | 停止远端画面渲染   |
| [startLocalView({userID, videoViewDomID})](#startlocalview(.7Buserid.2C-videoviewdomid.7D))   | 启动本地画面渲染   |
| [stopLocalView({userID, videoViewDomID})](#stoplocalview(.7Buserid.2C-videoviewdomid.7D))     | 停止本地画面渲染   |
| [openCamera()](#opencamera())                                                                 | 启动摄像头         |
| [closeCamera()](#closecamera())                                                               | 关闭摄像头         |
| [setMicMute(isMute)](#setmicmute(ismute))                                                     | 设备麦克风是否静音 |
| [setVideoQuality(profile)](#setvideoquality(profile) ) |   设置视频质量 |
| [switchToAudioCall()](#switchtoaudiocall()) | 视频通话切换语音通话|
| [switchToVideoCall()](#switchtovideocall()) | 语音通话切换视频通话|

## TRTCCalling 详解

### 创建 TRTCCalling 组件实例

首先，您需要在实时音视频 [控制台](https://console.cloud.tencent.com/trtc/app) 中创建一个应用，并取得 SDKAppID。
之后，就可以通过 `new TRTCCalling()` 方法获取 TRTCCalling 组件的一个实例。

<dx-codeblock>
:::  javascript javascript
let options = {
  SDKAppID: 0 // 接入时需要将0替换为您的即时通信 IM 应用的 SDKAppID
};
let trtcCalling = new TRTCCalling(options);
:::
</dx-codeblock>

### 事件订阅/取消订阅相关接口函数 



#### on(eventName, callback, context)
用于监听组件派发的事件，详细事件请参见 [事件表](#event)。

<dx-codeblock>
:::  javascript javascript
let handleInvite = function ({inviteID, sponsor, inviteData}) {
    console.log(`inviteID: ${inviteID}, sponsor: ${sponsor}, inviteData: ${JSON.stringify(inviteData)}`);
};
trtcCalling.on('onInvited', handleInvite, this);
:::
</dx-codeblock>



#### off(eventName, callback, context)
用于取消事件监听。

<dx-codeblock>
:::  javascript javascript
let handleInvite = function ({inviteID, sponsor, inviteData}) {
    console.log(`inviteID: ${inviteID}, sponsor: ${sponsor}, inviteData: ${JSON.stringify(inviteData)}`);
};
trtcCalling.off('onInvited', handleInvite, this);
:::
</dx-codeblock>

### SDK 基础函数



#### login({userID, userSig})
登录接口。

<dx-codeblock>
:::  javascript javascript
trtcCalling.login({userID, userSig})
:::
</dx-codeblock>

参数如下表所示：

| 参数    | 类型   | 含义                                                                                                                    |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| userID  | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。                   |
| userSig | String | 腾讯云设计的一种安全保护签名，获取方式请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |



#### logout()
 登出接口。
<dx-codeblock>
:::  javascript javascript
trtcCalling.logout()
:::
</dx-codeblock>

### 通话操作相关接口函数



#### call({userID, type, timeout})

1对1通话邀请，其中 type 为通话类型，1-语音通话，2-视频通话。

<dx-codeblock>
:::  javascript javascript
trtcCalling.call({userID, type, timeout})
:::
</dx-codeblock>

参数如下表所示：

| 参数    | 类型   | 含义                     |
| ------- | ------ | ------------------------ |
| userID  | String | 被邀请方 userID          |
| type    | Number | 1：语音通话，2：视频通话 |
| timeout | Number | 0为不超时, 单位 s（秒）    |



#### groupCall({userIDList, type, groupID})
groupID 参数是 IM SDK 中的群组 ID，如果填写该参数，那么通话请求消息是通过群消息系统广播出去的，这种消息广播方式比较简单可靠。如果不填写，那么 TRTCCalling 组件会采用单发消息逐一通知。

<dx-codeblock>
:::  javascript javascript
trtcCalling.groupCall({userIDList, type, groupID})
:::
</dx-codeblock>

参数如下表所示：

| 参数       | 类型   | 含义                     |
| ---------- | ------ | ------------------------ |
| userIDList | Array  | 邀请列表                 |
| type       | Number | 1：语音通话，2：视频通话 |
| groupID    | String | IM 群组 ID （选填）      |


#### accept({inviteID, roomID, callType})
当收到邀请后，调用该接口将接受当前的邀请。
>? 当上一个 invitation 未处理完成时，组件会默认占线，之后的邀请都会回复忙线。

<dx-codeblock>
:::  javascript javascript
import TRTCCalling from 'trtc-calling-js';
trtcCalling.on(TRTCCalling.EVENT.INVITED, ({inviteID, sponsor, inviteData}) => {
  // ...
  trtcCalling.accept({inviteID, roomID, callType})
})
:::
</dx-codeblock>

参数如下表所示：

| 参数     | 类型   | 含义                     |
| -------- | ------ | ------------------------ |
| inviteID | String | 邀请 ID，标识一次邀请    |
| roomID   | Number | 通话房间号 ID            |
| callType | Number | 1：语音通话，2：视频通话 |


#### reject({inviteID, isBusy, callType})
当收到邀请后，调用该接口将拒绝当前的邀请。

<dx-codeblock>
:::  javascript javascript
import TRTCCalling from 'trtc-calling-js';
trtcCalling.on(TRTCCalling.EVENT.INVITED, ({inviteID, sponsor, inviteData}) => {
  // ...
  trtcCalling.reject({inviteID, isBusy, callType})
})
:::
</dx-codeblock>

参数如下表所示：

| 参数     | 类型    | 含义                     |
| -------- | ------- | ------------------------ |
| inviteID | String  | 邀请 ID，标识一次邀请    |
| isBusy   | Boolean | 是否是忙线中             |
| callType | Number  | 1：语音通话，2：视频通话 |



#### hangup()
1. 当您处于通话中，可以调用该函数结束通话。
2. 当未拨通时, 可用来取消通话。

<dx-codeblock>
:::  javascript javascript
trtcCalling.hangup()
:::
</dx-codeblock>


### 视频控制相关接口函数


#### startRemoteView({userID, videoViewDomID})
将远端用户的摄像头数据渲染到指定的 DOM ID 节点里。
<dx-codeblock>
:::  javascript javascript
trtcCalling.startRemoteView({userID, videoViewDomID})
:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                                      |
| -------------- | ------ | --------------------------------------------------------- |
| userID         | String | 用户 ID                                                   |
| videoViewDomID | String | 该用户数据将通过渲染到该 DOM ID 节点的 video 标签进行播放 |


#### stopRemoteView({userID, videoViewDomID})
将远端用户的摄像头数据渲染的 DOM 节点删除。
<dx-codeblock>
:::  javascript javascript
trtcCalling.stopRemoteView({userID, videoViewDomID})
:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                              |
| -------------- | ------ | ------------------------------------------------- |
| userID         | String | 用户 ID                                           |
| videoViewDomID | String | 该 DOM ID 节点的 video 标签进行移除, 停止播放视频 |


#### startLocalView({userID, videoViewDomID})
将本地用户的摄像头数据渲染到指定的 DOM ID 节点里。
<dx-codeblock>
:::  javascript javascript
trtcCalling.startLocalView({userID, videoViewDomID})
:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                                        |
| -------------- | ------ | ----------------------------------------------------------- |
| userID         | String | 用户 ID                                                     |
| videoViewDomID | String | 本地用户数据将通过渲染到该 DOM ID 节点的 video 标签进行播放 |


#### stopLocalView({userID, videoViewDomID})
将本地用户的摄像头数据渲染的 DOM 节点删除。
<dx-codeblock>
:::  javascript javascript
trtcCalling.stopLocalView({userID, videoViewDomID})
:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                              |
| -------------- | ------ | ------------------------------------------------- |
| userID         | String | 用户 ID                                           |
| videoViewDomID | String | 该 DOM ID 节点的 video 标签进行移除, 停止播放视频 |


#### openCamera()
开启本地摄像头。
<dx-codeblock>
:::  javascript javascript
trtcCalling.openCamera()
:::
</dx-codeblock>


####  closeCamera()
关闭摄像头。
<dx-codeblock>
:::  javascript javascript
trtcCalling.closeCamera()
:::
</dx-codeblock>


####  setMicMute(isMute) 
开启/关闭麦克风。
<dx-codeblock>
:::  javascript javascript
trtcCalling.setMicMute(true) // 开启麦克风
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型    | 含义                                          |
| ------ | ------- | --------------------------------------------- |
| isMute | Boolean | <li/>true：麦克风关闭 <li/> false：麦克风打开 |

####  setVideoQuality(profile) 
设置视频质量。
>? 
- v0.8.0 及其之后版本，新增该方法。
- 此方法需在 call、groupCall、accept 之前设置，之后设置不生效。

<dx-codeblock>
::: javascript javascript
trtcCalling.setVideoQuality('720p') // 设置视频质量为720p
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型    | 含义                                         |
| ------ | ------- | -------------------------------------------- |
| profile | String | <li/>480p：640 × 480 <li/>720p：1280 × 720  <li/>1080p：1920 × 1080  |

####  switchToAudioCall() 
视频通话切换语音通话。
>?  
>- v0.10.0 及其之后版本，新增该方法。
>- 仅支持1v1通话过程中使用。
>- 失败监听 ERROR 事件，code：60001。

<dx-codeblock>
::: javascript javascript
trtcCalling.switchToAudioCall() // 视频通话切换语音通话
:::
</dx-codeblock>

####  switchToVideoCall() 
语音通话切换视频通话。
>?  
>- v0.10.0 及其之后版本，新增该方法。
>- 仅支持1v1通话过程中使用。
>- 失败监听 ERROR 事件，code：60002。

<dx-codeblock>
::: javascript javascript
trtcCalling.switchToVideoCall() // 语音通话切换视频通话
:::
</dx-codeblock>


[](id:event)
## TRTCCalling 事件表
您可以参考如下代码监听 [TRTCCalling 组件事件](https://web.sdk.qcloud.com/component/trtccalling/doc/web/zh-cn/module-EVENT.html)：

<dx-codeblock>
:::  javascript javascript
import TRTCCalling from 'trtc-calling-js';
// etc
function handleInviteeReject({userID}) {

}
trtcCalling.on(TRTCCalling.EVENT.REJECT, handleInviteeReject)
:::
</dx-codeblock>

### 邀请方事件
|                     CODE                      |   事件接收方   |           说明            |
| :-------------------------------------------: | :------------: | :-----------------------: |
|               [REJECT](#reject)               |     邀请方     |     被邀用户拒绝通话      |
|              [NO_RESP](#no_resp)              |     邀请方     |    被邀用户超时无应答     |
|            [LINE_BUSY](#line_busy)            |     邀请方     | 被邀用户正在通话中，忙线  |
|              [INVITED](#invited)              |     被邀方     |      收到了邀请通知       |
|       [CALLING_CANCEL](#calling_cancel)       |     被邀方     |     本次通话被取消了      |
|      [CALLING_TIMEOUT](#calling_timeout)      |     被邀方     |    本次通话超时未应答     |
|           [USER_ENTER](#user_enter)           | 邀请方和被邀方 |         用户进房          |
|           [USER_LEAVE](#user_leave)           | 邀请方和被邀方 |       用户退出房间        |
|             [CALL_END](#call_end)             | 邀请方和被邀方 |       本次通话结束        |
|           [KICKED_OUT](#kicked_out)           | 邀请方和被邀方 |   重复登录，被踢出房间    |
| [USER_VIDEO_AVAILABLE](#user_video_available) | 邀请方和被邀方 | 远端用户开启/关闭了摄像头 |
| [USER_AUDIO_AVAILABLE](#user_audio_available) | 邀请方和被邀方 | 远端用户开启/关闭了麦克风 |

### 通用事件回调

#### USER_ENTER
用户进房。

<dx-codeblock>
:::  javascript javascript
function handleUserEnter({userID}) {

}
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

#### USER_LEAVE
用户退出房间。

<dx-codeblock>
:::  javascript javascript
function handleUserLeave({userID}) {

}
:::
</dx-codeblock>
参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

#### CALL_END
本次通话结束。

<dx-codeblock>
:::  javascript javascript
function handleCallEnd() {

}
:::
</dx-codeblock>

#### KICKED_OUT
重复登录，被踢出房间。

<dx-codeblock>
:::  javascript javascript
function handleKickedOut() {

}
:::
</dx-codeblock>

#### USER_VIDEO_AVAILABLE
远端用户打开关闭摄像头。

<dx-codeblock>
:::  javascript javascript
function handleUserVideoChange({userID, isVideoAvailable}) {

}
:::
</dx-codeblock>

参数如下表所示：

| 参数             | 类型    | 含义                                                          |
| ---------------- | ------- | ------------------------------------------------------------- |
| userID           | String  | 用户 ID                                                       |
| isVideoAvailable | Boolean | <li/>true：远端用户打开摄像头 <li/> false：远端用户关闭摄像头 |

#### USER_AUDIO_AVAILABLE
远端用户开启/关闭了麦克风。

<dx-codeblock>
:::  javascript javascript
function handleUserAudioChange({userID, isAudioAvailable}) {

}
:::
</dx-codeblock>

参数如下表所示：

| 参数             | 类型    | 含义                                                           |
| ---------------- | ------- | -------------------------------------------------------------- |
| userID           | String  | 用户 ID                                                        |
| isAudioAvailable | Boolean | <li/>true：远端用户打开麦克风  <li/> false：远端用户关闭麦克风 |

### 邀请方事件回调

#### REJECT
用户拒绝通话。

<dx-codeblock>
:::  javascript javascript
function handleInviteeReject({userID}) {

}
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

#### NO_RESP
邀请用户无应答。

<dx-codeblock>
:::  javascript javascript
function handleNoResponse({userID, userIDList}) {

}
:::
</dx-codeblock>

参数如下表所示：

| 参数       | 类型   | 含义         |
| ---------- | ------ | ------------ |
| userID     | String | 用户 ID      |
| userIDList | Array  | 超时用户列表 |

#### LINE_BUSY
被邀请方正在通话中，忙线。

<dx-codeblock>
:::  javascript javascript
function handleInviteeLineBusy({userID}) {

}
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

### 被邀请方事件回调

#### INVITED
收到邀请通知。

<dx-codeblock>
:::  javascript javascript
function handleNewInvitationReceived({
    sponsor, userIDList, isFromGroup, inviteData, inviteID
}) {

}
:::
</dx-codeblock>

参数如下表所示：

| 参数        | 类型    | 含义                                                                                                     |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------- |
| sponsor     | String  | 邀请者                                                                                                   |
| userIDList  | Array   | 同时还被邀请的人                                                                                         |
| isFromGroup | Boolean | 是否 IM 群组邀请                                                                                         |
| inviteData  | Object  | <li/>针对新用户邀请： {version, callType, roomID}<li/>针对最后一位用户挂断：{version, callType, callEnd} |
| inviteID    | String  | 邀请 ID，标识一次邀请                                                                                    |

#### CALLING_CANCEL
本次通话被取消了。

<dx-codeblock>
:::  javascript javascript
function handleInviterCancel() {

}
:::
</dx-codeblock>

#### CALLING_TIMEOUT
本次通话超时未应答。

<dx-codeblock>
:::  javascript javascript
function handleCallTimeout() {

}
:::
</dx-codeblock>

## TRTCCalling 错误码表

您可以通过监听 EVENT 里的 ERROR 字段，对组件抛出的错误进行处理，示例代码如下：

<dx-codeblock>
:::  javascript javascript
import TRTCCalling from 'trtc-calling-js';
let onError = function(error) {
  console.log(error)
};
trtcCalling.on(TRTCCalling.EVENT.ERROR, onError);
:::
</dx-codeblock>

#### Error code 码
| code      | 错误类型    | 含义                        |
| --------- | ----------- | ----------------------------- |
| 60001     | 方法调用失败  | switchToAudioCall 调用失败   ｜
| 60002     | 方法调用失败  | switchToVideoCall 调用失败   ｜


## 常见问题
#### 为什么拨打不通，或者被踢下线？
组件暂不支持多实例登入，不支持**离线推送信令**功能，请您确认登入账号的唯一性。
> ?
>-  **多实例**：一个 UserID 重复登入，或在不同端登入，将会引起信令的混乱。
>-  **离线推送**：实例在线才能接收消息，实例离线时接收到的信令不会在上线后重新推送。
