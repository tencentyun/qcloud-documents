##  跑通 Demo
本文主要介绍如何快速运行腾讯云 TEduBoard Demo。

### 环境要求

- Xcode 9.0+
- OS X 10.10+ 的 Mac 真机
- 项目已配置有效的开发者签名

### 编译运行

1. 在终端窗口进入 Demo Podfile 文件所在目录
2. 执行`pod install`命令安装 TEduBoard SDK、TIMSDK、TRTC SDK，或执行`pod update`命令，更新本地库版本。
3. 使用 XCode（9.0及以上的版本）打开源码目录下的 .xcworkspace 工程，编译并运行即可。

### 账号配置

Demo 的测试账号为公共账号，多人同时登录会被强制退出，为保证您的顺利体验，请重新配置账号。

#### 1. 创建音视频应用

Demo 集成了实时音视频 TRTC SDK，为保证音视频功能的正常使用，请创建新应用。

步骤一：登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)，单击【应用管理】->【创建应用】。

步骤二：输入应用名称，单击【确定】，记录自动生成的应用标识 SDKAppID。

![](https://main.qcloudimg.com/raw/287edbf8848919054e01d51704369aa3.jpg)

#### 2. 创建即时通讯应用

在`创建音视频应用`后，会默认创建相同 SDKAppID 的即时通讯应用。

步骤一：登录 [即时通讯控制台](https://console.cloud.tencent.com/im)，单击 SDKAppID 对应的应用。

步骤二：单击【开发辅助工具】->【 UserSig 工具】，输入测试用户名，单击【生成签名（UserSig）】。

![](https://main.qcloudimg.com/raw/a2f24861652c760cbec05087dfe0d5df.jpg)

#### 3. 配置测试账号

打开 Demo Config 目录下的配置文件 config.json，替换新的 SDKAppID 以及新创建的 UserId 和 UserSig（UserToken）即可。

![](https://main.qcloudimg.com/raw/fc3f36d528c002aa30a032a924fecf5a.jpg)
