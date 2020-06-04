## 操作场景
本文介绍如何通过 Serverless Framework 提供的云函数 SCF 组件快速创建与部署一个云函数项目。如需了解更多组件及其使用方法，可前往 [Components 概述](https://cloud.tencent.com/document/product/1154/39270)。
>?SCF CLI 命令行工具于2020年2月起已不再进行维护，建议您使用功能更丰富及便捷的 Serverless Framework CLI 命令行工具进行项目开发。
>


## 操作步骤
### 安装 Serverless Framework
在命令行中，执行以下命令，通过 npm 安装最新版本的 Serverless Framework。
```
npm install -g serverless
```

### 创建函数目录
1. 执行以下命令，创建并进入新目录。本文以 `tencent-scf` 为例。
```
mkdir tencent-scf && cd tencent-scf
```
2. 依次执行以下命令，快速创建一个云函数应用。
```
serverless create --template-url https://github.com/serverless-components/tencent-scf/tree/v2/example
```
```
cd example
```
成功创建后，目录结构如下所示：
```
|- src
|   └── index.py
└──  serverless.yml
```

### 部署函数
1. 在 `serverless.yml` 文件所在的目录中，执行以下命令，部署云函数。
```
serverless deploy
```
2. 使用**微信**扫描命令行中的二维码，进行腾讯云授权登录和注册。如需配置持久的环境变量或密钥信息，请参见 [账号配置](#accountConfiguration)。
函数部署完成后，您可在命令行的输出中查看对应云函数的网关触发器提供的 URL 地址，使用浏览器访问该地址即可查看函数的部署效果。
>?如需查看部署过程的更多信息，可执行 `sls deploy --debug` 命令查看部署过程中的实时日志信息。（`sls` 是 `serverless` 命令的缩写）。
>


### 配置部署
云函数组件支持“0”配置部署，即您可直接使用配置文件中的默认值进行部署。同时也支持您根据自身需求，修改可选配置来进一步开发需部署的项目。

以下是云函数组件配置文件 `serverless.yml` 的说明，详情请参见 [全量配置及配置说明](https://github.com/serverless-components/tencent-scf/blob/v2/doc/configure.md)。
```yml
# serverless.yml
component: scf # (必填) 引用 component 的名称，当前用到的是 tencent-scf 组件
name: scfdemo # (必填) 该组件创建的实例名称
org: test # (可选) 用于记录组织信息，默认值为您的腾讯云账户 appid
app: scfApp # (可选) 该 SCF 应用名称
stage: dev # (可选) 用于区分环境信息，默认值是 dev
inputs:
  name: scfFunctionName
  src: ./src
  runtime: Nodejs10.15 # 云函数的运行时环境。除 Nodejs10.15 外，可选值为：Python2.7、Python3.6、Nodejs6.10、Nodejs8.9、Nodejs12.16、PHP5、PHP7、Golang1、Java8。
  region: ap-guangzhou
  handler: index.main_handler
  events:
    - apigw:
        name: serverless_api
        parameters:
          protocols:
            - http
            - https
          serviceName:
          description: The service of Serverless Framework
          environment: release
          endpoints:
            - path: /index
              method: GET
```
当您更新配置文件的字段后，再次运行 `serverless deploy` 或者 `serverless`  命令即可更新配置到云端。

### 开发与调试
完成云函数的部署后，可通过组件提供的开发调试能力对该项目进行二次开发，从而开发一个生产应用。

#### 开发模式
在 `serverless.yml` 文件所在的目录下，执行以下命令，进入开发模式。
```
serverless dev
```
本地代码在修改或更新后，无需再次运行 `serverless deploy` 命令反复进行部署，在进入开发模式后，组件可对本地代码的改动进行检测和自动上传。
`serverless dev` 同时支持实时输出云端日志，每次部署完毕后访问项目，即可在命令行中实时输出调用日志，便于查看业务情况和排障。

#### 云端调试
组件支持 Node.js 应用的云端调试能力，在进入开发模式后，将会自动监听远端端口，并将函数的超时时间临时配置为900s。此时您可以通过访问 `chrome://inspect/#devices` 查找远端的调试路径，并直接对云端代码进行断点等调试。在调试结束后，需要再次部署更新代码并还原超时时间。详情请参考 [开发模式和云端调试](https://cloud.tencent.com/document/product/583/44775)。



### 查看部署状态

在 `serverless.yml` 文件所在的目录下，可执行以下命令，查看部署状态。
```
serverless info
```

### 移除应用
在 `serverless.yml` 文件所在的目录下，可执行以下命令，移除已部署的云函数应用。移除后该组件会对应删除云上部署时所创建的所有相关资源。
```
serverless remove
```
>?支持通过 `sls remove --debug` 命令查看移除过程中的实时日志信息。（`sls` 是 `serverless` 命令的缩写）。


## 相关操作
### 账号配置<span id="accountConfiguration"></span>
目前默认支持 CLI 扫描二维码登录，如需配置持久的环境变量/密钥信息，可通过以下步骤进行配置：
1. 执行以下命令，在本地创建 `.env` 文件。
```console
touch .env # 腾讯云的配置信息
```
2. 在 `.env` 文件中，按照以下格式配置腾讯云的 SecretId 和 SecretKey 信息并保存。
```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果您没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果您已有腾讯云账号，可前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取 SecretId 和 SecretKey。
