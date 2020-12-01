## 操作场景
**腾讯云 Django 组件**通过使用 [Tencent Serverless Framework](https://github.com/serverless/components/tree/cloud)，基于云上 Serverless 服务（如对象存储等），实现“0”配置，便捷开发，极速部署您的 Django 网页应用。

Django 特性介绍：
- **"0"配置**：只需要关心项目代码，之后部署即可，Serverless Framework 会搞定所有配置。
- **按需付费**：按照请求的使用量进行收费，没有请求时无需付费。
- **极速部署**：仅需几秒，部署您的网页应用。
- **便捷协作**：支持开发模式与云端调试，方便多人协作。
- **拓展广泛** ：支持 Restful API 服务的部署。


## 操作步骤
### 1. 安装

通过 npm 安装最新版本的 Serverless Framework：
```
$ npm install -g serverless
```

### 2. 创建

创建并进入一个全新目录：
```
$ mkdir myDjangoDemo && cd myDjangoDemo
```

通过如下命令和模板链接，快速创建一个静态网站托管应用：
```
$ serverless create --template-url https://github.com/serverless-tencent/tencent-django/tree/master/example
$ cd example
```

### 3. 配置
在本地创建`serverless.yml`文件：
```shell
$ touch serverless.yml
```

在`serverless.yml`中进行如下配置：
```yml
component: django # (required) name of the component. In that case, it's express.
name: mydjangoDemo # (required) name of your express component instance.
org: mydjangoDemo # (optional) serverless dashboard org. default is the first org you created during signup.
app: mydjangoDemo # (optional) serverless dashboard app. default is the same as the name property.
stage: dev # (optional) serverless dashboard stage. default is dev.

inputs:
  region: ap-guangzhou
  functionName: DjangoFunction 
  djangoProjectName: mydjangocomponent #您的项目文件夹名称
  src:
    bucket: 输入您上传项目的存储桶名称
    src: ./src
  functionConf:
    timeout: 10
    memorySize: 256
    environment:
      variables:
        TEST: vale
    vpcConfig:
      subnetId: ''
      vpcId: ''
  apigatewayConf:
    protocols:
      - https
    environment: release

```
>!
如果您自己创建项目，请将 Python 所需要的依赖安装到项目目录，例如本实例需要`Django`，所以可以通过`pip`进行安装：
```
pip install Django -t ./
```

### 4. 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息

```shell
$ sls deploy --debug
```

### 5. 移除
通过以下命令移除部署的服务：
```shell
$ sls remove --debug
```

### 账号配置（可选）
当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建`.env`文件：
```shell
$ touch .env # 腾讯云的配置信息
```

在`.env`文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：
```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
