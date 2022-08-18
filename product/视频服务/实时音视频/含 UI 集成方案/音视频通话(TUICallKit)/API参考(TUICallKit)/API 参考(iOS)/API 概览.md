## TUICallKit (含 UI 接口)

TUICallKit API 是音视频通话组件的**含 UI 接口**，使用TUICallKit API，您可以通过简单接口快速实现一个类微信的音视频通话场景。

| API | 描述 |
|-----|-----|
| [createInstance](https://cloud.tencent.com/document/product/647/78753#createinstance) | 创建 TUICallKit 实例（单例模式） |
| [setSelfInfo](https://cloud.tencent.com/document/product/647/78753#setselfinfo) | 设置用户的头像、昵称             |
| [call](https://cloud.tencent.com/document/product/647/78753#call) | 发起 1v1 通话                    |
| [groupCall](https://cloud.tencent.com/document/product/647/78753#groupcall) | 发起群组通话                     |
| [joinInGroupCall](https://cloud.tencent.com/document/product/647/78753#joiningroupcall) | 主动加入当前的群组通话中         |
| [setCallingBell](https://cloud.tencent.com/document/product/647/78753#setcallingbell) | 设置自定义来电铃音               |
| [enableMuteMode](https://cloud.tencent.com/document/product/647/78753#enablemutemode) | 开启/关闭静音模式                |
| [enableFloatWindow](https://cloud.tencent.com/document/product/647/78753#enablefloatwindow) | 开启/关闭悬浮窗功能              |


## TUICallEngine (无 UI 接口)

TUICallEngine API 是音视频通话组件的**无 UI 接口**，如果 TUICallKit 的交互并不满足您的需求，您可以使用这套 API 根据您的业务需求自定义封装。

| API | 描述 |
|-----|-----|
| [createInstance](https://cloud.tencent.com/document/product/647/78754#createinstance) | 创建 TUICallEngine 实例（单例模式）                         |
| [destroyInstance](https://cloud.tencent.com/document/product/647/78754#destroyinstance) | 销毁 TUICallEngine 实例（单例模式）                         |
| [init](https://cloud.tencent.com/document/product/647/78754#init) | 完成音视频通话基础能力的鉴权                                |
| [addObserver](https://cloud.tencent.com/document/product/647/78754#addobserver) | 增加事件回调                                                |
| [removeObserver](https://cloud.tencent.com/document/product/647/78754#removeobserver) | 移除回调接口                                                |
| [call](https://cloud.tencent.com/document/product/647/78754#call) | 发起 1v1 通话                                               |
| [groupCall](https://cloud.tencent.com/document/product/647/78754#groupcall) | 发起群组通话                                                |
| [accept](https://cloud.tencent.com/document/product/647/78754#accept) | 接听通话                                                    |
| [reject](https://cloud.tencent.com/document/product/647/78754#reject) | 拒绝通话                                                    |
| [hangup](https://cloud.tencent.com/document/product/647/78754#hangup) | 结束通话                                                    |
| [ignore](https://cloud.tencent.com/document/product/647/78754#ignore) | 忽略通话                                                    |
| [inviteUser](https://cloud.tencent.com/document/product/647/78754#inviteuser) | 在群组通话中，邀请其他人加入                                |
| [joinInGroupCall](https://cloud.tencent.com/document/product/647/78754#joiningroupcall) | 主动加入当前的群组通话中                                    |
| [switchCallMediaType](https://cloud.tencent.com/document/product/647/78754#switchcallmediatype) | 切换通话媒体类型，比如视频通话切音频通话                    |
| [setRenderView](https://cloud.tencent.com/document/product/647/78754#setrenderview) | 设置显示视频画面的 View 对象                                |
| [startRemoteView](https://cloud.tencent.com/document/product/647/78754#startremoteview) | 设置显示视频画面的 View 对象                                |
| [stopRemoteView](https://cloud.tencent.com/document/product/647/78754#stopremoteview) | 设置显示视频画面的 View 对象                                |
| [openCamera](https://cloud.tencent.com/document/product/647/78754#opencamera) | 开启摄像头                                                  |
| [closeCamera](https://cloud.tencent.com/document/product/647/78754#closecamera) | 关闭摄像头                                                  |
| [switchCamera](https://cloud.tencent.com/document/product/647/78754#switchcamera) | 切换前后摄像头                                              |
| [openMicrophone](https://cloud.tencent.com/document/product/647/78754#openmicrophone) | 打开麦克风                                                  |
| [closeMicrophone](https://cloud.tencent.com/document/product/647/78754#closemicrophone) | 关闭麦克风                                                  |
| [selectAudioPlaybackDevice](https://cloud.tencent.com/document/product/647/78754#selectaudioplaybackdevice) | 选择音频播放设备（听筒/免提）                               |
| [setSelfInfo](https://cloud.tencent.com/document/product/647/78754#setselfinfo) | 设置用户的头像、昵称                                        |
| [enableMultiDeviceAbility](https://cloud.tencent.com/document/product/647/78754#enablemultideviceability) | 开启/关闭 TUICallEngine 的多设备登录模式 （尊享版套餐支持） |

## TUICallObserver 
TUICallObserver 是 TUICallEngine 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

| API | 描述 |
|-----|-----|
| [onError](https://cloud.tencent.com/document/product/647/78755#onerror) | 通话过程中错误回调           |
| [onCallReceived](https://cloud.tencent.com/document/product/647/78755#oncallreceived) | 通话请求的回调               |
| [onCallCancelled](https://cloud.tencent.com/document/product/647/78755#oncallcancelled) | 通话取消的回调               |
| [onCallBegin](https://cloud.tencent.com/document/product/647/78755#oncallbegin) | 通话接通的回调               |
| [onCallEnd](https://cloud.tencent.com/document/product/647/78755#oncallend) | 通话结束的回调               |
| [onCallMediaTypeChanged](https://cloud.tencent.com/document/product/647/78755#oncallmediatypechanged) | 通话的媒体类型发生改变的回调 |
| [onUserReject](https://cloud.tencent.com/document/product/647/78755#onuserreject) | xxxx 用户拒绝通话的回调      |
| [onUserNoResponse](https://cloud.tencent.com/document/product/647/78755#onusernoresponse) | xxxx 用户不响应的回调        |
| [onUserLineBusy](https://cloud.tencent.com/document/product/647/78755#onuserlinebusy) | xxxx 用户忙线的回调          |
| [onUserJoin](https://cloud.tencent.com/document/product/647/78755#onuserjoin) | xxxx 用户加入通话的回调      |
| [onUserLeave](https://cloud.tencent.com/document/product/647/78755#onuserleave) | xxxx 用户离开通话的回调      |
| [onUserVideoAvailable](https://cloud.tencent.com/document/product/647/78755#onuservideoavailable) | xxx 用户是否有视频流的回调   |
| [onUserAudioAvailable](https://cloud.tencent.com/document/product/647/78755#onuseraudioavailable) | xxx 用户是否有音频流的回调   |
| [onUserVoiceVolumeChanged](https://cloud.tencent.com/document/product/647/78755#onuservoicevolumechanged) | 所有用户音量大小的反馈回调   |
| [onUserNetworkQualityChanged](https://cloud.tencent.com/document/product/647/78755#onusernetworkqualitychanged) | 所有用户网络质量的反馈回调   |


## 关键类型定义
| API | 描述 |
|-----|-----|
| TUICallMediaType | 通话的媒体类型，枚举类型：视频通话、语音通话 |
| TUICallRole | 通话的角色，枚举类型：主叫、被叫 |
| TUICallStatus | 通话的状态，枚举类型：空闲、待接听、接听中 |
| TUIRoomId | 音视频房间Id，支持数字、字符串两种类型 |
| TUICallCamera | 摄像头Id参数，枚举类型：前摄、后摄|
| TUIAudioPlaybackDevice | 声音的播放设备，枚举类型：扬声器、听筒 |
| TUINetworkQualityInfo | 当前的网络质量信息 |
