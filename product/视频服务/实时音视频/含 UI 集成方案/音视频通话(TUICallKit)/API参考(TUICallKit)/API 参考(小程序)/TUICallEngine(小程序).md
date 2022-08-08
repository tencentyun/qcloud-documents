## TUICallEngine API 简介

TUICallEngine API 是音视频通话组件的**无 UI 接口**，如果 TUICallKit 的交互并不满足您的需求，您可以使用这套接口自己封装交互。
由于小程序开发的限制，需要先给live-pusher[绑定事件](#bind)，具体可以参照TUICallkit。

<h2 id="TUICallEngine"> API 概览</h2>

### 创建实例和事件回调

| API | 描述 |
|-----|-----|
| [createInstance](#createInstance) | 创建 TUICallEngine 实例（静态方法）|
| [destroyInstance](#destroyInstance) | 销毁 TUICallEngine 实例（静态方法）|
| [on](#on) | 增加事件监听|
| [off](#off) | 取消事件监听|


### 通话操作相关接口函数

| API | 描述 |
|-----|-----|
| [call](#call) | 发起 1v1 通话|
| [accept](#accept) | 接听通话 |
| [reject](#reject) | 拒绝通话 |
| [hangup](#hangup) | 结束通话|
| [switchCallMediaType](#switchCallMediaType) | 切换通话媒体类型，比如视频通话切音频通话|


### 设备控制相关接口函数

| API | 描述 |
|-----|-----|
| [openCamera](#openCamera) | 开启摄像头|
| [closeCamera](#closeCamera) | 关闭摄像头|
| [switchCamera](#switchCamera) | 切换前后摄像头|
| [openMicrophone](#openMicrophone) | 打开麦克风|
| [closeMicrophone](#closeMicrophone) | 关闭麦克风|
| [selectAudioPlaybackDevice](#selectAudioPlaybackDevice) | 选择音频播放设备（听筒/扬声器）|

### 其他接口函数

| API | 描述 |
|-----|-----|
| [setSelfInfo](#setselfinfo) | 设置用户的头像、昵称|


<h2 id="TUICallEngine"> API 详情</h2>

[](id:createInstance)
### createInstance
创建 TUICallEngine 的单例(class上的static方法)
```javascript
TUICallEngine.createInstance({
    sdkAppID:'xxxxxxx',
    tim,
})
```

说明

| 参数 | 是否必传 | 说明 |
|-----|-----|-----|
| sdkAppID | 必传 | SDKAppId是腾讯云用于区分客户的唯一标识 |
| tim | 非必传 | TIM 是 IM Web SDK 的命名空间，提供了创建 SDK 实例的静态方法 |


[](id:destroyInstance)
### destroyInstance
销毁 TUICallEngine 的单例(class上的static方法)
```javascript
TUICallEngine.destroyInstance()
```

### on
添加回调接口，您可以通过这个接听，监听`TRTC`相关的事件回调
```javascript
on(EventCode, handler, context);
```

说明

| 参数 | 类型 | 说明 |
|-----|-----|-----|
| Eventlist | String | [事件表](#evenlist) |
| handler | Function | 监听函数 |
| context | Object | 当前执行上下文 |



### off
移除回调接口
```javascript
off(EventCode, handler);
```
说明

| 参数 | 类型 | 说明 |
|-----|-----|-----|
| EventCode | String | [事件表](#evenlist) |
| handler | Function | 监听函数 |


### call
C2C邀请通话，被邀请方会收到的回调，如果当前处于通话中，可以调用该函数以邀请第三方进入通话

```javascript
call({
    userID:"xxxxxxx",
    type:MEDIA_TYPE.AUDIO
})
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 目标用户的userId |
| type | [MEDIA_TYPE](#MEDIA_TYPE) | 通话的媒体类型，AUDIO-语音通话，VIDEO-视频通话|


### accept
当您作为被邀请方收到的回调时，可以调用该函数接听来电

```javascript
accept();
```

### reject
当您作为被邀请方收到的回调时，可以调用该函数拒绝来电

```javascript
reject();
```

### hangup
当您处于通话中，可以调用该函数挂断通话
当您发起通话时，可用去了取消通话

```javascript
hangup();
```

[](id:switchCallMediaType)
### switchCallMediaType
切换通话媒体类型，比如视频通话切音频通话

```javascript
switchCallMediaType(MEDIA_TYPE.VIDEO);
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type| [MEDIA_TYPE](#MEDIA_TYPE)  |通话的媒体类型，AUDIO-语音通话，VIDEO-视频通话 |


[](id:openCamera)
### openCamera
您可以调用该函数开启摄像头

```javascript
openCamera();
```

[](id:closeCamera)
### closeCamera
您可以调用该函数关闭摄像头，处于通话中的用户会收到回调

```javascript
closeCamera();
```

[](id:switchCamera)
### switchCamera
切换前后摄像头

```javascript
switchCamera();
```

[](id:openMicrophone)
### openMicrophone
您可以调用该函数打开麦克风
处于通话中的用户会收到回调

```javascript
openMicrophone();
```


[](id:closeMicrophone)
### closeMicrophone
您可以调用该函数关闭麦克风
处于通话中的用户会收到回调

```javascript
closeMicrophone();
```

[](id:selectAudioPlaybackDevice)
### selectAudioPlaybackDevice
选择音频播放设备，目前支持听筒、扬声器，在通话场景中，可以使用这个接口来开启/关闭免提模式。

```javascript
selectAudioPlaybackDevice(AUDIO_PLAYBACK_DEVICE.EAR);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | [AUDIO_PLAYBACK_DEVICE](#AUDIO_PLAYBACK_DEVICE)| speaker:扬声器 ear:听筒 |


[](id:setSelfInfo)
### setSelfInfo
设置用户头像、昵称的接口

```javascript
setSelfInfo('xxxxxxx','头像.png') ;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nickName | String | 设置昵称 |
| avatar | String | 头像地址 |


[](id:evenlist)
事件表

| 事件名 | 说明 |
|-----|-----|
| [INVITED](#INVITED) | 被邀请通话 |
| [USER_ACCEPT](#USER_ACCEPT) | 用户接听 |
| [USER_ENTER](#USER_ENTER) | 用户进入通话 |
| [USER_LEAVE](#USER_LEAVE) | 用户离开通话 |
| [USER_UPDATE](#USER_UPDATE) | 用户更新 |
| [REJECT](#REJECT) | 用户拒绝通话 |
| [NO_RESP](#NO_RESP) | 用户无响应 |
| [LINE_BUSY](#LINE_BUSY) | 用户忙线 |
| [CALLING_CANCEL](#CALLING_CANCEL) | 通话被取消 |
| [CALLING_TIMEOUT](#CALLING_TIMEOUT) | 通话超时未应答 |
| [CALL_END](#CALL_END) | 通话结束 |
| [SDK_READY](#SDK_READY) | SDK Ready 回调 |
| [KICKED_OUT](#KICKED_OUT) | 被踢下线 |
| [CALL_MODE](#CALL_MODE) | 切换通话模式 |


[](id:INVITED)
### INVITED
被邀请通话
```javascript
let handleNewInvitationReceived=function(event){
    console.log('被邀请通话')
  }
tuiCallEngine.on(EVENT.INVITED, this.handleNewInvitationReceived, this);
```

[](id:USER_ACCEPT)
### USER_ACCEPT
用户接听
```javascript
let handleUserAccept=function(event) {
    console.log('用户接听')
}
tuiCallEngine.on(EVENT.USER_ACCEPT, this.handleUserAccept, this);
```

[](id:USER_ENTER)
### USER_ENTER
用户进入通话
```javascript
let handleUserEnter=function(event) {
    console.log('用户进入通话')
}
tuiCallEngine.on(EVENT.USER_ENTER, this.handleUserEnter, this);
```

[](id:USER_LEAVE)
### USER_LEAVE
用户离开通话
```javascript
let handleUserLeave=function(event) {
    console.log('用户离开通话')
}
tuiCallEngine.on(EVENT.USER_LEAVE, this.handleUserLeave, this);
```

[](id:USER_UPDATE)
### USER_UPDATE
用户更新
```javascript
let handleUserUpdate=function(event) {
    console.log('用户更新')
}
tuiCallEngine.on(EVENT.USER_UPDATE, this.handleUserUpdate, this)
```

[](id:REJECT)
### REJECT
用户拒绝通话
```javascript
let handleInviteeReject=function(event) {
    console.log('用户拒绝通话')
}
tuiCallEngine.on(EVENT.REJECT, this.handleInviteeReject, this);
```

[](id:NO_RESP)
### NO_RESP
用户无响应
```javascript
let handleNoResponse=function(event) {
    console.log('用户无响应')
}
tuiCallEngine.on(EVENT.NO_RESP, this.handleNoResponse, this);
```

[](id:LINE_BUSY)
### LINE_BUSY
用户忙线
```javascript
let handleLineBusy=function(event) {
    console.log('用户忙线')
}
tuiCallEngine.on(EVENT.LINE_BUSY, this.handleLineBusy, this);
```

[](id:CALLING_CANCEL)
### CALLING_CANCEL
通话被取消
```javascript
let handleCallingCancel=function(event) {
    console.log('通话被取消')
}
tuiCallEngine.on(EVENT.CALLING_CANCEL, this.handleCallingCancel, this);
```

[](id:CALLING_TIMEOUT)
### CALLING_TIMEOUT
通话超时未应答
```javascript
let handleCallingTimeout=function(event) {
    console.log('通话超时未应答')
}
tuiCallEngine.on(EVENT.CALLING_TIMEOUT, this.handleCallingTimeout, this);
```

[](id:CALL_END)
### CALL_END
通话结束
```javascript
let handleCallingEnd=function(event) {
    console.log('通话结束')
}
tuiCallEngine.on(EVENT.CALL_END, this.handleCallingEnd, this);
```

[](id:SDK_READY)
### SDK_READY
SDK Ready 回调
```javascript
let handleSDKReady=function(event) {
    console.log('SDK Ready 回调')
}
tuiCallEngine.on(EVENT.SDK_READY, this.handleSDKReady, this);
```

[](id:KICKED_OUT)
### KICKED_OUT
被踢下线
```javascript
let handleKickedOut=function(event) {
    console.log('被踢下线')
}
tuiCallEngine.on(EVENT.KICKED_OUT, this.handleKickedOut, this);
```

[](id:CALL_MODE)
### CALL_MODE
切换通话模式
```javascript
let handleCallMode=function(event) {
    console.log('切换通话模式')
}
tuiCallEngine.on(EVENT.CALL_MODE, this.handleCallMode, this);
```

[](id:MEDIA_TYPE)
通话的类型

| MEDIA_TYPE | 说明 |
|-----|-----|
| AUDIO | 音频 |
| VIDEO | 视频 |


[](id:AUDIO_PLAYBACK_DEVICE)
声音的播放设备

| AUDIO_PLAYBACK_DEVICE | 说明 |
|-----|-----|
| EAR | 听筒 |
| SPEAKER | 扬声器 |


[](id:bind)
通话中的事件处理

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