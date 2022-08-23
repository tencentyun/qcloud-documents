## TUICallObserver API 简介

TUICallObserver 是 TUICallEngine 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

[](id:TUICallObserver)
## 回调事件概览

| API | 描述 |
|-----|-----|
| [onError](#onerror)                                         | 通话过程中错误回调         |
| [onCallReceived](#oncallreceived)                           | 通话请求的回调             |
| [onCallCancelled](#oncallcancelled)                         | 通话取消的回调             |
| [onCallBegin](#oncallbegin)                                 | 通话接通的回调             |
| [onCallEnd](#oncallend)                                     | 通话结束的回调             |
| [onCallMediaTypeChanged](#oncallmediatypechanged)           | 通话媒体类型发生改变的回调 |
| [onUserReject](#onuserreject)                               | xxxx 用户拒绝通话的回调    |
| [onUserNoResponse](#onusernoresponse)                       | xxxx 用户不响应的回调      |
| [onUserLineBusy](#onuserlinebusy)                           | xxxx 用户忙线的回调        |
| [onUserJoin](#onuserjoin)                                   | xxxx 用户加入通话的回调    |
| [onUserLeave](#onuserleave)                                 | xxxx 用户离开通话的回调    |
| [onUserVideoAvailable](#onuservideoavailable)               | xxx 用户是否有视频流的回调 |
| [onUserAudioAvailable](#onuseraudioavailable)               | xxx 用户是否有音频流的回调 |
| [onUserVoiceVolumeChanged](#onuservoicevolumechanged)       | 所有用户音量大小的反馈回调 |
| [onUserNetworkQualityChanged](#onusernetworkqualitychanged) | 所有用户网络质量的反馈回调 |

## 回调事件详情

### onError
错误回调。

>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```objc
- (void)onError:(int)code message:(NSString * _Nullable)message;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码 |
| message | NSString | 错误信息 |

### onCallReceived
收到一个新的来电请求回调，被叫会收到，您可以通过监听这个事件，来决定是否显示通话接听界面。

```objc
- (void)onCallReceived:(NSString *)callerId calleeIdList:(NSArray<NSString *> *)calleeIdList isGroupCall:(BOOL)isGroupCall callMediaType:(TUICallMediaType)callMediaType;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callerId | NSString | 主叫 ID（邀请方）|
| calleeIdList | NSArray | 被叫 ID 列表（被邀请方） |
| isGroupCall | BOOL | 是否群组通话 |
| callMediaType | TUICallMediaType | 通话的媒体类型，比如视频通话、语音通话 |

### onCallCancelled
表示此次通话被主叫取消（取消原因有可能是主叫主动取消、也有可能是来自于通话超时取消），被叫会收到，您可以通过监听这个事件来实现类似未接来电等显示逻辑。

```objc
- (void)onCallCancelled:(NSString *)callerId;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callerId | NSString | 取消用户的 ID|

### onCallBegin
表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来开启云端录制、内容审核等流程。

```objc
- (void)onCallBegin:(TUIRoomId *)roomId callMediaType:(TUICallMediaType)callMediaType callRole:(TUICallRole)callRole;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | TUIRoomId | 此次通话的音视频房间 ID，目前仅支持数字房间号，后续版本会支持字符串房间号 |
| callMediaType | TUICallMediaType | 通话的媒体类型，视频通话、语音通话 |
| callRole | TUICallRole | 角色，枚举类型：主叫、被叫 |

### onCallEnd
表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来显示通话时长、通话类型等信息，或者来停止云端的录制流程。

```objc
- (void)onCallEnd:(TUIRoomId *)roomId callMediaType:(TUICallMediaType)callMediaType callRole:(TUICallRole)callRole totalTime:(float)totalTime;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | TUIRoomId | 此次通话的音视频房间 ID，目前仅支持数字房间号，后续版本会支持字符串房间号 |
| callMediaType | TUICallMediaType | 通话的媒体类型，视频通话、语音通话 |
| callRole | TUICallRole | 角色，枚举类型：主叫、被叫 |
| totalTime | float | 此次通话的时长 |

>! 客户端的事件一般都会随着杀进程等异常事件丢失掉，如果您需要通过监听通话时长来完成计费等逻辑，建议可以使用 REST API 来完成这类流程。

### onCallMediaTypeChanged
表示通话的媒体类型发生变化。

```objc
- (void)onCallMediaTypeChanged:(TUICallMediaType)oldCallMediaType newCallMediaType:(TUICallMediaType)newCallMediaType;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| oldCallMediaType | TUICallMediaType | 旧的通话类型 |
| newCallMediaType | TUICallMediaType | 新的通话类型 |

### onUserReject
通话被拒绝的回调，在1v1 通话中，只有主叫方会收到拒绝回调，在群组通话中，所有被邀请者都可以收到该回调。

```objc
- (void)onUserReject:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString | 拒绝用户的 ID。|

### onUserNoResponse
对方无回应的回调。

```objc
- (void)onUserNoResponse:(NSString *)userId;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString | 无响应用户的 ID |

### onUserLineBusy
通话忙线回调。

```objc
- (void)onUserLineBusy:(NSString *)userId;
```

### onUserJoin
有用户进入此次通话的回调。

```objc
- (void)onUserJoin:(NSString *)userId;
```

### onUserLeave
有用户离开此次通话的回调。

```objc
- (void)onUserLeave:(NSString *)userId;
```

### onUserAudioAvailable
用户是否开启音频上行回调。

```objc
- (void)onUserAudioAvailable:(NSString *)userId isAudioAvailable:(BOOL)isAudioAvailable;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString | 用户 ID|
| isAudioAvailable | BOOL | 用户音频是否可用|

### onUserVideoAvailable
用户是否开启视频上行回调。

```objc
- (void)onUserVideoAvailable:(NSString *)userId isVideoAvailable:(BOOL)isVideoAvailable;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString | 通话用户 ID|
| isVideoAvailable | BOOL | 用户视频是否可用|

### onUserVoiceVolumeChanged
用户通话音量的回调。

```objc
- (void)onUserVoiceVolumeChanged:(NSDictionary <NSString *, NSNumber *> *)volumeMap;
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volumeMap | NSDictionary &lt;NSString *, NSNumber *>| 音量表，根据每个 userid 可以获取对应的音量大小，音量最小值为0，音量最大值为100 |
| volumeMap | NSDictionary | 音量表，根据每个 userId 可以获取对应的音量大小，音量最小值为0，音量最大值为100 |

### onUserNetworkQualityChanged
用户网络质量的回调。

```objc
- (void)onUserNetworkQualityChanged:(NSArray<TUINetworkQualityInfo *> *)networkQualityList;
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| networkQualityList | NSArray | 网络状态，根据每个 userId 可以获取对应用户当前的网络质量 |
