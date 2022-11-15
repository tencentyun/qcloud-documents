本文档主要介绍如何订阅房间中其他用户的音视频流，也就是如何播放其他用户的音频和视频。为了方便起见，我们在接下来的文档中，会将“房间中的其他用户”统称为“远端用户”。
![](https://qcloudimg.tencent-cloud.cn/raw/692f3cddee1dc9e9dfadde81448643ad.png)

在使用 TRTC Web SDK 中，经常会接触到以下对象：
- Client 对象，代表一个本地客户端。[Client](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html) 类的方法提供了加入通话房间、发布本地流、订阅远端流等功能。
- Stream 对象，代表一个音视频流对象，包括本地音视频流对象 [LocalStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html) 和远端音视频流对象 [RemoteStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/RemoteStream.html)。Stream 类的方法主要提供音视频流对象的行为，包括音频和视频的播放控制。

## 步骤1：创建 Client 对象
可以参考文档 [进入房间-步骤1](https://cloud.tencent.com/document/product/647/74636#step1) 创建 client。

需要特别注意的是，创建 Client 时可选择设置订阅模式，TRTC 提供了两种订阅模式：
 - 自动订阅，当收到 stream-added 事件时，SDK 会立刻接收并解码该远端流所包含的音视频数据，这也是 SDK 的默认行为。
 - 手动订阅，由于负责屏幕分享的 client 只需推流、不需要拉流，因此可在屏幕分享 client 中关闭自动订阅。

```javascript
const client = TRTC.createClient({
  ...,
  autoSubscribe: false // 默认为 true 即自动订阅
});
```

## 步骤2：监听远端流加入事件并订阅远端流
订阅远端流首先需要知道有哪些远端流可以订阅，可以通过监听事件 [Client.on('stream-added')](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-Event.html#.STREAM_ADDED) 获取房间内的远端流，收到该事件说明这个远端流可以进行订阅，在事件回调通过 [Client.subscribe()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#subscribe) 订阅远端音视频流。

```javascript
client.on('stream-added', event => {
  const remoteStream = event.stream;
  console.log('远端流增加: ' + remoteStream.getId());
  //订阅远端流
  client.subscribe(remoteStream);
});
```
>!
>- 在进房之前监听 [Client.on('stream-added')](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-Event.html#.STREAM_ADDED) 事件，以确保您不会错过已在房间内的用户的远端流通知。
>- 远端流离开等其他事件可以在 [API 详细文档](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-Event.html) 中查看。


## 步骤3：监听订阅成功事件并播放远端流
在远端流订阅成功事件回调中，通过调用 [Stream.play()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Stream.html#play) 方法在网页中播放音视频。`play` 方法接受一个 div 元素 ID 或者一个 HTMLDivElement 对象作为参数，SDK 会在该 div 元素下自动创建相应的音视频标签并播放音视频。

`play` 方法更详细的参数说明参见 [Stream.play()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Stream.html#play)。 

```javascript
client.on('stream-subscribed', event => {
  const remoteStream = event.stream;
  console.log('远端流订阅成功：' + remoteStream.getId());
  // 播放远端流
  remoteStream.play('remote-stream-' + remoteStream.getId());
});
```
需要特别注意的是，由于[浏览器限制自动播放策略](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-21-advanced-auto-play-policy.html)的影响，调用 `play` 方法可能会返回 PLAY_NOT_ALLOWED 错误， 此时 SDK 会弹窗引导用户与页面产生交互。当产生交互后，SDK 会主动调用接口恢复播放。

您也可以在 [TRTC.createClient()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createClient) 接口中将 enableAutoPlayDialog 参数设置为 false，来关闭 SDK 的弹窗功能，并且由自己实现引导用户通过点击等操作调用 [Stream.resume()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Stream.html#resume) 恢复音视频播放。

```javascript
client.on('stream-subscribed', event => {
  const remoteStream = event.stream;
  console.log('远端流订阅成功：' + remoteStream.getId());
  // 使用 remoteStream 监听 error 的方式捕捉并处理 0x4043 错误
  remoteStream.on('error', error => {
    const errorCode = error.getCode();
    if (errorCode === 0x4043) {
      // PLAY_NOT_ALLOWED, 引导用户手势操作并调用 stream.resume 恢复音视频播放
      // remoteStream.resume()
    }
  });
  // 开始播放远端流
  remoteStream.play('remote-stream-' + remoteStream.getId());
});
```

## 步骤4：进入音视频通话房间
监听事件后，即可调用 Client.join() 进入音视频通话房间。可以参考文档 [进入房间-步骤2](https://cloud.tencent.com/document/product/647/74636#step2)。

## 完整代码

```javascript

const client = TRTC.createClient({
  mode: 'rtc',
  sdkAppId,
  userId,
  userSig
});

client.on('stream-added', event => {
  const remoteStream = event.stream;
  console.log('远端流增加: ' + remoteStream.getId());
  //订阅远端流
  client.subscribe(remoteStream);
});

client.on('stream-subscribed', event => {
  const remoteStream = event.stream;
  console.log('远端流订阅成功：' + remoteStream.getId());
  // 使用 remoteStream 监听 error 的方式捕捉并处理 0x4043 错误
  remoteStream.on('error', error => {
    const errorCode = error.getCode();
    if (errorCode === 0x4043) {
      // PLAY_NOT_ALLOWED, 引导用户手势操作并调用 stream.resume 恢复音视频播放
      // remoteStream.resume()
    }
  });
  // 开始播放远端流
  remoteStream.play('remote-stream-' + remoteStream.getId());
});

try {
  await client.join({ roomId });
  console.log('进房成功');
} catch (error) {
  console.error('进房失败，请稍后再试' + error);
}
```