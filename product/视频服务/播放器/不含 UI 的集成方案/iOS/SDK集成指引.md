本文主要介绍如何快速地将腾讯云视立方·播放器 LiteAVSDK_Player（iOS）集成到您的项目中，按照如下步骤进行配置，就可以完成 SDK 的集成工作。


## 开发环境要求
- Xcode 9.0+。
- iOS 9.0 以上的 iPhone 或者 iPad 真机。
- 项目已配置有效的开发者签名。

## 集成 LiteAVSDK
您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK，再将其导入到您当前的工程项目中。

[](id:cocoapods)
### CocoaPods集成
1. **安装 CocoaPods**
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```
2. **创建 Podfile 文件**
进入项目所在路径，输入以下命令行之后项目路径下会出现一个 Podfile 文件。
```
pod init
```
3. **编辑 Podfile 文件**
	使用 CocoaPod 官方源，支持选择版本号。编辑 Podfile 文件：
	
	Pod 方式直接集成最新版本 TXLiteAVSDK_Player：
```objective
platform :ios, '9.0'
source 'https://github.com/CocoaPods/Specs.git'

target 'App' do
pod 'TXLiteAVSDK_Player'
end
```
如果您需要指定某一个特定版本，可以在 podfile 文件中添加如下依赖：
```objective-c
pod 'TXLiteAVSDK_Player', '~> 10.3.11513'
```

4. **更新并安装 SDK**
  - 在终端窗口中输入如下命令以更新本地库文件，并安装 LiteAVSDK：
```
pod install
```

  - 或使用以下命令更新本地库版本：
```
pod update
```
pod 命令执行完后，会生成集成了 SDK 的 `.xcworkspace` 后缀的工程文件，双击打开即可。

[](id:manual)
### 手动集成SDK
1. 下载 最新版本 [TXLiteAVSDK_Player](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Player_iOS_latest.zip)  的 SDK + Demo 开发包。
2. 将 SDK/TXLiteAVSDK_Player.framework 添加到待集成的工程中，并勾选 `Do Not Embed`。
3. 需要配置项目 Target 的 -ObjC，否则会因为加载不到 SDK 的类别而导致 Crash。
```objective-c
打开 Xcode -> 选择对应的 Target -> 选择"Build Setting" Tab -> 搜索"Other Link Flag" -> 输入"-ObjC"
```
4. 添加相应的库文件（SDK 目录里）
   **TXFFmpeg.xcframework**：将.xcframework 文件添加到项目工程中，并在“General - Frameworks, Libraries, and Embedded Content”中将其设置为“Embed&Sign”，并在“Project Setting - Build Phases - Embed Frameworks”中进行检查，设置”Code Sign On Copy“选项为勾选状态，如下图所示：
    **TXSoundTouch.xcframework**：将.xcframework 文件添加到项目工程中，并在“General - Frameworks, Libraries, and Embedded Content”中将其设置为“Embed&Sign”，并在“Project Setting - Build Phases - Embed Frameworks”中进行检查，设置”Code Sign On Copy“选项为勾选状态，如下图所示：<br>
    <img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/b226decc76c33eff8c3f5b4cc4246bea.png" />
   <br>
   同时，切换到 Xcode 的 “Build Settings - Search Paths”，在“Framework Search Paths”中添加上述 Framework 所在的路径。
	 
	 **MetalKit.framework**：打开 Xcode，切换到“project setting - Build  Phases - Link Binary With Libraries”，选择左下角的“+”号，并输入“MetalKit”，并加入项目工程中，如下图所示：<br>
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/8ab7576dcc8bbe7b36396955ca06b186.png" />
<br>
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/8480798e5ba897077ed3cef8ebc12f2e.png" />
<br>

	 **ReplayKit.framework**：打开 Xcode，切换到“project setting - Build  Phases - Link Binary With Libraries”，选择左下角的“+”号，并输入“ReplayKit”，并加入项目工程中，如下图所示：<br>
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/aa07f3d4963ee703505a14a743f61a68.png" />
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/12491d4a64aa6df44e6a966e80ca54de.png" />
<br>
使用同样的方式添加如下系统库：
<br><b>系统 Framework 库</b>：SystemConfiguration, CoreTelephony, VideoToolbox, CoreGraphics, AVFoundation, Accelerate, MobileCoreServices<br>
<b>系统 Library 库:</b> libz, libresolv,  libiconv, libc++, libsqlite3

#### 画中画功能

如果需要使用画中画能力，请按如下图的方式进行配置，若无此部分需求可以忽略。

1、为了使用 iOS 的画中画（Picture-In-Picture），请将 SDK 升级到10.3版本及以上。
2、使用画中画能力时，需要开通后台模式。XCode 选择对应的Target -> Signing & Capabilities -> Background Modes，勾选“Audio, AirPlay, and Picture in Picture”，如图所示：
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/116e1e741f80d810502221fd143d8434.png" />

## 在工程中引入 SDK
项目代码中使用 SDK 有两种方式：
- **方式一：** 在项目需要使用 SDK API 的文件里，添加模块引用。
```
@import TXLiteAVSDK_Player;
```
- **方式二：**在项目需要使用 SDK API 的文件里，引入具体的头文件。
```
#import "TXLiteAVSDK_Player/TXLiteAVSDK.h"
```

## 给 SDK 配置 License 授权
1. 单击 [License 申请](https://console.cloud.tencent.com/vcube) 获取测试用 License，不配置 License 将会播放时视频失败，具体操作请参见 [测试版 License](https://cloud.tencent.com/document/product/1449/56981#test)。您会获得两个字符串：一个字符串是 licenseURL，另一个字符串是解密 key。
2. 在您的 App 调用 LiteAVSDK 的相关功能之前（建议在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中）进行如下设置：
```objc
@import TXLiteAVSDK_Player;
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSString * const licenceURL = @"<获取到的licenseUrl>";
    NSString * const licenceKey = @"<获取到的key>";
    
    //TXLiveBase 位于 "TXLiveBase.h" 头文件中
    [TXLiveBase setLicenceURL:licenceURL key:licenceKey]; 
    // TXLiveBase.delegate = self;
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}

#pragma mark - TXLiveBaseDelegate
- (void)onLicenceLoaded:(int)result Reason:(NSString *)reason {
    NSLog(@"onLicenceLoaded: result:%d reason:%@", result, reason);
}
@end
```

## 查看方法

License 设置成功后（需稍等一段时间，具体时间长短依据网络情况而定），您可以通过调用如下方法查看 License 信息：

```swift
NSLog(@"%@", [TXLiveBase getLicenceInfo]);
```

[](id:faq)

## 常见问题
1. 项目里面同时集成了直播 SDK/实时音视频/播放器等 LiteAVSDK 系列的多个 SDK 报符号冲突问题怎么解决？

如果集成了2个或以上产品（直播、播放器、TRTC、短视频）的 LiteAVSDK 版本，编译时会出现库冲突问题，因为有些 SDK 底层库有相同符号文件，这里建议只集成一个全功能版 SDK 可以解决，直播、播放器、TRTC、短视频这些都包含在一个 SDK 里面。具体请参见 [SDK 下载](https://vcube.cloud.tencent.com/home.html)。

