## 操作场景
该任务指导您使用 Serverless Framework 开源 CLI 在腾讯云上部署一个服务，并完成配置、创建、测试、部署等步骤。
>?
>- 通过 Serverless Framework 创建的资源，您可以在资源自身的控制台进行查看和管理，例如 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)、[API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) 等。
>- 预计2020年3月，Serverless Framework 将提供可视化的页面，您可以从 Serverless 应用的角度查看和管理资源。

## 前提条件
在使用之前，请确保如下软件已经安装：
- [Node.js](#node)（6.x或以上的版本）
- [Serverless Framework CLI](#cli)（1.57.0或以上的版本）

如果这些条件已经满足，您可以跳过此步骤，直接 [开始部署一个服务](#buzhou)。


<span id="node"></span>
#### 安装 Node.js 和 NPM

- 参考 [Node.js 安装指南](https://nodejs.org/zh-cn/download/) 根据您的系统环境进行安装。
- 安装完毕后，通过`node -v` 命令，查看安装好的 Node.js 版本信息：
```sh
$ node -v
vx.x.x
```
- 通过 `npm -v` 命令，查看安装好的 npm 版本信息：
```sh
$ npm -v
x.x.x
```

<span id="cli"></span>
#### 安装 Serverless Framework CLI

- 在命令行中运行如下命令：
```sh
npm install -g serverless
```

- 安装完毕后，通过运行 `serverless -v` 命令，查看 Serverless Framework CLI 的版本信息。
```sh
$ serverless -v
x.x.x
```

<span id="buzhou"></span>
## 操作步骤

完成上述安装准备后，通过如下步骤开始部署一个 Serverless 服务。

#### 通过模板创建服务
1. 使用 Serverless Framework 的 `tencent-nodejs` 模板创建一个新的服务。
通过运行如下命令进行创建，`--path`可以指定服务的路径：
```sh
# 创建一个serverless服务
$ serverless create --template tencent-nodejs --path my-service
```
2. 安装依赖。
进入服务所在路径，运行如下命令安装依赖：
```sh
$ cd my-service
$ npm install
```

#### 配置触发器
云函数需要通过触发器的事件调用进行触发，因此可以在`serverless.yml`中增加对触发器的配置，以 API 网关触发器为例，配置如下：
```yaml
service: my-service # service name

provider: # provider information
  name: tencent
  runtime: Nodejs8.9
  credentials: ~/credentials  #如不使用二维码一键登录，密钥字段需要和 credentials 文件路径一致

plugins:
  - serverless-tencent-scf

functions:
  hello_world:   # 函数名称
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
>?
>- 您可以通过 [详细配置文档](https://github.com/serverless-tencent/serverless-tencent-scf/blob/master/docs/zh/yaml.md)，查看`serverless.yml`中所有可用属性的属性列表。
>- Serverless Framework 会为控制台中实际部署的函数增加前缀组成函数名称，前缀规范为`service-stage-function`，默认的stage为`dev`。以上述配置为例，配置文件中的函数名称`hello_world`在控制台中的函数名称对应为`my-service-dev-hello_world`。


#### 部署服务
通过该命令部署或更新您创建的函数和触发器，资源配置会和`serverless.yml`中保持一致。
```bash
serverless deploy
```

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以在运行该命令后，直接用**微信**扫描命令中弹出的二维码，对云账户进行授权登录和注册。

更多部署详情参考 [部署服务](https://cloud.tencent.com/document/product/1154/38814) 文档。

#### 测试服务

替换如下命令中的链接地址，通过 curl 对其进行测试，该链接可以在`sls deploy`命令执行后获取得到。
```bash
$ curl -X POST https://service-xxxx-1300000000.ap-guangzhou.apigateway.myqcloud.com/release/
```

#### 云端调用

通过以下命令云端调用函数并且获得日志信息的返回。

```bash
serverless invoke -f hello_world
```
更多部署详情参考 [云端调用](https://cloud.tencent.com/document/product/1154/38815)。

#### 获取函数日志

单独开启一个命令行，输入如下命令，再次云端调用函数，并实时获取函数`hello_world`的云端调用日志信息。
```bash
serverless logs -f hello_world -t
```

#### 移除服务

如果您不再需要此服务，可以通过如下命令一键移除服务，该命令会清理相应函数和触发器资源。
```sh
serverless remove
```

#### 配置账户信息
当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以参考 [配置账号](https://cloud.tencent.com/document/product/1154/38811) 文档。
