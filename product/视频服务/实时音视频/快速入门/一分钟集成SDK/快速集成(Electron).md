本文主要介绍如何快速地将腾讯云 TRTC Electron SDK 集成到您的项目中。

## 支持的平台
-  Windows(PC)
-  Mac

## 环境要求

#### Windows 
1. 根据 Windows 操作系统选择下载最新版本的 [Node.js](https://nodejs.org/en/download/) 安装包 Windows Installer (.msi) 64-bit 或 Windows Installer (.msi) 32-bit。
2. 安装 Node.js。

#### Mac
1. 打开终端（Terminal）窗口，执行以下命令安装 Homebrew，如果已经安装请跳过此步骤。
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. 执行以下命令，安装 Node.js。
```
$ brew install node
```
3. 如果使用 Homebrew 的默认地址安装 Node.js 较慢，您可以考虑替换为国内镜像地址。
```cmd
$ cd `brew --repo`
$ git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
$ brew update
```

## 集成 TRTC Electron SDK

确保您的项目已经集成 Electron，在您的项目目录下的 package.json 检查是否含有以下代码：
```
"devDependencies": {
	"electron": "x.x.x" //版本需要4.0.0以上
}
```

在您的 Electron 项目中使用 npm 命令安装 SDK 包：

```
npm install trtc-electron-sdk@latest --save-dev
```

在项目目录下的 package.json 中检查 SDK 是否安装成功：
```
"dependencies": {
    "trtc-electron-sdk": "x.x.x"
}
```
>?TRTC Electron SDK 最新版可在 [trtc-electron-sdk](https://www.npmjs.com/package/trtc-electron-sdk) 中查看

在项目脚本里引入模块并使用：

```javascript
const TRTCCloud = require('trtc-electron-sdk');
this.rtcCloud = new TRTCCloud();
// 获取 SDK 版本号
this.rtcCloud.getSDKVersion();
```

从v7.0.149起，TRTC Electron SDK 增加了 trtc.d.ts 文件，方便使用 typescript 的开发者

```javascript
// 开启了 ES Module 融合模式 (esModuleInterop=true)
import * as trtc_namespace from 'trtc-electron-sdk';

const TRTCCloud = require('trtc-electron-sdk');

const rtcCloud: trtc_namespace.TRTCCloud = new TRTCCloud();
// 获取 SDK 版本号
rtcCloud.getSDKVersion();
```

## 常见问题

### 1. 防火墙有什么限制？

由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。
