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
| phone_dialing.mp3 | 发起呼叫时的声音 | 
| phone_hangup.mp3 | 被挂断的声音 | 
| phone_ringing.mp3 | 接到呼叫时的声音 | 

### 替换文案
您可以通过修改 values-zh 和 values-en 中的 `strings.xml` 文件来修改视频通话界面中的字符串内容。


## 方案二：自实现 UI 方案
TUICallKit 的整个通话功能是基于 TUICallEngine 这个无 UI 组件实现的，您可以删掉 tuicallkit 文件夹，完全基于 TUICallEngine 实现一套自己的 UI 界面。

### TUICallEngine

TUICallEngine 是整个通话组件的底层接口，主要提供了1对1音视频通话和群组内通话的发起、接听、拒绝、结束以及设备操作等关键接口。

| API | 描述 |
|-----|-----|
| [createInstance](https://cloud.tencent.com/document/product/647/78749#createinstance) | 创建 TUICallEngine 实例（单例模式）                         |
| [destroyInstance](https://cloud.tencent.com/document/product/647/78749#destroyinstance) | 销毁 TUICallEngine 实例（单例模式）                         |
| [init](https://cloud.tencent.com/document/product/647/78749#init) | 完成音视频通话基础能力的鉴权                                |
| [addObserver](https://cloud.tencent.com/document/product/647/78749#addobserver) | 增加事件回调                                                |
| [removeObserver](https://cloud.tencent.com/document/product/647/78749#removeobserver) | 移除回调接口                                                |
| [call](https://cloud.tencent.com/document/product/647/78749#call) | 发起 1v1 通话                                               |
| [groupCall](https://cloud.tencent.com/document/product/647/78749#groupcall) | 发起群组通话                                                |
| [accept](https://cloud.tencent.com/document/product/647/78749#accept) | 接听通话                                                    |
| [reject](https://cloud.tencent.com/document/product/647/78749#reject) | 拒绝通话                                                    |
| [hangup](https://cloud.tencent.com/document/product/647/78749#hangup) | 结束通话                                                    |
| [ignore](https://cloud.tencent.com/document/product/647/78749#ignore) | 忽略通话                                                    |
| [inviteUser](https://cloud.tencent.com/document/product/647/78749#inviteuser) | 在群组通话中，邀请其他人加入                                |
| [joinInGroupCall](https://cloud.tencent.com/document/product/647/78749#joiningroupcall) | 主动加入当前的群组通话中                                    |
| [switchCallMediaType](https://cloud.tencent.com/document/product/647/78749#switchcallmediatype) | 切换通话媒体类型，比如视频通话切音频通话                    |
| [startRemoteView](https://cloud.tencent.com/document/product/647/78749#startremoteview) | 开始订阅远端用户视频流                                      |
| [stopRemoteView](https://cloud.tencent.com/document/product/647/78749#stopremoteview) | 停止订阅远端用户视频流                                      |
| [openCamera](https://cloud.tencent.com/document/product/647/78749#opencamera) | 开启摄像头                                                  |
| [closeCamera](https://cloud.tencent.com/document/product/647/78749#closecamera) | 关闭摄像头                                                  |
| [switchCamera](https://cloud.tencent.com/document/product/647/78749#switchcamera) | 切换前后摄像头                                              |
| [openMicrophone](https://cloud.tencent.com/document/product/647/78749#openmicrophone) | 打开麦克风                                                  |
| [closeMicrophone](https://cloud.tencent.com/document/product/647/78749#closemicrophone) | 关闭麦克风                                                  |
| [selectAudioPlaybackDevice](https://cloud.tencent.com/document/product/647/78749#selectaudioplaybackdevice) | 选择音频播放设备（听筒/扬声器）                             |
| [setSelfInfo](https://cloud.tencent.com/document/product/647/78749#setselfinfo) | 设置用户的昵称、头像                                        |
| [enableMultiDeviceAbility](https://cloud.tencent.com/document/product/647/78749#enablemultideviceability) | 开启/关闭 TUICallEngine 的多设备登录模式 （尊享版套餐支持） |

## TUICallObserver 
TUICallObserver 是 TUICallEngine 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

| API | 描述 |
|-----|-----|
| [onError](https://cloud.tencent.com/document/product/647/78751#onerror) | 通话过程中错误回调           |
| [onCallReceived](https://cloud.tencent.com/document/product/647/78751#oncallreceived) | 通话请求的回调               |
| [onCallCancelled](https://cloud.tencent.com/document/product/647/78751#oncallcancelled) | 通话取消的回调               |
| [onCallBegin](https://cloud.tencent.com/document/product/647/78751#oncallbegin) | 通话接通的回调               |
| [onCallEnd](https://cloud.tencent.com/document/product/647/78751#oncallend) | 通话结束的回调               |
| [onCallMediaTypeChanged](https://cloud.tencent.com/document/product/647/78751#oncallmediatypechanged) | 通话的媒体类型发生改变的回调 |
| [onUserReject](https://cloud.tencent.com/document/product/647/78751#onuserreject) | xxxx 用户拒绝通话的回调      |
| [onUserNoResponse](https://cloud.tencent.com/document/product/647/78751#onusernoresponse) | xxxx 用户不响应的回调        |
| [onUserLineBusy](https://cloud.tencent.com/document/product/647/78751#onuserlinebusy) | xxxx 用户忙线的回调          |
| [onUserJoin](https://cloud.tencent.com/document/product/647/78751#onuserjoin) | xxxx 用户加入通话的回调      |
| [onUserLeave](https://cloud.tencent.com/document/product/647/78751#onuserleave) | xxxx 用户离开通话的回调      |
| [onUserVideoAvailable](https://cloud.tencent.com/document/product/647/78751#onuservideoavailable) | xxx 用户是否有视频流的回调   |
| [onUserAudioAvailable](https://cloud.tencent.com/document/product/647/78751#onuseraudioavailable) | xxx 用户是否有音频流的回调   |
| [onUserVoiceVolumeChanged](https://cloud.tencent.com/document/product/647/78751#onuservoicevolumechanged) | 所有用户音量大小的反馈回调   |
| [onUserNetworkQualityChanged](https://cloud.tencent.com/document/product/647/78751#onusernetworkqualitychanged) | 所有用户网络质量的反馈回调   |

## 关键类型定义
| API | 描述 |
|-----|-----|
| TUICallDefine.MediaType | 通话的媒体类型，枚举类型：视频通话、语音通话 |
| TUICallDefine.Role | 通话的角色，枚举类型：主叫、被叫 |
| TUICallDefine.Status | 通话的状态，枚举类型：空闲、待接听、接听中 |
| TUICommonDefine.RoomId | 音视频房间Id，支持数字、字符串两种类型 |
| TUICommonDefine.Camera | 摄像头Id参数，枚举类型：前摄、后摄|
| TUICommonDefine.AudioPlaybackDevice | 声音的播放设备，枚举类型：扬声器、听筒 |
| TUICommonDefine.NetworkQualityInfo | 当前的网络质量信息 |

