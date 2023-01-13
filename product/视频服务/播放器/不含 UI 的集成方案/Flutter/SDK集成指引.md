## 环境准备

- Flutter 2.0 及以上版本。
- Android 端开发：
    - Android Studio 3.5及以上版本。
    - App 要求 Android 4.1及以上版本设备。
- iOS 端开发：
    - Xcode 11.0及以上版本。
    - osx 系统版本要求 10.11 及以上版本
    - 请确保您的项目已设置有效的开发者签名。

## SDK 下载

腾讯云视立方 Flutter 播放器项目的地址是 [Player Flutter](https://github.com/LiteAVSDK/Player_Flutter) 。

## 快速集成

### 在项目的 pubspec.yaml 中添加依赖

支持基于LiteAVSDK Player 或 Professional 版本集成，您可以根据项目需要进行集成。

1. 集成 LiteAVSDK_Player 版本最新版本，默认情况下也是集成此版本。在`pubspec.yaml`中增加配置：
```yaml
super_player:
  git:
    url: https://github.com/LiteAVSDK/Player_Flutter
    path: Flutter
```
集成 LiteAVSDK_Professional 最新版本，则`pubspec.yaml`中配置改为：
```yaml
super_player:
  git:
    url: https://github.com/LiteAVSDK/Player_Flutter
    path: Flutter
    ref: Professional
```
如果需要集成指定播放器版本的 SDK，可以指定通过 ref 依赖的 tag 来指定到对应版本，如下所示：
```yaml
super_player:
  git:
    url: https://github.com/LiteAVSDK/Player_Flutter
    path: Flutter
    ref: release_player_v1.0.6 

# release_player_v1.0.6 表示将集成Android端TXLiteAVSDK_Player_10.6.0.11182 版本，iOS端集成TXLiteAVSDK_Player_10.6.11821版本
```

 更多归档的 tag 请参考 [release 列表](https://github.com/LiteAVSDK/Player_Flutter/releases) 。

2. 集成之后，可以通过代码编辑器自带的 UI 界面来获取 flutter 依赖，也可以直接使用如下命令获取
```yaml
flutter packages get
```

3. 使用过程中，可以通过以下命令来更新现有flutter依赖：
```dart
flutter pub upgrade
```

### 添加原生配置

#### Android 端配置
1. 在 Android 的`AndroidManifest.xml`中增加如下配置：
```xml
<!--网络权限-->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<!--存储-->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

2. 确保 Android 目录下的 `build.gradle` 使用了mavenCenter，能够成功下载到依赖。
```groovy
repositories {
  mavenCentral()
}
```

3. 如果需要更新原生SDK依赖版本，可手动删除 Android 目录下的 `build` 文件夹，也可以使用如下命令强制刷新。
```shell
./gradlew build
```


#### iOS 端配置

注意：**iOS 端目前暂不支持模拟器运行调试，建议在真机下进行开发调试**。

1. 在 iOS 的`Info.plist`中增加如下配置：
```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
2. iOS 原生采用`pod`方式进行依赖，编辑`podfile`文件，指定您的播放器 SDK 版本，默认集成的是 Player 版 SDK。
```xml
pod 'TXLiteAVSDK_Player'	        //Player版
```
Professional 版 SDK 集成：
```
pod 'TXLiteAVSDK_Professional' 	//Professional版
```
 如果不指定版本，默认会安装最新的`TXLiteAVSDK_Player`最新版本。

3. 部分情况下（如：发布了新版本），需要强制更新 iOS 播放器依赖，可以在 iOS 目录下使用如下命令进行更新：
```shell
rm -rf Pods
rm -rf Podfile.lock
pod update
```

## 集成视频播放 License

若您已获得相关 License 授权，需在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)  获取 License URL 和 License Key：
![](https://qcloudimg.tencent-cloud.cn/raw/9b4532dea04364dbff3e67773aab8c95.png)
若您暂未获得 License 授权，需先参见 [视频播放 License](https://cloud.tencent.com/document/product/881/74588) 获取相关授权。
集成播放器前，需要 [注册腾讯云账户](https://cloud.tencent.com/login) ，注册成功后申请视频播放能力 License， 然后通过下面方式集成，建议在应用启动时进行。
如果没有集成 License，播放过程中可能会出现异常。
```dart
String licenceURL = ""; // 获取到的 licence url
String licenceKey = ""; // 获取到的 licence key
SuperPlayerPlugin.setGlobalLicense(licenceURL, licenceKey);
```

## 深度定制开发指引

腾讯云播放器 SDK Flutter 插件对原生播放器能力进行了封装， 如果您要进行深度定制开发，建议采用如下方法：

- 基于点播播放，接口类为`TXVodPlayerController` 或直播播放，接口类为`TXLivePlayerController`，进行定制开发，项目中提供了定制开发 Demo，可参考 example 工程里的`DemoTXVodPlayer`和`DemoTXLivePlayer`。
- 播放器组件`SuperPlayerController` 对点播和直播进行了封装，同时提供了简单的 UI 交互， 由于此部分代码在 example 目录。如果您有对播放器组件定制化的需求，您可以进行如下操作：
  把播放器组件相关的代码，代码目录：`Flutter/superplayer_widget`，导入到您的项目中，进行定制化开发。

## 常见问题

1. iOS 端运行，出现 `No visible @interface for 'TXLivePlayer' declares the selector 'startLivePlay:type:'`等类似找不到接口错误。
**解决方法**：
可以使用如下命令，更新 IOS SDK：
```shell
rm -rf Pods
rm -rf Podfile.lock
pod update
```

2. 同时集成 tencent_trtc_cloud 和 flutter 播放器出现 SDK 或 符号冲突。
   常见异常日志：`java. lang.RuntimeException: Duplicate class com.tencent.liteav.TXLiteAVCode found in modules classes.jar`
**解决方法**：
此时需要集成 flutter 播放器的 Professional 版本，让 tencent_trtc_cloud 和 flutter 播放器共同依赖于同一个版的 LiteAVSDK_Professional。注意确保依赖的 LiteAVSDK_Professional 的版本必须一样。
例如：依赖 Android 端 TXLiteAVSDK_Professional_10.3.0.11196  和 iOS 端 TXLiteAVSDK_Professional to 10.3.12231 版本，依赖声明如下：

   ```xml
   tencent_trtc_cloud：2.3.8
   
   super_player:
     git:
       url: https://github.com/LiteAVSDK/Player_Flutter
       path: Flutter
       ref: release_pro_v1.0.3.11196_12231
   ```

3. 需要同时使用多个播放器实例的时候，频繁切换播放视频，画面呈现模糊。
**解决方法**：
在每个播放器组件容器销毁的时候，调用播放器的`dispose`方法，将播放器释放

4. 其余通用 flutter 依赖问题
**解决方法**：
 - 执行`flutter doctor`命令检查运行环境，直到出现“No issues found!”。
 - 执行`flutter pub get`确保所有依赖的组件都已更新成功。

5. 集成 superPlayer 之后，出现如下 manifest 错误：
```text
	Attribute application@label value=(super_player_example) from AndroidManifest.xml:9:9-45
	is also present at [com.tencent.liteav:LiteAVSDK_Player:10.8.0.13065] AndroidManifest.xml:22:9-41 value=(@string/app_name).
	Suggestion: add 'tools:replace="android:label"' to <application> element at AndroidManifest.xml:8:4-51:19 to override.
```
**解决方法**：
由于播放器 Android SDK 的 AndroidManifest 已经定义过 label，而 flutter 新建项目之后，在 Android 目录的 AndroidManifest 也会定义 label，此处建议根据错误提示，进入您的 Android 项目目录，在 AndroidManifest 的根节点`manifest`节点下增加` xmlns:tools="http://schemas.android.com/tools" `，并在 application 节点下增加`'tools:replace="android:label"'`。

6. 集成 superPlayer 之后，出现如下版本错误：
```text
uses-sdk:minSdkVersion 16 cannot be smaller than version 19 declared in library [:super_player]
```
**解决方法**：
目前播放器 Android SDK 最小支持版本为 android 19，flutter 部分版本默认 Android 最小支持版本为 android 16。建议您将最小支持版本提高到 android 19。具体修改方法为，进入您的 Android 项目的主 module 下，一般为`app`目录，将该目录下的`build.gradle`中的`minSdkVersion`修改为19。

## 更多功能

您可以通过运行项目中的 example 体验完整功能，example 运行指引。
播放器 SDK 官网提供了 iOS、Android 和 Web 端的 Demo 体验，[请点击这里](https://cloud.tencent.com/document/product/881/20204)。
