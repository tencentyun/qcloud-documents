## 操作场景
云函数 SCF 组件是 serverless-tencent 组件库中的基础组件之一。通过云函数 SCF 组件，可以快速切方便地创建、配置和管理腾讯云的云函数 SCF。

## 操作步骤

通过 SCF 组件，您可以对一个云函数进行完整的创建、配置、部署和删除等操作。支持命令如下：

#### 安装

通过 npm 安装 Serverless：
```console
$ npm install -g serverless
```

#### 创建
```
$ mkdir my-function
$ cd my-function
```
目录内容如下：

```
|- code
  |- index.js
|- serverless.yml
```
 
对于该例子可以使用以下 Demo，作为 index.js：
```javascript
'use strict';
exports.main_handler = async (event, context, callback) => {
    console.log("%j", event);
    return "hello world"
};

```

#### 配置

本地创建`serverless.yml`文件：

```console
$ touch serverless.yml
```
在`serverless.yml`中进行如下配置：
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
    # 打包 zip 时希望忽略的文件或者目录配置（可选）
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
>?您可以通过 [详细配置文档](https://github.com/serverless-tencent/serverless-tencent-scf/blob/master/docs/zh/yaml.md)，查看`serverless.yml`中所有可用属性的属性列表。


#### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息：

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

#### 移除

```console
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removed function myFunction successful

  1s › myFunction › done

```

####  账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```console
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存。
```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
> - 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
> - 如果已有腾讯云账号，可以在 [API 密钥管理
](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
