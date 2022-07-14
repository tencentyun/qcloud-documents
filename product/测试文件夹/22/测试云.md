## 操作场景

Web 函数是腾讯云云函数 SCF 新支持的函数能力，区别于事件函数（Event Function）对于事件格式的限制，该类型函数专注于优化 Web 服务场景，用户可以直接发送 HTTP 请求到 URL 触发函数执行，详情请参见 [函数概述](https://cloud.tencent.com/document/product/583/56124)。

Serverless Framework SCF 组件现已支持 Web 类型函数部署，您可以通过 SCF 组件，快速创建与部署 Web 函数。


## 操作步骤

1. 执行以下命令，初始化 Serverless Web 函数模版。
```sh
sls init http-demo
```
2. 进入示例项目，查看目录结构。示例如下：
```
. http-demo
├── serverless.yml  # 配置文件
├── package.json # 依赖项文件
├── scf_bootstrap # 项目启动文件
└── index.js # 服务函数
```
其中 `scf_bootstrap` 为项目启动文件，具体编写规则请参见 [启动文件说明](https://cloud.tencent.com/document/product/583/56126)。
3. 打开 `serverless.yml`，查看配置信息。
您只需要在 `yml` 里新增 `type` 参数，指定函数类型，即可完成 Web 类型函数部署。
<dx-alert infotype="notice" title="">
- 对于 Web 类型函数，无需再指定入口函数。
- 不填 `type` 参数时，默认为事件型函数。
- 如果本地代码里无 `scf_bootstrap` 启动文件，您可以在 `yml` 里指定 `entryFile` 参数指定入口函数，组件会根据运行语言，为您生成默认 `scf_bootstrap` 启动文件完成部署。部署完成后，需根据您的实际项目情况，在 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1) 修改 `scf_bootstrap` 文件内容。
</dx-alert>
示例 <code>yml</code> 如下:
<dx-codeblock>
:::  yaml
component: scf
name: http
inputs: 
  src: 
    src: ./
    exclude: 
      - .env
  # 指定 SCF 类型为 Web 类型
  type: web
  name: web-function
  region: ap-guangzhou
  runtime: Nodejs12.16
  # 对于 Node.js，可以支持打开自动安装依赖
  installDependency: true
  events: 
    - apigw: 
        parameters: 
          protocols: 
            - http
            - https
          environment: release
          endpoints: 
            - path: /
              method: ANY
:::
</dx-codeblock>
4. 在根目录下执行 `sls deploy` 命令，即可完成服务部署。示例如下：
```shell
$ sls deploy
serverless ⚡components
Action: "deploy" - Stage: "dev" - App: "http" - Name: "http"
type:         web
functionName: web-function
description:  This is a function in http application
namespace:    default
runtime:      Nodejs12.16
handler:      
memorySize:   128
lastVersion:  $LATEST
traffic:      1
triggers: 
  - 
    NeedCreate:  true
    created:     true
    serviceId:   service-xxxxxx
    serviceName: serverless
    subDomain:   service-xxxxxx.cd.apigw.tencentcs.com
    protocols:   http&https
    environment: release
    apiList: 
      - 
        path:            /
        method:          ANY
        apiName:         index
        created:         true
        authType:        NONE
        businessType:    NORMAL
        isBase64Encoded: false
        apiId:           api-xxxxxx
        internalDomain:  
        url:             https://service-xxxx.cd.apigw.tencentcs.com/release/
18s › http › 执行成功
```


## 相关命令

### 查看访问日志

与事件型函数相同，可直接通过 `sls log` 命令查看部署完成的函数最近10条日志信息。示例如下：
```sh
$ sls log
serverless ⚡components
Action: "log" - Stage: "dev" - App: "http" - Name: "http"
- 
  requestId:   xxxxx
  retryNum:    0
  startTime:   1624262955432
  memoryUsage: 0.00
  duration:    0
  message: 
    """
    """
- 
  requestId: xxxxx
  retryNum:    0
  startTime:   1624262955432
  memoryUsage: 0.00
  duration:    0
  message: 
    """
    """
```

### 测试服务

- 方案1：在浏览器直接打开输出的路径 URL，如果可以正常访问，则说明函数创建成功。如下图所示：
![](https://main.qcloudimg.com/raw/5268439a29278030d6614d35d7b9933b.png)
- 方案2：您可以使用其他 HTTP 测试工具，例如 CURL、POSTMAN 等工具测试您已创建成功的 Web 函数。如下示例为通过 CURL 工具测试：
```sh
curl https://service-xxx.cd.apigw.tencentcs.com/release/
```


### 删除服务

执行以下命令，即可移除您已部署的云上资源。
```sh
sls remove
```
