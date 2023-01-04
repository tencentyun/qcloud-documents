本文主要介绍如何快速将腾讯云即时通信 IM SDK 集成到您的 Flutter 项目中。

## 环境要求

| 平台 | 版本 |
|---------|---------|
| Flutter | 2.2.0 及以上版本。 |
|Android|Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。|
|iOS|Xcode 11.0及以上版本，真机调试请确保您的项目已设置有效的开发者签名。|

## 支持平台

我们致力于打造一套支持 Flutter 全平台的即时通信 IM SDK 及 TUIKit，帮助您一套代码，全平台运行。

| 平台 | 支持状态|
|---------|---------|
| iOS | 支持 |
| Android | 支持 |
| [Web](#web) | 支持，4.1.1+2版本起 |
| [macOS](#pc) | 支持，4.1.9版本起 |
| [Windows](#pc) | 支持，4.1.9版本起 |
| [混合开发](https://cloud.tencent.com/document/product/269/83153) （将 Flutter SDK 添加至现有原生应用） | 5.0.0版本起支持 |

>? Web/macOS/Windows 平台需要简单的几步额外引入，详情请查看本文 [Web 兼容](#web) 和 [Desktop兼容](#pc) 部分。

## 体验 DEMO

在开始接入前，您可以体验我们的 DEMO，快速了解腾讯云 IM Flutter 跨平台 SDK 及 TUIKit 的能力。

**以下各版本 DEMO，均由同一 Flutter 项目制作打包而成。** Desktop(macOS/Windows)平台，SDK 已支持，DEMO 将于近期上线。

<table style="text-align:center; vertical-align:middle; max-width: 800px">
  <tr>
    <th style="text-align:center;">移动端 APP</th>
    <th style="text-align:center;">WEB - H5</th>
  </tr>
  <tr>
    <td><div style="display: flex; justify-content: center; align-items: center; flex-direction: column; padding-top: 10px">iOS/Android APP，自动判断平台下载<img style="max-width:200px; margin: 20px 0 20px 0" src="https://qcloudimg.tencent-cloud.cn/raw/ca2aaff551410c74fce48008c771b9f6.png"/></div></td>
    <td><div style="display: flex; justify-content: center; align-items: center; flex-direction: column; padding-top: 10px">手机扫码体验在线Web版DEMO<img style="max-width:200px; margin: 20px 0 20px 0" src="https://qcloudimg.tencent-cloud.cn/raw/3c79e8bb16dd0eeab35e894a690e0444.png"/></div></td>
  </tr>
</table>

## 集成 IM SDK

您可以通过 [pub add](https://pub.dev/packages/tencent_cloud_chat_sdk) 的方式直接集成腾讯云 IM SDK（Flutter），或者在 pubspec.yaml 中写入 IM SDK 的方式来集成。

### flutter pub add 安装

在终端窗口中输入如下命令（需要提前安装 Flutter 环境）：

```
flutter pub add tencent_cloud_chat_sdk
```

>?如果您的项目还同时需要用于 [Web](#web) 或 [桌面端(macOS、Windows)](#pc)，一些额外的步骤是需要的，具体请看文末。

### 在 pubspec.yaml 中写入

```
dependencies:
  tencent_cloud_chat_sdk: "最新版本" //可在https://pub.dev/packages/tencent_cloud_chat_sdk 上查看im flutter sdk的最新版本并使用
```

此时您的 editor 或许会自动 flutter pub get，如果没有请您在命令行中手动输入 flutter pub get。

如果您的项目需要支持 Web，请在执行后续步骤前，[查看Web兼容说明章节](#web)，引入JS文件。

### 引入并初始化 SDK

```
import 'package:tencent_cloud_chat_sdk/tencent_cloud_chat_sdk.dart';
```

## Flutter for Web支持[](id:web)

IM SDK(tencent_cloud_chat_sdk) 4.1.1+2版本起，可完美兼容Web端。

相比 Android 和 iOS 端，需要一些额外步骤。如下：

### 升级 Flutter 3.x 版本

Flutter 3.x 版本 针对 Web 性能做了较多优化，强烈建议您使用其来开发 Flutter Web 项目。

### 引入 JS

>?如果您现有的 Flutter 项目不支持 Web，请在项目根目录下运行 `flutter create .` 添加 Web 支持。

进入您项目的 `web/` 目录，使用 `npm` 或 `yarn` 安装相关JS依赖。初始化项目时，根据屏幕指引，进行即可。

```shell
cd web

npm init

npm i tim-js-sdk

npm i tim-upload-plugin
```

打开 `web/index.html` ，在 `<head> </head>` 间引入这JS文件。如下：

```html
<script src="./node_modules/tim-upload-plugin/index.js"></script>
<script src="./node_modules/tim-js-sdk/tim-js-friendship.js"></script>
```

![](https://qcloudimg.tencent-cloud.cn/raw/a4d25e02c546e0878ba59fcda87f9c76.png)

### 引入 Flutter for Web 增补 SDK

```dart
flutter pub add tencent_im_sdk_plugin_web
```

## Flutter for Desktop(PC) 支持[](id:pc)

我们的无 UI SDK(tencent_cloud_chat_sdk) 4.1.9 版本起，可完美兼容 macOS、Windows 端。

相比 Android 和 iOS 端，需要一些额外步骤。如下：

### 升级 Flutter 3.x 版本

从 Flutter 3.0 版本起，才可用于打包 desktop 端，因此，如需使用，请升级至 Flutter 3.x 版本。

### 引入 Flutter for Desktop 增补 SDK

```dart
flutter pub add tencent_im_sdk_plugin_desktop
```

#### macOS 修改

打开 `macos/Runner/DebugProfile.entitlements` 文件。

在 `<dict></dict>` 中，加入如下 `key-value` 键值对。

```
<key>com.apple.security.app-sandbox</key>
<false/>
```

## 常见问题

### flutter pub get/add 失败如何解决？

请参见官网配置 [国内镜像](https://flutter.cn/community/china)。

## 联系我们

如果您在接入使用过程中有任何疑问，请扫码加入微信群，或加入QQ群：788910197 咨询。

![](https://qcloudimg.tencent-cloud.cn/raw/e830ae8c7b8d9253eb71e7c3d9f7b2be.png)
