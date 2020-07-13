## 操作场景
腾讯云 CDN 组件是 serverless-tencent 组件库中的基础组件之一。通过 CDN 组件，您可以快速方便的创建、配置和管理腾讯云的 CDN 产品。

## 前提条件

- 已安装 [Node.js](https://nodejs.org/en/)（Node.js 版本需不低于 8.6，建议使用 Node.js10.0 及以上版本）。
- 需要开通 [内容分发网络](https://console.cloud.tencent.com/cdn) 服务。

## 操作步骤

#### 安装

通过 npm 安装 Serverless：

```console
npm install -g serverless
```

如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版： 

```console
npm update -g serverless
```

####  配置

本地创建 `serverless.yml` 文件：
```shell
touch serverless.yml
```
在 `serverless.yml` 中进行如下配置：
```yml
# serverless.yml

component: cdn
name: cdnDemo
org: orgDemo
app: appDemo
stage: dev

inputs:
  area: overseas
  domain: mysite.com #域名
  origin:
    origins:
      - xxx.cos.ap-guangzhou.myqcloud.com  #源站，可以是域名或 IP
    originType: cos
    originPullProtocol: https
  serviceType: web
  forceRedirect:
    switch: on
    redirectType: https
    redirectStatusCode: 301
  https:
    switch: on
    http2: on
    certInfo:
      certId: 'abc'
      # certificate: 'xxx'
      # privateKey: 'xxx'
```

[查看详细配置文档 >>]( https://github.com/serverless-components/tencent-cdn/blob/master/docs/configure.md )

#### 部署

执行以下命令进行扫码授权部署：
```console
sls deploy
```

>?
>- 请确认您已经开通 [内容分发网络](https://console.cloud.tencent.com/cdn) 服务。
>- 微信扫码授权部署有过期时间，如果想要持久授权，请参考 [账号配置](#account)。

#### 移除

执行以下命令移除部署的 CDN 配置：
```console
sls remove
```

#### 账号配置（可选）
当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：
```shell
touch .env # 腾讯云的配置信息
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
