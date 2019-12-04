>!以下常见问题适用于3.x.x版本的 TRTC Web SDK。

### 如何确定当前浏览器是否支持 WebRTC？
请使用 WebRTCAPI.fn.detectRTC 检测支持度，如果反馈 false，业务应提供错误提示页面引导用户使用支持的环境。遇到特殊的 case 时，也可以通过以下方式处理：
- 打开 [能力检测页面](https://www.qcloudtrtc.com/webrtc-samples/abilitytest/index.html) 进行检测。
- 通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 寻求我们的协助。

### 出现啸叫（或重音）该如何处理？
Demo （Web）中已对本地的 video/audio 设置了 muted 属性，即设置本地视频流静音播放。若不做设置，会将本地视频流的声音再次作为音频输入源，造成“啸叫”或者“重音”问题。

```html
	<video muted autoplay playsinline></video>

	<audio muted autoplay playsinline></audio>
```

>?使用两个移动端（Android 或 iOS）近距离测试时，也可能出现“啸叫”或者“重音”问题，只需将其中一端采集和播放同时静音即可。

### 音频需要很长时间才能听到，该如何处理？
如果您使用的是纯音频场景，请使用 audio 标签加载音频流，而非 video。

### Android 微信/手机 QQ 无法正常使用，该如何处理？
请使用 [检测工具](http://debugx5.qq.com/) 确认 TBS 是否安装/升级成功，若未成功，请重新安装 TBS。

### 为何会提示 on set remote sdp failed（如下图）？
![](https://main.qcloudimg.com/raw/45f5395173438ebb5894d45197828ac5.png)
webrtcapi 实例化方法中参数 closeLocalMedia 表示是否关闭自动推流，当该参数设置为 false（默认值为 false）时，如果主动调用 startWebRTC 则会引发这个问题。

### 手机的耗电量异常高，该如何排查？
视频需要进行编码/解码，而编码/解码本身是十分耗电的，如果页面并没有进行推流/观看也耗电量异常高，您可以检查是否在断流回调中未重置 video 的 srcObject。

```javascript
    videoElement.srcObject = null
```

### 出现 SecurityError［安全错误］该如何处理？
该异常表示无法正确获取音视频。
WebRTC 必须在 HTTPS 或 localhost 的页面中被打开，否则将无法获取音视频设备。

### 出现 NotAllowedError［拒绝错误］是什么意思？
该异常表示用户拒绝了获取音视频设备的请求。

### 出现 OverConstrainedError［无法满足要求错误］该如何处理？
该异常表示指定的要求无法被设备满足，是一个类型为`OverconstrainedError`的对象，拥有一个 constraint 属性，这个属性包含了当前无法被满足的 constraint 对，如果您开启了多个 Tab 页同时推流，请确保分辨率采集是一致的。

###  出现 NotFoundError［找不到错误］是什么意思？
该异常表示找不到满足请求参数的媒体类型。

###  用户已经授权，为什么还会出现 NotReadableError［无法读取错误］？
尽管用户已授权使用相应的设备，操作系统上某个硬件、浏览器或者网页层面发生的错误导致设备无法被访问。

### 为什么会出现 AbortError［中止错误］？
尽管用户和操作系统都已授权访问设备硬件，并且也没有出现`NotReadableError`这类硬件引起的问题，仍然有一些问题可能导致了设备无法被使用，从而出现 AbortError［中止错误］。

### 是什么原因引起 TypeError［类型错误］？
constraints 对象未设置，或者都被设置为 false。

### 没有声音该如何处理？
浏览器使用的是默认的声音输出设备，建议调整声音输出设备并将非功放的其他设备暂时禁用，检查是否正常。

### Electron 开发无法进行视频通话该如何处理？
如果您使用的是 Electron，在提交 Mac App Store 后无法正常进行视频通话，请在 entitlements.plist 文件中加上`com.apple.securite.network.server` 。

### 如何避免 dom tree 重绘引起的黑屏问题？
如果您使用 react/vue/angular，video 与 stream 的关系是通过 js 来控制的。如果数据变化引起了页面的变化，您需要重新绑定 video 与 stream 的关系，否则会引发黑屏问题。

### iOS 黑屏是什么原因？
- 如果您使用的是 react/vue/angular，动态创建的 video 无法在浏览器中自动播放。
- 如果您使用了纯观众模式，不进行推流，iOS 不允许自动播放带声音的视频，远端视频流无法自动播放。需要在 onRemoteStreamUpdate 事件处理函数中，将远端流绑定到 video 标签后，加上 video.play()。


### 为什么关闭麦克风/静音了还有数据包？
关闭麦克风或静音后仍会有静音包。

### 为什么关闭摄像头了还有数据包？
关闭摄像头后仍会有黑屏包。

