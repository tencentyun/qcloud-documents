TRTCMeeting 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主持人创建会议房间，参会人员输入房间号后进入会议。
- 参会人员之间进行屏幕分享。
- 支持发送各种文本消息和自定义消息。

TRTCMeeting 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [多人视频会议（Flutter）](https://cloud.tencent.com/document/product/647/58405)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时视频会议组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 MeetingRoom 实现会议中聊天室的功能。

[](id:TRTCMeeting)

## TRTCMeeting API 概览
### SDK 基础接口

| API | 描述 |
|-----|-----|
| [sharedInstance](#sharedinstance) | 获取单例对象。|
| [destroySharedInstance](#destroysharedinstance) | 销毁单例对象。|
| [registerListener](#registerlistener) | 设置事件监听。|
| [unRegisterListener](#unregisterlistener) | 销毁事件监听。|
| [login](#login) | 登录。|
| [logout](#logout) | 登出。|
| [setSelfProfile](#setselfprofile) | 修改个人信息。|

### 会议房间相关接口

| API | 描述 |
|-----|-----|
| [createMeeting](#createmeeting) | 创建会议房间（主持人调用）。|
| [destroyMeeting](#destroymeeting) | 销毁会议房间（主持人调用）。|
| [enterMeeting](#entermeeting) | 进入会议房间（参会成员调用）。|
| [leaveMeeting](#leavemeeting) | 离开会议房间（参会成员调用）。|
| [getUserInfoList](#getuserinfolist) | 获取房间内所有的人员列表，enterMeeting()成功后调用才有效。|
| [getUserInfo](#getuserinfo) | 获取房间内指定人员的详细信息，enterMeeting()成功后调用才有效。|

### 远端用户相关接口

| API | 描述 |
|-----|-----|
| [startRemoteView](#startremoteview) | 播放指定成员的远端视频画面。|
| [stopRemoteView](#stopremoteview) | 停止播放指定成员的远端视频画面。|
| [setRemoteViewParam](#setremoteviewparam) | 设置指定成员的远端图像渲染参数。|
| [muteRemoteAudio](#muteremoteaudio) | 静音/取消静音指定成员的远端音频。|
| [muteAllRemoteAudio](#muteallremoteaudio) | 静音/取消静音所有成员的远端音频。|
| [muteRemoteVideoStream](#muteremotevideostream) | 暂停/恢复指定成员的远端视频。|
| [muteAllRemoteVideoStream](#muteallremotevideostream) | 暂停/恢复所有成员的远端视频流。|

### 本地视频操作接口

| API | 描述 |
|-----|-----|
| [startCameraPreview](#startcamerapreview) | 开启本地视频的预览画面。|
| [stopCameraPreview](#stopcamerapreview) | 停止本地视频采集及预览。|
| [switchCamera](#switchcamera) | 切换前后摄像头。|
| [setVideoEncoderParam](#setvideoencoderparam) | 设置视频编码器相关参数。|
| [setLocalViewMirror](#setlocalviewmirror) | 设置本地画面镜像预览模式。|

### 本地音频操作接口

| API | 描述 |
|-----|-----|
| [startMicrophone](#startmicrophone) | 开启麦克风采集。|
| [stopMicrophone](#stopmicrophone) | 停止麦克风采集。|
| [muteLocalAudio](#mutelocalaudio) | 开启/关闭本地静音。|
| [setSpeaker](#setspeaker) | 设置开启扬声器或听筒。|
| [setAudioCaptureVolume](#setaudiocapturevolume) | 设置麦克风采集音量。|
| [setAudioPlayoutVolume](#setaudioplayoutvolume) | 设置播放音量。|
| [startAudioRecording](#startaudiorecording) | 开始录音。|
| [stopAudioRecording](#stopaudiorecording) | 停止录音。|
| [enableAudioVolumeEvaluation](#enableaudiovolumeevaluation) | 启用音量大小提示。|

### 录屏接口

| API | 描述 |
|-----|-----|
| [startScreenCapture](#startscreencapture) | 启动屏幕分享。|
| [stopScreenCapture](#stopscreencapture) | 停止屏幕采集。|
| [pauseScreenCapture](#pausescreencapture) | 暂停屏幕采集。|
| [resumeScreenCapture](#resumescreencapture) | 恢复屏幕采集。|

### 获取相关管理对象接口

| API | 描述 |
|-----|-----|
| [getDeviceManager](#getdevicemanager) | 获取设备管理对象 [TXDeviceManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_device_manager/TXDeviceManager-class.html)。|
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_beauty_manager/TXBeautyManager-class.html)。|

### 消息发送相关接口

| API | 描述 |
|-----|-----|
| [sendRoomTextMsg](#sendroomtextmsg) | 在会议中广播文本消息，一般用于聊天。|
| [sendRoomCustomMsg](#sendroomcustommsg) | 发送自定义文本消息。|

[](id:TRTCLiveRoomDelegate)
## TRTCLiveRoomDelegate API 概览
### 通用事件回调

| API | 描述 |
|-----|-----|
| [onError](#onerror) | 错误回调。|
| [onWarning](#onwarning) | 警告回调。|
| [onKickedOffline](#onkickedoffline) | 其他用户登录了同一账号，被踢下线。|

### 会议房间事件回调

| API | 描述 |
|-----|-----|
| [onRoomDestroy](#onroomdestroy) | 会议房间被销毁的回调。|
| [onNetworkQuality](#onnetworkquality) | 网络状态回调。|
| [onUserVolumeUpdate](#onuservolumeupdate) | 用户通话音量回调。|

### 成员进出事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](#onenterroom) | 本地进会回调。|
| [onLeaveRoom](#onleaveroom) | 本地退会回调。|
| [onUserEnterRoom](#onuserenterroom) | 新成员进会回调。|
| [onUserLeaveRoom](#onuserleaveroom) | 成员退会回调。|

### 成员音视频事件回调

| API | 描述 |
|-----|-----|
| [onUserAudioAvailable](#onuseraudioavailable) | 成员开启/关闭麦克风的回调。|
| [onUserVideoAvailable](#onuservideoavailable) | 成员开启/关闭摄像头的回调。|
| [onUserSubStreamAvailable](#onusersubstreamavailable) | 成员开启/关闭辅路画面的回调。|

### 消息事件回调

| API | 描述 |
|-----|-----|
| [onRecvRoomTextMsg](#onrecvroomtextmsg) | 收到文本消息的回调。|
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | 收到自定义消息的回调。|

### 录屏事件回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureStarted](#onscreencapturestarted) | 录屏开始回调。|
| [onScreenCapturePaused](#onscreencapturepaused) | 录屏暂停回调。|
| [onScreenCaptureResumed](#onscreencaptureresumed) | 录屏恢复回调。|
| [onScreenCaptureStoped](#onscreencapturestoped) | 录屏停止回调。|

## SDK 基础接口
### sharedInstance

获取 [TRTCMeeting](https://cloud.tencent.com/document/product/647/58405) 单例对象。
```dart
static Future<TRTCMeeting> sharedInstance();
```

### destroySharedInstance

销毁 [TRTCMeeting](https://cloud.tencent.com/document/product/647/58405) 单例对象。
```dart
static void destroySharedInstance();
```
>? 销毁实例后，外部缓存的 TRTCMeeting 实例无法再使用，需要重新调用 [sharedInstance](#sharedinstance) 获取新实例。

### registerListener

设置事件监听，您可以通过 TRTCMeetingDelegate 获得 [TRTCMeeting](https://cloud.tencent.com/document/product/647/58405) 的各种状态通知。
```dart
void registerListener(MeetingListenerFunc func);
```
>? func 是 TRTCMeeting 的代理回调。

### unRegisterListener

销毁事件监听。
```dart
void unRegisterListener(MeetingListenerFunc func);
```

### login

登录。
```dart
Future<ActionCallback> login(int sdkAppId, String userId, String userSig);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppId | int | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。|
| userId | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。|
| userSig | String | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。|

### logout

登出。
```dart
Future<ActionCallback> logout();
```

### setSelfProfile

修改个人信息。
```dart
Future<ActionCallback> setSelfProfile(String userName, String avatarURL);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userName | String | 用户昵称。|
| avatarURL | String | 用户头像地址。|

## 会议房间相关接口
### createMeeting

创建会议（主持人调用）。
```dart
Future<ActionCallback> createMeeting(int roomId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 会议房间标识，需要由您分配并进行统一管理。|

主持人正常调用流程如下： 
1. 【主持人】调用 `createMeeting()` 并传入 `roomId` 创建会议，会议房间创建成功与否会通过 `ActionCallback` 通知给主持人。 
2. 【主持人】调用 `startCameraPreview()` 打开摄像头预览，此时可以调整美颜参数。
3. 【主持人】调用 `startMicrophone()` 打开麦克风采集。

### destroyMeeting

销毁会议房间（主持人调用）。主持人在创建会议后，可以调用该函数来销毁会议。
```dart
Future<ActionCallback> destroyMeeting(int roomId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 会议房间标识，需要由您分配并进行统一管理。|

### enterMeeting

进入会议房间（参会成员调用）。
```dart
Future<ActionCallback> enterMeeting(int roomId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 会议房间标识。|

参会成员进入会议的正常调用流程如下： 
1. 【参会成员】调用 `enterMeeting()` 并传入 `roomId` 即可进入会议房间。
2. 【参会成员】调用 `startCameraPreview()` 打开摄像头预览，调用 `startMicrophone()` 打开麦克风采集。
3. 【参会成员】收到 `onUserVideoAvailable` 的事件，调用 `startRemoteView()` 并传入成员的 `userId` 开始播放。

### leaveMeeting

离开会议房间（参会成员调用）。
```dart
Future<ActionCallback> leaveMeeting();
```

### getUserInfoList

获取房间内所有的人员列表，enterMeeting()成功后调用才有效。
```dart
Future<UserListCallback> getUserInfoList(List<String> userIdList);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userIdList | List&lt;String&gt; | 需要获取的 userId 列表。|

### getUserInfo

获取房间内指定人员的详细信息，enterMeeting()成功后调用才有效。
```dart
Future<UserListCallback> getUserInfo(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 指定成员的 ID。|

## 远端用户相关接口
### startRemoteView

播放指定成员的远端视频画面。
```dart
Future<void> startRemoteView(String userId, int streamType, int viewId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 指定成员的 ID。|
| streamType | int | 要观看的视频流类型。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a9a2aaa1d287b6a2169088c5ecbd25f19)。|
| viewId | int | TRTCCloudVideoView 生成的 viewId。|

### stopRemoteView

停止播放指定成员的远端视频画面。
```dart
Future<void> stopRemoteView(String userId, int streamType);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 指定成员的 ID。|
| streamType | int | 要观看的视频流类型。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a9a2aaa1d287b6a2169088c5ecbd25f19)。|

### setRemoteViewParam

设置指定成员的远端图像渲染参数。
```dart
Future<void> setRemoteViewParam(String userId, int streamType,
  {int fillMode, int rotation, int mirrorType});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 指定成员的 ID。|
| streamType | int | 要观看的视频流类型。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a9a2aaa1d287b6a2169088c5ecbd25f19)。|
| fillMode | int | 图像渲染模式，填充（默认值）或适应模式。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#ae697c0f66077568d33d0996064776b50)。|
| rotation | int | 图像顺时针旋转角度。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#ab3d380890a5e0b7b6a29bc5d0e58f8e8)。|
| mirrorType | int | 镜像模式。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#ae5d847e0006bf2cd689b1116721109ca)。|

### muteRemoteAudio

静音/取消静音指定成员的远端音频。
```dart
Future<void> muteRemoteAudio(String userId, bool mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 指定成员的 ID。|
| mute | boolean | true：静音；false：关闭静音。|

### muteAllRemoteAudio

静音/取消静音所有成员的远端音频。
```dart
Future<void> muteAllRemoteAudio(bool mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：静音；false：关闭静音。|

### muteRemoteVideoStream

暂停/恢复指定成员的远端视频。
```dart
Future<void> muteRemoteVideoStream(String userId, bool mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 指定成员的 ID。|
| mute | boolean | true：暂停；false：恢复。|

### muteAllRemoteVideoStream

暂停/恢复所有成员的远端视频流。
```dart
Future<void> muteAllRemoteVideoStream(bool mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：暂停；false：恢复。|

## 本地视频操作接口
### startCameraPreview

开启本地视频的预览画面。
```dart
Future<void> startCameraPreview(bool isFront, int viewId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isFront | boolean | true：前置摄像头；false：后置摄像头。|
| viewId | int | TRTCCloudVideoView 生成的 viewId。|

### stopCameraPreview

停止本地视频采集及预览。
```dart
Future<void> stopCameraPreview();
```

### switchCamera

切换前后摄像头。
```dart
Future<void> switchCamera(bool isFront);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isFront | boolean | true：前置摄像头；false：后置摄像头。|

### setVideoEncoderParam

设置视频编码器相关参数。
```dart
Future<void> setVideoEncoderParam({
  int videoFps,
  int videoBitrate,
  int videoResolution,
  int videoResolutionMode,
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| videoFps | int | 视频采集帧率。|
| videoBitrate | int | 码率，SDK 会按照目标码率进行编码，只有在网络不佳的情况下才会主动降低视频码率。|
| videoResolution | int | 视频分辨率。|
| videoResolutionMode | int | 分辨率模式。|
>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVideoEncParam)。

### setLocalViewMirror

设置本地画面镜像预览模式。
```dart
Future<void> setLocalViewMirror(bool isMirror);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isMirror | boolean | 是否开启镜像预览模式，true：开启；false：不开启。|

## 本地音频操作接口
### startMicrophone

开启麦克风采集。
```dart
Future<void> startMicrophone({int quality});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | int | 音频质量。详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a4451651bf7fc810efc4400964c3c0408)。|

### stopMicrophone

停止麦克风采集。
```dart
Future<void> stopMicrophone();
```

### muteLocalAudio

开启/关闭本地静音。
```dart
Future<void> muteLocalAudio(bool mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：静音；false：取消静音。|

### setSpeaker

设置开启扬声器或听筒。
```dart
Future<void> setSpeaker(bool useSpeaker);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| useSpeaker | boolean | true：扬声器；false：听筒。|

### setAudioCaptureVolume

设置麦克风采集音量。
```dart
Future<void> setAudioCaptureVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 采集音量，取值0 - 100，默认值为100。|

### setAudioPlayoutVolume

设置播放音量。
```dart
Future<void> setAudioPlayoutVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 播放音量，取值0 - 100，默认值100。|

### startAudioRecording

开始录音。
```dart
Future<int?> startAudioRecording(String filePath);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| filePath | String | 录音文件的保存路径，该路径需要用户自行指定，请确保路径存在且可写。该路径需精确到文件名及格式后缀，格式后缀决定录音文件的格式，目前支持的格式有 PCM、WAV 和 AAC。|

### stopAudioRecording

停止录音。
```dart
Future<void> stopAudioRecording();
```

### enableAudioVolumeEvaluation

启用音量大小提示。
```dart
Future<void> enableAudioVolumeEvaluation(int intervalMs);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| intervalMs | int | 决定了 onUserVoiceVolume 回调的触发间隔，单位为ms，最小间隔为100ms，如果小于等于0则会关闭回调，建议设置为300ms。|

## 录屏接口
### startScreenCapture

启动屏幕分享。
```dart
Future<void> startScreenCapture({
  int videoFps,
  int videoBitrate,
  int videoResolution,
  int videoResolutionMode,
  String appGroup,
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| videoFps | int | 视频采集帧率。|
| videoBitrate | int | 码率，SDK 会按照目标码率进行编码，只有在网络不佳的情况下才会主动降低视频码率。|
| videoResolution | int | 视频分辨率。|
| videoResolutionMode | int | 分辨率模式。|
| appGroup | String | 该参数仅仅在iOS端有效，Android端不需要关注这个参数。该参数是主 App 与 Broadcast 共享的 Application Group Identifier。|
>? 详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVideoEncParam)。

### stopScreenCapture

停止屏幕采集。
```dart
Future<void> stopScreenCapture();
```

### pauseScreenCapture

暂停屏幕采集。
```dart
Future<void> pauseScreenCapture();
```

### resumeScreenCapture

恢复屏幕采集。
```dart
Future<void> resumeScreenCapture();
```

## 获取相关管理对象接口
### getDeviceManager

获取设备管理对象 [TXDeviceManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_device_manager/TXDeviceManager-class.html)。
```dart
getDeviceManager();
```

### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_beauty_manager/TXBeautyManager-class.html)。
```dart
getBeautyManager();
```

通过美颜管理，您可以使用以下功能：
- 设置“美颜风格”、“美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。

## 消息发送相关接口
### sendRoomTextMsg

在会议中广播文本消息，一般用于聊天。
```dart
Future<ActionCallback> sendRoomTextMsg(String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。|

### sendRoomCustomMsg

发送自定义文本消息。
```dart
Future<ActionCallback> sendRoomCustomMsg(String cmd, String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmd | String | 命令字，由开发者自定义，主要用于区分不同消息类型。|
| message | String | 文本消息。|

## TRTCMeetingDelegate事件回调
## 通用事件回调
### onError

错误回调。
>? SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 错误码。|
| errMsg | String | 错误信息。|
| extraInfo | String | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。|

### onWarning

警告回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| warningCode | int | 错误码。|
| warningMsg | String | 警告信息。|
| extraInfo | String | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。|

### onKickedOffline

其他用户登录了同一账号，被踢下线。

## 会议房间事件回调
### onRoomDestroy

会议房间被销毁的回调。主持人退房时，房间内的所有用户都会收到此通知。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | String | 会议房间 ID。|

### onNetworkQuality

网络状态回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| localQuality | TRTCCloudDef.TRTCQuality | 上行网络质量。|
| remoteQuality | List&lt;TRTCCloudDef.TRTCQuality&gt; | 下行网络质量。|

### onUserVolumeUpdate

用户通话音量回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userVolumes | List | 所有正在说话的房间成员的音量，取值范围0 - 100。|
| totalVolume | int | 所有远端成员的总音量, 取值范围0 - 100。|

## 成员进出事件回调
### onEnterRoom

本地进会回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| result | int | 大于0时为进会耗时（ms），小于0时为进会错误码。|

### onLeaveRoom

本地退会回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 离开会议原因，0：主动调用 leaveMeeting 退会；1：被服务器踢出当前会议；2：当前会议整个被解散。|

### onUserEnterRoom

新成员进会回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 新进会成员的用户 ID。|

### onUserLeaveRoom

成员退会回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 退会成员的用户 ID。|

## 成员音视频事件回调
### onUserAudioAvailable

成员开启/关闭麦克风的回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。|
| available | boolean | true：用户打开麦克风；false：用户关闭麦克风。|

### onUserVideoAvailable

成员开启/关闭摄像头的回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。|
| available | boolean | true：用户打开摄像头；false：用户关闭摄像头。|

### onUserSubStreamAvailable

成员开启/关闭辅路画面的回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。|
| available | boolean | true：用户打开辅路画面；false：用户关闭辅路画面。|

## 消息事件回调
### onRecvRoomTextMsg

收到文本消息的回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。|
| sendId | String | 发送者用户 ID。|
| userAvatar | String | 发送者用户头像。|
| userName | String | 发送者用户昵称。|

### onRecvRoomCustomMsg

收到自定义消息的回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| command | String | 命令字，由开发者自定义，主要用于区分不同消息类型。|
| message | String | 文本消息。|
| sendId | String | 发送者用户 ID。|
| userAvatar | String | 发送者用户头像。|
| userName | String | 发送者用户昵称。|

## 录屏事件回调
### onScreenCaptureStarted

录屏开始回调。

### onScreenCapturePaused

录屏暂停回调。

### onScreenCaptureResumed

录屏恢复回调。

### onScreenCaptureStoped

录屏停止回调。

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | int | 停止原因，0：用户主动停止；1：屏幕窗口关闭导致停止。|
