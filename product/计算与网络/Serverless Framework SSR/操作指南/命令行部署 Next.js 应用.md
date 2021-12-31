## 操作场景
Serverless SSR 为您提供了完整的命令行开发流程，该任务指导您通过 [Serverless Framework](https://cloud.tencent.com/document/product/1154) 命令行工具完成 Next.js 应用的部署与开发。 

## 架构说明

Next.js 组件将在腾讯云账号中使用到如下 Serverless 服务：

- **API 网关**：API 网关将会接收外部请求并且转发到 SCF 云函数中。 
- **SCF 云函数**：云函数将承载 Next.js 应用。 
- **CAM 访问控制**：该组件会创建默认 CAM 角色用于授权访问关联资源。 
- **COS 对象存储**：为确保上传速度和质量，云函数压缩并上传代码时，会默认将代码包存储在特定命名的 COS 桶中

## 操作步骤
### 1. 安装

通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：
```bash
$ npm install -g serverless
```

### 2. 配置

本地初始化 next.js 的模版项目（可跳过，您也可以使用您已有的 next.js 项目）
```
sls init nextjs-demo
```

在项目的实际业务代码目录下，创建 `serverless.yml` 文件：
```bash
$ touch serverless.yml
```

进行如下配置：
```yml
# serverless.yml
component: nextjs # (必填) 组件名称，此处为 nextjs
name: nextjsDemo # (必填) 实例名称
org: orgDemo # (可选) 用于记录组织信息，默认值为您的腾讯云账户 APPID
app: appDemo # (可选) 该 next.js 应用名称
stage: dev # (可选) 用于区分环境信息，默认值是 dev

inputs:
  src: ./
  functionName: nextjsDemo
  region: ap-guangzhou
  runtime: Nodejs10.15
  exclude:
    - .env
  apigatewayConf:
    protocols:
      - http
      - https
    environment: release
```

查看 [更多配置及说明 >>](https://github.com/serverless-components/tencent-nextjs/tree/v2/docs/configure.md)


### 3. 部署

#### 3.1 构建静态资源

```bash
$ npm run build
```

#### 3.2 部署到云端

在 serverless.yml 文件下的目录中运行以下指令进行部署：

```bash
$ sls deploy
```

部署时需要进行身份验证，如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。 

>?如果希望查看更多部署过程的信息，可以通过`sls deploy --debug` 命令查看部署过程中的实时日志信息（`sls`是 `serverless` 命令的缩写）。


### 4. 查看部署状态

在`serverless.yml`文件所在的目录下，通过如下命令查看部署状态：

```
$ serverless info
```

### 5. 移除

在`serverless.yml`文件所在的目录下，通过以下命令移除部署通过以下命令移除部署的 API 网关，移除后该组件会对应删除云上部署时所创建的所有相关资源。 

```bash
$ sls remove
```

和部署类似，支持通过 `sls remove --debug` 命令查看移除过程中的实时日志信息（`sls`是 `serverless` 命令的缩写）。

## 更多操作

### 项目迁移
部署 Next.js 应用时，Serverless SSR 会自动为您创建 `sls.js` 入口文件，如果您的项目本身运行是基于 `express` 自定义服务，您也可以在项目中自定义入口文件 `sls.js`，需要参考您的服务启动文件进行修改，以下是一个 Next.js 项目的模板文件：

```js
const express = require('express')
const next = require('next')

const app = next({ dev: false })
const handle = app.getRequestHandler()

// not report route for custom monitor
const noReportRoutes = ['/_next', '/static']

async function createServer() {
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

### 账号配置

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```bash
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：

```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```

>?
>- 如果没有腾讯云账号，可以在此 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 `SecretId` 和`SecretKey`。


### 自定义监控

当您在部署 Next.js 应用时，如果 `serverless.yml` 中未指定 `role`，默认会尝试绑定 `QCS_SCFExcuteRole`，并且开启自定义监控，帮助您收集应用监控指标。 对于为自定义入口文件的项目，会默认上报除含有 `/_next` 和 `/static` 的路由。 

如果您想自定义上报自己的路由性能，可以自定义 `sls.js` 入口文件。 
对于无需上报的路由，在 express 服务的 `req` 对象上添加 `__SLS_NO_REPORT__` 属性值为 `true` 即可。 例如：
```js
server.get('/no-report', (req, res) => {
  req.__SLS_NO_REPORT__ = true
  return handle(req, res)
})
```
配置后，用户在访问 `GET /no-report` 路由时，就不会上报自定义监控指标。 





