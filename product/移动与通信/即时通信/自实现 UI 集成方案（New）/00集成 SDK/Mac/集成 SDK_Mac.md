
本文主要介绍如何快速地将腾讯云 IM SDK（Mac）集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求
- Xcode 9.0+。
- OS X 10.10+ 的 Mac 真机。
- 项目已配置有效的开发者签名。

## 集成 IM SDK
您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK 再将其导入到您当前的工程项目中。

### CocoaPods 自动加载
#### 1. 安装 CocoaPods
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```

#### 2. 创建 Podfile 文件
进入项目所在路径输入以下命令行，之后项目路径下会出现一个 Podfile 文件。
```
pod init
```

#### 3. 编辑 Podfile 文件
编辑 Podfile 文件，按如下方式设置：

```
platform :macos, '10.10'
source 'https://github.com/CocoaPods/Specs.git'

target 'mac_test' do
pod 'TXIMSDK_Mac'
end
```

#### 4. 更新并安装 SDK
在终端窗口中输入如下命令以更新本地库文件，并安装 TXIMSDK_Mac：
```
pod install
```
或使用以下命令更新本地库版本:
```
pod update
```

pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。

### 手动集成
#### 1. 从 [Github](https://github.com/tencentyun/TIMSDK) 获取 SDK 的下载地址：
![](https://main.qcloudimg.com/raw/8a68131164419de35a8780831b096502.png)

- ImSDKForMac.framework 为 IM SDK 的核心动态库文件。

| 包名 | 介绍 |  ipa增量 |
| --- | --- | --- |
| ImSDKForMac.framework |即时通信 IM 功能包 | 1.4M|

#### 2. 创建工程
**创建一个新的工程**：
![](https://main.qcloudimg.com/raw/7dd7a0f99893f52c63fd3144794a12cd.png)

**填入工程名**：

![](https://main.qcloudimg.com/raw/39f16307b69c8f0d766349e5ed201ef4.png)

#### 2. 集成 IM SDK

**添加依赖库：**选中 Demo 的**Target**，在**General**面板中的 **Embedded Binaries**和**Linked Frameworks and Libraries**添加依赖库。

![](https://main.qcloudimg.com/raw/440dd55e50d2fe52e1d83ed0aa4284be.png)

**添加依赖库：**
```
ImSDKForMac.framework
```
>! 需要在**Build Setting**-**Other Linker Flags**添加 `-ObjC`。

## 引用 IM SDK
项目代码中使用 SDK 有两种方式：
- 方式一： 在 Xcode -> Build Setting -> Herader Search Paths 设置 ImSDKForMac.framework/Headers 路径，在项目需要使用 SDK API 的文件里，直接引用头文件"ImSDK.h"。
```
#import "ImSDK.h"
```

- 方式二：在项目需要使用 SDK API 的文件里，引入具体的头文件 < ImSDKForMac/ImSDK.h >。
```
#import <ImSDKForMac/ImSDK.h>
```

