# iOS端集成

## 支持平台

+ SDK 支持 iOS 8.0 以上系统

## 开发环境

+ Xcode 9 或更高版本
+ OS X 10.10 或更高版本

## 设置步骤

### 1.链接SDK及系统库
1. 将下载的SDK资源包解压，并将SDK文件夹中的TXLiteAVSDK_开头的framework(如TXLiteAVSDK_UGC.framework)复制到工程所在文件夹,并拖动到工程当中。

2. 选中当工程的Target，添加以下系统库
1. Accelerate.framework
2. SystemConfiguration.farmework
3. libc++.tbd
4. libsqlite3.tbd

添加完毕后，工程库依赖如下图所示：![](https://main.qcloudimg.com/raw/a5fe16ca046a0aad84224e1ffa766a42.jpg)

### 2. 配置App权限
应用会需要相册及相册的访问权限，需要在Info.plist中添加对应项，可以通过在Info.plist中右键选Open as / Source Code粘贴并修改以下内容进行配置。
```
<key>NSAppleMusicUsageDescription</key>
<string>视频云工具包需要访问你的媒体库权限以获取音乐，不允许则无法添加音乐</string>
<key>NSCameraUsageDescription</key>
<string>视频云工具包需要访问你的相机权限，开启后录制的视频才会有画面</string>
<key>NSMicrophoneUsageDescription</key>
<string>视频云工具包需要访问你的麦克风权限，开启后录制的视频才会有声音</string>
<key>NSPhotoLibraryAddUsageDescription</key>
<string>视频云工具包需要访问你的相册权限，开启后才能保存编辑的文件</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>视频云工具包需要访问你的相册权限，开启后才能编辑视频文件</string>
```

### 3. SDK License 设置与基本信息获取
请参考 License介绍 的指引申请License后，从 [控制台](https://console.cloud.tencent.com/vod/license) 复制 key 和 url，见下图。
![](https://main.qcloudimg.com/raw/59ccde1fa75b2903aeb7147f6538089c.png)
在您的应用中使用短视频功能之前（建议在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中）进行如下设置

```objc
@import TXLiteAVSDK_UGC;
@implementation AppDelegate
- (BOOL)application:(UIApplication*)applicationdidFinishLaunchingWithOptions:(NSDictinoary*)options {
NSString * const licenceURL = @"<获取到的licnseUrl>";
NSString * const licenceKey = @"<获取到的key>";
[TXUGCBase setLicenceURL:licenceURL key:licenceKey];
NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
@end
```

- 对于使用 4.7 版本 license 的用户，如果您升级了 SDK 到 4.9 版本，您可以登录控制台，单击下图的 **切换到新版License** 按钮生成对应的 key 和 url，切换后的License必须使用4.9及更高的版本，切换后按照上述操作集成即可。
![](https://main.qcloudimg.com/raw/71ab2d47c9a01b2f514210e54f2b82fc.png)

- 商业版请参考[动效变脸](https://cloud.tencent.com/document/product/584/13509)

### 4. Log 配置
在  TXLiveBase 中可以设置 log 是否在控制台打印以及 log 的级别，相关接口如下：
- **setConsoleEnabled**
设置是否在 xcode 的控制台打印 SDK 的相关输出。

- **setLogLevel**
设置是否允许 SDK 打印本地 log，SDK 默认会将 log 写到当前 App 的 **Documents/logs** 文件夹下。
如果您需要我们的技术支持，建议将次开关打开，在重现问题后提供 log 文件，非常感谢您的支持。

- **Log 文件的查看**
小直播 SDK 为了减少 log 的存储体积，对本地存储的 log 文件做了加密，并且限制了 log 数量的大小，所以要查看 log 的文本内容，需要使用 log [解压缩工具](http://dldir1.qq.com/hudongzhibo/log_tool/decode_mars_log_file.py)。

```    objc
[TXLiveBase setConsoleEnabled:YES];
[TXLiveBase setLogLevel:LOGLEVEL_DEBUG];
```

### 5. 编译运行

如果前面各个步骤都操作正确的话，HelloSDK 工程就可以顺利编译通过。在 Debug 模式下运行 App，Xcode 的 Console 窗格会打印出 SDK 的版本信息。

> 2017-09-26 16:16:15.767 HelloSDK[17929:7488566] SDK Version = 5.2.5541 
