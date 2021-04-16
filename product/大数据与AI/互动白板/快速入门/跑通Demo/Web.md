##  跑通 Demo
本文主要介绍如何快速运行腾讯云 TEduBoard Demo。

### 环境

> 互动课堂 Demo 中集成了音视频能力 TRTC，由于 WebRTC 标准规定 WebRTC 只能运行在 HTTPS 或者 localhost 上，浏览器也目前只兼容 Chrome，所以前期开发建议先在本地搭建运行环境。

### 账号配置

#### 1. 创建白板应用

步骤一：登录 [互动白板控制台](https://console.cloud.tencent.com/tiw)，在左侧导航栏单击【应用管理】，进入互动白板应用列表。
步骤二：单击【创建应用】，进入创建新应用对话框。
步骤三：您可以选择创建一个新应用或从已有的 IM 应用中导入，文档转码和实时录制资源存储桶配置请参考 [存储桶配置](https://cloud.tencent.com/document/product/1137/45256)，回调配置请参考 [回调配置](https://cloud.tencent.com/document/product/1137/45255)，如果您暂时不需要使用文档转码和实时录制功能，可以在创建应用对话框中关闭相应功能，您可以在【应用配置】里随时配置资源存储桶打开该文档转码或实时录制功能。

![](https://main.qcloudimg.com/raw/ee28f8f7c5d0da78044e3a55b636a30b.png)


#### 2. 开通音视频服务

Demo 集成了实时音视频 TRTC SDK，为保证音视频功能的正常使用，请开通音视频服务。

步骤一： 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
步骤二： 单击【开通腾讯实时音视频服务】区域的【立即开通】。
步骤三： 在弹出的开通实时音视频 TRTC 服务对话框中，单击【确认】。

系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 创建一个与相同 SDKAppID 的实时音视频应用，互动白板，IM，实时音视频三者的账号与鉴权可复用。

![](https://main.qcloudimg.com/raw/15e5dda6aa294b4860c73433d69f01b6.png)

#### 3. 配置测试账号

> 注意：该方式生成 userSig 的方式只建议在开发阶段使用，生产环境建议使用服务端生成 userSig

步骤一：登录 [即时通讯控制台](https://console.cloud.tencent.com/im)，单击 SDKAppID 对应的应用。
步骤二：在【基本配置】->【 基本信息】中获取 SDKAppID 和密钥。（注意保密您的密钥）
![](https://main.qcloudimg.com/raw/927dbd204b483c778a73eabd2492033e.png)
步骤三：打开 demo/js/generateusersig/GenerateTestUserSig.js文件，将该文件的 SDKAPPID 和 SECRETKEY 替换为您自己的信息即可。
![](https://main.qcloudimg.com/raw/7674d60ff2aff8042bdec637f8cfeffb.png)


### 运行

#### 1. 安装 live-server

假设您已经安装了 npm，如果还没有安装 npm，请自行 google 安装 npm。

```
npm install -g live-server
```

#### 2. 在 Demo 目录下执行 live-server 命令

命令运行完成后，会自动在浏览器中打开 Demo 首页
```
live-server
```

您也可以使用其他 Web 服务器搭建环境。
