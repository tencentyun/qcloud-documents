本文主要介绍如何快速跑通Web版本的 TRTCCalling Demo。
Demo 中包括语音通话和视频通话场景：

 

 \- 语音通话：纯语音交互，支持多人互动语音聊天。

 \- 视频通话：视频通话，面向在线客服等需要面对面交流的沟通场景。

## 环境要求
* 请使用最新版本的 Chrome 浏览器。
* TRTCCalling 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://demo-1252463788.cos.ap-shanghai.myqcloud.com/trtccalling/demo/index.html) 检查配置是否生效。
  - TCP 端口：8687
  - UDP 端口：8000，8080，8800，843，443，16285
  - 域名：qcloud.rtc.qq.com

>! 
>- 一般情况下体验 Demo 需要部署至服务器，通过 https://域名/xxx 访问，或者直接在本地搭建服务器，通过 localhost:端口访问。
>- 目前桌面端 Chrome 浏览器支持 TRTC 桌面浏览器 SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。



## 操作步骤

<span id="step1"></span>

### 步骤1：创建新的应用

1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。

2. 单击【立即开始】，输入应用名称，例如`TestTRTC`，单击【创建应用】。

<span id="step2"></span>

### 步骤2：下载 SDK 和 Demo 源码
2. 鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/Web)】跳转至 Github（或单击【[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/H5_latest.zip?_ga=1.195966252.185644906.1567570704)】），下载相关 SDK 及配套的 Demo 源码。
 ![](https://main.qcloudimg.com/raw/0f35fe3bafe9fcdbd7cc73f991984d1a.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。



<span id="step3"></span>

### 步骤3：配置 Demo 工程文件

1. 解压 [步骤2](#step2) 中下载的源码包。

2. 找到并打开`./public/debug/GenerateTestUserSig.js`文件。

3. 设置`GenerateTestUserSig.js`文件中的相关参数：

  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>

  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 

  <img src="https://main.qcloudimg.com/raw/0ae7a197ad22784384f1b6e111eabb22.png">

4. 返回实时音视频控制台，单击【粘贴完成，下一步】。

5. 单击【关闭指引，进入控制台管理应用】。



>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此****该方法仅适合本地跑通 Demo 和功能调试****。

>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。



### 步骤4：运行 Demo
使用 Chrome 浏览器打开 dist 目录下的 index.html 文件即可运行 Demo。

- Demo 运行界面如图所示：
![](https://main.qcloudimg.com/raw/90118deded971621db7bb14b55073bcc.png)
- 输入用户userid，点击【登录】
![](https://main.qcloudimg.com/raw/f430fb067cddbb52ba32e4d0660cd331.png)
- 输入呼叫用户userid，即可语音或视频通话
![](https://main.qcloudimg.com/raw/72b855b2cde9a171e2719dba255c5713.png)
- 视频通话
![](https://main.qcloudimg.com/raw/99506cf44a7eceb25e7f6238a8d155a8.png)
- 语音通话
![](https://main.qcloudimg.com/raw/3eb67ebd31cc3fb4b1f2a975889806f0.png)



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