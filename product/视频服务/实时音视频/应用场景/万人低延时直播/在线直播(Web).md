本文主要介绍以观众身份进入直播间，然后发起连麦互动的场景，以主播身份进入房间进行直播的场景跟实时音视频通话场景流程一样，请参考 [实时音视频通话](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-01-basic-video-call.html)。

## 步骤1：创建 Client 对象

通过 [TRTC.createClient()](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createClient) 方法创建 [Client](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html) 对象，参数设置：

- `mode`：互动直播模式，设置为`live`
- `sdkAppId`：您从腾讯云申请的 sdkAppId
- `userId`：用户 ID
- `userSig`：用户签名

```javascript
const client = TRTC.createClient({
  mode: 'live',
  sdkAppId,
  userId,
  userSig
});
```

## 步骤2：以观众身份进入直播房间

调用 [Client.join()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#join) 进入音视频通话房间。
参数：

- `roomId`：房间 ID
- `role`：用户角色：
  - `anchor`：主播，主播角色具有发布本地流和接收远端流的权限。默认是主播角色。
  - `audience`：观众，观众角色只有接收远端流的权限，没有发布本地流的权限。若观众想要跟主播连麦互动，需要通过 [Client.switchRole()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#switchRole) 切换角色至`anchor`主播角色后再发布本地流。

```javascript
// 以观众角色进房收看
client
  .join({ roomId, role: 'audience' })
  .catch(error => {
    console.error('进房失败 ' + error);
  })
  .then(() => {
    console.log('进房成功');
  });
```

## 步骤3：收看直播
1. 远端流通过监听事件`client.on('stream-added')`获取，收到该事件后，通过 [Client.subscribe()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#subscribe) 订阅远端音视频流。
>?请在 [Client.join()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#join) 进房前注册`client.on('stream-added')`事件以确保您不会错过远端用户进房通知。
>
```javascript
client.on('stream-added', event => {
  const remoteStream = event.stream;
  console.log('远端流增加: ' + remoteStream.getId());
  //订阅远端流
  client.subscribe(remoteStream);
});
client.on('stream-subscribed', event => {
  const remoteStream = event.stream;
  console.log('远端流订阅成功：' + remoteStream.getId());
  // 播放远端流
  remoteStream.play('remote_stream-' + remoteStream.getId());
});
```
2. 在远端流订阅成功事件回调中，通过调用 [Stream.play()](https://trtc-1252463788.file.myqcloud.com/web/docs/Stream.html#play) 方法在网页中播放音视频。`play`方法接受一个 div 元素 ID 作为参数，SDK 内部会在该 div 元素下自动创建相应的音视频标签并在其上播放音视频。

```javascript
client.on('stream-subscribed', event => {
  const remoteStream = event.stream;
  console.log('远端流订阅成功：' + remoteStream.getId());
  // 播放远端流
  remoteStream.play('remote_stream-' + remoteStream.getId());
});
```

## 步骤4. 跟主播连麦互动

### 步骤4.1 切换角色

使用 [Client.switchRole()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#switchRole) 切换角色到`anchor`主播角色。

```javascript
client
  .switchRole('anchor')
  .catch(error => {
    console.error('角色切换失败 ' + error);
  })
  .then(() => {
    // 角色切换成功，现在是主播角色
  });
```

### 步骤4.2 连麦互动

1. 使用 [TRTC.createStream()](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createStream) 方法创建本地音视频流。
 以下实例从摄像头及麦克风中采集音视频流，参数设置如下：
 - `userId`：本地流所属用户 ID
 - `audio`：是否开启音频
 - `video`：是否开启视频

 ```javascript
const localStream = TRTC.createStream({ userId, audio: true, video: true });
```
2. 调用 [LocalStream.initialize()](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#initialize) 初始化本地音视频流。
```javascript
localStream
  .initialize()
  .catch(error => {
    console.error('初始化本地流失败 ' + error);
  })
  .then(() => {
    console.log('初始化本地流成功');
  });
```
3. 初始化本地流成功时，播放本地流。
```javascript
localStream
  .initialize()
  .catch(error => {
    console.error('初始化本地流失败 ' + error);
  })
  .then(() => {
    console.log('初始化本地流成功');
    localStream.play('local_stream');
  });
```
4. 在本地流初始化成功后，调用 [Client.publish()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#publish) 方法发布本地流，开启观众连麦互动。
```javascript
client
  .publish(localStream)
  .catch(error => {
    console.error('本地流发布失败 ' + error);
  })
  .then(() => {
    console.log('本地流发布成功');
  });
```

## 步骤5：退出直播房间

直播结束时调用 [Client.leave()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#leave) 方法退出直播房间，整个直播会话结束。

```javascript
client.leave().catch(error => {
  console
    .error(error => {
      console.error('退房失败 ' + error);
      // 错误不可恢复，需要刷新页面。
    })
    .then(() => {
      // 退房成功，可再次调用client.join重新进房开启新的通话。
    });
});
```
