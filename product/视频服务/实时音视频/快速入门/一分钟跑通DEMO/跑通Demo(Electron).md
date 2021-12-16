本文主要介绍如何快速运行腾讯云 TRTC Demo（Electron）。
![演示](https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/electron/livemode.gif)

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

[](id:step1)

### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择**开发辅助**>**[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
2. 单击**新建应用**输入应用名称，例如 `TestTRTC`；若您已创建应用可单击**选择已有应用**。
3. 根据实际业务需求添加或编辑标签，单击**创建**。
![](https://main.qcloudimg.com/raw/f04d288ed091c98a5e8056eb86fb49e8.png)
>?
>- 应用名称只能包含数字、中英文字符和下划线，长度不能超过15个字符。
>- 标签用于标识和组织您在腾讯云的各种资源。例如：企业可能有多个业务部门，每个部门有1个或多个 TRTC 应用，这时，企业可以通过给 TRTC 应用添加标签来标记部门信息。标签并非必选项，您可根据实际业务需求添加或编辑。

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1.根据实际业务需求下载 SDK 及配套的 Demo 源码。
2.下载完成后，单击**已下载，下一步**。
![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Electron/js/GenerateTestUserSig.js` 文件。
3. 设置 `GenerateTestUserSig.js` 文件中的相关参数：
<ul>
 <li/>SDKAPPID：默认为0 ，请设置为实际的 SDKAppID。
 <li/>SECRETKEY：默认为空字符串 ，请设置为实际的密钥信息。</ul>
 <img src="https://main.qcloudimg.com/raw/c3e8d8bfe0dba5130bcf0d20b6df0778.png">
4. 粘贴完成后，单击**已复制粘贴，下一步**即创建成功。
5. 编译完成后，单击**回到控制台概览**即可。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

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
| | |---log.js                            日志工具
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

[](id:step4)

### 步骤4：编译运行
<dx-tabs>
::: Windows平台
1.  安装 Node 最新版本，建议选择 64bit 的 `.msi` 文件。[Node 下载地址](https://nodejs.org/en/download/)。
2.  按下 `win + r` 输入 cmd，用管理员权限启动命令行窗口，并将目录定位到 [项目目录](#projectFolder)，并执行以下命令。
```shell
$ npm install
```![安装](https://main.qcloudimg.com/raw/5aba25ba2d5eddb5d956406ca5b6b9ac.png)
3. 如果 Electron 安装较慢甚至超时，您可以参考文章：[Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668) 中的 “安装时遇到的问题” 章节和 “附录：手动离线安装 Electron” 章节来完成 Electron 安装。
4.  待 npm 的依赖包都安装完成后，继续在命令行窗口执行以下命令，运行 Demo。
```shell
$ npm run start  # 首次运行，稍等片刻后，窗口中才会出现 UI
```![运行demo](https://main.qcloudimg.com/raw/47f6e01acb2d927f6d9e24a7c9f78af1.png)
:::
::: MacOS平台
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
```![](https://main.qcloudimg.com/raw/8bcc95adad07ff37e7f0a27893b8b7cf.png)
5.  待 npm 的依赖包都安装完成后，继续在命令行窗口执行以下命令，运行 Demo。
```shell
$ npm run start # 首次运行，稍等片刻后，窗口中才会出现 UI
```![mac下运行项目](https://main.qcloudimg.com/raw/423dae368118e5250e7fa878022bb26f.png)
:::
</dx-tabs>
    
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
2.  在左侧导航栏选择**应用管理**，单击目标应用所在行的**应用信息**。
3.  选择**快速上手**页签，单击**第二步 获取签发UserSig的密钥**区域的**点此升级**。

### 2. 两台设备同时运行 Demo，为什么看不到彼此的画面？

请确保两台设备在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个设备同时使用。

![](https://main.qcloudimg.com/raw/9a03335e435de0f12e2a26882f53db02.png)

### 3. 防火墙有什么限制？

由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参见 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。



>? 更多相关问题，请参见 [Electron 相关常见问题](https://cloud.tencent.com/document/product/647/62562)。

[](id:QQ)
## 技术咨询
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">695855795</dx-tag-link>

## 参见文档：

- [SDK API 手册](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/index.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/647/43117)
- [Simple Demo 源码](https://github.com/tencentyun/TRTCSDK/tree/master/Electron/TRTCSimpleDemo)
- [API Example 源码](https://github.com/tencentyun/TRTCSDK/tree/master/Electron/TRTC-API-Example)
- [Electron 常见问题](https://cloud.tencent.com/document/product/647/62562)
