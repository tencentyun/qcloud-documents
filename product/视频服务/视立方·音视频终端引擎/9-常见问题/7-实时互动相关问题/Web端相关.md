[](id:que1)

###  Web 端 SDK 支持哪些浏览器？ 

目前主要在桌面版 Chrome 浏览器、桌面版 Edge 浏览器、桌面版 Firefox 浏览器、桌面版 Safari 浏览器以及移动版的 Safari 浏览器上有较为完整的支持，其他平台（例如 Android 平台的浏览器）支持情况均比较差，具体详情请参见 [支持的平台](https://cloud.tencent.com/document/product/647/17249#.E6.94.AF.E6.8C.81.E7.9A.84.E5.B9.B3.E5.8F.B0)。
您可以在浏览器打开 [WEBRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 测试是否完整的支持 WebRTC 的功能。

[](id:que2)

###  音视频通话 TRTC 的 Web 端、小程序端、PC 端是不是同步的？

是的，音视频通话 TRTC 支持全平台互通。

[](id:que3)

###  TRTC Native SDK 有云端混流接口，Web 端和小程序端怎么实现云端混流？

Web 端和小程序端目前没有客户端接口，可以直接调用云直播的 [CreateCommonMixStream](https://cloud.tencent.com/document/api/267/43404) 接口实现混流。

[](id:que4)

###  运行 Web 端 SDK 时，出现错误：“RtcError: no valid ice candidate found”该如何处理？

出现该错误说明 TRTC Web SDK 在 STUN 打洞失败，请检查防火墙配置。TRTC Web SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/latest/official-demo/index.html) 检查配置是否生效。

 - TCP 端口：8687
 - UDP 端口：8000，8080，8800，843，443，16285
 - 域名：qcloud.rtc.qq.com

[](id:que5)

###  出现客户端错误："RtcError: ICE/DTLS Transport connection failed" 或 “RtcError: DTLS Transport connection timeout”该如何处理？

出现该错误说明 TRTC Web SDK 在建立媒体传输通道时失败，请检查防火墙配置。TRTC Web SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/latest/official-demo/index.html) 检查配置是否生效。

 - TCP 端口：8687
 - UDP 端口：8000，8080，8800，843，443，16285
 - 域名：qcloud.rtc.qq.com


[](id:que6)

###  音视频通话 TRTC  Web 端的截图功能如何实现？

参考 [Stream.getVideoFrame()](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Stream.html#getVideoFrame) 接口。

[](id:que7)

###  Web 端 SDK 日志中报错 NotFoundError、NotAllowedError、NotReadableError、OverConstrainedError 以及 AbortError 分别是什么意思？


| 错误名               | 描述                                                         | 处理建议                                                     |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| NotFoundError        | 找不到满足请求参数的媒体类型（包括音频、视频、屏幕分享）。<br>例如：PC 没有摄像头，但是请求浏览器获取视频流，则会报此错误。 | 建议在通话开始前引导用户检查通话所需的摄像头或麦克风等设备，若没有摄像头且需要进行语音通话，可在 [TRTC.createStream({ audio: true, video: false })](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.createStream) 指明仅采集麦克风。 |
| NotAllowedError      | 用户拒绝了当前的浏览器实例的访问音频、视频、屏幕分享请求。   | 提示用户不授权摄像头/麦克风访问将无法进行音视频通话。        |
| NotReadableError     | 用户已授权使用相应的设备，但由于操作系统上某个硬件、浏览器或者网页层面发生的错误导致设备无法被访问。 | 根据浏览器的报错信息处理，并提示用户“暂时无法访问摄像头/麦克风，请确保当前没有其他应用请求访问摄像头/麦克风，并重试”。 |
| OverConstrainedError | cameraId/microphoneId 参数的值无效。                         | 请确保 cameraId/microphoneId 传值正确且有效。                |
| AbortError           | 由于某些未知原因导致设备无法被使用。                         | -                                                            |


更多详情请参见 [initialize](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html?#initialize)。


[](id:que8)

###  Web 端 SDK 是否支持类似 enableSmallVideoStream 大小画面双路编码模式？ 

目前暂时不支持。

[](id:que9)

###  Web 端 SDK 在使用的过程中拔掉摄像头，怎么清除摄像头列表里面的数据？

可以尝试调用 [getCameras](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.getCameras) 方法是否能获取新的设备列表，如果仍然有拔掉的摄像头信息，说明浏览器底层也没有刷新这个列表，Web 端 SDK 也获取不到新的设备列表信息。

[](id:que10)

###  Web 端 SDK 怎么录制纯音频推流？为什么在控制台开启自动旁路和自动录制录制不成功呢？ 

需要设置 [createClient](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/TRTC.html#.createClient) 的 pureAudioPushMode 参数。

[](id:que11)

###  Web 端 SDK 可以获取当前音量大小吗？

可以通过 [getAudioLevel](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html#getAudioLevel) 获取当前音量大小。

[](id:que12)

###  Web 端屏幕分享弹框的样式可以更改吗？  

Web 端屏幕分享弹框的样式是由浏览器控制的，Web 页面无法更改。

[](id:que13)

###  Web 端用宽高设置推流的分辨率是所有浏览器都适用吗？

由于设备和浏览器的限制，视频分辨率不一定能够完全匹配，在这种情况下，浏览器会自动调整分辨率使其接近 Profile 对应的分辨率。详情请参见 [setVideoProfile](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/LocalStream.html?#setVideoProfile)。

[](id:que14)

###  怎么确认 Web 端 SDK 是否能正常获取到设备（摄像头/麦克风）列表？

1. 检查浏览器是否能够正常使用设备：
   直接在页面打开控制台，输入 `navigator.mediaDevices.enumerateDevices()` 确认能否获取到设备列表。

 - 如果正常获取到设备会返回一个 Promise，里面会有 MediaDeviceInfo 对象数组，数组里的每个对象对应一个可用的媒体设备。
 - 如果枚举失败，Promise 将返回 rejected，说明浏览器都没有识别到设备，需检查浏览器或设备。

2. 如果能获取设备列表，则输入 `navigator.mediaDevices.getUserMedia({ audio: true, video: true })` 确认能否正常返回 MediaStream 对象，不能正常返回说明浏览器没有获取到数据，需检查浏览器的配置。

[](id:que15)

###  Web 端的回声噪声问题怎么处理？

当其他端听到 Web 端的声音存在回声、噪声、杂音等情况时，说明 Web 端的 3A 处理没有生效。

- 若您使用了浏览器原生 [getUserMedia](https://developer.mozilla.org/zh-CN/docs/Web/API/MediaDevices/getUserMedia) API 进行自定义采集，则需要手动设置 3A 参数：
  - echoCancellation：回声消除开关
  - noiseSuppression：噪声抑制开关
  - autoGainControl：自动增益开关

>? 详细设置参考 [媒体追踪约束](https://developer.mozilla.org/zh-CN/docs/Web/API/MediaTrackConstraints)。

- 若您使用 TRTC.createStream 接口进行采集，则无需手动设置 3A 参数，SDK 默认开启 3A。


[](id:que16)

### Web 端是否可以监听远端离开房间？

支持监听远端退房事件，建议使用客户端事件中的 [client.on('peer-leave')](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/module-Event.html) 事件实现远端用户退房通知。

