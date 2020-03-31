## 操作场景
腾讯云 [Laravel](https://github.com/laravel/laravel) Serverless Component，支持 Restful API 服务的部署。

## 前提条件
#### 初始化 Laravel 项目
在使用此组件之前，您需要先初始化一个 `laravel` 项目：
```shell
php composer create-project --prefer-dist laravel/laravel serverless-laravel
```
>!Laravel 使用 Composer 管理依赖，所以您需要先自行安装 Composer，请参考 [官方安装文档](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-macos)。

#### 修改 Laravel 项目
由于云函数在执行时，只有 `/tmp` 可读写的，所以我们需要将 `laravel` 框架运行时的 `storage` 目录写到该目录下，为此需要修改 `bootstrap/app.php` 文件，在 `$app = new Illuminate\Foundation\Application` 后添加：
```php
$app->useStoragePath($_ENV['APP_STORAGE'] ?? $app->storagePath());
```

然后在根目录下的 `.env` 文件中新增如下配置：
```dotenv
# 视图文件编译路径
VIEW_COMPILED_PATH=/tmp/storage/framework/views

# 由于是无服务函数，所以没法存储 session 在硬盘上，如果不需要 sessions，可以使用 array
# 如果需要您可以将 session 存储到 cookie 或者数据库中
SESSION_DRIVER=array

# 建议将错误日志输出到控制台，方便云端去查看
LOG_CHANNEL=stderr

# 应用的 storage 目录必须为 /tmp
APP_STORAGE=/tmp
```

## 操作步骤
#### 安装
通过 npm 全局安装 [serverless cli](https://github.com/serverless/serverless)：
```shell
$ npm install -g serverless
```

#### 配置
在项目根目录，创建 `serverless.yml` 文件：
```shell
$ touch serverless.yml
```

在 `serverless.yml` 中进行如下配置：
```yml
# serverless.yml

MyComponent:
  component: "@serverless/tencent-laravel"
  inputs:
    region: ap-guangzhou 
    functionName: laravel-function
    code: ./
    functionConf:
      timeout: 10
      memorySize: 128
      environment:
        variables:
          TEST: vale
      vpcConfig:
        subnetId: ''
        vpcId: ''
    apigatewayConf:
      protocol: https
      environment: release
```

[查看详细配置文档 >>](https://github.com/serverless-components/tencent-laravel/tree/master/docs/configure.md)

#### 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过 `sls` 命令进行部署，并添加 `--debug` 参数查看部署过程中的信息：
>? `sls` 是 `serverless` 命令的简写。

```shell
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Compressing function laravel-function file to /Users/Downloads/serverless-laravel/.serverless/laravel-function.zip.
  DEBUG ─ Compressed function laravel-function file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-guangzhou-code]. sls-cloudfunction-default-laravel-function-1581888194.zip
  DEBUG ─ Uploaded package successful /Users/Downloads/serverless-laravel/.serverless/laravel-function.zip
  DEBUG ─ Creating function laravel-function
  DEBUG ─ Created function laravel-function successful
  DEBUG ─ Setting tags for function laravel-function
  DEBUG ─ Creating trigger for function laravel-function
  DEBUG ─ Deployed function laravel-function successful
  DEBUG ─ Starting API-Gateway deployment with name MyComponent.TencentApiGateway in the ap-guangzhou region
  DEBUG ─ Service with ID service-ok334ism created.
  DEBUG ─ API with id api-l7cppn6s created.
  DEBUG ─ Deploying service with id service-ok334ism.
  DEBUG ─ Deployment successful for the api named MyComponent.TencentApiGateway in the ap-guangzhou region.

  MyComponent: 
    region:              ap-guangzhou
    functionName:        laravel-function
    apiGatewayServiceId: service-ok334ism
    url:                 http://service-ok334ism-1258834142.gz.apigw.tencentcs.com/release/

  192s › MyComponent › done
```

#### 移除

通过以下命令移除部署的服务：
```shell
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing function
  DEBUG ─ Request id
  DEBUG ─ Removed function laravel-function successful
  DEBUG ─ Removing any previously deployed API. api-l7cppn6s
  DEBUG ─ Removing any previously deployed service. service-ok334ism

  18s › MyComponent › done
  
```

#### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：
```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```

>?
>- 如果没有腾讯云账号，可以在此 [注册新账号](https://cloud.tencent.com/register)。
>-  如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
