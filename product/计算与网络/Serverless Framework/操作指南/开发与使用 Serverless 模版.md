## 操作场景
Serverless Framework 支持您构建自己的 Serverless 组件或者项目模版， 并且将其发布在 Serverless Registry 应用中心中，提供给团队和他人使用。本篇文档将为您具体介绍，如何通过 Registry 开发您自己的模版并进行复用。

## 前提条件
已 [安装 Serverless Framework](https://cloud.tencent.com/document/product/1154/42990)，并保证您的 Serverless Framework 不低于以下版本：

```shell
$ serverless –v
Framework Core: 1.74.1 (standalone)
Plugin: 3.6.14
SDK: 2.3.1
Components: 2.31.6
```

## 操作步骤
### 使用 Regsitry 进行模版项目初始化

#### 1. 查看可用组件或模版
您可以使用以下两种方式查看可供使用的组件或模板：

1. 访问 [Serverless 应用中心](https://registry.serverless.com) 页面。
2. 使用 `sls registry` 命令列出所有推荐的组件或者项目模板：

```
$ sls registry

serverless ⚡ registry

Featured Components:

  apigateway - https://github.com/serverless-components/tencent-apigateway
  cdn - https://github.com/serverless-components/tencent-cdn
  cos - https://github.com/serverless-components/tencent-cos
  django - https://github.com/serverless-components/tencent-django/
  ...

Featured Templates:

  fullstack - Deploy a full stack application.
  fullstack-nosql - Deploy a nosql full stack application.
  ocr-app - Deploy a serverless OCR application.

Serverless › Find more here: https://registry.serverless.com
```

#### 2. 从模板初始化项目
确定了所要使用的项目模板后，您就可以使用内置的 init 命令初始化您的项目。init 命令将会自动从应用中心下载您所选择的模板，并为您创建好项目文件夹，操作如下：

```
$ sls init fullstack # 使用 fullstack 项目模板创建项目
$ cd  fullstack # 进入到项目文件夹
```

#### 3. 快速部署项目
初始化完成后，您可以在本地项目文件夹内完成您的项目开发，再通过 sls 指令完成云端快速部署：

```
$ sls deploy --all # 部署整个fullstack项目
```

### 通过 Registry 开发自己的模版
要将您基于 Serverless Component 部署的项目作为模板发布非常简单，您不需要对项目进行任何改造，只需要添加一个serverless.yml文件（或者修改已有的 serverless.yml 文件），在其中添加一些需要告诉注册中心的模板元信息即可。详细说明如下：

```text
# serverless.yml
name: fullstack # 项目模板的名字
displayName: fullstack全栈应用 #项目模板展示在控制台的名称（中文）
author: Tencent Cloud, Inc. # 作者的名字
org: Tencent Cloud, Inc. # 组织名称，可选
type: template #项目类型，可填 template 或 component，此处为模版
description: Deploy a full stack application. # 描述您的项目模板
description-i18n:
  zh-cn: 快速部署一个全栈应用 # 中文描述
keywords: tencent, serverless, express, website, fullstack # 关键字
repo: https://github.com/serverless-components/tencent-fullstack # 源代码
readme: https://github.com/serverless-components/tencent-fullstack/tree/master/README.md # 详细的说明文件
license: MIT # 版权声明
src: # 描述项目中的哪些文件需要作为模板发布
  src: ./ # 指定具体的相对目录，此目录下的文件将作为模板发布
  exclude: #描述在指定的目录内哪些文件应该被排除
    # 通常希望排除
    # 1. 包含 secrets 的文件
    # 2. .git git 源代码管理的相关文件
    # 3. node_modules 等第三方依赖文件
    - .env
    - '**/node_modules'
    - '**/package-lock.json'
```

serverless.yml 文件配置完成后，便可以使用发布命令 `sls registry publish` 将此项目作为模板发布到应用中心，其他人可通过您的模版名称进行项目复用。
