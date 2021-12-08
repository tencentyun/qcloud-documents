## TRTCCalling 简介

[TRTCCalling](https://www.npmjs.com/package/trtc-calling-js) 组件是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1和多人视频/语音通话。具体的实现过程请参见 [实时视频通话（Web）](https://cloud.tencent.com/document/product/647/49789)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。

## TRTCCalling API 

#### 事件订阅/取消订阅相关接口函数 

本组件基于事件分发进行管理，应用层可以根据组件下发的事件进行交互的改变。

| API                                       | 描述         |
| ----------------------------------------- | ------------ |
| [on(eventName, callback, context)](#on)   | 订阅事件     |
| [off(eventName, callback, context)](#off) | 取消事件订阅 |

#### SDK 基础函数

| API                                | 描述                                           |
| ---------------------------------- | ---------------------------------------------- |
| [login({userID, userSig})](#login) | 登录 IM 接口，所有功能需要先进行登录后才能使用 |
| [logout()](#logout)                | 登出接口，登出后无法再进行拨打操作             |

#### 通话操作相关接口函数

| API                                                          | 描述         |
| ------------------------------------------------------------ | ------------ |
| [call({userID, type, offlinePushInfo}))](#call)              | 单人通话邀请 |
| [groupCall({userIDList, type, groupID, offlinePushInfo})](#groupCall) | 群聊通话邀请 |
| [accept()](#accept)                                          | 接受通话邀请 |
| [reject()](#reject)                                          | 拒绝通话邀请 |
| [hangup()](#hangup)                                          | 挂断当前通话 |

#### 视频控制相关接口函数

| API                                                          | 描述                   |
| ------------------------------------------------------------ | ---------------------- |
| [startRemoteView({userID, videoViewDomID})](#startRemoteView) | 启动远端画面渲染       |
| [stopRemoteView({userID})](#stopRemoteView) | 停止远端画面渲染       |
| [startLocalView({userID, videoViewDomID})](#startLocalView) | 启动本地画面渲染       |
| [stopLocalView({userID})](#stopLocalView) | 停止本地画面渲染       |
| [openCamera()](#openCamera)                 | 启动摄像头             |
| [closeCamera()](#closeCamera)              | 关闭摄像头             |
| [setMicMute(isMute)](#setMicMute)     | 设备麦克风是否静音     |
| [setVideoQuality(profile)](#setVideoQuality) | 设置视频质量           |
| [switchToAudioCall()](#switchToAudioCall) | 视频通话切换语音通话   |
| [switchToVideoCall()](#switchToVideoCall) | 语音通话切换视频通话   |
| [getCameras()](#getCameras)                 | 获取摄像头设备列表   |
| [getMicrophones()](#getMicrophones)     | 获取麦克风设备列表   |
| [switchDevice({deviceType, deviceId})](#switchDevice) | 切换摄像头或麦克风设备 |


## TRTCCalling 详解

### 创建 TRTCCalling 组件实例

首先，您需要在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 中创建一个应用，并取得 SDKAppID。
之后，就可以通过 `new TRTCCalling()` 方法获取 TRTCCalling 组件的一个实例。

<dx-codeblock>
::: javascript javascript
let options = {
  SDKAppID: 0, // 接入时需要将0替换为您的即时通信IM应用的 SDKAppID
  // 从v0.10.2起，新增 tim 参数
  // tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
  tim: tim
};
let trtcCalling = new TRTCCalling(options);
:::
</dx-codeblock>

### 事件订阅/取消订阅相关接口函数 

[](id:on)
#### on(eventName, callback, context)

用于监听组件派发的事件，详细事件请参见 [事件表](#event)。

<dx-codeblock>
::: javascript javascript
let handleInvite = function ({inviteID, sponsor, inviteData}) {
    console.log(`inviteID: ${inviteID}, sponsor: ${sponsor}, inviteData: ${JSON.stringify(inviteData)}`);
};
trtcCalling.on('onInvited', handleInvite, this);
:::
</dx-codeblock>



[](id:off)
#### off(eventName, callback, context)

用于取消事件监听。

<dx-codeblock>
::: javascript javascript
let handleInvite = function ({inviteID, sponsor, inviteData}) {
    console.log(`inviteID: ${inviteID}, sponsor: ${sponsor}, inviteData: ${JSON.stringify(inviteData)}`);
};
trtcCalling.off('onInvited', handleInvite, this);
:::
</dx-codeblock>

### SDK 基础函数

[](id:login)
#### login({userID, userSig})

登录接口。

<dx-codeblock>
::: javascript javascript
trtcCalling.login({userID, userSig})
:::
</dx-codeblock>

参数如下表所示：

| 参数    | 类型   | 含义                                                                                                                    |
| ------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| userID  | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。                   |
| userSig | String | 腾讯云设计的一种安全保护签名，获取方式请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |

[](id:logout)
#### logout()

 登出接口。

<dx-codeblock>
::: javascript javascript
trtcCalling.logout()
:::
</dx-codeblock>

### 通话操作相关接口函数

[](id:call)
#### call({userID, type, offlinePushInfo})

1对1通话邀请，其中 type 为通话类型，1-语音通话，2-视频通话。

>?
>- v1.0.0 及其之后版本，取消 timeout 参数。
>- v1.0.0 及其之后版本，新增 offlinePushInfo 参数（**离线推送仅适用于 Android 或 iOS 终端，Web 和微信小程序不支持**）。

<dx-codeblock>
::: javascript javascript
// v1.0.0 之前
trtcCalling.call({userID, type, timeout});

// v1.0.0 版本及其之后
const offlinePushInfo = {
  title: '',
  description: '您有一个通话请求',
}
trtcCalling.call({userID, type, offlinePushInfo})
:::
</dx-codeblock>

参数如下表所示：

| 参数            | 类型   | 含义                                                       |
| --------------- | ------ | ---------------------------------------------------------- |
| userID          | String | 被邀请方 userID                                            |
| type            | Number | 1：语音通话，2：视频通话                                   |
| timeout         | Number | 0为不超时，单位 s（秒）。**仅限于v1.0.0之前的版本**        |
| offlinePushInfo | Object | 自定义离线消息推送（选填)。**仅限于v1.0.0及其之后的版本** |

offlinePushInfo 参数 (仅限于v1.0.0及其之后的版本)

| 参数                 | 类型   | 含义                                                   |
| -------------------- | ------ | ------------------------------------------------------ |
| title                | String | 离线推送标题（选填）                                   |
| description          | String | 离线推送内容（选填)                                    |
| androidOPPOChannelID | String | 离线推送设置 OPPO 手机 8.0 系统及以上的渠道 ID（选填） |
| extension            | String | 离线推送透传内容（选填）。**仅限于TRTCCalling 版本>=1.0.2, tsignaling 版本 >= 0.9.0** |

[](id:groupCall)
#### groupCall({userIDList, type, groupID, offlinePushInfo})
groupID 参数是 IM SDK 中的群组 ID，如果填写该参数，那么通话请求消息是通过群消息系统广播出去的，这种消息广播方式比较简单可靠。如果不填写，那么 TRTCCalling 组件会采用单发消息逐一通知。

>?v1.0.0 及其之后版本，新增 offlinePushInfo 参数（**离线推送仅适用于 Android 或 iOS 终端，Web 和微信小程序不支持**）。

<dx-codeblock>
::: javascript javascript
// v1.0.0之前
trtcCalling.groupCall({userIDList, type, groupID});

// v1.0.0及其之后
const offlinePushInfo = {
  title: '',
  description: '您有一个通话请求',
}
trtcCalling.groupCall({userIDList, type, groupID, offlinePushInfo})
:::
</dx-codeblock>

参数如下表所示：

| 参数            | 类型   | 含义                                                       |
| --------------- | ------ | ---------------------------------------------------------- |
| userIDList      | Array  | 邀请列表                                                   |
| type            | Number | 1：语音通话，2：视频通话                                   |
| groupID         | String | IM 群组 ID（选填）                                         |
| offlinePushInfo | Object | 自定义离线消息推送（选填)。**仅限于v1.0.0及其之后的版本** |

offlinePushInfo 参数 (仅限于v1.0.0及其之后的版本)

| 参数                 | 类型   | 含义                                                   |
| -------------------- | ------ | ------------------------------------------------------ |
| title                | String | 离线推送标题（选填）                                   |
| description          | String | 离线推送内容（选填)                                    |
| androidOPPOChannelID | String | 离线推送设置 OPPO 手机 8.0 系统及以上的渠道 ID（选填） |
| extension            | String | 离线推送透传内容（选填）。**仅限于TRTCCalling 版本>=1.0.2, tsignaling 版本 >= 0.9.0** |

[](id:accept)
#### accept()
当收到邀请后，调用该接口将接受当前的邀请。

>?
>- 当上一个 invitation 未处理完成时，组件会默认占线，之后的邀请都会回复忙线。
>- v1.0.0 及其之后版本，取消 params 参数。

<dx-codeblock>
::: javascript javascript
import TRTCCalling from 'trtc-calling-js';
trtcCalling.on(TRTCCalling.EVENT.INVITED, ({inviteID, sponsor, inviteData}) => {
  // ...
  // v1.0.0之前
  const { roomID, callType } = inviteData;
  trtcCalling.accept({inviteID, roomID, callType})
  // v1.0.0及其之后
  trtcCalling.accept();
})
:::
</dx-codeblock>

参数如下表所示：

| 参数     | 类型   | 含义                                                  |
| -------- | ------ | ----------------------------------------------------- |
| inviteID | String | 邀请 ID，标识一次邀请（监听事件 INVITED 回调数据 inviteID）。**仅限于v1.0.0之前的版本**    |
| roomID   | Number | 通话房间号 ID（监听事件 INVITED 回调数据 inviteData.roomID）。**仅限于v1.0.0之前的版本**            |
| callType | Number | 1：语音通话，2：视频通话（监听事件 INVITED 回调数据 inviteData.callType）。**仅限于v1.0.0之前的版本** |


[](id:reject)
#### reject()
当收到邀请后，调用该接口将拒绝当前的邀请。

>?v1.0.0 及其之后版本，取消 params 参数。

<dx-codeblock>
::: javascript javascript
import TRTCCalling from 'trtc-calling-js';
trtcCalling.on(TRTCCalling.EVENT.INVITED, ({inviteID, sponsor, inviteData}) => {
  // ...
  // v1.0.0之前
  const { callType } = inviteData;
  trtcCalling.reject({inviteID, isBusy, callType})
  // v1.0.0及其以后
  trtcCalling.reject();
})
:::
</dx-codeblock>

参数如下表所示：

| 参数     | 类型    | 含义                                                  |
| -------- | ------- | ----------------------------------------------------- |
| inviteID | String  | 邀请 ID, 标识一次邀请（监听事件 INVITED 回调数据 inviteID）。**仅限于v1.0.0之前的版本**   |
| isBusy   | Boolean | 是否是忙线中。**仅限于v1.0.0之前的版本**             |
| callType | Number  | 1：语音通话，2：视频通话（监听事件 INVITED 回调数据 inviteData.callType）。**仅限于v1.0.0之前的版本** |

[](id:hangup)
#### hangup()
1. 当您处于通话中，可以调用该函数结束通话。
2. 当未拨通时, 可用来取消通话。

<dx-codeblock>
::: javascript javascript
trtcCalling.hangup()
:::
</dx-codeblock>


### 视频控制相关接口函数
[](id:startRemoteView)
#### startRemoteView({userID, videoViewDomID})
将远端用户的摄像头数据渲染到指定的 DOM ID 节点里。

<dx-codeblock>
::: javascript javascript
trtcCalling.startRemoteView({userID, videoViewDomID})
:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                                      |
| -------------- | ------ | --------------------------------------------------------- |
| userID         | String | 用户 ID                                                   |
| videoViewDomID | String | 该用户数据将通过渲染到该 DOM ID 节点的 video 标签进行播放 |

[](id:stopRemoteView)
#### stopRemoteView({userID})
将远端用户的摄像头数据渲染的 DOM 节点删除。

>?v1.0.0 及其之后版本，移除 videoViewDomID 参数。

<dx-codeblock>
::: javascript javascript
// v1.0.0之前
trtcCalling.stopRemoteView({userID, videoViewDomID});
// v1.0.0及其之后
trtcCalling.stopRemoteView({userID});

:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                                         |
| -------------- | ------ | ------------------------------------------------------------ |
| userID         | String | 用户 ID                                                      |
| videoViewDomID | String | 该 DOM ID 节点的 video 标签进行移除，停止播放视频。**仅限于v1.0.0之前的版本** |

[](id:startLocalView)
#### startLocalView({userID, videoViewDomID})
将本地用户的摄像头数据渲染到指定的 DOM ID 节点里。

<dx-codeblock>
::: javascript javascript
trtcCalling.startLocalView({userID, videoViewDomID})
:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                                        |
| -------------- | ------ | ----------------------------------------------------------- |
| userID         | String | 用户 ID                                                     |
| videoViewDomID | String | 本地用户数据将通过渲染到该 DOM ID 节点的 video 标签进行播放 |

[](id:stopLocalView)
#### stopLocalView({userID})

将本地用户的摄像头数据渲染的 DOM 节点删除。

>?v1.0.0 及其之后版本，移除 videoViewDomID 参数。

<dx-codeblock>
::: javascript javascript
// v1.0.0之前
trtcCalling.stopLocalView({userID, videoViewDomID});
// v1.0.0及其之后
trtcCalling.stopLocalView({userID});
:::
</dx-codeblock>

参数如下表所示：

| 参数           | 类型   | 含义                                                         |
| -------------- | ------ | ------------------------------------------------------------ |
| userID         | String | 用户 ID                                                      |
| videoViewDomID | String | 该 DOM ID 节点的 video 标签进行移除，停止播放视频。**仅限于v1.0.0之前的版本** |

[](id:openCamera)
#### openCamera()
开启本地摄像头。

<dx-codeblock>
::: javascript javascript
trtcCalling.openCamera()
:::
</dx-codeblock>

[](id:closeCamera)
####  closeCamera()
关闭摄像头。

<dx-codeblock>
::: javascript javascript
trtcCalling.closeCamera()
:::
</dx-codeblock>

[](id:setMicMute)
####  setMicMute(isMute) 
开启/关闭麦克风。

<dx-codeblock>
::: javascript javascript
trtcCalling.setMicMute(true) // 关闭麦克风
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型    | 含义                                         |
| ------ | ------- | -------------------------------------------- |
| isMute | Boolean | <li/>true：麦克风关闭 <li/>false：麦克风打开 |

[](id:setVideoQuality)
####  setVideoQuality(profile) 
设置视频质量。
>?  
>- v0.8.0 及其之后版本，新增该方法。
>- 此方法需在 call、groupCall、accept 之前设置，之后设置不生效。

<dx-codeblock>
::: javascript javascript
trtcCalling.setVideoQuality('720p') // 设置视频质量为720p
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型    | 含义                                         |
| ------ | ------- | -------------------------------------------- |
| profile | String | <li/>480p：640 × 480 <li/>720p：1280 × 720  <li/>1080p：1920 × 1080  |

[](id:switchToAudioCall)
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

[](id:switchToVideoCall)
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

[](id:getCameras)
####  getCameras() 

您可以调用此接口获取摄像头设备列表。

>?v1.0.0 及其之后版本，新增该方法。

<dx-codeblock>
::: javascript javascript
trtcCalling.getCameras() // 获取摄像头列表
:::
</dx-codeblock>

[](id:getMicrophones)
####  getMicrophones() 

您可以调用此接口获取麦克风设备列表。

>?v1.0.0 及其之后版本，新增该方法。

<dx-codeblock>
::: javascript javascript
trtcCalling.getMicrophones() // 获取麦克风列表
:::
</dx-codeblock>

[](id:switchDevice)
####  switchDevice({deviceType, deviceId})

您可以调用此接口切换摄像头或麦克风设备。

>?v1.0.0 及其之后版本，新增该方法。

<dx-codeblock>
::: javascript javascript
trtcCalling.switchDevice({deviceType: 'video', deviceId: deviceId}) // 切换设备
:::
</dx-codeblock>

参数如下表所示：

| 参数       | 类型   | 含义                                                         |
| ---------- | ------ | ------------------------------------------------------------ |
| deviceType | String | video：摄像头, audio：麦克风                                 |
| deviceId   | String | <li/>摄像头设备标识通过 getCameras() 获取。<li/>麦克风设备标识通过 getMicrophones() 获取 |

[](id:event)
## TRTCCalling 事件表

您可以参考如下代码监听 [TRTCCalling 组件事件](https://web.sdk.qcloud.com/component/trtccalling/doc/web/zh-cn/module-EVENT.html)：

<dx-codeblock>
::: javascript javascript
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
|           [USER_LEAVE](#user_leave)           | 邀请方和被邀方 |      有用户离开通话       |
|             [CALL_END](#call_end)             | 邀请方和被邀方 |       本次通话结束        |
|           [KICKED_OUT](#kicked_out)           | 邀请方和被邀方 |   重复登录，被踢出房间    |
| [USER_VIDEO_AVAILABLE](#user_video_available) | 邀请方和被邀方 | 远端用户开启/关闭了摄像头 |
| [USER_AUDIO_AVAILABLE](#user_audio_available) | 邀请方和被邀方 | 远端用户开启/关闭了麦克风 |

### 通用事件回调

#### SDK_READY

SDK 进入 ready 状态时收到该回调

>?v1.0.0 及其之后版本，新增此事件。

<dx-codeblock>
::: javascript javascript
let onSDKReady = function(event) {
  console.log(event)
};
trtcCalling.on(TRTCCalling.EVENT.SDK_READY, onSDKReady);
:::
</dx-codeblock>

#### USER_ENTER

用户进房。
触发条件：当有用户进入通话。

<dx-codeblock>
::: javascript javascript
let handleUserEnter = function({userID}) {
  console.log(userID)
};
trtcCalling.on(TRTCCalling.EVENT.USER_ENTER, handleUserEnter);
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

#### USER_LEAVE

用户退出房间。
触发条件：当有用户退出通话。

<dx-codeblock>
::: javascript javascript
let handleUserLeave = function({userID}) {
  console.log(userID)
};
trtcCalling.on(TRTCCalling.EVENT.USER_LEAVE, handleUserLeave);
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

#### GROUP_CALL_INVITEE_LIST_UPDATE

群聊更新邀请列表收到该回调

>?v1.0.0 及其之后版本，新增此事件。

<dx-codeblock>
::: javascript javascript
let handleGroupInviteeListUpdate = function(event) {
  console.log(event)
};
trtcCalling.on(TRTCCalling.EVENT.GROUP_CALL_INVITEE_LIST_UPDATE, handleGroupInviteeListUpdate);
:::
</dx-codeblock>

#### CALL_END

本次通话结束。
触发条件：结束本次通话。

<dx-codeblock>
::: javascript javascript
let handleCallingEnd = function(event) {
  console.log(event)
};
trtcCalling.on(TRTCCalling.EVENT.CALL_END, handleCallingEnd);
:::
</dx-codeblock>

#### KICKED_OUT

重复登录，被踢出房间。
触发条件：在其他页面重复登录。

<dx-codeblock>
::: javascript javascript
let handleKickedOut = function(event) {
  console.log(event)
};
trtcCalling.on(TRTCCalling.EVENT.KICKED_OUT, handleKickedOut);
:::
</dx-codeblock>

#### USER_VIDEO_AVAILABLE

远端用户打开关闭摄像头。
触发条件：远端用户打开/关闭摄像头。

<dx-codeblock>
::: javascript javascript
let handleUserVideoChange = function({userID, isVideoAvailable}) {
  console.log(userID, isVideoAvailable)
};
trtcCalling.on(TRTCCalling.EVENT.USER_VIDEO_AVAILABLE, handleUserVideoChange);
:::
</dx-codeblock>

参数如下表所示：

| 参数             | 类型    | 含义                                                        |
| ---------------- | ------- | ----------------------------------------------------------- |
| userID           | String  | 用户 ID                                                     |
| isVideoAvailable | Boolean | <li/>true：远端用户打开摄像头<li/>false：远端用户关闭摄像头 |

#### USER_AUDIO_AVAILABLE

远端用户开启/关闭了麦克风。
触发条件：远端用户开启/关闭了麦克风。

<dx-codeblock>
::: javascript javascript
let handleUserAudioChange = function({userID, isAudioAvailable}) {
  console.log(userID, isAudioAvailable)
};
trtcCalling.on(TRTCCalling.EVENT.USER_AUDIO_AVAILABLE, handleUserAudioChange);
:::
</dx-codeblock>

参数如下表所示：

| 参数             | 类型    | 含义                                                          |
| ---------------- | ------- | ------------------------------------------------------------- |
| userID           | String  | 用户 ID                                                       |
| isAudioAvailable | Boolean | <li/>true：远端用户打开麦克风 <li/> false：远端用户关闭麦克风 |

### 邀请方事件回调

#### REJECT

用户拒绝通话。
触发条件：被邀请方拒绝通话，发起方收到 REJECT 事件回调。

<dx-codeblock>
::: javascript javascript
let handleInviteeReject = function({userID}) {
  console.log(userID)
};
trtcCalling.on(TRTCCalling.EVENT.REJECT, handleInviteeReject);
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

#### NO_RESP

邀请用户无应答。
触发条件：当 call/groupCall 设置 timeout，被邀请方未在 timeout 内未在接听，发起方收到 NO_RESP 事件回调。

<dx-codeblock>
::: javascript javascript
let handleNoResponse = function({userID, userIDList}) {
  console.log(userID, userIDList)
};
trtcCalling.on(TRTCCalling.EVENT.NO_RESP, handleNoResponse);
:::
</dx-codeblock>

参数如下表所示：

| 参数       | 类型   | 含义         |
| ---------- | ------ | ------------ |
| userID     | String | 用户 ID      |
| userIDList | Array  | 超时用户列表 |

#### LINE_BUSY

被邀请方正在通话中，忙线。
触发条件：被邀请方已再另一通话中，发起方收到 LINE_BUSY 事件回调。

<dx-codeblock>
::: javascript javascript
let handleLineBusy = function({userID}) {
  console.log(userID)
};
trtcCalling.on(TRTCCalling.EVENT.LINE_BUSY, handleLineBusy);
:::
</dx-codeblock>

参数如下表所示：

| 参数   | 类型   | 含义    |
| ------ | ------ | ------- |
| userID | String | 用户 ID |

### 被邀请方事件回调

#### INVITED

收到邀请通知。
触发条件：当有邀请通话时，被邀请方收到 INVITED 事件回调。

<dx-codeblock>
::: javascript javascript
let handleNewInvitationReceived = function({
    sponsor, userIDList, isFromGroup, inviteData, inviteID
}) {
  console.log(sponsor, userIDList, isFromGroup, inviteData, inviteID)
};
trtcCalling.on(TRTCCalling.EVENT.INVITED, handleNewInvitationReceived);
:::
</dx-codeblock>

参数如下表所示：

| 参数        | 类型    | 含义                                                                                                       |
| ----------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| sponsor     | String  | 邀请者                                                                                                     |
| userIDList  | Array   | 同时还被邀请的人                                                                                           |
| isFromGroup | Boolean | 是否 IM 群组邀请                                                                                           |
| inviteData  | Object  | <li/>针对新用户邀请： {version, callType, roomID} <li/> 针对最后一位用户挂断：{version, callType, callEnd} |
| inviteID    | String  | 邀请 ID，标识一次邀请                                                                                      |

#### CALLING_CANCEL

本次通话被取消了。
触发条件：发起方在呼叫过程中取消通话，被邀请方收到 CALLING_CANCEL 事件回调。

<dx-codeblock>
::: javascript javascript
let handleCallingCancel = function(event) {
  console.log(event)
};
trtcCalling.on(TRTCCalling.EVENT.CALLING_CANCEL, handleCallingCancel);
:::
</dx-codeblock>

#### CALLING_TIMEOUT

本次通话超时未应答。
触发条件：当 call/groupCall 设置 timeout，被邀请方未在 timeout 内未在接听，被邀请方收到 CALLING_TIMEOUT 事件回调。

<dx-codeblock>
::: javascript javascript
let handleCallingTimeout = function(event) {
  console.log(event)
};
trtcCalling.on(TRTCCalling.EVENT.CALLING_TIMEOUT, handleCallingTimeout);
:::
</dx-codeblock>

## TRTCCalling 错误码表

您可以通过监听 EVENT 里的 ERROR 字段，对组件抛出的错误进行处理，示例代码如下：

<dx-codeblock>
::: javascript javascript
import TRTCCalling from 'trtc-calling-js';
let onError = function(error) {
  console.log(error)
};
trtcCalling.on(TRTCCalling.EVENT.ERROR, onError);
:::
</dx-codeblock>

#### Error code 码

| code  | 错误类型     | 含义                       |
| ----- | ------------ | -------------------------- |
| 60001 | 方法调用失败 | switchToAudioCall 调用失败 |
| 60002 | 方法调用失败 | switchToVideoCall 调用失败 |
| 60003 | 权限获取失败 | 没有可用的麦克风设备       |
| 60004 | 权限获取失败 | 没有可用的摄像头设备       |
| 60005 | 权限获取失败 | 用户禁止使用设备           |

## 常见问题

#### 为什么拨打不通，或者被踢下线？
组件暂不支持多实例登入，不支持**离线推送信令**功能，请您确认登入账号的唯一性。
> ?
> - **多实例**：一个 UserID 重复登入，或在不同端登入，将会引起信令的混乱。
> - **离线推送**：实例在线才能接收消息，实例离线时接收到的信令不会在上线后重新推送。
