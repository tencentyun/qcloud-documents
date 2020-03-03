本文主要介绍屏幕分享的使用方法。
>!屏幕分享只支持 Chrome M72+。

## 创建和发布屏幕分享流

```
// 创建屏幕分享流
const localStream = TRTC.createStream({ audio: false, screen: true });
// 监听屏幕分享停止事件
localStream.on('screen-sharing-stopped', event => {
  console.log('screen sharing was stopped');
});

// 初始化屏幕分享流
localStream.initialize().then(() => {
  console.log('screencast stream init success');
  // 发布屏幕分享流
  client.publish(localStream).then(() => {
    console.log('screen casting');
  });
});
```

## 屏幕分享属性

屏幕分享属性包括分辨率、帧率和码率，可以通过 {@link LocalStream#setScreenProfile setScreenProfile()} 接口指定一个属性 Profile，每个 Profile 对应着一组分辨率、帧率和码率，也可以使用自定义分辨率、帧率和码率。屏幕分享默认使用 '1080p' Profile。

- 指定属性 Profile：
```
const localStream = TRTC.createStream({ audio: false, screen: true });
localStream.setScreenProfile('1080p');
localStream.initialize().then(() => {
  // screencast stream init success
});
```

- 使用自定义分辨率、帧率和码率：
```
const localStream = TRTC.createStream({ audio: false, screen: true });
localStream.setScreenProfile({ width: 1920, height: 1080, frameRate: 5, bitrate: 1600 /* kbps */});
localStream.initialize().then(() => {
  // screencast stream init success
});
```

屏幕分享属性推荐列表：

| profile | 分辨率（宽 x 高） | 帧率（fps） | 码率 (kbps) |
| :------ | :---------------- | :---------- | :---------- |
| 480p    | 640 x 480         | 5           | 900         |
| 480p_2  | 640 x 480         | 30          | 1000        |
| 720p    | 1280 x 720        | 5           | 1200        |
| 720p_2  | 1280 x 720        | 30          | 3000        |
| 1080p   | 1920 x 1080       | 5           | 1600        |
| 1080p_2 | 1920 x 1080       | 30          | 4000        |



## 同时推送摄像头视频和屏幕分享

一个 {@link Client Client} 至多只能同时推送一路音频和一路视频，若想同时推送摄像头视频和屏幕分享，建议创建另外一个独立的 Client 专门负责推送屏幕分享。

```
// 使用一个独立的用户ID进行推送屏幕分享
const shareId = 'share-userId';
const shareClient = TRTC.createClient({ mode: 'videoCall', sdkAppId, userId: shareId, userSig });

// 指明该 shareClient 默认不接收任何远端流 （它只负责发送屏幕分享流）
shareClient.setDefaultMuteRemoteStreams(true);
shareClient.join().then(() => {
  console.log('shareClient join success');
  // 创建屏幕分享流
  const localStream = TRTC.createStream({ audio: false, screen: true });
  localStream.initialize().then(() => {
    // screencast stream init success
    shareClient.publish(localStream).then(() => {
      console.log('screen casting');
    });
  });
});

// 主 Client 中指定取消订阅 shareId 的远端流
client.on('stream-added', event => {
  const remoteStream = event.stream;
  const remoteUserId = remoteStream.getUserId();
  if (remoteUserId === shareId) {
    // 取消订阅自己的屏幕分享流
    client.unsubscribe(remoteStream);
  } else {
    // 订阅其他一般远端流
    client.subscribe(remoteStream);
  }
});
```
