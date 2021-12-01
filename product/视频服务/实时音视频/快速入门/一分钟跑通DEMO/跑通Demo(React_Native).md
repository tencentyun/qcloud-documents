本文主要介绍如何快速运行腾讯云 TRTC Demo（React Native）。

## 环境要求
- ReactNative 0.63 及以上版本
- Node & Watchman，node版本需在 v12 以上
- **Android 端开发：**
  - Android Studio 3.5及以上版本
  - App 要求 Android 4.1及以上版本设备
- **iOS & macOS 端开发：**
  - Xcode 11.0及以上版本
  - osx 系统版本要求 10.11 及以上版本
  - 请确保您的项目已设置有效的开发者签名
- 环境安装请参见 [官方文档](https://reactnative.cn/docs/environment-setup)

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com) 账号，并完成实名认证。

## 操作步骤
[](id:step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择 **开发辅助>[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 单击 **新建应用** 输入应用名称，例如 `TestTRTC`；若您已创建应用可单击 **选择已有应用**。
3. 根据实际业务需求添加或编辑标签，单击 **创建**。
![](https://main.qcloudimg.com/raw/f04d288ed091c98a5e8056eb86fb49e8.png)
>?
>- 应用名称只能包含数字、中英文字符和下划线，长度不能超过15个字符。
>- 标签用于标识和组织您在腾讯云的各种资源。例如：企业可能有多个业务部门，每个部门有1个或多个 TRTC 应用，这时，企业可以通过给 TRTC 应用添加标签来标记部门信息。标签并非必选项，您可根据实际业务需求添加或编辑。

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 [Demo 源码](https://github.com/c1avie/TRTCReactNativeDemo)。
2. 下载完成后，单击 **已下载，下一步**。

>! 控制台暂时无法下载 ReactNative Demo，**请直接通过上方链接下载 Demo 源码**。

[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `/debug/config.js` 文件。
3. 设置 `SDKAPPID`和`SECRETKEY` 参数：
<ul><li/>SDKAPPID：默认为 PLACEHOLDER ，请设置为实际的 SDKAppID。
    <li/>SECRETKEY：默认为 PLACEHOLDER ，请设置为实际的密钥信息。</ul>
    <img src="https://main.qcloudimg.com/raw/fba60aa9a44a94455fe31b809433cfa4.png"/>
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。

>?
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:step4)
### 步骤4：权限配置
需要配置 App 权限才能运行。
<dx-tabs>
::: Android 端
1. 在 `AndroidManifest.xml` 中配置 App 的权限，TRTC SDK 需要以下权限：
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
在 `Info.plist` 中配置 App 的权限，TRTC SDK 需要以下权限：
```objectiveC
<key>NSCameraUsageDescription</key>
<string>授权摄像头权限才能正常视频通话</string>
<key>NSMicrophoneUsageDescription</key>
<string>授权麦克风权限才能正常语音通话</string>
```
:::
</dx-tabs>

[](id:step5)
### 步骤5：编译运行
启动 Metro，在您的 React Native 项目目录下运行 `npx react-native start`。
<dx-tabs>
:::  Android 端
新开窗口，启动开发调试：
```
npx react-native run-android
```
:::
::: iOS 端
1. 在 iOS 目录里执行 `pod install` 安装依赖。
2. 在 iOS 目录下打开 `.xcworkspace` ，启动 iOS 工程，在 iOS 工程目录里新建一个空的 swift 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/1b243c324d9e1e93d113d2431922c4de.jpeg)
3. 随后会弹出一个弹窗询问是否新建桥接文件，单击 **Create Bridging Header** 确认。
![](https://qcloudimg.tencent-cloud.cn/raw/8329b913890721ceef19be314462905d.png)
2. 新开窗口，启动开发调试。
```
npx react-native run-ios
```
:::
</dx-tabs>

