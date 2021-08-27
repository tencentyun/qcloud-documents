腾讯云文字识别（OCR）基于行业前沿的深度学习技术，将图片上的文字内容智能识别成为可编辑的文本，支持多场景下的印刷体、手写体文字识别，覆盖不同场景下的文字识别需求。
通过 Serverless Framework Component 和 OCR SDK， 您可快速部署一个基于 COS + API + SCF 的通用文字识别应用，主要包含以下组件：

- **Serverless RESTful API：** 通过云函数和 API 网关构建的 Express 框架实现  RESTful API。
- **Serverless 静态网站：** 前端通过托管 React 静态页面到对象存储 COS 中。
- **COS 云端存储:** 用户通过自己创建存储桶来存放目标图像。

## 前提条件

- 已安装 [Node.js](https://nodejs.org/en/)（**2020年9月1日起，Serverless 组件不再支持 Node.js10.0 以下版本，请注意升级**）
- 已开通 [OCR 通用文字识别](https://cloud.tencent.com/product/generalocr) 服务

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

安装完毕后，通过运行 `serverless -v` 命令，查看 Serverless Framework 的版本信息，确保版本信息不低于以下版本：

```shell
$ serverless –v
Framework Core: 1.74.1 (standalone)
Plugin: 3.6.14
SDK: 2.3.1
Components: 2.31.6
```

### 配置

1.新建一个本地文件夹，使用`serverless init`命令，下载相关 template。

```console
$ serverless init ocr-app
```

2.在模版中找到 `.env.example` 文件，并改名为 `.env` ，在里面输入您的账户、密钥信息和指定存储桶（此存储桶用于存放上传的图像）。

```
# .env
TENCENT_APP_ID=xxx
TENCENT_SECRET_ID=xxx
TENCENT_SECRET_KEY=xxx

# region of bucket
REGION=ap-guangzhou
```

3.下载所有 npm 依赖。

```console
$ npm run bootstrap
```
### 本地调试

1. 输入以下指令启动服务端：
```
$ cd server && npm run start
```
2. 输入以下指令启动前端：
```
$ cd frontend && npm run start
```
3. 通过 http://localhost:3000 登录前端页面进行本地调试。

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

部署成功后，您可以使用浏览器访问项目产生的 website 链接，即可看到生成的网站，单击**上传图片**，项目即可通过 OCR SDK 完成文字识别。


2.执行 `sls remove --all`，可移除项目。

```bash
$  sls remove --all

serverless ⚡ framework

38s › tencent-fullstack › Success
```
