本文主要介绍如何快速地将腾讯云视立方集成到您的项目中，按照如下步骤进行配置，就可以完成腾讯云视立方 SDK 在 Web 端的集成工作，主要包含 Web 播放器和 WebRTC 的集成方式。

## Web 播放器集成方式

腾讯云 Web 播放器是为了解决在手机浏览器和 PC 浏览器上播放音视频流的问题，它使您的视频内容可以不依赖用户安装 App，就能在朋友圈和微博等社交平台进行传播。

- 如果您需要在 Web 端进行直播播放，可使用Web超级播放器 TCPlayerLite，集成方式参见 [Web 超级播放器 TCPlayerLite](https://cloud.tencent.com/document/product/1449/57070)。
- 如果您需要在 Web 端进行点播播放，可使用Web超级播放器 TCPlayer，集成方式参见 [Web 超级播放器 TCPlayer](https://cloud.tencent.com/document/product/1449/57088)。
- 如果您需要快速实现第三方 Web 播放器与云点播能力的结合，可使用 Web 超级播放器 Adapter，集成方式参见 [Web 超级播放器 Adapter](https://cloud.tencent.com/document/product/1449/57089)。

## WebRTC 集成方式

### 支持的平台

WebRTC 技术由 Google 最先提出，目前主要在桌面版 Chrome 浏览器、桌面版 Edge 浏览器、桌面版 Firefox 浏览器、桌面版 Safari 浏览器以及移动版的 Safari 浏览器上有较为完整的支持，其他平台（例如 Android 平台的浏览器）支持情况均比较差。
- 在移动端推荐使用 [小程序](https://cloud.tencent.com/document/product/1449/56990) 解决方案，微信和手机 QQ 小程序均已支持，都是由各平台的 Native 技术实现，音视频性能更好，且针对主流手机品牌进行了定向适配。
- 如果您的应用场景主要为教育场景，那么教师端推荐使用稳定性更好的 [Electron](https://cloud.tencent.com/document/product/1449/58915) 解决方案，支持大小双路画面，更灵活的屏幕分享方案以及更强大的弱网络恢复能力。

腾讯云 TRTC 桌面浏览器 SDK 详细支持度表格请参见 [支持的平台](https://cloud.tencent.com/document/product/1449/57192#.E6.94.AF.E6.8C.81.E7.9A.84.E5.B9.B3.E5.8F.B0)。
> ! 
> - 您可以在浏览器中打开 [WebRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 页面进行检测是否完整支持 WebRTC。例如公众号等浏览器环境。
> - 由于 H.264 版权限制，华为系统的 Chrome 浏览器和以 Chrome WebView 为内核的浏览器均不支持 TRTC 桌面浏览器 SDK 的正常运行。


### 防火墙限制
TRTC 桌面浏览器 SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单。
- TCP 端口：8687
- UDP 端口：8000，8080，8800，843，443，16285
- 域名：qcloud.rtc.qq.com

### 集成桌面浏览器 SDK

- **NPM 集成**：
	1. 您需要在项目中使用 npm 安装 SDK 包。
```
npm install trtc-js-sdk --save
```
	2. 在项目脚本里引入模块。
```javascript
import TRTC from 'trtc-js-sdk';
```
- **Script 集成**：
您只需要在您的 Web 页面中添加如下代码即可：
```html
<script src="trtc.js"></script>
```

## 相关资源

SDK 下载地址：[单击下载](https://web.sdk.qcloud.com/trtc/webrtc/download/webrtc_latest.zip)。

更详细的初始化流程和 API 使用介绍请参见以下指引：

| 功能                       | Sample Code 指引                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 基础音视频通话             | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-11-basic-video-call.html)                      |
| 互动直播                   | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-12-basic-live-video.html)                            |
| 切换摄像头和麦克风         | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-13-basic-switch-camera-mic.html)            |
| 设置本地视频属性           | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-14-basic-set-video-profile.html)            |
| 动态关闭打开本地音频或视频 | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-15-basic-dynamic-add-video.html)            |
| 屏幕分享                   | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-16-basic-screencast.html)                   |
| 音量大小检测               | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-17-basic-detect-volume.html)                |
| 自定义采集与自定义播放渲染 | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-20-advanced-customized-capture-rendering.html) |
| 房间内上行用户个数限制     | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-04-info-uplink-limits.html)                |
| 背景音乐和音效实现方案     | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-22-advanced-audio-mixer.html)                  |

