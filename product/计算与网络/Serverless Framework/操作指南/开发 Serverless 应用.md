## 操作场景
Serverless Framework 提供了多个基础资源组件，用户可以通过不同组件的结合使用，快速完成云端资源的创建与部署，本教程将指导您如何使用已有组件，构建您自己的多组件 Serverless 应用模版。

## 前提条件
已 [安装 Serverless Framework](https://cloud.tencent.com/document/product/1154/42990)，并保证您的 Serverless Framework 不低于以下版本：

```shell
$ serverless –v
Framework Core: 2.16.1
Plugin: 4.3.0
SDK: 2.3.2
Components: 3.4.3
```


## 组件全量配置文档[](id:doc)

- [基础组件列表](https://cloud.tencent.com/document/product/1154/51106)
- [框架组件列表](https://cloud.tencent.com/document/product/1154/51124)


## 操作步骤
此处以部署一个使用 **Layer + Egg 框架项目**为例，指导您如何在项目中引入多个组件，并快速完成部署，步骤如下：

### 步骤1：创建项目
新建项目 `app-demo` 并进入该目录下：

   ```bash
   $ mkdir app-demo && cd app-demo
   ```

### 步骤2：构建 Egg 项目

1. 在 `app-demo` 目录下，新建 `src` 文件夹，并在文件夹中新建 Egg 项目：
```bash
$ mkdir src && cd src
$ npm init egg --type=simple
$ npm i
```

2. 在 `src` 目录下，编写配置文件 `serverless.yml`：
```bash
$ touch serverless.yml
```
 egg 组件的 yml 文件示例如下（全量配置文件可参考 [Eggjs 组件全量配置](https://github.com/serverless-components/tencent-egg/blob/master/docs/configure.md)）：
<dx-codeblock>
:::  yml
# serverless.yml
app: app-demo #应用名称，同一个应用下每个组件的 app、stage、org 参数必须保持一一致
org: app-demo
stage: dev
component: egg 
name:  app-demo-egg # (必填) 创建的实例名称

inputs:
  src:   
    src: ./    # 需要上传的项目路径
    exclude:   # 除去 node_modules 以及 .env 文件
      - .env
      - node_modules
  region: ap-guangzhou
  functionName: eggDemo  # 函数配置
  runtime: Nodejs10.15
  apigatewayConf:
    protocols:           # API 网关触发器配置，默认新创建网关
      - http
      - https
    environment: release
:::
</dx-codeblock>

 >!
>- 同一个应用下，每一个组件创建的资源的 **app、stage、org** 参数必须保持一致，**name** 参数必须唯一。
>- Egg 组件实际上创建的是一个 API 网关触发器 + 云函数资源，此处可根据您的实际开发场景，选择不同组件，配置方法相似，详情请参考 [组件全量配置](#doc)。


### 步骤3：创建层
回到 `app-demo` 根目录下，新建 `layer` 文件夹，并在里面新建 layer 配置文件 `serverless.yml`：
```
$ cd ..
$ mkdir layer && cd layer
$ touch serverless.yml
```
`serverless.yml` 可以按照如下模版配置（更多配置请参考 [Layer 组件全量配置](https://github.com/serverless-components/tencent-layer/blob/master/docs/configure.md)）：
<dx-codeblock>
:::  yml
# serverless.yml
app: app-demo #应用名称，同一个应用下每个组件的 app、stage、org 参数必须保持一致
org: app-demo
stage: dev
component: layer 
name:  app-demo-layer # (必填) 创建的实例名称

inputs:
  region: ap-guangzhou
  src: 
    src: ../src/node_modules # 您想要上传到层的项目路径，此处以 node_modules 为例
    targetDir: /node_modules # 上传后的文件打包目录
  runtimes:
    - Nodejs10.15
:::
</dx-codeblock>

>!
>- 同一个应用下，每一个组件创建的资源的 **app、stage、org** 参数必须保持一致，**name** 参数必须唯一。
>- layer 组件也支持从 COS 桶导入项目，详情参考[Layer组件全量配置](https://github.com/serverless-components/tencent-layer/blob/master/docs/configure.md)，填写 `bucket` 参数时注意不要带 `-${appid}`，组件会自动为您添加。

### 步骤4：组织资源关系

同一个应用内，用户可以根据各个资源的依赖关系组织资源的创建顺序，以该项目为例，用户需要先创建好 layer，再在 Egg 项目里使用该 layer，因此需要保证资源的创建顺序为 **layer -> eggjs 应用**，具体操作如下：

修改 Egg 项目的 yml 配置文件，在层配置部分按以下语法进行配置，引用 Layer 组件的部署输出作为 Egg 项目的部署输入，即可保证 Layer 组件一定在 Egg 项目之前完成创建：

```
$ cd ../src
```
在 `serverless.yml` 里，`inputs` 部分增加 layer 配置：
<dx-codeblock>
:::  yml
inputs:
  src:   
    src: ./    
    exclude:  
      - .env
      - node_modules
  region: ap-guangzhou
  functionName: eggDemo  
  runtime: Nodejs10.15
  layers:   # 增加 layer 配置
    - name: ${output:${stage}:${app}:app-demo-layer.name} #  layer名称
      version: ${output:${stage}:${app}:app-demo-layer.version} #  版本
  apigatewayConf:
    protocols:        
      - http
      - https
    environment: release
:::
</dx-codeblock>

变量引用格式请参考 [变量引用说明](#quote)。

此时已完成 Serverless 应用的构建，项目目录结构如下：

   ```
   ./app-demo
   ├── layer
   │   └── serverless.yml # layer 配置文件
   ├── src
   │   ├── serverless.yml # egg 组件配置文件
   │   ├── node_modules # 项目依赖文件
   │   ├── ...
   │   └── app # 项目路由文件
   └── .env # 环境变量文件
   ```
  
### 步骤5：部署应用
在项目根目录下，执行 `sls deploy`，即可完成 Layer 创建，并将 Layer 组件的输出作为 Egg 组件的输入，完成 Egg 框架上云。
<dx-codeblock>
:::  bash
$ sls deploy

serverless ⚡framework

app-demo-layer: 
  region:        ap-guangzhou
  name:          layer_component_xxx
  bucket:        sls-layer-ap-guangzhou-code
  object:        layer_component_xxx.zip
  description:   Layer created by serverless component
  runtimes: 
    - Nodejs10.15
  version:       3
  vendorMessage: null

app-demo-egg: 
  region:        ap-guangzhou
  scf: 
    functionName: eggDemo
    runtime:      Nodejs10.15
    namespace:    default
    lastVersion:  $LATEST
    traffic:      1
  apigw: 
    serviceId:   service-xxxx
    subDomain:   service-xxx.gz.apigw.tencentcs.com
    environment: release
    url:         https://service-xxx.gz.apigw.tencentcs.com/release/
  vendorMessage: null

76s › app-demo › "deploy" ran for 2 apps successfully.
:::
</dx-codeblock>


点击 `apigw` 输出的 URL，即可访问您已经创建好的应用，执行 `sls info`，可以查看部署的实例状态，执行 `sls remove`，可以快速移除应用。

### 步骤6：发布应用模版
完成模版构建后，Serverless Framework 支持您将自己的 Serverless 项目模版发布在 Serverless Registry 应用中心中，提供给团队和他人使用。

#### 1. 创建配置文件
根目录下，新建 `serverless.template.yml` 文件，此时项目目录结构如下：
   
   ```
   ./app-demo
   ├── layer
   │   └── serverless.yml # layer 配置文件
   ├── src
   │   ├── serverless.yml # egg 组件配置文件
   │   ├── node_modules # 项目依赖文件
   │   ├── ...
   │   └── app # 项目路由文件
   ├── .env # 环境变量文件
   └── serverless.template.yml # 模版项目描述文件
   ```

#### 2. 配置项目模版文件并发布
<dx-codeblock>
:::  yml
# serverless.template.yml
name: app-demo # 项目模板的名字，模版唯一标识，不可重复
displayName: 基于 layer 创建的 eggjs 项目模版 #项目模板展示在控制台的名称（中文）
author: Tencent Cloud, Inc. # 作者的名字
org: Tencent Cloud, Inc. # 组织名称，可选
type: template #项目类型，可填 template 或 component，此处为模版
description: Deploy an egg application with layer. # 描述您的项目模板
description-i18n:
  zh-cn: 基于 layer 创建的 eggjs 项目模版 # 中文描述
keywords: tencent, serverless, eggjs, layer # 关键字
repo:  # 源代码,通常为您的 github repo
readme:  # 详细的说明文件，通常为您的 github repo README 文件
license: MIT # 版权声明
src: # 描述项目中的哪些文件需要作为模板发布
  src: ./ # 指定具体的相对目录，此目录下的文件将作为模板发布
  exclude: #描述在指定的目录内哪些文件应该被排除
    # 通常希望排除
    # 1. 包含 secrets 的文件
    # 2. .git git 源代码管理的相关文件
    # 3. node_modules 等第三方依赖文件
    - .env
    - '**/node_modules'
    - '**/package-lock.json'
:::
</dx-codeblock>

`serverless.template.yml` 文件配置完成后，便可以使用发布命令 `sls publish` 将此项目作为模板发布到应用中心。
```
$ sls publish

serverless ⚡registry
Publishing "app-demo@0.0.0"...

Serverless › Successfully published app-demo
```

#### 3. 复用模版

完成发布后，其他人可通过 `sls init` 指令，快速下载您的模版并进行项目复用。
```
$ sls init app-demo --name example
$ cd example
$ npm install
```


## 变量引用说明[](id:quote)
`serverless.yml` 支持多种方式引用变量：

- **顶级参数引用**
   在 `inputs` 字段里，支持直接引用顶级配置信息，引用语法如下：`${org}`、`${app}`

- **环境变量引用**  
   在 `serverless.yml` 中，可以直接通过 `${env}` 的方式，直接引用环境变量配置（包含 .env 文件中的环境变量配置，以及手动配置在环境中的变量参数）。
   
   例如，通过`${env:REGION}`，引用环境变量 REGION。

- **引用其它组件输出结果**
   如果希望在当前组件配置文件中引用其他组件实例的输出信息，可以通过如下语法进行配置：
	 `${output:[app]:[stage]:[instance name].[output]}`

示例 yml：
<dx-codeblock>
:::  yml
org: xxx
app: demo
component: scf
name: rest-api
stage: dev

inputs:
  name: ${org}-${stage}-${app}-${name} # 命名最终为 "acme-prod-ecommerce-rest-api"
  region: ${env:REGION} # 环境变量中指定的 REGION= 信息
  vpcName: ${output:prod:my-app:vpc.name} # 获取其他组件中的输出信息
  vpcName: ${output:${stage}:${app}:vpc.name} # 上述方式也可以组合使用
:::
</dx-codeblock>


 
