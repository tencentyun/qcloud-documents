本文将介绍如何定制 TUICallKit 的用户界面，我们提供了两个方案供您选择：**界面微调方案**和**自实现 UI 方案**。

## 方案一：界面微调方案
通过直接修改我们提供的 UI 源代码，对 TUICallKit 的用户界面进行调整，TUICallKit 的界面源代码位于 [Github](https://github.com/tencentyun/TUICalling) 中的 `Android/tuicallkit` 文件夹下面：

### 替换图标

您可以直接替换 `res\drawable-xxhdpi` 文件夹下的图标，以确保整个 App 中的图标色调风格保持一致，请在替换时保持图标文件的名字不变。
![](https://qcloudimg.tencent-cloud.cn/raw/32a0db447f1ce053d2f85a3845702312.png)

### 替换铃声
您可以替换 `res\raw` 文件夹下的三个音频文件来达到替换铃声的目的：

| 文件名 | 用途 | 
|---------|---------|
| phone_dialing.wav | 发起呼叫时的声音 | 
| phone_hangup.mp3 | 被挂断的声音 | 
| phone_ringing.wav | 接到呼叫时的声音 | 

### 替换文案
您可以通过修改 values-zh 和 values-en 中的 `strings.xml` 文件来修改视频通话界面中的字符串内容。


## 方案二：自实现 UI 方案
TUICallKit 的整个通话功能是基于 TUICallEngine 这个无 UI 组件实现的，您可以删掉 tuicallkit 文件夹，完全基于 TUICallEngine 实现一套自己的 UI 界面。

### TUICallEngine
TUICallEngine 是整个通话组件的底层接口，主要提供了1对1音视频通话和群组内通话的发起、接听、拒绝、结束以及设备操作等关键接口。

| API | 描述 |
|-----|-----|
| [createInstance](#createInstance) | 创建 TUICallEngine 实例（单例模式）|
| [destroyInstance](#destroyInstance) | 销毁 TUICallEngine 实例（单例模式）|
| [init](#init) | 完成音视频通话基础能力的鉴权|
| [addObserver](#addObserver) | 增加事件回调|
| [removeObserver](#removeObserver) | 移除回调接口|
| [call](#call) | 发起 1 对 1 通话|
| [groupCall](#groupCall) | 发起群组内通话|
| [accept](#accept) | 接听通话 |
| [reject](#reject) | 拒绝通话 |
| [hangup](#hangup) | 结束通话|
| [ignore](#ignore) | 忽略通话|
| [inviteUser](#inviteUser) | 邀请其他人加入一个已经发起的群组内通话 |
| [joinInGroupCall](#joinInGroupCall) | 主动加入一个已经发起的群组内通话 |
| [switchCallMediaType](#switchCallMediaType) | 视频通话切换成语音通话，或者反向切换|
| [startRemoteView](#startRemoteView) | 开始渲染远端用户的视频流 |
| [stopRemoteView](#stopRemoteView) | 停止渲染远端用户的视频流 |
| [openCamera](#opencamera) | 开启摄像头|
| [closeCamara](#closecamara) | 关闭摄像头|
| [switchCamera](#switchcamera) | 切换前后摄像头|
| [openMicrophone](#setmicmute) | 打开麦克风|
| [closeMicrophone](#sethandsfree) | 关闭麦克风|
| [selectAudioPlaybackDevice](#setmicmute) | 选择音频播放设备（听筒/扬声器）|
| [setSelfInfo](#setSelfInfo) | 设置用户的昵称和头像|
| [enableMultiDeviceAbility](#enableMultiDeviceAbility) | 开启/关闭 TUICallEngine 的多设备登录模式 （尊享版套餐支持）|

## TUICallObserver 
TUICallObserver 是 TUICallEngine 对应的回调事件类，您可以通过此回调来监听自己感兴趣的回调事件。

| API | 描述 |
|-----|-----|
| [onError](#onError) | 通话过程中错误回调|
| [onCallReceived](#onCallReceived) | 收到新的通话|
| [onCallCancelled](#onCallCancelled) | 通话已经被取消 |
| [onCallBegin](#onCallBegin) | 通话已经开始|
| [onCallEnd](#onCallEnd) | 通话已经结束|
| [onCallMediaTypeChanged](#onCallMediaTypeChanged) | 通话的媒体类型发生改变的回调|
| [onUserReject](#onUserReject) |  通话要求被对方拒绝 |
| [onUserNoResponse](#onUserNoResponse) |  对方长时间没有响应您的通话请求|
| [onUserLineBusy](#onUserLineBusy) | 被呼叫的用户忙线中|
| [onUserJoin](#onUserJoin) | 有用户加入了当前的通话 |
| [onUserLeave](#onUserLeave) | 有用户离开了当前的通话 |
| [onUserVideoAvailable](#onUserVideoAvailable) | 通话中的用户开启/关闭了自己的视频|
| [onUserAudioAvailable](#onUserAudioAvailable) | 通话中的用户开启/关闭了自己的音频|
| [onUserVoiceVolumeChanged](#onUserVoiceVolumeChanged) | 音量大小的回调（每秒回调一次） |
| [onUserNetworkQualityChanged](#onUserNetworkQualityChanged) | 网络质量的回调（每秒回调一次）|


## 关键类型定义
| API | 描述 |
|-----|-----|
| [TUICallDefine.MediaType]() | 通话的媒体类型，枚举类型：视频通话、语音通话 |
| [TUICallDefine.Role]() | 通话的角色，枚举类型：主叫、被叫 |
| [TUICallDefine.Status]() | 通话的状态，枚举类型：空闲、待接听、接听中 |
| [TUICommonDefine.RoomId]() | 音视频房间 ID，支持数字、字符串两种类型 |
| [TUICommonDefine.Camera]() | 摄像头 ID 参数，枚举类型：前摄、后摄 |
| [TUICommonDefine.AudioPlaybackDevice]() | 声音的播放设备，枚举类型：扬声器、听筒 |
| [TUICommonDefine.NetworkQualityInfo]() | 当前的网络质量信息 |