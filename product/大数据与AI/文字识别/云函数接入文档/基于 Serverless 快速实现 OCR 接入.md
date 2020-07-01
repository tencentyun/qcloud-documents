## 概述
基于腾讯云 Serverless 服务，用户可以通过云函数 SCF 与 API 网关产品快速完成 OCR 接入工作，帮助用户实现“0”配置，便捷开发，方便运维的项目部署方案。Serverless Framework 的详细介绍，请阅读 [云函数产品文档](https://cloud.tencent.com/document/product/583) 。

本文档将为您介绍，如何通过 Serverless Framework 组件，快速部署一个接入 OCR 的应用。

使用组件：

- **Serverless Express：** 通过云函数和 API 网关构建的 Express 框架实现 RESTful API。
- **Serverless Website：** 前端通过托管 React 静态页面到 COS 对象存储中。
- **COS 云端存储:** 用户通过自己创建存储桶来存放目标图像。

## 前提条件

- 已安装 [Node.js](https://nodejs.org/en/)（Node.js 版本需不低于 8.6，建议使用 Node.js 10.0 及以上版本）
- 已开通 OCR 服务，单击 [立即开通](https://console.cloud.tencent.com/ocr) 

## 接入效果
应用页面如下，通过单击“Select”，完成本地图像上传，后台云函数将通过 OCR 完成文字识别工作。

<center>
<img src="https://main.qcloudimg.com/raw/a65e95a30bb124382414397a3a409132/demo.png" alt="demo" width="500">
</center>

## 操作步骤

### 安装

通过 npm 全局安装 [Serverless Framework](https://github.com/serverless/serverless)：

```shell
$ npm install -g serverless
```

如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版：

```shell
$ npm update -g serverless
```

安装完毕后，通过运行 serverless -v 命令，查看 Serverless Framework 的版本信息，确保版本信息不低于以下版本：

```shell
$ serverless –v
Framework Core: 1.67.3
Plugin: 3.6.6
SDK: 2.3.0
Components: 2.30.1
```

### 创建存储桶
登录 [COS 控制台](https://console.cloud.tencent.com/cos5)，创建新的 **公有存储桶** ，用于存放上传的图像，注意地域的选择。
接下来，点开 **基础配置**，为存储桶 [配置跨域访问 CORS](https://cloud.tencent.com/document/product/436/13318)，具体配置如下：

<center>
<img src="https://main.qcloudimg.com/raw/10187a76dfa158af6150acf02548d157/cos-cors-setup.png" alt="CORS config" width="300">
</center>

### 配置

1.新建一个本地文件夹，使用`create --template-url`命令，下载相关 template。

```console
$ serverless create --template-url https://github.com/serverless-tencent/serverless-demos/serverless-ocr
```

2.创建 `.env` 文件，在里面输入您的账户、密钥信息和指定存储桶(此存储桶用于存放上传的图像)。

```
# .env
TENCENT_APP_ID=xxx
TENCENT_SECRET_ID=xxx
TENCENT_SECRET_KEY=xxx

# region of bucket
REGION=ap-guangzhou
# bucket name, using to store upload pictures
BUCKET=ocr-images
```

>! 您需要先创建一个公开存储桶，用于存放上传的图像。

3.下载所有 npm 依赖

```console
$ npm run bootstrap
```


### 部署

1.执行以下命令进行部署：

```bash
$ sls deploy --all

serverless ⚡ framework

backend: 
  region: ap-guangzhou
  apigw: 
    serviceId:   service-4i62q1pg
    subDomain:   service-4i62q1pg-1258834142.gz.apigw.tencentcs.com
    environment: release
    url:         https://service-4i62q1pg-1258834142.gz.apigw.tencentcs.com/release/
  scf: 
    functionName: serverless-ocr
    runtime:      Nodejs10.15
    namespace:    default

frontend: 
  region:  ap-guangzhou
  website: https://serverless-ocr-1258834142.cos-website.ap-guangzhou.myqcloud.com

38s › serverless-ocr › Success

```

部署成功后，您可以使用浏览器访问项目产生的 website 链接，即可看到生成的网站，单击上传图片，项目即可通过 OCR SDK 完成文字识别。


2.执行 `sls remove --all`，可移除项目。

```bash
$  sls remove --all

serverless ⚡ framework

38s › tencent-fullstack › Success
```
