### 问题排查步骤建议

- 确定错误码排查问题


### 如何确定是否当前浏览器是否支持 WebRTC
请使用 WebRTCAPI.fn.detectRTC 检测支持度，如果反馈false，业务应提供错误提示页面引导用户使用支持的环境。遇到特殊的 case 时，也可以通过
- 打开 [能力检测页面](https://www.qcloudtrtc.com/webrtc-samples/abilitytest/index.html) 进行检测。
- 通过创建工单寻求我们的协助。

### 啸叫（或重音）
特别注意，我们的demo中，对本地的video/audio，是有设置一个 muted 属性的，这里的意思是指将本地视频流播放时静音，否则，就会出现本地视频流的声音又一次作为音频输入源的循环中，造成我们常说的“啸叫”或者“重音”问题。

```html
	<video muted autoplay playsinline></video>

	<audio muted autoplay playsinline></audio>
```


### 音频需要很长时间才能听到
如果您使用的是纯音频场景，请特别注意，使用 audio 标签来加载音频流，而不是使用video。


### Android 微信/手Q 也无法正常使用
有极少的情况会引起TBS没有安装/升级成功，可以打开这个网址进行检测 http://debugx5.qq.com/ 。

### on set remote sdp failed （如下图）
![](https://main.qcloudimg.com/raw/45f5395173438ebb5894d45197828ac5.png)
webrtcapi 实例化方法中有一个参数是closeLocalMedia
表示是否关闭自动推流，如果设置为false了（默认也是false），又去主动调用 startWebRTC，就会引发这个问题

### 手机的耗电问题
因为视频需要进行编解码，而编解码本身是很耗电的; 但是如果页面并没有进行推流/观看也耗电很快，您必须检查一下，是否在断流回调中，没有重置video的srcObject。

```javascript
    videoElement.srcObject = null
```

### SecurityError［安全错误］
无法正确获取音视频视频。
WebRTC 必须在 HTTPS 或 localhost 中的页面中被打开，否则无法获取音视频设备。

### NotAllowedError［拒绝错误］
用户拒绝了获取音视频设备的请求

### OverConstrainedError［无法满足要求错误］
指定的要求无法被设备满足，此异常是一个类型为`OverconstrainedError`的对象，拥有一个 constraint 属性，这个属性包含了当前无法被满足的 constraint 对，如果您开启了多个 Tab 页同时推流，请确定分辨率采集是一致的。

###  NotFoundError［找不到错误］
找不到满足请求参数的媒体类型。

###  NotReadableError［无法读取错误］
尽管用户已经授权使用相应的设备，操作系统上某个硬件、浏览器或者网页层面发生的错误导致设备无法被访问。

### AbortError［中止错误］
尽管用户和操作系统都授予了访问设备硬件的权利，并且也没有出现`NotReadableError`这类硬件引起的问题，但仍然有一些问题的出现导致了设备无法被使用。

### TypeError［类型错误］
constraints 对象未设置，或者都被设置为 false。

### 没有声音
浏览器使用的是默认的声音输出设备，调整声音输出设备，并将非功放的其他设备暂时禁用，确定是否 ok。


### Electron开发无法进行视频通话
如果您使用的是 Electron，在提交 Mac App Store 后无法正常进行视频通话，请在 entitlements.plist 文件中加上 `com.apple.securite.network.server` 。

### 小心 dom tree 重绘引起的黑屏问题
如果您使用的是 react/vue/angular，特别注意，video与stream 的关系，是通过 js 来控制的。如果数据变化引起了页面的变化，您需要重新绑定 video 与 stream 的关系，否则就会引发黑屏问题。

### iOS 黑屏？
- 如果您使用的是 react/vue/angular，特别注意，动态创建的 video 会在浏览器中无法自动播放。
- 如果您使用了纯观众模式，不进行推流，特别注意，iOS不允许自动播放带声音的视频，远端视频流无法自动播放。需要在onRemoteStreamUpdate事件处理函数中，将远端流绑定到video标签后，加上video.play()。


### 为什么关闭麦克风/静音了还有数据包
静音包。

### 为什么关闭摄像头了还有数据包
黑屏包。

