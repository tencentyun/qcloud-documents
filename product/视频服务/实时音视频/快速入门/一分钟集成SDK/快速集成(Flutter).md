本文主要介绍如何快速地将腾讯云 TRTC SDK（Flutter）集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

>! 目前 Windows/MacOs 端仅支持音频，视频接口暂不支持。Android/iOS 端支持视频通话。

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

## 集成 SDK

Flutter SDK 已经发布到 [pub 库](https://pub.dev/packages/tencent_trtc_cloud)，您可以通过配置 `pubspec.yaml` 自动下载更新。
1. 在项目的 `pubspec.yaml` 中写如下依赖：
```
dependencies:
  tencent_trtc_cloud: 最新版本号
```
2. 开通**摄像头**和**麦克风**的权限，即可开启语音通话功能。
<dx-tabs>
::: iOS\s端
1. 需要在 `Info.plist` 中加入对相机和麦克风的权限申请：
```
<key>NSCameraUsageDescription</key>
<string>授权摄像头权限才能正常视频通话</string>
<key>NSMicrophoneUsageDescription</key>
<string>授权麦克风权限才能正常语音通话</string>
```
2. 添加字段 `io.flutter.embedded_views_preview`，并设定值为 YES。
:::
::: macOS\s端
1. 需要在 `Info.plist` 中加入对相机和麦克风的权限申请：
```
<key>NSCameraUsageDescription</key>
<string>授权摄像头权限才能正常视频通话</string>
<key>NSMicrophoneUsageDescription</key>
<string>授权麦克风权限才能正常语音通话</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>App需要您的同意,才能访问相册</string>
```
2. 需要在 `macos/Runner/*.entitlements` 文件中添加`com.apple.security.network.client` 、 `com.apple.security.network.server`
添加后如下图所示：
![](https://main.qcloudimg.com/raw/13f3eab720ec1da03b149db1a7240d6d.png)
3. 单击 Link Binary with Libraries 项展开，单击底下的+号图标去添加依赖库。
![](https://main.qcloudimg.com/raw/17046154417930f9d31b6452782df55d.jpg)
4. 添加其所需依赖库：`libbz2.1.0.tbd` 。
添加后如下图所示：
![](https://imgcache.qq.com/operation/dianshi/other/lib.7518607f9764321c99fbcf14348715b65563bca2.png)
:::

::: Android\s端
1. 打开 `/android/app/src/main/AndroidManifest.xml` 文件。
2. 将 `xmlns:tools="http://schemas.android.com/tools"` 加入到 manifest 中。
3. 将 `tools:replace="android:label"` 加入到 application 中。
>? 若不执行此步，会出现 [Android Manifest merge failed 编译失败](https://cloud.tencent.com/document/product/647/51623#que6) 问题。


![图示](https://main.qcloudimg.com/raw/7a37917112831488423c1744f370c883.png)
:::

::: Windows\s端
1. 启用 Windows 支持：`flutter config --enable-windows-desktop`。
2. `flutter run -d windows`。
:::
</dx-tabs>





## 常见问题
- [iOS 打包运行 Crash？](https://cloud.tencent.com/document/product/647/51623#que3)
- [iOS 无法显示视频（Android 正常）？](https://cloud.tencent.com/document/product/647/51623#que4)
- [更新 SDK 版本后，iOS CocoaPods 运行报错？](https://cloud.tencent.com/document/product/647/51623#que5)
- [Android Manifest merge failed 编译失败？](https://cloud.tencent.com/document/product/647/51623#que6)
- [因为没有签名，真机调试报错?](https://cloud.tencent.com/document/product/647/51623#que7)
- [对插件内的 swift 文件做了增删后，build 时查找不到对应文件？](https://cloud.tencent.com/document/product/647/51623#que8)
- [Run 报错“Info.plit, error: No value at that key path or invalid key path: NSBonjourServices”？](https://cloud.tencent.com/document/product/647/51623#que9)
- [Pod install 报错？](https://cloud.tencent.com/document/product/647/51623#que10)
- [Run 的时候 iOS 版本依赖报错？](https://cloud.tencent.com/document/product/647/51623#que11)

