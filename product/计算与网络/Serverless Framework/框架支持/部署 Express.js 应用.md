## 操作场景
**腾讯云 Express 组件**通过使用 [Tencent Serverless Framework](https://github.com/serverless/components/tree/cloud)，基于云上 Serverless 服务（如网关、云函数等），实现“0”配置，便捷开发，极速部署您的 Express 应用，Express 组件支持丰富的配置扩展，提供了目前最易用、低成本并且弹性伸缩的 Experss 项目开发/托管能力。

Express.js 特性介绍：
- **按需付费**：按照请求的使用量进行收费，没有请求时无需付费。
- **"0"配置**：只需要关心项目代码，之后部署即可，Serverless Framework 会搞定所有配置。
- **极速部署**：仅需几秒，部署您的整个 express 应用。
- **实时日志**：通过实时日志的输出查看业务状态，便于直接在云端开发应用。
- **云端调试**：针对 Node.js 框架支持一键云端调试能力，屏蔽本地环境的差异。
- **便捷协作**：通过云端的状态信息和部署日志，方便的进行多人协作开发。
- **自定义域名**：支持配置自定义域名及 HTTPS 访问。

通过 [Serverless Framework Express 组件](https://github.com/serverless-components/tencent-express)，可以快速实现 Express 传统应用从本地到 Serverless 函数平台的迁移。

## 迁移前提

- 已经 [安装 Serverless Framework 1.67.2](https://cloud.tencent.com/document/product/1154/42990) 以上版本。
- 已经 [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/10495)。

>?如果您的账号为**腾讯云子账号**，请先联系主账号，参考 [账号和权限配置](https://cloud.tencent.com/document/product/1154/43006) 进行授权。

## 架构说明

Express 组件将在腾讯云账号中使用到如下 Serverless 服务：

- **API 网关**：API 网关将会接收外部请求并且转发到 SCF 云函数中。
- **SCF 云函数**：云函数将承载 Express 应用。
- **CAM 访问控制**：该组件会创建默认 CAM 角色用于授权访问关联资源。
- **COS 对象存储**：为确保上传速度和质量，云函数压缩并上传代码时，会默认将代码包存储在特定命名的 COS 桶中。
  
## 操作步骤

>?以下步骤主要针对命令行部署操作，控制台部署请参考 [控制台部署指南](https://cloud.tencent.com/document/product/1154/50957)。
### 1. 初始化 Express 模版项目（可选）
如果您本地并没有 Express 项目，可通过以下指令快速新建一个 Express 项目模版（本地已有项目可跳过该步骤）：
```
serverless init express-starter --name example
cd example
```

### 2. 修改项目代码
打开 Express 项目的入口文件 sls.js（或 app.js），注释掉本地的监听端口，并导出默认的 Express app：

```javascript
// sls.js

const express = require('express');
const app = express();

// *****

// 注释掉本地监听端口
// app.listen(3000);

// 导出 Express app
module.exports = app;
```

### 3. 快速生成 yml 文件并进行部署
完成代码修改后，通过执行 `sls deploy` 指令，Serverless Framework 会自动帮您生成基本的 `serverless.yml` 文件，并完成部署，实现 Express 框架应用的快速迁移。

生成的默认配置文件如下：
```yml
component: express
name: expressDemo
app: appDemo

inputs:
  entryFile: sls.js #以您实际入口文件名为准
  src: ./
  region: ap-guangzhou
  runtime: Nodejs10.15
  apigatewayConf:
    protocols:
      - http
      - https
    environment: release
```

部署完成后，通过访问输出的 API 网关链接，完成对应用的访问。

### 4. 修改 yml 配置文件

基于您实际部署需要，您可以在 `serverless.yml` 中完成更多配置，并执行 `sls deploy`重新部署。

yml 文件的配置信息请参考[ Express 组件全量配置](https://github.com/serverless-components/tencent-express/blob/master/docs/configure.md)

### 5. 监控运维
部署完成后，您可以通过访问 [Serverless 应用控制台](https://console.cloud.tencent.com/ssr)，查看应用的基本信息，监控日志。


## 账号配置

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```console
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：

```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
>


