本文主要介绍如何快速地将腾讯云视立方桌面浏览器 SDK 集成到您的项目中。

## 支持的平台

WebRTC 技术由 Google 最先提出，目前主要在桌面版 Chrome 浏览器、桌面版 Edge 浏览器、桌面版 Firefox 浏览器、桌面版 Safari 浏览器以及移动版的 Safari 浏览器上有较为完整的支持，其他平台（例如 Android 平台的浏览器）支持情况均比较差。
- 在移动端推荐使用 [小程序](https://cloud.tencent.com/document/product/647/32183) 解决方案，微信和手机 QQ 小程序均已支持，都是由各平台的 Native 技术实现，音视频性能更好，且针对主流手机品牌进行了定向适配。
- 如果您的应用场景主要为教育场景，那么教师端推荐使用稳定性更好的 [Electron](1) 解决方案，支持大小双路画面，更灵活的屏幕分享方案以及更强大的弱网络恢复能力。


<table>
<tr>
<th>操作系统</th>
<th width="22%">浏览器类型</th><th>浏览器最低<br>版本要求</th><th width="16%">接收（播放）</th><th width="16%">发送（上麦）</th><th>屏幕分享</th><th>SDK 版本要求</th>
</tr><tr>
<td rowspan="4">Mac OS</td>
<td>桌面版 Safari 浏览器</td>
<td>11+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Safari13+ 版本）</td>
<td>-</td>
</tr>
<tr>
<td>桌面版 Chrome 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Chrome72+ 版本）</td>
<td>-</td>
</tr>
<tr>
<td>桌面版 Firefox 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Firefox66+ 版本）</td>
<td>v4.7.0+</td>
</tr>
<tr>
<td>桌面版 Edge 浏览器</td>
<td>80+</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>v4.7.0+</td>
</tr>
<tr>
<td  rowspan="4">Windows</td>
<td>桌面版 Chrome 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Chrome72+ 版本）</td>
<td>-</td>
</tr>
<tr>
<td>桌面版 QQ 浏览器（极速内核）</td>
<td>10.4+</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
<td>-</td>
</tr>
<tr>
<td>桌面版 Firefox 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Firefox66+ 版本）</td>
<td>v4.7.0+</td>
</tr>
<tr>
<td>桌面版 Edge 浏览器</td>
<td>80+</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>v4.7.0+</td>
</tr>
<tr>
<td>iOS 11.1.2+</td>
<td>移动版 Safari 浏览器</td>
<td>11+</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
<td>-</td>
</tr>
<tr>
<td>iOS 12.1.4+</td>
<td>微信内嵌网页</td>
<td>-</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
<td>-</td>
</tr>
<tr>
<td>iOS 14.3+</td>
<td>微信内嵌网页</td>
<td>6.5+（微信版本）</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
<td>-</td>
</tr>
<tr>
<td  rowspan="4">Android</td>
<td>移动版 QQ 浏览器</td>
<td>-</td>
<td>不支持</td>
<td>不支持</td>
<td>不支持</td>
<td>-</td>
</tr><tr>
<td>移动版 UC 浏览器</td>
<td>-</td>
<td>不支持</td>
<td>不支持</td>
<td>不支持</td>
<td>-</td>
</tr>
<tr>
<td>微信内嵌网页（TBS 内核）</td>
<td>-</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
<td>-</td>
</tr>
<tr>
<td>微信内嵌网页（XWEB 内核）</td>
<td>-</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
<td>-</td>
</tr>
</table>


> ! 
> - 您可以在浏览器中打开 [WebRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 页面进行检测是否完整支持 WebRTC。例如公众号等浏览器环境。
> - 由于 H.264 版权限制，华为系统的 Chrome 浏览器和以 Chrome WebView 为内核的浏览器均不支持 TRTC 桌面浏览器 SDK 的正常运行。


## 防火墙限制
TRTC 桌面浏览器 SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单。
- TCP 端口：8687
- UDP 端口：8000，8080，8800，843，443，16285
- 域名：qcloud.rtc.qq.com

## 集成桌面浏览器 SDK

### NPM 集成

您需要在项目中使用 npm 安装 SDK 包。

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

SDK 下载地址：[单击下载](https://web.sdk.qcloud.com/trtc/webrtc/download/webrtc_latest.zip) 。

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

