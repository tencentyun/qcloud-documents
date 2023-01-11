
为方便 Electron 开发者调试和接入腾讯云游戏多媒体引擎产品 API，本文档主要为您介绍适用于 Electron 开发的工程配置指引。

## 支持的平台

- Windows（PC）

## 导入SDK
### 步骤1：安装 Node.js
1. 根据 Windows 操作系统选择下载最新版本的 Node.js  安装包 Windows Installer (.msi) 64-bit。
2. 打开应用程序列表中的 Node.js command prompt，启动命令行窗口，用于输入后续步骤中的各项命令。

### 步骤2：安装 Electron
在命令行窗口中执行如下命令，安装 Electron，建议版本号 >= 4.0.0。
```sh
$ npm install electron -g

```

### 步骤3：安装 Electron 版的 GME SDK

1. 在您的 Electron 项目中使用 npm 命令安装 Gme SDK 包：
```sh
$ npm install gme-electron-sdk@latest --save

```
2. 在项目脚本里引入模块并使用：
```
const { GmeContext } = require('gme-electron-sdk');
// import gmesdk from 'gme-electron-sdk';
gmeContext = new GmeContext();
// 获取 SDK 版本号
gmeContext.GetSDKVersion();

```

### 步骤4：打包可执行程序

安装打包工具：推荐使用Electron Forge，您可以执行如下命令

1. 将 Electron Forge 添加到您应用的开发依赖中，并使用其"import"命令设置 Forge 的脚手架：
```sh
npm install --save-dev @electron-forge/cli
npx electron-forge import
```
2. 使用 Forge 的 make 命令来创建可分发的应用程序：
```sh
npm run make
```
