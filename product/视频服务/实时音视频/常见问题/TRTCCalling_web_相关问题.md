[](id:base)
## 基础问题

[](id:b1)
### 什么 TRTCCalling？
TRTCCalling 是在 TRTC 和 TIM 的基础上诞生的一款快速集成的音视频的解决方案。支持1v1和多人视频/语音通话。
![](https://main.qcloudimg.com/raw/db70b140c138ba8c4aff32f679332ac3.png)      

[](id:b2)
### TRTCCalling 是否支持接受 roomID 为字符串?
roomID 可以 string，但只限于数字字符串。


[](id:environment)
## 环境问题

[](id:e1)
### Web 端 SDK 支持哪些浏览器？
TRTC Web SDK 对浏览器的详细支持度，请参见 [TRTC Web SDK 对浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)。
对于上述没有列出的环境，您可以在当前浏览器打开 [TRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 测试是否完整的支持 WebRTC 的功能。

[](id:e2)
### 如何实时检测当前网络的情况？
具体操作请参见 [通话前的网络质量检测](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-24-advanced-network-quality.html)。

[](id:e3)
### IM H5 Demo 项目本地跑通功能正常，但放在服务器上用 IP 访问后无法正常视频/语音通话?

- **背景**：IM 的 H5 Demo 在本地跑通后，使用 localhost 能正常实现消息发送、视频/语音通话功能。将项目放到服务器上用 IP 访问后，文字消息收发、控制台请求返回正常且控制台没有任何错误，但无法正常运行语音/视频通话，获取不到视频图像。
- **原因**：IM 中语音/通话视频使用的是 TRTCCalling SDK，用户使用 IP 访问时，使用的是 HTTP 协议。
- **解决方案**：TRTCCalling SDK 需在 HTTPS 或 localhost 环境下运行。


[](id:integrated)
## 集成问题

[](id:i1)
### calling 线上 Demo 无法进入 NO_RESP？
- **原因**：NO_RESP 事件触发条件：1-邀请者超时，2-被邀请者不在线。
- **解决方案**：请根据触发条件进行事件处理。

[](id:i2)
### calling 在 iPhone 微信的浏览器打开无法听到对方的声音？
- 原因：自动播放受限。
- 解决方案：calling 在1.0.0版本时，进行了处理。建议您升级 calling 至1.0.0及之后的版本。

[](id:i3)
### TRTCCalling handup() 报错：“uncaught (in promise) TypeError: cannot read property 'stop' of null”？
- **原因**：用户在监听事件中多次调用 handup()，导致 hangup 未执行完成又一次触发。
- **解决方案**：handup() 只需要执行一次，监听事件的后续操作，TRTCCalling 内部已进行处理，不需要再执行 hangup() 方法，只需做自己业务相关操作即可。

[](id:i3)
### 最新版本90的 Chrome 浏览器，trtccalling.js 提示：“不支持，TRTCClinet.您的浏览器不兼容此应用”？
- **原因**：IM 版本过低，检测机制有所缺失。
- **解决方案**：建议升级 IM 版本。

[](id:4)
### 在接通过程中报：“TypeError: Cannot read property 'getVideoTracks' of null”？

- **原因**：用户在接受时，还没有获取使用用户视频和麦克风到权限导致的。
- **解决方案**：在使用 startRemoteView、startLocalView 等操作设备方法时，建议使用异步方法。或者升级 TRTCCaling 版本至1.0.0。

[](id:i5)
### sdkAppid 用 script 方式引入时报：“TSignaling._onMessageReceived unknown bussinessID=undefined”?
- **详情**：同一个 sdkAppid用 script 方式引入的，与 script 引入的能互通，与 npm 引入的或 Android/iOS 的不能互通，且返回警告信息：`TSignaling._onMessageReceived unknown bussinessID=undefined`。
- **原因**：`bussinessId=undefined` 表示该版本 tsignaling 版本为旧版本，旧版本信令有问题。
- **解决方案**：升级 tsignaling 版本，且在引入过程中需注意**新版本 tsignaling 的文件名称为 `tsignaling-js`**。


[](id:i6)
### 提醒：“Uncaught ( in promise ) Error: createCustomMessage 接口需要 SDK 处于 ready 状态后才能调用”？

- **原因**：未按正确步骤完成初始化。
- **解决方案**：升级 TRTCCalling 版本至1.0.0，监听 SDK_READY 事件进行后续操作。


[](id:i7)
### 提醒：“Uncaught ( in promise ) RTCError: duplicated play() call observed, please stop() firstly &lt;INVALID_OPERATION 0x1001&gt;”？
- **原因**：在语音通过过程中，调用 startRemoteView 接口。
- **解决方案**：在语音通话过程中，取消 startRemoteView 操作。

[](id:i8)
### 提醒：“Uncaught ( in promise ) Error: inviteID is invalid or invitation has been processed”？
- **详情**：Web 端 trtccalling 与 native 端互通，web 呼叫 native 后，native 接听而 web 端摄像头还未开启，本地预览还没有画面就点挂断，native 还在通话页面。返回错误信息：`Uncaught ( in promise ) Error: inviteID is invalid or invitation has been processed`。
- **原因**：在获取用户设备时，若用户未授权音视频设备，可以进入音视频通话房间，但挂断时，native无法收到挂断信令。
- **解决方案**：calling 的1.0.0版本，进行前置获取并获取不成功时，不允许用户进入通话。建议您升级 calling 至1.0.0及之后的版本。

[](id:i9)
### 主叫呼叫成功后，被叫打印了日志（应该收到了呼叫），但没有走回调 handleNewInvitationReceived 回调？

- **原因**：TRTCCalling <= 0.6.0 和 Tsignaling <= 0.3.0 版本过低。
- **解决方案**：升级 TRTCCalling 和 Tsignaling 到最新版本。

[](id:i10)
### TRTCCalling 在 CALL 之后 主动 reject 后 无法在呼叫?

- **原因**：call之后主动 reject 后，calling 状态没重置导致。
- **解决方案**：升级 TRTCCalling 版本>=1.0.3。

[](id:i11)
### Error: TRTCCalling.call - 获取用户设备权限失败？

- **原因**：TRTCCalling 没有设备权限或者没有对于设备。
- **解决方案**：
	- 使用 [TRTC设备检测](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 进行检查。
	- 访问 [网站设置](chrome://settings/content) 查看使用 TRTCCalling 的网站是否开启摄像头/麦克风权限。
