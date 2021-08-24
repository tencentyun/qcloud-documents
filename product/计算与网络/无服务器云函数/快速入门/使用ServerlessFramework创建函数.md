## 操作场景
本文介绍如何通过 Serverless Framework 提供的云函数 SCF 组件快速创建与部署一个云函数项目。如需了解更多组件及其使用方法，可前往 [Components 概述](https://cloud.tencent.com/document/product/1154/39270)。
>?SCF CLI 命令行工具于2020年2月起已不再进行维护，建议您使用功能更丰富及便捷的 Serverless Framework CLI 命令行工具进行项目开发。
>

## 前提条件
- 已安装 Serverless Framework，详情请参见 [安装 Serverless Framework](https://cloud.tencent.com/document/product/583/44753)。
- 账号开通 Serverless 相关权限，详情请参见 [账号和权限配置](https://cloud.tencent.com/document/product/583/44786)。

## 操作步骤

### 创建函数
执行以下命令，快速创建一个开发语言为 Node.js 的函数示例。 
```
sls init scf-demo
```
>?命令中的 scf-demo 默认为 nodejs 模版，您也可以替换为其它语言的函数模版：`scf-golang`，`scf-php`，`scf-python`。

### 部署函数
在 `scf-demo` 目录下执行以下命令，进行函数部署。
```
sls deploy
```
将会弹出二维码，请直接扫码授权开始部署。部署成功后，会自动创建云函数资源。
>?如果鉴权失败，请参考 [权限配置](https://cloud.tencent.com/document/product/1154/43006) 进行授权。

### 查看函数信息
执行以下命令，查看已部署云函数资源信息。
```
sls info
```

### 移除函数
执行以下命令，移除已经部署云函数资源。
```
sls remove
```

## 相关功能
- 关于 Serverless Framework CLI 工具更多操作云函数的相关功能，请参见 [Serverless Framework CLI](https://cloud.tencent.com/document/product/583/44751) 。
- Serverless Web IDE 工具是基于浏览器的集成式开发环境，提供接近原生 IDE 的云端开发体验。更多使用 Web IDE 操作云函数的相关功能，请参见 [Serverless Web IDE](https://cloud.tencent.com/document/product/583/51345)。
- Tencentserverless 云函数 SDK 集成了云函数业务流接口，简化了云函数的调用方法。更多使用云函数 SDK 操作云函数的相关功能，请参见 [Python SDK](https://cloud.tencent.com/document/product/583/37102) 和 [Node.js SDK](https://cloud.tencent.com/document/product/583/37316)。
