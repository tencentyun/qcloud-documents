TRTCAudioCall 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1和多人视频通话。TRTCAudioCall 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [实时语音通话（iOS）](https://cloud.tencent.com/document/product/647/42046)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。


<h2 id="TRTCAudioCall">TRTCAudioCall API 概览</h2>

### SDK 基础函数

| API | 描述 |
|-----|-----|
| [shared](#shared) | 组件单例。|
| [delegate](#delegate) | 设置事件回调。|
| [setup](#setup) | 初始化函数，请在使用所有功能之前先调用该函数进行必要的初始化。|
| [destroy](#destroy) | 销毁函数，如果无需再运行该实例，请调用该接口。|
| [login](#login) | 登录组件接口，所有功能需要先进行登录后才能使用。|
| [logout](#logout) | 登出组件接口，登出后无法再进行拨打操作。|


### 通话操作相关接口函数

| API | 描述 |
|-----|-----|
| [call](#call) | 单人通话邀请。|
| [groupCall](#groupcall) | 群聊通话邀请。|
| [accept](#accept) | 接受当前通话。|
| [reject](#reject) | 拒绝当前通话。|
| [hangup](#hangup) | 结束当前通话。|

### 音频控制相关接口函数

| API | 描述 |
|-----|-----|
| [setMicMute](#setmicmute) | 静音远端音频。|
| [setHandsFree](#sethandsfree) | 设置免提。|

<h2 id="TRTCAudioCallDelegate">TRTCAudioCallDelegate API 概览</h2>

### 通用事件回调

| API | 描述 |
|-----|-----|
| [onError](#onerror) | 错误回调。|

### 邀请方回调

| API | 描述 |
|-----|-----|
| [onReject](#onreject) | 拒绝通话回调。|
| [onNoResp](#onnoresp) | 对方无回应回调。|
| [onLineBusy](#onlinebusy) | 通话忙线回调。|

### 被邀请方回调

| API | 描述 |
|-----|-----|
| [onInvited](#oninvited) | 被邀请通话回调。|
| [onCallingCancel](#oncallingcancel) | 当前通话被取消回调。|
| [onCallingTimeOut](#oncallingtimeout) | 当前通话超时回调。|

### 通用回调

| API | 描述 |
|-----|-----|
| [onGroupCallInviteeListUpdate](#ongroupcallinviteelistupdate) | 群聊更新邀请列表回调。|
| [onUserEnter](#onuserenter) | 用户进入通话回调。|
| [onUserLeave](#onuserleave) | 用户离开通话回调。|
| [onUserAudioAvailable](#onuseraudioavailable) | 用户是否开启音频上行回调。|
| [onUserVoiceVolume](#onuservoicevolume) | 用户通话音量回调。|
| [onCallEnd](#oncallend) | 通话结束回调。|

## SDK 基础函数
### shared
shared 是 TRTCAudioCall 的组件单例。

```swift
@objc public static let shared = TRTCAudioCall()
```

### delegate

[TRTCAudioCall](https://cloud.tencent.com/document/product/647/42046) 事件回调，您可以通过 TRTCAudioCallDelegate 获得 [TRTCAudioCall](https://cloud.tencent.com/document/product/647/42046) 的各种状态通知。
```swift
@objc public weak var delegate: TRTCAudioCallDelegate?
```

>?delegate 是 TRTCAudioCall 的代理回调。

### setup

初始化函数，请在使用所有功能之前先调用该函数进行必要的初始化。
```swift
@objc public func setup()
```

### destroy

销毁函数，如果无需再运行该实例，请调用该接口。
```swift
@objc func destroy()
```

### login

登录组件。
```swift
@objc func login(sdkAppID: UInt32,
                 user: String,
                 userSig: String,
                 success: @escaping (() -> Void),
                 failed: @escaping ((_ code: Int, _ message: String) -> Void))
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppID | UInt32 | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| user | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig | String | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| success | (() -> Void) | 登录成功回调。 |
| failed | ((_ code: Int, _ message: String) -> Void) | 登录失败回调。 |

### logout

登出组件。
```swift
@objc func logout(success: @escaping (() -> Void),
           failed: @escaping ((_ code: Int, _ message: String) -> Void))
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| success | (() -> Void) | 登出成功回调。 |
| failed | ((_ code: Int, _ message: String) -> Void) | 登出失败回调。 |


## 通话操作相关接口函数
### call

单人通话邀请，当前处于通话中也可继续调用邀请他人。

```swift
@objc func call(userID: String)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 呼叫用户 ID。 |

### groupCall

IM 群聊通话邀请，被邀请方会收到 `onInvited()` 回调。如果当前处于通话中，可以继续调用该函数继续邀请他人进入通话，同时正在通话的用户会收到 `onGroupCallInviteeListUpdate()` 回调。

```swift
@objc func groupCall(userIDs: [String], groupID: String)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userIDs | [String] | 邀请 ID 列表。 |
| groupID | String | 群 ID。 |



### accept

接受当前通话。当您作为被邀请方收到 `onInvited()` 的回调时，可以调用该函数接听来电。
```swift
@objc func accept()
```



### reject

拒绝当前通话。当您作为被邀请方收到 `onInvited()` 的回调时，可以调用该函数拒绝来电。
```swift
@objc func reject()
```

### hangup

挂断当前通话。当您处于通话中，可以调用该函数结束通话。

```swift
@objc func hangup()
```

## 音频控制相关接口函数
### setMicMute

静音远端音频。
```swift
@objc func setMicMute(isMute: Bool)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isMute | Bool | true：麦克风关闭，false：麦克风打开。 |

### setHandsFree

静音远端音频。
```swift
@objc func setHandsFree(isHandsFree: Bool)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isHandsFree | Bool | true：开启免提，false：关闭免提。 |

## TRTCAudioCallDelegate事件回调

## 通用事件回调
### onError

错误回调。
>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```swift
@objc optional func onError(code: Int32, msg: String?)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | Int | 错误码。 |
| msg | String? | 错误信息。 |


## 邀请方回调
### onReject

拒绝通话回调。
```swift
@objc optional func onReject(uid: String)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| uid | String | 拒绝用户的 ID。|

### onNoResp

对方无回应回调。
```swift
@objc optional func onNoResp(uid: String)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| uid | String | 无回应用户的 ID。|

### onLineBusy

通话忙线回调。
```swift
@objc optional func onLineBusy(uid: String)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| uid | String | 忙线用户的 ID。|


## 被邀请方回调
### onInvited

被邀请通话回调。
```swift
@objc optional func onInvited(sponsor: String, userIds: [String], isFromGroup: Bool)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sponsor | String | 发起方的 ID。|
| userIds | [String] | 邀请 ID 列表。|
| isFromGroup | Bool | 是否多人通话邀请。|

### onCallingCancel

当前通话被取消回调。接收方未处理请求，邀请方取消后会收到此回调。
```swift
@objc optional func onCallingCancel()
```

### onCallingTimeOut

当前通话超时回调。
```swift
@objc optional func onCallingTimeOut()
```

## 通用回调
### onGroupCallInviteeListUpdate

群聊更新邀请列表回调。
```swift
@objc optional func onGroupCallInviteeListUpdate(userIds: [String])
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userIds | [String] | 邀请 ID 列表。|

### onUserEnter

用户进入通话回调。
```swift
@objc optional func onUserEnter(uid: String)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| uid | String | 进入通话用户 ID。|

### onUserLeave

用户进入通话回调。
```swift
@objc optional func onUserLeave(uid: String)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| uid | String | 离开通话用户 ID。|

### onUserAudioAvailable

用户是否开启音频上行回调。
```swift
@objc optional func onUserAudioAvailable(uid: String, available: Bool)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| uid | String | 通话用户 ID。|
| available | Bool | 用户音频是否可用。|

### onUserVoiceVolume

用户通话音量回调。
```swift
@objc optional func onUserVoiceVolume(uid: String, volume: UInt32)
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| uid | String | 通话用户 ID。|
| volume | UInt32 | 通话者的音量, 取值范围0 - 100。|

### onCallEnd

通话结束回调。
```swift
@objc optional func onCallEnd()
```
