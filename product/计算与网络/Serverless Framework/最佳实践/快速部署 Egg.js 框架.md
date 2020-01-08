
## 操作场景
腾讯云 [Egg.js](https://github.com/eggjs/egg) Serverless Component，支持 Restful API 服务的部署。

## 前提条件

#### 初始化 Egg 项目

```shell
$ mkdir egg-example && cd egg-example
$ npm init egg --type=simple
$ npm i
```

#### 修改 Egg 配置

由于云函数在执行时，只有 `/tmp` 可读写的，所以我们需要将 `egg.js` 框架运行尝试的日志写到该目录下，为此需要修改 `config/config.default.js` 中的配置如下：

```js
const config = exports = {
  env: 'prod', // 推荐云函数的 egg 运行环境变量修改为 prod
  rundir: '/tmp',
  logger: {
    dir: '/tmp',
  },
};
```

## 操作步骤
#### 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：
```shell
$ npm install -g serverless
```

#### 配置
在项目根目录创建 `serverless.yml` 文件：
```shell
$ touch serverless.yml
```
在`serverless.yml` 文件中进行如下配置：
```yml
# serverless.yml

MyComponent:
  component: "@serverless/tencent-egg"
  inputs:
    region: ap-guangzhou 
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
      protocol: https
      environment: release
```

[查看详细配置文档 >>](https://github.com/serverless-components/tencent-egg/tree/master/docs/configure.md)

#### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过 `sls` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息：
```shell
$ sls --debug
```

>?`sls` 是 `serverless` 命令的简写。

#### 移除

通过以下命令移除部署的 API 网关：
```shell
$ sls remove --debug
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
