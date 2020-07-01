本文主要介绍如何快速地将腾讯云 TRTC SDK（Mac）集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。


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
- 方式一：使用腾讯云 LiteAV SDK 的 pod 路径。

```
	platform :osx, '10.10'

	target 'Your Target' do
	pod 'TXLiteAVSDK_TRTC_Mac', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_TRTC_Mac.podspec'
	end
```

- 方式二：使用 CocoaPod 官方源，支持选择版本号。

```
	platform :osx, '10.10'
	source 'https://github.com/CocoaPods/Specs.git'

	target 'Your Target' do
	pod 'TXLiteAVSDK_TRTC_Mac'
	end
```

#### 4. 安装与更新 SDK
在终端窗口中输入如下命令执行安装 TRTC SDK：
```
pod install
```
或使用以下命令更新本地库版本：
```
pod update
```

pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。

### 手动集成
1. 下载 [TRTC-SDK ](https://github.com/tencentyun/TRTCSDK/tree/master/Mac) 的 Mac 版本。
2. 打开您的 Xcode 工程项目，将第一步中下载的 framework 导入到您的工程。
3. 选择要运行的 target，选中 Build Phases 项。
![](https://main.qcloudimg.com/raw/b5097f8ac4cbaa5044d92b2a96ea2b9e.jpg)
4. 单击 **Link Binary with Libraries** 项展开，单击底下的+号图标去添加依赖库。
![](https://main.qcloudimg.com/raw/17046154417930f9d31b6452782df55d.jpg)
5. 依次添加所下载的 SDK Framework 及其所需依赖库：`AudioUnit.framework`和`libc++.tbd`。  
   添加后如下图所示：
  ![](https://main.qcloudimg.com/raw/7bddb832347a971f3e69238480fa3e8d.jpg)

## 授权摄像头和麦克风使用权限
使用 SDK 的音视频功能，需要授权麦克风和摄像头的使用权限。在 App 的 Info.plist 中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
- **Privacy - Microphone Usage Description**，并填入麦克风使用目的提示语。
- **Privacy - Camera Usage Description**，并填入摄像头使用目的提示语 。
如下图所示
![](https://main.qcloudimg.com/raw/be76bd6f3f22d31385d871710b51b771.jpg) 


## 引用 TRTC SDK
项目代码中使用 SDK 有两种方式：
- 方式一： 在项目需要使用 SDK API 的文件里，添加模块引用。
```
@import TXLiteAVSDK_TRTC_Mac;
```
- 方式二：在项目需要使用 SDK API 的文件里，引入具体的头文件。
```
#import TXLiteAVSDK_TRTC_Mac/TRTCCloud.h
```


