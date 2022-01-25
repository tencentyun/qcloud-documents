本文主要介绍如何快速运行腾讯云 IM Demo（Flutter）。

## 环境要求

| 平台 | 版本 | 
|---------|---------|
| Flutter | 2.2.0 及以上版本。 | 
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 帐号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
### 步骤1：创建应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
>同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
![](https://main.qcloudimg.com/raw/78340e403359fcf4d753ade29ae9aace.png)
3. 请保存 SDKAppID 信息。可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、创建时间以及到期时间。
  ![](https://main.qcloudimg.com/raw/ed34d9294a485d8d06b3bb7e0cc5ae59.png)
4. 单击创建后的应用，左侧导航栏单击**辅助工具**>**UserSig 生成&校验**，创建一个 UserID 及其对应的 UserSig，复制签名信息，后续登录使用。
![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

[](id:step2)
### 步骤2：下载 SDK 与源码
1. 根据您的实际业务需求，下载 SDK 及配套的 [Demo 源码](https://github.com/tencentyun/TIMSDK/tree/master/Flutter/Demo/im_discuss)。
2. 下载完成进入目录：TIMSDK/Flutter/Demo/im_discuss
![](https://qcloudimg.tencent-cloud.cn/raw/8b865854e14e8848b4e8d31d8daf55ac.png)
3. Flutter pub get 安装依赖，启动 Demo 项目，在命令行中输入：
<dx-codeblock>
:::  plaintext
flutter run --dart-define=SDK_APPID=xxxx --dart-define=ISPRODUCT_ENV=false --dart-define=KEY=xxxx
:::
</dx-codeblock>
>?
>-  `--dart-define=SDK_APPID=xxxx`其中`xxxx`需替换成替换成 [步骤1](#step1) 中您创建的 SDKAppID。
>- `--dart-define=ISPRODUCT_ENV=false` 对开发生产环境做判断，如您是开发环境请标 false。
>-  `--dart-define=KEY=xxxx` 其中`xxxx`需替换成 [步骤1](#step1) 中的密钥信息。
4. Visual Studio 配置 launch.json 启动。
![](https://qcloudimg.tencent-cloud.cn/raw/e495955902c8a594085aa045891ffe2a.png)


### 步骤3（可选）：使用 IDE 运行调试
<dx-tabs>
::: Android 平台[](id:android)
1. 在 Android Studio 打开 discuss/andorid 目录。
![](https://comm.qq.com/imsdk/im-flutter-plugin-doc/doc_04.png)
2. 启动一个 Android 的模拟器，单击 **Build And Run**，Demo 可以运行起来。您可以随机输入一个 UserID（数字字母组合）。
>?UI 可能会有部分调整更新，请以最新版为准。
:::
::: iOS 平台[](id:ios)
1. 打开 Xcode，打开文件 discuss/ios/Runner.xcodeproj：
![](https://comm.qq.com/imsdk/im-flutter-plugin-doc/doc_05.png)
2. 连接 iPhone 真机，单击 **Build And Run**，iOS 工程等待编译完成，会有新窗口弹出 Xcode 工程。
3. 打开 iOS 工程，设置主 Target 的 Signing & Capabilities（需要苹果开发者帐号），让项目可以在 iPhone 真机上运行。
4. 启动项目，在真机上进行 Demo 的调试。
![](https://comm.qq.com/imsdk/im-flutter-plugin-doc/doc_06.png)
:::
</dx-tabs>

## 常见问题

### 支持哪些平台？
目前支持 iOS 、Android 和 Web 三个平台，另外 Windows 和 Mac 版正在开发中，敬请期待。

### Android 单击 Build And Run 报错找不到可用设备？
确保设备没被其他资源占用，或单击 **Build** 生成 APK 包，再拖动进模拟器里运行。

### iOS 第一次运行报错？
按照上面的 Demo 运行配置后，如果报错，可以单击**Product**>**Clean**，清除产物后重新 Build，或者关闭 Xcode 重新打开再次 Build。

### Flutter 环境问题
如您需得知 Flutter 的环境是否存在问题，请运行 Flutter doctor 检测 Flutter 环境是否装好。

