## 操作场景

**腾讯云 [Nuxt.js](https://github.com/nuxt/nuxt.js) 组件**通过使用 [**Tencent Serverless Framework**](https://github.com/serverless/components/tree/cloud)，基于云上 Serverless 服务（如 API 网关、云函数等），实现“0”配置，便捷开发，极速部署采用 Nuxt.js 框架的网页应用，Nuxt.js 组件支持丰富的配置扩展，提供了目前便捷实用、开发成本低的网页应用项目的开发/托管能力。

特性介绍：
- **按需付费**：按照请求的使用量进行收费，没有请求时无需付费。
- **"0"配置**：只需要关心项目代码，直接部署即可，Serverless Framework 会搞定所有配置。
- **极速部署**：部署速度快，仅需几秒即可部署整个应用。
- **实时日志**：通过实时日志的输出查看业务状态，便于直接在云端开发应用。
- **云端调试**：可在云端直接进行项目调试，从而避免本地环境的差异。
- **便捷协作**：通过云端控制台的状态信息和部署日志，方便进行多人协作开发。


## 前提条件

#### 初始化 Nuxt.js 项目

在本地创建根目录，并初始化一个 Nuxt.js 项目：
```bash
$ mkdir serverless-nuxtjs && cd serverless-nuxtjs
$ npx create-nuxt-app src
```
>!本教程中的 Nuxt 项目使用 JavaScript 与 Npm 安装包进行构建，初始化项目的时候请选择相应的选项。

## 操作步骤
### 1. 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：
```bash
$ npm install -g serverless
```

### 2. 配置
在项目根目录创建 `serverless.yml` 文件：
```bash
$ touch serverless.yml
```
在 `serverless.yml` 中进行如下配置：
```yml
# serverless.yml
component: nuxtjs # (必填) 组件名称，此处为 nuxtjs
name: nuxtjsDemo # (必填) 实例名称
org: orgDemo # (可选) 用于记录组织信息，默认值为您的腾讯云账户 APPID
app: appDemo # (可选) 该 nuxt.js 项目名称
stage: dev # (可选) 用于区分环境信息，默认值是 dev

inputs:
  src:
    src: ./src
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

查看 [更多配置及说明 >>](https://github.com/serverless-components/tencent-nextjs/tree/v2/docs/configure.md)

### 3. 部署
#### 3.1 构建静态资源

进入到 nuxt 项目目录下，构建静态资源：
```bash
$ cd src && npm run build
```

#### 3.2 部署到云端

回到在 serverless.yml 文件所在的项目根目录，运行以下指令进行部署：
```bash
# 进入项目根目录 serverless-nuxtjs
$ sls deploy

serverless ⚡ framework
Action: "deploy" - Stage: "dev" - App: "appDemo" - Instance: "nuxtjsDemo"

region: ap-guangzhou
apigw:
  serviceId:   service-4v2jx72g
  subDomain:   service-4v2jx72g-1258834142.gz.apigw.tencentcs.com
  environment: release
  url:         https://xxxxxx.gz.apigw.tencentcs.com/release/
scf:
  functionName: nuxtjs_component_mm518kl
  runtime:      Nodejs10.15
  namespace:    default

139s › nuxtjsDemo › Success
```

部署时需要进行身份验证，如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。
>?如果希望查看更多部署过程的信息，可以通过 `sls deploy --debug` 命令查看部署过程中的实时日志信息（`sls`是 `serverless` 命令的缩写）。


### 4. 开发调试

部署了 Nuxt.js 应用后，可以通过开发调试能力对该项目进行二次开发，从而开发一个生产应用。在本地修改和更新代码后，不需要每次都运行 `serverless deploy` 命令来反复部署。您可以直接通过 `serverless dev` 命令对本地代码的改动进行检测和自动上传。
可以通过在 `serverless.yml` 文件所在的目录下运行 `serverless dev` 命令开启开发调试能力。
`serverless dev` 同时支持实时输出云端日志，每次部署完毕后，对项目进行访问，即可在命令行中实时输出调用日志，便于查看业务情况和排障。

### 5. 查看部署状态

在 `serverless.yml` 文件所在的目录下，通过如下命令查看部署状态：

```
$ serverless info
```

### 6. 移除

在 `serverless.yml` 文件所在的目录下，通过以下命令移除部署的 API 网关，移除后该组件会对应删除云上部署时所创建的所有相关资源。

```bash
$ sls remove
```
和部署类似，支持通过 `sls remove --debug` 命令查看移除过程中的实时日志信息（`sls`是 `serverless` 命令的缩写）。

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

