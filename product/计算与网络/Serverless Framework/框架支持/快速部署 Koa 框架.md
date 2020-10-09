## 操作场景
Koa 组件通过使用 serverless-tencent 的基础组件（如 API 网关组件、SCF 组件等），可以帮助我们快速、方便的在腾讯云创建、配置和管理一个 [Koa 框架](https://koajs.com/)。

>!建议您使用 Node.js10.0 及以上版本，否则 Component V2 部署有可能报错。

## 操作步骤
通过 Koa 组件，对一个 Koa 应用进行完整的创建、配置、部署和删除等操作。支持命令如下：

### 1. 安装

通过 npm 安装 Serverless：
```console
npm install -g serverless
```

### 2. 创建

1.本地创建一个新文件夹，并在文件夹下创建 `serverless.yml`：
```console
mkdir test && cd test
touch serverless.yml 
```
2.初始化一个新的 npm 包，并安装 Koa：
```
npm init              # 创建后持续回车
npm i --save koa  # 安装 koa
```
3.本地创建一个 `sls.js` 文件：
```console
touch sls.js
```
4.在 `sls.js` 文件中创建您的 Koa App：
```js
const koa = require('koa')
const app = new koa()

app.use(async (ctx, next) => {
  if (ctx.path !== '/') return next()
  ctx.body = 'Hello from Koa'
})

// set binary types
// app.binaryTypes = [*/*];

// don't forget to export!
module.exports = app
```

### 3. 配置

在 serverless.yml 中进行如下配置：
```yml
# serverless.yml

app: appDemo # (optional) serverless dashboard app. default is the same as the name property.
stage: dev # (optional) serverless dashboard stage. default is dev.
component: koa # (required) name of the component. In that case, it's koa.
name: koaDemo # (required) name of your koa component instance.

inputs:
  src:
    src: ./ # (optional) path to the source folder. default is a hello world app.
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
[查看详细配置文档 >>](https://github.com/serverless-components/tencent-koa/blob/master/docs/configure.md)

### 4. 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls deploy`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息。
>?`sls`命令是`serverless`命令的缩写

```
$ sls deploy

  koa:
    region:              ap-shanghai
    functionName:        KoaComponent_7xRrrd
    apiGatewayServiceId: service-n0vs2ohb
    url:                 http://service-n0vs2ohb-1300415943.ap-shanghai.apigateway.myqcloud.com/release/

  36s › koa › done

```

部署完毕后，可以在浏览器中访问返回的链接，看到对应的 Koa 返回值。

### 5. 移除

通过以下命令移除部署的存储桶：
```
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removed function KoaComponent_MHrAzr successful
  DEBUG ─ Removing any previously deployed API. api-kf2hxrhc
  DEBUG ─ Removing any previously deployed service.  service-n0vs2ohb

  13s › koa › done
```

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
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi)中获取 SecretId 和 SecretKey。

## 更多组件
可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。
