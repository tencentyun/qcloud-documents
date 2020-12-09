## 操作场景
 腾讯云 [Laravel](https://github.com/laravel/laravel) Serverless Component，支持 Laravel 6.0及以上版本。 

## 前提条件
### 初始化 Laravel 项目
在使用此组件之前，您需要先初始化一个 `laravel` 项目：
```shell
composer create-project --prefer-dist laravel/laravel serverless-laravel
```
>!Laravel 使用 Composer 管理依赖，所以您需要先自行安装 Composer，请参考 [官方安装文档](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-macos)。


## 操作步骤
### 安装
通过 npm 全局安装 [serverless cli](https://github.com/serverless/serverless)：
```shell
npm install -g serverless
```

### 配置
在项目根目录下创建 `serverless.yml` 文件，[查看详细配置文档]( https://github.com/serverless-components/tencent-laravel/blob/master/docs/configure.md )
：
```shell
touch serverless.yml
```

在 `serverless.yml` 中进行如下配置：
```yml
# serverless.yml

component: laravel
name: laravelDemo
org: orgDemo
app: appDemo
stage: dev

inputs:
  src: ./
  region: ap-guangzhou
  runtime: Php7
  apigatewayConf:
    protocols:
      - http
      - https
    environment: release
```


### 部署

执行以下命令进行扫码授权部署：

```console
sls deploy
```

>?
>-  **在部署前，您需要先清理本地运行的配置缓存，执行 `php artisan config:clear` 即可。** 
>- 微信扫码授权部署有过期时间，如果想要持久授权，请参考 [账号配置](#account)。

### 移除

执行以下命令移除部署的服务：

```console
sls remove
```

<span id="account"></span>
### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```shell
touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：

```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```

>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。

