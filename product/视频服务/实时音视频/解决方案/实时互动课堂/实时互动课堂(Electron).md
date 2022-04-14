TRTC 实时互动课堂是一款开源的在线课堂软件，支持一名教师给多名学生在线上课，一个课堂最多同时支持 300 人在线实时互动。如果开启旁路直播、CDN推流服务，可支持上万人在线观看。本软件基于[腾讯云实时音视频通信（Tencent Real-Time Communication, TRTC）](https://cloud.tencent.com/product/trtc)、[腾讯云即时通信（Tencent Instant Message, TIM）](https://cloud.tencent.com/product/im)、Electron、React 和 Webpack 等构建。
>! [腾讯云实时音视频通信（Tencent Real-Time Communication, TRTC）](https://cloud.tencent.com/product/trtc)、[腾讯云即时通信（Tencent Instant Message, TIM）](https://cloud.tencent.com/product/im) 是以 SDK 形式提供的 PaaS 服务，源代码不开源。TRTC 实时互动课堂开源代码只包括 UI 部分和基于 SDK 实现的互动课堂功能代码。

## Demo 体验

建议使用两台电脑体验，效果更佳，一台作为教师端，创建课堂；另一台作为学生端，加入课堂。

<input type="button" value="Windows 版" style="height: 30px;width: 150px;min-width: 24px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;white-space: nowrap;margin-right:10px;"  onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-windows-latest.zip')" />

<input type="button" value="MacOS 版" style="height: 30px;width: 150px;margin-top: 5px;min-width: 24px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;white-space: nowrap;" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-mac-latest.zip')" />

## 效果展示
您可以下载、安装我们已经构建好的 App 安装包， 体验实时互动课堂的能力效果。除了基础的实时音视频通话、白板分享、屏幕分享、文字聊天功能，还提供了全员禁麦、学生举手申请发言、老师邀请学生发言、点名、签到等丰富的课堂互动功能。

<table>
<tr><th style="text-align:center">教师端</th><th style="text-align:center">学生端</th><tr>
<tr><td><img src="https://web.sdk.qcloud.com/trtc/electron/download/resources/education-v2/preview-teacher.gif"/></td><td><img src="https://web.sdk.qcloud.com/trtc/electron/download/resources/education-v2/preview-student.gif"/></td><tr>
</table>

## 跑通源码
单击进入 [Github](https://github.com/TencentCloud/trtc-education-electron)，参照说明文档运行源码。可以根据您的业务需要，基于开源代码二次开发。

## 多终端互联互通

Electron 版的实时互动课堂，与 [Windows & Mac](https://cloud.tencent.com/document/product/647/63494)、[Android](https://cloud.tencent.com/document/product/647/45667)、[iOS](https://cloud.tencent.com/document/product/647/45681) 版的 [多人音视频房间](https://cloud.tencent.com/document/product/647/70345) 可以实现互通，软件逻辑层有一个接口一致的 TUIRoom 层实现多端互通，如果您有这些终端的互通需求，可以同时结合这些终端的开源项目，一起使用。

## 技术咨询
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">695855795</dx-tag-link>

## 参考文档

- [SDK API 手册](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/index.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/647/43117)
- [Simple Demo 源码](https://github.com/LiteAVSDK/TRTC_Electron/tree/main/TRTCSimpleDemo)
- [API Example 源码](https://github.com/LiteAVSDK/TRTC_Electron/tree/main/TRTC-API-Example)
- [Electron 常见问题](https://cloud.tencent.com/document/product/647/62562)
