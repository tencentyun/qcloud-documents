## 操作场景
Koa 组件通过使用 serverless-tencent 的基础组件（如 API 网关组件、SCF 组件等），可以帮助我们快速、方便的在腾讯云创建、配置和管理一个 [Koa 框架](https://koajs.com/)。

## 操作步骤
通过 Koa 组件，对一个 Koa 应用进行完整的创建、配置、部署和删除等操作。支持命令如下：

#### 安装

通过 npm 安装 Serverless：
```console
$ npm install -g serverless
```

#### 创建

1. 本地创建 `serverless.yml` 文件和 `app.js`文件：
```console
$ touch serverless.yml
```
2. 初始化一个新的 npm 包，并安装 Koa：
```
npm init              # 创建后持续回车
npm i --save koa  # 安装 koa
```
3. 创建一个 `app.js`文件，
```console
$ touch app.js
```
4. 在 `app.js` 文件中创建您的 Koa App：
```js
const koa = require('koa');
const app = new koa();
app.use(async (ctx, next) => {
  if (ctx.path !== '/') return next();
  ctx.body = 'Hello from Koa';
});
// don't forget to export!
module.exports = app;
```

#### 配置

在 serverless.yml 中进行如下配置：
```yml
# serverless.yml

koa:
  component: '@serverless/tencent-koa'
  inputs:
    region: ap-shanghai
```

#### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息。
>?`sls`命令是`serverless`命令的缩写

```
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Compressing function KoaComponent_7xRrrd file to /Users/dfounderliu/Desktop/temp/code/.serverless/KoaComponent_7xRrrd.zip.
  DEBUG ─ Compressed function KoaComponent_7xRrrd file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-shanghai-code]. sls-cloudfunction-default-KoaComponent_7xRrrd-1572512568.zip
  DEBUG ─ Uploaded package successful /Users/dfounderliu/Desktop/temp/code/.serverless/KoaComponent_7xRrrd.zip
  DEBUG ─ Creating function KoaComponent_7xRrrd
  DEBUG ─ Created function KoaComponent_7xRrrd successful
  DEBUG ─ Starting API-Gateway deployment with name koa.TencentApiGateway in the ap-shanghai region
  DEBUG ─ Using last time deploy service id service-n0vs2ohb
  DEBUG ─ Updating service with serviceId service-n0vs2ohb.
  DEBUG ─ Endpoint ANY / already exists with id api-9z60urs4.
  DEBUG ─ Updating api with api id api-9z60urs4.
  DEBUG ─ Service with id api-9z60urs4 updated.
  DEBUG ─ Deploying service with id service-n0vs2ohb.
  DEBUG ─ Deployment successful for the api named koa.TencentApiGateway in the ap-shanghai region.

  koa:
    region:              ap-shanghai
    functionName:        KoaComponent_7xRrrd
    apiGatewayServiceId: service-n0vs2ohb
    url:                 http://service-n0vs2ohb-1300415943.ap-shanghai.apigateway.myqcloud.com/release/

  36s › koa › done

```

部署完毕后，可以在浏览器中访问返回的链接，看到对应的 Koa 返回值。

#### 移除

通过以下命令移除部署的存储桶：
```
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removed function KoaComponent_MHrAzr successful
  DEBUG ─ Removing any previously deployed API. api-kf2hxrhc
  DEBUG ─ Removing any previously deployed service.  service-n0vs2ohb

  13s › koa › done
```

#### 账号配置（可选）

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
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi)中获取 SecretId 和 SecretKey。
