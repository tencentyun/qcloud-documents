## TUICallEngine (无 UI 接口)

TUICallEngine API 是音视频通话组件的**无 UI 接口**，您可以使用这套 API 根据您的业务需求自定义封装。

| API | 描述 |
|-----|-----|
| [createInstance](https://tcloud-doc.isd.com/document/product/647/78757?!preview#createInstance) | 创建 TUICallEngine 实例（单例模式）|
| [destroyInstance](https://tcloud-doc.isd.com/document/product/647/78757?!preview#destroyInstance) | 销毁 TUICallEngine 实例（单例模式）|
| [on](https://tcloud-doc.isd.com/document/product/647/78757?!preview#on) | 监听事件|
| [off](https://tcloud-doc.isd.com/document/product/647/78757?!preview#off) | 取消监听事件|
| [login](https://tcloud-doc.isd.com/document/product/647/78757?!preview#login) | 登录接口|
| [logout](https://tcloud-doc.isd.com/document/product/647/78757?!preview#logout) | 登出接口|
| [setSelfInfo](https://tcloud-doc.isd.com/document/product/647/78757?!preview#setSelfInfo) | 设置用户昵称和头像|
| [call](https://tcloud-doc.isd.com/document/product/647/78757?!preview#call) | C2C邀请通话|
| [groupCall](https://tcloud-doc.isd.com/document/product/647/78757?!preview#groupCall) | 群聊邀请通话|
| [accept](https://tcloud-doc.isd.com/document/product/647/78757?!preview#accept) | 接听通话 |
| [reject](https://tcloud-doc.isd.com/document/product/647/78757?!preview#reject) | 拒绝通话 |
| [hangup](https://tcloud-doc.isd.com/document/product/647/78757?!preview#hangup) | 结束通话|
| [switchCallingType](https://tcloud-doc.isd.com/document/product/647/78757?!preview#switchCallingType) | 音视频通话切换|
| [startRemoteView](https://tcloud-doc.isd.com/document/product/647/78757?!preview#startRemoteView) | 启动远端画面渲染|
| [stopRemoteView](https://tcloud-doc.isd.com/document/product/647/78757?!preview#stopRemoteView) | 停止远端画面渲染|
| [startLocalView](https://tcloud-doc.isd.com/document/product/647/78757?!preview#startLocalView) | 启动本地画面渲染|
| [stopLocalView](https://tcloud-doc.isd.com/document/product/647/78757?!preview#stopLocalView) | 停止本地画面渲染|
| [openCamera](https://tcloud-doc.isd.com/document/product/647/78757?!preview#opencamera) | 开启摄像头|
| [closeCamara](https://tcloud-doc.isd.com/document/product/647/78757?!preview#closecamara) | 关闭摄像头|
| [openMicrophone](https://tcloud-doc.isd.com/document/product/647/78757?!preview#openMicrophone) | 打开麦克风|
| [closeMicrophone](https://tcloud-doc.isd.com/document/product/647/78757?!preview#closeMicrophone) | 关闭麦克风|
| [setMicMute](https://tcloud-doc.isd.com/document/product/647/78757?!preview#setmicmute) | 设备麦克风是否静音|
| [setVideoQuality](https://tcloud-doc.isd.com/document/product/647/78757?!preview#setVideoQuality) | 设置视频质量|
| [getDeviceList](https://tcloud-doc.isd.com/document/product/647/78757?!preview#getDeviceList) | 获取设备列表|
| [switchDevice](https://tcloud-doc.isd.com/document/product/647/78757?!preview#switchDevice) | 切换摄像头或麦克风设备|

## 事件类型定义
TUICallEvent 是 TUICallEngine 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

| EVENT | 描述 |
|-----|-----|
| [TUICallEvent.ERROR](https://tcloud-doc.isd.com/document/product/647/78758?!preview#ERROR) | SDK 内部发生了错误|
| [TUICallEvent.SDK_READY](https://tcloud-doc.isd.com/document/product/647/78758?!preview#SDK_READY) | SDK 进入 ready 状态时收到该回调|
| [TUICallEvent.KICKED_OUT](https://tcloud-doc.isd.com/document/product/647/78758?!preview#KICKED_OUT) | 重复登陆，收到该回调说明被踢出房间|
| [TUICallEvent.USER_ACCEPT](https://tcloud-doc.isd.com/document/product/647/78758?!preview#USER_ACCEPT) | 如果有用户接听，那么会收到此回调 |
| [TUICallEvent.USER_ENTER](https://tcloud-doc.isd.com/document/product/647/78758?!preview#USER_ENTER) | 如果有用户同意进入通话，那么会收到此回调|
| [TUICallEvent.USER_LEAVE](https://tcloud-doc.isd.com/document/product/647/78758?!preview#USER_LEAVE) | 如果有用户同意离开通话，那么会收到此回调|
| [TUICallEvent.REJECT](https://tcloud-doc.isd.com/document/product/647/78758?!preview#REJECT) | 用户拒绝通话 |
| [TUICallEvent.NO_RESP](https://tcloud-doc.isd.com/document/product/647/78758?!preview#NO_RESP) | 邀请用户无应答|
| [TUICallEvent.LINE_BUSY](https://tcloud-doc.isd.com/document/product/647/78758?!preview#LINE_BUSY) | 邀请方忙线|
| [TUICallEvent.CALLING_TIMEOUT](https://tcloud-doc.isd.com/document/product/647/78758?!preview#CALLING_TIMEOUT) | 作为被邀请方会收到，收到该回调说明本次通话超时未应答|
| [TUICallEvent.USER_VIDEO_AVAILABLE](https://tcloud-doc.isd.com/document/product/647/78758?!preview#USER_VIDEO_AVAILABLE) | 远端用户开启/关闭了摄像头, 会收到该回调|
| [TUICallEvent.USER_AUDIO_AVAILABLE](https://tcloud-doc.isd.com/document/product/647/78758?!preview#USER_AUDIO_AVAILABLE) | 远端用户开启/关闭了麦克风, 会收到该回调|
| [TUICallEvent.USER_VOICE_VOLUME](https://tcloud-doc.isd.com/document/product/647/78758?!preview#USER_VOICE_VOLUME) | 远端用户说话音量调整, 会收到该回调|
| [TUICallEvent.GROUP_CALL_INVITEE_LIST_UPDATE](https://tcloud-doc.isd.com/document/product/647/78758?!preview#GROUP_CALL_INVITEE_LIST_UPDATE) | 群聊更新邀请列表收到该回调|
| [TUICallEvent.INVITED](https://tcloud-doc.isd.com/document/product/647/78758?!preview#INVITED) | 被邀请进行通话|
| [TUICallEvent.CALLING_CANCEL](https://tcloud-doc.isd.com/document/product/647/78758?!preview#CALLING_CANCEL) | 作为被邀请方会收到，收到该回调说明本次通话被取消了|
| [TUICallEvent.CALLING_END](https://tcloud-doc.isd.com/document/product/647/78758?!preview#CALLING_END) | 收到该回调说明本次通话结束了|
| [TUICallEvent.DEVICED_UPDATED](https://tcloud-doc.isd.com/document/product/647/78758?!preview#DEVICED_UPDATED) | 设备列表更新收到该回调 |
| [TUICallEvent.CALL_TYPE_CHANGED](https://tcloud-doc.isd.com/document/product/647/78758?!preview#CALL_TYPE_CHANGED) | 通话类型切换收到该回调 |

## 文档链接

- [TUICallEngine](https://tcloud-doc.isd.com/document/product/647/78757?!preview)
- [TUICallEvent](https://tcloud-doc.isd.com/document/product/647/78758?!preview)
- [TUICallEngine API 文档](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/TUICallEngine.html)




