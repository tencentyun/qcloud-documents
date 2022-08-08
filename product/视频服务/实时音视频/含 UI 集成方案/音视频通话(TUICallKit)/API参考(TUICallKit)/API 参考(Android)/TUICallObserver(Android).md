## TUICallObserver API 简介

TUICallObserver 是 TUICallEngine 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

<h2 id="TUICallObserver"> 回调事件概览</h2>

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

<h2 id="TUICallObserver"> 回调事件详情</h2>

### onError

错误回调。
>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```java
void onError(int code, String msg);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码 |
| msg | String | 错误信息 |

### onCallReceived

收到一个新的来电请求回调，被叫会收到，您可以通过监听这个事件，来决定是否显示通话接听界面。
```java
void onCallReceived(String callerId, List<String> calleeIdList, boolean isGroupCall, TUICallDefine.MediaType callMediaType);
```

### onCallCancelled

表示此次通话被主叫取消（取消原因有可能是主叫主动取消、也有可能是来自于通话超时取消），被叫会收到，您可以通过监听这个事件来实现类似未接来电等显示逻辑。
```java
void onCallCancelled(String callerId);
```

### onCallBegin

表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来开启云端录制、内容审核等流程。
```java
void onCallBegin(TUICommonDefine.RoomId roomId, TUICallDefine.MediaType callMediaType, TUICallDefine.Role callRole);
```

### onCallEnd

表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来显示通话时长、通话类型等信息，或者来停止云端的录制流程。
```java
void onCallEnd(TUICommonDefine.RoomId roomId, TUICallDefine.MediaType callMediaType, TUICallDefine.Role callRole, long totalTime);
```

>! 客户端的事件一般都会随着杀进程等异常事件丢失掉，如果您需要通过监听通话时长来完成计费等逻辑，建议可以使用REST API来完成这类流程。


### onCallMediaTypeChanged

表示通话的媒体类型发生变化。
```java
void onCallMediaTypeChanged(TUICallDefine.MediaType oldCallMediaType,TUICallDefine.MediaType newCallMediaType);
```

### onUserReject

通话被拒绝的回调，在1v1 通话中，只有主叫方会收到拒绝回调，在群组通话中，所有被邀请者都可以收到该回调。
```java
void onUserReject(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 拒绝用户的 ID |

### onUserNoResponse

对方无回应的回调。
```java
void onUserNoResponse(String userId);
```
### onUserLineBusy

通话忙线回调。
```java
void onUserLineBusy(String userId);
```

### onUserJoin

有用户进入此次通话的回调。
```java
void onUserJoin(String userId);
```

### onUserLeave

有用户离开此次通话的回调。
```java
void onUserLeave(String userId);
```

### onUserVideoAvailable

用户是否开启视频上行回调。
```java
void onUserVideoAvailable(String userId, boolean isVideoAvailable);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 通话用户 ID|
| isVideoAvailable | boolean | 用户视频是否可用|

### onUserAudioAvailable

用户是否开启音频上行回调。
```java
void onUserAudioAvailable(String userId, boolean isAudioAvailable);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID|
| isAudioAvailable | boolean | 用户音频是否可用|

### onUserVoiceVolumeChanged

用户通话音量的回调。
```java
void onUserVoiceVolumeChanged(Map<String, Integer> volumeMap);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volumeMap | Map<String, Integer> | 音量表，根据每个 userid 可以获取对应的音量大小，音量最小值为0，音量最大值为100 |

### onUserNetworkQualityChanged

用户网络质量的回调。
```java
void onUserNetworkQualityChanged(List<TUICallDefine.NetworkQualityInfo> networkQualityList);
```