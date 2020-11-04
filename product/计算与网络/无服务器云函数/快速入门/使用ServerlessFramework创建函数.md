## 操作场景
本文介绍如何通过 Serverless Framework 提供的云函数 SCF 组件快速创建与部署一个云函数项目。如需了解更多组件及其使用方法，可前往 [Components 概述](https://cloud.tencent.com/document/product/1154/39270)。
>?SCF CLI 命令行工具于2020年2月起已不再进行维护，建议您使用功能更丰富及便捷的 Serverless Framework CLI 命令行工具进行项目开发。
>

### 前提条件

- 已安装 Serverless Framework（参考 [安装 Serverless Framework](https://cloud.tencent.com/document/product/583/44753)）
- 账号开通 Serverless 相关权限（参考 [账号和权限配置](https://cloud.tencent.com/document/product/583/44786)）


### 操作步骤

#### 创建

 使用 `sls init` 命令创建。快速创建一个 nodejs 的 SCF 示例：

```
sls init scf-demo
```

>?命令中的 `scf-demo` 可以更换成其他语言模板。目前 SCF 组件支持的模板有：go1-helloworld 、nodejs1015-helloworld、php72-helloworld、python36-helloworld。


#### 部署

执行以下命令，将会弹出二维码，直接扫码授权进行部署：

```
sls deploy
```

>?如果鉴权失败，请参考 [权限配置](https://cloud.tencent.com/document/product/1154/43006) 进行授权。

部署成功后，会自动创建云函数资源。

#### 查看

执行以下命令，查看您部署云函数资源：

```
sls info
```

#### 移除

执行以下命令，移除您已经部署云函数资源：

```
sls remove
```

>?Serverless Framework CLI 工具更多操作云函数能力，请参考[Serverless Framework CLI](https://cloud.tencent.com/document/product/583/45352) 。