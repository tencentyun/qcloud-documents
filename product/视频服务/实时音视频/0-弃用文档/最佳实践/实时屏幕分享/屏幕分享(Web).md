TRTC Web SDK 屏幕分享支持度请查看 [浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)。同时 SDK 提供 [TRTC.isScreenShareSupported](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.isScreenShareSupported) 接口判断当前浏览器是否支持屏幕分享。
本文通过以下不同的场景介绍实现过程。

> !
> - Web 端暂不支持发布辅流，发布屏幕分享是通过发布主流实现的。远端屏幕分享流来自于 Web 用户时，[RemoteStream.getType()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/RemoteStream.html#getType) 返回值为 'main'，通常会通过 userId 来标识这是来自 Web 端屏幕分享流。
> - Native（iOS、Android、Mac、Windows 等）端支持发布辅流，并且发布屏幕分享是通过发布辅流实现的。远端屏幕分享流来自于 Native 用户时，[RemoteStream.getType()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/RemoteStream.html#getType) 返回值为 'auxiliary'。

## 创建和发布屏幕分享流
>!请严格按照以下顺序执行创建和发布屏幕分享流的代码。

### 步骤1：创建屏幕分享流
屏幕分享流包含视频流和音频流。其中音频流分为麦克风音频或者系统音频。
<dx-codeblock>
:::javascript
// good 正确用法
// 仅采集屏幕视频流
const shareStream = TRTC.createStream({ audio: false, screen: true, userId });
// or 采集麦克风音频及屏幕视频流
const shareStream = TRTC.createStream({ audio: true, screen: true, userId });
// or 采集系统音频及屏幕视频流
const shareStream = TRTC.createStream({ screenAudio: true, screen: true, userId });

// bad 错误用法
const shareStream = TRTC.createStream({ camera: true, screen: true });
// or
const shareStream = TRTC.createStream({ camera: true, screenAudio: true });

:::
</dx-codeblock>

>! 
>- audio 与 screenAudio 属性不能同时设为true，camera 与 screenAudio 属性不能同时设为 true。关于 screenAudio 更多信息会在本文第五部分介绍。
>- camera 与 screen 属性不能同时设为 true。

### 步骤2：初始化屏幕分享流
初始化时浏览器会向用户请求屏幕共享的内容和权限，如果用户拒绝授权或者系统未授予浏览器屏幕分享的权限，代码会捕获到 `NotReadableError` 或者 `NotAllowedError` 错误，这时需要引导用户进行浏览器设置或者系统设置开启屏幕共享权限，并且重新初始化屏幕分享流。
>! 由于 Safari 的限制，屏幕分享流的初始化操作，必须在点击事件的回调中完成，该问题详细介绍请参见本文 [常见问题](#que)。

<dx-codeblock>
:::javascript
try {
  await shareStream.initialize();
} catch (error) {
  // 当屏幕分享流初始化失败时, 提醒用户并停止后续进房发布流程
  switch (error.name) {
    case 'NotReadableError':
      // 提醒用户确保系统允许当前浏览器获取屏幕内容
      return;
    case 'NotAllowedError':
      if (error.message.includes('Permission denied by system')) {
        // 提醒用户确保系统允许当前浏览器获取屏幕内容
      } else {
        // 用户拒绝/取消屏幕分享
      }
      return;
    default:
      // 初始化屏幕分享流时遇到了未知错误，提醒用户重试
      return;
  }
}
:::
</dx-codeblock>

### 步骤3：创建负责进行屏幕分享的客户端对象
通常情况下，建议给 userId 加上前缀 `share_`，用来标识这是一个屏幕分享的客户端对象。

<dx-codeblock>
:::javascript
const shareClient = TRTC.createClient({
  mode: 'rtc',
  sdkAppId,
  userId, // 例如：‘share_teacher’
  userSig
});
// 客户端对象进入房间
try {
  await shareClient.join({ roomId });
  // ShareClient join room success
} catch (error) {
  // ShareClient join room failed
}

:::
</dx-codeblock>
### 步骤4：发布屏幕分享流
通过第一步创建的客户端对象进行发布。发布成功后，远端就能收到屏幕分享流。
<dx-codeblock>
:::javascript
try {
  await shareClient.publish(shareStream);
} catch (error) {
  // ShareClient failed to publish local stream
}
:::
</dx-codeblock>

### 完整代码
<dx-codeblock>
:::javascript
// 通常情况下，建议给 userId 加上前缀 `share_`，用来标识这是用于屏幕分享的客户端对象。
const userId = 'share_userId';
const roomId = 'roomId';
// 仅采集屏幕视频流
const shareStream = TRTC.createStream({ audio: false, screen: true, userId });
// or 采集麦克风音频及屏幕视频流
// const shareStream = TRTC.createStream({ audio: true, screen: true, userId });
// or 采集系统音频及屏幕视频流
// const shareStream = TRTC.createStream({ screenAudio: true, screen: true, userId });
try {
  await shareStream.initialize();
} catch (error) {
  // 当屏幕分享流初始化失败时, 提醒用户并停止后续进房发布流程
  switch (error.name) {
    case 'NotReadableError':
      // 提醒用户确保系统允许当前浏览器获取屏幕内容
      return;
    case 'NotAllowedError':
      if (error.message.includes('Permission denied by system')) {
        // 提醒用户确保系统允许当前浏览器获取屏幕内容
      } else {
        // 用户拒绝/取消屏幕分享
      }
      return;
    default:
      // 初始化屏幕分享流时遇到了未知错误，提醒用户重试
      return;
  }
}
const shareClient = TRTC.createClient({
  mode: 'rtc',
  sdkAppId,
  userId, // 例如：‘share_teacher’
  userSig
});
// 客户端对象进入房间
try {
  await shareClient.join({ roomId });
  // ShareClient join room success
} catch (error) {
  // ShareClient join room failed
}
try {
  await shareClient.publish(shareStream);
} catch (error) {
  // ShareClient failed to publish local stream
}:::
</dx-codeblock>

## 屏幕分享参数配置
可设置的参数包括分辨率、帧率和码率，如果有需要可以通过 [setScreenProfile()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html#setScreenProfile) 接口指定 profile，每个 profile 对应着一组分辨率、帧率和码率。SDK 默认使用 '1080p' 的配置。

<dx-codeblock>
:::javascript
const shareStream = TRTC.createStream({ audio: false, screen: true, userId });
// setScreenProfile() 必须在 initialize() 之前调用。
shareStream.setScreenProfile('1080p');
await shareStream.initialize();
:::
</dx-codeblock>

或者使用自定义分辨率、帧率和码率：

<dx-codeblock>
:::javascript
const shareStream = TRTC.createStream({ audio: false, screen: true, userId });
// setScreenProfile() 必须在 initialize() 之前调用。
shareStream.setScreenProfile({ width: 1920, height: 1080, frameRate: 5, bitrate: 1600 /* kbps */});
await shareStream.initialize();
:::
</dx-codeblock>
屏幕分享属性推荐列表：

| profile | 分辨率（宽 x 高） | 帧率（fps） | 码率 (kbps) |
|:--------|:----------------|:----------|:------------|
| 480p    | 640 x 480       | 5         | 900         |
| 480p_2  | 640 x 480       | 30        | 1000        |
| 720p    | 1280 x 720      | 5         | 1200        |
| 720p_2  | 1280 x 720      | 30        | 3000        |
| 1080p   | 1920 x 1080     | 5         | 1600        |
| 1080p_2 | 1920 x 1080     | 30        | 4000        |

>! 建议按照推荐的参数进行配置，避免设置过高的参数，引发不可预料的问题。

## 停止屏幕分享

<dx-codeblock>
:::javascript
// 屏幕分享客户端取消发布流
await shareClient.unpublish(shareStream);
// 关闭屏幕分享流
shareStream.close();
// 屏幕分享客户端退房
await shareClient.leave();

// 以上三个步骤非必须，按照场景需求执行需要的代码即可，通常需要添加是否已进房，是否已经发布流的判断，更详细的代码示例请参考 [demo 源码](https://github.com/LiteAVSDK/TRTC_Web/blob/main/base-js/js/share-client.js)。
:::
</dx-codeblock>

另外用户还可能会通过浏览器自带的按钮停止屏幕分享，因此屏幕分享流需要监听屏幕分享停止事件，并进行相应的处理。
<img src="https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/assets/screen-sharing-stop.png" width="600px">

<dx-codeblock>
:::javascript
// 屏幕分享流监听屏幕分享停止事件
shareStream.on('screen-sharing-stopped', event => {
  // 屏幕分享客户端停止推流
  await shareClient.unpublish(shareStream);
  // 关闭屏幕分享流
  shareStream.close();
  // 屏幕分享客户端退房
  await shareClient.leave();
});
:::
</dx-codeblock>

## 同时发布摄像头视频和屏幕分享
一个 Client 至多只能同时发布一路音频和一路视频。同时发布摄像头视频和屏幕分享，需要创建两个 Client，让它们“各司其职”。
例如创建两个 Client 分别为：
- **client**：负责发布本地音视频流，并订阅除了 shareClient 之外的所有远端流。
- **shareClient**：负责发布屏幕分享流，且不订阅任何远端流。

>! 
>- 负责屏幕分享的 shareClient 需要关闭自动订阅，否则会出现重复订阅远端流的情况。请参见 [API说明](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createClient)。
>- 负责本地音视频流发布的 client 需要取消订阅 shareClient 发布的流。否则会出现自己订阅自己的情况。

示例代码：
<dx-codeblock>
:::javascript
const client = TRTC.createClient({ mode: 'rtc', sdkAppId, userId, userSig });
// 需要设置 shareClient 关闭自动订阅远端流，即：autoSubscribe: false
const shareClient = TRTC.createClient({ mode: 'rtc', sdkAppId, `share_${userId}`, userSig, autoSubscribe: false,});

// 负责本地音视频流发布的 client 需要取消订阅 shareClient 发布的流。
client.on('stream-added', event => {
  const remoteStream = event.stream;
  const remoteUserId = remoteStream.getUserId();
  if (remoteUserId === `share_${userId}`) {
    // 取消订阅自己的屏幕分享流
    client.unsubscribe(remoteStream);
  } else {
    // 订阅其他一般远端流
    client.subscribe(remoteStream);
  }
});

await client.join({ roomId });
await shareClient.join({ roomId });

const localStream = TRTC.createStream({ audio: true, video: true, userId }); 
const shareStream = TRTC.createStream({ audio: false, screen: true, userId });

// ... 省略初始化和发布相关代码，按需发布流即可。

:::
</dx-codeblock>

## 屏幕分享采集系统声音

**采集系统声音只支持 Chrome M74+ ，在 Windows 和 Chrome OS 上，可以捕获整个系统的音频，在 Linux 和 Mac 上，只能捕获选项卡的音频。其它 Chrome 版本、其它系统、其它浏览器均不支持。**

<dx-codeblock>
:::javascript
// 创建屏幕分享流 screenAudio 请设置为 true， 不支持同时采集系统和麦克风音量，请勿同时设置 audio 属性为 true
const shareStream = TRTC.createStream({ screenAudio: true, screen: true, userId });
await shareStream.initialize();
...
:::
</dx-codeblock>

在弹出的对话框中勾选`分享音频`，发布的 stream 将会带上系统声音。

![](https://main.qcloudimg.com/raw/4e990a612028480c9c36419d96ea64b7.png)

## 常见问题[](id:que)

1. **Safari 屏幕分享出现报错 `getDisplayMedia must be called from a user gesture handler`**
因为 Safari 限制了 `getDisplayMedia` 屏幕采集的接口，必须在用户点击事件的回调函数执行的 1 秒内才可以调用。请参见  [webkit issue](https://bugs.webkit.org/show_bug.cgi?id=198040)。
```javascript
// good
async function onClick() {
  // 建议在 onClick 执行时，先执行采集逻辑
  const screenStream = TRTC.createStream({ screen: true });
  await screenStream.initialize();
  await client.join({ roomId: 123123 });
}

// bad
async function onClick() {
  await client.join({ roomId: 123123 });
  // 进房可能耗时超过 1s，可能会采集失败
  const screenStream = TRTC.createStream({ screen: true });
  await screenStream.initialize();
}
```
2. [WebRTC 屏幕分享已知问题及规避方案](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-02-info-webrtc-issues.html#h2-9)
