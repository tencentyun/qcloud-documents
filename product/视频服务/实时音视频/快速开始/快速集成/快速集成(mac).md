本文主要介绍如何快速地将腾讯云 TRTC SDK 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。


## 开发环境要求
- Xcode 9.0+
- macOS 10.10 以上的系统

## 集成 TRTC SDK
您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK 再将其导入到您当前的工程项目中。

### CocoaPods
**1. 安装 CocoaPods**
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）
```
sudo gem install cocoapods
```

**2. 创建 Podfile 文件**
进入项目所在路径，然后输入以下命令行，之后项目路径下会出现一个 Podfile 文件。
```
pod init
```

**3. 编辑 Podfile 文件**
编辑 Podfile 文件，有如下有两种设置方式

方式一：使用腾讯云 LiteAV SDK 的pod路径
```
platform :osx, '10.10'

target 'test' do
pod 'TXLiteAVSDK_TRTC_Mac', :podspec => 'http://pod-1252463788.cosgz.myqcloud.com/liteavsdkspec/TXLiteAVSDK_TRTC_Mac.podspec'
end
```
方案二：使用Pod官方源，支持选择版本号

```
platform :osx, '10.10'
source 'https://github.com/CocoaPods/Specs.git'

target 'test' do
pod 'TXLiteAVSDK_TRTC_Mac'
end
```

**4. 安装与更新 SDK**
在终端窗口中输入如下命令执行安装 TRTC SDK
```
pod install
```
或
```
pod update
```


### 手动集成
**1. 下载 TRTC-SDK**

**2. 在 Link Binary with Libraries 中添加所下载的SDK Framework，并添加依赖库**
- AudioUnit
- libc++

### 授权摄像头和麦克风
在App工程的Info.plist中添加以下两项，分别对应麦克风和摄像头在系统弹出授权对话框时的提示信息。
- NSMicrophoneUsageDescription
- NSCameraUsageDescription

## 验证
在工程中调用获取SDK版本信息接口，以验证工程设置是否正确
**1. 头文件引用**
使用模块引用方式(推荐)，
```
@import TXLiteAVSDK_TRTC_Mac
```
或者引用具体的头文件:

```
#import TXLiteAVSDK_TRTC_Mac/TRTCCloud.h
```
**2.添加调用代码**
在viewDidLoad方法中添加代码：
```
- (void)viewDidLoad {
[super viewDidLoad];
// 打印SDK的版本信息
NSLog(@"SDK Version = %@", [TRTCCloud getSDKVersion]);
}
```
**3.编译运行**
如果前面各个步骤都操作正确的话，工程应该可以顺利编译通过。在Debug模式下运行APP，Xcode的Console窗格会打印出SDK的版本信息

```
2018-12-28 20:33:30.263568+0800 TRTCDemo[92809:15254997] SDK Version = 5.4.10
```
至此，确认工程配置完成。

