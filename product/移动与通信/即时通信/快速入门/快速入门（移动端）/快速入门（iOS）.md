本文主要介绍如何快速运行腾讯云即时通信 IM Demo（iOS）。以下视频将帮助您快速入门：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/course-3130-56316"></iframe></div>

## 操作步骤
[](id:step1)
### 步骤1：创建应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
>同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/febed2f15dee6ff09f066ba228c7fc27.png)
3. 创建完成后，可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、创建时间、标签以及到期时间。请记录 SDKAppID 信息。
![](https://qcloudimg.tencent-cloud.cn/raw/853d2c3c0d5887dadc254eb0e03a215e.png)


[](id:step2)
### 步骤2：获取密钥信息
1. 单击目标应用卡片，进入应用的基础配置页面。
![](https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png)
2. 在**基本信息**区域，单击**显示密钥**，复制并保存密钥信息。
>!请妥善保管密钥信息，谨防泄露。

[](id:step3)
### 步骤3：下载并配置 Demo 源码

1. 下载即时通信 IM Demo 工程，具体下载地址请参见 [SDK 下载](https://cloud.tencent.com/document/product/269/36887)。
>?为尊重表情设计版权，下载的 Demo 工程中不包含大表情元素切图，您可以使用自己本地表情包来配置代码。未授权使用 IM Demo 中的表情包可能会构成设计侵权。
2. 打开所属终端目录的工程，找到对应的 `GenerateTestUserSig` 文件。
 iOS 路径：iOS/Demo/TUIKitDemo/Private/GenerateTestUserSig.h
 Mac 路径：Mac/Demo/TUIKitDemo/Debug/GenerateTestUserSig.h
3. 设置`GenerateTestUserSig`文件中的相关参数：
 - SDKAPPID：请设置为 [步骤1](#step1) 中获取的实际应用 SDKAppID。
 - SECRETKEY：请设置为 [步骤2](#step2) 中获取的实际密钥信息。
 ![](https://qcloudimg.tencent-cloud.cn/raw/addadc8b9b34c83794ad59034e3a7c23.png)


>!本文提到的获取 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig)。

[](id:step4)
### 步骤4：编译运行
可参见 [步骤3](#step3) 克隆的 Demo 工程中对应目录下的`README.md`文件。

1. 终端执行以下命令，检查 pod 版本。
```
pod --version
```
若提示 pod 不存在，或 pod 版本小于 1.7.5，请执行以下命令安装最新 pod。
```
//更换 gem 源
gem sources --remove https://rubygems.org/
gem sources --add https://gems.ruby-china.com/
//安装 pod
sudo gem install cocoapods -n /usr/local/bin
//如果安装了多个 Xcode ，请使用下面的命令选择 Xcode 版本（一般选择最新的 Xcode 版本）
sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
//更新 pod 本地库
pod setup
```
2. 终端执行以下命令，安装依赖库。
```
//iOS
cd iOS/TUIKitDemo
pod install
//Mac
cd Mac/TUIKitDemo
pod install
```
 如果安装失败，执行以下命令更新本地的 CocoaPods 仓库列表。
 ```bash
 pod repo update
 ```
3. 编译运行：
 - iOS 进入 iOS/TUIKitDemo 文件夹，打开`TUIKitDemo.xcworkspace`编译运行。
 - Mac 进入Mac/TUIKitDemo 文件夹，打开`TUIKitDemo.xcworkspace`编译运行。

>!Demo 默认集成了音视频通话功能，由于该功能依赖的音视频 SDK 暂不支持模拟器，请使用真机调试或者运行 Demo。


## 进阶功能
- [UI 界面库](https://cloud.tencent.com/document/product/269/37190)
- [开启视频通话](https://cloud.tencent.com/document/product/269/39167)

## 相关文档
- [价格说明](https://cloud.tencent.com/document/product/269/11673)
- [折扣活动](https://cloud.tencent.com/document/product/269/46181)
