## TUICallObserver API 简介

TUICallObserver 是 TUICallKit 对应的回调事件类，您可以通过此回调，来监听自己感兴趣的回调事件。

<h2 id="TUICallObserver"> 回调事件概览</h2>

| API | 描述 |
|-----|-----|
| [onError](#onError) | 通话过程中错误回调|
| [onCallReceived](#onCallReceived) | 通话请求的回调|
| [onCallCancelled](#onCallCancelled) | 通话取消的回调 |
| [onCallBegin](#onCallBegin) | 通话接通的回调|
| [onCallEnd](#onCallEnd) | 通话结束的回调|

<h2 id="TUICallObserver"> 回调事件详情</h2>

通过 globalEvent 监听原生插件抛出的事件。
```
const TUICallingEvent = uni.requireNativePlugin('globalEvent');
```

### onError

错误回调。
>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```javascript
TUICallingEvent.addEventListener('onError', (code, msg) => {
  console.log('onError', code, msg);
});
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| msg | String | 错误信息。 |

### onCallReceived

收到一个新的来电请求回调，被叫会收到，您可以通过监听这个事件，来决定是否显示通话接听界面。
```javascript
TUICallingEvent.addEventListener('onCallReceived', (callerId, calleeIdList, isGroupCall, callMediaType) => {
  console.log('onCallReceived', callerId, calleeIdList, isGroupCall, callMediaType);
});
```

### onCallCancelled

表示此次通话被主叫取消（取消原因有可能是主叫主动取消、也有可能是来自于通话超时取消），被叫会收到，您可以通过监听这个事件来实现类似未接来电等显示逻辑。
```javascript
TUICallingEvent.addEventListener('onCallCancelled', (callerId) => {
  console.log('onCallCancelled', callerId);
});
```

### onCallBegin

表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来开启云端录制、内容审核等流程。
```javascript
TUICallingEvent.addEventListener('onCallBegin', (roomId, callMediaType, callRole) => {
  console.log('onCallBegin', roomId, callMediaType, callRole);
});
```

### onCallEnd

表示通话接通，主叫和被叫都可以收到，您可以通过监听这个事件来显示通话时长、通话类型等信息，或者来停止云端的录制流程。
```javascript
TUICallingEvent.addEventListener('onCallEnd', (roomId, callMediaType, callRole, totalTime) => {
  console.log('onCallEnd', roomId, callMediaType, callRole, totalTime);
});
```

>! 客户端的事件一般都会随着杀进程等异常事件丢失掉，如果您需要通过监听通话时长来完成计费等逻辑，建议可以使用REST API来完成这类流程；
