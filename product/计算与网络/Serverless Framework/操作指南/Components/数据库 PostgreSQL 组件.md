## 操作场景
PostgreSQL for Serverless（ServerlessDB）是一款基于 PostgreSQL 数据库实现的按需分配资源的数据库产品，其数据库将根据您的实际请求数来自动分配资源。PostgreSQL for Serverless 仅需创建实例，即可正常使用，您无需关心数据库实例规格，仅需要在数据库处于活动状态期间按照实际用量进行付费，不需要为数据库的闲时进行付费。详情参考 [ServerlessDB](https://cloud.tencent.com/document/product/409/42844) 文档。

通过 PostgreSQL ServerlessDB 组件，您可以快速方便的创建、配置和管理腾讯云的 PostgreSQL 实例。

## 操作步骤
### 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：

```shell
$ npm install -g serverless
```

### 配置

本地创建`.env`文件：

```bash
$ touch .env # 腾讯云的配置信息
```

在`.env`文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：

```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。

在项目根目录创建`serverless.yml`文件：

```shell
$ touch serverless.yml
```
在`serverless.yml`中进行如下配置：
```yml
# serverless.yml
MyPostgreSQL:
  component: '@serverless/tencent-postgresql'
  inputs:
    region: ap-guangzhou
    zone: ap-guangzhou-3
    dBInstanceName: serverlessDb
    dBVersion: 10.4
    dBCharset: UTF8
    vpcConfig:
      vpcId: 123
      subnetId: 123
    extranetAccess: false
```
[查看详细配置文档 >>](https://github.com/serverless-components/tencent-postgresql/tree/master/docs/configure.md)

### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息：
>?`sls`是`serverless`命令的简写。

```bash
$ sls --debug
```

### 移除
通过以下命令移除部署的 DB 实例：

```bash
$ sls remove --debug
```

### 更多组件
您可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。
