本文介绍如何快速跑通腾讯云 Web 直播互动组件的体验 Demo。

## 效果展示

![](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/doc-assets/demo-official-website.gif)

## 环境要求

- 请使用最新版本的 Chrome 浏览器。
- TWebLive 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/index.html) 检查配置是否生效。
  - TCP 端口：8687
  - UDP 端口：8000，8080，8800，843，443，16285
  - 域名：qcloud.rtc.qq.com

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

### 步骤1：创建新的应用<span id="step1"></span>

1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
2. 进入[【应用管理】](https://console.cloud.tencent.com/trtc/app)，单击【创建应用】，输入应用名称，例如 `testtrtc`，单击【确定】。

### 步骤2：获取 SDKAppID 和密钥<span id="step2"></span>

1. 在应用列表里，找到已创建的应用，单击右侧的【应用信息】进入详情页，即可复制保存 `SDKAppID` 信息。
![](https://main.qcloudimg.com/raw/64bad9b2d6a0589f2c97b7c021af27ed.png)
2. 单击【快速上手】页签，查看【第二步 获取签发UserSig的密钥】标签，单击【复制密钥】。
![](https://main.qcloudimg.com/raw/648d534f5de68488c0d6d83567bcc8e1.png)

>! 请妥善保管密钥信息，谨防泄露。

### 步骤3：下载并配置 Demo 源码<span id="step3"></span>

1. 下载腾讯云 Web 直播互动组件 Demo 工程，[下载地址](https://github.com/tencentyun/TWebLive)。
2. 打开 `TWebLive/dist/debug/GenerateTestUserSig.js` 文件，并设置相关参数：
 - SDKAPPID：请设置为 [步骤2](#step2) 中获取的实际应用 `SDKAppID`。
 - SECRETKEY：请设置为 [步骤2](#step2) 中获取的实际密钥信息。

![](https://main.qcloudimg.com/raw/2bae16dd7363d1deffcfc82f1bd848f5.png)


>!
>- 本地计算 UserSig 的方式仅用于本地开发调试，请勿直接发布到线上，一旦您的 `SECRETKEY` 泄露，攻击者就可以盗用您的腾讯云流量。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

### 步骤4：运行 Demo<span id="step4"></span>

使用 Chrome 浏览器打开 `dist` 目录下的 `index.html` 文件即可运行 Demo。

>!
>- 一般情况下体验 Demo 需要部署至服务器，通过 `https://域名/xxx` 访问，或者直接在本地搭建服务器，通过 `localhost:端口`访问。
- 目前桌面端 Chrome 浏览器支持 TRTC 桌面浏览器 SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

**Demo 运行界面如图所示：**
![](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/doc-assets/demo-pusher.png)

TWebLive 需要使用摄像头和麦克风采集音视频，在体验过程中您可能会收到来自 Chrome 浏览器的相关提示，单击【允许】。
![](https://main.qcloudimg.com/raw/1a2c1e7036720b11f921f8ee1829762a.png)

## 支持平台

WebRTC 技术由 Google 最先提出，目前主要在桌面版 Chrome 浏览器、桌面版 Safari 浏览器以及移动版的 Safari 浏览器上有较为完整的支持，其他平台（例如 Android 平台的浏览器）支持情况均比较差。
- 在移动端推荐使用 [小程序](https://cloud.tencent.com/document/product/647/32399) 解决方案，微信和手机 QQ 小程序均已支持，都是由各平台的 Native 技术实现，音视频性能更好，且针对主流手机品牌进行了定向适配。
- 如果您的应用场景主要为教育场景，那么教师端推荐使用稳定性更好的 [Electron](https://cloud.tencent.com/document/product/647/38549) 解决方案，支持大小双路画面，更灵活的屏幕分享方案以及更强大的弱网络恢复能力。

|  操作系统   |          浏览器类型          | 浏览器最低版本要求 | 接收（播放） | 发送（上麦） |
| :---------: | :--------------------------: | :----------------: | :----------: | :----------: |
|   Mac OS    |     桌面版 Safari 浏览器     |        11+         |     支持     |     支持     |
|   Mac OS    |     桌面版 Chrome 浏览器     |        56+         |     支持     |     支持     |
|   Mac OS    |    桌面版 Firefox 浏览器     |        56+         |     支持     |     支持     |
|   Mac OS    |      桌面版 Edge 浏览器      |        80+         |     支持     |     支持     |
|   Windows   |     桌面版 Chrome 浏览器     |        56+         |     支持     |     支持     |
|   Windows   | 桌面版 QQ 浏览器（极速内核） |       10.4+        |     支持     |     支持     |
|   Windows   |    桌面版 Firefox 浏览器     |        56+         |     支持     |     支持     |
|   Windows   |      桌面版 Edge 浏览器      |        80+         |     支持     |     支持     |
| iOS 11.1.2+ |     移动版 Safari 浏览器     |        11+         |     支持     |     支持     |
| iOS 12.1.4+ |         微信内嵌网页         |         -          |     支持     |    不支持    |
|   Android   |       移动版 QQ 浏览器       |         -          |    不支持    |    不支持    |
|   Android   |       移动版 UC 浏览器       |         -          |    不支持    |    不支持    |
|   Android   |   微信内嵌网页（TBS 内核）   |         -          |     支持     |     支持     |
|   Android   |  微信内嵌网页（XWEB 内核）   |         -          |     支持     |    不支持    |

>! 由于 H.264 版权限制，华为系统的 Chrome 浏览器和以 Chrome WebView 为内核的浏览器均不支持 TRTC 桌面浏览器端 SDK 的正常运行。

## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？

TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。

### 2. 出现客户端错误：“RtcError: no valid ice candidate found”该如何处理？

出现该错误说明 TRTC 桌面浏览器 SDK 在 STUN 打洞失败，请根据环境要求检查防火墙配置。

### 3. 出现客户端错误：“RtcError: ICE/DTLS Transport connection failed”或 “RtcError: DTLS Transport connection timeout”该如何处理？

出现该错误说明 TRTC 桌面浏览器 SDK 在建立媒体传输通道时失败，请根据环境要求检查防火墙配置。

### 4. 出现10006 error 该如何处理？

如果出现 `"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"`，请确认您的实时音视频应用的服务状态是否为可用状态。
登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击【帐号信息】，在帐号信息面板即可确认服务状态。
![](https://main.qcloudimg.com/raw/13c9b520ea333804cffb4e2c4273fced.png)


## 相关文档

- [TWebLive 接口手册](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblive/TWebLive.html)
- [在线 Demo](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/index.html)
