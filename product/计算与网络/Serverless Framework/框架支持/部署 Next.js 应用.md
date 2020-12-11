## 操作场景
腾讯云 [Next.js 组件](https://github.com/zeit/next.js) 通过使用 [Tencent Serverless Framework](https://github.com/serverless/components/tree/cloud)，基于云上 Serverless 服务（如 API 网关、云函数等），实现“0”配置，便捷开发，极速部署采用 Next.js 框架的网页应用，Next.js 组件支持丰富的配置扩展，提供了目前便捷实用，开发成本低的网页应用项目的开发/托管能力。

Next.js 特性介绍：
- **按需付费**：按照请求的使用量进行收费，没有请求时无需付费。
-  **"0"配置**：只需要关心项目代码，直接部署即可，Serverless Framework 会搞定所有配置。
- **极速部署**：部署速度快，仅需几秒，部署您的整个应用。
- **实时日志**：通过实时日志的输出查看业务状态，便于直接在云端开发应用。
- **云端调试**：可在云端直接进行项目调试，从而避免本地环境的差异。
- **便捷协作**：通过云端控制台的状态信息和部署日志，方便进行多人协作开发。


## 迁移前提

- 已经 [安装 Serverless Framework 1.67.2](https://cloud.tencent.com/document/product/1154/42990) 以上版本。
- 已经[注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)并完成[实名认证](https://cloud.tencent.com/document/product/378/10495)。

  > 如果您的账户为**腾讯云子账号**，请首先联系主账号，参考 [账号和权限配置](https://cloud.tencent.com/document/product/1154/43006) 进行授权。

## 架构说明

Next.js 组件将在腾讯云账号中使用到如下 Serverless 服务：

- **API 网关**：API 网关将会接收外部请求并且转发到 SCF 云函数中。
- **SCF 云函数**：云函数将承载 Next.js 应用。
- **CAM 访问控制**：该组件会创建默认 CAM 角色用于授权访问关联资源。
- **COS 对象存储**：为确保上传速度和质量，云函数压缩并上传代码时，会默认将代码包存储在特定命名的 COS 桶中

## 操作步骤

> 以下步骤主要针对命令行部署操作，控制台部署请参考[控制台部署指南](./console)。

### 1. （可选）初始化 Next.js 模版项目
如果您本地并没有 Next.js 项目，可通过以下指令快速新建一个 Next.js 项目模版（本地已有项目可跳过该步骤）
```
serverless init nextjs-starter --name example
cd example
```

### 2. （可选）修改入口函数代码
如果项目使用了自定义 Node.js 服务，比如 express 或者 koa 框架，你需要对入口文件 sls.js（或 app.js）做出改造，导出对应框架 app（未使用可跳过该步骤）, 点此查看[改造模版](#1)。


### 3. 项目构建
```
npm run build
```

### 4. 快速生成 yml 文件并进行部署

完成代码修改后，通过执行 `sls deploy` 指令，Serverless Framework 会自动帮您生成基本的 `serverless.yml` 文件，并完成部署，实现 Next.js 框架应用的快速迁移。

生成的默认配置文件如下：
```yml
component: nextjs
name: nextjsDemo
app: appDemo

inputs:
  src: ./
  exclude:
      - .env
  region: ap-guangzhou
  runtime: Nodejs10.15
  apigatewayConf:
    protocols:
      - http
      - https
    environment: release
```
部署完成后，通过访问输出的 API 网关链接，完成对应用的访问。

### 5. 查看部署状态

在`serverless.yml`文件所在的目录下，通过如下命令查看部署状态：

```
$ serverless info
```

## 更多操作

<span id="1"></span>
### 项目迁移改造模版
- Express 模版

```js
const express = require('express')
const next = require('next')

// not report route for custom monitor
const noReportRoutes = ['/_next', '/static', '/favicon.ico']

async function createServer() {
  const app = next({ dev: false })
  const handle = app.getRequestHandler()

  await app.prepare()

  const server = express()
  server.all('*', (req, res) => {
    noReportRoutes.forEach((route) => {
      if (req.path.indexOf(route) !== -1) {
        req.__SLS_NO_REPORT__ = true
      }
    })
    return handle(req, res)
  })

  // define binary type for response
  // if includes, will return base64 encoded, very useful for images
  server.binaryTypes = ['*/*']

  return server
}

module.exports = createServer
```

- Koa 模版
```js
const Koa = require('koa')
const next = require('next')

async function createServer() {
  const app = next({ dev: false })
  const handle = app.getRequestHandler()

  const server = new Koa()
  server.use((ctx) => {
    ctx.status = 200
    ctx.respond = false
    ctx.req.ctx = ctx

    return handle(ctx.req, ctx.res)
  })

  // define binary type for response
  // if includes, will return base64 encoded, very useful for images
  server.binaryTypes = ['*/*']

  return server
}

module.exports = createServer
```

### 自定义监控

当您在部署 Next.js 应用时，如果 `serverless.yml` 中未指定 `role`，默认会尝试绑定 `QCS_SCFExcuteRole`，并且开启自定义监控，帮助您收集应用监控指标。对于为自定义入口文件的项目，会默认上报除含有 `/_next` 和 `/static` 的路由。

如果您想自定义上报自己的路由性能，可以自定义 `sls.js` 入口文件。
对于无需上报的路由，在 express 服务的 `req` 对象上添加 `__SLS_NO_REPORT__` 属性值为 `true` 即可。例如：
```js
server.get('/no-report', (req, res) => {
  req.__SLS_NO_REPORT__ = true
  return handle(req, res)
})
```
配置后，用户在访问 `GET /no-report` 路由时，就不会上报自定义监控指标。



## 更多资源
### 账号配置
当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件。
```bash
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存。
```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 `SecretId` 和`SecretKey`。


### 更多组件
可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。

### 常见问题
**为什么不需要入口文件了？**
在上一个版本中，使用此组件，用户需要在项目根目录新增 sls.js 文件，现在组件帮忙处理了，所以不需要用户单独处理。具体请参考 [GitHub 文档](https://github.com/serverless-components/tencent-nextjs/issues/1)。

