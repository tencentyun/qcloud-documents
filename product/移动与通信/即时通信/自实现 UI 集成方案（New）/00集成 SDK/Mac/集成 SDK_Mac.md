本文主要介绍如何快速将腾讯云即时通信 IM SDK 集成到您的 Mac 项目中。

## 开发环境要求

- Xcode 9.0+。
- OS X 10.10+ 的 Mac 真机。
- 项目已配置有效的开发者签名。

## 集成 IM SDK

您可以选择使用 CocoaPods 自动加载的方式，或者先下载 SDK 再将其导入到您当前的工程项目中。

### CocoaPods 自动加载

#### 1. 安装 CocoaPods

在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：

```shell
sudo gem install cocoapods
```

#### 2. 创建 Podfile 文件

进入项目所在路径输入以下命令行，之后项目路径下会出现一个 Podfile 文件。

```ruby
pod init
```

#### 3. 编辑 Podfile 文件

如果使用增强版 SDK，请您按照如下方式设置 Podfile 文件：

```ruby
platform :macos, '10.10'
source 'https://github.com/CocoaPods/Specs.git'

target 'mac_test' do
pod 'TXIMSDK_Plus_Mac'
end
```

如果使用增强版 Pro SDK，请您按照如下方式设置 Podfile 文件：

```ruby
platform :macos, '10.10'
source 'https://github.com/CocoaPods/Specs.git'

target 'mac_test' do
pod 'TXIMSDK_Plus_Pro_Mac'
end
```

#### 4. 更新并安装 SDK

在终端窗口中输入如下命令以更新本地库文件，并安装 TXIMSDK_Plus_Mac：

```ruby
pod install
```

或使用以下命令更新本地库版本:

```ruby
pod update
```

pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。

> ? 如果 pod install 和 pod update 命令执行失败，提示版本不匹配，请先使用 pod repo update 更新本地 cocoapods 库。

### 手动集成

#### 1. 从 [Github]() 获取 SDK 的下载地址：

![](https://qcloudimg.tencent-cloud.cn/raw/f3a622cfde94381e793ade73cfedfc8b.png)

**ImSDKForMac_Plus.framework 为 IM SDK 的核心动态库文件。**

| 包名                       | 介绍               | ipa增量 |
| -------------------------- | ------------------ | ------- |
| ImSDKForMac_Plus.framework | 即时通信 IM 功能包 | 1.4M    |

#### 2. 创建工程

**创建一个新的工程**：
![](https://qcloudimg.tencent-cloud.cn/raw/01e44e524be7c812751266f70c6d799c.png)

**填入工程名**：

![](https://main.qcloudimg.com/raw/39f16307b69c8f0d766349e5ed201ef4.png)

#### 3. 集成 IM SDK

**添加依赖库：**

- 首先将 ImSDKForMac_Plus.framework 拖入您的工程中；
- 其次选中工程的**Target**，在 **General** 面板中的 **Frameworks, Libraries, and Embedded Content** 中添加依赖库。

![](https://qcloudimg.tencent-cloud.cn/raw/62a9d07ac2a915019aefabbbd287fc1e.png)

如果运行后，提示 `image not found` 并出现如下图的 crash，此时需要在 **General** 面板中的 **Frameworks, Libraries, and Embedded Content** 中将 **Embed** 改成 **Embed Without Signing**。

![](https://qcloudimg.tencent-cloud.cn/raw/18535db0c56c54f7383738a683d24918.png)





## 引用 IM SDK

项目代码中使用 SDK 有两种方式：

- 方式一： 在 Xcode > Build Setting > Header Search Paths 设置 ImSDKForMac_Plus.framework/Headers 路径，在项目需要使用 SDK API 的文件里，直接引用头文件"ImSDKForMac_Plus.h"。
```objectivec
#import "ImSDKForMac_Plus.h"
```
- 方式二：在项目需要使用 SDK API 的文件里，引入具体的头文件 <ImSDKForMac_Plus/ImSDKForMac_Plus.h>。
```objective-c
#import <ImSDKForMac_Plus/ImSDKForMac_Plus.h>
```
