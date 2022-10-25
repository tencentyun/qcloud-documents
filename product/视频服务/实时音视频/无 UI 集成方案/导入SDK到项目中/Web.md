本文主要介绍如何快速地将腾讯云 TRTC Web SDK 集成到您的项目中。
## 准备工作
集成 TRTC Web SDK 之前需要了解的事项。

### 支持的平台
TRTC Web SDK 基于 WebRTC 实现，目前支持桌面端和移动端的主流浏览器，详细支持度表格请参见 [支持的平台](https://cloud.tencent.com/document/product/647/17249#.E6.94.AF.E6.8C.81.E7.9A.84.E5.B9.B3.E5.8F.B0)。
如果您的应用场景不在支持的表格里，可以打开 [TRTC Web SDK 能力检测页面](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 检测当前环境是否支持 WebRTC 所有能力，例如 WebView 等环境。

### URL 域名协议限制
由于浏览器安全策略的限制，使用 WebRTC 能力对页面的访问协议有严格的要求，请参照以下表格进行开发和部署应用。

| 应用场景     | 协议             | 接收（播放） | 发送（上麦） | 屏幕分享 | 备注     |
|----------|:-----------------|:---------|----------|--------|----------|
| 生产环境     | HTTPS 协议       | 支持       | 支持       | 支持     | **推荐** |
| 生产环境     | HTTP 协议        | 支持       | 不支持     | 不支持   |          |
| 本地开发环境 | http://localhost | 支持       | 支持       | 支持     | **推荐** |
| 本地开发环境 | http://127.0.0.1 | 支持       | 支持       | 支持     |          |
| 本地开发环境 | http://[本机IP]  | 支持       | 不支持     | 不支持   |          |
| 本地开发环境 | file:///         | 支持       | 支持       | 支持     |          |

### 防火墙限制

在使用 TRTC Web SDK 时，用户可能因防火墙限制导致无法正常进行音视频通话，请参考 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399) 将相应端口及域名添加至防火墙白名单中。

## 开始集成
SDK 提供了 UMD、ES Module 类型的模块，以及 TypeScript Type Definition 文件，满足在不同类型项目中集成。
### NPM 集成
1. 您需要在项目中使用 npm 安装 [trtc-js-sdk](https://www.npmjs.com/package/trtc-js-sdk) 包。
```
npm install trtc-js-sdk --save
```
2. 在项目脚本里引入模块。
```javascript
import TRTC from 'trtc-js-sdk';
```

### Script 集成
1. 在您的 Web 页面中添加如下代码即可：
```html
<script src="trtc.js"></script>
```
2. 在脚本中通过 `TRTC` 命名空间访问 API。
```javascript
const client = TRTC.createClient({...});
```

**资源下载**
- [单击下载 SDK 及示例](https://web.sdk.qcloud.com/trtc/webrtc/download/webrtc_latest.zip)
- [GitHub 仓库地址](https://github.com/LiteAVSDK/TRTC_Web)

## 详细指引
更详细的初始化流程和 API 使用介绍请参见以下指引：

| 功能                       | Sample Code 指引                                                                                                    |
|--------------------------|-------------------------------------------------------------------------------------------------------------------|
| 基础音视频通话             | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-11-basic-video-call.html)                      |
| 实现互动直播连麦           | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-12-basic-live-video.html)                      |
| 切换摄像头和麦克风         | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-13-basic-switch-camera-mic.html)               |
| 设置本地视频属性           | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-14-basic-set-video-profile.html)               |
| 动态关闭打开本地音频或视频 | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-15-basic-dynamic-add-video.html)               |
| 屏幕分享                   | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-16-basic-screencast.html)                      |
| 音量大小检测               | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-17-basic-detect-volume.html)                   |
| 自定义采集与自定义播放渲染 | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-20-advanced-customized-capture-rendering.html) |
| 房间内上行用户个数限制     | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-04-info-uplink-limits.html)                    |
| 背景音乐和音效实现方案     | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-22-advanced-audio-mixer.html)                  |
| 通话前环境与设备检测       | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-23-advanced-support-detection.html)            |
| 通话前的网络质量检测       | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-24-advanced-network-quality.html)              |
| 检测设备插拔行为           | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-25-advanced-device-change.html)                |
| 实现推流到 CDN             | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-26-advanced-publish-cdn-stream.html)           |
| 开启大小流传输             | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-27-advanced-small-stream.html)                 |
| 开启美颜                   | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-28-advanced-beauty.html)                       |
| 开启水印                   | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-29-advance-water-mark.html)                    |
| 实现跨房连麦               | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-30-advanced-cross-room-link.html)              |
| 实现云端混流               | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-31-advanced-mix-transcode.html)                |
| 实现云端录制               | [指引链接](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-32-advanced-cloud-record.html)                 |
| 实现语音识别               | [指引链接](https://cloud.tencent.com/document/product/1093/68499)                                                   |

>? 
>- [单击查看](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-10-basic-get-started-with-demo.html) 更多能力。
>- 常见问题参见 [Web 端相关](https://cloud.tencent.com/document/product/647/45558)。
