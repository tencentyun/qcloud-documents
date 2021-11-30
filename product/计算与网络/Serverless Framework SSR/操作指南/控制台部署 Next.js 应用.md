## 操作场景
Serverless SSR 为您提供了完整的控制台开发应用流程，该任务指导您通过 Serverless SSR 控制台部署 Next.js 应用。 


## 操作步骤
### 步骤1：创建应用
1. 登录 [Serverless SSR 控制台](https://console.cloud.tencent.com/ssr)。
2. 单击**新建应用** ，进入项目创建页面。 
3. 根据页面提示，填写应用基本信息。 
 - 应用名：2 - 63个字符，只能包含小写字母、数字及分隔符“-”、且必须以小写字母开头，数字或小写字母结尾。 创建后不可更改。 
 - 环境：选择 dev、test、prod 任一种方式，也支持自定义环境。 
 - 地域：与云函数支持地域相同，详情请参考 [地域列表](https://cloud.tencent.com/document/api/583/17238#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
 - 创建方式：支持 **[应用模版](#1)** 创建和 **[导入已有项目](#2)** 两种方式，您可以根据自己的实际情况，选择相应的创建方案。 
 >?
 >- 目前只支持 Next.js、Nuxt.js 两个框架的项目部署。 
 >- 导入已有项目时，如果您使用了 Express 等 web 框架替代默认的Web Server，需要做简单的改造，具体操作请参考 [自定义路由项目改造](https://cloud.tencent.com/document/product/1242/49214)。
4. 单击**创建**，Serverless SSR 将为您自动部署应用，您可以查看项目的部署日志。 

<span id="1"></span>
#### 应用模版创建

如果选择模版创建，您可以通过选择 Serverless SSR 提供的项目模版，快速创建一个 SSR 应用，模版部署时，Serverless SSR 将为默认您完成以下配置：
1. 新建层，并将项目依赖包 node_modules 存放在层中，层的使用请参考 [层管理](https://cloud.tencent.com/document/product/583/40159)。
2. 新建 COS 存储桶，拆分静态资源，将静态资源托管到 COS 桶中。 
![](https://main.qcloudimg.com/raw/33a09a5fcf29dce6cb97f512c1113744.png)

您还可以在**高级设置**部分，为您的项目进行静态资源存储、自定义域名、CDN 加速等高级能力的配置。 
![](https://main.qcloudimg.com/raw/6cd8a9b7b7bfd48aa3d3549cdc2104be.png)
>?配置自定义域名时，请确定您的域名已在腾讯云备案并配置了 CNAME 解析，详细步骤参考 [自定义域名配置](https://cloud.tencent.com/document/product/628/11791)。
 
 <span id="2"></span>
 #### 导入已有项目
 Serverless SSR 支持您通过**代码托管导入**和**文件夹上传**两种方式实现已有项目迁移，目前支持 Next.js 和 Nuxt.js 两个 SSR 框架。 
 
 - 代码托管
 目前支持 **GitHub、GitLab、Gitee** 的代码仓库地址，也支持公开的自定义代码库，您可以通过选择应用的触发方式，完成应用的自动更新，详情请参考 [项目触发方式管理]()。
 ![](https://main.qcloudimg.com/raw/120257e5c810fb9050965806f37fae0b.png)
 
 - 文件夹上传
 您可以通过上传文件夹的方式直接导入本地项目，Serverless SSR 将自动为您创建层，并将依赖包 node_modules 传入层中完成部署。 
 ![](https://main.qcloudimg.com/raw/3ad3998d05ec22d309b3fe60505f069c.png)


   
### 步骤2：资源管理
在 [Serverless 应用](https://console.cloud.tencent.com/ssr) 页面，单击目标 Next.js 应用进入应用详情页，查看项目部署后输出的基本信息、项目请求次数、项目报错统计等多项监控指标，方便您轻松实现项目的管理运维。 
<img src="https://main.qcloudimg.com/raw/b55916d9b944ce1281e5530c1db54115.png" width="770px">



### 步骤3：开发部署
在应用详情页顶部，单击**开发部署**，您可以轻松地实现应用的配置修改与二次部署上传，支持**本地上传、代码托管、CLI 开发**三种方式。 
<img src="https://main.qcloudimg.com/raw/5b727ac0d6715f339574e37d3580ac89.png" width="770px">


## 自定义路由项目改造指引

导入已有项目时，如果您的 Next.js 项目本身运行就是基于 express 自定义服务的，则您需要在项目中自定义入口文件  `sls.js`，或在控制台填入您自己的启动文件名，以下是一个模板文件：
```js
const express = require('express')
const next = require('next')

const app = next({ dev: false })
const handle = app.getRequestHandler()

// not report route for custom monitor
const noReportRoutes = ['/_next', '/static']

async function createServer() {
  await app.prepare()
  const server = express()

  server.all('*', (req, res) => {
    noReportRoutes.forEach((route) => {
      if (req.path.indexOf(route) !== -1) {
        req.__SLS_NO_REPORT__ = true
      }
    })
    return handle(req, res)
  })

  // define binary type for response
  // if includes, will return base64 encoded, very useful for images
  server.binaryTypes = ['*/*']

  return server
}

module.exports = createServer
```
