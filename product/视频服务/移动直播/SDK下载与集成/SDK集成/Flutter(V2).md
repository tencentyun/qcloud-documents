本文主要介绍如何快速地将 [腾讯云视立方·移动直播 live_flutter_plugin Flutter 插件](https://pub.dev/packages/live_flutter_plugin) 集成到您的项目中，按照如下步骤进行配置，就可以完成 live_flutter_plugin 的集成工作。示例工程请参见 [live_flutter_plugin_example](https://github.com/LiteAVSDK/Live_Flutter)。

## 环境准备
- Flutter 2.0 及以上版本。
- **Android 端开发：**
  - Android Studio 3.5及以上版本。
  - App 要求 Android 4.1及以上版本设备。
- **iOS & macOS 端开发：**
  - Xcode 11.0及以上版本。
  - osx 系统版本要求 10.11 及以上版本
  - 请确保您的项目已设置有效的开发者签名。


## 快速集成 SDK
Flutter SDK 已经发布到 pub 库，您可以通过配置 pubspec.yaml 自动下载更新。

1. 在项目的 pubspec.yaml 中写如下依赖：
```dart
dependencies:
  live_flutter_plugin: latest version number
```
2. 开通摄像头和麦克风的权限，即可开启语音通话功能。
<dx-tabs>
::: iOS
1. 需要在 `Info.plist` 中加入对相机和麦克风的权限申请：
```dart
<key>NSCameraUsageDescription</key>
<string>授权摄像头权限才能正常视频通话</string>
<key>NSMicrophoneUsageDescription</key>
<string>授权麦克风权限才能正常语音通话</string>
```
2. 开通摄像头和麦克风的权限，即可开启语音通话功能。
:::
::: Android
1. 打开 `/android/app/src/main/AndroidManifest.xml` 文件。
2. 将 `xmlns:tools="http://schemas.android.com/tools"` 加入到 manifest 中。
3. 将 `tools:replace="android:label"` 加入到 application 中。
>? 若不执行此步，会出现 Android Manifest merge failed 编译失败问题。
>
![](https://main.qcloudimg.com/raw/7a37917112831488423c1744f370c883.png)
:::
</dx-tabs>


## 快速开始
1. 单击 [License 申请]((https://cloud.tencent.com/document/product/454/34750)) 获取测试用 License，您会获得两个字符串：一个字符串是 licenseURL，另一个字符串是解密 key。
2. 在您的 App 调用 live_flutter_plugin 的相关功能之前进行如下设置：
```dart
import 'package:live_flutter_plugin/v2_tx_live_premier.dart';

 /// 腾讯云License管理页面(https://console.cloud.tencent.com/live/license)
setupLicense() {
  // 当前应用的License LicenseUrl
  var LICENSEURL = "";
  // 当前应用的License Key
  var LICENSEURLKEY = "";
  V2TXLivePremier.setLicence(LICENSEURL, LICENSEURLKEY);
}

```

## 常见问题
更多常见问题请参见 [Flutter 相关问题](https://cloud.tencent.com/document/product/647/51623)。

### 如何获取可用的推流 URL？
开通直播服务后，可以使用 **直播控制台** > **辅助工具** > [**地址生成器**](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator) 生成推流地址，详细信息请参见 [推拉流URL](https://cloud.tencent.com/document/product/454/7915)。

### iOS 无法显示视频（Android 正常）？

请确认在您的 info.plist 中 `io.flutter.embedded_views_preview` 是否为 `YES`。

### Android Manifest merge failed 编译失败？
1. 请打开 `/example/android/app/src/main/AndroidManifest.xml` 文件。
2. 将 `xmlns:tools="http://schemas.android.com/tools"` 加入到 manifest 中。
3. 将 `tools:replace="android:label"` 加入到 application中。

![图示](https://main.qcloudimg.com/raw/7a37917112831488423c1744f370c883.png)
