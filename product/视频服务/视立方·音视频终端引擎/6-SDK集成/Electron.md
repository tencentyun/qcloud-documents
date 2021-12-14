本文主要介绍如何快速地在 Electron 端将腾讯云视立方 SDK 集成到您的项目中，腾讯云视立方 SDK Electron 端仅**音视频通话 TRTC 版本**支持。按照如下步骤进行配置，就可以完成 SDK 在 Electron 端的集成工作。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | - | - | - | &#10003; | - | - |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。


## 支持的平台
-  Windows（PC）
-  Mac

## 集成 TRTC Electron SDK

### 步骤1：安装 Node.js
<dx-tabs>
::: Windows\s平台安装指引
1. 根据 Windows 操作系统选择下载最新版本的 [Node.js](https://nodejs.org/en/download/)  安装包 **Windows Installer (.msi) 64-bit**。
2. 打开应用程序列表中的 Node.js command prompt，启动命令行窗口，用于输入后续步骤中的各项命令。
![](https://main.qcloudimg.com/raw/148c49336f0d89829736af81de305de4.png)
:::
::: MacOS\s平台安装指引
1. 打开终端（Terminal）窗口，执行以下命令安装 Homebrew，如果已经安装请跳过此步骤。
<dx-codeblock>
::: shell shell
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
:::
</dx-codeblock>
2. 执行以下命令，安装 Node.js，必须大于 10.0 版本。
```shell
$ brew install node
```
3. 如果使用 Homebrew 的默认地址安装 Node.js 较慢，您可以考虑替换为国内镜像地址。
```shell
$ cd `brew --repo`
$ git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
$ brew update
```
:::
</dx-tabs>

### 步骤2：安装 Electron
在命令行窗口中执行如下命令，安装 Electron，建议版本号 >= 4.0.0。
```shell
$ npm install electron@latest --save-dev
```
>?在国内网络安装 Electron 可能会遇到一系列下载过程的障碍。如果您安装 Electron 没有成功，可以参考 [Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668) 进行处理。

### 步骤3：安装 Electron 版的腾讯云视立方 TRTC SDK
1. 在您的 Electron 项目中使用 npm 命令安装 SDK 包：
```
	$ npm install trtc-electron-sdk@latest --save
```
>? TRTC Electron SDK 最新版可在 [trtc-electron-sdk](https://www.npmjs.com/package/trtc-electron-sdk) 中查看。
2. 在项目脚本里引入模块并使用：
```javascript
const TRTCCloud = require('trtc-electron-sdk').default;
// import TRTCCloud from 'trtc-electron-sdk';
this.rtcCloud = new TRTCCloud();
// 获取 SDK 版本号
this.rtcCloud.getSDKVersion();
```
	从 Electron SDK v7.9.348起，TRTC Electron SDK 增加了 trtc.d.ts 文件，方便使用 TypeScript 的开发者：
``` 
import TRTCCloud from 'trtc-electron-sdk';
const rtcCloud: TRTCCloud = new TRTCCloud();
// 获取 SDK 版本号
rtcCloud.getSDKVersion();
```

## 打包可执行程序

### 步骤1：安装打包工具
1. 推荐使用打包工具 `electron-builder` 进行打包，您可以执行如下命令安装 `electron-builder`：
```bash
$ npm install electron-builder@latest --save-dev
```
2. 为了正确打包 Electron 版本的 TRTC SDK（也就是 `trtc_electron_sdk.node` 文件），您还需要执行如下命令以安装 `native-ext-loader` 工具：
```bash
$ npm install native-ext-loader@latest --save-dev
```

###  步骤2：修改 webpack.config.js 配置
`webpack.config.js` 包含了项目构建的配置信息，`webpack.config.js` 文件的位置如下：
- 通常情况下，`webpack.config.js` 位于项目的根目录。
- 使用 `create-react-app` 创建项目的情况下，此配置文件为 `node_modules/react-scripts/config/webpack.config.js`。
- 使用 `vue-cli` 创建项目的情况下，webpack 的配置存放在 `vue.config.js` 配置中的 `configureWebpack` 属性中。
- 如您的工程文件经过了定制化，还请自行查找 webpack 配置。

#### 操作说明
1. 首先使 `webpack.config.js` 在构建时可以接收名为 `--target_platform` 的命令行参数，以使代码构建过程按不同的目标平台特点正确打包，在 `module.exports` 之前添加以下代码：
```
const os = require('os');
const targetPlatform = (function(){
	let target = os.platform();
	for (let i=0; i<process.argv.length; i++) {
		if (process.argv[i].includes('--target_platform=')) {
			target = process.argv[i].replace('--target_platform=', '');
			break;
		}
	}
	if (!['win32', 'darwin'].includes) target = os.platform();
	return target;
})();
```
>! `os.platform()` 返回的结果中，"darwin" 表示 Mac 平台。"win32" 表示 Windows 平台，不论 64 位还是 32 位。
2. 然后在 `rules` 选项中添加以下配置，`targetPlatform` 变量可以使 `rewritePath` 可以根据不同的目标平台切换不同的配置：
```js
rules: [
	{ 
		test: /\.node$/, 
		loader: 'native-ext-loader', 
		options: { 
			rewritePath: targetPlatform === 'win32' ? './resources' : '../Resources' 
		} 
	},
]
```
	该配置的含义是：
	- 打包 Windows 下的 `.exe` 文件时，让 `native-ext-loader` 到 `[应用程序根目录]/resources` 目录下加载 TRTC SDK。
	- 打包 Mac 下的 `.dmg` 时，让 `native-ext-loader` 到 `[应用程序目录]/Contents/Frameworsk/../Resources` 目录下加载 TRTC SDK。

还需要在 `package.json` 中的构建脚本中添加 `--target_platform` 参数，将在下一步进行。

###  步骤3：修改 package.json 配置
`package.json` 位于项目的根目录，其中包含了项目打包所必须的信息。但默认情况下，`package.json`  中的路径是需要修改才能顺利实现打包的，我们可以按如下步骤修改此文件： 

1. 修改 `main` 配置。
<dx-codeblock>
::: javascript javascript
// 多数情况下，main 文件名称可以任意配置，例如 TRTCSimpleDemo 中的可以配置为：
"main": "main.electron.js",

// 但是，使用 create-react-app 脚手架创建的项目，main 文件必须配置为：
"main": "public/electron.js",
:::
</dx-codeblock>
2. 复制以下 `build` 配置，添加到您的 `package.json` 文件中，这是 `electron-builder` 需要读取到的配置信息。
<dx-codeblock>
::: json json
"build": {
    "appId": "[appId 请自行定义]",
    "directories": {
			"output": "./bin"
    },
    "win": {
    "extraFiles": [
      {
        "from": "node_modules/trtc-electron-sdk/build/Release/",
        "to": "./resources",
        "filter": ["**/*"]
      }
    ]
    },
    "mac": {
    "extraFiles": [
      { 
        "from": "node_modules/trtc-electron-sdk/build/Release/trtc_electron_sdk.node", 
        "to": "./Resources" 
      }
    ]
    }
},
:::
</dx-codeblock>
3. 在 `scripts` 节点下添加以下构建和打包的命令脚本：
 本文以 `create-react-app` 和 `vue-cli` 项目为例，其它工具创建的项目也可以参考此配置：
<dx-codeblock>
::: json json
// create-react-app 项目请使用此配置
"scripts": {
	"build:mac": "react-scripts build --target_platform=darwin",
    "build:win": "react-scripts build --target_platform=win32",
    "compile:mac": "node_modules/.bin/electron-builder --mac",
    "compile:win64": "node_modules/.bin/electron-builder --win --x64",
    "pack:mac": "npm run build:mac && npm run compile:mac",
    "pack:win64": "npm run build:win && npm run compile:win64"
}

// vue-cli 项目请使用此配置
"scripts": {
	"build:mac": "vue-cli-service build --target_platform=darwin",
	"build:win": "vue-cli-service build --target_platform=win32",
	"compile:mac": "node_modules/.bin/electron-builder --mac",
	"compile:win64": "node_modules/.bin/electron-builder --win --x64",
	"pack:mac": "npm run build:mac && npm run compile:mac",
	"pack:win64": "npm run build:win && npm run compile:win64"
}
:::
</dx-codeblock>

| 参数                        | 说明                                                         |
| --------------------------- | ------------------------------------------------------------ |
| main                        | Electron 的入口文件，一般情况下可以自由配置。但如果项目使用 `create-react-app` 脚手架创建，则入口文件必须配置为 `public/electron.js`。 |
| build.win.extraFiles        | 打包 Windows 程序时，`electron-builder` 会把 `from` 所指目录下的所有文件复制到 bin/win-unpacked/resources（全小写）。 |
| build.mac.extraFiles        | 打包 Mac 程序时，`electron-builder` 会把 `from` 指向的 `trtc_electron_sdk.node` 文件复制到 bin/mac/your-app-name.app/Contents/Resources（首字母大写）。 |
| build.directories.output    | 打包文件的输出路径。例如这个配置会输出到 `bin` 目录下，可根据实际需要修改。 |
| build.scripts.build:mac     | 以 Mac 平台为目标构建脚本。                                  |
| build.scripts.build:win     | 以 Windows 平台为目标构建脚本。                              |
| build.scripts.compile:mac   | 编译为 Mac 下的 `.dmg` 安装文件。                              |
| build.scripts.compile:win64 | 编译为 Windows 下的 `.exe` 安装文件。                          |
| build.scripts.pack:mac      | 先调用 `build:mac` 构建代码，再调用 `compile:mac` 打包成 `.dmg` 安装文件。 |
| build.scripts.pack:win64    | 先调用 `build:win` 构建代码，再调用 `compile:win64` 打包成 `.exe` 安装文件。 |






###  步骤4：执行打包命令
- 打包 Mac.dmg 安装文件：
```bash
$ cd [项目目录]
$ npm run pack:mac
```
	成功执行后，打包工具会生成 `bin/your-app-name-0.1.0.dmg` 安装文件，请选择此文件发布。
- 打包 Windows.exe 安装文件：
```bash
$ cd [项目目录]
$ npm run pack:win64
```
	成功执行后，打包工具会生成 `bin/your-app-name Setup 0.1.0.exe` 安装文件，请选择此文件发布。


>!TRTC Electron SDK 暂不支持跨平台打包（例如在 Mac 下打包 Windows 的 .exe 文件，或在 Windows 平台下打包 Mac 的 .dmg 文件）。目前我们正在研究跨平台打包方案，敬请期待。

## 常见问题

### 1. 防火墙有什么限制？

由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参见 [应对公司防火墙限制](https://cloud.tencent.com/document/product/1449/58956)。

### 2. Electron 安装或打包异常

如果您在集成 Electron 过程中遇到异常：例如安装超时或失败，打包后出现 trtc_electron_sdk.node 文件加载失败等情况，请参见 [Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668)。



