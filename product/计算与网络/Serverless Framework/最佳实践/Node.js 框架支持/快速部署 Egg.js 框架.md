
## 操作场景
腾讯云 [Egg.js](https://github.com/eggjs/egg) Serverless Component，支持 Restful API 服务的部署。

## 前提条件

#### 初始化 Egg 项目
```shell
$ mkdir egg-example && cd egg-example
$ npm init egg --type=simple
$ npm i
```

#### 新增初始化文件

在项目根目录下新建`sls.js`文件，内容如下：
```js
const { Application } = require('egg')

const app = new Application({
  env: 'prod'
})

module.exports = app
```

#### 修改 Egg 配置

由于云函数在执行时，只有`/tmp`可读写的，所以我们需要将`egg.js`框架运行尝试的日志写到该目录下，为此需要修改`config/config.default.js`中的配置如下：

```js
const config = exports = {
  env: 'prod', // 推荐云函数的 egg 运行环境变量修改为 prod
  rundir: '/tmp',
  logger: {
    dir: '/tmp',
  },
};
```

#### 注意事项

由于`egg`的`egg-static`静态资源插件是默认开启的，所以在启动应用时，会尝试创建`app/public`目录，但是云函数执行环境只有`/tmp`可读写，所以需要本地创建，并添加`.gitkeep`文件（内容为空）。

如果您不需要使用静态资源，可以通过修改`config/plugin.js`禁用静态资源功能：
```js
module.exports = {
  static: {
    enable: false
  }
}
```

如果您需要开启静态资源功能，并且 public 已经存在，且里面包含静态资源。此时需要配置`binaryTypes`，修改`sls.js`文件如下：
```js
const { Application } = require('egg')

const app = new Application({
  env: 'prod'
})

// 这里可以根据实际情况来配置
// 如果您的站点开启 gzip，那么所有返回类型都应该是二进制类型，所以应该是 app.binaryTypes = ['*/*']
app.binaryTypes = ['image/*']

module.exports = app
```


## 操作步骤
#### 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：
```shell
$ npm install -g serverless
```

#### 配置
在项目根目录创建`serverless.yml`文件：
```shell
$ touch serverless.yml
```
在`serverless.yml` 文件中进行如下配置：
```yml
# serverless.yml

MyComponent:
  component: "@serverless/tencent-egg"
  inputs:
    region: ap-beijing 
    functionName: egg-function
    code: ./
    functionConf:
      timeout: 10
      memorySize: 128
      environment:
        variables:
          TEST: vale
      vpcConfig:
        subnetId: ''
        vpcId: ''
    apigatewayConf:
      protocols:
        - https
      environment: release
```

[查看详细配置文档 >>](https://github.com/serverless-components/tencent-egg/tree/master/docs/configure.md)

#### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过 `sls` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息：
>?`sls` 是 `serverless` 命令的简写。

```shell
$ sls --debug    

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Compressing function egg-function file to /Users/tina/Desktop/live/egg-proj/.serverless/egg-function.zip.
  DEBUG ─ Compressed function egg-function file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-beijing-code]. sls-cloudfunction-default-egg-function-1581335565.zip
  DEBUG ─ Uploaded package successful /Users/tina/Desktop/live/egg-proj/.serverless/egg-function.zip
  DEBUG ─ Creating function egg-function
  DEBUG ─ Updating code... 
  DEBUG ─ Updating configure... 
  DEBUG ─ Created function egg-function successful
  DEBUG ─ Setting tags for function egg-function
  DEBUG ─ Creating trigger for function egg-function
  DEBUG ─ Deployed function egg-function successful
  DEBUG ─ Starting API-Gateway deployment with name MyComponent.TencentApiGateway in the ap-beijing region
  DEBUG ─ Service with ID service-n5m5e8x3 created.
  DEBUG ─ API with id api-cmkhknda created.
  DEBUG ─ Deploying service with id service-n5m5e8x3.
  DEBUG ─ Deployment successful for the api named MyComponent.TencentApiGateway in the ap-beijing region.

  MyComponent: 
    region:              ap-beijing
    functionName:        egg-function
    apiGatewayServiceId: service-n5m5e8x3
    url:                 https://service-n5m5e8x3-1251971143.bj.apigw.tencentcs.com/release/

  32s › MyComponent › done
```

#### 移除

通过以下命令移除部署的 API 网关和云函数：
```shell
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing function
  DEBUG ─ Request id
  DEBUG ─ Removed function egg-function successful
  DEBUG ─ Removing any previously deployed API. api-cmkhknda
  DEBUG ─ Removing any previously deployed service. service-n5m5e8x3

  8s › MyComponent › done

```

#### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```shell
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：
```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
