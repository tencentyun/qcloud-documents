## 操作场景
**腾讯云 Express 组件**通过使用 [Tencent Serverless Framework](https://github.com/serverless/components/tree/cloud)，基于云上 Serverless 服务（如网关、云函数等），实现“0”配置，便捷开发，极速部署您的 Express 应用，Express 组件支持丰富的配置扩展，提供了目前最易用、低成本并且弹性伸缩的 Experss 项目开发/托管能力。

Express.js 特性介绍：
- **按需付费**：按照请求的使用量进行收费，没有请求时无需付费。
- **"0"配置**：只需要关心项目代码，之后部署即可，Serverless Framework 会搞定所有配置。
- **极速部署**：仅需几秒，部署您的整个 express 应用。
- **实时日志**：通过实时日志的输出查看业务状态，便于直接在云端开发应用。
- **云端调试**：针对 Node.js 框架支持一键云端调试能力，屏蔽本地环境的差异。
- **便捷协作**：通过云端的状态信息和部署日志，方便的进行多人协作开发。
- **自定义域名**：支持配置自定义域名及 HTTPS 访问。

## 前提条件
已安装 Node.js（参考 [Node.js 安装指南](https://nodejs.org/zh-cn/download/)）。

## 操作步骤
#### 1. 安装

通过 npm 安装最新版本的 Serverless Framework：
```
$ npm install -g serverless
```

#### 2. 创建

创建并进入一个全新目录：
```
$ mkdir tencent-express && cd tencent-express
```

通过如下命令和模板链接，快速创建一个 Express 应用：
```
$ serverless create --template-url https://github.com/serverless-components/tencent-express/tree/v2/example
$ cd example
```

执行如下命令，安装 Express 应用的对应依赖：
```
$ cd src && npm install
```
安装完毕后，目录结构如下所示：
```
|- src
|   ├── sls.js
|   ├── node_modules
|   └── package.json
└──  serverless.yml
```

#### 3. 部署

在`serverless.yml`文件下的目录中运行`sls deploy`进行 Express 项目的部署。第一次部署可能耗时相对较久，但后续的二次部署会在几秒钟之内完成。部署完毕后，您可以在命令行的输出中查看到您的 Express 应用的 URL 地址，点击地址即可访问您的 Express 项目。
```
$ sls deploy

Please scan QR code login from wechat. 
Wait login...
Login successful for TencentCloud. 

serverless ⚡ framework
Action: "deploy" - Stage: "dev" - App: "appDemo" - Instance: "expressDemo"

region: ap-guangzhou
apigw: 
  serviceId:   service-xxxxxxxx
  subDomain:   service-xxxxxxxx-1250000000.gz.apigw.tencentcs.com
  environment: release
  url:         https://service-xxxxxxxx-1250000000.gz.apigw.tencentcs.com/release/
scf: 
  functionName: expressDemo
  runtime:      Nodejs10.15
  namespace:    default

23s › expressDemo › Success
```
>!
- 如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，请先通过**微信**扫描命令行中的二维码进行授权登录和注册。
- 如果出现了`internal server error`的报错，请检查是否在创建模板后没有运行`npm install`。
- 如果希望查看更多部署过程的信息，可以通过`sls deploy --debug`命令查看部署过程中的实时日志信息（`sls`是`serverless`命令的缩写）。


#### 4. 配置

Express 组件支持“0”配置部署，也就是可以直接通过配置文件中的默认值进行部署。但您依然可以修改更多可选配置来进一步开发该 Express 项目。

以下是 Express 组件的`serverless.yml`完整配置说明：
```yml
# serverless.yml

component: express # (必填) 引用 component 的名称，当前用到的是 express-tencent 组件
name: express-api # (必填) 该 express 组件创建的实例名称
org: test # (可选) 用于记录组织信息，默认值为您的腾讯云账户 appid
app: expressApp # (可选) 该 express 应用名称
stage: dev # (可选) 用于区分环境信息，默认值是 dev

inputs:
  region: ap-guangzhou
  functionName: express-api
  serviceName: mytest
  runtime: Nodejs8.9
  serviceId: service-np1uloxw
  src: ./src
  functionConf:
    timeout: 10
    memorySize: 128
    environment:
      variables:
        TEST: vale
  apigatewayConf:
    customDomains:
      - domain: abc.com
        certificateId: abcdefg
        isDefaultMapping: 'FALSE'
        pathMappingSet:
          - path: /
            environment: release
        protocols:
          - http
          - https
```

查看 [全量配置及配置说明 >>](https://github.com/serverless-components/tencent-express/blob/v2/docs/configure.md)

当您根据该配置文件更新配置字段后，再次运行`serverless deploy`或者`serverless`就可以更新配置到云端。

#### 5. 开发调试

部署了 Express.js 应用后，可以通过开发调试能力对该项目进行二次开发，从而开发一个生产应用。在本地修改和更新代码后，不需要每次都运行`serverless deploy`命令来反复部署。您可以直接通过`serverless dev`命令对本地代码的改动进行检测和自动上传。

可以通过在`serverless.yml`文件所在的目录下运行`serverless dev`命令开启开发调试能力。

`serverless dev`同时支持实时输出云端日志，每次部署完毕后，对项目进行访问，即可在命令行中实时输出调用日志，便于查看业务情况和排障。

除了实时日志输出之外，针对 Node.js 应用，当前也支持云端调试能力。在开启`serverless dev`命令之后，将会自动监听远端端口，并将函数的超时时间临时配置为900s。此时您可以通过访问 chrome://inspect/#devices 查找远端的调试路径，并直接对云端代码进行断点等调试。在调试模式结束后，需要再次部署从而将代码更新并将超时时间设置为原来的值。详情请参考 [开发模式和云端调试](https://cloud.tencent.com/document/product/1154/43220)。

#### 6. 查看状态

在`serverless.yml`文件所在的目录下，通过如下命令查看部署状态：

```
$ serverless info
```

#### 7. 移除

在`serverless.yml`文件所在的目录下，通过以下命令移除部署的 Express 服务。移除后该组件会对应删除云上部署时所创建的所有相关资源。
```
$ serverless remove
```

和部署类似，支持通过`sls remove --debug`命令查看移除过程中的实时日志信息（`sls`是 `serverless` 命令的缩写）。

## 架构说明

Express 组件将在腾讯云账户中使用到如下 Serverless 服务：

- **API 网关**：API 网关将会接收外部请求并且转发到 SCF 云函数中。
- **SCF 云函数**：云函数将承载 Express.js 应用。
- **CAM 访问控制**：该组件会创建默认 CAM 角色用于授权访问关联资源。
- **COS 对象存储**：为确保上传速度和质量，云函数压缩并上传代码时，会默认将代码包存储在特定命名的 COS 桶中。
- **SSL 证书服务**：如果您在 yaml 文件中配置了 `domain` 字段，需要做自定义域名绑定并开启 HTTPS 时，也会用到证书管理服务和域名服务。Serverless Framework 会根据已经备案的域名自动申请并配置 SSL 证书。

## 账号配置

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
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
