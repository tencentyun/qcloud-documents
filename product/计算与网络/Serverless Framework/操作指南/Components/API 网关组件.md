## 操作场景
API 网关组件是 serverless-tencent 组件库中的基础组件之一，您可以通过该组件快速且方便地创建、配置和管理腾讯云的 API 网关产品。

## 操作步骤
通过 API 网关组件，您可以对一个 API 服务/接口进行完整的创建、配置、部署和删除等操作，支持的命令如下：

#### 安装

通过 npm 安装 Serverless：

```console
$ npm install -g serverless
```

#### 配置

本地创建 `serverless.yml` 文件，在其中进行如下配置：

```console
$ touch serverless.yml
```

```yml
# serverless.yml

restApi:
  component: "@serverless/tencent-apigateway"
  inputs:
    region: ap-shanghai
    protocol: http
    serviceName: serverless
    environment: release
    endpoints:
      - path: /users
        method: POST
        function:
          functionName: myFunction

```

* [查看详细配置文档>>](https://github.com/serverless-tencent/tencent-apigateway/blob/master/docs/configure.md)


#### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息：

```console
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Starting API-Gateway deployment with name restApi in the ap-shanghai region
  DEBUG ─ Service with ID service-g1ihx7c7 created.
  DEBUG ─ API with id api-4dv8r7wg created.
  DEBUG ─ Deploying service with id service-g1ihx7c7.
  DEBUG ─ Deployment successful for the api named restApi in the ap-shanghai region.

  restApi: 
    protocol:    http
    subDomain:   service-g1ihx7c7-1300415943.ap-shanghai.apigateway.myqcloud.com
    environment: release
    region:      ap-shanghai
    serviceId:   service-g1ihx7c7
    apis: 
      - 
        path:   /users
        method: POST
        apiId:  api-4dv8r7wg

  24s › restApi › done

```

#### 移除

通过以下命令移除部署的 API 网关：
```console
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing any previously deployed API. api-4dv8r7wg
  DEBUG ─ Removing any previously deployed service. service-g1ihx7c7

  13s › restApi › done

```

####  账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件

```console
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存。
```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
> - 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
> - 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
