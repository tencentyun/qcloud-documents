
## 操作场景
腾讯云 [Egg.js](https://github.com/eggjs/egg) Serverless Component，支持 Restful API 服务的部署。

## 前提条件

#### 初始化 Egg 项目
```shell
$ mkdir serverless-egg && cd serverless-egg
$ npm init egg src --type=simple
$ cd src && npm install
```


## 操作步骤
### 1. 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：
```shell
$ npm install -g serverless
```

### 2. 配置
在项目根目录创建`serverless.yml`文件：
```shell
$ touch serverless.yml
```
在`serverless.yml` 文件中进行如下配置（yml 文件的配置信息请参考 [全量配置文档](https://github.com/serverless-components/tencent-egg/blob/master/docs/configure.md)）：
```yml
component: egg
name: eggDemo
app: appDemo

inputs:
  src: ./
  region: ap-guangzhou
  runtime: Nodejs10.15
  apigatewayConf:
    protocols:
      - http
      - https
    environment: release
```

### 3. 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过 `sls deploy` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息：
>?`sls` 是 `serverless` 命令的简写。

```shell
$ sls deploy

  MyComponent: 
    region:              ap-beijing
    functionName:        egg-function
    apiGatewayServiceId: service-n5m5e8x3
    url:                 https://service-n5m5e8x3-1251971143.bj.apigw.tencentcs.com/release/

  32s › MyComponent › done
```

### 4. 移除

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

### 账号配置（可选）

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

## 更多资源
### 常见问题

1. **app/public 目录部署后不存在如何解决？**

   通常初始化的 egg 项目，会自动创建 app/public 目录。但是在打包压缩时，如果该目录为空，则部署后，该目录不会存在。所以 egg 项目启动时会自动创建，但是云函数是没有操作权限的，建议在 app/public 目录下创建一个空文件 .gitkeep，来解决此问题。

2. **引入 Layer，部署后报依赖模块查找失败如何解决？**

   详情请参考 issue：[关于将 egg 项目 node_modules 上传层部署问题](https://github.com/serverless-components/tencent-egg/issues/11#issue-618169731)。

### 更多组件
可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。
