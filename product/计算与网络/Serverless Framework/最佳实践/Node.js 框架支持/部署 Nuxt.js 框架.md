# 腾讯云 Nuxt.js Serverless Component

## 简介

腾讯云 [Nuxt.js](https://github.com/nuxt/nuxt.js) Serverless Component 支持通过云函数和 API 网关在云端部署 Nuxt.js 框架。

## 目录

0. [准备](#0-准备)
1. [安装](#1-安装)
1. [配置](#2-配置)
1. [部署](#3-部署)
1. [移除](#4-移除)

### 0. 准备

#### 初始化 Nuxt.js 项目

```bash
$ npx create-nuxt-app serverlesss-nuxtjs
$ cd serverlesss-nuxtjs
```

添加 `express` 依赖：

```
$ npm i express --save
```

> 注释：这里通过 express 服务来代理 nuxt.js 的服务。

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
NuxtjsFunc:
  component: '@serverless/tencent-nuxtjs'
  inputs:
    functionName: nuxtjs-function
    region: ap-guangzhou
    code: ./
    functionConf:
      timeout: 30
      memorySize: 128
    environment:
      variables:
        RUN_ENV: test
    apigatewayConf:
      protocols:
        - http
        - https
      environment: release
```

- [更多配置](https://github.com/serverless-components/tencent-nuxtjs/tree/master/docs/configure.md)

### 3. 部署

#### 3.1 构建静态资源

```bash
$ npm run build
```

#### 3.2 部署到云端

如您的账号未 [登陆](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过 `微信` 扫描命令行中的二维码进行授权登陆和注册。

通过 `sls` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息

```bash
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Generating serverless handler...
  DEBUG ─ Generated serverless handler successfully.
  DEBUG ─ Compressing function nuxtjs-function file to /Users/yugasun/Desktop/Develop/serverless/tencent-nuxtjs/example/.serverless/nuxtjs-function.zip.
  DEBUG ─ Compressed function nuxtjs-function file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-guangzhou-code]. sls-cloudfunction-default-nuxtjs-function-1584350378.zip
  DEBUG ─ Uploaded package successful /Users/yugasun/Desktop/Develop/serverless/tencent-nuxtjs/example/.serverless/nuxtjs-function.zip
  DEBUG ─ Creating function nuxtjs-function
  nuxtjs-function [████████████████████████████████████████] 100% | ETA: 0s | Speed: 1502.16k/s
  DEBUG ─ Created function nuxtjs-function successful
  DEBUG ─ Setting tags for function nuxtjs-function
  DEBUG ─ Creating trigger for function nuxtjs-function
  DEBUG ─ Deployed function nuxtjs-function successful
  DEBUG ─ Starting API-Gateway deployment with name ap-guangzhou-apigateway in the ap-guangzhou region
  DEBUG ─ Service with ID service-dxcq0xuu created.
  DEBUG ─ API with id api-b83j9sme created.
  DEBUG ─ Deploying service with id service-dxcq0xuu.
  DEBUG ─ Deployment successful for the api named ap-guangzhou-apigateway in the ap-guangzhou region.

  NuxtjsFunc:
    functionName:        nuxtjs-function
    functionOutputs:
      ap-guangzhou:
        Name:        nuxtjs-function
        Runtime:     Nodejs8.9
        Handler:     serverless-handler.handler
        MemorySize:  128
        Timeout:     30
        Region:      ap-guangzhou
        Namespace:   default
        Description: This is a template function
    region:              ap-guangzhou
    apiGatewayServiceId: service-dxcq0xuu
    url:                 https://service-dxcq0xuu-1251556596.gz.apigw.tencentcs.com/release/
    cns:                 (empty array)

  38s › NuxtjsFunc › done
```

> 注意: `sls` 是 `serverless` 命令的简写。

### 4. 移除

通过以下命令移除部署的 Nuxjs 服务，包括云函数和 API 网关。

```bash
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removed function nuxtjs-function successful
  DEBUG ─ Removing any previously deployed API. api-b83j9sme
  DEBUG ─ Removing any previously deployed service. service-dxcq0xuu

  8s › NuxtjsFunc › done
```

### 账号配置（可选）

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

### 更多组件

可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。

### FAQ

1. [为什么不需要入口文件了？](https://github.com/serverless-components/tencent-nuxtjs/issues/1)