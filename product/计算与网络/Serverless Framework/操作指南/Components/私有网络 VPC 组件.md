# 腾讯云 VPC 组件

## 简介

腾讯云 VPC 组件，支持通过 `serverless.yml` 配置快速创建指定名称的私有网络和子网，并输出 VPCID 和 SubnetID，便于配置其他组件所需的网络信息。

## 快速开始

1. [安装](#1-安装)
2. [配置](#2-配置)
3. [部署](#3-部署)
4. [移除](#4-移除)
5. [账号配置（可选）](#5-账号配置（可选）)

### 1. 安装

通过 npm 全局安装 [serverless cli](https://github.com/serverless/serverless)

```shell
$ npm install -g serverless
```

### 2. 配置

在项目根目录创建 `serverless.yml` 文件，在其中进行如下配置

```shell
$ touch serverless.yml
```

```yml
# serverless.yml
MyVpc:
  component: '@serverless/tencent-vpc'
  inputs:
    region: ap-guangzhou
    zone: ap-guangzhou-2
    vpcName: serverless
    subnetName: serverless
```

- [更多配置](https://github.com/serverless-components/tencent-vpc/tree/master/docs/configure.md)

### 3. 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过 `微信` 扫描命令行中的二维码进行授权登陆和注册。

通过 `sls` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息

```bash
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Creating vpc serverless...
  DEBUG ─ Create vpc serverless success.
  DEBUG ─ Creating subnet serverless...
  DEBUG ─ Create subnet serverless success.

  MyVpc:
    region:     ap-guangzhou
    zone:       ap-guangzhou-2
    vpcName:    serverless
    subnetName: serverless
    subnetId:   subnet-kwtsloz4
    vpcId:      vpc-hqydtuy1

  5s › MyVpc › done
```

> 注意: `sls` 是 `serverless` 命令的简写。

### 4. 移除

通过以下命令移除部署的 Vpc

```bash
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Start removing subnet subnet-kwtsloz4
  DEBUG ─ Removed subnet subnet-kwtsloz4
  DEBUG ─ Start removing vpc vpc-hqydtuy1
  DEBUG ─ Removed vpc vpc-hqydtuy1

  7s › MyVpc › done
```

### 5. 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/秘钥信息，也可以本地创建 `.env` 文件

```bash
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存

如果没有腾讯云账号，可以在此 [注册新账号](https://cloud.tencent.com/register)。

如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 `SecretId` 和`SecretKey`.

```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```