1. TUIRoom 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建房间，进入房间人员输入房间号后进入房间。
- 进入房间人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TUIRoom 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人音视频互动(Android)](https://cloud.tencent.com/document/product/647/45667)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频房间组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 实现聊天室的功能（**IM SDK 使用 Android 版本**）。


## TUIRoom API 概览

### TUIRoomCore 基础函数

| API| 描述  |
| ----------------------------------- | -------------- |
| [getInstance](#getinstance)         | 获取单例对象。 |
| [destroyInstance](#destroyinstance) | 销毁单例对象。 |
| [setListener](#setlistener)         | 设置事件回调。 |

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
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager。](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager) |


### 相关设置接口

| API| 描述 |
| ----------------------------------------------- | ---------------------- |
| [setVideoQosPreference](#setvideoqospreference) | 设置网络流控相关参数。 |

### 获取 SDK 版本接口函数

| API  | 描述|
| ------------------------------- | --------------- |
| [getSDKVersion](#getsdkversion) | 获取 SDK 版本。 |

## TUIRoomCoreListener API 概览[](id:TUIRoomCoreListener)

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
| [onReceiveChatMessage](#onreceivechatmessage)     | 收到文本消息回调。   |
| [onReceiveRoomCustomMsg](#onreceiveroomcustommsg) | 收到自定义消息回调。 |

### 场控事件回调

| API | 描述 |
| ------------------------------------------------------------ | ---------------------------------- |
| [onReceiveSpeechInvitation](#onreceivespeechinvitation)      | 用户收到主持人发言邀请回调。       |
| [onReceiveInvitationCancelled](#onreceiveinvitationcancelled) | 用户收到主持人取消发言邀请回调。   |
| [onReceiveReplyToSpeechInvitation](#onreceivereplytospeechinvitation) | 主持人收到用户同意邀请发言的回调。 |
| [onReceiveSpeechApplication](#onreceivespeechapplication)    | 主持人收到用户发言申请的回调。     |
| [onSpeechApplicationCancelled](#onspeechapplicationcancelled) | 用户取消申请发言回调。             |
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

获取 [TUIRoomCore](https://cloud.tencent.com/document/product/647/45667) 单例对象。
```java
public static TUIRoomCore getInstance(Context context);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| context | Context | Android 上下文，内部会转为 ApplicationContext 用于系统 API 调用。 |


### destroyInstance

```java
void destroyInstance();
```

### setListener

[TUIRoomCore](https://cloud.tencent.com/document/product/647/45667) 事件回调，您可以通过 TUIRoomCoreListener 获得 [TUIRoomCore](https://cloud.tencent.com/document/product/647/45667) 的各种状态通知。

```java
void setListener(TUIRoomCoreListener listener);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | TUIRoomCoreListener | 接收事件回调类。 |

### createRoom

创建房间（主持人调用）。
```java
void createRoom(String roomId, TUIRoomCoreDef.SpeechMode speechMode, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型 | 含义  |
|-----------| ------------- | -------------------------------------- |
| roomId  | String  | 房间标识，需要由您分配并进行统一管理。 |
| speechMode| TUIRoomCoreDef.SpeechMode | 发言模式。|
| callback | TUIRoomCoreCallback.ActionCallback | 创建房间的结果回调。|

主持人正常调用流程如下：
1. **主持人**调用 `createRoom()` 创建房间，房间创建成功与否会通过 `TUIRoomCoreCallback.ActionCallback` 通知给主持人。
2. **主持人**调用 `startCameraPreview()` 打开摄像头采集和预览。
3. **主持人**调用 `startLocalAudio()` 打开本地麦克风。

### destroyRoom

销毁房间房间（主持人调用），主持人在创建房间后，可以调用该函数来销毁房间。
```java
void destroyRoom(TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型 | 含义  |
| ------- | ------ | ---------- |
| callback | UIRoomCoreCallback.ActionCallback | 销毁房间的结果回调。 |

### enterRoom

进入房间（加入房间成员调用）。
```java
void enterRoom(String roomId, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| roomId | String | 房间标识。 |
| callback | UIRoomCoreCallback.ActionCallback | 结果回调。  |


加入房间成员进入房间的正常调用流程如下：
1. **进入房间成员**调用 `enterRoom` 并传入 roomId 即可进入房间房间。
2. **进入房间成员**调用 `startCameraPreview()` 打开摄像头预览，调用 `startLocalAudio()` 打开麦克风采集。
3. **进入房间成员**收到 `onRemoteUserCameraAvailable` 的事件，调用 `startRemoteView()`开始播放视频。

### leaveRoom

离开房间（进入房间成员调用）。
```java
 void leaveRoom(TUIRoomCoreCallback.ActionCallback callback);
```

  参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| callback | UIRoomCoreCallback.ActionCallback | 结果回调。

### getRoomInfo

获取房间信息。
```java
TUIRoomCoreDef.RoomInfo getRoomInfo();
```

### getRoomUsers

获取房间所有成员信息。
```java
 List<TUIRoomCoreDef.UserInfo> getRoomUsers();
```

### getUserInfo

获取房间成员信息。
```java
void getUserInfo(String userId, TUIRoomCoreCallback.UserInfoCallback callback);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| userId | String | 用户标识。 |
| callback | UIRoomCoreCallback.UserInfoCallback | 房间人员详细信息回调。 |


### setSelfProfile

设置用户信息。
```java
void setSelfProfile(String userName, String avatarURL, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型| 含义  |
| ---------- | ------ | -------------- |
| userName  | String | 用户姓名。  |
| avatarURL | String | 用户头像 URL。 |
| callback | TUIRoomCoreCallback.ActionCallback | 是否设置成功的结果回调。 |


### transferRoomMaster

将群转交给其他用户。
```java
 void transferRoomMaster(String userId, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| userId | String | 用户标识。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |


## 本地推流接口

### startCameraPreview

开始本地摄像头预览。
```java
void startCameraPreview(boolean isFront, TXCloudVideoView view);
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| isFront | boolean | true：前置摄像头；false：后置摄像头。 |
| view | TXCloudVideoView | 承载视频画面的控件。 |


### stopCameraPreview

停止本地摄像头预览。
```java
 void stopCameraPreview();
```

### startLocalAudio

开启麦克风采集。
```java
 void startLocalAudio(int quality);
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| quality | int | 采集的声音音质：<li/>TRTC_AUDIO_QUALITY_MUSIC<li/>TRTC_AUDIO_QUALITY_DEFAULT<li/>TRTC_AUDIO_QUALITY_SPEECH |

### stopLocalAudio

停止麦克风采集
```java
void stopLocalAudio();
```

### setVideoMirror

设置本地画面镜像预览模式。
```java
 void setVideoMirror(int type);
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| type | int | 镜像类型。 |

### setSpeaker

设置开启扬声器。
```java
 void setSpeaker(boolean isUseSpeaker);
```

参数如下表所示：

| 参数 | 类型  | 含义 |
| ---- | -------------- | ---------- |
| isUseSpeaker | boolean | true：扬声器，false：听筒。 |

## 远端用户相关接口

### startRemoteView
订阅远端用户的视频流。

```java
void startRemoteView(String userId, TXCloudVideoView view, TUIRoomCoreDef.SteamType streamType, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型 | 含义  |
| -------------- | ------------- | -------------------------- |
| userId  | String  | 需要播放的用户 ID。  |
| view | TXCloudVideoView  | 承载视频画面的 view 控件。 |
| streamType  | TUIRoomCoreDef.SteamType | 流类型。|
| callback  | TUIRoomCoreCallback.ActionCallback | 结果回调。|


### stopRemoteView

取消订阅并停止播放远端视频画面。
```java
void stopRemoteView(String userId, TUIRoomCoreCallback.ActionCallback callback);

```

参数如下表所示：

| 参数 | 类型 | 含义  |
| ------- | ------------- | ----------------------- |
| userId | String  | 需要停止播放的用户 ID。 |
| callback  | TUIRoomCoreCallback.ActionCallback | 结果回调。|

### switchCamera

切换前后摄像头。
```java
void switchCamera(boolean isFront);

```

参数如下表所示：

| 参数 | 类型 | 含义  |
| ------- | ------------- | ----------------------- |
| isFront | boolean  | true：前置摄像头；false：后置摄像头。 |

## 发送消息接口

### sendChatMessage

在房间中广播文本消息，一般用于文本聊天。
```java
void sendChatMessage(String message, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| message | String | 消息内容。 |
| callback  | TUIRoomCoreCallback.ActionCallback | 发送结果回调。|


### sendCustomMessage

发送自定义消息。
```java
void sendCustomMessage(String data, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| data | String | 消息内容。 |
| callback  | TUIRoomCoreCallback.ActionCallback | 发送结果回调。|

## 场控相关接口

### muteUserMicrophone

禁用/恢复某用户的麦克风。
```java
void muteUserMicrophone(String userId, boolean mute, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | String| 用户 ID。  |
| mute  | boolean  | 是否禁用。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### muteAllUsersMicrophone

禁用/恢复所有用户的麦克风。
```java
void muteAllUsersMicrophone(boolean mute, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
| ---- | ---- | ---------- |
| mute | boolean | 是否禁用。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |


### muteUserCamera

禁用/恢复某用户的摄像头。
```java
void muteUserCamera(String userId, boolean mute, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | String| 用户 ID。  |
| mute  | boolean  | 是否禁用。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### muteAllUsersCamera

禁用/恢复所有用户的摄像头。
```java
void muteAllUsersCamera(boolean mute, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
| ---- | ---- | ---------- |
| mute  | boolean  | 是否禁用。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### muteChatRoom

禁言/恢复文字聊天。
```java
void muteChatRoom(boolean mute, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
| ---- | ---- | ---------- |
| mute  | boolean  | 是否禁用。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |


### kickOffUser

主持人踢人。
```java
void kickOffUser(String userId, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | String| 用户 ID。  |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### startCallingRoll

主持人开始点名。
```java
 void startCallingRoll(TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### stopCallingRoll

主持人结束点名。
```java
 void stopCallingRoll(TUIRoomCoreCallback.ActionCallback callback);
 
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### replyCallingRoll

成员回复主持人点名。
```java
void replyCallingRoll(TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |


### sendSpeechInvitation

主持人邀请成员发言。
```java
void sendSpeechInvitation(String userId, TUIRoomCoreCallback.InvitationCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | String| 用户 ID。  |
| callback | TUIRoomCoreCallback.InvitationCallback | 结果回调。 |

### cancelSpeechInvitation

主持人取消邀请成员发言。
```java
 void cancelSpeechInvitation(String userId, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | String| 用户 ID。  |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### replySpeechInvitation

成员同意/拒绝主持人的发言邀请。
```java
void replySpeechInvitation(boolean agree, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| agree | boolean  | 是否同意。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### sendSpeechApplication

成员申请发言。
```java
void sendSpeechApplication(TUIRoomCoreCallback.InvitationCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomCoreCallback.InvitationCallback | 结果回调。 |

### cancelSpeechApplication

成员取消申请发言。
```java
void cancelSpeechApplication(TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### replySpeechApplication

主持人同意/拒绝成员的申请发言。
```java
void replySpeechApplication(boolean agree, String userId, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| agree  | boolean| 是否同意。 |
| userId  | String| 用户 ID。  |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### forbidSpeechApplication

主持人禁止申请发言。
```java
 void forbidSpeechApplication(boolean forbid, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数| 类型 | 含义 |
| ------ | ---- | ---------- |
| forbid | boolean | 是否禁止。 |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |


### sendOffSpeaker

主持人令成员停止发言。
```java
void sendOffSpeaker(String userId, TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| userId  | String| 用户 ID。  |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### sendOffAllSpeakers

主持人令所有成员停止发言。
```java
void sendOffAllSpeakers(TUIRoomCoreCallback.ActionCallback callback);
```

参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |

### exitSpeechState

成员停止发言，转变为观众。
```java
void exitSpeechState(TUIRoomCoreCallback.ActionCallback callback);
```
参数如下表所示：

| 参数  | 类型  | 含义 |
| -------- | -------- | ---------- |
| callback | TUIRoomCoreCallback.ActionCallback | 结果回调。 |


## 屏幕分享接口
### startScreenCapture

启动屏幕分享。
```java
void startScreenCapture(TRTCCloudDef.TRTCVideoEncParam encParams, TRTCCloudDef.TRTCScreenShareParams screenShareParams);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| encParams | TRTCCloudDef.TRTCVideoEncParam | 设置屏幕分享时的编码参数，推荐采用上述推荐配置，如果您指定 encParams 为 null，则使用您调用 startScreenCapture 之前的编码参数设置。 |
| screenShareParams | TRTCCloudDef.TRTCScreenShareParams | 设置屏幕分享的特殊配置，其中推荐设置 floatingView，一方面可以避免 App 被系统强杀；另一方面也能助于保护用户隐私。 |

>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58)。

### stopScreenCapture

停止屏幕采集。
```java
void stopScreenCapture();
```

## 美颜滤镜相关接口函数
### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。
```java
TXBeautyManager getBeautyManager();
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
```java
 void setVideoQosPreference(TRTCCloudDef.TRTCNetworkQosParam preference);
```

参数如下表所示：

| 参数 | 类型| 含义  |
| ---------- | --------------------- | -------------- |
| preference | TRTCCloudDef.TRTCNetworkQosParam | 网络流控策略。 |

### setAudioQuality

设置音质。
```java
void setAudioQuality(int quality);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | int | 音频质量，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a955cccaddccb0c993351c656067bee55)。 |

### setVideoResolution

设置分辨率。

```java
void setVideoResolution(int resolution);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| resolution | int | 视频分辨率，详细请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#aa3b72c532f3ffdf64c6aacab26be5f87)。 |


### setVideoFps

设置帧率。
```java
void setVideoFps(int fps);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| fps | int | 视频采集帧率。 |

>?**推荐取值**：15fps或20fps，5fps以下，卡顿感明显。10fps以下，会有轻微卡顿感。20fps以上，则过于浪费（电影的帧率为24fps）。


### setVideoBitrate

设置码率。
```java
void setVideoBitrate(int bitrate);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bitrate | int | 码率，SDK 会按照目标码率进行编码，只有在网络不佳的情况下才会主动降低视频码率。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html)。 |

>? **推荐取值**：请参考 TRTCVideoResolution 在各档位注释的最佳码率，也可以在此基础上适当调高。 例如 TRTC_VIDEO_RESOLUTION_1280_720 对应1200kbps的目标码率，您也可以设置为1500kbps以便获得更好的清晰度观感。

### enableAudioEvaluation

启用音量大小提示。
```java
void enableAudioEvaluation(boolean enable);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：打开，false：关闭。 |

>? 开启后会在 onUserVolumeUpdate 中获取到 SDK 对音量大小值的评估。

### setAudioPlayVolume

设置播放音量。
```java
void setAudioPlayVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 播放音量，0-100， 默认100。 |

### setAudioCaptureVolume

设置麦克风采集音量
```java
void setAudioCaptureVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 采集音量，0-100， 默认100。 |

### startFileDumping

开始录音。
```java
void startFileDumping(TRTCCloudDef.TRTCAudioRecordingParams trtcAudioRecordingParams);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| trtcAudioRecordingParams | TRTCCloudDef.TRTCAudioRecordingParams | 录音参数，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCAudioRecordingParams)。 |

>? 该方法调用后， SDK 会将通话过程中的所有音频（包括本地音频，远端音频，BGM 等）录制到一个文件里。无论是否进房，调用该接口都生效。如果调用 leaveRoom 时还在录音，录音会自动停止。

### stopFileDumping

停止录音。
```java
void stopFileDumping();
```

## 获取 SDK 版本接口

### getSdkVersion

获取 SDK 版本信息。
```java
int getSdkVersion();
```

## 错误事件回调
### onError

```java
void onError(int code, String message);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| code | int | 错误码。|
| message | String | 错误信息。 |

## 基础事件回调

### onDestroyRoom

房间解散回调。
```java
void onDestroyRoom();
```

### onUserVoiceVolume

用户音量大小回调。
```java
void onUserVoiceVolume(String userId, int volume);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------------------------------- |
| userId | String | 用户 ID。  |
| volume  | int | 用户的音量大小，取值范围 0 - 100。 |

### onRoomMasterChanged

主持人更改回调。
```java
void onRoomMasterChanged(String previousUserId, String currentUserId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| previousUserId | String | 更改前的主持人用户 ID。 |
| currentUserId | String | 更改后的主持人用户 ID。 |


## 远端用户回调事件

### onRemoteUserEnter

远端用户进入房间回调。
```java
void onRemoteUserEnter(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | String | 用户 ID。 |

### onRemoteUserLeave

远端用户离开房间回调。
```java
void onRemoteUserLeave(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | String | 用户 ID。 |

### onRemoteUserCameraAvailable

远端用户是否开启摄像头视频。
```java
void onRemoteUserCameraAvailable(String userId, boolean available);
```

参数如下表所示：

| 参数| 类型| 含义  |
| --------- | ------ | ----------------------------------------- |
| userId| String | 用户 ID。|
| available | boolean| true：有视频流数据；false：无视频流数据。 |

### onRemoteUserScreenVideoAvailable

成员**开启**/**关闭**视频分享的通知。
```java
void onRemoteUserScreenVideoAvailable(String userId, boolean available);
```

参数如下表所示：

| 参数| 类型| 含义  |
| --------- | ------ | ----------------------------------------- |
| userId| String | 用户 ID。|
| available | boolean| 是否有屏幕分享流数据。 |

### onRemoteUserAudioAvailable

远端用户是否开启音频上行回调。
```java
void onRemoteUserAudioAvailable(String userId, boolean available);
```

参数如下表所示：

| 参数| 类型| 含义  |
| --------- | ------ | ----------------------------------------- |
| userId| String | 用户 ID。|
| available | boolean| 是否有音频数据。 |

### onRemoteUserEnterSpeechState

远端用户开始发言。
```java
void onRemoteUserEnterSpeechState(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | String | 用户 ID。 |

### onRemoteUserExitSpeechState

远端用户结束发言。
```java
void onRemoteUserExitSpeechState(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | String | 用户 ID。 |


## 聊天室消息事件回调

### onReceiveChatMessage

收到文本消息。
```java
void onReceiveChatMessage(String userId, String message);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| userId | String | 用户 ID。  |
| message | String | 文本消息。 |

### onReceiveRoomCustomMsg

收到自定义消息。
```java
void onReceiveRoomCustomMsg(String userId, String data);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | String | 用户 ID。 |
| message | String | 自定义消息。 |

## 场控消息回调

### onReceiveSpeechInvitation

用户收到主持人发言邀请回调。
```java
void onReceiveSpeechInvitation(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | String | 主持人用户 ID。 |

### onReceiveInvitationCancelled

用户收到主持人取消发言邀请回调。
```java
void onReceiveInvitationCancelled(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | String | 主持人用户 ID。 |

### onReceiveReplyToSpeechInvitation

主持人收到用户同意邀请发言的回调。
```java
void onReceiveReplyToSpeechInvitation(String userId, boolean agree);
```

参数如下表所示：

| 参数 | 类型| 含义 |
| ------- | ------ | ---------- |
| userId | String | 用户 ID。  |
| agree| boolean| 是否同意。 |

### onReceiveSpeechApplication

主持人收到用户发言申请的回调。
```java
void onReceiveSpeechApplication(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | String | 用户 ID。 |

### onSpeechApplicationCancelled

用户取消申请发言回调。
```java
void onSpeechApplicationCancelled(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | String | 用户 ID。 |

### onSpeechApplicationForbidden

主持人禁止申请发言回调。
```java
void onSpeechApplicationForbidden(boolean isForbidden);
```

参数如下表所示：

| 参数| 类型 | 含义 |
| --------- | ---- | ---------- |
| isForbidden | boolean | 是否禁止。 |

### onOrderedToExitSpeechState

成员被请求停止发言的回调。
```java
void onOrderedToExitSpeechState(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | ------------ |
| userId | String | 主持人用户 ID。 |


### onCallingRollStarted

主持人开始点名，成员收到的回调。
```java
void onCallingRollStarted(String userId);
```

### onCallingRollStopped

主持人结束点名，成员收到的回调。
```java
void onCallingRollStopped(String userId);
```

### onMemberReplyCallingRoll

成员回复点名，主持人收到的回调。
```java
void onMemberReplyCallingRoll(String userId);
```

参数如下表所示：

| 参数 | 类型| 含义|
| ------- | ------ | --------- |
| userId | String | 用户 ID。 |

### onChatRoomMuted

主持人更改聊天室是否禁言回调。
```java
void onChatRoomMuted(boolean muted);
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| muted | boolean | 是否禁用。 |

### onMicrophoneMuted

主持人设置禁用麦克风回调。
```java
void onMicrophoneMuted(boolean muted);
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| muted | boolean | 是否禁用。 |

### onCameraMuted

主持人设置禁用摄像头回调。
```java
void onCameraMuted(boolean muted);
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| muted | boolean | 是否禁用。 |

### onReceiveKickedOff

主持人踢人的回调。
```java
void onReceiveKickedOff(String userId);
```

参数如下表所示：

| 参数  | 类型 | 含义 |
| ----- | ---- | ---------- |
| userId | String | 主持人/管理员 用户 ID。 |

## 统计和质量回调

### onStatistics

技术指标统计回调。
```java
void onStatistics(TRTCStatistics statistics);
```

参数如下表所示：

| 参数| 类型 | 含义 |
| ------ | ---------------------- | ---------- |
| statis | TRTCStatistics | 统计数据。 |

### onNetworkQuality

网络状况回调。
```java
void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality, List<TRTCCloudDef.TRTCQuality> remoteQuality);

```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| localQuality | TRTCCloudDef.TRTCQuality | 上行网络质量。 |
| remoteQuality | List&amp;lt;TRTCCloudDef.TRTCQuality&amp;gt; | 下行网络质量。 |

>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aba07d4191391dadef900422521f34e5b)


## 屏幕分享事件回调

### onScreenCaptureStarted

开始屏幕分享回调。

```java
 void onScreenCaptureStarted();
```

### onScreenCaptureStopped

停止屏幕分享回调。

```java
void onScreenCaptureStopped(int reason);
```

参数如下表所示：

| 参数| 类型 | 含义|
| ------ | ---- | ------------------------------------------------------ |
| reason | int  | 停止原因，0：用户主动停止；1：被其他应用抢占导致停止。 |
