本文主要介绍如何快速地在 Mac 端将腾讯云视立方 SDK 集成到您的项目中，腾讯云视立方 SDK Mac 端仅**音视频通话 TRTC 版本**支持。按照如下步骤进行配置，就可以完成 SDK 在 Mac 端的集成工作。

## 版本支持

本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | - | - | - | &#10003; | - | - |
| SDK 下载 <div style="width: 90px"/>  | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 开发环境要求
- Xcode 9.0+。
- OS X10.10+ 的 Mac 真机。
- 项目已配置有效的开发者签名。

## 集成 TRTC SDK
您可以选择使用 CocoaPods 自动加载的方式，或者手动先下载 SDK 再将其导入到您当前的工程项目中。

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
编辑 Podfile 文件，有如下有两种设置方式：
- 方式一：使用腾讯云视立方 LiteAV SDK 的 pod 路径。
<dx-codeblock>
::: pod路径
	platform :osx, '10.10'
	
	target 'Your Target' do
	pod 'TXLiteAVSDK_TRTC_Mac', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_TRTC_Mac.podspec'
	end
:::
</dx-codeblock>
- 方式二：使用 CocoaPod 官方源，支持选择版本号。
<dx-codeblock>
::: pod路径
	platform :osx, '10.10'
	source 'https://github.com/CocoaPods/Specs.git'
	
	target 'Your Target' do
	pod 'TXLiteAVSDK_TRTC_Mac'
	end
:::
</dx-codeblock>

#### 4. 安装与更新 SDK
在终端窗口中输入如下命令执行安装腾讯云视立方TRTC SDK：
```
pod install
```
或使用以下命令更新本地库版本：
```
pod update
```

pod 命令执行完后，会生成集成了 SDK 的 `.xcworkspace` 后缀的工程文件，双击打开即可。

### 手动集成
1. 下载 [TRTC-SDK ](https://vcube.cloud.tencent.com/home.html?sdk=video) 的 Mac 版本。
2. 打开您的 Xcode 工程项目，将第一步中下载的 framework 导入到您的工程。
3. 选择要运行的 target，选中 Build Phases 项。
![](https://main.qcloudimg.com/raw/b5097f8ac4cbaa5044d92b2a96ea2b9e.jpg)
4. 单击 **Link Binary with Libraries** 项展开，单击底下的+号图标去添加依赖库。
![](https://main.qcloudimg.com/raw/17046154417930f9d31b6452782df55d.jpg)
5. 依次添加所下载的 SDK Framework 及其所需依赖库：`AudioUnit.framework`、`libc++.tbd` 和 `Accelerate.framework`。  
添加后如下图所示：
![](https://main.qcloudimg.com/raw/258ffc87c493d23cf591bb2ff9102677.png)

## 授权摄像头和麦克风使用权限
使用 SDK 的音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
- **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
- **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语。
如下图所示：
![](https://main.qcloudimg.com/raw/be76bd6f3f22d31385d871710b51b771.jpg) 

如果 App 启用了 **App Sandbox** 或 **Hardened Runtime**，需要勾选上 `Network`、`Camera` 和 `Audio Input` 这几个选项。
- App Sandbox 配置如下图所示：
![](https://main.qcloudimg.com/raw/b77d2ab814e6e14e8bed17efdcbee1a6.png)
- Hardened Runtime 配置如下图所示：
![](https://main.qcloudimg.com/raw/2b569e1c95bb4c97b7045112d6e3ce9c.png)

## 引用腾讯云视立方 TRTC SDK
腾讯云视立方TRTC SDK 支持两种调用方式，您可以任选一种：
### 方案一：通过 Objective-C 或 Swift 接口引用腾讯云视立方 TRTC SDK
在 Objective-C 或 Swift 代码中使用 SDK 有两种方式：
- **模块引用**：在项目需要使用 SDK API 的文件里，添加模块引用。
```
@import TXLiteAVSDK_TRTC_Mac;
```
- **头文件引用**：在项目需要使用 SDK API 的文件里，引入具体的头文件。
```
#import TXLiteAVSDK_TRTC_Mac/TRTCCloud.h
```

[](id:using_cpp)
### 方案二：通过 C++ 接口引用 TRTC SDK
1. **引用头文件**：如果您要使用 C++ 接口来开发Mac应用，请引用 `TXLiteAVSDK_TRTC_Mac.framework/Headers/cpp_interface` 目录下的头文件。
```
#include TXLiteAVSDK_TRTC_Mac/cpp_interface/ITRTCCloud.h
```
2. **使用命名空间**：C++ 全平台接口的接口、类型等均定义在 trtc 命名空间中，为了让代码更加简洁，建议您直接使用 trtc 命名空间。
```
using namespace trtc;
```

>? 对于 C++ 接口的使用方式，请参见 [全平台（C++）API 概览](https://cloud.tencent.com/document/product/1449/58932)。
