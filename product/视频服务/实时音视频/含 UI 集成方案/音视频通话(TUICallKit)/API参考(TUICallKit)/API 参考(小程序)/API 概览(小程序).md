## TUICallKit (含 UI 接口)

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景。

| API                                                          | 描述                 |
|-----|-----|
| [init](https://tcloud-doc.isd.com/document/product/647/78760?!preview#init) | 初始化 TUICallKit    |
| [call](https://tcloud-doc.isd.com/document/product/647/78760?!preview#call) | 发起 1v1 通话        |
| [setSelfInfo](https://tcloud-doc.isd.com/document/product/647/78760?!preview#setselfinfo) | 设置用户的头像、昵称 |
| [destroyed](https://tcloud-doc.isd.com/document/product/647/78760?!preview#destroyed) | 销毁 TUICallKit      |

## TUICallEngine (无 UI 接口)

TUICallEngine API 是音视频通话组件的**无 UI 接口**，如果 TUICallKit 的交互并不满足您的需求，您可以使用这套 API 根据您的业务需求自定义封装。

| API | 描述 |
|-----|-----|
| [createInstance](https://tcloud-doc.isd.com/document/product/647/78761?!preview#createinstance) | 创建 TUICallEngine 实例（静态方法）      |
| [destroyInstance](https://tcloud-doc.isd.com/document/product/647/78761?!preview#destroyinstance) | 销毁 TUICallEngine 实例（静态方法）      |
| [on](https://tcloud-doc.isd.com/document/product/647/78761?!preview#on) | 增加事件监听                             |
| [off](https://tcloud-doc.isd.com/document/product/647/78761?!preview#off) | 取消事件监听                             |
| [call](https://tcloud-doc.isd.com/document/product/647/78761?!preview#call) | 发起 1v1 通话                            |
| [accept](https://tcloud-doc.isd.com/document/product/647/78761?!preview#accept) | 接听通话                                 |
| [reject](https://tcloud-doc.isd.com/document/product/647/78761?!preview#reject) | 拒绝通话                                 |
| [hangup](https://tcloud-doc.isd.com/document/product/647/78761?!preview#hangup) | 结束通话                                 |
| [switchCallMediaType](https://tcloud-doc.isd.com/document/product/647/78761?!preview#switchcallmediatype) | 切换通话媒体类型，比如视频通话切音频通话 |
| [openCamera](https://tcloud-doc.isd.com/document/product/647/78761?!preview#opencamera) | 开启摄像头                               |
| [closeCamera](https://tcloud-doc.isd.com/document/product/647/78761?!preview#closecamera) | 关闭摄像头                               |
| [switchCamera](https://tcloud-doc.isd.com/document/product/647/78761?!preview#switchcamera) | 切换前后摄像头                           |
| [openMicrophone](https://tcloud-doc.isd.com/document/product/647/78761?!preview#openmicrophone) | 打开麦克风                               |
| [closeMicrophone](https://tcloud-doc.isd.com/document/product/647/78761?!preview#closemicrophone) | 关闭麦克风                               |
| [selectAudioPlaybackDevice](https://tcloud-doc.isd.com/document/product/647/78761?!preview#selectaudioplaybackdevice) | 选择音频播放设备（听筒/扬声器）          |
| [setSelfInfo](https://tcloud-doc.isd.com/document/product/647/78761?!preview#setselfinfo) | 设置用户的头像、昵称                     |


## 关键常量定义
| 常量 | 描述 |
|-----|-----|
| [EVENT](#EVENT)                                 | 通话的事件表                            |
| [CALL_STATUS](#CALL_STATUS)                     | 通话的状态 默认、呼叫中/被呼叫中 接通中 |
| [MEDIA_TYPE](#MEDIA_TYPE)                       | 通话的类型  音频 视频                   |
| [AUDIO_PLAYBACK_DEVICE](#AUDIO_PLAYBACK_DEVICE) | 声音的播放设备 扬声器、听筒             |

[](id:EVENT)

### 通话的事件表

| 事件名 | 说明 |
|-----|-----|
| [INVITED](https://tcloud-doc.isd.com/document/product/647/78761?!preview#invited) | 被邀请通话     |
| [USER_ACCEPT](https://tcloud-doc.isd.com/document/product/647/78761?!preview#user_accept) | 用户接听       |
| [USER_ENTER](https://tcloud-doc.isd.com/document/product/647/78761?!preview#user_enter) | 用户进入通话   |
| [USER_LEAVE](https://tcloud-doc.isd.com/document/product/647/78761?!preview#user_leave) | 用户离开通话   |
| [USER_UPDATE](https://tcloud-doc.isd.com/document/product/647/78761?!preview#user_update) | 用户更新       |
| [REJECT](https://tcloud-doc.isd.com/document/product/647/78761?!preview#reject) | 用户拒绝通话   |
| [NO_RESP](https://tcloud-doc.isd.com/document/product/647/78761?!preview#no_resp) | 用户无响应     |
| [LINE_BUSY](https://tcloud-doc.isd.com/document/product/647/78761?!preview#line_busy) | 用户忙线       |
| [CALLING_CANCEL](https://tcloud-doc.isd.com/document/product/647/78761?!preview#calling_cancel) | 通话被取消     |
| [CALLING_TIMEOUT](https://tcloud-doc.isd.com/document/product/647/78761?!preview#calling_timeout) | 通话超时未应答 |
| [CALL_END](https://tcloud-doc.isd.com/document/product/647/78761?!preview#call_end) | 通话结束       |
| [SDK_READY](https://tcloud-doc.isd.com/document/product/647/78761?!preview#sdk_ready) | SDK Ready 回调 |
| [KICKED_OUT](https://tcloud-doc.isd.com/document/product/647/78761?!preview#kicked_out) | 被踢下线       |
| [CALL_MODE](https://tcloud-doc.isd.com/document/product/647/78761?!preview#call_mode) | 切换通话模式   |

[](id:CALL_STATUS)

### 通话的状态

| CALL_STATUS | 说明 |
|-----|-----|
| IDLE | 默认 |
| CALLING | 呼叫中/被呼叫中 |
| CONNECTED | 接通中 |

[](id:MEDIA_TYPE)
### 通话的类型

| MEDIA_TYPE | 说明 |
|-----|-----|
| AUDIO | 音频 |
| VIDEO | 视频 |

[](id:AUDIO_PLAYBACK_DEVICE)
### 声音的播放设备

| AUDIO_PLAYBACK_DEVICE | 说明 |
|-----|-----|
| EAR | 听筒 |
| SPEAKER | 扬声器 |
