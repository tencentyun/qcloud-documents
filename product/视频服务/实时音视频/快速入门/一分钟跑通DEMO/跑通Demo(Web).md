本文主要介绍如何快速运行腾讯云 TRTC Web SDK Demo。

>?TRTC Web SDK Demo 主要面向开发者，如您想快速体验 TRTC Web SDK 功能，可直接访问 [官网体验 Ddemo](https://trtc-1252463788.file.myqcloud.com/web/demo/official-demo/index.html)。
在开始体验之前，建议您先了解 [TRTC Web SDK API 概览](https://trtc-1252463788.file.myqcloud.com/web/docs/index.html) 和 [基础音视频通话教程](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-01-basic-video-call.html)。

<span id="requirements"></span>
## 环境要求
- 请使用最新版本的 Chrome 浏览器。
- TRTC Web SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Ddemo](https://trtc-1252463788.file.myqcloud.com/web/demo/official-demo/index.html) 检查配置是否生效。
 - TCP 端口：8687
 - UDP 端口：8000，8800，843，443
 - 域名：qcloud.rtc.qq.com
 
 
## 操作步骤
<span id="step1"></span>
### 步骤1：创建新的应用
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/rav) ，单击【创建应用】。
  如果您已有应用，请记录其 SDKAppID 然后直接 [下载 SDK 和 Demo 源码](#step2)。否则，继续执行下一步。
2. 填写新建应用的应用名称等信息，单击【确定】。
  应用创建完成后，自动生成一个应用标识 SDKAppID，请记录 SDKAppID 信息。
 ![](https://main.qcloudimg.com/raw/1acc030cfc47e32bc36873c9a494b88a.png)

<span id="step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 单击应用卡片，进入【快速上手】页面。
2. 单击【第一步 下载SDK + 配套Demo源码】区域的【Web】跳转至 [Github](https://github.com/tencentyun/TRTCSDK)（或直接访问 [Gitee](https://gitee.com/cloudtencent/TRTCSDK)），下载相关 SDK 和 Demo 源码。
![](https://main.qcloudimg.com/raw/dc356e48e252440270448438b5568b41.png)

<span id="step3"></span>
### 步骤3：查看并拷贝加密密钥
1. 单击【第二步 获取签发UserSig的密钥】区域的【查看密钥】，即可获取用于计算 UserSig 的加密密钥。
2. 单击【复制密钥】，将密钥拷贝到剪贴板中。
![](https://main.qcloudimg.com/raw/d0b780f7b28833533e12807d1b11d8be.png)

<span id="CopyKey"></span>
### 步骤4：配置 Demo 工程文件
Demo 源码工程中的`GenerateTestUserSig.js`文件可以通过 HMAC-SHA256 算法在本地计算 UserSig，用于快速跑通 Demo。
 
1. 解压 [步骤2](#step2) 中下载的源码包。
2. 找到并打开 `Web/js/debug/GenerateTestUserSig.js`文件。
3. 设置`GenerateTestUserSig.js`文件中的相关参数：
  - SDKAPPID：请设置为 [步骤1](#step1) 中获取的实际 SDKAppID。
  - SECRETKEY：请设置为 [步骤3](#step3) 中获取的实际密钥信息。
  ![](https://main.qcloudimg.com/raw/d8f5960ab7c08bb0a488ac7e98d162ba.png)

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤5：运行 Demo
使用 Chrome 浏览器打开 Demo 根目录下的`index.html`文件即可运行 Demo。

>!
> - 一般情况下体验 Demo 需要部署至服务器，通过`https://域名/xxx`访问，或者直接在本地搭建服务器，通过`localhost:端口`访问。
> - 目前桌面端 Chrome 浏览器支持 TRTC Web SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

Demo 运行界面如图所示：
![](https://main.qcloudimg.com/raw/d261de9f7d9a467afcbd26cf273149a4.png)
- 单击【加入房间】加入音视频通话房间并且发布本地音视频流。
 您可以打开多个页面，每个页面都单击 【加入房间】，正常情况下可以看到多个画面并模拟实时音视频通话。
- 单击【离开房间】退出音视频通话。
- 单击【开始推流】发布本地音视频流。
- 单击【停止推流】停止发布本地音视频流。

>?WebRTC 需要使用摄像头和麦克风采集音视频，在体验过程中您可能会收到来自 Chrome 浏览器的相关提示，单击【允许】。
![](https://main.qcloudimg.com/raw/2f595dc976970c5398efd993ade5b22b.png)

## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先单击【第二步 获取签发UserSig的密钥】区域的【点此升级】升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法](https://cloud.tencent.com/document/product/647/17275#.E8.80.81.E7.89.88.E6.9C.AC.E7.AE.97.E6.B3.95) ECDSA-SHA256。

### 2. 出现客户端错误：“RtcError: no valid ice candidate found”该如何处理？
出现该错误说明 TRTC Web SDK 在 STUN 打洞失败，请根据 [环境要求](#requirements) 检查防火墙配置。

### 3. 出现客户端错误："RtcError: ICE/DTLS Transport connection failed" 或 “RtcError: DTLS Transport connection timeout”该如何处理？
出现该错误说明 TRTC Web SDK 在建立媒体传输通道时失败，请根据 [环境要求](#requirements) 检查防火墙配置。

### 4. 出现10006 error 该如何处理？
如果出现"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"，请确认您的实时音视频应用的服务状态是否为可用状态。
登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击【帐号信息】，在帐号信息面板即可确认服务状态。
![](https://main.qcloudimg.com/raw/13c9b520ea333804cffb4e2c4273fced.png)
