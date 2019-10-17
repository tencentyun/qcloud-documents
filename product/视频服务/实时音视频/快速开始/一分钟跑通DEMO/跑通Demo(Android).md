本文主要介绍如何快速运行腾讯云 TRTC Demo（Android）。

## 环境要求
- 最低兼容 Android 4.1（SDK API Level 16），建议使用 Android 5.0 （SDK API Level 21）及以上版本
- Android Studio 2.0 及以上版本
- App 要求 Android 4.1 及以上设备

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
<span id="step1"></span>
### 步骤1：创建新的应用
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)。
 - 若是首次登录，直接单击【立即开始】。
  ![](https://main.qcloudimg.com/raw/063eb714daa9ab9076b20663bd4c78b7.png)
 - 否则需先单击【+创建应用并跑通Demo】，再点击【立即开始】。
  ![](https://main.qcloudimg.com/raw/fb5ca0967f09d4970b2dc610f17d5b2c.png)
2. 输入应用名称，单击【创建应用】。
 ![](https://main.qcloudimg.com/raw/da7b1535b37c4d0b3e63ce49598149fe.png)

<span id="step2"></span>
### 步骤2：下载 SDK 和 Demo 源码
1. 鼠标移动至 Android 卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK)】跳转至 Github（或单击【[ZIP](https://gitee.com/cloudtencent/TRTCSDK)】），下载相关 SDK 及配套的 Demo 源码。
  ![](https://main.qcloudimg.com/raw/363243119b9faf74f8585ee08d01e5a9.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】。

<span id="step3"></span>
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤3](#step2) 中下载的源码包，找到并打开`Android/TRTCDemo/app/src/main/java/com/tencent/liteav/demo/trtc/debug/GenerateTestUserSig.java`文件，配置下列参数：
  - SDKAPPID：设置为对应的 **SDKAppID**。
  - SECRETKEY：设置为对应的**密钥**。
  ![](https://main.qcloudimg.com/raw/7f1c7345b4019984553fae9480fde461.png)
2. 返回实时音视频控制台，单击【粘贴完成，下一步】。
3. 单击【关闭指引，进入控制台管理应用】。

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：编译运行
使用 Android Studio（3.2 以上的版本）打开源码工程`TRTCDemo`，单击【运行】即可。

## 常见问题

### 1. 两台手机同时运行 Demo，为什么看不到彼此的画面？
请确保两台手机在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个终端同时使用。
![](https://main.qcloudimg.com/raw/c7b1589e1a637cf502c6728f3c3c4f99.png)

### 2. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以在对 UDP 有拦截的办公网络下无法使用。如遇到类似问题，请参考 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399) 排查并解决。
