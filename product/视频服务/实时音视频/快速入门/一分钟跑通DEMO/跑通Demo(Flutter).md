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
2. 单击【立即开始】，输入应用名称，例如 `TestTRTC`，单击【创建应用】。

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 单击【[Github](https://github.com/c1avie/trtc_demo)】跳转至 Github，下载相关 SDK 及配套的 Demo 源码。
![](https://main.qcloudimg.com/raw/7a4343e8004f1a459637267aa934db13.png)
2. 下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。


[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 解压 [步骤2](#step2) 中下载的源码包。
2. 找到并打开 `/lib/debug/GenerateTestUserSig.dart` 文件。
3. 设置 `GenerateTestUserSig.java` 文件中的相关参数：
<ul><li/>SDKAPPID：默认为 PLACEHOLDER ，请设置为实际的 SDKAppID。
	</li>SECRETKEY：默认为 PLACEHOLDER ，请设置为实际的密钥信息。
<img src="https://main.qcloudimg.com/raw/8933718aafec140c01ea5bae0bf8cace.png"/>
4. 返回实时音视频控制台，单击【粘贴完成，下一步】。
5. 单击【关闭指引，进入控制台管理应用】。

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



