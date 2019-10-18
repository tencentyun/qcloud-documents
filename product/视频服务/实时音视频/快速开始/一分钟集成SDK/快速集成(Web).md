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

## 更新日志

### 4.1.0（2019-10-17）

**Feature**

- Stream.play() 接口支持传入 HTMLDivElement 对象。
- 增加音频码率调控设置，开发者可通过 LocalStream.setAudioProfile() 设置音频属性，目前支持两种 Profile：standard 和 high。

**BugFixes**

- 修复旧版本 Chrome 上的 WebAudio Context 数量受限问题。
- 修复 replaceTrack() 未重启本地音视频播放器问题。
- 修复 LocalStream.setScreenProfile() 自定义属性设置未生效问题。
- 修复 audio/video player 重启及状态上报问题。

### 4.0.0（2019-10-11）

TRTC Web SDK (WebRTC) 重构版本，提供 Client/Stream 模式的接口，各对象职责更明确，语义更简洁明了。
重构版本与旧版本不兼容，除接口改动之外，还提供以下功能：
- 视频属性 （分辨率、帧率及码率）控制完全由 App 通过 SDK 的 LocalStream.setVideoProfile() 接口设置，不再支持老版本通过腾讯云控制台的“画面设定 （Spear Role）”。
- SDK 在 Stream 对象中封装了音视频播放器，音视频播放完全由 SDK 控制。
- 提供远端流的订阅与取消订阅功能，开发者可以通过 Client.subscribe()/unsubscribe() 接口灵活控制远端流的音频、视频或音视频数据流的接收。

### 3.1.0（2019-04-17）

- 修复屏幕分享切换视频流失败问题。
- 修复其他已知问题。

### 3.0.6（2019-04-08）

- 修复已知问题。

### 3.0（2018-09-11）

- 调整初始化接口。
- 弃用字段 accountType。
- 弃用字段 closeLocalMedia 默认不再推流。
- 弃用字段 video 不再支持配置是否进行音视频推流。
- 弃用字段 audio 不再支持配置是否进行音视频推流。
- 弃用成功和失败回调。

### 2.6.1（2018-08-16）

- 增加接口 getSpeakerDevices（枚举音频输出设备）。
- 增加接口 chooseSpeakerDevice（选择音频输出设备）。

### 2.6 （2018-08-10）

- 新增 SoundMeter 接口。
- 新增日志上报的字段。
- createRoom 名称改为 enterRoom。

## 常见问题

### 1. 防火墙有什么限制？

由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。
