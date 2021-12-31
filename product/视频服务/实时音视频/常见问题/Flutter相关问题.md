[](id:que1)
### 两台手机同时运行 Demo，为什么看不到彼此的画面？
请确保两台手机在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个终端同时使用。
![](https://main.qcloudimg.com/raw/c7b1589e1a637cf502c6728f3c3c4f99.png)
 
[](id:que2)
### 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以在对 UDP 有拦截的办公网络下无法使用。如遇到类似问题，请参见 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399) 排查并解决。

[](id:que3)
### iOS 打包运行 Crash？
请排查是否 iOS14 以上的 debug 模式问题，具体请参见 [官方说明](https://flutter.cn/docs/development/ios-14#launching-debug-flutter-without-a-host-computer)。

[](id:que4)
### iOS 无法显示视频（Android 正常）？
请确认在您项目的 `info.plist` 中 `io.flutter.embedded_views_preview` 值为 YES。

[](id:que5)
### 更新 SDK 版本后，iOS CocoaPods 运行报错？
1. 删除 iOS 目录下 `Podfile.lock` 文件。
2. 执行 `pod repo update`。
3. 执行 `pod install`。
4. 重新运行。

[](id:que6)
### Android Manifest merge failed 编译失败？
1. 请打开 `/example/android/app/src/main/AndroidManifest.xml` 文件。
2. 将 `xmlns:tools="http://schemas.android.com/tools"` 加入到 manifest 中。
3. 将 `tools:replace="android:label"` 加入到 application 中。

![img](https://main.qcloudimg.com/raw/7a37917112831488423c1744f370c883.png)

[](id:que7)
### 因为没有签名，真机调试报错?
若报错信息如下图所示：
![](https://main.qcloudimg.com/raw/809ae94061575b4e670f3a80ac9f3781.png)
1. 您需购买苹果证书，并进行配置、签名操作后，即可在真机上调试。
2. 证书购买成功后，在 `target > signing & capabilities` 中进行配置。

[](id:que8)
### 对插件内的 swift 文件做了增删后，build 时查找不到对应文件？
在主工程目录的 `/ios` 文件路径下 `pod install` 即可。

[](id:que9)
### Run 报错“Info.plit, error: No value at that key path or invalid key path: NSBonjourServices”？
执行 `flutter clean` 后，重新运行即可。

[](id:que10)
### Pod install 报错？
若报错信息如下图所示：
![](https://main.qcloudimg.com/raw/73db67cfc9e6b934fed947b63c6d2120.png)
报错信息里面提示 pod install 的时候没有 `generated.xconfig` 文件，因此运行报错，您根据提示**需要执行 flutter pub get** 解决。
>? 该问题是 flutter 编译后的问题，新项目或者执行了 `flutter clean` 后，都不存在这个问题。

[](id:que11)
### Run 的时候 iOS 版本依赖报错？
若报错信息如下图所示：
![](https://main.qcloudimg.com/raw/9102b3394560ca9df2f70549baabe3ff.png)
可能是 pods 的 target 版本无法满足所依赖的插件，因此造成报错。因此您需修改报错 pods 中的 target 到对应的版本。

[](id:que12)
### Flutter 支持自定义采集和渲染吗？
目前不支持。自定义采集和渲染平台支持详情，请参见 [支持的平台](https://cloud.tencent.com/document/product/647/34066#.E6.94.AF.E6.8C.81.E7.9A.84.E5.B9.B3.E5.8F.B0)。
