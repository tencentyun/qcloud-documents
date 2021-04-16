本文主要介绍如何快速运行腾讯云 TRTC Demo（Flutter）。

## 环境要求
- Flutter 1.12 及以上版本。
- Android 端开发：
  -  Android Studio 3.5及以上版本。
  -  App 要求 Android 4.1及以上版本设备。
- iOS 端开发：
  - Xcode 11.0及以上版本。
  - 请确保您的项目已设置有效的开发者签名。

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

[](id:step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 输入应用名称，例如 TestTRTC，单击【创建】。
![](https://main.qcloudimg.com/raw/9b2db43594f4744b42ef74c94494ea8e.png)

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 Demo 源码。
2. 下载完成后，单击【已下载，下一步】。
![](https://main.qcloudimg.com/raw/3b115019ddfd0866108ed1add30810d8.png)


[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `/example/lib/debug/GenerateTestUserSig.dart` 文件。
3. 设置 `GenerateTestUserSig.dart` 文件中的相关参数：
<ul><li/>SDKAPPID：默认为 PLACEHOLDER ，请设置为实际的 SDKAppID。
	<li/>SECRETKEY：默认为 PLACEHOLDER ，请设置为实际的密钥信息。</ul>
	<img src="https://main.qcloudimg.com/raw/31b265429e66a899acccb875a8c17ad6.png"/>
4. 粘贴完成后，单击【已复制粘贴，下一步】即创建成功。
5. 编译完成后，单击【回到控制台概览】即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：编译运行
1. 执行 `flutter pub get`。
2. 编译运行调试：
<dx-tabs>
:::  Android端
1. 执行 `flutter run`。
2. 使用 Android Studio（3.5及以上的版本）打开源码工程。
3. 单击【运行】即可。
:::
::: iOS端
1. 使用 XCode（11.0及以上的版本）打开源码目录下的 `/ios工程`。
2. 编译并运行 Demo 工程即可。
:::
</dx-tabs>



## 常见问题

- [两台手机同时运行 Demo，为什么看不到彼此的画面？](https://cloud.tencent.com/document/product/647/51623#que1)
- [防火墙有什么限制？](https://cloud.tencent.com/document/product/647/51623#que2)
- [iOS 打包运行 Crash？](https://cloud.tencent.com/document/product/647/51623#que3)
- [iOS 无法显示视频（Android 正常）？](https://cloud.tencent.com/document/product/647/51623#que4)
- [更新 SDK 版本后，iOS CocoaPods 运行报错？](https://cloud.tencent.com/document/product/647/51623#que5)
- [Android Manifest merge failed 编译失败？](https://cloud.tencent.com/document/product/647/51623#que6)
- [因为没有签名，真机调试报错?](https://cloud.tencent.com/document/product/647/51623#que7)
- [对插件内的 swift 文件做了增删后，build 时查找不到对应文件？](https://cloud.tencent.com/document/product/647/51623#que8)
- [Run 报错“Info.plit, error: No value at that key path or invalid key path: NSBonjourServices”？](https://cloud.tencent.com/document/product/647/51623#que9)
- [Pod install 报错？](https://cloud.tencent.com/document/product/647/51623#que10)
- [Run 的时候 iOS 版本依赖报错？](https://cloud.tencent.com/document/product/647/51623#que11)



