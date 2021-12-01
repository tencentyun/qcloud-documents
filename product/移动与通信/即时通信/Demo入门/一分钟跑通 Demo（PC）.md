本文主要介绍如何快速运行腾讯云即时通信 IM Demo（Electron）。

## 环境要求

| 平台 | 版本 |
|---------|---------|
| Electron | 13.1.5 及以上版本。 |
|Node.js|v14.2.0|

## 前提条件

您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 帐号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
## 步骤1：创建应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
>?如果您已有应用，请记录其 SDKAppID 并 [获取密钥信息](#step2)。
>同一个腾讯云帐号，最多可创建300个即时通信 IM 应用。若已有300个应用，您可以先 [停用并删除](https://cloud.tencent.com/document/product/269/32578#.E5.81.9C.E7.94.A8.2F.E5.88.A0.E9.99.A4.E5.BA.94.E7.94.A8) 无需使用的应用后再创建新的应用。**应用删除后，该 SDKAppID 对应的所有数据和服务不可恢复，请谨慎操作。**
>
2. 单击**创建新应用**，在**创建应用**对话框中输入您的应用名称，单击**确定**。
![](https://main.qcloudimg.com/raw/78340e403359fcf4d753ade29ae9aace.png)
3. 请保存 SDKAppID 信息。可在控制台总览页查看新建应用的状态、业务版本、SDKAppID、创建时间以及到期时间。
    ![](https://main.qcloudimg.com/raw/ed34d9294a485d8d06b3bb7e0cc5ae59.png)
4. 单击创建后的应用，左侧导航栏单击**辅助工具**>**UserSig 生成&校验**，创建一个 UserID 及其对应的 UserSig，复制签名信息，后续登录使用。
![](https://main.qcloudimg.com/raw/8315da2551bf35ec85ce10fd31fe2f52.png)

[](id:step2)
## 步骤2：下载源码安装依赖并运行
1. 克隆即时通信 IM Electron Demo 源码到本地。
```javascript
git clone https://github.com/tencentyun/im_electron_demo.git
```

2. 安装项目依赖。
```javascript
// 项目根目录
npm install

// 渲染进程目录
cd src/client
npm install
```

3. 项目运行。
```javascript
// 项目根目录
npm start
```

4. 项目打包。
```javascript
// mac打包
npm run build:mac
// windows打包
npm run build:windows
```



## 常见问题

### 支持哪些平台？
目前支持 Macos 和 Windows 两个平台。

### 安装开发环境问题，出现`gypgyp ERR!ERR`错误如何解决？
请参见 [gypgyp ERR!ERR! ](https://stackoverflow.com/questions/57879150/how-can-i-solve-error-gypgyp-errerr-find-vsfind-vs-msvs-version-not-set-from-c)。

### Mac 端执行`npm run start` 会出现白屏，如何解决？
Mac 端执行`npm run start` 会出现白屏，原因是渲染进程的代码还没有 build 完成，主进程打开的3000端口为空页面，当渲染进程代码 build 完成重新刷新窗口后即可解决问题。或者执行`cd src/client && npm run dev:react`, `npm run dev:electron`, 分开启动渲染进程和主进程。
