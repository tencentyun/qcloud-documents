## 操作场景

**腾讯云 [Nuxt.js](https://github.com/nuxt/nuxt.js) 组件**通过使用 [**Tencent Serverless Framework**](https://github.com/serverless/components/tree/cloud)，基于云上 Serverless 服务（如 API 网关、云函数等），实现“0”配置，便捷开发，极速部署采用 Nuxt.js 框架的网页应用，Nuxt.js 组件支持丰富的配置扩展，提供了目前便捷实用、开发成本低的网页应用项目的开发/托管能力。

特性介绍：
- **按需付费**：按照请求的使用量进行收费，没有请求时无需付费。
- **"0"配置**：只需要关心项目代码，直接部署即可，Serverless Framework 会搞定所有配置。
- **极速部署**：部署速度快，仅需几秒即可部署整个应用。
- **实时日志**：通过实时日志的输出查看业务状态，便于直接在云端开发应用。
- **云端调试**：可在云端直接进行项目调试，从而避免本地环境的差异。
- **便捷协作**：通过云端控制台的状态信息和部署日志，方便进行多人协作开发。


通过 [Serverless Framework Nuxt.js 组件](https://github.com/serverless-components/tencent-nuxtjs)，可以快速实现 Next.js 传统应用从本地到 Serverless 函数平台的迁移。

## 迁移前提

- 已经 [安装 Serverless Framework 1.67.2](https://cloud.tencent.com/document/product/1154/42990) 以上版本。
- 已经[注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)并完成[实名认证](https://cloud.tencent.com/document/product/378/10495)。

>?如果您的账号为**腾讯云子账号**，请首先联系主账号，参考 [账号和权限配置](https://cloud.tencent.com/document/product/1154/43006) 进行授权。

## 架构说明

Nuxt.js 组件将在腾讯云账号中使用到如下 Serverless 服务：

- **API 网关**：API 网关将会接收外部请求并且转发到 SCF 云函数中。
- **SCF 云函数**：云函数将承载 Nuxt.js 应用。
- **CAM 访问控制**：该组件会创建默认 CAM 角色用于授权访问关联资源。
- **COS 对象存储**：为确保上传速度和质量，云函数压缩并上传代码时，会默认将代码包存储在特定命名的 COS 桶中。

## 操作步骤
>?以下步骤主要针对命令行部署操作，控制台部署请参考 [控制台部署指南](https://cloud.tencent.com/document/product/1154/50957)。

### 1. 初始化 Nuxt.js 模版项目（可选）
如果您本地并没有 Next.js 项目，可通过以下指令快速新建一个 Next.js 项目模版（本地已有项目可跳过该步骤）：
```
serverless init nuxtjs-starter --name example
cd example
```

### 2. 修改入口函数代码（可选）
如果项目使用了自定义 Node.js 服务，例如 express 或者 koa 框架，您需要对入口文件 sls.js（或 app.js）做出改造，导出对应框架 app（未使用可跳过该步骤）, 点此查看 [改造模版](#1)。

### 3. 项目构建
```
npm run build
```

### 4. 快速生成 yml 文件并进行部署

完成代码修改后，通过执行 `sls deploy` 指令，Serverless Framework 会自动帮您生成基本的 `serverless.yml` 文件，并完成部署，实现 Nuxt.js 框架应用的快速迁移。

生成的默认配置文件如下：
```yml
component: nuxtjs
name: nuxtjsDemo
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


<span id="1"></span>
## 项目迁移改造模版

- Express 模版

```js
const express = require('express')
const { loadNuxt } = require('nuxt')

async function createServer() {
  // not report route for custom monitor
  const noReportRoutes = ['/_nuxt', '/static', '/favicon.ico']

  const server = express()
  const nuxt = await loadNuxt('start')

  server.all('*', (req, res, next) => {
    noReportRoutes.forEach((route) => {
      if (req.path.indexOf(route) === 0) {
        req.__SLS_NO_REPORT__ = true
      }
    })
    return nuxt.render(req, res, next)
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
const express = require('express')
const { loadNuxt } = require('nuxt')

async function createServer() {
  // not report route for custom monitor
  const noReportRoutes = ['/_nuxt', '/static', '/favicon.ico']

  const server = express()
  const nuxt = await loadNuxt('start')

  server.all('*', (req, res, next) => {
    noReportRoutes.forEach((route) => {
      if (req.path.indexOf(route) === 0) {
        req.__SLS_NO_REPORT__ = true
      }
    })
    return nuxt.render(req, res, next)
  })

  // define binary type for response
  // if includes, will return base64 encoded, very useful for images
  server.binaryTypes = ['*/*']

  return server
}

module.exports = createServer
```

### 自定义监控

>?目前仅支持自定义 Express 服务的项目。

当在部署 Nuxt.js 应用时，如果 `serverless.yml` 中未指定 `role`，默认会尝试绑定 `QCS_SCFExcuteRole`，并且开启自定义监控，帮助用户收集应用监控指标。对于为自定义入口文件的项目，会默认上报除含有 `/_nuxt`、`/static` 和 `/favicon.ico` 的路由。

如果您想自定义上报自己的路由性能，那么可以自定义 `sls.js` 入口文件，对于无需上报的路由，在 express 服务的 `req` 对象上添加 `__SLS_NO_REPORT__` 属性值为 `true` 即可。例如：

```js
server.get('/no-report', (req, res, next) => {
  req.__SLS_NO_REPORT__ = true
  return nuxt.render(req, res, next)
})
```

那么用户在访问 `GET /no-report` 路由时，就不会上报自定义监控指标。

## 更多资源
### 账号配置

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件。
```bash
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存。
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 `SecretId` 和`SecretKey`。

```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>!使用中国境外 IP 登录时，需要在 `.env` 文件中添加 `SERVERLESS_PLATFORM_VENDOR=tencent` ，使 sls 默认使用 tencent 组件。

### 更多组件

您可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。

### 常见问题
**为什么不需要入口文件了？**
在上一个版本中，使用此组件，用户需要在项目根目录新增 sls.js 文件，现在组件帮忙处理了，所以不需要用户单独处理。具体请参考 [GitHub 文档](https://github.com/serverless-components/tencent-nuxtjs/issues/1)。

