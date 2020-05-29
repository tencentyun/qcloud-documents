本文主要介绍如何快速地将腾讯云 TRTC SDK（iOS）集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求
- Xcode 9.0+。
- iOS 9.0 以上的 iPhone 或者 iPad 真机。
- 项目已配置有效的开发者签名。

## 集成 TRTC SDK
您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK 再将其导入到您当前的工程项目中。

### CocoaPods
#### 1. 安装 CocoaPods
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```

#### 2. 创建 Podfile 文件
进入项目所在路径，输入以下命令行之后项目路径下会出现一个 Podfile 文件。
```
pod init
```

#### 3. 编辑 Podfile 文件
编辑 Podfile 文件，并根据需要选择合适的 SDK 版本：
- [精简版](https://cloud.tencent.com/document/product/647/32689#TRTC)：安装包体积增量最小，但仅支持 TRTC 和 CDN 播放（TXLivePlayer）功能。
```
  platform :ios, '8.0'
  
  target 'App' do
  pod 'TXLiteAVSDK_TRTC', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_TRTC.podspec'
  end
```

- [专业版](https://cloud.tencent.com/document/product/647/32689#Professional)：除了 TRTC，还包含 RTMP 推流（TXLivePusher）、CDN 播放（TXLivePlayer）、点播播放（TXVodPlayer）以及短视频（UGSV）等多种功能。
```
  platform :ios, '8.0'
  
  target 'App' do
  pod 'TXLiteAVSDK_Professional', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_Professional.podspec'
  end
```

您也可以使用 CocoaPod 官方源，但下载速度可能较慢：
```
   platform :ios, '8.0'
   source 'https://github.com/CocoaPods/Specs.git'
   
   target 'App' do
   pod 'TXLiteAVSDK_TRTC'
   end
```

#### 4. 更新并安装 SDK
在终端窗口中输入如下命令以更新本地库文件，并安装 TRTC SDK：
```
pod install
```
或使用以下命令更新本地库版本：
```
pod update
```

pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。


### 手动集成
1. 下载 [TRTC - SDK ](https://github.com/tencentyun/TRTCSDK/tree/master/iOS/SDK) ，下载完成后进行解压。
2. 打开您的 Xcode 工程项目，选择要运行的 target , 选中 **Build Phases** 项。
 ![](https://main.qcloudimg.com/raw/2719ff925e92de21a2ba370a8ba5a32c.jpg)
3. 单击 **Link Binary with Libraries** 项展开，单击底下的“+”号图标去添加依赖库。
 ![](https://main.qcloudimg.com/raw/2e3b382fccadb0fe9e1038fffa1ef12f.jpg)
4. 依次添加所下载的 TRTC SDK Framework 及其所需依赖库 **libc++** 。
 ![](https://main.qcloudimg.com/raw/0327c1ab6562e0f6e7f17b2e0fbe96dd.jpg)


## 授权摄像头和麦克风使用权限
使用 SDK 的音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
- **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
- **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语。

![](https://main.qcloudimg.com/raw/54cc6989a8225700ff57494cba819c7b.jpg)


## 引用 TRTC SDK
项目代码中使用 SDK 有两种方式：
- 方式一： 在项目需要使用 SDK API 的文件里，添加模块引用。
```
@import TXLiteAVSDK_TRTC;
```

- 方式二：在项目需要使用 SDK API 的文件里，引入具体的头文件。
```
#import TXLiteAVSDK_TRTC/TRTCCloud.h
```

## 常见问题
### 1. TRTC SDK 是否支持后台运行？
支持，如需要进入后台仍然运行相关功能，可选中当前工程项目，在 **Capabilities** 下的设置  **Background Modes** 打开为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture** ，如下图所示：
![](https://main.qcloudimg.com/raw/d960dfec88388936abce2d4cb77ac766.jpg)
