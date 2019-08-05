本文主要介绍如何快速地将腾讯云 TRTC Demo 运行起来，您只需参考如下步骤依次执行即可。

## 1. 创建新的应用
进入腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 创建一个新的应用，获得 SDKAppID，SDKAppID 是腾讯云后台用来区分不同实时音视频应用的唯一标识，在第4步中会用到。
![](https://main.qcloudimg.com/raw/b9d211494b6ec8fcea765d1518b228a1.png)

接下来，点击应用进入**快速上手**页面，参考页面上指引的“第一步”、“第二步”和“第三步”操作，即可快速跑通 Demo。

## 2. 下载 SDK+Demo 源码
“快速上手”页面中第一步里的几个链接地址分别为各个平台的 SDK 和 Demo 源码，点击会跳转到 Github 上，如果您当前网络访问 Github 太慢，可以在项目首页中找到镜像下载地址。

![](https://main.qcloudimg.com/raw/d56b4e4434da42d1a3b8e3540cf6718e.png)

## 3. 查看并拷贝加密密钥
点击**查看密钥**按钮，即可看到用于计算 UserSig 的加密密钥，点击“复制密钥”按钮，可以将密钥拷贝到剪贴板中。

![](https://main.qcloudimg.com/raw/5843542ec2e0446d326d7d44f96a5ec0.png)

<h2 id="CopyKey"> 4. 粘贴密钥到Demo工程的指定文件中 </h2>
我们在各个平台的 Demo 的源码工程中都提供了一个叫做 “GenerateTestUserSig” 的文件，它可以通过 HMAC-SHA256 算法本地计算出 UserSig，用于快速跑通 Demo。您只需要将第1步中获得的 SDKAppID 和第3步中获得的加密密钥拷贝到文件中的指定位置即可，如下所示：

![](https://main.qcloudimg.com/raw/9275a5f99bf00467eac6c34f6ddd3ca5.jpg)

## 5. 开通小程序类目与推拉流标签权限
出于政策和合规的考虑，微信暂时没有放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：

- 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
- 小程序推拉流标签使用权限暂时只开放给有限[类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
- 符合类目要求的小程序，需要在【微信公众平台】-【开发】-【接口设置】中自助开通该组件权限，如下图所示：

![](https://main.qcloudimg.com/raw/cabb6b98121754b7956bd02029714616.jpg)

## 6. 编译运行
6.1. 打开微信开发者工具后，选择【小程序】菜单栏，然后单击新建图标，选择【导入项目】。
6.2. 输入小程序 AppID（注意：不是上面的 SDKAppID），单击【导入】：
![](https://main.qcloudimg.com/raw/b4eefa2896672e132f827fea79a2608b.jpg)
6.3. 单击【预览】，生成二维码，通过手机微信扫码二维码即可进入小程序。

>! 
>- 小程序 &lt;live-player&gt; 和 &lt;live-pusher&gt; 标签需要在手机微信上才能使用，微信开发者工具上无法使用。
>- 为了小程序能够使用腾讯云房间管理服务，您需要在手机微信上开启调试功能：手机微信扫码二维码后，单击右上角【...】>【打开调试】。
![](https://main.qcloudimg.com/raw/79a3773337d34682b5f84f5694cd0290.jpg)

## 7. 发布上线
关于小程序的发布流程，请参见 [小程序发布上线](https://developers.weixin.qq.com/miniprogram/dev/quickstart/basic/release.html#%E5%8F%91%E5%B8%83%E4%B8%8A%E7%BA%BF)。

在小程序发布上线前，请务必要在微信小程序控制台的【开发】>【开发设置】>[【服务器域名】](https://mp.weixin.qq.com/wxopen/devprofile?action=get_profile&token=1269878219&lang=zh_CN)中配置“request 合法域名”，否则将无法使用腾讯云的房间管理服务。需要配置的域名包括：

| 域名 | 说明 | 
|:-------:|---------|
|`https://official.opensso.tencent-cloud.com` | WebRTC音视频鉴权服务域名 | 
|`https://yun.tim.qq.com` | WebRTC音视频鉴权服务域名 | 
|`https://cloud.tencent.com`| 推流域名 | 
|`https://webim.tim.qq.com` | IM域名 | 

![](https://main.qcloudimg.com/raw/7ffe4227bcac149f30c61a7d28808c14.jpg)

## 常见问题
### 1. 开发和运行环境要求
- 微信 App iOS 最低版本要求：6.5.21。
- 微信 App Android 最低版本要求：6.5.19。
- 小程序基础库最低版本要求：1.7.0。
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。

### 2. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。

### 3. 调试时为什么要开启调试模式？
开启调试可以跳过把这些域名加入小程序白名单的工作，否则可能会遇到登录失败，通话无法连接的问题。
