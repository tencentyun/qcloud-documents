# 全栈组件(Vue.js+Express.js)

用于通过多个 Serverless Components 部署 Serverless 全栈应用程序。可以帮助开发者更方便快捷的部署 Serverless 应用，比如利用后端API与前端Vue.js结合等场景。

此项目的完全基于腾讯云 Serverless 服务器，可大大缩减使用成本。 如果正在寻找一个低开销的便捷轻量的 Serverless 服务管理框架，这里将是最好的选择。

该 Template 包括:

* **serverless Express.js 后端** - 由腾讯云 Servelress Cloud Function（无服务云函数SCF） 和腾讯云 API Gateway 提供相关能力，支持express.js框架，帮助开发者架构自己的项目和路由。
* **serverless Vue.js 前端** - 由腾讯云 Cloud Object Storage（对象存储COS）提供相关存储能力.  通过后端API传递到前端，并使用 Vue.js 做相关渲染。

&nbsp;

1. [安装](#1-安装)
2. [创建](#2-创建)
3. [部署](#3-部署)
4. [使用](#4-使用)

&nbsp;


### 1. 安装

首先，通过如下命令安装 [Serverless Framework](https://www.github.com/serverless/serverless):

```console
$ npm i -g serverless
```

然后，我们可以新建一个本地文件夹，使用 `create --template-url` ，安装相关template。或者也可以将文件直接下载到本地：

```console
$ serverless create --template-url https://github.com/serverless/components/tree/master/templates/tencent-fullstack-application
```

### 2. 创建

使用`cd`命令，进入`tencent-fullstack-application` 文件夹，在其根目录创建 `.env` 文件

```console
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 APPID，SecretId 和 SecretKey 信息并保存

如果没有腾讯云账号，可以在此[注册新账号](https://cloud.tencent.com/register)。

如果已有腾讯云账号，可以在[API密钥管理](https://console.cloud.tencent.com/cam/capi)中获取`APPID`, `SecretId` 和`SecretKey`

```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
TENCENT_APP_ID=123
```

或者，可以在部署之前手动将它们设置为环境变量。

将 NPM 依赖项分别安装在  `dashboard` 和 `api` 两个文件目录：

```console
$ cd dashboard
$ npm i
```

```
$ cd api
$ npm i
```

完成后的目录结构，如下所示:

```
|- api
|- dashboard
|- serverless.yml      # 使用项目中的 yml 文件
|- .env      # 腾讯云 SecretId/Key/AppId
```

### 3. 部署

可以直接通过 `serverless` 命令来部署应用:

```console
$ serverless
```

当然，也可以使用 `--debug` 调试命令来查看所有环境部署的详细情况：

```console
$ serverless --debug
```

### 4. 使用

首次部署成功后，即可在本地运行服务，并与后端腾讯云服务进行通讯

```console
$ cd dashboard && npm run start
```

### 5. 注意

目前暂不支持淘宝等第三方npm源，报错`Component "@serverless/tencent-express" was not found on NPM nor could it be resolved locally.`请设置并使用npm官方源体验：

```console
$ npm config rm registry
$ npm set registry https://registry.npmjs.org/
```

