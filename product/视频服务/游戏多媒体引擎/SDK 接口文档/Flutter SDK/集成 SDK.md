
为方便 Flutter 开发者调试和接入腾讯云游戏多媒体引擎产品 API，本文档主要为您介绍适用于 Flutter 开发的工程配置指引。

## 支持的平台
GME Flutter SDK 支持 iOS、Android 平台。

##  引入SDK

### 步骤1：下载 GME Flutter SDK 

在 [下载指引](https://cloud.tencent.com/document/product/607/18521) 中下载 SDK 文件，该版本中包括 GME Plugin，请将 SDK 文件解压到本地目录里。

### 步骤2：增加 Flutter 工程中 GME 插件的依赖

在您的 Flutter 项目中的 pubspec.yaml 文件中添加 GME 的依赖，注意参数中的 path 指上述 SDK 解压的路径
```
dependencies:
  flutter:
    sdk: flutter
  gme:
    path: ../
```

保存 pubspec.yaml 文件后在终端（命令行界面）中输入 flutter pub get 命令使您的项目中的 GME 插件生效（如果您的 IDE 中配置了 Flutter 的插件，保存将会自动执行该命令）。

```
flutter pub get
```

##  iOS 工程修改

1. 在终端环境里进入到您的 Flutter 项目内 iOS 工程目录中，执行 pod install。
2. 在 xcode 工程中配置 GME 依赖的库（如果您的工程中本来就有，此步骤可以忽略）依赖文件如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/97a63c009a3096c16b294fa455a21aba.png)
3. 游戏多媒体引擎 iOS 平台所需要的隐私权限如下：
 - Required background modes：允许后台运行（可选）。
 - Microphone Usage Description：允许麦克风权限。
 
## Android 工程修改
1. 因 GME 需要获取通话等权限并使用了 flutter permission-handler 权限管理插件，所以需要使用31以上版本的 Android SDK（如在工程中已经使用请忽略），修改如图：
<img src="https://qcloudimg.tencent-cloud.cn/raw/5d60d468796dd2551784debfd4839f78.png"  width="70%" /></img> 
2. 在 flutter 工程文件 android/app/src/AndroidManifest.xml 中添加工程权限（如已修改请忽略）。
```
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```
