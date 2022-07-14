本文介绍如何快速以 Iframe 集成 Web 在线视频剪辑能力。学习完本教程之后，您将部署一个完整的 Demo，包含服务端以及可访问的前端页面，您可以在前端上传视频，并进行在线剪辑、合成导出。


## 准备工作[](id:step0)
1. 注册 [腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fproduct%2Flvb)，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 进入 [腾讯云点播服务开通页](https://console.cloud.tencent.com/vod/overview) ，勾选同意《腾讯云服务协议》和《腾讯云点播计费说明》，单击 **申请开通** 即可开通云点播服务。
>? 若已开通云点播服务，请直接进入下一步骤。


## 步骤1：开通服务并创建平台[](id:step1)
1. 登录 [腾讯多媒体创作引擎控制台](https://console.cloud.tencent.com/cme)。
2. 单击 **前往一键授权**，进入授权页面，单击 **同意授权** 授权成功，并返回腾讯多媒体创作引擎控制台。
3. 单击左侧导航栏的 **平台配置**，进入平台配置页面。
4. 单击 **创建新平台**，填写平台名称，选择该平台绑定的云点播子应用，单击 **确定**。

![](https://main.qcloudimg.com/raw/21e4ca6a6e312f16795545cd4b1136f1.png)

完成创建平台后，可以获取到平台的名称 `Platform`，用于 Demo 的配置使用。

## 步骤2：获取云 API 密钥[](id:step2)
获取腾讯云用户身份密钥，即`SecretId`和`SecretKey`，具体步骤如下：
1.  登录控制台，选择 **云产品** > **访问管理** >[ **API密钥管理** ](https://console.cloud.tencent.com/cam/capi)，进入 API 密钥管理页面。
2.  获取云 API 密钥。如果您尚未创建密钥，则单击 **新建密钥** 即可创建一对 SecretId 和 SecretKey。
>?获取得到的`SecretId`和`SecretKey`也是用于 Demo 的配置使用。

## 步骤3：下载并部署 Demo[](id:step3)
### 环境准备
多媒体创作引擎提供的 Demo 是基于 Node.js 开发的，在运行 Demo 之前需要检查本地是否安装了 Node.js，若没有安装 Node.js 的可以登录官网进行包进行快速安装，详情请参见：[Node.js 安装包下载](https://nodejs.org)。

### 源码下载
Demo 的代码托管在 Github 上，开发者可以登录上去直接进行下载，详情请参见：[Demo Github 地址](https://github.com/tencentyun/cme-node-demo)。
开发者也可以直接在本地通过 git 命令下载代码：
```bash
git clone https://github.com/tencentyun/cme-node-demo.git
```
### 安装运行
Demo 依赖一些其它的包，首先需通过 npm 安装依赖，开发者通过命令行跳到项目的根目录下，并执行安装命令：
```bash
cd cme-node-demo/
npm install
```
在项目下有个核心的配置文件`config.js`，开发者将之前获取的平台及密钥填写到对应的位置上：
```js
const config = {
  port: 9090,
  secretId: "You SecretId",
  secretKey: "Your SecretKey",
  platform: "Your Platform"
};
```

依赖安装完成后，运行启动命令：
```bash
npm start
```
Demo 运行成功后，我们在浏览器输入`http://localhost:9090`即可进入 Demo 的显示页面。

## 步骤4：验证功能[](id:step4)
### 创建项目
在 Demo 上可以直接创建一个视频编辑项目，创建完成后可以进入项目进行编辑。
![](https://main.qcloudimg.com/raw/37dba2fcfda1d3334d5491435b5957d6.png)

### 上传素材
在项目中单击 **添加媒体资源**，页面弹出上传面板，用户选择本地文件，上传完成后即可在页面中出现新添加的素材。
![](https://main.qcloudimg.com/raw/9aceed7d146c81b48a7a3252ca2b1604.png)

### 导出项目
完成视频编辑后，单击 **导出视频**，后台会发起导出任务，最后的导出结果可在页面中获取到。
![](https://main.qcloudimg.com/raw/0aa27764722cdfde81a3d65a4ee29ae0.png)

