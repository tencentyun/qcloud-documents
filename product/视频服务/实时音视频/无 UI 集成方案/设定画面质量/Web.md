本文主要介绍如何在视频通话或互动直播中设置画面质量，开发者可以根据具体业务需求调整视频画面的清晰度和流畅度，获得更好的用户体验。
视频属性包括分辨率、帧率和码率。

## 实现方式

通过本地音视频流 Stream 对象的 `{@link LocalStream#setVideoProfile setVideoProfile()}` 方法设置视频属性：

- 指定一个预定义的 Profile，每个 Profile 对应着一套推荐的分辨率、帧率和码率。
```
const localStream = TRTC.createStream({ userId, audio: true, video: true });
// 设置视频属性 Profile 为 ‘480p’
localStream.setVideoProfile('480p');

localStream.initialize().then(() => {
  console.log('local stream init success');
  localStream.play('local_stream');
});
```

- 指定自定义分辨率、帧率和码率
```
const localStream = TRTC.createStream({ userId, audio: true, video: true });
// 自定义视频分辨率、帧率和码率
localStream.setVideoProfile({ width: 640, height: 480, frameRate: 15, bitrate: 900 /* kpbs */});

localStream.initialize().then(() => {
  console.log('local stream init success');
  localStream.play('local_stream');
});
```

> !
> - v4.8.4 及其之后版本，`{@link LocalStream#setVideoProfile setVideoProfile()}` 方法支持动态调用，详细信息请查看 `{@link LocalStream#setVideoProfile setVideoProfile()}` 接口描述。
> - v4.8.4 之前版本，`{@link LocalStream#setVideoProfile setVideoProfile()}` 需要在本地流调用 `{@link LocalStream#initialize initialize()}` 初始化之前调用，不支持在通话过程中动态调整视频属性。

## 视频属性 Profile 列表

| 视频 Profile | 分辨率（宽 × 高） | 帧率（fps） | 码率（kbps） |
| :----------- | :---------------- | :---------- | :----------- |
| 120p         | 160 × 120         | 15          | 200          |
| 180p         | 320 × 180         | 15          | 350          |
| 240p         | 320 × 240         | 15          | 400          |
| 360p         | 640 × 360         | 15          | 800          |
| 480p         | 640 × 480         | 15          | 900          |
| 720p         | 1280 × 720        | 15          | 1500         |
| 1080p        | 1920 × 1080       | 15          | 2000         |
| 1440p        | 2560 × 1440       | 30          | 4860         |
| 4K           | 3840 × 2160       | 30          | 9000         |

由于设备和浏览器的限制，视频分辨率不一定能够完全匹配，在这种情况下，浏览器会自动调整分辨率使其接近 Profile 对应的分辨率
