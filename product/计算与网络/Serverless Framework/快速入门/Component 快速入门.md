## 操作场景
该任务指导您通过 Serverless Framework Component，在腾讯云上快速创建、配置和部署一个云函数 + API 网关的服务。

>?
>- 通过 Serverless Framework 创建的资源，您可以在资源自身的控制台进行查看和管理，例如 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)、[API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) 等。
>- 预计2020年4月，Serverless Framework 将提供可视化的页面，您可以从 Serverless 应用的角度查看和管理资源。

## 前提条件
在使用之前，请确保已经 [安装 Serverless Framework 1.57.0 以上版本](https://cloud.tencent.com/document/product/1154/42990)。

## 操作步骤
### 创建服务

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

### 配置服务
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


### 部署服务
如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以在运行该命令后，直接用**微信**扫描命令中弹出的二维码，对云账户进行授权登录和注册。

通过`sls`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息：
>?`sls`是`serverless`命令的简写。

```bash
sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.