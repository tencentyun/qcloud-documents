## TUICallKit (含 UI 接口)

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景。

| API | 描述 |
|-----|-----|
| [createInstance](#sharedinstance) | 创建 TUICallKit 实例（单例模式）|
| [setSelfInfo](#setSelfInfo) | 设置用户的头像、昵称|
| [call](#call) | 发起 1v1 通话|
| [groupCall](#groupCall) | 发起群组通话|
| [joinInGroupCall](#joinInGroupCall) | 主动加入当前的群组通话中 |
| [setCallingBell](#setCallingBell) | 设置自定义来电铃音 |
| [enableMuteMode](#enableMuteMode) | 开启/关闭静音模式 |
| [enableFloatWindow](#enableFloatWindow) | 开启/关闭悬浮窗功能 |


## TUICallEngine (无 UI 接口)

TUICallEngine API 是音视频通话组件的**无 UI 接口**，如果 TUICallKit 的交互并不满足您的需求，您可以使用这套 API 根据您的业务需求自定义封装。

| API | 描述 |
|-----|-----|
| [createInstance](#createInstance) | 创建 TUICallEngine 实例（单例模式）|
| [destroyInstance](#destroyInstance) | 销毁 TUICallEngine 实例（单例模式）|
| [init](#init) | 完成音视频通话基础能力的鉴权|
| [addObserver](#addObserver) | 增加事件回调|
| [removeObserver](#removeObserver) | 移除回调接口|
| [call](#call) | 发起 1v1 通话|
| [groupCall](#groupCall) | 发起群组通话|
| [accept](#accept) | 接听通话 |
| [reject](#reject) | 拒绝通话 |
| [hangup](#hangup) | 结束通话|
| [ignore](#ignore) | 忽略通话|
| [inviteUser](#inviteUser) | 在群组通话中，邀请其他人加入 |
| [joinInGroupCall](#joinInGroupCall) | 主动加入当前的群组通话中 |
| [switchCallMediaType](#switchCallMediaType) | 切换通话媒体类型，比如视频通话切音频通话|
| [setRenderView](#setRenderView) | 设置显示视频画面的 View 对象 |
| [startRemoteView](#startRemoteView) | 设置显示视频画面的 View 对象 |
| [stopRemoteView](#stopRemoteView) | 设置显示视频画面的 View 对象 |
| [openCamera](#opencamera) | 开启摄像头|
| [closeCamara](#closecamara) | 关闭摄像头|
| [switchCamera](#switchcamera) | 切换前后摄像头|
| [openMicrophone](#setmicmute) | 打开麦克风|
| [closeMicrophone](#sethandsfree) | 关闭麦克风|
| [selectAudioPlaybackDevice](#setmicmute) | 选择音频播放设备（听筒/免提）|
| [setSelfInfo](#setSelfInfo) | 设置用户的头像、昵称|
| [enableMultiDeviceAbility](#enableMultiDeviceAbility) | 开启/关闭 TUICallEngine 的多设备登录模式 （尊享版套餐支持）|



## TUICallObserver 
TUICallObserver 是 TUICallEngine 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

| API | 描述 |
|-----|-----|
| [onError](#onError) | 通话过程中错误回调|
| [onCallReceived](#onCallReceived) | 通话请求的回调|
| [onCallCancelled](#onCallCancelled) | 通话取消的回调 |
| [onCallBegin](#onCallBegin) | 通话接通的回调|
| [onCallEnd](#onCallEnd) | 通话结束的回调|
| [onCallTypeChanged](#onCallTypeChanged) | 通话的媒体类型发生改变的回调|
| [onUserReject](#onUserReject) |  xxxx 用户拒绝通话的回调 |
| [onUserNoResponse](#onUserNoResponse) |  xxxx 用户不响应的回调|
| [onUserLineBusy](#onUserLineBusy) | xxxx 用户忙线的回调|
| [onUserJoin](#onUserJoin) | xxxx 用户加入通话的回调 |
| [onUserLeave](#onUserLeave) | xxxx 用户离开通话的回调|
| [onUserVideoAvailable](#onUserVideoAvailable) | xxx 用户是否有视频流的回调|
| [onUserAudioAvailable](#onUserAudioAvailable) | xxx 用户是否有音频流的回调|
| [onUserVoiceVolumeChanged](#onUserVoiceVolumeChanged) | 所有用户音量大小的反馈回调 |
| [onUserNetworkQualityChanged](#onUserNetworkQualityChanged) | 所有用户网络质量的反馈回调。|


## 关键类型定义
| API | 描述 |
|-----|-----|
| [TUICallMediaType]() | 通话的媒体类型，枚举类型：视频通话、语音通话 |
| [TUICallRole]() | 通话的角色，枚举类型：主叫、被叫 |
| [TUICallStatus]() | 通话的状态，枚举类型：空闲、待接听、接听中 |
| [TUIRoomId]() | 音视频房间Id，支持数字、字符串两种类型 |
| [TUICallCamera]() | 摄像头Id参数，枚举类型：前摄、后摄|
| [TUIAudioPlaybackDevice]() | 声音的播放设备，枚举类型：扬声器、听筒 |
| [TUINetworkQualityInfo]() | 当前的网络质量信息 |







