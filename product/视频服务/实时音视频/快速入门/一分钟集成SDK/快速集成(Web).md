本文主要介绍如何快速地将腾讯云 TRTC Web SDK 集成到您的项目中。

## 支持的平台

在 Web 端实现实时音视频通话，需要浏览器完整支持 WebRTC 能力，目前已知支持 WebRTC 的浏览器如下表所示：

| 操作系统平台 | 浏览器/webview | 版本要求 | 备注                                                                                                                              |
| ------------ | -------------- | -------- | ------------------------------------ |
| iOS          | Safari         | 11.1.2   | 由于苹果 Safari 仍有偶现的 bug，产品化方案建议先规避，待苹果解决后再使用，<br > 因此对于 iOS 推荐使用兼容性更好的小程序解决方案。 |
| Android      | TBS            | 43600    | 微信和手机 QQ 默认内置的浏览器内核为 [TBS](http://x5.tencent.com/)。    |
| Android      | Chrome         | 60+      | 需要支持 H264 编解码。    |
| Mac          | Chrome         | 47+      | - |
| Mac          | Safari         | 11+      | - |
| Windows(PC)  | Chrome         | 52+      | - |
| Windows(PC)  | QQ 浏览器      | 10.2     | - |

> ?基于 TBS 内核的 WebView，需满足版本 ≥ 43600。
> 可以在浏览器中打开 [WebRTC 能力测试](https://www.qcloudtrtc.com/webrtc-samples/abilitytest/index.html) 页面进行检测是否完整支持 WebRTC。例如公众号等浏览器环境。
> 华为系统的 Chrome 浏览器和以 Chrome WebView 为内核的浏览器不支持 H264 编码。


## 环境要求
TRTC Web SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单。
- TCP 端口：8687
- UDP 端口：8000，8800，843，443
- 域名：qcloud.rtc.qq.com

## 集成 TRTC Web SDK

### NPM 集成

在您的项目中使用 npm 安装 SDK 包。

```
npm install trtc-js-sdk --save
```

在项目脚本里引入模块。

```javascript
import TRTC from 'trtc-js-sdk';
```

### Script 集成

您只需要在您的 Web 页面中添加如下代码即可：

```html
<script src="trtc.js"></script>
```

## 相关资源

SDK 下载地址：[单击下载](http://trtc-1252463788.cosgz.myqcloud.com/web/sdk/trtc.js)

更详细的初始化流程和 API 使用介绍请参见以下指引：

| 功能                       | Sample Code 指引                                                                                           |
| -------------------------- | --------------------------- |
| 基础音视频通话  | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-01-basic-video-call.html)           |
| 互动直播      | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-02-live-video.html)                 |
| 切换摄像头和麦克风   | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-03-advanced-switch-camera-mic.html) |
| 设置本地视频属性  | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-04-advanced-set-video-profile.html) |
| 动态关闭打开本地音频或视频 | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-05-advanced-dynamic-add-video.html) |
| 屏幕分享   | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-06-advanced-screencast.html)        |
| 音量大小检测  | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-07-advanced-detect-volume.html)     |


