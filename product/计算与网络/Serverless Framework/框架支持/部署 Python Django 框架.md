## 操作场景
**腾讯云 Django 组件**通过使用 [Tencent Serverless Framework](https://github.com/serverless/components/tree/cloud)，基于云上 Serverless 服务（如对象存储等），实现“0”配置，便捷开发，极速部署您的 Django 网页应用。

Django 特性介绍：
- **"0"配置**：只需要关心项目代码，之后部署即可，Serverless Framework 会搞定所有配置。
- **按需付费**：按照请求的使用量进行收费，没有请求时无需付费。
- **极速部署**：仅需几秒，部署您的网页应用。
- **便捷协作**：支持开发模式与云端调试，方便多人协作。
- **拓展广泛** ：支持 Restful API 服务的部署。


## 操作步骤
### 1. 安装 Serverless CLI

通过 npm 安装最新版本的 Serverless CLI：
```
$ npm install -g serverless
```

### 2. 初始化 Django 模版项目（可选）
如果您本地并没有 Django 项目，可通过以下指令完成 Django 项目初始化（本地已有项目可跳过该步骤）：
```
serverless init django-starter --name example
cd example
```

### 3. 安装项目依赖
如果您自己创建项目，请将 Python 所需要的依赖安装到项目目录，例如本实例需要 Django，所以可以通过 pip 进行安装：
```
pip install Django -t ./
```

### 4. 配置 yml 文件
在项目根目录下，新建 `serverless.yml` 文件。
```sh
touch serverless.yml
```
将下列配置模版粘贴到文件中，实现基本的项目配置。
>?基于您实际部署需要，您可以在 `serverless.yml` 中完成更多配置，yml 文件的配置信息请参考 [ Django 组件全量配置](https://github.com/serverless-components/tencent-django/blob/master/docs/configure.md)。
```yml
#serverless.yml
component: django
name: djangoDemo
org: orgDemo
app: appDemo
stage: dev

inputs:
  region: ap-guangzhou
  djangoProjectName: mydjangocomponent
  src: ./src
  functionConf:
    timeout: 10
    memorySize: 256
  apigatewayConf:
    protocols:
      - https
    environment: release
```


### 5. 应用部署
通过 `sls deploy` 命令进行部署，并可以添加 --debug 参数查看部署过程中的信息。

```
sls deploy --debug
```
部署完成后，通过访问输出的 API 网关链接，完成对应用的访问。


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
