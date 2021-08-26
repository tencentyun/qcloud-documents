## Tencentcloud-Serverless-Nodejs SDK 简介

Tencentcloud-Serverless-Nodejs 是腾讯云云函数 SDK，集成云函数业务流接口，简化云函数的调用方法。在使用该 SDK 的情况下，用户可以方便的从本地、云服务器（CVM）、容器、以及云端函数里快速调用某一个云函数，无需再进行公有云 API 的接口封装。

## 功能特性
Tencentcloud-Serverless-Nodejs SDK 的功能特性可分为以下几点：

* 高性能，低时延的进行函数调用。
* 填写必须的参数后，即可快速进行函数间的调用（SDK 会默认获取环境变量中的参数，例如 region，secretId 等）。
* 支持内网域名的访问。
* 支持 keepalive 能力。
* 支持跨地域函数调用。


## 快速开始
### 开发准备
- 开发环境
已安装 Node.js 8.9 及以上版本。
- 运行环境
已安装 tencentcloud-serverless-nodejs SDK，支持 Windows、Linux 和 Mac 操作系统。
- 建议使用 [Serverless Framework CLI](https://cloud.tencent.com/document/product/583/37510)，可快速部署本地云函数。

### 安装 tencentcloud-serverless-nodejs SDK
#### 通过 npm 安装（推荐）
1. 根据实际需求，选择目录路径，并在该路径下创建新的目录。
例如，创建一个名称为 `testNodejsSDK` 的项目目录，项目路径为  `/Users/xxx/Desktop/testNodejsSDK`。
2. 进入 `testNodejsSDK` 目录，并依次执行以下命令，安装 tencentcloud-serverless-nodejs SDK。
```shell
npm init -y
npm install tencentcloud-serverless-nodejs
```
安装完成后，在 `testNodejsSDK` 目录下可以查看到 `node_modules`，`package.json` 和 `package-lock.json`。

#### 通过源码包安装
前往 [Github 代码托管地址](https://github.com/TencentCloud/tencentcloud-serverless-nodejs) 下载最新源码包，解压源码包后进行安装。

#### 使用云函数在线依赖安装
使用 [云函数在线依赖安装](https://cloud.tencent.com/document/product/583/37920)，在 `package.json` 中执行以下命令并进行安装。
```js
{
    "dependencies": {
    "tencentcloud-serverless-nodejs":"*"
  }
}
```


### 云端函数互调
#### 示例
>!
> - 不同地域下的函数互调，须指定地域，命名规则参见 [地域列表](https://cloud.tencent.com/document/api/583/17238#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
> - 如果不指定地域，默认为同地域下函数互调。
> - 命名空间不指定，默认为 default。
> - 需要打开调用方函数外网访问权限。
> - 如果没有手动传入 secretId 和 secretKey 等参数，函数需绑定有 SCF Invoke 权限（或者包含 SCF Invoke，例如 SCF FullAccess）的角色，可参考 [创建函数运行角色](https://cloud.tencent.com/document/product/583/41755)。


1. [](id:Step1)创建一个地域为**北京**，名称为 “FuncInvoked”，并用于**被调用**的 Node.js 云函数。该云函数内容如下：
```js
'use strict';
exports.main_handler = async (event, context, callback) => {
      console.log("\n Hello World from the function being invoked\n")
      console.log(event)
      console.log(event["non-exist"])
      return event
};
```
2. 在 `testNodejsSDK` 目录下新建文件 `index.js`，并输入如下示例代码，创建**发起调用**的 Node.js 云函数。
<dx-codeblock>
:::  js
const { SDK, LogType }  = require('tencentcloud-serverless-nodejs')
exports.main_handler = async (event, context) => {
  context.callbackWaitsForEmptyEventLoop = false
  const sdk = new SDK({
    region:'ap-beijing'
  }) //如果在云函数中运行并且绑定了有SCF调用资格的运行角色，会默认取环境变量中的鉴权信息
  const res = await sdk.invoke({
    functionName: 'FuncInvoked',
    logType: LogType.Tail,
    data: {
      name: 'test',
      role: 'test_role'
    }
  })
  console.log(res)
  // return res
}
:::
</dx-codeblock>
 
 其中主要参数获取途径如下：
 - **region**：**被调用**云函数所在地域，本文以 [步骤1](#Step1) 中的北京地域为例。
 - **functionName**：**被调用**云函数名称，本文以 [步骤1](#Step1) 中已创建的 `FuncInvoked` 函数为例。
 - **qualifier**：**被调用**云函数版本，如未指定则默认使用 `$LATEST`。详情请参见 [查看版本](https://cloud.tencent.com/document/product/583/31211)。
 - **namespace**：**被调用**云函数所在命名空间， 如未指定则默认 `default`。详情请参见 [命名空间管理](https://cloud.tencent.com/document/product/583/35913)。
 - **data**：传递给**被调用**云函数的数据，被调用的云函数可以从 event 入参中读取此数据。
3. 创建一个地域为**成都**，名称为 “NodejsInvokeTest”，并用于**调用**的 Node.js 云函数。该云函数主要设置信息如下：
 - 执行方法：选择**index.main_handler**。
 - 代码提交方式：选择**本地上传 zip 包**。
    将 `testNodejsSDK` 目录下的所有文件压缩为 zip 格式，并上传到云端。
4. 
在 [云函数控制台](https://console.cloud.tencent.com/scf/list) 中的函数详情页面，通过进入函数代码子页面，单击**运行**，测试运行函数。输出结果如下：
```shell
"Already invoked a function!"
```




### 本地调用云端函数

#### 示例

1. 创建一个地域为**北京**，名称为 “FuncInvoked”，并且用于**被调用**的 Node.js 云函数。该云函数内容如下：
```js
'use strict';
exports.main_handler = async (event, context, callback) => {
      console.log("\n Hello World from the function being invoked\n")
      console.log(event)
      console.log(event["non-exist"])
      return event
};
```
2. 在 `testNodejsSDK` 目录下新建文件 `index.js`，作为**发起调用**的 Node.js 云函数，并输入如下示例代码：
<dx-codeblock>
:::  js
const { SDK, LogType }  = require('tencentcloud-serverless-nodejs')
exports.main_handler = async (event, context) => {
  context.callbackWaitsForEmptyEventLoop = false
  const sdk = new SDK({
    region:'ap-beijing',
    secretId: 'AKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxj',
    secretKey: 'WtxxxxxxxxxxxxxxxxxxxxxxxxxxxxqL'
  }) //如果在云函数中运行并且绑定了有SCF调用资格的运行角色，会默认取环境变量中的鉴权信息
  const res = await sdk.invoke({
    functionName: 'FuncInvoked',
    logType: LogType.Tail,
    data: {
      name: 'test',
      role: 'test_role'
    }
  })
  console.log(res)
  // return res
}
:::
</dx-codeblock>
<dx-alert infotype="notice" title="">
secretId 及 secretKey：指云 API 的密钥 ID 和密钥 Key。您可以通过登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，选择**访问密钥** > **API 密钥管理**，获取相关密钥或创建相关密钥。
</dx-alert>
3. 进入 index.js 所在文件目录，执行以下命令，查看结果。
 - Linux 及 Mac 操作系统，执行以下命令：
```shell
export NODE_ENV=development && node index.js
```
 - Windows 操作系统执行以下命令：
```shell
set NODE_ENV=development && node index.js
```
 输出结果如下：
```shell
prepare to invoke a function!
{"key":"value"}
Already invoked a function!
```







## 接口列表
### API Reference
- [Init](#Init)
- [Invoke](#Invoke)

[](id:Init)
#### Init
在使用 SDK 前，建议执行 `npm init` 命令进行初始化 SDK。
>?
>- 初始化命令可传入 `region`，`secretId`，`secretKey`参数。
>- 完成初始化后，调用 API 接口时可复用初始化的配置。


**参数信息：**

| 参数名    | 是否必填 |  类型  |                                       描述 |
| :-------- | :------: | :----: | ----------------------------------------- |
| region    |    否    | `String` |                                       地域 |
| secretId  |    否    | `String` |  默认会取 process.env.TENCENTCLOUD_SECRETID  |
| secretKey |    否    | `String` | 默认会取 process.env.TENCENTCLOUD_SECRETKEY |
| token |    否    | `String` | 默认会取 process.env.TENCENTCLOUD_SESSIONTOKEN |


[](id:Invoke)
#### Invoke
调用函数，目前支持同步调用。

**参数信息：**

| 参数名       | 是否必填 |  类型  |                    描述 |
| :----------- | :------: | :----: | ----------------------|
| functionName |    是    | `String` |                函数名称 |
| qualifier    |    否    | `String` | 函数版本，默认为 $LATEST |
| data         |    否    | `String` |            函数运行入参 |
| namespace    |    否    | `String` | 命名空间，默认为 default |
| region    |    否    | `String` |                                       地域 |
| secretId  |    否    | `String` |  默认会取 process.env.TENCENTCLOUD_SECRETID |
| secretKey |    否    | `String` | 默认会取 process.env.TENCENTCLOUD_SECRETKEY |
| token |    否    | `String` | 默认会取 process.env.TENCENTCLOUD_SESSIONTOKEN |


