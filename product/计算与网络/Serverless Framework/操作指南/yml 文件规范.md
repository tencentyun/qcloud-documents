Serverless Framework 通过项目配置文件 `serverless.yml` 完成应用的类型识别与资源配置，本地开发完成后的项目，必须先配置 yml 文件，才可以通过运行 `sls deploy` 命令，将 serverless.yml 中的配置文件和 inputs 中指定参数或代码目录会都被传入 Serverless Components 部署引擎中，从而完成云端部署。

## 基本信息

一个基本的 `serverless.yml` 文件里，第一层配置字段为以下内容：

```yml
#应用组织信息（可选）
org: '' # 组织名称。留空则则使用默认值为用户 APPID
app: '' # 应用名称。留空则默认取当前组件的实例名称为app名称。
stage: '' # 环境名称。默认值是 dev。建议使用 ${env.STAGE} 变量定义环境名称

#组件信息
component: scf # (必选) 组件名称，在该实例中为 scf
name: scfdemo # (必选) 组件实例名称。

#组件参数配置，根据每个组件，实现具体的资源信息配置
inputs:

```

## 详细配置

在 `inputs` 字段里，根据每个组件创建的云上资源，会进行对应的信息配置，此处以 [云函数 SCF 组件](https://github.com/serverless-components/tencent-scf) 为例，input 字段内的二级目录如下：

```yml
inputs:
  name: xxx # 云函数名称，默认为 ${name}-${stage}-${app}
  src: ./src # 项目代码路径，默认写法，新建特定命名的 COS Bucket 并上传
  handler: index.main_handler #入口
  runtime: Nodejs10.15 # 运行环境 默认 Nodejs10.15
  region: ap-guangzhou # 函数所在区域
  description: This is a function in ${app} application.
  environment: #  环境变量
    variables: #  环境变量对象
      TEST: value
  layers: #layer配置
    - name: scfLayer #  layer名称
      version: 1 #  版本
  events: # 触发器配置
    - timer: # 定时触发器
        parameters:
          cronExpression: '*/5 * * * * * *' # 每5秒触发一次
          enable: true
```

## 全量配置列表
目前 Serverless Framework 各个组件的全量配置信息列表如下：

### 基础组件
<style>
table th:nth-of-type(1) {
width: 150px;        
}
</style>
| 组件名称                   |    全量配置                           |  
| ----------------------- | ------------------------------------- | 
| SCF 组件     | [SCF - serverless.yml 全量配置](https://github.com/serverless-components/tencent-scf/blob/master/docs/configure.md)         |
| Website 组件  |[Website - serverless.yml 全量配置](https://github.com/serverless-components/tencent-website/blob/master/docs/configure.md)|      
| API 网关组件     | [API 网关 - serverless.yml 全量配置](https://github.com/serverless-components/tencent-apigateway/blob/master/docs/configure.md)                |      
| VPC 组件     | [VPC - serverless.yml 全量配置](https://github.com/serverless-components/tencent-vpc/blob/master/docs/configure.md)          |      
| COS 组件     | [COS - serverless.yml 全量配置](https://github.com/serverless-components/tencent-cos/blob/master/docs/configure.md)              |      
| PostgreSQL 组件   | [PostgreSQL - serverless.yml 全量配置](https://github.com/serverless-components/tencent-postgresql/blob/master/docs/configure.md)         |      
| CynosDB 组件     | [CynosDB - serverless.yml 全量配置](https://github.com/serverless-components/tencent-cynosdb/blob/master/docs/configure.md)             |      
| CDN 组件 | [CDN - serverless.yml 全量配置](https://github.com/serverless-components/tencent-cdn/blob/master/example/serverless.yml)           |
| Layer 组件    |[Layer - serverless.yml 全量配置](https://github.com/serverless-components/tencent-layer/blob/master/docs/configure.md)|

### 框架组件
<style>
table th:nth-of-type(1) {
width: 150px;        
}
</style>

| 组件名称                   |    全量配置                           |  
| ----------------------- | ------------------------------------- | 
| Express 组件     | [Express - serverless.yml 全量配置](https://github.com/serverless-components/tencent-express/blob/master/docs/configure.md) |
|  Koa 组件       | [Koa - serverless.yml 全量配置](https://github.com/serverless-components/tencent-koa/blob/master/docs/configure.md)         |      
| Egg 组件  | [Egg - serverless.yml 全量配置](https://github.com/serverless-components/tencent-egg/blob/master/docs/configure.md)   |      
| Next.js 组件  | [Next.js - serverless.yml 全量配置](https://github.com/serverless-components/tencent-nextjs/blob/master/docs/configure.md)   |
| Nuxt.js 组件 | [Nuxt.js - serverless.yml 全量配置](https://github.com/serverless-components/tencent-nuxtjs/blob/master/docs/configure.md) |
| Flask 组件 | [Flask - serverless.yml 全量配置](https://github.com/serverless-components/tencent-flask/blob/master/docs/configure.md) |
| Django 组件 | [Django - serverless.yml 全量配置](https://github.com/serverless-components/tencent-django/blob/master/docs/configure.md)|
|Laravel 组件|[Laravel - serverless.yml 全量配置](https://github.com/serverless-components/tencent-laravel/blob/master/docs/configure.md)|
|ThinkPHP 组件|[ThinkPHP - serverless.yml 全量配置](https://github.com/serverless-components/tencent-thinkphp/blob/master/docs/configure.md)|
