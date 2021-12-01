本文主要介绍如何快速运行腾讯云 IM Demo（Unity）。

## 环境要求

| 平台 | 版本 | 
|---------|---------|
| Unity | 2019.4.15f1 及以上版本。 | 
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。|

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 帐号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
## 步骤1：创建应用
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
## 步骤2：下载 SDK 与源码
1. 根据您的实际业务需求，下载 SDK 及配套的 [Demo 源码](https://cloud.tencent.com/document/product/269/36887)。
2. 下载完成后，双击打开 Package，默认全选并导入包资源到当前 Unity 项目。
![](https://main.qcloudimg.com/raw/c338ce838fff81841f85b06fd3dc5c6c.png)
3. 打开源码 Assets/TIMCloud/Demo/ExampleEntry.cs，把 [步骤1](#step1) 获取的 SDKAppID，UserID，UserSig 填入下图红框内，把 Config.key 所在行注释掉。
![](https://main.qcloudimg.com/raw/e31692ae98503221f45ece41039ead92.png)
4. ExampleEntry.cs 注释动态获取 userSig 逻辑（由于动态获取的配置稍微复杂，后续需要可以单独配置）。
![](https://main.qcloudimg.com/raw/7a8ac734ac60a73caf6139fc0d1d250f.png)

## 步骤3：打包运行
### Android 平台
1. 配置 Unity Editor，单击**File**>**Build Setting**，切换至 Android。
![](https://main.qcloudimg.com/raw/d913d32e36aa01ff93acf0316d4f103f.png)
2. 启动一个 Android 的模拟器，单击 **Build And Run**，Demo 就能跑起来。

>- Demo 里面包含了已上线的所有 API，可以测试和作为调用参考，API 文档参见 [SDK API（Unity）](https://cloud.tencent.com/document/product/269/54111)。
> - UI 可能会有部分调整更新，请以最新版为准。
>
![](https://main.qcloudimg.com/raw/e6f3583d0b807af62a27ee753cfa3b53.png)
3. 接口测试，需要先在第一行第二个输入框里添加 UserID，然后调用 initSDK 和 login，数据展示窗口显示调用成功，然后基本上接口都可以尝试调用。

### iOS 平台
1. 配置 Unity Editor，单击**File**>**Build Setting**，切换至 iOS。
![](https://main.qcloudimg.com/raw/3982b96c4f9e76107bb4aadac33a5de5.png)
2. 连接 iPhone 真机，单击**Build And Run**，需要选择一个新的目录存放编译出来的 iOS 工程，等待编译完成，会有新窗口弹出 Xcode 工程。
3. 打开 iOS 工程，设置主 Target 的 Signing & Capabilities（需要苹果开发者帐号），让项目可以在 iPhone 真机上运行。
4. 启动项目，在真机上进行 Demo 的调试。

## 常见问题

### 支持哪些平台？
目前支持 iOS 和 Android 两个平台，另外 Windows 和 Mac 版正在开发中，敬请期待。

### Android 单击 Build And Run 报错找不到可用设备？
确保设备没被其他资源占用，或单击 Build 生成 apk 包，再拖动进模拟器里运行。

### iOS 第一次运行报错？
按照上面的 Demo 运行配置后，如果报错，可以单击**Product**>**Clean**，清除产物后重新 Build，或者关闭 Xcode 重新打开再次 Build。
### 2019.04版 Unity，iOS 平台报错？
Library/PackageCache/com.unity.collab-proxy@1.3.9/Editor/UserInterface/Bootstrap.cs(23,20): error CS0117: 'Collab' does not contain a definition for 'ShowChangesWindow'
在 Editor 工具栏单击**Window**>**Package Manager**，将 Unity Collaborate 降级到1.2.16。

### 2019.04版 Unity，iOS 平台报错？
Library/PackageCache/com.unity.textmeshpro@3.0.1/Scripts/Editor/TMP_PackageUtilities.cs(453,84): error CS0103: The name 'VersionControlSettings' does not exist in the current context
打开源码，把`|| VersionControlSettings.mode != "Visible Meta Files"`这部分代码删除即可。
