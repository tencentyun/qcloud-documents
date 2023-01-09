本文主要介绍本地流的自定义采集和音视频流的自定义播放渲染等高阶用法。

## 自定义采集

本地流在通过 {@link TRTC.createStream createStream()} 创建时，可以指定使用 SDK 的默认采集方式，

如下，从摄像头和麦克风采集音视频数据：

```
const localStream = TRTC.createStream({ userId, audio: true, video: true });
localStream.initialize().then(() => {
  // local stream initialized success
});
```

或者，采集屏幕分享流：

```
const localStream = TRTC.createStream({ userId, audio: false, screen: true });
localStream.initialize().then(() => {
  // local stream initialized success
});
```

上述两种本地流的创建方式都是使用 SDK 的默认采集方式。为了便于开发者对音视频流进行预处理，createStream 支持从外部音视频源创建本地流，通过这种方式创建本地流，开发者可以实现自定义采集，比如说：

- 可以通过使用 [getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) 采集摄像头和麦克风音视频流。
- 通过 [getDisplayMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia) 采集屏幕分享流。
- 通过 [captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/captureStream) 采集页面中正在播放的音视频。
- 通过 [captureStream](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream) 采集 canvas 画布中的动画。

### 采集页面中正在播放的视频源

```javascript
// 检测您当前的浏览器是否支持从 video 元素采集 stream
const isVideoCapturingSupported = () => {
	if (typeof document === 'undefined') {
		return false;
	}
	const videoElement = document.createElement('video');
	return ['captureStream', 'mozCaptureStream', 'webkitCaptureStream'].some(item => item in videoElement);
};

// 检测您当前的浏览器是否支持从 video 元素采集 stream
if (!isVideoCapturingSupported()) {
	console.log('your browser does not support capturing stream from video element');
	return
}
// 获取您页面在播放视频的 video 标签 
const video = document.getElementByID('your-video-element-ID');
// 从播放的视频采集视频流
const stream = video.captureStream();
const audioTrack = stream.getAudioTracks()[0];
const videoTrack = stream.getVideoTracks()[0];

const localStream = TRTC.createStream({ userId, audioSource: audioTrack, videoSource: videoTrack });

// 请确保视频属性跟外部传进来的视频源一致，否则会影响视频通话体验
localStream.setVideoProfile('480p');

localStream.initialize().then(() => {
    // local stream initialized success
});
```

### 采集 canvas 中的动画

```javascript
// 检测您当前的浏览器是否支持从 canvas 元素采集 stream
const isCanvasCapturingSupported = () => {
	if (typeof document === 'undefined') {
		return false;
	}
	const canvasElement = document.createElement('canvas');
	return ['captureStream', 'mozCaptureStream', 'webkitCaptureStream'].some(item => item in canvasElement);
};

// 检测您当前的浏览器是否支持从 canvas 元素采集 stream
if (!isCanvasCapturingSupported()) {
	console.log('your browser does not support capturing stream from canvas element');
	return
}
// 获取您的 canvas 标签 
const canvas = document.getElementByID('your-canvas-element-ID');

// 从 canvas 采集 15 fps 的视频流
const fps = 15;
const stream = canvas.captureStream(fps);
const videoTrack = stream.getVideoTracks()[0];

const localStream = TRTC.createStream({ userId, videoSource: videoTrack });

// 请确保视频属性跟外部传进来的视频源一致，否则会影响视频通话体验
localStream.setVideoProfile('480p');

localStream.initialize().then(() => {
    // local stream initialized success
});
```

## 自定义播放渲染

对于通过 TRTC.createStream() 创建并初始化好的本地流或者通过 Client.on('stream-added') 接收到的远端流，可以通过音视频流对象的 {@link Stream#play Stream.play()} 方法进行音频和视频的播放渲染，Stream.play() 内部会自动创建音频播放器和视频播放器并将相应地 <audio>/<video> 标签插入到 App 传下来的 Div 容器中。

如果 App 想用自己的播放器，可以绕过 Stream.play()/stop() 方法调用，通过 {@link Stream#getAudioTrack Stream.getAudioTrack()}/{@link Stream#getVideoTrack Stream.getVideoTrack()} 方法获取相应的音视频轨道，然后利用自己的播放器进行音视频的播放渲染。使用这种自定义播放渲染方式后，Stream.on('player-state-changed') 事件将不会被触发，App 需要自行监听音视频轨道 [MediaStreamTrack](https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack) 的 `mute/unmute/ended` 等事件来判断当前音视频数据流的状态。

同时，App 层需要监听 `Client.on('stream-added')`、`Client.on('stream-updated')` 和 `Client.on('stream-removed')` 等事件来处理音视频流的生命周期。

> !
> - 在 'stream-added' 与 'stream-updated' 两个事件的处理回调中，都必须检查是否有音频或视频 track，在 ’stream-updated‘ 事件处理中，如果有音频或视频 track，那么请务必更新播放器并使用最新的音视频 track 进行播放。
> - [线上示例](https://web.sdk.qcloud.com/trtc/webrtc/demo/latest/custom-capture-render/index.html)
