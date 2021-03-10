## 操作场景

Layer 组件是 serverless-tencent 组件库中的基础组件之一。 您可以通过该组件快速且方便地创建、配置和管理腾讯云函数的层资源。 

## 前提条件

已安装 [Node.js](https://nodejs.org/en/)
>!2020年9月1日起，Serverless 组件不再支持 Node.js10.0 以下版本，请注意升级。

## 操作步骤

### 安装

通过 npm 安装 Serverless：

```console
npm install -g serverless
```

如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版： 

```console
npm update -g serverless
```

###  配置

本地创建 `serverless.yml` 文件，在其中进行如下配置：

```console
touch serverless.yml
```

```yml
# serverless.yml

component: layer
name: layerDemo
app: appDemo
stage: dev

inputs:
  region: ap-guangzhou
  name: layerDemo
  src: ./layer-folder
  runtimes:
    - Nodejs10.15

```
[查看详细配置文档 >>]( https://github.com/serverless-components/tencent-layer/blob/master/docs/configure.md )


### 部署

 执行以下命令进行扫码授权部署： 

```console
sls deploy
```

>?微信扫码授权部署有过期时间，如果想要持久授权，请参考 [账号配置](#account)。

### 移除

 执行以下命令移除部署的服务： 

```
sls remove
```

<span id="account"></span>
###  账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```console
touch .env # 腾讯云的配置信息
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
