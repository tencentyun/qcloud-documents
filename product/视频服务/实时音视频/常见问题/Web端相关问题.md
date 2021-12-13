## 一、基础环境问题
[](id:b1)
### Web 端 SDK 支持哪些浏览器？
TRTC Web SDK 对浏览器的详细支持度，请参见 [TRTC Web SDK 对浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)。
对于上述没有列出的环境，您可以在当前浏览器打开 [TRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 测试是否完整的支持 WebRTC 的功能。

[](id:b2)
### 通话前音视频设备测试？
您可以查看 [通话前环境与设备检测](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-23-advanced-support-detection.html)。

[](id:b3)
### 如何实时检测当前网络的情况？
具体请参见 [通话前的网络质量检测](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-24-advanced-network-quality.html)。

[](id:b4)
### 为什么本地开发测试能正常使用 TRTC Web SDK，但是部署到线上无法使用？

出于对用户安全、隐私等问题的考虑，浏览器限制网页只有在安全的环境下（例如 `https`、 `localhost`、`file://` 等协议），才能采集麦克风、摄像头。HTTP 协议是不安全的，浏览器会禁止在 HTTP 协议下采集媒体设备。

若您在本地开发测试一切正常，但是页面部署后，却无法正常采集摄像头、麦克风。则请检查您的网页是否部署到了 HTTP 协议上，若是，请使用 HTTPS 部署您的网页，并确保具备合格的 HTTPS 安全证书。

更多详情请参见 [URL域名及协议限制说明](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html#h2-2)。

[](id:b5)
### 是否支持混流、旁路推流、大小流、美颜、水印？
您可请参见 [混流](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#startMixTranscode)、[旁路推流](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-26-advanced-publish-cdn-stream.html)、[大小流](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-27-advanced-small-stream.html)、[美颜](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-28-advanced-beauty.html) 、[水印](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-29-advance-water-mark.html)文档实现高级功能。

[](id:b6)
### WebRTC 有哪些已知问题？
具体请参见 [WebRTC 已知问题及规避方案](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-02-info-webrtc-issues.html)。

## 二、推拉流问题
[](id:p1)
### Web 端 SDK 日志中报错 NotFoundError、NotAllowedError、NotReadableError、OverConstrainedError 以及 AbortError 分别是什么意思？
| 错误名 | 描述 | 处理建议 |
| -------------------- | -------------------- | -------------------- |
| NotFoundError | 找不到满足请求参数的媒体类型（包括音频、视频、屏幕分享）。 例如：PC 没有摄像头，但是请求浏览器获取视频流，则会报此错误。 | 建议在通话开始前引导用户检查通话所需的摄像头或麦克风等设备，若没有摄像头且需要进行语音通话，可在 [TRTC.createStream({ audio: true, video: false })](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.createStream) 指明仅采集麦克风。 |
| NotAllowedError | 用户拒绝了当前的浏览器实例的访问音频、视频、屏幕分享请求。   | 提示用户不授权摄像头/麦克风访问将无法进行音视频通话。        |
| NotReadableError | 用户已授权使用相应的设备，但由于操作系统上某个硬件、浏览器或者网页层面发生的错误导致设备无法被访问。 | 根据浏览器的报错信息处理，并提示用户“暂时无法访问摄像头/麦克风，请确保当前没有其他应用请求访问摄像头/麦克风，并重试”。 |
| OverConstrainedError | cameraId/microphoneId 参数的值无效。 | 请确保 cameraId/microphoneId 传值正确且有效。 |
| AbortError | 由于某些未知原因导致设备无法被使用。 | - |

更多详情请参见 [initialize](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html?#initialize)。

[](id:p2)
### 部分手机上的浏览器无法正常运行 TRTC 进行推拉流？
TRTC Web SDK 对浏览器的详细支持度，请参见 [TRTC Web SDK 对浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)。
对于上述没有列出的环境，您可以在当前浏览器打开 [TRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 测试是否完整的支持 WebRTC 的功能。

[](id:p3)
### Web 端用宽高设置推流的分辨率是所有浏览器都适用吗？
由于设备和浏览器的限制，视频分辨率不一定能够完全匹配，在这种情况下，浏览器会自动调整分辨率使其接近 Profile 对应的分辨率。详情请参见 [setVideoProfile](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html?#setVideoProfile)。

[](id:p4)
### Web 端屏幕分享的样式支持修改吗？
屏幕分享的样式由浏览器控制，目前不能修改。

[](id:p5)
### Web 端支持混流吗？
Web 端支持发起混流，具体请参见 [如何调用混流转码接口](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#startMixTranscode)。

[](id:p6)
### Web 端 SDK 在使用的过程中拔掉摄像头，怎么清除摄像头列表里面的数据？
可以尝试调用 [TRTC.getCameras](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.getCameras) 方法是否能获取新的设备列表，如果仍然有拔掉的摄像头信息，说明浏览器底层也没有刷新这个列表，Web 端 SDK 也获取不到新的设备列表信息。

[](id:p7)
### iOS 的微信内嵌浏览器不能正常推流？
请参见 [浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)，查看 iOS 上的微信内嵌浏览器对推拉流的支持情况。

## 三、播放问题
[](id:v1)
### 音视频互通过程中出现有画面没有声音问题？
- 因浏览器自动播放策略限制，音频播放会出现 PLAY_NOT_ALLOWED 异常，此时业务层需要引 导用户手动操作 Stream.resume() 来恢复音频播放，具体请参见 [自动播放受限处理建议](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-21-advanced-auto-play-policy.html)。
- 未知异常导致，请通过监控仪表盘查询收发两端的 audioLevel & audioEnergy。

[](id:v2)
### Web 通话画面显示不了?
检查一下 Web 页面上是否有获取到数据，在确认数据收发正常时，可以检查 `<video>` 元素的 srcObject 属性是否赋值了正确的 mediaStream 对象，如果赋值错误，肯定显示不了。

[](id:v3)
### Web 通话过程中出现回声、杂音、噪声、声音小？
通话双方的设备相距太近的时候，属于正常现象，测试时请相互距离远一点。当其他端听到 Web 端的声音存在回声、噪声、杂音等情况时，说明 Web 端的 3A 处理没有生效。
若您使用了浏览器原生 [getUserMedia](https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices/getUserMedia) API 进行自定义采集，则需要手动设置 3A 参数：
- echoCancellation：回声消除开关
- noiseSuppression：噪声抑制开关
- autoGainControl：自动增益开关，详细设置请参见 [媒体追踪约束](https://developer.mozilla.org/zh-CN/docs/Web/API/MediaTrackConstraints)。

若您使用 [TRTC.createStream](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#createStream) 接口进行采集，则无需手动设置 3A 参数，SDK 默认开启 3A。

## 四、其他
[](id:o0)
### 2.x、3.x 版本的 SDK，在 Chrome 96+ 版本无法正常通话该如何处理？
最新版本的 [Chrome 96 废弃了 Plan-B](https://www.chromestatus.com/feature/5823036655665152)，将会导致 TRTC 实时音视频老版本的(2.x，3.x ) Web SDK 会出现无法通话的情况，请您尽快将 Web SDK 升级至我们的最新版本。4.x 版本SDK 的接口与老版本(2.x, 3.x)不兼容，请参考 [快速集成(Web)](https://cloud.tencent.com/document/product/647/16863) 升级接入 4.x 版本 SDK。

[](id:o1)
###  运行 Web 端 SDK 时，出现错误：“RtcError: no valid ice candidate found”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在 STUN 打洞失败，请检查防火墙配置。TRTC 桌面浏览器 SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/basic-rtc.html) 检查配置是否生效。

具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)。

[](id:o2)
###  出现客户端错误："RtcError: ICE/DTLS Transport connection failed" 或 “RtcError: DTLS Transport connection timeout”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在建立媒体传输通道时失败，请检查防火墙配置。TRTC 桌面浏览器 SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/basic-rtc.html) 检查配置是否生效。

具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)。


[](id:o3)
### Web 端 SDK 可以获取当前音量大小吗？
可以通过 [getAudioLevel](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html#getAudioLevel) 获取当前音量大小，具体请参见 [切换摄像头和麦克风](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-13-basic-switch-camera-mic.html) 。

[](id:o4)
### 什么情况会触发 Client.on(‘client-banned’)？

当用户被踢时会触发该事件，例如：使用同名用户同时登录、调用后台 RESTAPI [移除用户](https://cloud.tencent.com/document/product/647/40496?from=10680) 将用户踢出房间。
>! 同名用户同时登录是不允许的行为，可能会导致双方通话异常，业务层应避免出现同名用户同时登录。

更多具体详情，请参见 [CLIENT_BANNED 事件](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-ClientEvent.html#.CLIENT_BANNED)。

[](id:o5)
### Web 端是否可以监听远端离开房间？
支持监听远端退房事件，建议使用客户端事件中的 [client.on('peer-leave')](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-Event.html) 事件实现远端用户退房通知。

[](id:o6)
### TRTC 的 Web 端、小程序端、PC 端是不是互通的？
是的，实时音视频支持全平台互通。

[](id:o7)
### TRTC Web 端的截图功能如何实现？
具体请参见 [Stream.getVideoFrame()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Stream.html#getVideoFrame) 接口。

[](id:o8)
### Web 端 SDK 怎么录制纯音频推流？为什么在控制台开启自动旁路和自动录制录制不成功呢？
需要设置 [createClient](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.createClient) 的 pureAudioPushMode 参数。

[](id:o9)
### 出现 Client.on(‘error’) 问题该如何处理？
这个表示 SDK 遇到不可恢复错误，业务层要么刷新页面重试要么调用 Client.leave 退房后再调用 Client.join 重试。

[](id:o10)
### 小程序和 Web 端支持自定义流 ID 吗？
Web 端4.3.8以上版本已支持自定义流 ID，可以更新 SDK 版本。小程序当前暂不支持。

[](id:011)
### Web 端如何在屏幕分享的时候采集系统声音？
具体操作请参见 [屏幕分享采集系统声音](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-16-basic-screencast.html#h2-6)。
目前采集系统声音只支持 Chrome M74+ ，在 Windows 和 Chrome OS 上，可以捕获整个系统的音频，在 Linux 和 Mac 上，只能捕获选项卡的音频。其它 Chrome 版本、其它系统、其它浏览器均不支持。

[](id:012)
### Web 端如何切换摄像头和麦克风？
您可以先获取到系统的摄像头和麦克风设备后，调用 [switchDevice](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html#switchDevice) 来进行切换，具体操作请参见 [切换摄像头和麦克风](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-13-basic-switch-camera-mic.html)。
