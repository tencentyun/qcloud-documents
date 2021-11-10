##  跑通 Demo
本文主要介绍如何快速运行腾讯云 TEduBoard Demo。

### 账号配置

#### 1. 创建白板应用

步骤一：登录 [互动白板控制台](https://console.cloud.tencent.com/tiw)，在左侧导航栏单击**应用管理**，进入互动白板应用列表。
步骤二：单击**创建应用**，进入创建新应用对话框。
步骤三：您可以选择创建一个新应用或从已有的 IM 应用中导入，文档转码和实时录制资源存储桶配置请参考 [存储桶配置](https://cloud.tencent.com/document/product/1137/45256)，回调配置请参考 [回调配置](https://cloud.tencent.com/document/product/1137/45255)，如果您暂时不需要使用文档转码和实时录制功能，可以在创建应用对话框中关闭相应功能，您可以在**应用配置**里随时配置资源存储桶打开该文档转码或实时录制功能。

![](https://main.qcloudimg.com/raw/ee28f8f7c5d0da78044e3a55b636a30b.png)

#### 2. 配置测试账号

>!该方式生成 userSig 的方式只建议在开发阶段使用，生产环境建议使用服务端生成 userSig

步骤一：登录 [即时通讯控制台](https://console.cloud.tencent.com/im)，单击 SDKAppID 对应的应用。
步骤二：在**基本配置**>**基本信息**中获取 SDKAppID 和密钥。（注意保密您的密钥）
![](https://main.qcloudimg.com/raw/927dbd204b483c778a73eabd2492033e.png)
步骤三：打开 src/config/index.js 文件，将该文件的 sdkAppId 和 secretKey 替换为您自己的信息即可。
![](https://main.qcloudimg.com/raw/97031b62881d1f16afdb7226c5033ba6.png)

如果您需要体验完整功能，请根据 Demo 源码配置文件的提示进行配置。

### 运行

#### 项目安装
```
npm install
```

#### 项目运行
```
npm run serve
```
