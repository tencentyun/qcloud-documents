
本文主要介绍如何快速地将腾讯云 IM SDK(iOS) 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 开发环境要求
- Xcode 9.0+。
- iOS 8.0 以上的 iPhone 或者 iPad 真机。
- 项目已配置有效的开发者签名。

## 集成 IM SDK
您可以选择使用 CocoaPods 自动加载的方式，或者先 [下载](https://github.com/tencentyun/TIMSDK/tree/master/iOS/IMSDK) SDK，再将其导入到您当前的工程项目中。

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
如果使用基础版 SDK，请您按照如下方式设置 Podfile 文件：

```
platform :ios, '8.0'
source 'https://github.com/CocoaPods/Specs.git'

target 'App' do
pod 'TXIMSDK_iOS'
end
```

如果使用增强版 SDK，请您按照如下方式设置 Podfile 文件：
```
platform :ios, '8.0'
source 'https://github.com/CocoaPods/Specs.git'

target 'App' do
pod 'TXIMSDK_Plus_iOS'
end
```

如果使用增强版 bitcode 版本 SDK，请您按照如下方式设置 Podfile 文件：
```
platform :ios, '8.0'
source 'https://github.com/CocoaPods/Specs.git'

target 'App' do
pod 'TXIMSDK_Plus_iOS_Bitcode'
end
```

如果使用增强版 xcframework 版本 SDK，请您按照如下方式设置 Podfile 文件：
```
platform :ios, '8.0'
source 'https://github.com/CocoaPods/Specs.git'

target 'App' do
pod 'TXIMSDK_Plus_iOS_XCFramework'
end
```

如果使用增强版 xcframework 版本 SDK（支持 bitcode），请您按照如下方式设置 Podfile 文件：
```
platform :ios, '8.0'
source 'https://github.com/CocoaPods/Specs.git'

target 'App' do
pod 'TXIMSDK_Plus_iOS_Bitcode_XCFramework'
end
```

#### 4. 更新并安装 SDK
在终端窗口中输入如下命令以更新本地库文件，并安装 TXIMSDK：
```
pod install
```
或使用以下命令更新本地库版本：
```
pod update
```

pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。
>?若 pod 搜索失败，建议尝试更新 pod 的本地 repo 缓存。更新命令如下：
>```
pod setup
pod repo update
rm ~/Library/Caches/CocoaPods/search_index.json
```

### 手动集成
#### 1. 下载 SDK
从 [Github](https://github.com/tencentyun/TIMSDK/tree/master/iOS/IMSDK) 下载最新版本 SDK。

- ImSDK.framework 和 ImSDK_Plus.framework 是 IM SDK 的核心动态库文件。
<table>
<thead>
<tr>
<th>包名</th>
<th>介绍</th>
</tr>
</thead>
<tbody><tr>
<td>ImSDK.framework</td>
<td>基础版 IM 功能包</td>
</tr>
<tr>
<td>ImSDK_Plus.framework</td>
<td>增强版 IM 功能包</td>
</tr>
</tbody></table>
- TXLiteAVSDK_UGC.framework 是腾讯云短视频（UGC）SDK，用于实现即时通信 IM 中的短视频收发能力，为可选组件。
<table>
<thead>
<tr>
<th>包名</th>
<th>介绍</th>
<th>功能</th>
</tr>
</thead>
<tbody><tr>
<td>TXLiteAVSDK_UGC.framework</td>
<td>小视频录制、编辑能力扩展包</td>
<td>包含小视频录制功能、小视频编辑功能，详情请参阅 <a href="https://cloud.tencent.com/product/ugsv">短视频 SDK 文档</a></td>
</tr>
</tbody></table>

#### 2. 创建工程
**创建一个新工程**：
![](https://main.qcloudimg.com/raw/de4a148165dbfafd1f403e88018b0012.jpg)
**填入工程名**（例如 IMDemo）：
![](https://main.qcloudimg.com/raw/d9aebb74fe2fb4740c88e7cbda31987a.jpg)

#### 3. 集成 IM SDK

**添加依赖库：**选中 IMDemo 的**Target**，在**General**面板中的 **Embedded Binaries**和**Linked Frameworks and Libraries**添加依赖库。若使用基础版 SDK，请选择 ImSDK.framework；若使用增强版 SDK，请选择 ImSDK_Plus.framework。
![](https://main.qcloudimg.com/raw/3a1cc30c280362be2d99058dde347d4f.png)
**设置链接参数：**在**Build Setting**>**Other Linker Flags**添加 `-ObjC`。
>?手动集成需要在**TARGET**>**General**>**Frameworks**> Libraries and Embedded Content，将 ImSDK.framework 修改为 Embed&Sing。
## 引用 IM SDK
项目代码中使用 SDK 有两种方式：

#### 方式一
在 Xcode > Build Setting > Header Search Paths 设置 SDK 头文件的路径，然后在项目需要使用 SDK API 的文件里，引入具体的头文件。

- 如果使用基础版，请按照如下方式引用头文件：
```
#import "ImSDK.h"
```
- 如果使用增强版，请按照如下方式引用头文件：
```
#import "ImSDK_Plus.h"
```

#### 方式二
 
在项目需要使用 SDK API 的文件里，引入具体的头文件。
- 如果使用基础版，请按照如下方式引用头文件：
```
#import <ImSDK/ImSDK.h>
```
- 如果使用增强版，请按照如下方式引用头文件：
```
#import <ImSDK_Plus/ImSDK_Plus.h>
```
