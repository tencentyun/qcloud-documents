TUIRoom 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建房间，进入房间人员输入房间号后进入房间。
- 进入房间人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TUIRoom 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人音视频房间(iOS)](https://cloud.tencent.com/document/product/647/45681)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频房间组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 实现聊天室的功能（**IM SDK 使用 iOS 版本**）。


## TUIRoom API 概览

### TUIRoomCore 基础函数

| API| 描述  |
| ----------------------------------- | -------------- |
| [shareInstance](#shareinstance)     | 获取单例对象。 |
| [destroyInstance](#destroyinstance) | 销毁单例对象。 |
| [setDelegate](#setdelegate)         | 设置事件回调。 |

### 房间相关接口函数

| API| 描述 |
| ----------------------------------------- | ---------------------------------- |
| [createRoom](#createroom)                 | 创建房间（主持人调用）。       |
| [destroyRoom](#destroyroom)               | 销毁房间（主持人调用）。       |
| [enterRoom](#enterroom)                   | 进入房间（进入房间成员调用）。 |
| [leaveRoom](#leaveroom)                   | 离开房间（其他房间成员调用）。 |
| [getRoomInfo](#getroominfo)               | 获取房间信息。                 |
| [getRoomUsers](#getroomusers)             | 获取房间内所有成员信息。       |
| [getUserInfo](#getuserinfo)               | 获取某个用户的信息。           |
| [transferRoomMaster](#transferroommaster) | 转移主持人权限（主持人调用）。 |

### 本地音视频操作接口

| API| 描述  |
| ----------------------------------------- | -------------------------- |
| [startCameraPreview](#startcamerapreview) | 开启本地视频的预览画面。   |
| [stopCameraPreview](#stopcamerapreview)   | 停止本地视频采集及预览。   |
| [startLocalAudio](#startlocalaudio)       | 开启麦克风采集。           |
| [stopLocalAudio](#stoplocalaudio)         | 停止麦克风采集。           |
| [setVideoMirror](#setvideomirror)         | 设置本地画面镜像预览模式。 |
| [setSpeaker](#setspeaker)                 | 设置开启扬声器。           |

### 远端用户相关接口

| API| 描述 |
| ----------------------------------- | ---------------------------------- |
| [startRemoteView](#startremoteview) | 订阅并播放指定成员的远端视频画面。 |
| [stopRemoteView](#stopremoteview)   | 取消订阅并停止播放远端视频画面。   |

### 发送聊天消息接口

| API| 描述  |
| ----------------------------------- | -------------- |
| [sendChatMessage](#sendchatmessage)     | 发送聊天消息。   |
| [sendCustomMessage](#sendcustommessage) | 发送自定义消息。 |

### 场控相关接口

| API | 描述 |
| --------------------------------------------------- | ------------------------------------------------------- |
| [muteUserMicrophone](#muteusermicrophone)           | 禁用/恢复某用户的麦克风。                               |
| [muteAllUsersMicrophone](#muteallusersmicrophone)   | 禁用/恢复所有用户的麦克风，并且状态会同步到房间信息中。 |
| [muteUserCamera](#muteusercamera)                   | 禁用/恢复某用户的摄像头。                               |
| [muteAllUsersCamera](#mutealluserscamera)           | 禁用/恢复所有用户的摄像头，并且状态会同步到房间信息中。 |
| [muteChatRoom](#mutechatroom)                       | 开启/停止聊天室禁言（主持人调用）。                     |
| [kickOffUser](#kickoffuser)                         | 移除房间内的某人（主持人调用）。                        |
| [startCallingRoll](#startcallingroll)               | 主持人开始点名。                                        |
| [stopCallingRoll](#stopcallingroll)                 | 主持人结束点名。                                        |
| [replyCallingRoll](#replycallingroll)               | 成员回复主持人点名。                                    |
| [sendSpeechInvitation](#sendspeechinvitation)       | 主持人邀请成员发言。                                    |
| [cancelSpeechInvitation](#cancelspeechinvitation)   | 主持人取消邀请成员发言。                                |
| [replySpeechInvitation](#replyspeechinvitation)     | 成员同意/拒绝主持人的申请发言。                         |
| [sendSpeechApplication](#sendspeechapplication)     | 成员申请发言。                                          |
| [replySpeechApplication](#replyspeechapplication)   | 主持人同意/拒绝成员的申请发言。                         |
| [forbidSpeechApplication](#forbidspeechapplication) | 主持人禁止申请发言。                                    |
| [sendOffSpeaker](#sendoffspeaker)                   | 主持人令成员停止发言。                                  |
| [sendOffAllSpeakers](#sendoffallspeakers)           | 主持人令全体停止发言。                                  |
| [exitSpeechState](#exitspeechstate)                 | 成员停止发言，转变为观众。                              |

### 屏幕分享接口

| API | 描述 |
|-----|-----|
| [startScreenCapture](#startscreencapture) | 启动屏幕分享。 |
| [stopScreenCapture](#stopscreencapture)   | 停止屏幕采集。 |

### 美颜滤镜相关接口函数

| API | 描述 |
|-----|-----|
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。|


### 相关设置接口

| API| 描述 |
| ----------------------------------------------- | ---------------------- |
| [setVideoQosPreference](#setvideoqospreference) | 设置网络流控相关参数。|

### 获取 SDK 版本接口函数

| API  | 描述|
| ------------------------------- | --------------- |
| [getSDKVersion](#getsdkversion) | 获取 SDK 版本。 |

## TUIRoomCoreDelegate API 概览

### 错误事件回调

| API  | 描述 |
| ------------------- | ---------- |
| [onError](#onerror) | 错误回调。 |

### 基础事件回调

| API  | 描述|
| ------------------------------------------- | ------------------ |
| [onDestroyRoom](#ondestroyroom)             | 房间解散回调。     |
| [onUserVoiceVolume](#onuservoicevolume)     | 音量大小回调回调。 |
| [onRoomMasterChanged](#onroommasterchanged) | 主持人更改回调。   |

### 远端用户事件回调

| API | 描述  |
| ------------------------------------------------------------ | -------------------------------- |
| [onRemoteUserEnter](#onremoteuserenter)                      | 远端用户进入房间回调。           |
| [onRemoteUserLeave](#onremoteuserleave)                      | 远端用户离开房间回调。           |
| [onRemoteUserCameraAvailable](#onremoteusercameraavailable)  | 远端用户是否开启摄像头视频回调。 |
| [onRemoteUserScreenVideoAvailable](#onremoteuserscreenvideoavailable) | 远端用户是否开启屏幕分享回调。   |
| [onRemoteUserAudioAvailable](#onremoteuseraudioavailable)    | 远端用户是否开启音频上行回调。   |
| [onRemoteUserEnterSpeechState](#onremoteuserenterspeechstate) | 远端用户开始发言回调。           |
| [onRemoteUserExitSpeechState](#onremoteuserexitspeechstate)  | 远端用户结束发言回调。           |

### 消息事件回调

| API  | 描述|
| ------------------------------------------------- | ------------------ |
| [onReceiveChatMessage](#onreceivechatmessage) | 收到文本消息回调。 |

### 场控事件回调

| API | 描述 |
| ------------------------------------------------------------ | ---------------------------------- |
| [onReceiveSpeechInvitation](#onreceivespeechinvitation)      | 用户收到主持人发言邀请回调。       |
| [onReceiveInvitationCancelled](#onreceiveinvitationcancelled) | 用户收到主持人取消发言邀请回调。   |
| [onReceiveReplyToSpeechInvitation](#onreceivereplytospeechinvitation) | 主持人收到用户同意邀请发言的回调。 |
| [onReceiveSpeechApplication](#onreceivespeechapplication)    | 主持人收到用户发言申请的回调。     |
| [onSpeechApplicationCancelled](#onspeechapplicationcancelled) | 用户取消申请发言回调。             |
| [OnReceiveReplyToSpeechApplication](#onreceivereplytospeechapplication) | 主持人同意发言申请回调。           |
| [onSpeechApplicationForbidden](#onspeechapplicationforbidden) | 主持人禁止申请发言回调。           |
| [onOrderedToExitSpeechState](#onorderedtoexitspeechstate)    | 成员被请求停止发言的回调。         |
| [onCallingRollStarted](#oncallingrollstarted)                | 主持人开始点名，成员收到的回调。   |
| [onCallingRollStopped](#oncallingrollstopped)                | 主持人结束点名，成员收到的回调。   |
| [onMemberReplyCallingRoll](#onmemberreplycallingroll)        | 成员回复点名，主持人收到的回调。   |
| [onChatRoomMuted](#onchatroommuted)                          | 主持人更改聊天室是否禁言回调。     |
| [onMicrophoneMuted](#onmicrophonemuted)                      | 主持人设置禁用麦克风回调。         |
| [onCameraMuted](#oncameramuted)                              | 主持人设置禁用摄像头回调。         |
| [onReceiveKickedOff](#onreceivekickedoff)                    | 成员收到主持人踢人的回调。         |


### 统计和质量回调

| API  | 描述|
| ------------------------------------- | ------------------ |
| [onStatistics](#onstatistics)         | 技术指标统计回调。 |
| [onNetworkQuality](#onnetworkquality) | 网络质量回调。     |

### 屏幕分享相关回调

| API  | 描述|
| ------------------------------------------------- | ------------------ |
| [onScreenCaptureStarted](#onscreencapturestarted) | 开始屏幕分享回调。 |
| [onScreenCaptureStopped](#onscreencapturestopped) | 停止屏幕分享回调。 |

## TUIRoomCore 基础函数

### getInstance

获取 [TUIRoomCore](https://cloud.tencent.com/document/product/647/45681) 单例对象。
```objectivec
+ (instancetype)shareInstance;
```
### destroyInstance

```objectivec
+ (void)destroyInstance;
```

### setDelegate

[TUIRoomCore](https://cloud.tencent.com/document/product/647/45681) 事件回调，您可以通过 TUIRoomCoreDelegate 获得 [TUIRoomCore](https://cloud.tencent.com/document/product/647/45681) 的各种状态通知。

```objectivec
- (void)setDelegate:(id<TUIRoomCoreDelegate>)delegate;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| delegate | TUIRoomCoreDelegate | 接收事件回调类。 |

### createRoom

创建房间（主持人调用）。
```objectivec
- (void)createRoom:(NSString *)roomId
        speechMode:(TUIRoomSpeechMode)speechMode
        callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型 | 含义  |
|-----------| ------------- | -------------------------------------- |
| roomId  | NSString  | 房间标识，需要由您分配并进行统一管理。 |
| speechMode| TUIRoomSpeechMode | 发言模式。|
| callback | TUIRoomActionCallback | 创建房间的结果回调。|

主持人正常调用流程如下：
1. **主持人**调用 `createRoom()` 创建房间，房间创建成功与否会通过 TUIRoomActionCallback 通知给主持人。
2. **主持人**调用 `startCameraPreview()` 打开摄像头采集和预览。
3. **主持人**调用 `startLocalAudio()` 打开本地麦克风。

### destroyRoom

销毁房间房间（主持人调用）。主持人在创建房间后，可以调用该函数来销毁房间。
```objectivec
- (void)destroyRoom:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型 | 含义  |
| ------- | ------ | ---------- |
| callback | TUIRoomActionCallback | 销毁房间的结果回调。 |

### enterRoom

进入房间（加入房间成员调用）。
```objectivec
- (void)enterRoom:(NSString *)roomId
        callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| roomId | NSString | 房间标识。 |
| callback | TUIRoomActionCallback| 结果回调。 |


加入房间成员进入房间的正常调用流程如下：
1. **进入房间成员**调用`enterRoom`并传入 roomId 即可进入房间房间。
2. **进入房间成员**调用 `startCameraPreview()` 打开摄像头预览，调用 `startLocalAudio()` 打开麦克风采集。
3. **进入房间成员**收到`onRemoteUserCameraAvailable`的事件，调用`startRemoteView()`开始播放视频。

### leaveRoom

离开房间（进入房间成员调用）。
```objectivec
 - (void)leaveRoom:(TUIRoomActionCallback)callback;
```

  参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| callback | TUIRoomActionCallback | 结果回调。 |

### getRoomInfo

获取房间信息。
```objectivec
- (nullable TUIRoomInfo *)getRoomInfo;
```

### getRoomUsers

获取房间所有成员信息。
```objectivec
 - (nullable NSArray<TUIRoomUserInfo *> *)getRoomUsers;
```

### getUserInfo

获取房间成员信息。
```objectivec
- (void)getUserInfo:(NSString *)userId
           callback:(TUIRoomUserInfoCallback)callback;
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| userId | NSString | 用户标识。 |
| callback | TUIRoomUserInfoCallback | 房间人员详细信息回调。 |


### setSelfProfile

设置用户信息。
```objectivec
- (void)setSelfProfile:(NSString *)userName
        avatarURL:(NSString *)avatarURL
        callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型| 含义  |
| ---------- | ------ | -------------- |
| userName  | NSString | 用户姓名。  |
| avatarURL | NSString | 用户头像 URL。 |
| callback | TUIRoomActionCallback | 是否设置成功的结果回调。 |


### transferRoomMaster

将群转交给其他用户。
```objectivec
 - (void)transferRoomMaster:(NSString *)userId
                  callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| userId | NSString | 用户标识。 |
| callback | TUIRoomActionCallback| 结果回调。 |


## 本地推流接口

### startCameraPreview

开始本地摄像头预览。
```objectivec
- (void)startCameraPreview:(BOOL)isFront
                      view:(UIView *)view;
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| isFront | BOOL | YES：前置摄像头，NO：后置摄像头。 |
| view | UIView | 承载视频画面的控件。 |


### stopCameraPreview

停止本地摄像头预览。
```objectivec
- (void)stopCameraPreview;
```

### startLocalAudio

开启麦克风采集。
```objectivec
- (void)startLocalAudio:(TRTCAudioQuality)quality;
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| quality | TRTCAudioQuality | 采集的声音音质。 |

### stopLocalAudio

停止麦克风采集
```objectivec
- (void)stopLocalAudio;
```
### setVideoMirror

设置本地画面镜像预览模式。
```objectivec
 - (void)setVideoMirror:(TRTCVideoMirrorType)type;
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| type | TRTCVideoMirrorType | 镜像类型。 |

### setSpeaker

设置开启扬声器。
```objectivec
 - (void)setSpeaker:(BOOL)isUseSpeaker;
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| isUseSpeaker | BOOL | YES：扬声器，NO：听筒。 |

## 远端用户相关接口

### startRemoteView
订阅远端用户的视频流。

```objectivec
- (void)startRemoteView:(NSString *)userId
                   view:(UIView *)view
             streamType:(TUIRoomStreamType)streamType
               callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型 | 含义  |
| -------------- | ------------- | -------------------------- |
| userId  | NSString  | 需要播放的用户 ID。  |
| view | UIView  | 承载视频画面的 view 控件。 |
| streamType  | TUIRoomStreamType | 流类型。|
| callback  | TUIRoomActionCallback | 结果回调。|


### stopRemoteView

取消订阅并停止播放远端视频画面。
```objectivec
- (void)stopRemoteView:(NSString *)userId
            streamType:(TUIRoomStreamType)streamType
              callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型 | 含义  |
| ------- | ------------- | ----------------------- |
| userId | NSString  | 需要停止播放的用户 ID。 |
| streamType | TUIRoomStreamType  | 流类型。 |
| callback  | TUIRoomActionCallback | 结果回调。|

### switchCamera

切换前后摄像头。
```objectivec
- (void)switchCamera:(BOOL)isFront;

```

参数如下表所示：

| 参数 | 类型 | 含义  |
| ------- | ------------- | ----------------------- |
| isFront | BOOL  | YES：前置摄像头；NO：后置摄像头。 |

## 发送消息接口

### sendChatMessage

在房间中广播文本消息，一般用于文本聊天。
```objectivec
- (void)sendChatMessage:(NSString *)message
               callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| message | NSString | 消息内容。 |
| callback  | TUIRoomActionCallback | 发送结果回调。|

## 场控相关接口

### muteUserMicrophone

禁用/恢复某用户的麦克风。
```objectivec
- (void)muteUserMicrophone:(NSString *)userId
                      mute:(BOOL)mute
                  callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | NSString| 用户 ID。  |
| mute  | BOOL  | 是否禁用。 |
| callback | TUIRoomActionCallback | 结果回调。 |

### muteAllUsersMicrophone

禁用/恢复所有用户的麦克风。
```objectivec
- (void)muteAllUsersMicrophone:(BOOL)mute
                      callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
| ---- | ---- | ---------- |
| mute | BOOL | 是否禁用。 |
| callback | TUIRoomActionCallback | 结果回调。 |


### muteUserCamera

禁用/恢复某用户的摄像头。
```objectivec
- (void)muteUserCamera:(NSString *)userId
                  mute:(BOOL)mute
              callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | NSString| 用户 ID。  |
| mute  | BOOL  | 是否禁用。 |
| callback | TUIRoomActionCallback | 结果回调。 |

### muteAllUsersCamera

禁用/恢复所有用户的摄像头。
```objectivec
- (void)muteAllUsersCamera:(BOOL)mute
                  callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
| ---- | ---- | ---------- |
| mute  | BOOL  | 是否禁用。 |
| callback | TUIRoomActionCallback | 结果回调。 |

### muteChatRoom

禁言/恢复文字聊天。
```objectivec
- (void)muteChatRoom:(BOOL)mute
            callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
| ---- | ---- | ---------- |
| mute  | BOOL  | 是否禁用。 |
| callback | TUIRoomActionCallback | 结果回调。 |


### kickOffUser

主持人踢人。
```objectivec
- (void)kickOffUser:(NSString *)userId
           callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | NSString| 用户 ID。  |
| callback | TUIRoomActionCallback | 结果回调。 |

### startCallingRoll

主持人开始点名。
```objectivec
 - (void)startCallingRoll:(TUIRoomActionCallback)callback;
```
参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomActionCallback | 结果回调。 |

### stopCallingRoll

主持人结束点名。
```objectivec
- (void)stopCallingRoll:(TUIRoomActionCallback)callback;
```
参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomActionCallback | 结果回调。 |

### replyCallingRoll

成员回复主持人点名。
```objectivec
- (void)replyCallingRoll:(TUIRoomActionCallback)callback;
```
参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomActionCallback | 结果回调。 |

### sendSpeechInvitation

主持人邀请成员发言。
```objectivec
- (void)sendSpeechInvitation:(NSString *)userId
                    callback:(TUIRoomInviteeCallback)callback
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | NSString| 用户 ID。  |
| callback | TUIRoomInviteeCallback | 结果回调。 |

### cancelSpeechInvitation

主持人取消邀请成员发言。
```objectivec
- (void)cancelSpeechInvitation:(NSString *)userId
                      callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | NSString| 用户 ID。  |
| callback | TUIRoomActionCallback | 结果回调。 |

### replySpeechInvitation

成员同意/拒绝主持人的发言邀请。
```objectivec
- (void)replySpeechInvitation:(BOOL)agree
                     callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| agree | BOOL  | 是否同意。 |
| callback | TUIRoomActionCallback | 结果回调。 |

### sendSpeechApplication

成员申请发言。
```objectivec
- (void)sendSpeechApplication:(TUIRoomInviteeCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomInviteeCallback | 结果回调。 |

### cancelSpeechApplication

成员取消申请发言。
```objectivec
- (void)cancelSpeechApplication:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomActionCallback| 结果回调。 |

### replySpeechApplication

主持人同意/拒绝成员的申请发言。
```objectivec
- (void)replySpeechApplication:(BOOL)agree
                        userId:(NSString *)userId
                      callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| agree  | BOOL| 是否同意  |
| userId  | NSString| 用户 ID。  |
| callback | TUIRoomActionCallback | 结果回调。 |

### forbidSpeechApplication

主持人禁止申请发言。
```objectivec
- (void)forbidSpeechApplication:(BOOL)forbid
                       callback:(TUIRoomActionCallback)callback;
```

参数如下表所示：

| 参数| 类型 | 含义 |
| ------ | ---- | ---------- |
| forbid | BOOL | 是否禁止。 |
| callback | TUIRoomActionCallback | 结果回调。 |


### sendOffSpeaker

主持人令成员停止发言。
```objectivec
- (void)sendOffSpeaker:(NSString *)userId
              callback:(TUIRoomInviteeCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | NSString| 用户 ID。  |
| callback | TUIRoomInviteeCallback | 结果回调。 |

### sendOffAllSpeakers

主持人令所有成员停止发言。
```objectivec
- (void)sendOffAllSpeakers:(TUIRoomInviteeCallback)callback;
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomInviteeCallback| 结果回调。 |

### exitSpeechState

成员停止发言，转变为观众。
```objectivec
- (void)exitSpeechState:(TUIRoomActionCallback)callback;
```
参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomActionCallback | 结果回调。 |


## 屏幕分享接口
### startScreenCapture

启动屏幕分享。
```objectivec
- (void)startScreenCapture:(TRTCVideoEncParam *)encParam API_AVAILABLE(ios(11.0));
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| encParams | TRTCVideoEncParam | 设置屏幕分享时的编码参数。 |

>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58)

### stopScreenCapture

停止屏幕采集。
```objectivec
- (void)stopScreenCapture API_AVAILABLE(ios(11.0));
```

## 美颜滤镜相关接口函数
### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。
```objectivec
- (TXBeautyManager *)getBeautyManager;
```

通过美颜管理，您可以使用以下功能：
- 设置“美颜风格”、“美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。

## 相关设置接口

### setVideoQosPreference

设置网络流控相关参数。
```objectivec
- (void)setVideoQosPreference:(TRTCNetworkQosParam *)preference;
```

参数如下表所示：

| 参数 | 类型| 含义  |
| ---------- | --------------------- | -------------- |
| preference | TRTCNetworkQosParam | 网络流控策略。 |

### setAudioQuality

设置音质
```objectivec
- (void)setAudioQuality:(TRTCAudioQuality)quality;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | TRTCAudioQuality | 音频质量，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a955cccaddccb0c993351c656067bee55) |

### setVideoResolution

设置分辨率。

```objectivec
- (void)setVideoResolution:(TRTCVideoResolution)resolution;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| resolution | TRTCVideoResolution | 视频分辨率，详细请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#aa3b72c532f3ffdf64c6aacab26be5f87)。 |


### setVideoFps

设置帧率。
```objectivec
- (void)setVideoFps:(int)fps;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| fps | int | 视频采集帧率。 |

>?**推荐取值**：15fps或20fps，5fps以下，卡顿感明显。10fps以下，会有轻微卡顿感。20fps以上，则过于浪费（电影的帧率为24fps）。


### setVideoBitrate

设置码率。
```objectivec
- (void)setVideoBitrate:(int)bitrate;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bitrate | int | 码率，SDK 会按照目标码率进行编码，只有在网络不佳的情况下才会主动降低视频码率。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html)。 |

>? **推荐取值**：请参考 TRTCVideoResolution 在各档位注释的最佳码率，也可以在此基础上适当调高。 例如 TRTC_VIDEO_RESOLUTION_1280_720 对应1200kbps的目标码率，您也可以设置为1500kbps以便获得更好的清晰度观感。

### enableAudioEvaluation

启用音量大小提示。
```objectivec
- (void)enableAudioEvaluation:(BOOL)enable;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | BOOL | YES：打开，NO：关闭。 |

>? 开启后会在 onUserVolumeUpdate 中获取到 SDK 对音量大小值的评估。

### setAudioPlayVolume

设置播放音量。
```objectivec
- (void)setAudioPlayVolume:(NSInteger)volume;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 播放音量，0-100， 默认100。 |

### setAudioCaptureVolume

设置麦克风采集音量。
```objectivec
- (void)setAudioCaptureVolume:(NSInteger)volume;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 采集音量，0-100， 默认100。 |

### startFileDumping

开始录音。
```objectivec
- (void)startFileDumping:(TRTCAudioRecordingParams *)params;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| params | TRTCAudioRecordingParams | 录音参数，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCAudioRecordingParams) |

>? 该方法调用后， SDK 会将通话过程中的所有音频（包括本地音频，远端音频，BGM 等）录制到一个文件里。无论是否进房，调用该接口都生效。如果调用 leaveRoom 时还在录音，录音会自动停止。

### stopFileDumping

停止录音。
```objectivec
- (void)stopFileDumping;
```

## 获取 SDK 版本接口

### getSdkVersion

获取 SDK 版本信息。
```objectivec
- (NSInteger)getSdkVersion;
```

## 错误事件回调
### onError

```objectivec
- (void)onError:(NSInteger)code message:(NSString *)message;
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| code | NSInteger | 错误码。|
| message | NSString | 错误信息。 |

## 基础事件回调

### onDestroyRoom

房间解散回调。
```objectivec
- (void)onDestroyRoom;
```

### onUserVoiceVolume

用户音量大小回调。
```objectivec
- (void)onUserVoiceVolume:(NSString *)userId volume:(NSInteger)volume;
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------------------------------- |
| userId | NSString | 用户 ID。  |
| volume  | NSInteger | 用户的音量大小，取值范围 0 - 100。 |

### onRoomMasterChanged

主持人更改回调。
```objectivec
- (void)onRoomMasterChanged:(NSString *)previousUserId
              currentUserId:(NSString *)currentUserId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| previousUserId | NSString | 更改前的主持人用户 ID。 |
| currentUserId | NSString | 更改后的主持人用户 ID。 |


## 远端用户回调事件

### onRemoteUserEnter

远端用户进入房间回调。
```objectivec
- (void)onRemoteUserEnter:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | NSString | 用户 ID。 |

### onRemoteUserLeave

远端用户离开房间回调。
```objectivec
- (void)onRemoteUserLeave:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | NSString | 用户 ID。 |

### onRemoteUserCameraAvailable

远端用户是否开启摄像头视频。
```objectivec
- (void)onRemoteUserCameraAvailable:(NSString *)userId
                          available:(BOOL)available;
```

参数如下表所示：

| 参数| 类型| 含义  |
| --------- | ------ | ----------------------------------------- |
| userId| NSString | 用户 ID。|
| available | BOOL| YES：有视频流数据；NO：无视频流数据。 |

### onRemoteUserScreenVideoAvailable

成员**开启**/**关闭**视频分享的通知。
```objectivec
- (void)onRemoteUserScreenVideoAvailable:(NSString *)userId
                               available:(BOOL)available;
```

参数如下表所示：

| 参数| 类型| 含义  |
| --------- | ------ | ----------------------------------------- |
| userId| NSString | 用户 ID。|
| available | BOOL| 是否有屏幕分享流数据。 |

### onRemoteUserAudioAvailable

远端用户是否开启音频上行回调。
```objectivec
- (void)onRemoteUserAudioAvailable:(NSString *)userId
                         available:(BOOL)available;
```

参数如下表所示：

| 参数| 类型| 含义  |
| --------- | ------ | ----------------------------------------- |
| userId| NSString | 用户 ID。|
| available | BOOL| 是否有音频数据。 |

### onRemoteUserEnterSpeechState

远端用户开始发言。
```objectivec
- (void)onRemoteUserEnterSpeechState:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | NSString | 用户 ID。 |

### onRemoteUserExitSpeechState

远端用户结束发言。
```objectivec
- (void)onRemoteUserExitSpeechState:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | NSString | 用户 ID。 |


## 聊天室消息事件回调

### onReceiveChatMessage

收到文本消息。
```objectivec
- (void)onReceiveChatMessage:(NSString *)userId message:(NSString *)message;
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| userId | NSString | 用户 ID。  |
| message | NSString | 文本消息。 |


## 场控消息回调

### onReceiveSpeechInvitation

用户收到主持人发言邀请回调。
```objectivec
- (void)onReceiveSpeechInvitation:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | NSString | 主持人用户 ID。 |

### onReceiveInvitationCancelled

用户收到主持人取消发言邀请回调。
```objectivec
- (void)onReceiveInvitationCancelled:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | NSString | 主持人用户 ID。 |

### OnReceiveSpeechApplication

主持人收到用户发言申请的回调。
```objectivec
void onReceiveSpeechApplication(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | NSString | 用户 ID。 |

### onSpeechApplicationCancelled

用户取消申请发言回调。
```objectivec
- (void)onSpeechApplicationCancelled:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | NSString | 用户 ID。 |

### onSpeechApplicationForbidden

主持人禁止申请发言回调。
```objectivec
- (void)onSpeechApplicationForbidden:(BOOL)isForbidden userId:(NSString *)userId;
```

参数如下表所示：

| 参数| 类型 | 含义 |
| --------- | ---- | ---------- |
| isForbidden | BOOL | 是否禁止。 |
| userId | NSString | 用户 ID。 |

### onOrderedToExitSpeechState

成员被请求停止发言的回调。
```objectivec
- (void)onOrderedToExitSpeechState:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | NSString | 主持人用户ID。 |


### onCallingRollStarted

主持人开始点名，成员收到的回调。
```objectivec
- (void)onCallingRollStarted:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | NSString | 主持人用户 ID。 |

### onCallingRollStopped

主持人结束点名，成员收到的回调。
```objectivec
- (void)onCallingRollStopped:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | NSString | 主持人用户 ID。 |

### onMemberReplyCallingRoll

成员回复点名，主持人收到的回调。
```objectivec
- (void)onMemberReplyCallingRoll:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | NSString | 用户 ID。 |

### onChatRoomMuted

主持人更改聊天室是否禁言回调。
```objectivec
- (void)onChatRoomMuted:(BOOL)muted userId:(NSString *)userId;
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| muted | BOOL | 是否禁用。 |
| userId | NSString | 主持人用户 ID。 |

### onMicrophoneMuted

主持人设置禁用麦克风回调。
```objectivec
- (void)onMicrophoneMuted:(BOOL)muted userId:(NSString *)userId;
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| muted | BOOL | 是否禁用。 |
| userId | NSString | 主持人用户 ID。 |

### onCameraMuted

主持人设置禁用摄像头回调。
```objectivec
- (void)onCameraMuted:(BOOL)muted userId:(NSString *)userId;
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| muted | BOOL | 是否禁用。 |
| userId | NSString | 主持人用户 ID。 |

### onReceiveKickedOff

主持人踢人的回调。
```objectivec
- (void)onReceiveKickedOff:(NSString *)userId;
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| userId | NSString | 主持人/管理员 用户 ID。 |

## 统计和质量回调

### onStatistics

技术指标统计回调。
```objectivec
- (void)onStatistics:(TRTCStatistics *)statistics;
```

参数如下表所示：

| 参数| 类型 | 含义 |
| ------ | ---------------------- | ---------- |
| statis | TRTCStatistics | 统计数据。 |

### onNetworkQuality

网络状况回调。
```objectivec
- (void)onNetworkQuality:(TRTCQualityInfo *)localQuality remoteQuality:(NSArray<TRTCQualityInfo *> *)remoteQuality;

```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| localQuality | TRTCQualityInfo | 上行网络质量。 |
| remoteQuality |NSArray&lt;TRTCQualityInfo *&gt; | 下行网络质量。 |

>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aba07d4191391dadef900422521f34e5b)。


## 屏幕分享事件回调

### onScreenCaptureStarted

开始屏幕分享回调。

```objectivec
 - (void)onScreenCaptureStarted;
```

### onScreenCaptureStopped

停止屏幕分享回调。

```objectivec
- (void)onScreenCaptureStopped:(NSInteger)reason;
```

参数如下表所示：

| 参数| 类型 | 含义|
| ------ | ---- | ------------------------------------------------------ |
| reason | NSInteger  | 停止原因，0：用户主动停止；1：被其他应用抢占导致停止。 |
