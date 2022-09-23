## TUICallObserver API 简介

TUICallObserver 是 TUICallKit 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

## 回调事件概览

| API | 描述 |
|-----|-----|
| [onError](#onerror)                 | 通话过程中错误回调 |
| [onCallReceived](#oncallreceived)   | 通话请求的回调     |
| [onCallCancelled](#oncallcancelled) | 通话取消的回调     |
| [onCallBegin](#oncallbegin)         | 通话接通的回调     |
| [onCallEnd](#oncallend)             | 通话结束的回调     |

## 回调事件详情

通过 globalEvent 监听原生插件抛出的事件。
```
const TUICallingEvent = uni.requireNativePlugin('globalEvent');
```

### onError
错误回调。
>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```javascript
TUICallingEvent.addEventListener('onError', (res) => {
  console.log('onError', JSON.stringify(res));
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| res | Object | 错误回调参数 |
| res.code | Number | 错误码 |
| res.msg | String | 错误信息 |

### onCallReceived
收到一个新的来电请求回调，被叫会收到，您可以通过监听这个事件，来决定是否显示通话接听界面。
```javascript
TUICallingEvent.addEventListener('onCallReceived', (res) => {
  console.log('onCallReceived', JSON.stringify(res));
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| res | Object | 回调参数 |
| res.callerId | String | 主叫 ID（邀请方） |
| res.calleeIdList | Array\<String> | 被叫 ID 列表（被邀请方） |
| res.isGroupCall | Boolean | 是否群组通话 |
| res.callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |

### onCallCancelled
表示此次通话被主叫取消（取消原因有可能是主叫主动取消、也有可能是来自于通话超时取消），被叫会收到，您可以通过监听这个事件来实现类似未接来电等显示逻辑。
```javascript
TUICallingEvent.addEventListener('onCallCancelled', (res) => {
  console.log('onCallCancelled', res);
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| res | Object | 回调参数 |
| res.callerId | String | 取消用户的 ID |

### onCallBegin
表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来开启云端录制、内容审核等流程。
```javascript
TUICallingEvent.addEventListener('onCallBegin', (res) => {
  console.log('onCallBegin', JSON.stringify(res));
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| res | Object | 回调参数 |
| res.roomID | Number | 此次通话的音视频房间 Id，目前仅支持数字房间号，后续版本会支持字符串房间号 |
| res.callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |
| res.callRole | Number | 角色，枚举类型：主叫(callRole = 1)、被叫(callRole = 2) |


### onCallEnd
表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来显示通话时长、通话类型等信息，或者来停止云端的录制流程。
```javascript
TUICallingEvent.addEventListener('onCallEnd', (res) => {
  console.log('onCallEnd', JSON.stringify(res));
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| res | Object | 回调参数 |
| res.roomID | Number | 此次通话的音视频房间 Id，目前仅支持数字房间号，后续版本会支持字符串房间号 |
| res.callMediaType | Number | 通话的媒体类型，比如：语音通话(callMediaType = 1)、视频通话(callMediaType = 2) |
| res.callRole | Number | 角色，枚举类型：主叫(callRole = 1)、被叫(callRole = 2) |
| res.totalTime | Number | 此次通话的时长，单位 ms |

>! 客户端的事件一般都会随着杀进程等异常事件丢失掉，如果您需要通过监听通话时长来完成计费等逻辑，建议可以使用REST API来完成这类流程。
