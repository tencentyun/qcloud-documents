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

## 5. 编译运行
使用 Chrome 浏览器打开 Demo 根目录下的 **index.html** 即可运行 Demo。由于 WebRTC 需要使用摄像头和麦克风采集，所以在体验过程中您可能会收到来自 Chrome 浏览器的如下提示，点击“允许”即可。
![](https://main.qcloudimg.com/raw/970dde95f01c45c6721ceadf5bae3831.jpg)

## 常见问题

### 1. 开发环境有什么要求？
请使用最新版本的 Chrome 浏览器。

### 2. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。
