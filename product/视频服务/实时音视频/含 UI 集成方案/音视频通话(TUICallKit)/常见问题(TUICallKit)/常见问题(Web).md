## 一、基础环境问题

### Web 端 SDK 支持哪些浏览器？
TRTC Web SDK 对浏览器的详细支持度，请参见 [TRTC Web SDK 对浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)。
对于上述没有列出的环境，您可以在当前浏览器打开 [TRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 测试是否完整的支持 WebRTC 的功能。

### 如何实时检测当前网络的情况？
具体请参见 [通话前的网络质量检测](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-24-advanced-network-quality.html)。

### 为什么本地开发测试能正常使用，但是部署到线上用 IP 访问后无法正常视频/语音通话？

出于对用户安全、隐私等问题的考虑，浏览器限制网页只有在安全的环境下（例如 `https`、 `localhost`、`file://` 等协议），才能采集麦克风、摄像头。HTTP 协议是不安全的，浏览器会禁止在 HTTP 协议下采集媒体设备。

若您在本地开发测试一切正常，但是页面部署后，却无法正常采集摄像头、麦克风。则请检查您的网页是否部署到了 HTTP 协议上，若是，请使用 HTTPS 部署您的网页，并确保具备合格的 HTTPS 安全证书。

更多详情请参见 [URL域名及协议限制说明](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html#h2-2)。

### 在接通过程中报：“is not included in the current tim\'s package”？
-  **原因**：
   -  您所下载TIM的依赖包版本过低；
   -  您的TIM依赖包版本正确，则可能是 SDKAppID 未购买音视频套餐或套餐包不支持所调用的功能。
- **解决方案**：
  - 升级TIM包版本到>=2.21.2；
  - 购买支持音视频套餐的 SDKAppID。

## 二、集成问题

### tuiCallEngine.handup() 报错：“uncaught (in promise) TypeError: cannot read property 'stop' of null”？
- **原因**：用户在监听事件中多次调用 handup()，导致 hangup 未执行完成又一次触发。
- **解决方案**：handup() 只需要执行一次，监听事件的后续操作，TRTCCalling 内部已进行处理，不需要再执行 hangup() 方法，只需做自己业务相关操作即可。

### 在接通过程中报：“TypeError: Cannot read property 'getVideoTracks' of null”？

- **原因**：用户在接受时，还没有获取使用用户视频和麦克风到权限导致的。
- **解决方案**：在使用 startRemoteView、startLocalView 等操作设备方法时，建议使用异步方法。升级 TRTCCaling 版本至最新版本。

### sdkAppid 用 script 方式引入时报：“TSignaling._onMessageReceived unknown bussinessID=undefined”?
- **详情**：同一个 sdkAppid用 script 方式引入的，与 script 引入的能互通，与 npm 引入的或 Android/iOS 的不能互通，且返回警告信息：`TSignaling._onMessageReceived unknown bussinessID=undefined`。
- **原因**：`bussinessId=undefined` 表示该版本 tsignaling 版本为旧版本，旧版本信令有问题。
- **解决方案**：升级 tsignaling 版本，且在引入过程中需注意**新版本 tsignaling 的文件名称为 `tsignaling-js`**。

### 提醒：“Uncaught ( in promise ) RTCError: duplicated play() call observed, please stop() firstly &lt;INVALID_OPERATION 0x1001&gt;”？
- **原因**：在语音通过过程中，调用 startRemoteView 接口。
- **解决方案**：在语音通话过程中，取消 startRemoteView 操作。

### Error: tuiCallEngine.call - 获取用户设备权限失败？

- **原因**：TRTCCalling 没有设备权限或者没有对于设备。
- **解决方案**：
	- 使用 [TRTC 设备检测](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 进行检查。
	- 访问 **Chrome 的网站设置**（chrome://settings/content） 查看使用 TRTCCalling 的网站是否开启摄像头/麦克风权限。

### TUICallEngine web 是否支持接收离线消息？

- 不支持接收离线消息。
- 支持离线消息推送，可以通过 call / groupCall 中的 [offlinePushInfo]() 添加需要推送的消息。

### Error: TRTCClient.getMediaDevicesAuth - failed to get user video steam - NotReadableError: Could not start video source？

- **原因**：系统没有给浏览器开启摄像头权限。
- **解决方案**：在系统设置中找到相机（Windows）/ 摄像头（Mac），开启对应浏览器的权限。
