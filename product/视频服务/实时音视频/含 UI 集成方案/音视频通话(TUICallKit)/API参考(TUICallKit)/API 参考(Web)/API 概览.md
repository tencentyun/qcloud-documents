## TUICallEngine (无 UI 接口)

TUICallEngine API 是音视频通话组件的**无 UI 接口**，如果 TUICallKit 的交互并不满足您的需求，您可以使用这套 API 根据您的业务需求自定义封装。

| API | 描述 |
|-----|-----|
| [createInstance](#createInstance) | 创建 TUICallEngine 实例（单例模式）|
| [destroyInstance](#destroyInstance) | 销毁 TUICallEngine 实例（单例模式）|
| [on](#on) | 监听事件|
| [off](#off) | 取消监听事件|
| [login](#login) | 登录接口|
| [logout](#logout) | 登出接口|
| [setSelfInfo](#setSelfInfo) | 设置用户昵称和头像|
| [call](#call) | C2C邀请通话|
| [groupCall](#groupCall) | 群聊邀请通话|
| [accept](#accept) | 接听通话 |
| [reject](#reject) | 拒绝通话 |
| [hangup](#hangup) | 结束通话|
| [switchCallingType](#switchCallingType) | 音视频通话切换|
| [startRemoteView](#startRemoteView) | 启动远端画面渲染|
| [stopRemoteView](#stopRemoteView) | 停止远端画面渲染|
| [startLocalView](#startLocalView) | 启动本地画面渲染|
| [stopLocalView](#stopLocalView) | 停止本地画面渲染|
| [openCamera](#opencamera) | 开启摄像头|
| [closeCamara](#closecamara) | 关闭摄像头|
| [openMicrophone](#openMicrophone) | 打开麦克风|
| [closeMicrophone](#closeMicrophone) | 关闭麦克风|
| [setMicMute](#setmicmute) | 设备麦克风是否静音|
| [setVideoQuality](#setVideoQuality) | 设置视频质量|
| [getDeviceList](#getDeviceList) | 获取设备列表|
| [switchDevice](#switchDevice) | 切换摄像头或麦克风设备|

## 事件类型定义
| EVENT | 描述 |
|-----|-----|
| [TUICallEvent.ERROR](#ERROR) | SDK 内部发生了错误|
| [TUICallEvent.SDK_READY](#SDK_READY) | SDK 进入 ready 状态时收到该回调|
| [TUICallEvent.KICKED_OUT](#KICKED_OUT) | 重复登陆，收到该回调说明被踢出房间|
| [TUICallEvent.USER_ACCEPT](#USER_ACCEPT) | 如果有用户接听，那么会收到此回调 |
| [TUICallEvent.USER_ENTER](#USER_ENTER) | 如果有用户同意进入通话，那么会收到此回调|
| [TUICallEvent.USER_LEAVE](#USER_LEAVE) | 如果有用户同意离开通话，那么会收到此回调|
| [TUICallEvent.REJECT](#REJECT) | 用户拒绝通话 |
| [TUICallEvent.NO_RESP](#NO_RESP) | 邀请用户无应答|
| [TUICallEvent.LINE_BUSY](#LINE_BUSY) | 邀请方忙线|
| [TUICallEvent.CALLING_TIMEOUT](#CALLING_TIMEOUT) | 作为被邀请方会收到，收到该回调说明本次通话超时未应答|
| [TUICallEvent.USER_VIDEO_AVAILABLE](#USER_VIDEO_AVAILABLE) | 远端用户开启/关闭了摄像头, 会收到该回调|
| [TUICallEvent.USER_AUDIO_AVAILABLE](#USER_AUDIO_AVAILABLE) | 远端用户开启/关闭了麦克风, 会收到该回调|
| [TUICallEvent.USER_VOICE_VOLUME](#USER_VOICE_VOLUME) | 远端用户说话音量调整, 会收到该回调|
| [TUICallEvent.GROUP_CALL_INVITEE_LIST_UPDATE](#GROUP_CALL_INVITEE_LIST_UPDATE) | 群聊更新邀请列表收到该回调|
| [TUICallEvent.INVITED](#INVITED) | 被邀请进行通话|
| [TUICallEvent.CALLING_CANCEL](#CALLING_CANCEL) | 作为被邀请方会收到，收到该回调说明本次通话被取消了|
| [TUICallEvent.CALLING_END](#CALLING_END) | 收到该回调说明本次通话结束了|
| [TUICallEvent.DEVICED_UPDATED](#DEVICED_UPDATED) | 设备列表更新收到该回调 |
| [TUICallEvent.CALL_TYPE_CHANGED](#CALL_TYPE_CHANGED) | 通话类型切换收到该回调 |

## 文档链接

- [TUICallEngine](https://tcloud-doc.isd.com/document/product/647/78757)
- [TUICallEvent](https://tcloud-doc.isd.com/document/product/647/78758)
- [TUICallEngine API 文档](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/TUICallEngine.html)




