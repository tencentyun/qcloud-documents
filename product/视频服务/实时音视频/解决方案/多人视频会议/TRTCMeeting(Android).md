TRTCMeeting 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建会议房间，参会人员输入房间号后进入会议。
- 参会人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TRTCMeeting 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人视频会议(Android)](https://cloud.tencent.com/document/product/647/45667)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时视频会议组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 MeetingRoom 实现会议中聊天室的功能。


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
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。|

### 分享相关接口

| API | 描述 |
|-----|-----|
| [getLiveBroadcastingURL](#getlivebroadcastingurl) | 获取 CDN 分享链接。|

### 消息发送相关接口函数

| API | 描述 |
|-----|-----|
| [sendRoomTextMsg](#sendroomtextmsg) | 在房间中广播文本消息，一般用于聊天。|
| [sendRoomCustomMsg](#sendroomcustommsg) | 发送自定义（信令）消息。|


<h2 id="TRTCMeetingDelegate">TRTCMeetingDelegate API 概览</h2>

### 通用事件回调

| API | 描述 |
|-----|-----|
| [onError](#onerror) | 错误回调。|

### 会议房间事件回调

| API | 描述 |
|-----|-----|
| [onRoomDestroy](#onroomdestroy) | 会议房间被销毁的回调。|
| [onNetworkQuality](#onnetworkquality)     | 网络状态回调。   |
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

### 录屏事件回调

| API                                                 | 描述           |
| --------------------------------------------------- | -------------- |
| [onScreenCaptureStarted](#onscreencapturestarted) | 录屏开始通知。 |
| [onScreenCapturePaused](#onscreencapturepaused)   | 录屏暂停回调。 |
| [onScreenCaptureResumed](#onscreencaptureresumed) | 录屏恢复回调。 |
| [onScreenCaptureStoped](#onscreencapturestoped)   | 录屏停止回调。 |

## SDK 基础函数

[](id:sharedInstance)
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
| userName | String | 昵称。 |
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
1. 【主持人】调用 `createMeeting()` 创建会议，会议房间创建成功与否会通过 ActionCallback 通知给主持人。
2. 【主持人】调用 `startCameraPreview()` 打开摄像头预览，此时可以调整美颜参数。 
3. 【主持人】调用 `startMicrophone()` 打开麦克风采集。

   

### destroyMeeting

销毁会议房间（主持人调用）。主持人在创建会议后，可以调用该函数来销毁会议。
```java
public abstract void destroyMeeting(int roomId, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 会议房间标识，需要由您分配并进行统一管理。 |
| callback | ActionCallback | 销毁房间的结果回调，成功时 code 为0。 |


### enterMeeting

进入会议（参会成员调用）。
```java
public abstract void enterMeeting(int roomId, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 会议房间标识。 |
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


## 远端用户相关接口

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
| userId | String | 用户 ID。|
| userListCallback | UserListCallback | 用户详细信息回调。 |


### startRemoteView

播放指定成员的远端视频画面。在 `onUserVideoAvailable()` 为true回调时，调用该接口。
```java
public abstract void startRemoteView(String userId, TXCloudVideoView view, final TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 需要播放的用户 ID。|
| view | TXCloudVideoView | 承载视频画面的 view 控件。|
| callback | ActionCallback | 操作回调。|

### stopRemoteView

停止播放远端视频画面。在 `onUserVideoAvailable()` 为false回调时，调用该接口。
```java
public abstract void stopRemoteView(String userId, final TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 需要停止播放的用户 ID。|
| callback | ActionCallback | 操作回调。|

### setRemoteViewFillMode

根据用户id和设置远端图像的渲染模式。
```java
public abstract void setRemoteViewFillMode(String userId, int fillMode);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。|
| fillMode | int  | 填充或适应模式，默认值：填充（FILL） 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ab4197bc2efb62b471b49f926bab9352f) |



### setRemoteViewRotation

设置远端图像的顺时针旋转角度。
```java
public abstract void setRemoteViewRotation(String userId, int rotation);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| rotation | int  | 顺时针旋转角度, 详情请参见[TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a87fd1307871debc7c051de4878eb6d69) |



### muteRemoteAudio

静音远端音频。
```java
public abstract void muteRemoteAudio(String userId, boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| mute | boolean | true：开启静音；false：关闭静音。|

   

### muteRemoteVideoStream

屏蔽指定成员的视频流。
```java
public abstract void muteRemoteVideoStream(String userId, boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| mute | boolean | true：屏蔽；false：解除屏蔽。|


​      

## 本地视频操作接口
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
| resolution | int | 视频分辨率, 详细请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#aa3b72c532f3ffdf64c6aacab26be5f87) |



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


### setVideoBitrate

设置码率
```java
public abstract void setVideoBitrate(int bitrate);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bitrate | int | 码率，SDK 会按照目标码率进行编码，只有在网络不佳的情况下才会主动降低视频码率。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html) |

>? 【推荐取值】请参考本 TRTCVideoResolution 在各档位注释的最佳码率，也可以在此基础上适当调高。 例如 TRTC_VIDEO_RESOLUTION_1280_720 对应1200kbps的目标码率，您也可以设置为1500kbps以便获得更好的清晰度观感。



### setLocalViewMirror

设置本地画面镜像预览模式
```java
public abstract void setLocalViewMirror(int type);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | int | 镜像模式。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa353b5cf5662c43252eb8e5132f041c1) |

## 本地音频操作接口

### startMicrophone

开启麦克风采集
```java
public abstract void startMicrophone();
```

### stopMicrophone

停止麦克风采集
```java
public abstract void stopMicrophone();
```

### setAudioQuality

设置音质
```java
public abstract void setAudioQuality(int quality);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | int | 音频质量。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a955cccaddccb0c993351c656067bee55) |


### muteLocalAudio

静音/取消静音本地的音频
```java
public abstract void muteLocalAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | 静音/取消静音。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a37f52481d24fa0f50842d3d8cc380d86) |



### setSpeaker

设置开启扬声器
```java
public abstract void setSpeaker(boolean useSpeaker);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| useSpeaker | boolean | true:扬声器 false:听筒 |



### setAudioCaptureVolume

设置麦克风采集音量
```java
public abstract void setAudioCaptureVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 采集音量，0-100， 默认100。 |


### setAudioPlayoutVolume

设置播放音量
```java
public abstract void setAudioPlayoutVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 播放音量，0-100， 默认100。 |


### startFileDumping

开始录音
```java
public abstract void startFileDumping(TRTCCloudDef.TRTCAudioRecordingParams trtcAudioRecordingParams);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| trtcAudioRecordingParams | TRTCCloudDef.TRTCAudioRecordingParams | 录音参数。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCAudioRecordingParams) |

>? 该方法调用后， SDK 会将通话过程中的所有音频（包括本地音频，远端音频，BGM 等）录制到一个文件里。无论是否进房，调用该接口都生效。如果调用 exitMeeting 时还在录音，录音会自动停止。

### stopFileDumping

停止录音
```java
public abstract void stopFileDumping();
```

### enableAudioEvaluation

启用音量大小提示
```java
public abstract void enableAudioEvaluation(boolean enable);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean |  true 打开 false 关闭。 |

>? 开启后会在 onUserVolumeUpdate 中获取到 SDK 对音量大小值的评估。

## 录屏接口
### startScreenCapture

启动屏幕分享。
```java
public abstract void startScreenCapture(TRTCCloudDef.TRTCVideoEncParam encParams, TRTCCloudDef.TRTCScreenShareParams screenShareParams);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| encParams | TRTCCloudDef.TRTCVideoEncParam | 设置屏幕分享时的编码参数，推荐采用上述推荐配置，如果您指定 encParams 为 null，则使用您调用 startScreenCapture 之前的编码参数设置。 |
| screenShareParams | TRTCCloudDef.TRTCScreenShareParams | 设置屏幕分享的特殊配置，其中推荐设置 floatingView，一方面可以避免 App 被系统强杀；另一方面也能助于保护用户隐私。 |

>? 详情请参见[TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58)

### stopScreenCapture

停止屏幕采集。
```java
public abstract void stopScreenCapture();
```

### pauseScreenCapture

暂停屏幕分享。
```java
public abstract void pauseScreenCapture();
```

### resumeScreenCapture

恢复屏幕分享。
```java
public abstract void resumeScreenCapture();
```

## 分享接口
### getLiveBroadcastingURL

获取 CDN 分享链接。
```java
public abstract String getLiveBroadcastingURL();
```

返回值如下表所示：

| 返回值 | 类型 | 含义 |
|-----|-----|-----|
| url  | String  | CDN 分享链接。 |

## 美颜滤镜相关接口函数
### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。
```java
public abstract TXBeautyManager getBeautyManager();
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
```java
public abstract void sendRoomTextMsg(String message, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。 |
| callback | ActionCallback | 发送结果回调。|

   

### sendRoomCustomMsg

发送自定义文本消息。
```java
public abstract void sendRoomCustomMsg(String cmd, String message, TRTCMeetingCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmd | String | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message | String | 文本消息。 |
| callback | ActionCallback | 发送结果回调。|

   

## TRTCMeetingDelegate 事件回调

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



## 房间事件回调
### onRoomDestroy

房间被销毁的回调。主持人退房时，房间内的所有用户都会收到此通知。
```java
void onRoomDestroy(String roomId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | String | 房间 ID。 |

### onNetworkQuality

网络状态回调。
```java
 void onNetworkQuality(TRTCCloudDef.TRTCQuality localQuality, List<TRTCCloudDef.TRTCQuality> remoteQuality);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| localQuality | TRTCCloudDef.TRTCQuality | 上行网络质量。 |
| remoteQuality | List&lt;TRTCCloudDef.TRTCQuality&gt; | 下行网络质量。 |

>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aba07d4191391dadef900422521f34e5b)


### onUserVolumeUpdate

启用音量大小提示，会通知每个成员的音量大小
```java
void onUserVolumeUpdate(String userId, int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| volume | int | 音量大小，取值0-100。 |



## 成员进出事件回调
### onUserEnterRoom

新成员进房通知。
```java
void onUserEnterRoom(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 新进房成员的用户 ID。 |


### onUserLeaveRoom

成员退房通知。
```java
void onUserLeaveRoom(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 退房成员的用户 ID。 |


## 成员音视频事件回调
### onUserVideoAvailable

成员开启/关闭摄像头的通知。
```java
void onUserVideoAvailable(String userId, boolean available);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| available | boolean | true：用户打开摄像头；false：用户关闭摄像头。 |

   

### onUserAudioAvailable

成员开启/关闭麦克风的通知。
```java
void onUserAudioAvailable(String userId, boolean available);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| available | boolean | true：用户打开麦克风；false：用户关闭麦克风。 |

   

## 消息事件回调
### onRecvRoomTextMsg

收到文本消息。
```java
void onRecvRoomTextMsg(String message, TRTCMeetingDef.UserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。|
| userInfo | TRTCMeetingDef.UserInfo | 发送者用户信息。|

   

### onRecvRoomCustomMsg

收到自定义消息。
```java
void onRecvRoomCustomMsg(String cmd, String message, TRTCMeetingDef.UserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmd | String | 命令字，由开发者自定义，主要用于区分不同消息类型。|
| message | String | 文本消息。|
| userInfo | TRTCMeetingDef.UserInfo | 发送者用户信息。 |


## 录屏事件回调

### onScreenCaptureStarted

录屏开始通知。

```java
void onScreenCaptureStarted();
```

### onScreenCapturePaused

录屏暂停通知。

```java
void onScreenCapturePaused();
```

### onScreenCaptureResumed

录屏恢复通知。

```java
void onScreenCaptureResumed();
```

### onScreenCaptureStoped

录屏停止通知。

```java
void onScreenCaptureStopped(int reason);
```

参数如下表所示：

| 参数   | 类型 | 含义                                               |
| ------ | ---- | -------------------------------------------------- |
| reason | int  | 停止原因，0：用户主动停止；1：被其他应用抢占导致停止 |





