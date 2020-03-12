## 集成 SDK

本文主要介绍如何快速的将腾讯云 TEduBoard SDK 集成到您的项目中。

## 支持平台

| 操作系统平台  | 浏览器/Webview  | 版本要求  |  备注|
| ------------------------- | -------- | ---------------------- |------- |
| Windows  | Chrome | 50+   |   Win7+   |
| Windows  | IE | 10+ | Win7+    |
| Windows  | Firefox | 50+ | Win7+    |
| Mac  | Chrome | 50+   |   -   |
| Mac  | Safari | 8+ | -    |
| Mac  | Firefox | 50+ | -    |
| iOS          | - | 系统版本 8.1+ | - |
| Android      | - | 系统版本 4.2+ | 推荐使用 Chrome 浏览器，微信浏览器，手机 QQ 浏览器 |

## 集成 TEduBoard SDK

您只需要在您的 Web 页面中添加如下代码即可：

```html
<!-- axios SDK -->
<script src="https://resources-tiw.qcloudtrtc.com/board/third/axios/axios.min.js"></script>
<!-- COS SDK -->
<script src="https://resources-tiw.qcloudtrtc.com/board/third/cos/5.1.0/cos.min.js"></script>
<!-- TEduBoard SDK -->
<script src="https://resources-tiw.qcloudtrtc.com/board/2.4.4/TEduBoard.min.js"></script>
```

如果您需要添加视频文件还需要添加以下代码：
```html
<link href="https://resources-tiw.qcloudtrtc.com/board/third/videojs/video-js.min.css" rel="stylesheet">
<script src="https://resources-tiw.qcloudtrtc.com/board/third/videojs/video.min.js"></script>
```

