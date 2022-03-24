本文主要介绍如何快速运行腾讯云 TRTC Web SDK Demo。
## 准备工作
运行 TRTC Web SDK Demo 之前需要了解的事项。

### 支持的平台
TRTC Web SDK 基于 WebRTC 实现，目前支持桌面端和移动端的主流浏览器，详细支持度表格请参见 [支持的平台](https://cloud.tencent.com/document/product/647/17249#.E6.94.AF.E6.8C.81.E7.9A.84.E5.B9.B3.E5.8F.B0)。
如果您的应用场景不在支持的表格里，可以打开 [TRTC Web SDK 能力检测页面](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 检测当前环境是否支持 WebRTC 所有能力，例如 WebView 等环境。

- 移动端同时推荐使用 [小程序](https://cloud.tencent.com/document/product/647/32183) 解决方案，微信和手机 QQ 小程序均已支持，都是由各平台的 Native 技术实现，音视频性能更好，且针对主流手机品牌进行了定向适配。
- 如果您的应用场景主要为教育场景，那么教师端推荐使用 [Electron](https://cloud.tencent.com/document/product/647/38549) 解决方案，支持大小双路画面，更灵活的屏幕分享方案以及更强大的弱网络恢复能力。 

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
TRTC Web SDK 依赖以下端口及域名进行数据传输，请将其加入防火墙白名单。配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/basic-rtc.html) 检查配置是否生效。具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)。
- TCP 端口：8687
- UDP 端口：8000，8080，8800，843，443，16285
- 域名：`*.rtc.qq.com`，`yun.tim.qq.com`


## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

[](id:step1)

### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助** > **[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 单击 **新建应用** 输入应用名称，例如 `TestTRTC`；若您已创建应用可单击 **选择已有应用**。
3. 根据实际业务需求添加或编辑标签，单击 **创建**。

![](https://main.qcloudimg.com/raw/f04d288ed091c98a5e8056eb86fb49e8.png)

>?
>- 应用名称只能包含数字、中英文字符和下划线，长度不能超过15个字符。
>- 标签用于标识和组织您在腾讯云的各种资源。例如：企业可能有多个业务部门，每个部门有1个或多个 TRTC 应用，这时，企业可以通过给 TRTC 应用添加标签来标记部门信息。标签并非必选项，您可根据实际业务需求添加或编辑。

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 下载 Web 端 SDK 及配套的 Demo 源码。
2. 下载完成后，单击 **“已下载，下一步”**。

<img src="https://qcloudimg.tencent-cloud.cn/raw/694a75aa29fa7ae11cb14f3948bbf386.png" width="800px">

[](id:step3)
### 步骤3：获取 SDKAppId 和 密钥（SecretKey)
1. 进入修改配置页，获取 `SDKAppID` 和`密钥`。
2. 复制粘贴 SDKAppId 和 密钥（SecretKey）完成后，单击 **已复制粘贴，下一步** 即创建成功。

![](https://qcloudimg.tencent-cloud.cn/raw/c9652bf61b518cf7c849676afeced0fc.png)

[](id:step4)
### 步骤4：运行 Demo 

为满足不同客户的需求，TRTC Web 目前提供以下几种基础 Demo：
- **`base-js`** 为 TRTC Web 基础 Demo。TRTC Web 基础 Demo 集成了 TRTC Web SDK 的基础音视频通话、设备选择等功能，使用 jQuery 开发，可直接在浏览器中运行。快速体验可访问 [base-js 在线体验地址](https://web.sdk.qcloud.com/trtc/webrtc/demo/latest/official-demo/index.html)。
- **`quick-demo-js`** 为 TRTC Web 快速运行 Demo (原生 Js 版本)。TRTC Web 快速运行 Demo (原生 Js 版本) 集成了 TRTC Web SDK 的基础音视频通话、设备选择等功能，使用原生 Js 开发，可直接在浏览器中运行。快速体验可访问 [quick-demo-js 在线体验地址](https://web.sdk.qcloud.com//trtc/webrtc/demo/quick-demo-js/index.html)。
- **`quick-demo-vue2-js`** 为 TRTC Web 快速运行 Demo (Vue2 版本)。TRTC Web 快速运行 Demo (Vue2 版本) 集成了 TRTC Web SDK 的基础音视频通话、设备选择等功能，使用 Vue2 开发，需要您安装 Node 环境。快速体验可访问  [quick-demo-vue2-js 在线体验地址](https://web.sdk.qcloud.com/trtc/webrtc/demo/quick-demo-vue2-js/index.html)。

<dx-tabs>
::: Demo 1：base-js       
1. 在下载的源码中找到并打开 `TRTC_Web/base-js/js/debug/GenerateTestUserSig.js` 文件。
2. 设置 `GenerateTestUserSig.js` 文件中的相关参数：
  - SDKAPPID：默认为0，请设置为实际的 `SDKAppID`。
  - SECRETKEY：默认为空字符串，请设置为实际的`密钥`信息。 
<img src="https://imgcache.qq.com/operation/dianshi/other/pic-demo-web.56f27c320c21670c64d708d7008588bbd0cea2db.png" width="800px">
3. 运行 Demo：
使用 Chrome 浏览器打开 Demo 根目录下的 `index.html` 文件即可运行 Demo。
>!
> - 一般情况下体验 Demo 需要部署至服务器，通过 `https://域名/xxx` 访问，或者直接在本地搭建服务器，通过 `localhost:端口` 访问。
> - 目前桌面端 Chrome 浏览器支持 TRTC Web SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。
> 
Demo 运行界面如图所示：
![](https://main.qcloudimg.com/raw/e989c968446e6e3bdcc19c58e40e2b86.png)
	- 单击 **加入房间** 加入音视频通话房间并且发布本地音视频流。
	 您可以打开多个页面，每个页面都单击  **加入房间**，正常情况下可以看到多个画面并模拟实时音视频通话。
	- 单击摄像头图标可以选择摄像头设备。
	- 单击麦克风图标可以选择麦克风设备。
>?WebRTC 需要使用摄像头和麦克风采集音视频，在体验过程中您可能会收到来自 Chrome 浏览器的相关提示，单击 **允许**。
> ![](https://main.qcloudimg.com/raw/1a2c1e7036720b11f921f8ee1829762a.png)

:::
::: Demo 2：quick-demo-js    
1. 在下载的源码中找到并使用浏览器打开 `TRTC_Web/quick-demo-js/index.html` 文件。
>?
>- TRTC Web SDK 支持的浏览器请参见 [TRTC Web SDK 支持的平台](https://cloud.tencent.com/document/product/647/17249#.E6.94.AF.E6.8C.81.E7.9A.84.E5.B9.B3.E5.8F.B0)。
>- TRTC Web SDK 域名及端口白名单配置请参见 [TRTC Web SDK 域名及端口白名单配置](https://cloud.tencent.com/document/product/647/34399#webrtc-.E9.9C.80.E8.A6.81.E9.85.8D.E7.BD.AE.E5.93.AA.E4.BA.9B.E7.AB.AF.E5.8F.A3.E6.88.96.E5.9F.9F.E5.90.8D.E4.B8.BA.E7.99.BD.E5.90.8D.E5.8D.95.EF.BC.9F)。
2. 在浏览器打开的页面中填写 <a href="#step3">步骤三</a> 获取的 SDKAppId 和 SecretKey。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1bc92d7a252de240d18a40edceda031f.png" width="800px">
3. 功能体验：
	- 单击**进入房间**按钮进入房间
	- 单击**发布流**按钮发布本地流
	- 单击**取消发布流**按钮取消发布本地流
	- 单击**离开房间**按钮离开房间
	- 单击**开始共享屏幕**按钮布屏幕分享流
	- 单击**停止共享屏幕**按钮取消发布屏幕分享流
4. 加入房间后您可以通过分享邀请链接与被邀请人一起体验 TRTC Web 语音及视频互通功能。
:::
::: Demo 3：quick-demo-vue2-js      
1. 在下载的源码中找到并进入到 `TRTC_Web/quick-demo-vue2-js/` 目录下。
2. 安装依赖
```shell
npm install
```
3. 本地运行 Demo
```shell
npm run serve
```
默认浏览器会自动打开 [http://localhost:8080/](http://localhost:8080/) 地址。
>!
> - 端口号以 npm run serve 运行之后的实际端口号为准，默认为 8080。
> - TRTC Web SDK 支持的浏览器请参考：[TRTC Web SDK 支持的平台](https://cloud.tencent.com/document/product/647/17249#.E6.94.AF.E6.8C.81.E7.9A.84.E5.B9.B3.E5.8F.B0)。
> - TRTC Web SDK 域名协议限制请参考：[TRTC Web SDK 域名协议限制](https://cloud.tencent.com/document/product/647/17249#url-.E5.9F.9F.E5.90.8D.E5.8D.8F.E8.AE.AE.E9.99.90.E5.88.B6)。
> - TRTC Web SDK 域名及端口白名单配置请参考：[TRTC Web SDK 域名及端口白名单配置](https://cloud.tencent.com/document/product/647/34399#webrtc-.E9.9C.80.E8.A6.81.E9.85.8D.E7.BD.AE.E5.93.AA.E4.BA.9B.E7.AB.AF.E5.8F.A3.E6.88.96.E5.9F.9F.E5.90.8D.E4.B8.BA.E7.99.BD.E5.90.8D.E5.8D.95.EF.BC.9F)。
4. 在浏览器打开的页面中填写 <a href="#step3">步骤三</a> 获取的 SDKAppId 和 SecretKey。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c467bb6c522c80061d7663bb2a5ba4c8.png" width="800px">
5. 功能体验：
	- 单击**进入房间**按钮进入房间
	- 单击**发布流**按钮发布本地流
	- 单击**取消发布流**按钮取消发布本地流
	- 单击**离开房间**按钮离开房间
	- 单击**开始共享屏幕**按钮布屏幕分享流
	- 单击**停止共享屏幕**按钮取消发布屏幕分享流
6. 加入房间后您可以通过分享邀请链接与被邀请人一起体验 TRTC Web 语音及视频互通功能。
:::
</dx-tabs>

>!
>- 本文使用的生成 UserSig 的方案是在客户端中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。


## 常见问题
### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6（Web SDK 4.0）版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法 ECDSA-SHA256](https://cloud.tencent.com/document/product/647/17275#Old)，如已升级，您按需切换为新旧算法。

升级/切换操作：
 1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
 2. 在左侧导航栏选择 **应用管理**，单击目标应用所在行的 **应用信息**。
 3. 选择 **快速上手** 页签，单击 **第二步 获取签发UserSig的密钥** 区域的 **点此升级** 、 **非对称式加密** 或 **HMAC-SHA256**。
  - 升级：
  ![](https://qcloudimg.tencent-cloud.cn/raw/8cc65ddd7101486fda684e990acd4626.png)
  - 切换回老版本算法 ECDSA-SHA256：
 ![](https://qcloudimg.tencent-cloud.cn/raw/7650c896868586c96623145bafe8a209.png)
  - 切换为新版本算法 HMAC-SHA256：
 ![](https://qcloudimg.tencent-cloud.cn/raw/2796b694419cc7f2aaabf4efe79704da.png)

### 2. 出现客户端错误：“RtcError: no valid ice candidate found”该如何处理？
出现该错误说明 TRTC Web SDK 在 STUN 打洞失败，请根据 [环境要求](#requirements) 检查防火墙配置。

### 3. 出现客户端错误："RtcError: ICE/DTLS Transport connection failed" 或 “RtcError: DTLS Transport connection timeout”该如何处理？
出现该错误说明 TRTC Web SDK 在建立媒体传输通道时失败，请根据 [环境要求](#requirements) 检查防火墙配置。

### 4. 出现10006 error 该如何处理？
如果出现"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"，请确认您的实时音视频应用的服务状态是否为正常状态。
登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击 **帐号信息**，在帐号信息面板即可确认服务状态。
![](https://qcloudimg.tencent-cloud.cn/raw/e0ada374cd9f95fcc8401d5ceacf5358.png)

>? 其他常见问题参见 [Web 端相关](https://cloud.tencent.com/document/product/647/45558)。
