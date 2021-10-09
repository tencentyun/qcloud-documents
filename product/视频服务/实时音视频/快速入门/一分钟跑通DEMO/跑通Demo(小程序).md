 本文主要介绍如何快速跑通微信小程序版本的 TRTC Demo，您可以从 [Github](https://github.com/tencentyun/TRTCSDK) 上的 WXMini 目录下获取相关代码。Demo 中前三个功能项演示了三个不同的应用场景：
 
 - **语音聊天室**：纯语音交互，支持多人互动语音聊天，以及混音、混响等声音特效功能。适合在线狼人杀、在线语音直播等社交类场景。
 - **双人通话**：1v1视频通话，配合 [Web IM SDK](https://cloud.tencent.com/document/product/269/37411) 可以实现在线问诊，在线客服等需要面对面交流的沟通场景。
 - **多人会议**：支持多路视频通话、大小画面和屏幕分享等围绕视频会议相关的高级功能，适用于远程培训、在线教育等场景。
 
![](https://web.sdk.qcloud.com/trtc/miniapp/doc/zh-cn/6517a8a927130474927628457cdc27bee.jpeg)

## 环境要求
- 微信 App iOS 最低版本要求：7.0.9。
- 微信 App Android 最低版本要求：7.0.8。
- 小程序基础库最低版本要求：2.10.0。
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。
- 由于小程序测试号不具备 &lt;live-pusher&gt; 和 &lt;live-player&gt; 的使用权限，需要申请常规小程序账号进行开发。
- 不支持 uniapp 开发环境，请使用原生小程序开发环境。

## 前提条件
1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. **开通小程序类目与推拉流标签权限（如不开通则无法正常使用）**。
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
 - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
 - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
 - 符合类目要求的小程序，需要在【[微信公众平台](https://mp.weixin.qq.com)】>【开发】>【开发管理】>【接口设置】中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/dc6d3c9102bd81443cb27b9810c8e981.png)

## 操作步骤
[](id:step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【新建应用】输入应用名称，例如 `TestTRTC`；若您已创建应用可单击【选择已有应用】。
3. 根据实际业务需求添加或编辑标签，单击【创建】。
![](https://main.qcloudimg.com/raw/f04d288ed091c98a5e8056eb86fb49e8.png)
>?
>- 应用名称只能包含数字、中英文字符和下划线，长度不能超过15个字符。
>- 标签用于标识和组织您在腾讯云的各种资源。例如：企业可能有多个业务部门，每个部门有1个或多个 TRTC 应用，这时，企业可以通过给 TRTC 应用添加标签来标记部门信息。标签并非必选项，您可根据实际业务需求添加或编辑。

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 Demo 源码。
2. 下载完成后，单击【已下载，下一步】。
![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `./debug/GenerateTestUserSig.js` 文件。
3. 设置 `GenerateTestUserSig.js` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
  <img src="https://main.qcloudimg.com/raw/575902219de19b4f2d4595673fa755d4.png">
4. 粘贴完成后，单击【已复制粘贴，下一步】即创建成功。
5. 编译完成后，单击【回到控制台概览】即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：编译运行
1. 打开微信开发者工具，选择【小程序】，单击新建图标，选择【导入项目】。
2. 填写您微信小程序的 AppID，单击【导入】。
 >!此处应输入您微信小程序的 AppID，而非 SDKAppID。
 >
![](https://main.qcloudimg.com/raw/a06f3651a1399eabaa802a607b9a9cf8.png) 
3. 单击【预览】，生成二维码，通过手机微信扫码二维码即可进入小程序。

>! 
>- 小程序 &lt;live-player&gt; 和 &lt;live-pusher&gt; 标签需要在手机微信上才能使用，微信开发者工具上无法使用。
>- 为了小程序能够使用腾讯云房间管理服务，您需要在手机微信上开启调试功能：手机微信扫码二维码后，单击右上角【...】>【打开调试】。
![](https://main.qcloudimg.com/raw/ba85130b18cac0f713994a3a5feb2e83.png)

[](id:online)
## 上线/部署到正式环境
- 请申请域名并做备案。
- 请将服务端代码部署到申请的服务器上。
- 请将以下域名配置到小程序控制台 request 合法域名里：
<table>
<tr><th>域名</th><th>说明</th></tr>
<tr>
<td><code>https://cloud.tencent.com</code></td>
<td>推流域名</td>
</tr><tr>
<td><code>https://yun.tim.qq.com</code></td>
<td>业务域名</td>
</tr></table>


## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，该如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法 ECDSA-SHA256](https://cloud.tencent.com/document/product/647/17275#Old)，如已升级，您按需切换为新旧算法。

升级/切换操作：
 1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
 2. 在左侧导航栏选择【应用管理】，单击目标应用所在行的【应用信息】。
 3. 选择【快速上手】页签，单击【第二步 获取签发UserSig的密钥】区域的【点此升级】、【非对称式加密】或【HMAC-SHA256】。
  - 升级：
![](https://main.qcloudimg.com/raw/6d09db9663d8ca6b46f2ae3ab95cfa4b.png)
  - 切换回老版本算法 ECDSA-SHA256：
![](https://main.qcloudimg.com/raw/786e763bcc67ea982ecae1aa16035c40.png)
  - 切换为新版本算法 HMAC-SHA256：
![](https://main.qcloudimg.com/raw/23e06303e03c277ed3c5824e9e15ab75.png)

### 2. 防火墙有什么限制？

由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参见 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。
