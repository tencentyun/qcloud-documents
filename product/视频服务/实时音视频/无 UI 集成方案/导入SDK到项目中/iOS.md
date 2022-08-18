本文介绍如何将 SDK 导入到您的项目中：
![](https://qcloudimg.tencent-cloud.cn/raw/49940081e803fb4534019ad5cb03dff8.png)
## 开发环境要求
- Xcode 9.0+。 
- iOS 9.0 以上的 iPhone 或者 iPad 真机。
- 项目已配置有效的开发者签名。

## 第一步：导入 SDK
您可以选择使用 CocoaPods 方案，或者先将 SDK 下载到本地，再将其手动导入到您当前的项目中。

### 方案一：使用 CocoaPods
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
根据您的项目需要选择合适的版本，并编辑 Podfile 文件：
    - **选项一：TRTC 精简版**
安装包体积增量最小，但仅支持实时音视频（TRTC）和 直播播放器（TXLivePlayer）两项功能。如选择此版本，请按如下方式编辑 Podfile 文件：
```
 platform :ios, '8.0'
  
  target 'App' do
  pod 'TXLiteAVSDK_TRTC', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_TRTC.podspec'
  end
```
    - **选项二：Professional 专业版**
包含实时音视频（TRTC）、直播播放器（TXLivePlayer）、RTMP 推流（TXLivePusher）、点播播放器（TXVodPlayer）和短视频录制和编辑（UGSV）等众多功能。如选择此版本，请按如下方式编辑 Podfile 文件：
```
 platform :ios, '8.0'
  
  target 'App' do
  pod 'TXLiteAVSDK_Professional', :podspec => 'https://liteav.sdk.qcloud.com/pod/liteavsdkspec/TXLiteAVSDK_Professional.podspec'
  end
```
4. **更新并安装 SDK**
    - 在终端窗口中输入如下命令以更新本地库文件，并安装 SDK：
```
pod install
```
    - 或使用以下命令更新本地库版本：
```
pod update
```
pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。

### 方案二：下载 SDK 并手动导入
1. 下载 [SDK](https://cloud.tencent.com/document/product/647/32689) 并解压到本地。
2. 打开您的 Xcode 工程项目，选择要运行的 target , 选中 **Build Phases** 项。
![](https://qcloudimg.tencent-cloud.cn/raw/be1dada9803b1bfd26c0feddb2f1cbb5.png)
3. 单击 **Link Binary with Libraries** 项展开，单击底下的“+”号图标去添加依赖库。
![](https://qcloudimg.tencent-cloud.cn/raw/79123f9d068777fc4b8a164583c872f6.png)
4. 依次添加下载的 `TXLiteAVSDK_TRTC.Framework`（或者 `TXLiteAVSDK_Professional.Framework`）、`TXFFmpeg.xcframework`、`TXSoundTouch.xcframework`、及其所需依赖库 `GLKit.framework`、`AssetsLibrary.framework`、`SystemConfiguration.framework`、`libsqlite3.0.tbd`、`CoreTelephony.framework`、`AVFoundation.framework`、`OpenGLES.framework`、`Accelerate.framework`、`MetalKit.framework`、`libresolv.tbd`、`MobileCoreServices.framework`、`libc++.tbd`、`CoreMedia.framework`。
![](https://qcloudimg.tencent-cloud.cn/raw/29f2ff828e7244195c0daf95b12a178e.png)
5. 单击 **General**，选择 **Frameworks,Libraries,and Embedded Content**，检查 TXLiteAVSDK_TRTC.framework 所需要动态库 **TXFFmpeg.xcframework**、**TXSoundTouch.xcframework**是否已经添加，是否正确选择选择 **Embed & Sign**，如果没有单击底下的“**+**”号图标依次添加。
![](https://qcloudimg.tencent-cloud.cn/raw/0e56b082c37ea2d8cff1e309433070af.png)

## 第二步：配置 App 权限
1. 如需使用 SDK 提供的音视频功能，需要给 App 授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
	- **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
	- **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语。
![](https://qcloudimg.tencent-cloud.cn/raw/c814236b930d5a908122b4a60a13d327.png)
2. 如需 App 进入后台仍然运行相关功能，可在 XCode 中选中当前工程项目，并在 **Capabilities** 下将设置项  **Background Modes** 设定为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture** ，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/57ee6aa850d7d73c3b67d8d1942c2b47.png)

## 第三步：在项目中引用 SDK
在完成了第一步的导入和第二步的设备权限授权后，就可以在项目中引用 SDK 中提供的接口 API 了。

### 通过 Objective-C 或 Swift 接口引用
在 Objective-C 或 Swift 代码中使用 SDK 有两种方式：
- **模块引用**：在项目需要使用 SDK API 的文件里，添加模块引用。
```
@import TXLiteAVSDK_TRTC;
```
- **头文件引用**：在项目需要使用 SDK API 的文件里，引入具体的头文件。
```
#import "TXLiteAVSDK_TRTC/TRTCCloud.h"
```

>? 对于 Objective-C 接口的使用方式，请参见 [iOS&Mac API 概览](https://cloud.tencent.com/document/product/647/32258)。

[](id:using_cpp)
### 通过 C++ 接口引用(可选)
如果您的项目是通过 QT 或者 Electron 这样的跨平台框架引入 SDK，请引用 `TXLiteAVSDK_TRTC.framework/Headers/cpp_interface` 目录下的头文件：
```
#include "TXLiteAVSDK_TRTC/cpp_interface/ITRTCCloud.h"
```

>? 对于 C++ 接口的使用方式，请参见 [全平台（C++）API 概览](https://cloud.tencent.com/document/product/647/32268)。

