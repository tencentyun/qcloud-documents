## 操作场景
Koa 组件通过使用 serverless-tencent 的基础组件（如 API 网关组件、SCF 组件等），可以帮助我们快速、方便的在腾讯云创建、配置和管理一个 [Koa 框架](https://koajs.com/)。

>!建议您使用 Node.js10.0 及以上版本，否则 Component V2 部署有可能报错。

## 迁移前提

- 已经 [安装 Serverless Framework 1.67.2](https://cloud.tencent.com/document/product/1154/41775) 以上版本。
- 已经[注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)并完成[实名认证](https://cloud.tencent.com/document/product/378/10495)。

>?如果您的账号为**腾讯云子账号**，请首先联系主账号，参考 [账号和权限配置](https://cloud.tencent.com/document/product/1154/43006) 进行授权。
  
## 操作步骤
>?以下步骤主要针对命令行部署操作，控制台部署请参考 [控制台部署指南](https://cloud.tencent.com/document/product/1154/50957)。

### 1. （可选）初始化 Koa 模版项目
如果您本地并没有 Koa 项目，可通过以下指令快速新建一个 Koa 项目模版（本地已有项目可跳过该步骤）：
```
serverless init koa-starter --name example
cd example
```

### 2. 修改项目代码
打开 Koa 项目的入口文件 sls.js（或 app.js），注释掉本地的监听端口，并导出默认的 Koa app：

```javascript
// sls.js

const koa = require('koa');
const app = koa();

// *****

// 注释掉本地监听端口
// app.listen(3000);

// 导出 Express app
module.exports = app;
```

### 3. 快速生成 yml 文件并进行部署
完成代码修改后，通过执行 `sls deploy` 指令，Serverless Framework 会自动帮您生成基本的 `serverless.yml` 文件，并完成部署，实现 Koa 框架应用的快速迁移。

生成的默认配置文件如下：
```yml
component: koa
name: koaDemo
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

### 4. 修改 yml 文件

基于您实际部署需要，您可以在 `serverless.yml` 中完成更多配置，并执行 `sls deploy`重新部署。

yml 文件的配置信息请参考[ Koa 组件全量配置](https://github.com/serverless-components/tencent-koa/blob/master/docs/configure.md)。

### 5. 监控运维
部署完成后，您可以通过访问 [Serverless SSR 控制台](https://console.cloud.tencent.com/ssr)，查看应用的基本信息和监控日志。

### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：
```console
touch .env # 腾讯云的配置信息
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

## 更多组件
可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。
