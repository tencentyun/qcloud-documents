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
我们在各个平台的 Demo 的源码工程中都提供了一个叫做 “GenerateTestUserSig” 的文件，它可以通过 HMAC-SHA256 算法本地计算出 UserSig，用于快速跑通 Demo。

| 语言版本 |  适用平台 | GenerateTestUserSig 的源码位置 |
|:---------:|:---------:|:---------:|
| Objective-C | iOS  | [Github](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/TRTCDemo/TRTC/GenerateTestUserSig.h)|
| Objective-C | Mac  | [Github](https://github.com/tencentyun/TRTCSDK/tree/master/Mac/TRTCDemo/TRTC/GenerateTestUserSig.h)|
| Java | Android  | [Github](https://github.com/tencentyun/TRTCSDK/tree/master/Android/TRTCDemo/app/src/main/java/com/tencent/liteav/demo/trtc/debug/GenerateTestUserSig.java) |
| C++ | Windows | [Github](https://github.com/tencentyun/TRTCSDK/tree/master/Windows/DuilibDemo/GenerateTestUserSig.h)|
| C# | Windows | [Github](https://github.com/tencentyun/TRTCSDK/tree/master/Windows/CSharpDemo/GenerateTestUserSig.cs)|
| Javascript | Web | [Github](https://github.com/tencentyun/TRTCSDK/tree/master/H5/js/debug/GenerateTestUserSig.js)|
| Javascript | 微信小程序 | [Github](https://github.com/tencentyun/TRTCSDK/tree/master/WXMini/pages/webrtc-room/debug/GenerateTestUserSig.js)|


您只需要将第1步中获得的 SDKAppID 和第3步中获得的加密密钥拷贝到文件中的指定位置即可，如下所示：

![](https://main.qcloudimg.com/raw/de28c1eb03e779ddb7131dc2d666d8d2.jpg)

> !安全警告：本地计算 UserSig 的做法虽然能够工作，但仅适合于调试 Demo 的场景，不适用于线上产品。
> 
> 这是因为客户端代码中的 SECRETKEY 很容易被反编译逆向破解，尤其是 Web 端的代码被破解的难度几乎为零。一旦您的密钥泄露，攻击者就可以计算出正确的 UserSig 来盗用您的腾讯云流量。
> 
> [安全方案](https://cloud.tencent.com/document/product/647/17275#Server)：将 UserSig 的计算代码和加密密钥放在您的业务服务器上，然后由 App 按需向您的服务器获取实时算出的 UserSig。由于攻破服务器的成本要远高于破解客户端 App，所以服务器计算的方案能够更好地保护您的加密密钥。

## 5. 编译运行
使用 XCode （9.0 以上的版本） 打开源码目录下的 TRTCDemo.xcodeproj 工程，编译并运行 Demo 工程即可。

## 常见问题

### 1. 开发环境有什么要求？
- Xcode 9.0+
- 请确保您的项目已设置有效的开发者签名。

### 2. 两台手机运行 Demo，为什么看不到彼此的画面？
请确保两台手机在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个终端同时使用。
![](https://main.qcloudimg.com/raw/c7b1589e1a637cf502c6728f3c3c4f99.png)

### 3. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。
