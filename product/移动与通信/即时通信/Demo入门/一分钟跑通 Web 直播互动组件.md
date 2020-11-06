本文介绍如何快速跑通腾讯云 Web 直播互动组件的体验 Demo。

## 效果展示

![](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/doc-assets/demo-official-website.gif)

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

### 步骤1：创建应用

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
2. 单击【+添加新应用】。
3. 在【创建应用】对话框中输入您的应用名称，单击【确定】。
 创建完成后，可在控制台总览页查看新建应用的状态、业务版本、`SDKAppID`、创建时间以及到期时间。请记录 `SDKAppID` 信息。
  ![](https://main.qcloudimg.com/raw/2753962b67754a9ebb2a2a5b8042f2ef.png)


### 步骤2：获取密钥信息并开通实时音视频服务

1. 单击目标应用卡片，进入应用的基础配置页面。
2. 在【基本信息】区域，单击【显示密钥】，复制并保存密钥信息。
 >!请妥善保管密钥信息，谨防泄露。
3. 开通腾讯云实时音视频服务。
![](https://main.qcloudimg.com/raw/a4bec00426fc66d7b87404e6a9649f83.png)

### 步骤3：下载并配置 Demo 源码

1. 下载腾讯云 Web 直播互动组件 Demo 工程，[下载地址](https://github.com/tencentyun/TWebLive)。
2. 打开 `TWebLive/dist/debug/GenerateTestUserSig.js` 文件，并设置相关参数：
 - SDKAPPID：请设置为步骤1中获取的实际应用 SDKAppID。
 - SECRETKEY：请设置为步骤2中获取的实际密钥信息。
 ![](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/doc-assets/sdkappid_secretkey.png)


>!
>- 本地计算 UserSig 的方式仅用于本地开发调试，请勿直接发布到线上，一旦您的 `SECRETKEY` 泄露，攻击者就可以盗用您的腾讯云流量。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

### 步骤4：运行 Demo
使用 Chrome 浏览器打开 `dist` 目录下的 `index.html` 文件即可运行 Demo。
>!
>- 一般情况下体验 Demo 需要部署至服务器，通过 `https://域名/xxx` 访问，或者直接在本地搭建服务器，通过 `localhost:端口` 访问。
>- 目前桌面端 Chrome 浏览器支持 TRTC 桌面浏览器 SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

Demo 运行界面如图所示：
![](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/doc-assets/demo-pusher.png)

WebRTC 需要使用摄像头和麦克风采集音视频，在体验过程中您可能会收到来自 Chrome 浏览器的相关提示，单击【允许】。
![](https://main.qcloudimg.com/raw/1a2c1e7036720b11f921f8ee1829762a.png)

## 环境要求
- 请使用最新版本的 Chrome 浏览器。
- TWebLive 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/index.html) 检查配置是否生效。
  - TCP 端口：8687
  - UDP 端口：8000，8080，8800，843，443，16285
  - 域名：qcloud.rtc.qq.com

## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。

### 2. 出现客户端错误：“RtcError: no valid ice candidate found”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在 STUN 打洞失败，请根据环境要求检查防火墙配置。

### 3. 出现客户端错误：“RtcError: ICE/DTLS Transport connection failed”或“RtcError: DTLS Transport connection timeout”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在建立媒体传输通道时失败，请根据环境要求检查防火墙配置。

### 4. 出现10006 error 该如何处理？
如果出现"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"，请确认您的实时音视频应用的服务状态是否为可用状态。
登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击【帐号信息】，在帐号信息面板即可确认服务状态。
![](https://main.qcloudimg.com/raw/13c9b520ea333804cffb4e2c4273fced.png)


## 相关文档

- [TWebLive 接口手册](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblive/TWebLive.html)
- [在线 Demo](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/index.html)
