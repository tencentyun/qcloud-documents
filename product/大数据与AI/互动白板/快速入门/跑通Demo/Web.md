##  跑通 Demo
本文主要介绍如何快速运行腾讯云 TEduBoard Demo。

### 运行

>! 互动课堂 Demo 中集成了音视频能力 TRTC，由于 WebRTC 标准规定 WebRTC 只能运行在 HTTPS 或者 localhost 上，浏览器也目前暂时只兼容 Chrome，所以前期开发建议先在本地搭建运行环境。

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

打开 Demo/js目录下的配置文件 account_dev.js，替换新的 SDKAppID 以及新创建的 UserId 和 UserSig（UserToken）即可。

![](https://main.qcloudimg.com/raw/b8f9ec9e9e82a1874f2532b1e5eb8c61.png)
