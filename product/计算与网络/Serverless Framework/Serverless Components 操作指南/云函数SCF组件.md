# 腾讯云云函数SCF组件

## 简介
该组件是serverless-tencent组件库中的基础组件之一。通过云函数SCF组件，可以快速，方便的创建，配置和管理腾讯云的SCF云函数。

## 快速开始
&nbsp;

通过SCF组件，对一个云函数进行完整的创建，配置，部署和删除等操作。支持命令如下：

1. [安装](#1-安装)
2. [创建](#2-创建)
3. [配置](#3-配置)
4. [部署](#4-部署)
5. [移除](#5-移除)

&nbsp;

### 1. 安装

通过npm安装serverless

```console
$ npm install -g serverless
```

### 2. 创建

```
$ mkdir my-function
$ cd my-function
```
目录内容如下:

```
|- code
  |- index.js
|- serverless.yml
|- .env      # your Tencent SecretId/Key/AppId
```

在 `.env` 文件中配置腾讯云的APPID，SecretId和SecretKey信息并保存

如果没有腾讯云账号，可以在此[注册新账号](https://cloud.tencent.com/register)。

如果已有腾讯云账号，可以在[API密钥管理](https://console.cloud.tencent.com/cam/capi)中获取`APPID`, `SecretId` 和`SecretKey`.

```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```

对于该例子可以使用一下Demo，作为index.js：

```javascript
'use strict';
exports.main_handler = async (event, context, callback) => {
    console.log("%j", event);
    return "hello world"
};

```


### 3. 配置

在serverless.yml中进行如下配置

```yml
# serverless.yml
myFunction1:
  component: "@serverless/tencent-scf"
  inputs:
    name: myFunction1
    codeUri: ./code       # 代码目录
    handler: index.main_handler
    runtime: Nodejs8.9
    region: ap-guangzhou
    description: My Serverless Function
    memorySize: 128
    timeout: 20
    # 打包zip时希望忽略的文件或者目录配置（可选）
    exclude:
      - .gitignore
      - .git/**
      - node_modules/**
      - .serverless
      - .env
    include:
          - /Users/dfounderliu/Desktop/temp/.serverless/myFunction1.zip
    environment:
      variables:
        TEST: vale
    vpcConfig:
      subnetId: ''
      vpcId: ''

myFunction2:
  component: "@serverless/tencent-scf"
  inputs:
    name: myFunction2
    codeUri: ./code

```

* [点击此处查看配置文档](https://github.com/serverless-tencent/tencent-scf/blob/master/docs/configure.md)


### 4. 部署

通过如下命令进行部署，并查看部署过程中的信息
```console
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Starting Website Removal.
  DEBUG ─ Removing Website bucket.
  DEBUG ─ Removing files from the "my-bucket-1300415943" bucket.
  DEBUG ─ Removing "my-bucket-1300415943" bucket from the "ap-guangzhou" region.
  DEBUG ─ "my-bucket-1300415943" bucket was successfully removed from the "ap-guangzhou" region.
  DEBUG ─ Finished Website Removal.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Compressing function myFunction file to /Users/dfounderliu/Desktop/temp/code/.serverless/myFunction.zip.
  DEBUG ─ Compressed function myFunction file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-guangzhou-code]. sls-cloudfunction-default-myFunction-1572519895.zip
  DEBUG ─ Uploaded package successful /Users/dfounderliu/Desktop/temp/code/.serverless/myFunction.zip
  DEBUG ─ Creating function myFunction
  DEBUG ─ Created function myFunction successful

  myFunction: 
    Name:        myFunction
    Runtime:     Nodejs8.9
    Handler:     index.main_handler
    MemorySize:  128
    Timeout:     3
    Region:      ap-guangzhou
    Role:        QCS_SCFExcuteRole
    Description: This is a template function
    UsingCos:    true

  6s › myFunction › done

```

### 5. 移除

```console
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removed function myFunction successful

  1s › myFunction › done

```

### 还支持哪些组件？

可以在 [Serverless Components](https://github.com/serverless/components) repo 中查询更多组件的信息。
