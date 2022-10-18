## 操作场景
腾讯云 [ThinkPHP](https://github.com/top-think/think) Serverless Component 支持基于 ThinkPHP（≥ 6.x）的 RESTful API 服务的部署。

## 前提条件
#### 初始化 ThinkPHP 项目
1. 本地已经搭建了 PHP 环境，且建议版本 ≥ PHP7.1（ThinkPHP 6 推荐版本）。
2. 安装 Composer ：ThinkPHP 使用 Composer 管理依赖，安装方式请参考 [官方安装文档](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-macos)。

上述两个步骤完成后，使用 Composer 初始化一个 `ThinkPHP` 项目：
```bash
composer create-project topthink/think serverless-thinkphp
```

## 操作指南
### 1. 安装

通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：

```bash
npm install -g serverless
```

### 2. 配置
在项目根目录，创建 `serverless.yml` 文件：
```bash
$ touch serverless.yml
```

在 `serverless.yml` 中进行如下配置：
```yml
# serverless.yml
app: appDemo
stage: dev
component: thinkphp
name: thinkphpDemo

inputs:
  src:
    src: ./
    exclude:
      - .env
  region: ap-guangzhou
  runtime: Php7
  apigatewayConf:
    protocols:
      - http
      - https
    environment: release
```

[更多配置 >>](https://github.com/serverless-components/tencent-thinkphp/tree/master/docs/configure.md)

### 3. 部署

>!在部署前，需要先执行 `php think clear` 清理本地运行的配置缓存。

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过 `sls` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息：
```bash
$ sls deploy --debug
```

### 4. 移除

通过以下命令移除部署的 ThinkPHP 项目：

```bash
$ sls remove --debug
```

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

### 更多组件

您可以在 [Serverless Components](https://github.com/serverless-components) repo 中查询更多组件的信息。
