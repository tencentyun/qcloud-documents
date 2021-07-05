Web 函数是腾讯云 SCF 云函数新支持的函数能力，区别于事件函数（Event Function）对于事件格式的限制，该类型函数专注于优化 Web 服务场景，用户可以直接发送 HTTP 请求到 URL 触发函数执行，详细说明请参考[官网文档](https://cloud.tencent.com/document/product/583/56124)。

Serverless Framework SCF 组件现已支持该类型函数部署，您可以通过 SCF 组件，快速创建与部署 Web 函数。

### 部署指引
1. 初始化 serverless web 函数模版
```
sls init http-demo
```
进入示例项目，查看目录结构：
```
. http-demo
├── serverless.yml  # 配置文件
├── package.json # 依赖项文件
├── scf_bootstrap # 项目启动文件
└── index.js # 服务函数
```
其中 `scf_bootstrap` 为项目启动文件，具体编写规则请参考[启动文件说明](https://cloud.tencent.com/document/product/583/56126)。

2. 打开 `serverless.yml`，查看配置信息

您只需要在 `yml` 里新增 `type` 参数，指定函数类型，即可完成 Web 类型函数部署

> 注意：
> - 对于 web 类型函数，无需再指定入口函数
> - 不填 `type` 参数时，默认为事件型函数
> - 如果本地代码里没有 `scf_bootstrap` 启动文件，您可以在 `yml` 里指定 `entryFile` 参数指定入口函数，组件会根据运行语言，为您生成默认 `scf_bootstrap` 启动文件完成部署，部署完成后注意根据您的实际项目情况，在函数控制台修改 `scf_bootstrap` 文件内容。

示例 `yml`:
```yml
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
```

3. 在根目录下执行 `sls deploy`，即可完成服务部署
```sh
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

### 功能支持
**1. 查看访问日志**

与事件型函数相同，直接通过 `sls log`，即可查看部署完成的函数最近10条日志i 信息
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
**2. 测试服务**
- 方案一：在浏览器里打开直接打开输出的路径 URL，如果可以正常访问，则说明函数创建成功。如下图所示：
![](https://main.qcloudimg.com/raw/aa148dbd46bf5d9a11b32d86ed3c57ba.png)
- 方案二：您可以使用其他 HTTP 测试工具，如 CURL、POSTMAN 等测试您已创建成功的 Web 函数：
```sh
$ curl https://service-xxx.cd.apigw.tencentcs.com/release/
```
**3. 删除服务**

直接执行 `sls remove`，即可移除您已部署的云上资源
