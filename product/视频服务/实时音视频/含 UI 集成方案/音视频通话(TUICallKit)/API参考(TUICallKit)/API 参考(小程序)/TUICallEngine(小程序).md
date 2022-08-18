## TUICallEngine API 简介

TUICallEngine API 是音视频通话组件的**无 UI 接口**，如果 TUICallKit 的交互并不满足您的需求，您可以使用这套接口自己封装交互。
由于小程序开发的限制，需要先给live-pusher[绑定事件](#bind)，具体可以参照[TUICallkit](https://cloud.tencent.com/document/product/647/78760?!preview)。

[](id:TUICallEngine)
## API 概览

### 创建实例和事件回调

| API | 描述 |
|-----|-----|
| [createInstance](#createinstance)   | 创建 TUICallEngine 实例（静态方法）|
| [destroyInstance](#destroyinstance) | 销毁 TUICallEngine 实例（静态方法）|
| [on](#on)                           | 增加事件监听|
| [off](#off)                         | 取消事件监听|


### 通话操作相关接口函数

| API | 描述 |
|-----|-----|
| [call](#call)                               | 发起 1v1 通话                            |
| [accept](#accept)                           | 接听通话                                 |
| [reject](#reject)                           | 拒绝通话                                 |
| [hangup](#hangup)                           | 结束通话                                 |
| [switchCallMediaType](#switchcallmediatype) | 切换通话媒体类型，比如视频通话切音频通话 |


### 设备控制相关接口函数

| API | 描述 |
|-----|-----|
| [openCamera](#opencamera)                               | 开启摄像头                      |
| [closeCamera](#closecamera)                             | 关闭摄像头                      |
| [switchCamera](#switchcamera)                           | 切换前后摄像头                  |
| [openMicrophone](#openmicrophone)                       | 打开麦克风                      |
| [closeMicrophone](#closemicrophone)                     | 关闭麦克风                      |
| [selectAudioPlaybackDevice](#selectaudioplaybackdevice) | 选择音频播放设备（听筒/扬声器） |

### 其他接口函数

| API | 描述 |
|-----|-----|
| [setSelfInfo](#setselfinfo) | 设置用户的头像、昵称 |

[](id:TUICallEngine)

## API 详情
### createInstance
创建 TUICallEngine 的单例（class 上的 static 方法）：
```javascript
TUICallEngine.createInstance({
    sdkAppID:'xxxxxxx',
    tim,
})
```

**说明**

| 参数 | 是否必传 | 说明 |
|-----|-----|-----|
| sdkAppID | 必传 | SDKAppId 是腾讯云用于区分客户的唯一标识 |
| tim | 非必传 | TIM 是 IM Web SDK 的命名空间，提供了创建 SDK 实例的静态方法 |


[](id:destroyInstance)
### destroyInstance
销毁 TUICallEngine 的单例（class 上的 static 方法）：
```javascript
TUICallEngine.destroyInstance()
```

### on
添加回调接口，您可以通过这个接听，监听 TRTC 相关的事件回调。
```javascript
on(EventCode, handler, context);
```

**说明**

| 参数 | 类型 | 说明 |
|-----|-----|-----|
| Eventlist | String | [事件表](#evenlist) |
| handler | Function | 监听函数 |
| context | Object | 当前执行上下文 |

### off
移除回调接口。
```javascript
off(EventCode, handler);
```
**说明**

| 参数 | 类型 | 说明 |
|-----|-----|-----|
| EventCode | String | [事件表](#evenlist) |
| handler | Function | 监听函数 |


### call
C2C邀请通话，被邀请方会收到的回调，如果当前处于通话中，可以调用该函数以邀请第三方进入通话。

```javascript
call({
    userID:"xxxxxxx",
    type:MEDIA_TYPE.AUDIO
})
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 目标用户的 userId |
| type | [MEDIA_TYPE](#MEDIA_TYPE) | 通话的媒体类型，AUDIO：语音通话，VIDEO：视频通话 |


### accept
当您作为被邀请方收到的回调时，可以调用该函数接听来电。

```javascript
accept();
```

### reject
当您作为被邀请方收到的回调时，可以调用该函数拒绝来电。

```javascript
reject();
```

### hangup
- 当您处于通话中，可以调用该函数挂断通话
- 当您发起通话时，可用去了取消通话

```javascript
hangup();
```

### switchCallMediaType
切换通话媒体类型，比如视频通话切音频通话。

```javascript
switchCallMediaType(MEDIA_TYPE.VIDEO);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type| [MEDIA_TYPE](#MEDIA_TYPE)  |通话的媒体类型，AUDIO-语音通话，VIDEO-视频通话 |

### openCamera
您可以调用该函数开启摄像头。

```javascript
openCamera();
```

### closeCamera
您可以调用该函数关闭摄像头，处于通话中的用户会收到回调。

```javascript
closeCamera();
```

### switchCamera
切换前后摄像头。

```javascript
switchCamera();
```

### openMicrophone
您可以调用该函数打开麦克风，处于通话中的用户会收到回调。

```javascript
openMicrophone();
```

### closeMicrophone
您可以调用该函数关闭麦克风，处于通话中的用户会收到回调。

```javascript
closeMicrophone();
```

### selectAudioPlaybackDevice
选择音频播放设备，目前支持听筒、扬声器，在通话场景中，可以使用这个接口来开启/关闭免提模式

```javascript
selectAudioPlaybackDevice(AUDIO_PLAYBACK_DEVICE.EAR);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | [AUDIO_PLAYBACK_DEVICE](#AUDIO_PLAYBACK_DEVICE)| speaker：扬声器，ear：听筒 |

### setSelfInfo
设置用户头像、昵称的接口。

```javascript
setSelfInfo('xxxxxxx','头像.png') ;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nickName | String | 设置昵称 |
| avatar | String | 头像地址 |

[](id:evenlist)
## 事件表

| 事件名 | 说明 |
|-----|-----|
| [INVITED](#invited)                 | 被邀请通话     |
| [USER_ACCEPT](#user_accept)         | 用户接听       |
| [USER_ENTER](#user_enter)           | 用户进入通话   |
| [USER_LEAVE](#user_leave)           | 用户离开通话   |
| [USER_UPDATE](#user_update)         | 用户更新       |
| [REJECT](#reject)                   | 用户拒绝通话   |
| [NO_RESP](#no_resp)                 | 用户无响应     |
| [LINE_BUSY](#line_busy)             | 用户忙线       |
| [CALLING_CANCEL](#calling_cancel)   | 通话被取消     |
| [CALLING_TIMEOUT](#calling_timeout) | 通话超时未应答 |
| [CALL_END](#call_end)               | 通话结束       |
| [SDK_READY](#sdk_ready)             | SDK Ready 回调 |
| [KICKED_OUT](#kicked_out)           | 被踢下线       |
| [CALL_MODE](#call_mode)             | 切换通话模式   |

### INVITED
被邀请通话。
```javascript
let handleNewInvitationReceived = function(event){
    console.log('被邀请通话')
  }
tuiCallEngine.on(EVENT.INVITED, this.handleNewInvitationReceived, this);
```

### USER_ACCEPT
用户接听。
```javascript
let handleUserAccept = function(event) {
    console.log('用户接听')
}
tuiCallEngine.on(EVENT.USER_ACCEPT, this.handleUserAccept, this);
```

### USER_ENTER
用户进入通话。
```javascript
let handleUserEnter = function(event) {
    console.log('用户进入通话')
}
tuiCallEngine.on(EVENT.USER_ENTER, this.handleUserEnter, this);
```

### USER_LEAVE
用户离开通话。
```javascript
let handleUserLeave = function(event) {
    console.log('用户离开通话')
}
tuiCallEngine.on(EVENT.USER_LEAVE, this.handleUserLeave, this);
```

### USER_UPDATE
用户更新。
```javascript
let handleUserUpdate = function(event) {
    console.log('用户更新')
}
tuiCallEngine.on(EVENT.USER_UPDATE, this.handleUserUpdate, this)
```

### REJECT
用户拒绝通话。
```javascript
let handleInviteeReject = function(event) {
    console.log('用户拒绝通话')
}
tuiCallEngine.on(EVENT.REJECT, this.handleInviteeReject, this);
```

### NO_RESP
用户无响应。
```javascript
let handleNoResponse = function(event) {
    console.log('用户无响应')
}
tuiCallEngine.on(EVENT.NO_RESP, this.handleNoResponse, this);
```

### LINE_BUSY
用户忙线。
```javascript
let handleLineBusy = function(event) {
    console.log('用户忙线')
}
tuiCallEngine.on(EVENT.LINE_BUSY, this.handleLineBusy, this);
```

### CALLING_CANCEL
通话被取消。
```javascript
let handleCallingCancel = function(event) {
    console.log('通话被取消')
}
tuiCallEngine.on(EVENT.CALLING_CANCEL, this.handleCallingCancel, this);
```

### CALLING_TIMEOUT
通话超时未应答。
```javascript
let handleCallingTimeout = function(event) {
    console.log('通话超时未应答')
}
tuiCallEngine.on(EVENT.CALLING_TIMEOUT, this.handleCallingTimeout, this);
```

### CALL_END
通话结束。
```javascript
let handleCallingEnd = function(event) {
    console.log('通话结束')
}
tuiCallEngine.on(EVENT.CALL_END, this.handleCallingEnd, this);
```

### SDK_READY
SDK Ready 回调。
```javascript
let handleSDKReady = function(event) {
    console.log('SDK Ready 回调')
}
tuiCallEngine.on(EVENT.SDK_READY, this.handleSDKReady, this);
```

### KICKED_OUT
被踢下线。
```javascript
let handleKickedOut = function(event) {
    console.log('被踢下线')
}
tuiCallEngine.on(EVENT.KICKED_OUT, this.handleKickedOut, this);
```

### CALL_MODE
切换通话模式。
```javascript
let handleCallMode = function(event) {
    console.log('切换通话模式')
}
tuiCallEngine.on(EVENT.CALL_MODE, this.handleCallMode, this);
```

[](id:MEDIA_TYPE)
#### 通话的类型

| MEDIA_TYPE | 说明 |
|-----|-----|
| AUDIO | 音频 |
| VIDEO | 视频 |

[](id:AUDIO_PLAYBACK_DEVICE)

#### 声音的播放设备

| AUDIO_PLAYBACK_DEVICE | 说明 |
|-----|-----|
| EAR | 听筒 |
| SPEAKER | 扬声器 |

[](id:bind)

#### 通话中的事件处理

| 事件名 | 说明 |
|-----|-----|
| _pusherNetStatus | pusher 的网络状况 |
| _playNetStatus | player 的网络状况 |
| _pusherStateChangeHandler | live-pusher 改变状态事件处理 |
| _pusherAudioVolumeNotify | live-pusher 麦克风采集的音量大小事件处理 |
| _playerStateChange | live-player 状态事件处理 |
| _playerAudioVolumeNotify | live-player 麦克风采集的音量大小事件处理 |
| _pusherAudioHandler | 订阅 / 取消订阅 Audio |
| _pusherVideoHandler | 订阅 / 取消订阅 Video |