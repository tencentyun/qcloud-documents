TRTCMeeting 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建会议房间，参会人员输入房间号后进入会议。
- 参会人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TRTCMeeting 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人视频会议（Android）](https://cloud.tencent.com/document/product/647/45667)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时直播组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 AVChatroom 实现直播聊天室的功能，同时，通过 IM 消息串联主播间的连麦流程。


<h2 id="TRTCMeeting">TRTCMeeting API 概览</h2>

### SDK 基础函数

| API | 描述 |
|-----|-----|
| [sharedInstance](#sharedinstance) | 获取单例对象。 |
| [destroySharedInstance](#destroysharedinstance) | 销毁单例对象。 |
| [setDelegate](#setdelegate) | 设置事件回调。|
| [setDelegateHandler](#setdelegatehandler) | 设置事件回调所在的线程。 |
| [login](#login) | 登录。|
| [logout](#logout) | 登出。|
| [setSelfProfile](#setselfprofile) | 修改个人信息。|

### 会议房间相关接口函数

| API | 描述 |
|-----|-----|
| [createMeeting](#createmeeting) | 创建会议房间（主持人调用）。|
| [destroyMeeting](#destroymeeting) | 销毁会议房间（主持人调用）。|
| [enterMeeting](#entermeeting) | 进入会议房间（参会成员调用）。|
| [leaveMeeting](#leavemeeting) | 离开会议房间（参会成员调用）。|

### 远端用户相关接口
| API | 描述 |
|-----|-----|
| [getUserInfoList](#getuserinfolist) | 获取房间内所有的人员列表，enterMeeting() 成功后调用才有效。|
| [getUserInfo](#getuserinfo) | 获取房间内指定人员的详细信息，enterMeeting() 成功后调用才有效。|
| [startRemoteView](#startremoteview) | 播放指定成员的远端视频画面。|
| [stopRemoteView](#stopremoteview) | 停止播放远端视频画面。 |
| [setRemoteViewFillMode](#setremoteviewfillmode) | 根据用户 ID 和设置远端图像的渲染模式， |
| [setRemoteViewRotation](#setremoteviewrotation) | 设置远端图像的顺时针旋转角度。 |
| [muteRemoteAudio](#muteremoteaudio) | 屏蔽指定成员的声音。 |
| [muteRemoteVideoStream](#muteremotevideostream) | 屏蔽指定成员的视频流。 |

### 本地视频操作接口

| API | 描述 |
|-----|-----|
| [startCameraPreview](#startcamerapreview) | 开启本地视频的预览画面。|
| [stopCameraPreview](#stopcamerapreview) | 停止本地视频采集及预览。|
| [switchCamera](#switchcamera) | 切换前后摄像头。|
| [setVideoResolution](#setvideoresolution) | 设置分辨率。 |
| [setVideoFps](#setvideofps) | 设置帧率。|
| [setVideoBitrate](#setvideobitrate) | 设置码率。|
| [setLocalViewMirror](#setlocalviewmirror) | 设置本地画面镜像预览模式。|

### 本地音频操作接口

| API | 描述 |
|-----|-----|
| [startMicrophone](#startmicrophone) | 开启麦克风采集。|
| [stopMicrophone](#stopmicrophone) | 停止麦克风采集。|
| [setAudioQuality](#setaudioquality) | 设置音质。|
| [muteLocalAudio](#mutelocalaudio) | 开启本地静音。|
| [setSpeaker](#setspeaker) | 设置开启扬声器。|
| [setAudioCaptureVolume](#setaudiocapturevolume) | 设置麦克风采集音量。|
| [setAudioPlayoutVolume](#setaudioplayoutvolume) | 设置播放音量。|
| [startFileDumping](#startfiledumping) | 开始录音。|
| [stopFileDumping](#stopfiledumping) | 停止录音。|
| [enableAudioEvaluation](#enableaudioevaluation) | 启用音量大小提示。|

### 录屏接口

| API | 描述 |
|-----|-----|
| [startScreenCapture](#startscreencapture) | 启动屏幕分享。 |
| [stopScreenCapture](#stopscreencapture) | 停止屏幕采集。|
| [pauseScreenCapture](#pausescreencapture) | 暂停屏幕分享。|
| [resumeScreenCapture](#resumescreencapture) | 恢复屏幕分享。|

### 美颜滤镜相关接口函数

| API | 描述 |
|-----|-----|
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](http://doc.qcloudtrtc.com/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。|

### 调试相关接口函数

| API | 描述 |
|-----|-----|
| [getLiveBroadcastingURL](#getlivebroadcastingurl) | 获取 CDN 分享链接。|

### 消息发送相关接口函数

| API | 描述 |
|-----|-----|
| [sendRoomTextMsg](#sendroomtextmsg) | 在房间中广播文本消息，一般用于聊天。|
| [sendRoomCustomMsg](#sendroomcustommsg) | 发送自定义文本消息。|


<h2 id="TRTCMeetingDelegate">TRTCMeetingDelegate API 概览</h2>

### 通用事件回调

| API | 描述 |
|-----|-----|
| [onError](#onerror) | 错误回调。|
| [onNetworkQuality](#onnetworkquality) | 网络状态回调。|

### 会议房间事件回调

| API | 描述 |
|-----|-----|
| [onRoomDestroy](#onroomdestroy) | 会议房间被销毁的回调。|

### 会议房间事件回调

| API | 描述 |
|-----|-----|
| [onUserVolumeUpdate](#onuservolumeupdate) | 用户通话音量回调。|

### 成员进出事件回调

| API | 描述 |
|-----|-----|
| [onUserEnterRoom](#onuserenterroom) | 收到新成员进房通知。|
| [onUserLeaveRoom](#onuserleaveroom) | 收到成员退房通知。|

### 成员音视频事件回调

| API | 描述 |
|-----|-----|
| [onUserVideoAvailable](#onuservideoavailable) | 成员开启/关闭摄像头的通知。|
| [onUserAudioAvailable](#onuseraudioavailable) | 成员开启/关闭麦克风的通知。|


### 消息事件回调

| API | 描述 |
|-----|-----|
| [onRecvRoomTextMsg](#onrecvroomtextmsg) | 收到文本消息。|
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | 收到自定义消息。|

## SDK 基础函数

<span id="sharedInstance"></span>
### sharedInstance

获取 [TRTCMeeting](https://cloud.tencent.com/document/product/647/45667) 单例对象。
```java
 public static synchronized TRTCMeeting sharedInstance(Context context);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| context | Context | Android 上下文，内部会转为 ApplicationContext 用于系统 API 调用 |

   

### destroySharedInstance

销毁 [TRTCMeeting](https://cloud.tencent.com/document/product/647/45667) 单例对象。
>?销毁实例后，外部缓存的 TRTCMeeting 实例无法再使用，需要重新调用 [sharedInstance](#sharedInstance) 获取新实例。

```java
public static void destroySharedInstance();
```   

### setDelegate

[TRTCMeeting](https://cloud.tencent.com/document/product/647/45667) 事件回调，您可以通过 TRTCMeetingDelegate 获得 [TRTCMeeting](https://cloud.tencent.com/document/product/647/45667) 的各种状态通知。
```java
public abstract void setDelegate(TRTCMeetingDelegate delegate);
```

>?setDelegate 是 TRTCMeeting 的代理回调。   

### setDelegateHandler

设置事件回调所在的线程。
```java
public abstract void setDelegateHandler(Handler handler);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| handler | Handler | TRTCMeeting 中的各种状态通知回调会通过该 handler 通知给您，请勿与 setDelegate 混用。 |

### login

登录。
```java
public abstract void login(int sdkAppId,
 String userId, String userSig,
 TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppId | int |  您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userId | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig | String | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| callback | ActionCallback | 登录回调，成功时 code 为0。 |


### logout

登出。
```java
public abstract void logout(TRTCMeetingCallback.ActionCallback callback);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 登出回调，成功时 code 为0。 |

   

### setSelfProfile

修改个人信息。
```java
public abstract void setSelfProfile(String userName, String avatarURL, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| name | String | 昵称。 |
| avatarURL | String | 头像地址。 |
| callback | ActionCallback | 个人信息设置回调，成功时 code 为0。 |

   


## 会议房间相关接口函数
### createMeeting

创建会议（主持人调用）。
```java
public abstract void createMeeting(int roomId, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 会议房间标识，需要由您分配并进行统一管理。 |
| callback | ActionCallback | 创建房间的结果回调，成功时 code 为0。 |

主持人正常调用流程如下： 
1. 【主持人】调用 `createMeeting()` 创建会议，会议房间创建成功与否会通过 ActionCallback 通知给主播。
2. 【主持人】调用 `startCameraPreview()` 打开摄像头预览，此时可以调整美颜参数。 
3. 【主持人】调用 `startMicrophone()` 打开麦克风采集。

   

### destroyRoom

销毁会议房间（主持人调用）。主持人在创建会议后，可以调用该函数来销毁会议。
```java
public abstract void destroyMeeting(int roomId, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 销毁房间的结果回调，成功时 code 为0。 |
   

### enterMeeting

进入会议（参会成员调用）。
```java
public abstract void enterMeeting(int roomId, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 房间标识。 |
| callback | ActionCallback | 进入房间的结果回调，成功时 code 为0。 |


参会成员进入会议的正常调用流程如下： 
1. 【参会成员】调用`enterMeeting`并传入 roomId 即可进入会议房间。
2. 【参会成员】调用 `startCameraPreview()` 打开摄像头预览，调用 `startMicrophone()` 打开麦克风采集。
3. 【参会成员】收到`onUserVideoAvailable`的事件，调用`startRemoteView(userId)`并传入成员的 userId 开始播放。
   

### leaveMeeting

离开会议（参会成员调用）。
```java
public abstract void leaveMeeting(TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 退出房间的结果回调，成功时 code 为0。 |

   

### getUserInfoList

获取房间内所有的人员列表，enterMeeting() 成功后调用才有效。


```java
public abstract void getUserInfoList(TRTCMeetingCallback.UserListCallback userListCallback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userListCallback | UserListCallback | 用户详细信息回调。 |
   

### getUserInfo

获取房间内指定人员的详细信息，enterMeeting() 成功后调用才有效。
```java
public abstract void getUserInfo(String userId, TRTCMeetingCallback.UserListCallback userListCallback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userListCallback | UserListCallback | 用户详细信息回调。 |


## 推拉流相关接口函数
### startCameraPreview

开启本地视频的预览画面。
```java
public abstract void startCameraPreview(boolean isFront, TXCloudVideoView view);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isFront | boolean | true：前置摄像头；false：后置摄像头。 |
| view | TXCloudVideoView | 承载视频画面的控件。 |

   

### stopCameraPreview

停止本地视频采集及预览。
```java
public abstract void stopCameraPreview();
```

   

### switchCamera

切换前后摄像头
```java
public abstract void switchCamera(boolean isFront);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isFront | boolean | 切换前后摄像头，true：前置摄像头；false：后置摄像头。 |
   

### setVideoResolution

设置分辨率

```java
public abstract void setVideoResolution(int resolution);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| resolution | int | 视频分辨率, 详细请参见 [TRTC SDK](http://doc.qcloudtrtc.com/group__TRTCCloudDef__android.html#aa3b72c532f3ffdf64c6aacab26be5f87) |



   

### setVideoFps

设置帧率
```java
public abstract void setVideoFps(int fps);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| fps | int | 视频采集帧率。 |

>?【推荐取值】 15fps或20fps，5fps以下，卡顿感明显。10fps以下，会有轻微卡顿感。20fps以上，则过于浪费（电影的帧率为24fps）。


### stopPlay

停止渲染远端视频画面。需在 `onAnchorExit()` 回调时，调用该接口。
```java
public abstract void stopPlay(String userId, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户信息。|
| callback | ActionCallback | 操作回调。|
   

## 主播和观众连麦
### requestJoinAnchor

观众请求连麦。
```java
public abstract void requestJoinAnchor(String reason, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | String | 连麦原因。 |
| responseCallback | ActionCallback | 主播响应回调。 |


主播和观众的连麦流程如下：
1. 【观众】调用 `requestJoinAnchor()` 向主播发起连麦请求。
2. 【主播】会收到 `TRTCLiveRoomDelegate` 的 `onRequestJoinAnchor()` 回调通知。
3. 【主播】调用 `responseJoinAnchor()` 决定是否接受来自观众的连麦请求。
4. 【观众】会收到 responseCallback 回调通知，该通知会携带主播的处理结果。
5. 【观众】如果请求被同意，则调用 `startCameraPreview()` 开启本地摄像头。
6. 【观众】然后调用 `startPublish()` 正式进入推流状态。
7. 【主播】一旦观众进入连麦状态，主播会收到 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知。
8. 【主播】主播调用 `startPlay()` 即可看到连麦观众的视频画面。
9. 【观众】如果直播间里已有其他观众正在跟主播连麦，新加入的连麦观众会收到 `onAnchorEnter()` 通知，调用 `startPlay()` 播放其他连麦者的视频画面。

   

### responseJoinAnchor

主播处理连麦请求。主播在收到 `TRTCLiveRoomDelegate` 的 `onRequestJoinAnchor()` 回调后需要调用此接口来处理观众的连麦请求。
```java
public abstract void responseJoinAnchor(String userId, boolean agree, String reason);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 观众 ID。 |
| agree | boolean | true：同意；false：拒绝。 |
| reason | String | 同意/拒绝连麦的原因描述。 |
   

### kickoutJoinAnchor

主播踢除连麦观众。主播调用此接口踢除连麦观众后，被踢连麦观众会收到 `TRTCLiveRoomDelegate` 的 `onKickoutJoinAnchor()` 回调通知。

```java
public abstract void kickoutJoinAnchor(String userId, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 连麦观众 ID。 |
| callback | ActionCallback | 操作回调。|
  


## 主播跨房间 PK
### requestRoomPK

主播请求跨房 PK。
```java
public abstract void requestRoomPK(int roomId, String userId, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 被邀约房间 ID。 |
| userId | String | 被邀约主播 ID。 |
| responseCallback | ActionCallback | 请求跨房 PK 的结果回调。 |

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B 之间的跨房 PK 流程如下：
1. 【主播 A】调用 `requestRoomPK()` 向主播 B 发起连麦请求。
2. 【主播 B】会收到 `TRTCLiveRoomDelegate` 的 `onRequestRoomPK()` 回调通知。
3. 【主播 B】调用 `responseRoomPK()` 决定是否接受主播 A 的 PK 请求。
4. 【主播 B】如果接受主播 A 的要求，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来显示主播 A 的视频画面。
5. 【主播 A】会收到 `responseCallback` 回调通知，该通知会携带来自主播 B 的处理结果。
6. 【主播 A】如果请求被同意，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 显示主播 B 的视频画面。

   

### responseRoomPK

主播响应跨房 PK 请求。主播响应后，对方主播会收到 `requestRoomPK` 传入的 `responseCallback` 回调。
```java
public abstract void responseRoomPK(String userId, boolean agree, String reason);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 发起 PK 请求的主播 ID。 |
| agree | boolean | true：同意；false：拒绝。 |
| reason | String | 同意/拒绝 PK 的原因描述。 |
   

### quitRoomPK

退出跨房 PK。PK 中的任何一个主播退出跨房 PK 状态后，另一个主播会收到 `TRTCLiveRoomDelegate` 的 `onQuitRoomPk()` 回调通知。
```java
public abstract void quitRoomPK(TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 操作回调。|
   

## 音视频控制相关接口函数
### switchCamera

切换前后摄像头。
```java
public abstract void switchCamera();
```

   

### setMirror

设置是否镜像展示。
```java
public abstract void setMirror(boolean isMirror);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isMirror | boolean | 开启/关闭镜像。 |

   

### muteLocalAudio

静音本地音频。
```java
public abstract void muteLocalAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：开启静音；false：关闭静音。|

   

### muteRemoteAudio

静音远端音频。
```java
public abstract void muteRemoteAudio(String userId, boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 远端的用户 ID。 |
| mute | boolean | true：开启静音；false：关闭静音。|

   

### muteAllRemoteAudio

静音所有远端音频。
```java
public abstract void muteAllRemoteAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：开启静音；false：关闭静音。|

   

## 背景音乐音效相关接口函数
### getAudioEffectManager

获取背景音乐音效管理对象 [TXAudioEffectManager](http://doc.qcloudtrtc.com/group__TRTCCloud__android.html#a3646dad993287c3a1a38a5bc0e6e33aa)。
```java
public abstract TXAudioEffectManager getAudioEffectManager();
```
   

## 美颜滤镜相关接口函数
### getBeautyManager

获取美颜管理对象 [TXBeautyManager](http://doc.qcloudtrtc.com/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。
```java
public abstract TXBeautyManager getBeautyManager();
```

通过美颜管理，您可以使用以下功能：
- 设置“美颜风格”、“美白”、“红润”、“大眼”、“瘦脸”、“V 脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。


## 消息发送相关接口函数
### sendRoomTextMsg

在房间中广播文本消息，一般用于弹幕聊天。
```java
public abstract void sendRoomTextMsg(String message, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。 |
| callback | ActionCallback | 发送结果回调。|

   

### sendRoomCustomMsg

发送自定义文本消息。
```java
public abstract void sendRoomCustomMsg(String cmd, String message, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmd | String | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message | String | 文本消息。 |
| callback | ActionCallback | 发送结果回调。|

   

## 调试相关接口函数
### showVideoDebugLog

是否在界面中展示debug信息。
```java
public abstract void showVideoDebugLog(boolean isShow);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isShow | boolean | 开启/关闭 Debug 信息显示。 |

   

## TRTCLiveRoomDelegate事件回调

## 通用事件回调
### onError

错误回调。
>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```java
void onError(int code, String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | String | 错误信息。 |
   

### onWarning

警告回调。
```java
void onWarning(int code, String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | String | 警告信息。 |

   

### onDebugLog

Log 回调。
```java
void onDebugLog(String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 日志信息。 |

   


## 房间事件回调
### onRoomDestroy

房间被销毁的回调。主播退房时，房间内的所有用户都会收到此通知。
```java
void onRoomDestroy(String roomId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | String | 房间 ID。 |

### onRoomInfoChange

直播房间信息变更回调。多用于直播连麦、PK下房间状态变化通知场景。
```java
void onRoomInfoChange(TRTCLiveRoomDef.TRTCLiveRoomInfo roomInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomInfo | TRTCLiveRoomInfo | 房间信息。 |

## 主播和观众进出事件回调
### onAnchorEnter

收到新主播进房通知。连麦观众和跨房 PK 主播进房后观众会收到新主播的进房事件，您可以调用 `TRTCLiveRoom` 的 `startPlay()` 显示该主播的视频画面。
```java
void onAnchorEnter(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 新进房主播 ID。 |
   

### onAnchorExit

收到主播退房通知。房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 `TRTCLiveRoom` 的 `stopPlay()` 关闭该主播的视频画面。
```java
void onAnchorExit(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 退房用户 ID。 |
   

### onAudienceEnter

收到观众进房通知。
```java
void onAudienceEnter(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 进房观众信息。 |

   

### onAudienceExit

收到观众退房通知。
```java
void onAudienceExit(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 退房观众信息。 |

   


## 主播和观众连麦事件回调
### onRequestJoinAnchor

主播收到观众连麦请求时的回调。
```java
void onRequestJoinAnchor(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, String reason, int timeOut);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 请求连麦观众信息。|
| reason | String | 连麦原因描述。|
| timeout | int | 处理请求的超时时间，如果上层超过该时间没有处理，则会自动将该次请求废弃。 |

   

### onKickoutJoinAnchor

连麦观众收到被踢出连麦的通知。连麦观众收到被主播踢除连麦的消息，您需要调用 `TRTCLiveRoom` 的 `stopPublish()` 退出连麦。
```java
void onKickoutJoinAnchor();
```
  


## 主播 PK 事件回调
### onRequestRoomPK

收到请求跨房 PK 通知。主播收到其他房间主播的 PK 请求，如果同意 PK ，您需要等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来播放邀约主播的流。
```java
void onRequestRoomPK(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, int timeout);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 发起跨房连麦的主播信息。|
| timeout | int | 处理请求的超时时间。 |
   

### onQuitRoomPK

收到断开跨房 PK 通知。
```java
void onQuitRoomPK();
```

## 消息事件回调
### onRecvRoomTextMsg

收到文本消息。
```java
void onRecvRoomTextMsg(String message, TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。|
| user | TRTCLiveUserInfo | 发送者用户信息。|

   

### onRecvRoomCustomMsg

收到自定义消息。
```java
void onRecvRoomCustomMsg(String cmd, String message, TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| command | String | 命令字，由开发者自定义，主要用于区分不同消息类型。|
| message | String | 文本消息。|
| user | TRTCLiveUserInfo | 发送者用户信息。 |