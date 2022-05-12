本文主要介绍如何快速地将腾讯云 TRTC SDK（React Native）集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 环境要求
- ReactNative 0.63 及以上版本。
- Node & Watchman，node版本需在 v12 以上
- **Android 端开发：**
  - Android Studio 3.5及以上版本
  - App 要求 Android 4.1及以上版本设备
  - Java Development Kit
- **iOS & macOS 端开发：**
  - Xcode 11.0及以上版本
  - osx 系统版本要求 10.11 及以上版本
  - 请确保您的项目已设置有效的开发者签名
- 环境安装请参见 [官方文档](https://reactnative.cn/docs/environment-setup)

## 集成 SDK
ReactNative SDK 已经发布到 [npm](https://www.npmjs.com/package/trtc-react-native)，您可以通过配置 `package.json` 安装。
1. 在项目的 `package.json` 中写如下依赖：
```
"dependencies": {
  "trtc-react-native": "^2.0.0"
},
```
2. 开通**摄像头**和**麦克风**的权限，即可开启语音通话功能。
<dx-tabs>
::: Android 端
1. 在 `AndroidManifest.xml` 中配置 App 的权限，TRTC SDK 需要以下权限。
```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-feature android:name="android.hardware.camera" />
<uses-feature android:name="android.hardware.camera.autofocus" />
```
>! 请勿设置 `android:hardwareAccelerated="false"`，关闭硬件加速之后，会导致对方的视频流无法渲染。
2. Android 端音视频权限需要手动申请。
```java
if (Platform.OS === 'android') {
  await PermissionsAndroid.requestMultiple([
    PermissionsAndroid.PERMISSIONS.RECORD_AUDIO, //音频需要
    PermissionsAndroid.PERMISSIONS.CAMERA, // 视频需要
  ]);
}
```
:::
::: iOS 端
1. 需要在 `Info.plist` 中加入对相机和麦克风的权限申请：
```objectiveC
<key>NSCameraUsageDescription</key>
<string>授权摄像头权限才能正常视频通话</string>
<key>NSMicrophoneUsageDescription</key>
<string>授权麦克风权限才能正常语音通话</string>
```
2. 链接原生库，请参见 [链接原生库](https://reactnative.cn/docs/linking-libraries-ios)。
::: 
</dx-tabs>



