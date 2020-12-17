## 操作场景
PostgreSQL for Serverless（ServerlessDB）是一款基于 PostgreSQL 数据库实现的按需分配资源的数据库产品，其数据库将根据您的实际请求数来自动分配资源。PostgreSQL for Serverless 仅需创建实例，即可正常使用，您无需关心数据库实例规格，仅需要在数据库处于活动状态期间按照实际用量进行付费，不需要为数据库的闲时进行付费。详情参考 [ServerlessDB](https://cloud.tencent.com/document/product/409/42844) 文档。

通过 PostgreSQL ServerlessDB 组件，您可以快速方便地创建、配置和管理腾讯云的 PostgreSQL 实例。

特性介绍：

- **按需付费** - 按照请求的使用量进行收费，没有请求时无需付费。
- **"0"配置** - 默认配置将由 Serverless 完成。
- **极速部署** - 仅需几秒，创建或更新您的数据库。
- **便捷协作** - 通过云端数据库的状态信息和部署日志，方便的进行多人协作开发。

## 操作步骤
#### 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：

```shell
$ npm install -g serverless
```

#### 账号配置

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

#### 配置

创建并进入一个全新目录：
```
$ mkdir tencent-postgreSQL && cd tencent-postgreSQL
```

在新目录创建`serverless.yml`文件：

```shell
$ touch serverless.yml
```
在`serverless.yml`中进行如下配置：
```yml
# serverless.yml
component: postgresql #(必填) 引用 component 的名称，当前用到的是 postgresql 组件
name: serverlessDB # (必填) 该 postgresql 组件创建的实例名称
org: test # (可选) 用于记录组织信息，默认值为您的腾讯云账户 appid
app: serverlessDB # (可选) 该 sql 应用名称
stage: dev # (可选) 用于区分环境信息，默认值是 dev

inputs:
  region: ap-guangzhou  # 可选 ap-guangzhou, ap-shanghai, ap-beijing
  zone: ap-guangzhou-2  # 可选 ap-guangzhou-2, ap-shanghai-2, ap-beijing-3
  dBInstanceName: serverlessDB
  vpcConfig:
    vpcId: vpc-xxxxxxx
    subnetId: subnet-xxxxxx
  extranetAccess: false
```
PostgreSQL 组件支持0配置部署，您可以直接通过配置文件中的默认值进行部署。您依然可以修改更多可选配置来进一步开发该项目。

[查看详细配置文档 >>](https://github.com/serverless-components/tencent-postgresql/blob/master/docs/configure.md)

>!当前 PGSQL for Serverless 仅支持**北京三区**，**广州二区**，**上海二区**三个地域的创建和部署，因此在填写 yaml 中的地域可用区时需要注意填写为正确的地域和对应的 VPC 子网信息。

#### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息：
>?`sls`是`serverless`命令的简写。

```bash
$ sls deploy
```

#### 移除
通过以下命令移除部署的 DB 实例：

```bash
$ sls remove
```

## 最佳实践

部署 PG Serverless DB 之后，您可以参考 [部署支持数据库操作的全栈网站](https://cloud.tencent.com/document/product/1154/43009) 使用该 DB 实例。

## 更多组件
您可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。

