>?当前推流 SDK 为内测版本，相关计费规则以后续发布的正式版本为准。

SDK 提供了对视频流画面的处理功能，包括多路视频流的混合（画中画）、画面效果的处理（镜像、滤镜）和其他元素的添加（水印、文本）。基本步骤是为：SDK 首先采集多路流，然后对多路流进行本地混流处理，对画面进行合并，声音进行混合，最后再进行其他效果处理。这些都依赖于浏览器本身功能的支持，因此对浏览器的性能有一定要求。具体的接口协议可以参考 [TXVideoEffectManager](https://webrtc-demo.myqcloud.com/push-sdk/v2/docs/TXVideoEffectManager.html)，下面简单介绍本地混流的基础用法。

## 基础使用
使用本地混流功能需要完成SDK的初始化并获取 SDK 实例 livePusher，初始化代码请参见 [对接攻略](https://cloud.tencent.com/document/product/267/56505#.E5.AF.B9.E6.8E.A5.E6.94.BB.E7.95.A5)。

### 步骤1：获取视频效果管理实例
```javascript
var videoEffectManager = livePusher.getVideoEffectManager();
```

### 步骤2：开启本地混流
首先需要启用本地混流功能。默认情况下 SDK 只支持采集一路视频流和一路音频流，启用之后，就可以采集多路流，这些流将在浏览器本地进行混合处理。
```javascript
videoEffectManager.enableMixing(true);
```

### 步骤3：设置混流参数
对混流参数进行设置，主要是设置最终混流后生成视频的分辨率和帧率。
```javascript
videoEffectManager.setMixingConfig({
	videoWidth: 1280,
	videoHeight: 720,
	videoFramerate: 15
});
```

### 步骤4：采集多路流
启用本地混流之后，开始采集多路流，例如先打开摄像头，再进行屏幕分享。注意保存流 ID ，后续操作都需要使用流 ID 。
```javascript
var cameraStreamId = null;
var screenStreamId = null;

livePusher.startCamera().then((streamId) => {
	cameraStreamId = streamId;
}).catch((error) => {
	console.log('打开摄像头失败：'+ error.toString());
});

livePusher.startScreenCapture().then((streamId) => {
	screenStreamId = streamId;
}).catch((error) => {
	console.log('屏幕分享失败：'+ error.toString());
});
```

### 步骤5：设置画面布局

对采集的两路画面进行布局设置。这里我们主要显示屏幕分享画面，摄像头画面出现在左上角。具体参数配置请参见 [TXLayoutConfig](https://webrtc-demo.myqcloud.com/push-sdk/v2/docs/TXVideoEffectManager.html#~TXLayoutConfig) 。
```javascript
videoEffectManager.setLayout([{
	streamId: screenStreamId,
	x: 640,
	y: 360,
	width: 1280,
	height: 720,
	zOrder: 1
}, {
	streamId: cameraStreamId,
	x: 160,
	y: 90,
	width: 320,
	height: 180,
	zOrder: 2
}]);
```

### 步骤6：设置镜像效果
摄像头采集到的画面实际上是反的，这里对摄像头画面进行一次左右翻转。
```javascript
videoEffectManager.setMirror({
	streamId: cameraStreamId,
	mirrorType: 1
});
```

### 步骤7：添加水印
先准备好一个图片对象，然后将这个图片对象作为水印添加到视频流画面中，这里把水印图片放置在右上角。
```javascript
var image = new Image();
image.src = './xxx.png'; // 图片地址注意不要跨域，否则会有跨域问题

videoEffectManager.setWatermark({
	image: image,
	x: 1230,
	y: 50,
	width: 100,
	height: 100,
	zOrder: 3
});
```

### 步骤8：开始推流
上面操作都完成后，我们最终得到了一个由画中画布局、镜像效果和水印组成的视频流，然后把处理之后的视频流推送到服务器。
```javascript
livePusher.startPush('webrtc://domain/AppName/StreamName?txSecret=xxx&txTime=xxx');
```
