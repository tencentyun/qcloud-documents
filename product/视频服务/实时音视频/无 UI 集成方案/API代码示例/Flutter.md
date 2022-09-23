本文主要介绍如何快速运行腾讯云 TRTC Demo（Flutter）。

>! 目前 Windows/MacOs 端暂不支持屏幕分享及设备选择功能。

## 环境要求
- Flutter 2.0 及以上版本。
- **Android 端开发：**
  - Android Studio 3.5及以上版本。
  - App 要求 Android 4.1及以上版本设备。
- **iOS & macOS 端开发：**
  - Xcode 11.0及以上版本。
  - osx 系统版本要求 10.11 及以上版本
  - 请确保您的项目已设置有效的开发者签名。
- **Windows 开发：**
    - 操作系统：Windows 7 SP1 或更高的版本（基于 x86-64 的 64 位操作系统）。
    - 磁盘空间：除安装 IDE 和一些工具之外还应有至少 1.64 GB 的空间。
    - 安装 [Visual Studio 2019](https://visualstudio.microsoft.com/zh-hans/downloads/)。

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com) 账号，并完成实名认证。

## 操作步骤
[](id:step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择**开发辅助** > [**快速跑通Demo**](https://console.cloud.tencent.com/trtc/quickstart)。
2. 单击**新建应用**输入应用名称，例如 `TestTRTC`；若您已创建应用可单击**选择已有应用**。
3. 根据实际业务需求添加或编辑标签，单击**创建**。
![](https://main.qcloudimg.com/raw/f04d288ed091c98a5e8056eb86fb49e8.png)
>?
>- 应用名称只能包含数字、中英文字符和下划线，长度不能超过15个字符。
>- 标签用于标识和组织您在腾讯云的各种资源。例如：企业可能有多个业务部门，每个部门有1个或多个 TRTC 应用，这时，企业可以通过给 TRTC 应用添加标签来标记部门信息。标签并非必选项，您可根据实际业务需求添加或编辑。

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 [Demo 源码](https://github.com/LiteAVSDK/TRTC_Flutter/tree/master/TRTC-Simple-Demo)。
2. 下载完成后，单击**已下载，下一步**。
![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)


[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `TRTC-Simple-Demo/lib/debug/GenerateTestUserSig.dart` 文件。
3. 设置 `GenerateTestUserSig.dart` 文件中的相关参数：
<ul><li/>SDKAPPID：默认为 PLACEHOLDER ，请设置为实际的 SDKAppID。
	<li/>SECRETKEY：默认为 PLACEHOLDER ，请设置为实际的密钥信息。</ul>
	<img src="https://main.qcloudimg.com/raw/fba60aa9a44a94455fe31b809433cfa4.png"/>
4. 粘贴完成后，单击**已复制粘贴，下一步**即创建成功。
5. 编译完成后，单击**回到控制台概览**即可。

>?
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:step4)
### 步骤4：编译运行
1. 执行 `flutter pub get`。
2. 编译运行调试：
<dx-tabs>
:::  Android 端
1. 执行 `flutter run`。
2. 使用 Android Studio（3.5及以上的版本）打开源码工程，单击**运行**即可。
:::
::: iOS 端
1. 到 iOS 目录 `pod install`。
2. 使用 XCode（11.0及以上的版本）打开源码目录下的 `/ios` 工程，编译并运行 Demo 工程即可。
:::
::: Windows 端
1. 启用 Windows 支持：`flutter config --enable-windows-desktop`。
2. `flutter run -d windows`。
:::
::: macOS 端
1. 启用 macOS 支持：`flutter config --enable-macos-desktop`。
2. 到macos目录 `pod install`。
2. 执行 `flutter run -d macos`。
:::
</dx-tabs>

## 常见问题
### 如何查看 TRTC 日志？
TRTC 的日志默认压缩加密，后缀为 `.xlog`。地址如下：
- **iOS 端**：sandbox 的 `Documents/log`。
- **Android 端**：
	- 6.7及之前的版本：`/sdcard/log/tencent/liteav`。
	- 6.8之后的版本：`/sdcard/Android/data/包名/files/log/tencent/liteav/`。

### iOS 无法显示视频（Android 没问题）？
请确认在您的 info.plist 中，`io.flutter.embedded_views_preview` 是否为 YES。 

### Android Manifest merge failed 编译失败？
请打开 `/example/android/app/src/main/AndroidManifest.xml` 文件。
    
1. 将 `xmlns:tools="http://schemas.android.com/tools"` 加入到 manifest 中。
2. 将 `tools:replace="android:label"` 加入到 application 中。
![图示](https://main.qcloudimg.com/raw/7a37917112831488423c1744f370c883.png)

>? 更多常见问题，请参见 [Flutter 相关问题](https://cloud.tencent.com/document/product/647/51623)。

