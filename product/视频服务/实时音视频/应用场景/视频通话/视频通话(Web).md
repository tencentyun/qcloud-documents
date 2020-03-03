本文主要介绍腾讯云 TRTC Web SDK 的基本工作流程以及如何实现一个实时音视频通话功能。

在使用 TRTC Web SDK 中，经常会接触到以下对象：
- Client 对象，代表一个本地客户端。[Client](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html) 类的方法提供了加入通话房间、发布本地流、订阅远端流等功能。
- Stream 对象，代表一个音视频流对象，包括本地音视频流对象 [LocalStream](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html) 和远端音视频流对象 [RemoteStream](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html)。Stream 类的方法主要提供音视频流对象的行为，包括音频和视频的播放控制。

基本音视频通话的 API 调用流程如下图所示：
![](https://main.qcloudimg.com/raw/8ffc08d1face5a69ecd2bfff3afbc765.png)

## 步骤1：创建 Client 对象

通过 [TRTC.createClient()](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createClient) 方法创建 [Client](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html) 对象，参数设置如下：
- `mode`: 实时音视频通话模式，设置为`videoCall`
- `sdkAppId`: 您从腾讯云申请的 sdkAppId
- `userId`: 用户 ID
- `userSig`: 用户签名

```javascript
const client = TRTC.createClient({
  mode: 'videoCall',
  sdkAppId,
  userId,
  userSig
});
```

## 步骤2：进入音视频通话房间

调用 [Client.join()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#join) 进入音视频通话房间。
参数`roomId`：房间 ID

```javascript
client
  .join({ roomId })
  .catch(error => {
    console.error('进房失败 ' + error);
  })
  .then(() => {
    console.log('进房成功');
  });
```

## 步骤3：发布本地流和订阅远端流

1. 使用 [TRTC.createStream()](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createStream) 方法创建本地音视频流。
 以下实例从摄像头及麦克风中采集音视频流，参数设置如下：
 - `userId`：本地流所属的用户 ID
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

3. 在本地流初始化成功后，调用 [Client.publish()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#publish) 方法发布本地流。
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

4. 远端流通过监听事件`client.on('stream-added')`获取，收到该事件后，通过 [Client.subscribe()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#subscribe) 订阅远端音视频流。
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

5. 在本地流初始化成功的回调中，或远端流订阅成功事件回调中，通过调用 [Stream.play()](https://trtc-1252463788.file.myqcloud.com/web/docs/Stream.html#play) 方法在网页中播放音视频。`play`方法接受一个 div 元素 ID 作为参数，SDK 内部会在该 div 元素下自动创建相应的音视频标签并在其上播放音视频。
 - 初始化本地流成功时播放本地流
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
 - 订阅远端流成功时播放远端流
```javascript
client.on('stream-subscribed', event => {
  const remoteStream = event.stream;
  console.log('远端流订阅成功：' + remoteStream.getId());
  // 播放远端流
  remoteStream.play('remote_stream-' + remoteStream.getId());
});
```

## 步骤4：退出音视频通话房间

通话结束时调用 [Client.leave()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#leave) 方法退出音视频通话房间，整个音视频通话会话结束。

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
