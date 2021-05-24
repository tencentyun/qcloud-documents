## 操作场景
腾讯云 [Next.js](https://github.com/zeit/next.js) Serverless Component，支持 Restful API 服务的部署。

## 前提条件
#### 初始化 Next.js 项目

```bash
$ npm init next-app
```

#### 新增初始化文件
在项目根目录下新建`sls.js`文件，内容如下：

```js
const express = require('express')
const next = require('next')

const app = next({ dev: false })
const handle = app.getRequestHandler()

async function creatServer() {
  await app.prepare()
  const server = express()

  server.all('*', (req, res) => {
    return handle(req, res)
  })

  // 定义是否返回 base64 编码的文件 mime 类型。默认是所有文件，因为 next.js 默认 build 开启 gzip.
  // 如果需要修改，请先理解 gzip 的文件编码方式。
  server.binaryTypes = ['*/*']

  return server
}

module.exports = creatServer
```

添加`express`依赖：
```
$ npm i express --save
```

>?这里通过 express 服务来代理 next.js 的服务。

## 操作步骤
#### 安装

通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：
```bash
$ npm install -g serverless
```

#### 配置

1.在项目根目录创建`serverless.yml`文件：
```bash
$ touch serverless.yml
```

2.在`serverless.yml`中进行如下配置：
```yml
# serverless.yml
NextjsFunc:
  component: '@serverless/tencent-nextjs'
  inputs:
    functionName: nextjs-function
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

[查看详细配置文档 >>](https://github.com/serverless-components/tencent-nextjs/tree/master/docs/configure.md)

#### 部署

您可以通过下面步骤进行部署：

**1. 构建静态资源**
```bash
$ npm run build
```

**2. 部署到云端**
如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息：
>?`sls`是`serverless`命令的简写。

```bash
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Compressing function nextjs-function file to /Users/yugasun/Desktop/Develop/serverless/tencent-nextjs/example/.serverless/nextjs-function.zip.
  DEBUG ─ Compressed function nextjs-function file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-guangzhou-code]. sls-cloudfunction-default-nextjs-function-1582430808.zip
  DEBUG ─ Uploaded package successful /Users/yugasun/Desktop/Develop/serverless/tencent-nextjs/example/.serverless/nextjs-function.zip
  DEBUG ─ Creating function nextjs-function
  DEBUG ─ Updating code...
  DEBUG ─ Updating configure...
  DEBUG ─ Created function nextjs-function successful
  DEBUG ─ Setting tags for function nextjs-function
  DEBUG ─ Creating trigger for function nextjs-function
  DEBUG ─ Deployed function nextjs-function successful
  DEBUG ─ Starting API-Gateway deployment with name NextjsFunc.TencentApiGateway in the ap-guangzhou region
  DEBUG ─ Using last time deploy service id service-32okcrfq
  DEBUG ─ Updating service with serviceId service-32okcrfq.
  DEBUG ─ Endpoint ANY / already exists with id api-5242vfgi.
  DEBUG ─ Updating api with api id api-5242vfgi.
  DEBUG ─ Service with id api-5242vfgi updated.
  DEBUG ─ Deploying service with id service-32okcrfq.
  DEBUG ─ Deployment successful for the api named NextjsFunc.TencentApiGateway in the ap-guangzhou region.

  NextjsFunc:
    region:              ap-guangzhou
    functionName:        nextjs-function
    apiGatewayServiceId: service-32okcrfq
    url:                 https://service-32okcrfq-1251556596.gz.apigw.tencentcs.com/release/

  34s › NextjsFunc › done
```


#### 移除

通过以下命令移除部署的服务：
```bash
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing function
  DEBUG ─ Request id
  DEBUG ─ Removed function nextjs-function successful
  DEBUG ─ Removing any previously deployed API. api-5242vfgi
  DEBUG ─ Removing any previously deployed service. service-32okcrfq

  11s › NextjsFunc › done
```

#### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建`.env`文件：
```bash
$ touch .env # 腾讯云的配置信息
```
在`.env`文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：
```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
