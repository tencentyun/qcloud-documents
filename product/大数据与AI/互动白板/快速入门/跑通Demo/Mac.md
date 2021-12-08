##  跑通 Demo
本文主要介绍如何快速运行腾讯云 TEduBoard Demo。

### 环境要求

- Xcode 9.0+
- OS X 10.10+ 的 Mac 真机
- 项目已配置有效的开发者签名 

### 编译运行

1. 在终端窗口进入 Demo Podfile 文件所在目录。
2. 执行`pod install`命令安装 TEduBoard SDK、TIMSDK、TRTC SDK，或执行`pod update`命令，更新本地库版本。
3. 使用 XCode（9.0及以上的版本）打开源码目录下的 .xcworkspace 工程，编译并运行即可。

### 账号配置

Demo 的测试账号为公共账号，多人同时登录会被强制退出，为保证您的顺利体验，请重新配置账号。

#### 1. 创建白板应用

步骤一：登录 [互动白板控制台](https://console.cloud.tencent.com/tiw)，在左侧导航栏单击**应用管理**，进入互动白板应用列表。
步骤二：单击**创建应用**，进入创建新应用对话框。
步骤三：您可以选择创建一个新应用或从已有的 IM 应用中导入，文档转码和实时录制资源存储桶配置请参考 [存储桶配置](https://cloud.tencent.com/document/product/1137/45256)，回调配置请参考 [回调配置](https://cloud.tencent.com/document/product/1137/45255)，如果您暂时不需要使用文档转码和实时录制功能，可以在创建应用对话框中关闭相应功能，您可以在**应用配置**里随时配置资源存储桶打开该文档转码或实时录制功能。

![](https://main.qcloudimg.com/raw/ee28f8f7c5d0da78044e3a55b636a30b.png)


#### 2. 开通音视频服务

Demo 集成了实时音视频 TRTC SDK，为保证音视频功能的正常使用，请开通音视频服务。

步骤一： 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
步骤二： 单击**开通腾讯实时音视频服务**区域的**立即开通**。
步骤三： 在弹出的开通实时音视频 TRTC 服务对话框中，单击**确认**。

系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 创建一个与相同 SDKAppID 的实时音视频应用，互动白板，IM，实时音视频三者的账号与鉴权可复用。

![](https://main.qcloudimg.com/raw/15e5dda6aa294b4860c73433d69f01b6.png)

#### 3. 配置测试账号

步骤一：登录 [即时通讯控制台](https://console.cloud.tencent.com/im)，单击 SDKAppID 对应的应用。
步骤二：单击**开发辅助工具**>**UserSig 工具**，输入测试用户名，单击**生成签名（UserSig）**。
![](https://main.qcloudimg.com/raw/a2f24861652c760cbec05087dfe0d5df.jpg)
步骤三：打开 Demo Config 目录下的配置文件 config.json，替换新的 SDKAppID 以及新创建的 UserId 和 UserSig（UserToken）即可。
![](https://main.qcloudimg.com/raw/fc3f36d528c002aa30a032a924fecf5a.jpg)
