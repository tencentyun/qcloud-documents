如果您习惯使用 cli 进行开发，Serverless SSR 为您提供了完整的命令行开发流程体验，步骤如下：

>注: 目前 Serverless SSR 只支持 Next.js 与 Nuxt.js 两个框架组件的部署


### 1. 安装

通过 npm 全局安装 [serverless cli](https://github.com/serverless/serverless)

```bash
$ npm install -g serverless
```

### 2. 配置

在项目根目录创建 `serverless.yml` 文件，在其中进行如下配置

```bash
$ touch serverless.yml
```

```yml
# serverless.yml
component: nuxtjs # (必填) 组件名称，此处为nuxtjs
name: nuxtjsDemo # (必填) 实例名称
org: orgDemo # (可选) 用于记录组织信息，默认值为您的腾讯云账户 appid
app: appDemo # (可选) 该 nuxt.js 项目名称
stage: dev # (可选) 用于区分环境信息，默认值是 dev

inputs:
  src:
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

- 点此查看[更多配置及说明](https://github.com/serverless-components/tencent-nextjs/tree/v2/docs/configure.md)


### 3. 部署

#### 3.1 构建静态资源

进入到 nuxt 项目目录下，构建静态资源

```bash
$ cd src && npm run build
```

#### 3.2 部署到云端

在 serverless.yml 文件下的目录中运行以下指令进行部署：

```bash
$ sls deploy
```

部署时需要进行身份验证，如您的账号未 [登陆](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过 `微信` 扫描命令行中的二维码进行授权登陆和注册。

> 注意: 如果希望查看更多部署过程的信息，可以通过`sls deploy --debug` 命令查看部署过程中的实时日志信息，`sls`是 `serverless` 命令的缩写。
> `sls` 是 `serverless` 命令的简写。

### 4. 开发调试

部署了 应用后，可以通过开发调试能力对该项目进行二次开发，从而开发一个生产应用。在本地修改和更新代码后，不需要每次都运行 `serverless deploy` 命令来反复部署。你可以直接通过 `serverless dev` 命令对本地代码的改动进行检测和自动上传。

可以通过在 `serverless.yml`文件所在的目录下运行 `serverless dev` 命令开启开发调试能力。

`serverless dev` 同时支持实时输出云端日志，每次部署完毕后，对项目进行访问，即可在命令行中实时输出调用日志，便于查看业务情况和排障。

### 5. 查看部署状态

在`serverless.yml`文件所在的目录下，通过如下命令查看部署状态：

```
$ serverless info
```

### 6. 移除

在`serverless.yml`文件所在的目录下，通过以下命令移除部署通过以下命令移除部署的 API 网关，移除后该组件会对应删除云上部署时所创建的所有相关资源。

```bash
$ sls remove
```

和部署类似，支持通过 `sls remove --debug` 命令查看移除过程中的实时日志信息，`sls`是 `serverless` 命令的缩写。

### 账号配置

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/秘钥信息，也可以本地创建 `.env` 文件

```bash
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存

如果没有腾讯云账号，可以在此 [注册新账号](https://cloud.tencent.com/register)。

如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 `SecretId` 和`SecretKey`.

```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```

### 项目迁移

部署您的本地项目到云端时，Serverless SSR 会自动帮您创建入口函数 `sls.js`, 您也可以在项目中自定义入口文件 `sls.js`，需要参考你的服务启动文件进行修改，以下是一个 Nuxt.js 项目的模板文件：


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

当在部署 Nuxt.js 应用时，如果 `serverless.yml` 中未指定 `role`，默认会尝试绑定 `QCS_SCFExcuteRole`，并且开启自定义监控，帮助用户收集应用监控指标。对于为自定义入口文件的项目，会默认上报除含有 `/_next` 和 `/static` 的路由。如果你想自定义上报自己的路由性能，那么可以自定义 `sls.js` 入口文件，对于无需上报的路由，在 express 服务的 `req` 对象上添加 `__SLS_NO_REPORT__` 属性值为 `true` 即可。比如：

```js
server.get('/no-report', (req, res) => {
  req.__SLS_NO_REPORT__ = true
  return handle(req, res)
})
```

那么用户在访问 `GET /no-report` 路由时，就不会上报自定义监控指标。
