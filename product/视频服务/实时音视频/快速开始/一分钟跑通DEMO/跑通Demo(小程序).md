本文主要介绍如何快速运行腾讯云 TRTC Demo（Web）。

## 环境要求
- 微信 App iOS 最低版本要求：6.5.21
- 微信 App Android 最低版本要求：6.5.19
- 小程序基础库最低版本要求：1.7.0
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。


## 操作步骤
<span id="step1"></span>
### 步骤1：创建新的应用
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/rav) ，单击【创建应用】。
  如果您已有应用，请记录其 SDKAppID 然后直接 [下载 SDK 和 Demo 源码](#step2)。否则，继续执行下一步。
2. 填写新建应用的应用名称等信息，单击【确定】。
  应用创建完成后，自动生成一个应用标识 SDKAppID，请记录 SDKAppID 信息。
![](https://main.qcloudimg.com/raw/1acc030cfc47e32bc36873c9a494b88a.png)

<span id="step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 单击应用卡片，进入【快速上手】页面。
2. 单击【第一步 下载SDK+配套demo源码】区域的【小程序】跳转至 [Github](https://github.com/tencentyun/TRTCSDK)（或直接访问 [Gitee](https://gitee.com/cloudtencent/TRTCSDK)），下载相关 SDK 和 Demo 源码。
![](https://main.qcloudimg.com/raw/486d7696aeb29e457bd654b5936a56e2.png)

<span id="step3"></span>
### 步骤3：查看并拷贝加密密钥
1. 单击【第二步 获取签发UserSig的密钥】区域的【查看密钥】，即可获取用于计算 UserSig 的加密密钥。
2. 单击【复制密钥】，将密钥拷贝到剪贴板中。
 ![](https://main.qcloudimg.com/raw/d0b780f7b28833533e12807d1b11d8be.png)

<h3 id="CopyKey">步骤4：配置 Demo 工程文件</h3>
 Demo 源码工程中的`GenerateTestUserSig.js`文件可以通过 HMAC-SHA256 算法在本地计算 UserSig，用于快速跑通 Demo。
 
1. 解压 [步骤2](#step2) 中下载的源码包。
2. 找到并打开 `WXMini/pages/webrtc-room/debug/GenerateTestUserSig.js`文件。
3. 设置`GenerateTestUserSig.js`文件中的相关参数：
  - SDKAPPID：请设置为 [步骤1](#step1) 中获取的实际 SDKAppID。
  - SECRETKEY：请设置为 [步骤3](#step3) 中获取的实际密钥信息。
  ![](https://main.qcloudimg.com/raw/c523de56afa69a7309872cbcfd75445f.png)

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤5：开通小程序类目与推拉流标签权限
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
- 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
- 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
- 符合类目要求的小程序，需要在【微信公众平台】>【开发】>【接口设置】中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/cabb6b98121754b7956bd02029714616.jpg)

### 步骤6：编译运行
1. 打开微信开发者工具，选择【小程序】，单击新建图标，选择【导入项目】。
2. 填写您微信小程序的 AppID，单击【导入】。
 >!此处应输入您微信小程序的 AppID，而非 SDKAppID。
 >
 ![](https://main.qcloudimg.com/raw/b4eefa2896672e132f827fea79a2608b.jpg)
3. 单击【预览】，生成二维码，通过手机微信扫码二维码即可进入小程序。

>! 
>- 小程序 &lt;live-player&gt; 和 &lt;live-pusher&gt; 标签需要在手机微信上才能使用，微信开发者工具上无法使用。
>- 为了小程序能够使用腾讯云房间管理服务，您需要在手机微信上开启调试功能：手机微信扫码二维码后，单击右上角【...】>【打开调试】。
![](https://main.qcloudimg.com/raw/79a3773337d34682b5f84f5694cd0290.jpg)

### 步骤7：发布上线
1. 打开微信小程序控制台，选择【开发】>【开发设置】>【[服务器域名](https://mp.weixin.qq.com/wxopen/devprofile?action=get_profile&token=1269878219&lang=zh_CN)】中配置“request 合法域名”，否则将无法使用腾讯云的房间管理服务。需要配置的域名如下表所示：
<table>
     <tr>
         <th nowrap="nowrap">域名</th>  
         <th>说明</th>  
     </tr>
	 <tr>      
         <td>https://official.opensso.tencent-cloud.com</td>    
	      <td>WebRTC 音视频鉴权服务域名</td>   
     </tr> 
	 <tr>
	     <td>https://yun.tim.qq.com</td>   
	     <td>WebRTC 音视频鉴权服务域名</td>   
     </tr> 
	 <tr>      
	     <td>https://cloud.tencent.com</td>   
	     <td>推流域名</td>   
     </tr> 
		 	 <tr>      
	     <td>https://webim.tim.qq.com</td>   
	     <td>IM 域名</td>   
     </tr> 
</table>

 ![](https://main.qcloudimg.com/raw/7ffe4227bcac149f30c61a7d28808c14.jpg)

2. 发布微信小程序，具体发布流程请参见 [小程序发布上线](https://developers.weixin.qq.com/miniprogram/dev/quickstart/basic/release.html#%E5%8F%91%E5%B8%83%E4%B8%8A%E7%BA%BF)。

## 常见问题
### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先单击【第二步 获取签发UserSig的密钥】区域的【点此升级】升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法](https://cloud.tencent.com/document/product/647/17275?!preview&!editLang=zh#.E8.80.81.E7.89.88.E6.9C.AC.E7.AE.97.E6.B3.95) ECDSA-SHA256。

### 2. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。

### 3. 调试时为什么要开启调试模式？
开启调试后，可以略过把“request 合法域名”加入小程序白名单的操作，避免遇到登录失败，通话无法连接的问题。
