
本文主要介绍如何快速地将腾讯云视立方·直播 LiteAVSDK（iOS）集成到您的项目中，按照如下步骤进行配置，就可以完成 SDK 的集成工作。下面以全功能的 [全功能版 SDK](https://cloud.tencent.com/document/product/454/7873) 为例：

## 开发环境要求
- Xcode 9.0+。
- iOS 9.0 以上的 iPhone 或者 iPad 真机。
- 项目已配置有效的开发者签名。

## 集成 LiteAVSDK
您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK，再将其导入到您当前的工程项目中。

[](id:cocoapods)
### CocoaPods
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
编辑 Podfile 文件，有如下有两种设置方式：
	-  方式一：使用腾讯云 LiteAVSDK 的 podspec 文件路径。
```podspec
platform :ios, '9.0'

target 'App' do
pod 'TXLiteAVSDK_Professional', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_Professional.podspec'
end
```
	-  方式二：使用 CocoaPod 官方源，支持选择版本号。
```
platform :ios, '9.0'
source 'https://github.com/CocoaPods/Specs.git'

target 'App' do
pod 'TXLiteAVSDK_Professional'
end
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
### 手动集成
1. 下载 [LiveAVSDK](https://cloud.tencent.com/document/product/454/7873) ，下载完成后进行解压。
2. 打开您的 Xcode 工程项目，选择要运行的 target , 选中 **Build Phases** 项。
![](https://qcloudimg.tencent-cloud.cn/raw/db2f2f8d061a20af01a16c0dde7c8247.png)
3. 单击 **Link Binary with Libraries** 项展开，单击底下的 **+** 添加依赖库。
![](https://qcloudimg.tencent-cloud.cn/raw/625efe18420f8f4c01af264007e942d7.png)
4. 依次添加所下载的 `TXLiteAVSDK_Professional.framework` 、`TXFFmpeg.xcframework`、`TXSoundTouch.xcframework` 及其所需依赖库：
```node
AVFoundation.framework
VideoToolbox.framework
libz.tbd
OpenGLES.framework
Accelerate.framework
libsqlite3.0.tbd
MetalKit.framework
CoreTelephony.framework
libresolv.tbd
GLKit.framework
Foundation.framework
SystemConfiguration.framework
AssetsLibrary.framework
libc++.tbd
CoreServices.framework
CoreMedia.framework
```
![](https://qcloudimg.tencent-cloud.cn/raw/2cad68ebf4de0faba9fad17c8cf769e7.png)
5. 选中 Build Settings 项，搜索 `Other Linker Flags`。添加 `-ObjC`。
![](https://qcloudimg.tencent-cloud.cn/raw/c4709ea5f04ab51f6f2ce454ba1c1275.png)

## 授权摄像头和麦克风使用权限
使用 SDK 的音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
- **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
- **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语。

![](https://qcloudimg.tencent-cloud.cn/raw/9c5f126ece7c31723545a137b38268c6.png)

## 在工程中引入 SDK
项目代码中使用 SDK 有两种方式：
- **方式一：** 在项目需要使用 SDK API 的文件里，添加模块引用。
```
@import TXLiteAVSDK_Professional;
```
- **方式二：**在项目需要使用 SDK API 的文件里，引入具体的头文件。
```
#import "TXLiteAVSDK_Professional/TXLiteAVSDK.h"
```

## 给 SDK 配置 License 授权
1. 单击 [License 申请](https://console.cloud.tencent.com/live/license) 获取测试用 License，您会获得两个字符串：一个字符串是 licenseURL，另一个字符串是解密 key。
2. 在您的 App 调用 LiteAVSDK 的相关功能之前（建议在 `- [AppDelegate application:didFinishLaunchingWithOptions:]` 中）进行如下设置：
```objc
@import TXLiteAVSDK_Professional;
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSString * const licenceURL = @"<获取到的licenseUrl>";
    NSString * const licenceKey = @"<获取到的key>";
    
    //TXLiveBase 位于 "TXLiveBase.h" 头文件中
    [TXLiveBase setLicenceURL:licenceURL key:licenceKey]; 
    NSLog(@"SDK Version = %@", [TXLiveBase getSDKVersionStr]);
}
@end
```

[](id:faq)
## 常见问题
### 1. LiteAVSDK 是否支持后台运行？
**支持**，如需要进入后台仍然运行相关功能，操作如下：
1. 选中当前工程项目，选择 **Signing&Capabilities** ，单击左上角**+**，如图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/d06bbd6669a4d60bbf2c217b0a8cc961.png)
2. 选择 **Background Modes**。
![](https://qcloudimg.tencent-cloud.cn/raw/d43e735cb3450fe10c3327803904c0b2.png)
3. 在 **Background Modes**中勾选 **Audio，AirPlay and Picture in Picture** ，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e37c5de253b07f27de0a6554ba3a6311.png)

### 2. 项目里面同时集成了直播 SDK/实时音视频/播放器等 LiteAVSDK 系列的多个 SDK 报符号冲突问题怎么解决？
如果集成了2个或以上产品（直播、播放器、TRTC、短视频）的 LiteAVSDK 版本，编译时会出现库冲突问题，因为有些 SDK 底层库有相同符号文件，这里建议只集成一个全功能版 SDK 可以解决，直播、播放器、TRTC、短视频这些都包含在一个 SDK 里面。具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/454/7873)。

