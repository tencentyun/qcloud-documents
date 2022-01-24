## Demo 体验
<input type="button" value="Windows 版" style="height: 30px;width: 150px;min-width: 24px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;white-space: nowrap;margin-right:10px;"  onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-windows-latest.zip')" />

<input type="button" value="MacOS 版" style="height: 30px;width: 150px;margin-top: 5px;min-width: 24px;background-color: #00a4ff;color: #fff;border: 1px solid #00a4ff;line-height: 30px;text-align: center;display: inline-block;cursor: pointer;outline: 0 none;box-sizing: border-box;text-decoration: none;font-size: 12px;white-space: nowrap;" onclick="window.open('https://web.sdk.qcloud.com/trtc/electron/download/solution/education-v2/TRTCEducationElectron-mac-latest.zip')" />

## 效果展示
您可以下载、安装我们已经构建好的 App 安装包， 体验实时互动课堂的能力效果。不仅提供了基础的音视频通话、屏幕分享、白板、文字聊天等基础功能，还实现了全员禁麦、学生举手申请发言、老师邀请学生发言、点名、签到等高级功能。

<table>
<tr><th style="text-align:center">教师端</th><th style="text-align:center">学生端</th><tr>
<tr><td><img src="https://web.sdk.qcloud.com/trtc/electron/download/resources/education-v2/preview-teacher.gif"/></td><td><img src="https://web.sdk.qcloud.com/trtc/electron/download/resources/education-v2/preview-student.gif"/></td><tr>
</table>

## 跑通实时互动课堂源代码
[](id:step1)
### 步骤1：创建应用并获取 SDKAppID 和密钥
如果您之前已经创建过腾讯云实时音视频的应用，可以跳过该步骤，直接使用之前创建应用的 SDKAppID 和密钥。

1. 登录实时音视频控制台，选择**开发辅助** > **[快速跑通 Demo](https://console.cloud.tencent.com/trtc/quickstart)**，在**创建应用**页签，输入您的应用名称，例如 `TestTRTC`，单击**创建**按钮。  
![](https://qcloudimg.tencent-cloud.cn/raw/82cfe02c5a2752311cc24ee91f109769.png)
2. 跳过**下载源码**页签，直接单击**下一步**按钮，进入**修改配置**页签，记录下页面上显示的 SDKAppID 和密钥，后续步骤将会用到。
![](https://qcloudimg.tencent-cloud.cn/raw/11d39bf7db12604ce62546a5a8e2eb40.png)

[](id:step2)
### 步骤2：配置即时通信 IM
>? 本功能同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。 即时通信 IM 属于增值服务，详细计费规则请参见 [即时通信 IM 价格说明](https://cloud.tencent.com/document/product/269/11673)。

1. 进入**相关云服务**菜单，单击下图中**即时通信 IM 应用**跳转到 IM 应用管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/673eea54650d3fd62aa7499dfd0db39d.png)
2. 找到刚创建的应用，单击进入该应用管理页面，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fba11fe331d1d9de2423ad6f75026c33.png)
3. 打开菜单**功能配置** > **登录与消息**，如下图所示，单击**登录设置**区域的**编辑**链接，将 **Web 端可同时在线个数**设置为大于等于 2 的值（目前本应用最多需要同时登录 2 个 Web IM 实例，可以设置更多一些，以备后续使用）。
![](https://qcloudimg.tencent-cloud.cn/raw/86fef12084d3ad37b9671a9167651f40.png)

[](id:step3)
### 步骤3：运行环境准备
本代码工程的运行依赖于 node.js 和 yarn。

1. **安装 node.js：**
建议 [node.js](https://nodejs.org/en/download/) 使用 14.16.0 以上版本，安装完成后，在命令行终端执行以下命令检查 node.js 版本。
```
node --version
```
2. **安装 yarn：**
 - 如果 node.js 版本小于 16.10，在命令行终端执行以下命令安装 [yarn](https://yarnpkg.com/getting-started/install)。
```
npm i -g corepack
```
 - 如果 node.js 版本大于等于 16.10，在命令行终端执行以下命令安装 yarn。
```
corepack enable
```
>!Window 10、11 下如果遇到权限不足的错误提示，请尝试以管理员身份，在 cmd 控制台执行。



[](id:step4)
### 步骤4：克隆代码工程

您可以直接[下载代码](https://github.com/TencentCloud/trtc-education-electron)，解压后进入代码目录 `trtc-education-electron`，或者使用 [git](https://git-scm.com/downloads) 工具克隆代码工程。使用 git 工具克隆代码工程，请在命令行终端执行以下命令：

```
git clone https://github.com/TencentCloud/trtc-education-electron.git

cd trtc-education-electron
```

[](id:step5)
### 步骤5: 配置 SDKAppID 和密钥
1. 找到并打开 `src/main/config/generateUserSig.js` 文件。
2. 设置 `generateUserSig.js` 文件中的相关参数，用于生成身份认证用的用户签名 UserSig：：
   - SDKAPPID：默认为 0，请设置为 [步骤1](#step1) 创建应用的 SDKAppID。
   - SECRETKEY：默认为空字符串，请设置为 [步骤1](#step1) 创建应用的密钥。

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:step6)
### 步骤6: 开发模式运行
在命令行终端中，进入代码目录 `trtc-education-electron`，执行以下命令。
```
yarn

yarn start
```
>!
>- 第一次执行 yarn 命令安装依赖时，Window10、Window11 下如果遇到权限不足的错误提示，请尝试以管理员身份，在 cmd 控制台执行一次。之后就可以以普通用户身份在 cmd 控制台或者集成开发工具自带终端中执行，例如：Visual Studio Code、WebStorm 等。
>- 安装依赖过程中，如遇到 Electron 下载慢甚至卡住不动等问题，您可以参考 [Electron 常见问题收录](https://cloud.tencent.com/developer/article/1616668) 文档解决。

[](id:step7)
### 步骤7: 构建安装包、运行
在命令行终端中，进入代码目录 `trtc-education-electron`，执行以下命令构建安装包，构建好的安装包位于 `trtc-education-electron/build/release` 目录下，可以安装运行。

```
yarn package
```

>!只能使用 Mac 电脑构建 Mac 安装包，使用 Windows 电脑构建 Windows 安装包。

[](id:QQ)
## 技术咨询
了解更多详情您可 QQ 咨询：<dx-tag-link link="#QQ" tag="技术交流群">695855795</dx-tag-link>

## 参考文档

- [SDK API 手册](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/index.html)
- [SDK 更新日志](https://cloud.tencent.com/document/product/647/43117)
- [Simple Demo 源码](https://github.com/tencentyun/TRTCSDK/tree/master/Electron/TRTCSimpleDemo)
- [API Example 源码](https://github.com/tencentyun/TRTCSDK/tree/master/Electron/TRTC-API-Example)
- [Electron 常见问题](https://cloud.tencent.com/document/product/647/62562)
