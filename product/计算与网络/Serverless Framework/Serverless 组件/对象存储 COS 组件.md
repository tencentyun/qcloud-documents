## 操作场景

对象存储 COS 组件是 serverless-tencent 组件库中的基础组件之一。通过对象存储 COS 组件，可以快速且方便的创建、配置和管理腾讯云的 COS 存储桶。

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

org: orgDemo
app: appDemo
stage: dev
component: cos
name: cosDemo

inputs:
  bucket: my-bucket
  region: ap-guangzhou

```
[查看详细配置文档 >>]( https://github.com/serverless-components/tencent-cos/blob/master/docs/configure.md )


### 部署

执行以下命令进行部署，返回信息如下： 

```console
[root@iZh8dhuyhmexn3Z demo]# sls deploy

serverless ⚡ framework
Action: "deploy" - Stage: "dev" - App: "appDemo" - Instance: "cosDemo"

region: ap-guangzhou
bucket: my-bucket-xxxxxxx
url:    http://my-bucket-xxxxxxx.cos.ap-guangzhou.myqcloud.com

Full details: https://serverless.cloud.tencent.com/instances/appDemo%3Adev%3AcosDemo

3s › cosDemo › Success

```

>?微信扫码授权部署有过期时间，如果想要持久授权，请参考 [账号配置](#account)。

### 移除

执行`sls remove`命令移除部署的存储桶，返回信息如下：

```
[root@iZh8dhuyhmexn3Z demo]# sls remove

serverless ⚡ framework
Action: "remove" - Stage: "dev" - App: "appDemo" - Instance: "cosDemo"

3s › cosDemo › Success
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
