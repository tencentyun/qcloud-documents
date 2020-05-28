腾讯云文字识别（OCR）基于行业前沿的深度学习技术，将图片上的文字内容智能识别成为可编辑的文本，支持多场景下的印刷体、手写体文字识别，覆盖不同场景下的文字识别需求。
通过 Serverless Framework Component 和 OCR SDK， 您可快速部署一个基于 COS + API + SCF 的通用文字识别应用，主要包含以下组件：

- **Serverless RESTful API：** 通过云函数和 API 网关构建的 Express 框架实现  RESTful API。
- **Serverless 静态网站：** 前端通过托管 React 静态页面到对象存储 COS 中。
- **COS 云端存储:** 用户通过自己创建存储桶来存放目标图像。

## 前提条件

已安装 [Node.js](https://nodejs.org/en/)（Node.js 版本需不低于8.6版本，建议使用Node.js10.0 及以上版本）

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
Framework Core: 1.67.3
Plugin: 3.6.6
SDK: 2.3.0
Components: 2.30.1
```

### 创建存储桶

1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos5)，创建新的 **公有存储桶**（参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)） ，用于存放上传的图像，注意地域的选择。
2. 在桶列表的【基础配置】中，为存储桶 [配置跨域访问 CORS](https://cloud.tencent.com/document/product/436/13318)，具体配置如下：
![](https://main.qcloudimg.com/raw/7c397d30e8231ce983c1fce44abd7326.png)

### 配置

1.新建一个本地文件夹，使用`create --template-url`命令，下载相关 template。

```console
$ serverless create --template-url https://github.com/serverless-tencent/serverless-demos/serverless-ocr
```

2.在模版中找到 `.env.example` 文件，并改名为 `.env` ，在里面输入您的账户、密钥信息和指定存储桶（此存储桶用于存放上传的图像）

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
>?您需要先创建一个公有存储桶，用于存放上传的图像。

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

部署成功后，您可以使用浏览器访问项目产生的 website 链接，即可看到生成的网站，单击【上传图片】，项目即可通过 OCR SDK 完成文字识别。


2.执行 `sls remove --all`，可移除项目。

```bash
$  sls remove --all

serverless ⚡ framework

38s › tencent-fullstack › Success
```
