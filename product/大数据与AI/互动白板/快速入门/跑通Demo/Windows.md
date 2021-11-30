##  跑通 Demo
本文主要介绍如何快速运行腾讯云 TEduBoard Demo。

### 环境要求

- Microsoft Visual Studio 2015及以上版本，推荐使用 Microsoft Visual Studio 2015
- Windows SDK 8.0及以上版本，推荐使用 Windows SDK 8.1 

### 编译运行

1. 进入 Demo 目录下,使用 Visual Studio 打开解决方案文件 `TICDemo.sln`。
2. 在 Visual Studio 中选择“x86”配置(如下图)，然后编译运行即可。
![](https://main.qcloudimg.com/raw/5fec9d2687624a69109c7c89ee752116.png)

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
步骤三：打开 Demo 项目下的配置文件 `config.json`，替换新的 SDKAppID 以及新创建的 UserId 和 UserSig（UserToken）即可。
![](https://main.qcloudimg.com/raw/27fe81a6aff6a85939a72929e02778da.png)
