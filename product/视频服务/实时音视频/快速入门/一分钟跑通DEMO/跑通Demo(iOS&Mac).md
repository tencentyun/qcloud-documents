本文主要介绍如何快速运行腾讯云 TRTC Demo（iOS&Mac）。

## 环境要求
- Xcode 11.0及以上版本
- 请确保您的项目已设置有效的开发者签名

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
<span id="step1"></span>
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如`TestTRTC`，单击【创建应用】。

<span id="step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至对应卡片，下载相关 SDK 及配套的 Demo 源码。
 - **iOS：**单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/iOS)】跳转至 Github（或单击【[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_iOS_latest.zip?_ga=1.195966252.185644906.1567570704)】）
  ![](https://main.qcloudimg.com/raw/716b5af9207ad2b11835dec4e2d15da0.png)
 - **Mac：**单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/Mac)】跳转至 Github（或单击【[ZIP](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Mac_latest.tar.bz2?_ga=1.195966252.185644906.1567570704)】）
  ![](https://main.qcloudimg.com/raw/65b9538a23789b1a728674ea3646062c.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。

<span id="step3"></span>
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#step2) 中下载的源码包。
2. 找到并打开`GenerateTestUserSig.h`文件：
 <table><tr>
      <th nowrap="nowrap">适用平台</th>
      <th nowrap="nowrap">文件相对路径</th>
  </tr>
<tr>
      <td>iOS</td>
<td>iOS/TRTCScenesDemo/TRTCScenesDemo/debug/GenerateTestUserSig.h</td>
  </tr>
<tr>
    <td>Mac</td>
    <td>Mac/TRTCScenesDemo/TRTCDemo/TRTC/GenerateTestUserSig.h</td>
  </tr></table>
3. 设置`GenerateTestUserSig.h`文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
	<img src="https://main.qcloudimg.com/raw/15d986c5f4bc340e555630a070b90d63.png">
4. 返回实时音视频控制台，单击【粘贴完成，下一步】。
5. 单击【关闭指引，进入控制台管理应用】。

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：编译运行
1. 在终端窗口进入 TRTCSDK iOS/Mac Demo Podfile 文件所在目录。
2. 执行`pod install`命令安装 TRTC SDK，或者执行`pod update`命令，更新本地库版本。
3. 使用 XCode（11.0及以上的版本）打开源码目录下的 TRTCDemo.xcworkspace 工程，编译并运行 Demo 工程即可。

## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法 ECDSA-SHA256](https://cloud.tencent.com/document/product/647/17275#.E8.80.81.E7.89.88.E6.9C.AC.E7.AE.97.E6.B3.95)，如已升级，您按需切换为新旧算法。

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

### 2. 两台手机同时运行 Demo，为什么看不到彼此的画面？
请确保两台手机在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个终端同时使用。
![](https://main.qcloudimg.com/raw/c7b1589e1a637cf502c6728f3c3c4f99.png)

### 3. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。
