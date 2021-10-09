
TRTCMeeting 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建会议房间，参会人员输入房间号后进入会议。
- 参会人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TRTCMeeting 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人视频会议(iOS)](https://cloud.tencent.com/document/product/647/45681)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时视频会议组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 MeetingRoom 实现会议中聊天室的功能。

## TRTCMeeting API 概览

### SDK基础函数

| API                                 | 描述                     |
| ----------------------------------- | ------------------------ |
| [sharedInstance](#sharedinstance) | 获取单例对象。           |
| [delegateQueue](#delegatequeue)   | 设置事件回调所在的线程。 |
| [delegate](#delegate)             | 设置事件回调。           |
| [login](#login)                   | 登录。                   |
| [logout](#logout)                 | 登出。                   |
| [setSelfProfile](#setselfprofile) | 设置用户信息。           |

### 会议房间相关接口函数

| API                                 | 描述                           |
| ----------------------------------- | ------------------------------ |
| [createMeeting](#createmeeting)   | 创建会议房间（主持人调用）。   |
| [destroyMeeting](#destroymeeting) | 销毁会议房间（主持人调用）。   |
| [enterMeeting](#entermeeting)     | 进入会议房间（参会成员调用）。 |
| [leaveMeeting](#leavemeeting)     | 离开会议房间（参会成员调用）。 |

### 远端用户接口

| API                                               | 描述                                                         |
| ------------------------------------------------- | ------------------------------------------------------------ |
| [getUserInfoList](#getuserinfolist)             | 获取房间内所有的人员列表，enterMeeting() 成功后调用才有效。  |
| [getUserInfo](#getuserinfo)                     | 获取房间内指定人员的详细信息，enterMeeting() 成功后调用才有效。 |
| [startRemoteView](#startremoteview)             | 播放指定成员的远端视频画面。                                 |
| [stopRemoteView](#stopremoteview)               | 停止播放远端视频画面。                                       |
| [setRemoteViewFillMode](#setremoteviewfillmode) | 根据用户 ID 和设置远端图像的渲染模式。                         |
| [setRemoteViewRotation](#setremoteviewrotation) | 设置远端图像的顺时针旋转角度。                               |
| [muteRemoteAudio](#muteremoteaudio)             | 屏蔽远端指定成员的声音。                                     |
| [muteRemoteVideoStream](#muteremotevideostream) | 屏蔽远端指定成员的视频流。                                   |

### 本地视频操作接口

| API                                         | 描述                       |
| ------------------------------------------- | -------------------------- |
| [startCameraPreview](#startcamerapreview) | 开启本地视频的预览画面。   |
| [stopCameraPreview](#stopcamerapreview)   | 停止本地视频采集及预览。   |
| [switchCamera](#switchcamera)   | 切换前后摄像头。           |
| [setVideoResolution](#setvideoresolution) | 设置分辨率。               |
| [setVideoFps](#setvideofps)               | 设置帧率。                 |
| [setVideoBitrate](#setvideobitrate)       | 设置码率。                 |
| [setLocalViewMirror](#setlocalviewmirror) | 设置本地画面镜像预览模式。 |

### 本地音频操作接口

| API                                               | 描述                 |
| ------------------------------------------------- | -------------------- |
| [startMicrophone](#startmicrophone)             | 开启麦克风采集。     |
| [stopMicrophone](#stopmicrophone)               | 停止麦克风采集。     |
| [setAudioQuality](#setaudioquality)             | 设置音质。           |
| [muteLocalAudio](#mutelocalaudio)               | 开启本地静音。       |
| [setSpeaker](#setspeaker)                       | 设置开启扬声器。     |
| [setAudioCaptureVolume](#setaudiocapturevolume) | 设置麦克风采集音量。 |
| [setAudioPlayoutVolume](#setaudioplayoutvolume) | 设置播放音量。       |
| [startFileDumping](#startfiledumping)           | 开始录音。           |
| [stopFileDumping](#stopfiledumping)             | 停止录音。           |
| [enableAudioEvaluation](#enableaudioevaluation) | 启用音量大小提示。   |

### 录屏接口

| API                                           | 描述           |
| --------------------------------------------- | -------------- |
| [startScreenCapture](#startscreencapture)   | 启动屏幕分享。 |
| [stopScreenCapture](#stopscreencapture)     | 停止屏幕采集。 |
| [pauseScreenCapture](#pausescreencapture)   | 暂停屏幕分享。 |
| [resumeScreenCapture](#resumescreencapture) | 恢复屏幕分享。 |

### 美颜滤镜相关接口函数

| API                                     | 描述                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html)。 |

### 分享接口

| API                                                 | 描述              |
| --------------------------------------------------- | ----------------- |
| [getLiveBroadcastingURL](#getlivebroadcastingurl) | 获取 CDN 分享链接。 |

### 消息发送相关接口函数

| API                                       | 描述                                                       |
| ----------------------------------------- | ---------------------------------------------------------- |
| [sendRoomTextMsg](#sendroomtextmsg)     | 在房间中广播文本消息，一般用于文本聊天。                     |
| [sendRoomCustomMsg](#sendroomcustommsg) | 在房间中广播自定义（信令）消息。 |

## TRTCMeetingDelegate API 概览

### 通用事件回调

| API                   | 描述       |
| --------------------- | ---------- |
| [onError](#onerror) | 错误回调。 |

### 会议房间事件回调

| API                                         | 描述                   |
| ------------------------------------------- | ---------------------- |
| [onRoomDestroy](#onroomdestroy)           | 会议房间被销毁的回调。 |
| [onNetworkQuality](#onnetworkquality)     | 网络状态回调。         |
| [onUserVolumeUpdate](#onuservolumeupdate) | 用户通话音量回调。     |

### 成员进出事件回调

| API                                   | 描述                 |
| ------------------------------------- | -------------------- |
| [onUserEnterRoom](#onuserenterroom) | 收到新成员进房通知。 |
| [onUserLeaveRoom](#onuserleaveroom) | 收到成员退房通知。   |

### 成员音视频事件回调

| API                                             | 描述                        |
| ----------------------------------------------- | --------------------------- |
| [onUserVideoAvailable](#onuservideoavailable) | 成员开启/关闭摄像头的通知。 |
| [onUserAudioAvailable](#onuseraudioavailable) | 成员开启/关闭麦克风的通知。 |

### 录屏事件回调

| API                                                 | 描述           |
| --------------------------------------------------- | -------------- |
| [onScreenCaptureStarted](#onscreencapturestarted) | 录屏开始通知。 |
| [onScreenCapturePaused](#onscreencapturepaused)   | 录屏暂停回调。 |
| [onScreenCaptureResumed](#onscreencaptureresumed) | 录屏恢复回调。 |
| [onScreenCaptureStoped](#onscreencapturestoped)   | 录屏停止回调。 |

### 消息事件回调

| API                                           | 描述             |
| --------------------------------------------- | ---------------- |
| [onRecvRoomTextMsg](#onrecvroomtextmsg)     | 收到文本消息。   |
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | 收到自定义消息。 |

### 录屏事件回调

| API                                                 | 描述           |
| --------------------------------------------------- | -------------- |
| [onScreenCaptureStarted](#onscreencapturestarted) | 录屏开始通知。 |
| [onScreenCapturePaused](#onscreencapturepaused)   | 录屏暂停回调。 |
| [onScreenCaptureResumed](#onscreencaptureresumed) | 录屏恢复回调。 |
| [onScreenCaptureStoped](#onscreencapturestoped)   | 录屏停止回调。 |

## TRTCMeetingDef API 概览

### TRTCMeetingUserInfo 会议用户信息

| 属性                                    | 描述                                   |
| --------------------------------------- | -------------------------------------- |
| [userId](#userid)       | 用户 ID。           |
| [userName](#username)   | 用户名称（昵称）。 |
| [avatarURL](#avatarurl) | 用户头像 URL。      |
| [isVideoAvailable](#isvideoavailable) | 用户是否打开了视频。                   |
| [isAudioAvailable](#isaudioavailable) | 用户是否打开音频。                     |
| [isMuteVideo](#ismutevideo)           | 是否对用户静画（不播放该用户的视频）。 |
| [isMuteAudio](#ismuteaudio)           | 是否对用户静音（不播放改用户的音频）。 |


## SDK 基础函数

### sharedInstance

获取 [TRTCMeeting](https://cloud.tencent.com/document/product/647/45681) 单例对象。

```objective-c
+ (instancetype)sharedInstance;
```

### delegateQueue

设置事件回调所在的线程。

```objective-c
- (void)setDelegateQueue:(dispatch_queue_t)delegateQueue
```

参数如下表所示：

| 参数          | 类型             | 含义                                                         |
| ------------- | ---------------- | ------------------------------------------------------------ |
| delegateQueue | dispatch_queue_t | TRTCMeeting 中的各种状态通知回调会通过该 queue 通知给您，请勿与 setDelegate 混用。 |

### delegate

[TRTCMeeting](https://cloud.tencent.com/document/product/647/45681) 事件回调，您可以通过 TRTCMeetingDelegate 获得 [TRTCMeeting](https://cloud.tencent.com/document/product/647/45681) 的各种状态通知。

### login

登录。

```objective-c
- (void)login:(UInt32)sdkAppId userId:(NSString *)userId userSig:(NSString *)userSig callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                                                         |
| -------- | ------------------- | ------------------------------------------------------------ |
| sdkAppId | UInt32              | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userId   | NSString            | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（_）。 |
| userSig  | NSString            | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| callback | TRTCMeetingCallback | 登录回调，成功时 code 为0。                                  |

### logout

登出。

```objective-c
- (void)logout:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                        |
| -------- | ------------------- | --------------------------- |
| callback | TRTCMeetingCallback | 登出回调，成功时 code 为0。 |

### setSelfProfile

修改个人信息。

```objective-c
- (void)setSelfProfile:(NSString *)userName avatarURL:(NSString *)avatarURL callback:(TRTCMeetingCallback)callback;
```

| 参数      | 类型                | 含义                                      |
| --------- | ------------------- | ----------------------------------------- |
| userName  | NSString            | 用户昵称。                                |
| avatarURL | NSString            | 用户头像。                                |
| callback  | TRTCMeetingCallback | 设置用户信息的结果回调，成功时 code 为0。 |



## 会议房间相关接口函数

### createMeeting

创建会议（主持人调用）。

```objective-c
- (void)createMeeting:(UInt32)roomId callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                                   |
| -------- | ------------------- | -------------------------------------- |
| roomId   | UInt32              | 房间标识，需要由您分配并进行统一管理。 |
| callback | TRTCMeetingCallback | 创建房间的结果回调，成功时 code 为0。  |

主持人正常调用流程如下： 

1. 【主持人】调用 `createMeeting()` 创建会议，会议房间创建成功与否会通过 `TRTCMeetingCallback` 通知给主持人。
2. 【主持人】调用 `startCameraPreview()` 打开摄像头预览，此时可以调整美颜参数。 
3. 【主持人】调用 `startMicrophone()` 打开麦克风采集。

### destroyMeeting

销毁会议房间（主持人调用）。主持人在创建会议后，可以调用该函数来销毁会议。

```objective-c
- (void)destroyMeeting:(UInt32)roomId callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                                   |
| -------- | ------------------- | -------------------------------------- |
| roomId   | UInt32              | 房间标识，需要由您分配并进行统一管理。 |
| callback | TRTCMeetingCallback | 创建房间的结果回调，成功时 code 为0。  |

### enterMeeting

进入会议（参会成员调用）。

```objective-c
- (void)enterMeeting:(UInt32)roomId callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                                   |
| -------- | ------------------- | -------------------------------------- |
| roomId   | UInt32              | 房间标识，需要由您分配并进行统一管理。 |
| callback | TRTCMeetingCallback | 进入房间的结果回调，成功时 code 为0。  |

参会成员进入会议的正常调用流程如下： 
1. 【参会成员】调用`enterMeeting`并传入 roomId 即可进入会议房间。
2. 【参会成员】调用`startCameraPreview()`打开摄像头预览，调用`startMicrophone()`打开麦克风采集。
3. 【参会成员】收到`onUserVideoAvailable`的事件，调用`startRemoteView(userId)`并传入成员的 userId 开始播放。
   
### leaveMeeting

离开会议（参会成员调用）。

```objective-c
- (void)leaveMeeting:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                                  |
| -------- | ------------------- | ------------------------------------- |
| callback | TRTCMeetingCallback | 退出房间的结果回调，成功时 code 为0。 |



## 远端用户相关接口

### getUserInfoList

获取房间内所有的人员列表，enterMeeting() 成功后调用才有效。

```objective-c
- (void)getUserInfoList:(TRTCMeetingUserListCallback)callback;
```

参数如下表所示：

| 参数     | 类型                        | 含义               |
| -------- | --------------------------- | ------------------ |
| callback | TRTCMeetingUserListCallback | 用户详细信息回调。 |

### getUserInfo

获取房间内指定人员的详细信息，enterMeeting() 成功后调用才有效。

```objective-c
- (void)getUserInfo:(NSString *)userId callback:(TRTCMeetingUserListCallback)callback;
```

参数如下表所示：

| 参数     | 类型                        | 含义               |
| -------- | --------------------------- | ----------- |
| userId | NSString | 远端的用户 ID。                   |
| callback | TRTCMeetingUserListCallback | 用户详细信息回调。 |

### startRemoteView

播放指定成员的远端视频画面。在 `onUserVideoAvailable()` 为true回调时，调用该接口。

```objective-c
- (void)startRemoteView:(NSString *)userId view:(UIView *)view callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                       |
| -------- | ------------------- | -------------------------- |
| userId   | NSString            | 需要观看的用户 ID。         |
| view     | UIView              | 承载视频画面的 view 控件。 |
| callback | TRTCMeetingCallback | 操作回调。                 |

### stopRemoteView

停止渲染远端视频画面。在 `onUserVideoAvailable()` 为false回调时，调用该接口。

```objective-c
- (void)stopRemoteView:(NSString *)userId callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义             |
| -------- | ------------------- | ---------------- |
| userId   | NSString            | 需要停止播放的用户 ID。 |
| callback | TRTCMeetingCallback | 操作回调。       |

### setRemoteViewFillMode

根据用户id和设置远端图像的渲染模式

```objective-c
- (void)setRemoteViewFillMode:(NSString *)userId fillMode:(TRTCVideoFillMode)fillMode;
```

参数如下表所示：

| 参数     | 类型              | 含义                                                         |
| -------- | ----------------- | ------------------------------------------------------------ |
| userId   | NSString          | 用户 ID。                                                    |
| fillMode | TRTCVideoFillMode | 填充或适应模式，默认值：填充（TRTCVideoFillMode_Fill），详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afda6658d1bf7dc9bc1445838b95d21ff)。 |

### setRemoteViewRotation

设置远端图像的顺时针旋转角度

```objective-c
- (void)setRemoteViewRotation:(NSString *)userId rotation:(NSInteger)rotation;
```

参数如下表所示：

| 参数     | 类型      | 含义                                                         |
| -------- | --------- | ------------------------------------------------------------ |
| userId   | NSString  | 对方的用户 ID。                                              |
| rotation | NSInteger | 顺时针旋转角度, 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2ef26a9ede0ba4fa6c5739229e1eee90)。 |

### muteRemoteAudio

静音远端音频。

```objective-c
- (void)muteRemoteAudio:(NSString *)userId mute:(BOOL)mute;
```

参数如下表所示：

| 参数   | 类型     | 含义                              |
| ------ | -------- | --------------------------------- |
| userId | NSString | 远端的用户 ID。                   |
| mute   | BOOL     | true：开启静音；false：关闭静音。 |

### muteRemoteVideoStream

屏蔽指定成员的视频流。

```objective-c
- (void)muteRemoteVideoStream:(NSString *)userId mute:(BOOL)mute;
```

参数如下表所示：

| 参数   | 类型     | 含义                          |
| ------ | -------- | ----------------------------- |
| userId | NSString | 远端的用户 ID。               |
| mute   | BOOL     | true：屏蔽；false：解除屏蔽。 |



## 本地视频操作接口

### startCameraPreview

开启本地视频的预览画面。

```objective-c
- (void)startCameraPreview:(BOOL)isFront view:(UIView *)view;
```

参数如下表所示：

| 参数    | 类型   | 含义                                  |
| ------- | ------ | ------------------------------------- |
| isFront | BOOL   | true：前置摄像头；false：后置摄像头。 |
| view    | UIView | 承载视频画面的控件。                  |

### stopCameraPreview

停止本地视频采集及预览。

```objective-c
- (void)stopCameraPreview;
```

### switchCamera

切换前后摄像头。

```objective-c
- (void)switchCamera:(BOOL)isFront;
```

参数如下表所示：

| 参数    | 类型 | 含义                                                  |
| ------- | ---- | ----------------------------------------------------- |
| isFront | BOOL | 切换前后摄像头，true：前置摄像头；false：后置摄像头。 |

### setVideoResolution

设置分辨率。

```objective-c
- (void)setVideoResolution:(TRTCVideoResolution)resolution;
```

参数如下表所示：

| 参数       | 类型                | 含义                                                         |
| ---------- | ------------------- | ------------------------------------------------------------ |
| resolution | TRTCVideoResolution | 视频分辨率, 详细请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#gaa58db9156c82d75257499cb5e0cdf0e5)。 |

### setVideoFps

设置帧率。

```objective-c
- (void)setVideoFps:(int)fps;
```

参数如下表所示：

| 参数 | 类型 | 含义           |
| ---- | ---- | -------------- |
| fps  | int  | 视频采集帧率。 |

>? 【推荐取值】 15fps或20fps，5fps以下，卡顿感明显。10fps以下，会有轻微卡顿感。20fps以上，则过于浪费（电影的帧率为24fps）。

### setVideoBitrate

设置码率。

```objective-c
- (void)setVideoBitrate:(int)bitrate;
```

参数如下表所示：

| 参数    | 类型 | 含义                                                         |
| ------- | ---- | ------------------------------------------------------------ |
| bitrate | int  | 码率，SDK 会按照目标码率进行编码，只有在网络不佳的情况下才会主动降低视频码率。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#a21a93f89a608f4642ecc9d81ef25a454)。 |

>?【推荐取值】请参考 TRTCVideoResolution 在各档位注释的最佳码率，也可以在此基础上适当调高。 例如 TRTC_VIDEO_RESOLUTION_1280_720 对应1200kbps的目标码率，您也可以设置为1500kbps以便获得更好的清晰度观感。

### setLocalViewMirror

设置本地画面镜像预览模式。

```objective-c
- (void)setLocalViewMirror:(TRTCLocalVideoMirrorType)type;
```

参数如下表所示：

| 参数 | 类型                     | 含义                                                         |
| ---- | ------------------------ | ------------------------------------------------------------ |
| type | TRTCLocalVideoMirrorType | 镜像模式。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#a21a93f89a608f4642ecc9d81ef25a454)。 |



## 本地音频操作接口

### startMicrophone

开启麦克风采集。

```objective-c
- (void)startMicrophone;
```

### stopMicrophone

停止麦克风采集。

```objective-c
- (void)stopMicrophone;
```

### setAudioQuality

设置音质。

```objective-c
- (void)setAudioQuality:(TRTCAudioQuality)quality;
```

参数如下表所示：

| 参数    | 类型             | 含义                                                         |
| ------- | ---------------- | ------------------------------------------------------------ |
| quality | TRTCAudioQuality | 音频质量。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2cdffa1529fcaec866404f4f9b92ec53)。 |

### muteLocalAudio

静音/取消静音本地的音频。

```objective-c
- (void)muteLocalAudio:(BOOL)mute;
```

参数如下表所示：

| 参数 | 类型 | 含义                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| mute | BOOL | 静音/取消静音。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4ada386a75d8042a432da05fde5552d9)。 |

### setSpeaker

设置开启扬声器。

```objective-c
- (void)setSpeaker:(BOOL)useSpeaker;
```

参数如下表所示：

| 参数       | 类型 | 含义                         |
| ---------- | ---- | ---------------------------- |
| useSpeaker | BOOL | true：扬声器 ；false：听筒。 |

### setAudioCaptureVolume

设置麦克风采集音量。

```objective-c
- (void)setAudioCaptureVolume:(NSInteger)volume;
```

参数如下表所示：

| 参数   | 类型      | 含义                        |
| ------ | --------- | --------------------------- |
| volume | NSInteger | 采集音量，0-100， 默认100。 |

### setAudioPlayoutVolume

设置播放音量。

```objective-c
- (void)setAudioPlayoutVolume:(NSInteger)volume;
```

参数如下表所示：

| 参数   | 类型      | 含义                        |
| ------ | --------- | --------------------------- |
| volume | NSInteger | 播放音量，0-100， 默认100。 |

### startFileDumping

开始录音。

```objective-c
- (void)startFileDumping:(TRTCAudioRecordingParams *)params;
```

参数如下表所示：

| 参数   | 类型                     | 含义                                                         |
| ------ | ------------------------ | ------------------------------------------------------------ |
| params | TRTCAudioRecordingParams | 录音参数。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCAudioRecordingParams)。 |

>? 该方法调用后， SDK 会将通话过程中的所有音频（包括本地音频，远端音频，BGM 等）录制到一个文件里。无论是否进房，调用该接口都生效。如果调用 exitMeeting 时还在录音，录音会自动停止。

### stopFileDumping

停止录音。

```objective-c
- (void)stopFileDumping;
```

### enableAudioEvaluation

启用音量大小提示。

```objective-c
- (void)enableAudioEvaluation:(BOOL)enable;
```

参数如下表所示：

| 参数   | 类型 | 含义                      |
| ------ | ---- | ------------------------- |
| enable | BOOL | true：打开；false：关闭。 |

>? 开启后会在 onUserVolumeUpdate 中获取到 SDK 对音量大小值的评估。



## 录屏接口

### startScreenCapture

启动屏幕分享。

```objective-c
- (void)startScreenCapture:(TRTCVideoEncParam *)params;
```

参数如下表所示：

| 参数   | 类型              | 含义                                                         |
| ------ | ----------------- | ------------------------------------------------------------ |
| params | TRTCVideoEncParam | 设置屏幕分享时的编码参数，推荐采用上述推荐配置，如果您指定 encParams 为 nil，则使用您调用 startScreenCapture 之前的编码参数设置。 |

>? 详情请参见[TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a92330045ce479f3b5e5c6b366731c7ff)

### stopScreenCapture

停止屏幕采集。

```objective-c
- (int)stopScreenCapture
```

### pauseScreenCapture

暂停屏幕分享。

```objective-c
- (int)pauseScreenCapture
```

### resumeScreenCapture

恢复屏幕分享。

```objective-c
- (int)resumeScreenCapture
```



## 分享接口

### getLiveBroadcastingURL

获取 CDN 分享链接。

```objective-c
- (NSString *)getLiveBroadcastingURL;
```

返回值如下表所示：

| 返回值 | 类型     | 含义          |
| ------ | -------- | ------------- |
| url    | NSString | CDN 分享链接。 |



## 美颜滤镜相关接口函数

### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html)。

```objective-c
- (TXBeautyManager *)getBeautyManager;
```

通过美颜管理，您可以使用以下功能：

- 设置“美颜风格”、“美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。



## 消息发送相关接口函数

### sendRoomTextMsg

在房间中广播文本消息。

```objective-c
- (void)sendRoomTextMsg:(NSString *)message callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义           |
| -------- | ------------------- | -------------- |
| message  | NSString            | 文本消息。     |
| callback | TRTCMeetingCallback | 发送结果回调。 |

### sendRoomCustomMsg

发送自定义文本消息。

```objective-c
- (void)sendRoomCustomMsg:(NSString *)cmd message:(NSString *)message callback:(TRTCMeetingCallback)callback;
```

参数如下表所示：

| 参数     | 类型                | 含义                                               |
| -------- | ------------------- | -------------------------------------------------- |
| cmd      | NSString            | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | NSString            | 文本消息。                                         |
| callback | TRTCMeetingCallback | 发送结果回调。                                     |



## TRTCMeetingDelegate 事件回调

## 通用事件回调

### onError

>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```objective-c
- (void)onError:(NSInteger)code message:(NSString* _Nullable)message;
```

参数如下表所示：

| 参数    | 类型      | 含义       |
| ------- | --------- | ---------- |
| code    | NSInteger | 错误码。   |
| message | NSString  | 错误信息。 |



## 房间事件回调

### onRoomDestroy

房间被销毁的回调。主持人退房时，房间内的所有用户都会收到此通知。

```objective-c
- (void)onRoomDestroy:(NSString *)roomId;
```

参数如下表所示：

| 参数   | 类型     | 含义      |
| ------ | -------- | --------- |
| roomId | NSString | 房间 ID。 |

### onNetworkQuality

网络状态回调。

```objective-c
- (void)onNetworkQuality:(TRTCQualityInfo *)localQuality
           remoteQuality:(NSArray<TRTCQualityInfo*> *)remoteQuality;
```

参数如下表所示：

| 参数          | 类型                       | 含义           |
| ------------- | -------------------------- | -------------- |
| localQuality  | TRTCQualityInfo            | 上行网络质量。 |
| remoteQuality | NSArray&lt;TRTCQualityInfo *&gt; | 下行网络质量。 |

>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a723002319845fbfc03db501aa9da6c28)。

### onUserVolumeUpdate

启用音量大小提示，会通知每个成员的音量大小。

```objective-c
- (void)onUserVolumeUpdate:(NSString *)userId volume:(NSInteger)volume;
```

参数如下表所示：

| 参数   | 类型      | 含义                  |
| ------ | --------- | --------------------- |
| userId | NSString  | 用户 ID。            |
| volume | NSInteger | 音量大小，取值0-100。 |



## 成员进出事件回调

### onUserEnterRoom

新成员进房通知。

```objective-c
- (void)onUserEnterRoom:(NSString *)userId;
```

参数如下表所示：

| 参数   | 类型     | 含义            |
| ------ | -------- | --------------- |
| userId | NSString | 新进房成员的用户 ID。 |


### onUserLeaveRoom

成员退房通知。

```objective-c
- (void)onUserLeaveRoom:(NSString *)userId;
```

参数如下表所示：

| 参数   | 类型     | 含义          |
| ------ | -------- | ------------- |
| userId | NSString | 退房成员的用户 ID。 |



## 成员音视频事件回调

### onUserVideoAvailable

成员开启/关闭摄像头的通知。

```objective-c
- (void)onUserVideoAvailable:(NSString *)userId available:(BOOL)available;
```

参数如下表所示：

| 参数      | 类型     | 含义                                          |
| --------- | -------- | --------------------------------------------- |
| userId    | NSString | 用户 ID。                                    |
| available | BOOL     | true：用户打开摄像头；false：用户关闭摄像头。 |

### onUserAudioAvailable

成员开启/关闭麦克风的通知。

```objective-c
- (void)onUserAudioAvailable:(NSString *)userId available:(BOOL)available;
```

参数如下表所示：

| 参数      | 类型     | 含义                                          |
| --------- | -------- | --------------------------------------------- |
| userId    | NSString | 用户 ID。                                    |
| available | BOOL     | true：用户打开麦克风；false：用户关闭麦克风。 |

   

## 消息事件回调

### onRecvRoomTextMsg

收到文本消息。

```objective-c
- (void)onRecvRoomTextMsg:(NSString* _Nullable)message userInfo:(TRTCMeetingUserInfo *)userInfo;
```

参数如下表所示：

| 参数    | 类型                | 含义             |
| ------- | ------------------- | ---------------- |
| message | NSString            | 文本消息。       |
| userInfo | TRTCMeetingUserInfo | 发送者用户信息。 |

### onRecvRoomCustomMsg

收到自定义消息。

```objective-c
- (void)onRecvRoomCustomMsg:(NSString* _Nullable)cmd message:(NSString* _Nullable)message userInfo:(TRTCMeetingUserInfo *)userInfo;
```

参数如下表所示：

| 参数     | 类型                | 含义                                               |
| -------- | ------------------- | -------------------------------------------------- |
| cmd      | NSString            | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | NSString            | 文本消息。                                         |
| userInfo | TRTCMeetingUserInfo | 发送者用户信息。                                   |



## 录屏事件回调

### onScreenCaptureStarted

录屏开始通知。

```objective-c
- (void)onScreenCaptureStarted;
```

### onScreenCapturePaused

录屏暂停通知。

```objective-c
- (void)onScreenCapturePaused:(int)reason;
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| reason | int  | 暂停原因，0：用户主动暂停；1：屏幕窗口不可见暂停。 |

### onScreenCaptureResumed

录屏恢复通知。

```objective-c
- (void)onScreenCaptureResumed:(int)reason;
```

参数如下表所示：

| 参数   | 类型 | 含义                                                       |
| ------ | ---- | ---------------------------------------------------------- |
| reason | int  | 恢复原因，0：用户主动恢复；1：屏幕窗口恢复可见从而恢复分享 |

### onScreenCaptureStoped

录屏停止通知。

```objective-c
- (void)onScreenCaptureStoped:(int)reason;
```

参数如下表所示：

| 参数   | 类型 | 含义                                                 |
| ------ | ---- | ---------------------------------------------------- |
| reason | int  | 停止原因，0：用户主动停止；1：屏幕窗口关闭导致停止。 |



## TRTCMeetingDef 相关属性

## TRTCMeetingUserInfo

### userId

用户 ID。

```objective-c
@property (nonatomic, strong) NSString *userId;
```

### userName

用户名称（昵称）。

```objective-c
@property (nonatomic, strong) NSString *userName;
```

### avatarURL

用户头像 URL。

```objective-c
@property (nonatomic, strong) NSString *avatarURL;
```

### roomId

房间号。

```objective-c
@property (nonatomic, assign) UInt32 roomId;
```

### isVideoAvailable

用户是否打开了视频。

```objective-c
@property (nonatomic, assign) BOOL isVideoAvailable;
```

### isAudioAvailable

用户是否打开音频。

```objective-c
@property (nonatomic, assign) BOOL isAudioAvailable;
```

### isMuteVideo

是否对用户静画（不播放该用户的视频）。

```objective-c
@property (nonatomic, assign) BOOL isMuteVideo;
```

### isMuteAudio

是否对用户静音（不播放该用户的音频）。

```objective-c
@property (nonatomic, assign) BOOL isMuteAudio;
```

