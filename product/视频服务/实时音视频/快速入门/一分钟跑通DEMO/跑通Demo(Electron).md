本文主要介绍如何快速运行腾讯云 TRTC Demo（Electron）。
![演示](https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/electron/livemode.gif)

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

<span id="step1" name="step1"> </span>

### 步骤1：创建新的应用

1.  登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2.  单击【立即开始】，输入应用名称，例如 `TestTRTC`，单击【创建应用】。

<span id="step2" name="step2"> </span>

### 步骤2：下载 SDK 和 Demo 源码

1.  鼠标移动至对应卡片，单击【[Github](https://github.com/tencentyun/TRTCSDK/tree/master/Electron)】跳转至 Github（或单击【[ZIP](https://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Electron_latest.zip)】），下载相关 SDK 及配套的 Demo 源码。
    ![img](https://main.qcloudimg.com/raw/6273f79193eb7af25eff64020a0ea476.png)
2.  下载完成后，返回实时音视频控制台，单击【我已下载，下一步】，可以查看 SDKAppID 和密钥信息。

<span id="step3" name="step3"> </span>

### 步骤3：配置 Demo 工程文件
1.  解压 [步骤2](#step2) 中下载的源码包，找到 `TRTCSDK/Electron/TRTCSimpleDemo/`目录，此为 **项目目录**，下文中提到的<span id="projectFolder" name="projectFolder"> “项目目录”</span>，指的即是 `TRTCSDK/Electron/TRTCSimpleDemo/`目录。
2.  找到项目目录中的 `debug/gen-test-user-sig.js` 文件，并打开。
3.  设置 `gen-test-user-sig.js` 文件中的相关参数：
	-   SDKAPPID：默认为0，请设置为实际的 SDKAppID。
	-   SECRETKEY：默认为空字符串，请设置为实际的密钥信息。    
4.  返回实时音视频控制台，单击【粘贴完成，下一步】。
5.  单击【关闭指引，进入控制台管理应用】。

**文件目录说明：**
```bash
.
|---README.md                             README 文件，请详细阅读
|---main.electron.js                      Electron 主文件
|---public                                存放静态文件
|---babel.config.js
|---package.json
|---vue.config.js                         vue-cli 工程文件
|---src                                   源代码目录
| |---app.vue
| |---common.css
| |---main.js
| |---components                          UI 组件目录
| | |---main-menu.vue
| | |---nav-bar.vue
| | |---show-screen-capture.vue
| |---common                              工具函数、公共库等
| | |---live-room-service.js
| | |---log.js														日志工具
| | |---mtah5.js													
| | |---routes.js
| | |---rand.js
| |---pages                               页面目录
| | |---index.vue                         主页
| | |---trtc                              视频会议相关页面
| | | |---trtc-room.vue                   视频会议房间页面
| | | |---trtc-index.vue                  视频会议入口页
| | |---404.vue
| | |---live                              直播页
| | | |---live-index.vue                  直播入口页
| | | |---live-room-audience.vue          观众席页
| | | |---live-room-anchor.vue            主播间页
| |---debug                               注意！在部署时，请将此文件夹内的签名逻辑移到服务器实现
| | |---lib-generate-test-usersig.min.js  
| | |---gen-test-user-sig.js              
```

<span id="step4"> </span>

### 步骤4：编译运行

#### Windows 平台
1.  安装 Node 最新版本，建议选择 64bit 的 `.msi` 文件。[Node 下载地址](https://nodejs.org/en/download/)
2.  按下 `win + r` 输入 cmd，用管理员权限启动命令行窗口，并将目录定位到 [项目目录](#projectFolder)，并执行以下命令。
 ```shell
$ npm install
```
![安装](https://main.qcloudimg.com/raw/5aba25ba2d5eddb5d956406ca5b6b9ac.png)
3. 如果 Electron 安装较慢甚至超时，您可以参考文章：[Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668) 中的 “安装时遇到的问题” 章节和 “附录：手动离线安装 Electron” 章节来完成 Electron 安装。
4.  待 npm 的依赖包都安装完成后，继续在命令行窗口执行以下命令，运行 Demo。
```shell
$ npm run start  # 首次运行，稍等片刻后，窗口中才会出现 UI
```
![运行demo](https://main.qcloudimg.com/raw/47f6e01acb2d927f6d9e24a7c9f78af1.png)

#### Mac OS 平台

1.  打开终端（Terminal）或 cmd 窗口，执行以下命令安装 Homebrew，如果已经安装请跳过此步骤。
```shell
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2.  执行以下命令，安装 Node.js。
```shell
$ brew install node
```
3.  如果使用 Homebrew 的默认地址安装 Node.js 较慢，您可以考虑替换为国内镜像地址。
 ```shell
$ cd `brew --repo`
$ git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
$ brew update
```
4.  通过 cd 命令定位项目目录，并执行以下命令。
```shell
$ npm install 
```
![](https://main.qcloudimg.com/raw/8bcc95adad07ff37e7f0a27893b8b7cf.png)
5.  待 npm 的依赖包都安装完成后，继续在命令行窗口执行以下命令，运行 Demo。
```shell
$ npm run start # 首次运行，稍等片刻后，窗口中才会出现 UI
```
![mac下运行项目](https://main.qcloudimg.com/raw/423dae368118e5250e7fa878022bb26f.png)
    
### 项目主要命令

| 命令 | 说明 |
|--|--|
| npm run start | 以开发环境运行 Demo |
| npm run pack:mac | 打包 Mac 的 .dmg 安装文件 |
| npm run pack:win64 | 打包 Windows 64 位的 .exe 安装文件 |

## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？

TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法 ECDSA-SHA256](https://cloud.tencent.com/document/product/647/17275#Old)。

**升级操作：**
1.  登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
2.  在左侧导航栏选择【应用管理】，单击目标应用所在行的【应用信息】。
3.  选择【快速上手】页签，单击【第二步 获取签发UserSig的密钥】区域的【点此升级】。

### 2. 两台设备同时运行 Demo，为什么看不到彼此的画面？

请确保两台设备在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个设备同时使用。

![](https://main.qcloudimg.com/raw/9a03335e435de0f12e2a26882f53db02.png)

### 3. 防火墙有什么限制？

由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。


