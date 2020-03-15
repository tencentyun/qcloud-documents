## 操作场景
该任务指导您使用 Serverless Framework 开源 Component 在腾讯云上部署一个云函数 + API 网关的服务，并完成创建、配置、部署等步骤。

>?
>- 通过 Serverless Framework 创建的资源，您可以在资源自身的控制台进行查看和管理，例如 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)、[API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) 等。
>- 预计2020年3月，Serverless Framework 将提供可视化的页面，您可以从 Serverless 应用的角度查看和管理资源。

## 前提条件
在使用之前，请确保如下软件已经安装：
- [Node.js](#node)（6.x或以上的版本）
- [Serverless Framework](#sf)（1.57.0或以上的版本）

如果这些条件已经满足，您可以跳过此步骤，直接 [开始部署一个服务](#steps)。

<span id="node"></span>
#### 安装 Node.js 和 NPM

1. 参考 [Node.js 安装指南](https://nodejs.org/zh-cn/download/) 根据您的系统环境进行安装。
2. 安装完毕后，通过`node -v`命令，查看安装好的 Node.js 版本信息：
```sh
$ node -v
vx.x.x
```
3. 通过`npm -v`命令，查看安装好的 npm 版本信息：
```sh
$ npm -v
x.x.x
```

<span id="sf"></span>
#### 安装 Serverless Framework

1. 在命令行中运行如下命令：
```sh
$ npm install -g serverless
```
>?如 Mac 系统提示无权限，则需要运行`sudo npm install -g serverless`进行安装。
2. 安装完毕后，通过运行`serverless -v`命令，查看 Serverless Framework CLI 的版本信息。
```sh
$ serverless -v
x.x.x
```

<span id="steps"></span>
## 操作步骤

完成上述安装准备后，通过如下步骤开始部署一个 Serverless 服务。

#### 创建服务

1. 创建并进入目录：
```bash
$ mkdir my-function && cd my-function
```
2. 在目录中创建`index.js`作为云函数的入口函数：
```bash
$ touch index.js
```
3. 在`index.js`中增加如下代码：
```javascript
'use strict';
exports.main_handler = async (event, context, callback) => {
    console.log("%j", event);
    return "hello world"
};
```

#### 配置服务
在本地创建`serverless.yml`文件，
```bash
$ touch serverless.yml
```

在`serverless.yml`中进行如下配置：

```yaml
# serverless.yml
myFunction:
  component: "@serverless/tencent-scf"
  inputs:
    name: myFunction
    codeUri: ./       # 代码目录
    handler: index.main_handler
    runtime: Nodejs8.9
    region: ap-guangzhou
    description: My Serverless Function
    memorySize: 128
    events:  # 触发器配置
      - apigw:
          name: serverless
          parameters:
            protocols:
              - http
            endpoints:
              - path: /
                method: GET
```
>?您可以通过 [详细配置文档](https://github.com/serverless-components/tencent-scf/blob/master/docs/configure.md)，查看`serverless.yml`中所有可用属性的属性列表。


#### 部署服务
如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以在运行该命令后，直接用**微信**扫描命令中弹出的二维码，对云账户进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息：
>?`sls`是`serverless`命令的简写。

```bash
sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
Please scan QR code login from wechat. 
Wait login...
Login successful for TencentCloud. 
  DEBUG ─ Compressing function myFunction file to /Users/tina/Desktop/live/scfcomponent/my-function/.serverless/myFunction.zip.
  DEBUG ─ Compressed function myFunction file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-guangzhou-code]. sls-cloudfunction-default-myFunction-1582797244.zip
  DEBUG ─ Uploaded package successful /Users/tina/Desktop/live/scfcomponent/my-function/.serverless/myFunction.zip
  DEBUG ─ Creating function myFunction
  DEBUG ─ Created function myFunction successful
  DEBUG ─ Setting tags for function myFunction
  DEBUG ─ Creating trigger for function myFunction
  DEBUG ─ Starting API-Gateway deployment with name myFunction.serverless in the ap-guangzhou region
  DEBUG ─ Service with ID service-qs0cud0s created.
  DEBUG ─ API with id api-irl0q216 created.
  DEBUG ─ Deploying service with id service-qs0cud0s.
  DEBUG ─ Deployment successful for the api named myFunction.serverless in the ap-guangzhou region.
  DEBUG ─ Deployed function myFunction successful

  myFunction: 
    Name:        myFunction
    Runtime:     Nodejs8.9
    Handler:     index.main_handler
    MemorySize:  128
    Timeout:     3
    Region:      ap-guangzhou
    Description: My Serverless Function
    APIGateway: 
      - serverless - http://service-qs0cud0s-1300862921.gz.apigw.tencentcs.com/release

  22s › myFunction › done
```

#### 测试服务
在浏览器中打开输出链接，或替换如下命令中的链接地址，通过 curl 对其进行测试，该链接可以在`sls`命令执行后获取得到。
```bash
$ curl -X GET http://service-qs0cud0s-1300862921.gz.apigw.tencentcs.com/release
```

#### 移除服务
如果您不再需要此服务，可以通过如下命令一键移除服务，该命令会清理相应函数和触发器资源。
```sh
serverless remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing any previously deployed API. api-irl0q216
  DEBUG ─ Removing any previously deployed service. service-qs0cud0s
  DEBUG ─ Removing function
  DEBUG ─ Removed function myFunction successful

  9s › myFunction1 › done
```

#### 配置账户信息（可选）
当前默认支持部署时扫描微信二维码登录，如您希望配置持久的环境变量/密钥信息，也可以参考 [配置账号](https://cloud.tencent.com/document/product/1154/38811) 文档。
