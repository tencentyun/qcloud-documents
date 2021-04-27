本文主要介绍如何快速运行腾讯云 TRTC 桌面浏览器 SDK Demo。

## 支持的平台

WebRTC 技术由 Google 最先提出，目前主要在桌面版 Chrome 浏览器、桌面版 Edge 浏览器、桌面版 Firefox 浏览器、桌面版 Safari 浏览器以及移动版的 Safari 浏览器上有较为完整的支持，其他平台（例如 Android 平台的浏览器）支持情况均比较差。
- 在移动端推荐使用 [小程序](https://cloud.tencent.com/document/product/647/32399) 解决方案，微信和手机 QQ 小程序均已支持，都是由各平台的 Native 技术实现，音视频性能更好，且针对主流手机品牌进行了定向适配。
- 如果您的应用场景主要为教育场景，那么教师端推荐使用稳定性更好的 [Electron](https://cloud.tencent.com/document/product/647/38549) 解决方案，支持大小双路画面，更灵活的屏幕分享方案以及更强大的弱网络恢复能力。



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

>! 
>- 您可以在浏览器中打开 [WebRTC 能力测试](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 页面进行检测是否完整支持 WebRTC。例如公众号等浏览器环境。
>- 由于 H.264 版权限制，华为系统的 Chrome 浏览器和以 Chrome WebView 为内核的浏览器均不支持 TRTC 桌面浏览器端 SDK 的正常运行。

[](id:requirements)
## 环境要求
- 请使用最新版本的 Chrome 浏览器。
- TRTC 桌面浏览器 SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/latest/official-demo/index.html) 检查配置是否生效。
 - TCP 端口：8687
 - UDP 端口：8000，8080，8800，843，443，16285
 - 域名：qcloud.rtc.qq.com
 
## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

[](id:step1)

### 步骤1：创建新的应用
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如 TestTRTC，单击【创建】。
![](https://main.qcloudimg.com/raw/9b2db43594f4744b42ef74c94494ea8e.png)

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 Demo 源码。
2. 下载完成后，单击【已下载，下一步】。
![](https://main.qcloudimg.com/raw/3b115019ddfd0866108ed1add30810d8.png)

[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Web/TRTCSimpleDemo/js/debug/GenerateTestUserSig.js` 文件。
3. 设置 `GenerateTestUserSig.js` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
	<img src="https://main.qcloudimg.com/raw/4c55667af4fc19b7cfd4f8e34cebcc18.png">
4. 粘贴完成后，单击【已复制粘贴，下一步】即创建成功。
5. 编译完成后，单击【回到控制台概览】即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：运行 Demo
使用 Chrome 浏览器打开 Demo 根目录下的 `index.html` 文件即可运行 Demo。

>!
> - 一般情况下体验 Demo 需要部署至服务器，通过 `https://域名/xxx` 访问，或者直接在本地搭建服务器，通过 `localhost:端口` 访问。
> - 目前桌面端 Chrome 浏览器支持 TRTC 桌面浏览器 SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

Demo 运行界面如图所示：
![](https://main.qcloudimg.com/raw/e989c968446e6e3bdcc19c58e40e2b86.png)
- 单击【加入房间】加入音视频通话房间并且发布本地音视频流。
 您可以打开多个页面，每个页面都单击 【加入房间】，正常情况下可以看到多个画面并模拟实时音视频通话。
- 单击摄像头图标可以选择摄像头设备。
- 单击麦克风图标可以选择麦克风设备。

>?WebRTC 需要使用摄像头和麦克风采集音视频，在体验过程中您可能会收到来自 Chrome 浏览器的相关提示，单击【允许】。
> ![](https://main.qcloudimg.com/raw/1a2c1e7036720b11f921f8ee1829762a.png)


## 常见问题
### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法 ECDSA-SHA256](https://cloud.tencent.com/document/product/647/17275#Old)，如已升级，您按需切换为新旧算法。

升级/切换操作：
 1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
 2. 在左侧导航栏选择【应用管理】，单击目标应用所在行的【应用信息】。
 3. 选择【快速上手】页签，单击【第二步 获取签发UserSig的密钥】区域的【点此升级】、【非对称式加密】或【HMAC-SHA256】。
  - 升级：
   ![](https://main.qcloudimg.com/raw/69bd0957c99e6a6764368d7f13c6a257.png)
  - 切换回老版本算法 ECDSA-SHA256：
   ![](https://main.qcloudimg.com/raw/f89c00f4a98f3493ecc1fe89bea02230.png)
  - 切换为新版本算法 HMAC-SHA256：
   ![](https://main.qcloudimg.com/raw/b0412153935704abc9e286868ad8a916.png)

### 2. 出现客户端错误：“RtcError: no valid ice candidate found”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在 STUN 打洞失败，请根据 [环境要求](#requirements) 检查防火墙配置。

### 3. 出现客户端错误："RtcError: ICE/DTLS Transport connection failed" 或 “RtcError: DTLS Transport connection timeout”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在建立媒体传输通道时失败，请根据 [环境要求](#requirements) 检查防火墙配置。

### 4. 出现10006 error 该如何处理？
如果出现"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"，请确认您的实时音视频应用的服务状态是否为可用状态。
登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击【帐号信息】，在帐号信息面板即可确认服务状态。
![](https://main.qcloudimg.com/raw/13c9b520ea333804cffb4e2c4273fced.png)
