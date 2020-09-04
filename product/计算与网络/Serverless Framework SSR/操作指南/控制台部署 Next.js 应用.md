## 操作场景
Serverless SSR 为您提供了完整的控制台开发应用流程，该任务指导您通过 Serverless SSR 控制台部署 Next.js 应用。


## 操作步骤
### 创建应用
1. 登录 [Serverless SSR 控制台](https://console.cloud.tencent.com/ssr)。
2. 单击【新建应用】 ，进入项目创建页面。
3. 根据页面提示，填写应用基本信息。
 - 应用名：2 - 63个字符，只能包含小写字母、数字及分隔符“-”、且必须以小写字母开头，数字或小写字母结尾。
 - 环境：选择 dev、test、prod 任一种方式。
 - 创建方式：支持**应用模版**创建和 zip 包**导入已有项目** 两种方式，您可以根据自己的实际情况，选择相应的创建方案。
 >?
 >- 目前 zip 包只支持 Next.js、Nuxt.js 两个框架的项目上传。
 >- 导入已有项目时，必须先在本地通过 `npm run build` 指令构建好静态资源后才能打包上传。
 >- 压缩项目时注意项目的打包路径，只打包项目根目录里的所有文件，如果连同根目录一同打包可能会造成解压失败。
 
![](https://main.qcloudimg.com/raw/aa8fd46990b2a77f12bbd2746a89d2a8.png)
您还可以在【高级配置】部分，为您的项目进行静态资源存储、自定义域名、CDN 加速等高级能力的配置。
![](https://main.qcloudimg.com/raw/2170428dc6aa1140190f03e1df425975.png)
4. 单击【创建】，已创建的应用信息将显示在 Serverless 应用页面。

   
### 管理应用
在 [Serverless 应用](https://console.cloud.tencent.com/ssr) 页面，单击目标 Next.js 应用进入应用详情页，查看项目部署后输出的基本信息、项目请求次数、项目报错统计等多项监控指标，方便您轻松实现项目的管理运维。
 ![](https://main.qcloudimg.com/raw/ba6142ec15457cd99d944281bf8e5fcc.png)


### 下载代码
通过应用详情页的【下载代码】，您可轻松地将代码下载到本地进行二次开发，开发完成后，通过控制台完成重新上传。
>?
>- 本地代码上传时，必须先在本地通过 `npm run build` 指令构建好静态资源后才能打包上传。
>- 压缩项目时注意项目的打包路径，只打包项目根目录里的所有文件，如果连同根目录一同打包可能会造成解压失败。

 ![](https://main.qcloudimg.com/raw/82076e1fcbceedc4f6055174606257ed.png)  

## 本地项目迁移指引
#### Next.js
您可以通过上传 zip 包的方式，将您的本地项目迅速部署到云端，如果您的 Next.js 项目本身运行就是基于 express 自定义服务的，则您需要在项目中自定义入口文件 sls.js，需要参考您的服务启动文件进行修改。以下是一个模板文件：
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
