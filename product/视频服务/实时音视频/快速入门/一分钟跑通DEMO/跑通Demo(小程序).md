 本文主要介绍如何快速跑通微信小程序版本的 TRTC Demo，您可以从 [Github](https://github.com/tencentyun/TRTCSDK) 上的 WXMini 目录下获取相关代码。Demo 中前三个功能项演示了三个不同的应用场景：
 
 - 语音聊天室：纯语音交互，支持多人互动语音聊天，以及混音、混响等声音特效功能。适合在线狼人杀、在线语音直播等社交类场景。
 - 双人通话：1v1视频通话，配合 [Web IM SDK](https://cloud.tencent.com/document/product/269/37411) 可以实现在线问诊，在线客服等需要面对面交流的沟通场景。
 - 多人会议：支持多路视频通话、大小画面和屏幕分享等围绕视频会议相关的高级功能，适用于远程培训、在线教育等场景。
 
![](https://main.qcloudimg.com/raw/6517a8a927130474927628457cdc27be.jpg)

## 环境要求

- 微信 App iOS 最低版本要求：7.0.9
- 微信 App Android 最低版本要求：7.0.8
- 小程序基础库最低版本要求：2.10.0
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
<span id="step1"></span>
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如`TestTRTC`，单击【创建应用】。

<span id="step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/WXMini)】跳转至 Github（或单击【[ZIP](https://liteavsdk-1252463788.cosgz.myqcloud.com/TRTC_WXMini_latest.zip)】），下载相关 SDK 及配套的 Demo 源码。
 ![](https://main.qcloudimg.com/raw/c7835c66e2650eaa1cbdf97a0bc97033.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。


<span id="step3"></span>
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#step2) 中下载的源码包。
2. 找到并打开`./debug/GenerateTestUserSig.js`文件。
3. 设置`GenerateTestUserSig.js`文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
  <img src="https://main.qcloudimg.com/raw/0ae7a197ad22784384f1b6e111eabb22.png">
4. 返回实时音视频控制台，单击【粘贴完成，下一步】。
5. 单击【关闭指引，进入控制台管理应用】。

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：开通小程序类目与推拉流标签权限
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
- 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
- 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
- 符合类目要求的小程序，需要在【[微信公众平台](https://mp.weixin.qq.com)】>【开发】>【接口设置】中自助开通该组件权限，如下图所示：
 ![](https://main.qcloudimg.com/raw/ad87091aaae2db6ad412136297886c15.png)

### 步骤5：编译运行
1. 打开微信开发者工具，选择【小程序】，单击新建图标，选择【导入项目】。
2. 填写您微信小程序的 AppID，单击【导入】。
 >!此处应输入您微信小程序的 AppID，而非 SDKAppID。
 >
 ![](https://main.qcloudimg.com/raw/b4eefa2896672e132f827fea79a2608b.jpg)   
3. 单击【预览】，生成二维码，通过手机微信扫码二维码即可进入小程序。

>! 
>- 小程序 &lt;live-player&gt; 和 &lt;live-pusher&gt; 标签需要在手机微信上才能使用，微信开发者工具上无法使用。
>- 为了小程序能够使用腾讯云房间管理服务，您需要在手机微信上开启调试功能：手机微信扫码二维码后，单击右上角【...】>【打开调试】。
![](https://main.qcloudimg.com/raw/9ae12892a437c25c2317fb62f7f851ba.png)


## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，该如何获取密钥？
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

### 2. 防火墙有什么限制？

由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。

### 3. 调试时为什么要开启调试模式？

开启调试后，可以略过把“request 合法域名”加入小程序白名单的操作，避免遇到登录失败，通话无法连接的问题。

### 4.为什么出现黑屏/画面卡住？

您可以检查小程序 Demo 左下方的控制面板，打开【调试模式】即可在界面上看到详细的推拉流信息，如果没有推拉流信息则表示未成功进房或 live-pusher，live-player 创建失败。
![](https://main.qcloudimg.com/raw/b370373d41217c2c0efca37ab87cc94a.jpg)


| 参数          | 含义                                                         |
| ------------- | ------------------------------------------------------------ |
| appVersion    | 微信版本号                                                   |
| libVersion    | 基础库版本号                                                 |
| template      | trtc-room 组件的 template                                      |
| debug         | 是否开启推拉流的 debug 信息                                    |
| userID        | 生成的用户 ID                                                 |
| roomID        | 房间号                                                       |
| camera        | 是否开启摄像头                                               |
| mic           | 是否开启麦克风                                               |
| switch camera | 摄像头位置（front / back）                                       |
| Room          | 进房，退房，退房并返回上一界面操作                           |
| user count    | 房间内人数以及 user 信息<br/>userID<br/>mainV：该用户是否有主路视频<br/>mainA：该用户是否有主路音频<br/>auxV：该用户是否有辅路视频 |
| stream count  | 房间内流的数量以及流信息<br/>userID<br/>SubV：是否订阅此路流的视频<br />SubA：是否订阅此路流的音频 |

