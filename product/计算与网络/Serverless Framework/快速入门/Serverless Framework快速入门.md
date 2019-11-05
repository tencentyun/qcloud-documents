
# Serverless Framework快速入门

通过如下几步，使用Serverless Framework开源CLI在腾讯云上部署一个服务，完成配置-创建-测试-部署等步骤。

## 前提条件

在使用之前，请确保如下软件已经安装：

- [您的环境中已经安装了Node.js 6.x 或以上的版本](#安装 Node.js 和 NPM)
- [您的环境已经安装了Serverless Framework CLI 1.47.0 或以上的版本](#安装Serverless Framework CLI)

如果这些条件已经满足，您可以跳过此步骤，直接开始部署一个服务。

### 安装 Node.js 和 NPM

- 参考 [Node.js安装指南](https://nodejs.org/zh-cn/download/)根据您的系统环境进行安装。
- 安装完毕后，通过`node -v` 命令，查看安装好的Node.js版本信息

```sh
$ node -v
vx.x.x
```

- 通过 `npm -v` 命令，查看安装好的npm版本信息

```sh
$ npm -v
x.x.x
```

### 安装Serverless Framework CLI

- 在命令行中运行如下命令

```sh
npm install -g serverless
```

- 安装完毕后，通过运行 `serverless -v` 命令，查看Serverless Framework CLI的版本信息。

```sh
$ serverless -v
x.x.x
```

## 创建并部署你的serverless 服务

完成上述安装准备后，通过如下步骤开始部署一个serverless 服务

### 通过模板创建一个新的服务

1. 使用Serverless Framework的 `tencent-nodejs`模板创建新的服务

通过运行如下命令进行创建，`--path`可以指定服务的路径
```sh
# 创建一个serverless服务
$ serverless create --template tencent-nodejs --path my-service

2. 安装依赖

进入服务所在路径，运行如下命令安装依赖
```sh
$ cd my-service
$ npm install
```

### 配置账户信息

参考该文档[配置您的腾讯云账户](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E9%85%8D%E7%BD%AE%E8%B4%A6%E5%8F%B7.md) 。

### 为服务配置触发器

云函数需要通过触发器的事件调用进行触发，因此可以在`serverless.yml`中增加对触发器的配置，以API网关触发器为例，配置如下：

```yaml
service: my-service # service name

provider: # provider information
  name: tencent
  runtime: Nodejs8.9
  credentials: ~/credentials  #秘钥配置需要和上一步配置的账户信息文件路径一致

plugins:
  - serverless-tencent-scf

functions:
  function_one:
    handler: index.main_handler
    runtime: Nodejs8.9
    events:
        - apigw:
           name: hello_world_apigw
           parameters:
             stageName: release
             serviceId:
             httpMethod: ANY
```

### 部署服务

通过该命令部署或更新您创建的函数和触发器，资源配置会和`serverless.yml`中保持一致。

```bash
serverless deploy
```
更多部署详情参考 [deploy command](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E9%83%A8%E7%BD%B2%E6%9C%8D%E5%8A%A1.md)

### 测试服务

替换如下命令中的链接地址，通过curl对其进行测试，该链接可以在`sls deploy`命令执行后获取得到。

```bash
$ curl -X POST https://service-xxxx-1300000000.ap-guangzhou.apigateway.myqcloud.com/release/
```

### 云端调用

通过以下命令云端调用函数并且获得日志信息的返回。

```bash
serverless invoke -f hello
```
更多部署详情参考 [云端调用](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C/Serverless%20Framework/%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97/%E4%BA%91%E7%AB%AF%E8%B0%83%E7%94%A8.md)

### 获取函数日志

单独开启一个命令行，通过如下命令，实时获取函数`hello`的云端调用日志信息。

```bash
serverless logs -f hello -t
```

### 移除你的服务

如果不再需要此服务，可以通过如下命令一键移除服务，该命令会清理相应函数和触发器资源。

```sh
serverless remove
```

## 更多丰富案例

查看[Git仓库](https://github.com/serverless-tencent/Plugin-Example)获取更多案例。

