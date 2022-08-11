## TUICallEvent API 简介

TUICallEvent API 是音视频通话组件的**事件接口**。

<h2 id="TUICallEvent"> 事件列表</h2>

| EVENT | 描述 |
|-----|-----|
| [TUICallEvent.ERROR](#error) | SDK 内部发生了错误                                   |
| [TUICallEvent.SDK_READY](#sdk_ready) | SDK 进入 ready 状态时收到该回调                      |
| [TUICallEvent.KICKED_OUT](#kicked_out) | 重复登陆，收到该回调说明被踢出房间                   |
| [TUICallEvent.USER_ACCEPT](#user_accept) | 如果有用户接听，那么会收到此回调                     |
| [TUICallEvent.USER_ENTER](#user_enter) | 如果有用户同意进入通话，那么会收到此回调             |
| [TUICallEvent.USER_LEAVE](#user_leave) | 如果有用户同意离开通话，那么会收到此回调             |
| [TUICallEvent.REJECT](#reject) | 用户拒绝通话                                         |
| [TUICallEvent.NO_RESP](#no_resp) | 邀请用户无应答                                       |
| [TUICallEvent.LINE_BUSY](#line_busy) | 邀请方忙线                                           |
| [TUICallEvent.CALLING_TIMEOUT](#calling_timeout) | 作为被邀请方会收到，收到该回调说明本次通话超时未应答 |
| [TUICallEvent.USER_VIDEO_AVAILABLE](#user_video_available) | 远端用户开启/关闭了摄像头, 会收到该回调              |
| [TUICallEvent.USER_AUDIO_AVAILABLE](#user_audio_available) | 远端用户开启/关闭了麦克风, 会收到该回调              |
| [TUICallEvent.USER_VOICE_VOLUME](#user_voice_volume) | 远端用户说话音量调整, 会收到该回调                   |
| [TUICallEvent.GROUP_CALL_INVITEE_LIST_UPDATE](#group_call_invitee_list_update) | 群聊更新邀请列表收到该回调                           |
| [TUICallEvent.INVITED](#invited) | 被邀请进行通话                                       |
| [TUICallEvent.CALLING_CANCEL](#calling_cancel) | 作为被邀请方会收到，收到该回调说明本次通话被取消了   |
| [TUICallEvent.CALLING_END](#calling_end) | 收到该回调说明本次通话结束了                         |
| [TUICallEvent.DEVICED_UPDATED](#deviced_updated) | 设备列表更新收到该回调                               |
| [TUICallEvent.CALL_TYPE_CHANGED](#call_type_changed) | 通话类型切换收到该回调                               |

### ERROR
SDK 内部发生了错误。
```javascript
let onError = function(error) {
  console.log(error)
};
tuiCallEngine.on(TUICallEvent.ERROR, onError);
```

### SDK_READY
SDK 进入 ready 状态时收到该回调。
```javascript
let onSDKReady = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.SDK_READY, onSDKReady);
```

### KICKED_OUT
重复登陆，收到该回调说明被踢出房间。
```javascript
let handleOnKickedOut = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.KICKED_OUT, handleOnKickedOut);
```

### USER_ACCEPT
如果有用户接听，那么会收到此回调。
```javascript
let handleUserAccept = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.USER_ACCEPT, handleUserAccept);
```

### USER_ENTER
如果有用户同意进入通话，那么会收到此回调。
```javascript
let handleUserEnter = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.USER_ENTER, handleUserEnter);
```

### USER_LEAVE
如果有用户同意离开通话，那么会收到此回调。
```javascript
let handleUserLeave = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.USER_LEAVE, handleUserLeave);
```

### REJECT
用户拒绝通话。
```javascript
let handleInviteeReject = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.REJECT, handleInviteeReject);
```

### NO_RESP
邀请用户无应答。
- 在C2C通话中，只有发起方会收到无人应答的回调 例如 A 邀请 B、C 进入通话，B不应答，A可以收到该回调，但C不行
- 在IM群组通话中，所有被邀请人均能收到该回调 例如 A 邀请 B、C 进入通话，B不应答，A、C均能收到该回调
```javascript
let handleNoResponse = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.NO_RESP, handleNoResponse);
```

### LINE_BUSY
邀请方忙线。
```javascript
let handleLineBusy = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.LINE_BUSY, handleLineBusy);
```

### CALLING_TIMEOUT
作为被邀请方会收到，收到该回调说明本次通话超时未应答。
```javascript
let handleCallingTimeout = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.CALLING_TIMEOUT, handleCallingTimeout);
```

### USER_VIDEO_AVAILABLE
远端用户开启/关闭了摄像头, 会收到该回调。
```javascript
let handleUserVideoChange = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.USER_VIDEO_AVAILABLE, handleUserVideoChange);
```


### USER_AUDIO_AVAILABLE
远端用户开启/关闭了麦克风, 会收到该回调。
```javascript
let handleUserAudioChange = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.USER_AUDIO_AVAILABLE, handleUserAudioChange);

```

### USER_VOICE_VOLUME
远端用户说话音量调整, 会收到该回调
```javascript
let handleUserVoiceVolumeChange = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.USER_VOICE_VOLUME, handleUserVoiceVolumeChange);
```

### GROUP_CALL_INVITEE_LIST_UPDATE
群聊更新邀请列表收到该回调。
```javascript
let handleGroupInviteeListUpdate = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.GROUP_CALL_INVITEE_LIST_UPDATE, handleGroupInviteeListUpdate);
```

### INVITED
被邀请进行通话。
```javascript
let handleNewInvitationReceived = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.INVITED, handleNewInvitationReceived);
```

### CALLING_CANCEL
作为被邀请方会收到，收到该回调说明本次通话被取消了。
```javascript
let handleCallingCancel = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.CALLING_CANCEL, handleCallingCancel);
```


### CALLING_END
收到该回调说明本次通话结束了。
```javascript
let handleCallingEnd = function(event) {
  console.log(event)
};
tuiCallEngine.on(TUICallEvent.CALLING_END, handleCallingEnd);
```

### DEVICED_UPDATED
设备列表更新收到该回调。
```javascript
let handleDeviceUpdated = function({ microphoneList, cameraList, currentMicrophoneID, currentCameraID }) {
  console.log(microphoneList, cameraList, currentMicrophoneID, currentCameraID)
};
tuiCallEngine.on(TUICallEvent.DEVICED_UPDATED, handleDeviceUpdated);
```

### CALL_TYPE_CHANGED
通话类型切换收到该回调。
```javascript
let handleCallTypeChanged = function({ oldCallType, newCallType }) {
  console.log(oldCallType, newCallType)
};
tuiCallEngine.on(TUICallEvent.CALL_TYPE_CHANGED, handleDeviceUpdated);
```