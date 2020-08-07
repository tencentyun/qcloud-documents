通过 [Serverless SSR 控制台]()，您可以快速创建与部署您的 SSR 项目，部署流程如下:

### 1. 创建项目
   
   点击 “新建应用” ，进入项目创建页面，目前 Serverless 控制台支持 **模版创建** 与 **zip 包上传** 两种项目部署方式，您可以根据自己的实际情况，选择相应的创建方案：
    ![image](https://github.com/Jiachen0417/MarkDownPics/blob/master/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-08-06%2009.53.14.png)
   
   您还可以在“高级配置”部分，为您的项目进行静态资源存储、自定义域名、CDN 加速等高级能力的配置：
   
   <img src="https://github.com/Jiachen0417/MarkDownPics/blob/master/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-08-06%2009.57.11.png" width = "60%" />
   
   > 注意：目前 zip 包只支持 Next.js、Nuxt.js 两个框架的项目上传
   
### 2. 项目管理，监控运维
    
   创建成功后，您可以在“项目详情”页面查看项目部署后输出的基本信息，并查看项目请求次数、项目报错统计等多项监控指标，方便您轻松实现项目的管理运维。
   
   <img src="https://github.com/Jiachen0417/MarkDownPics/blob/master/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-08-06%2010.06.46.png" width = "60%" />

### 3. 下载代码，二次开发
   
   通过应用详情页的 **“下载代码”** 按钮，您可轻松地将代码下载到本地进行二次开发，开发完成后，通过控制台完成重新上传
   

### 本地项目迁移指引
#### Next.js

您可以通过上传 zip 包的方式，将您的本地项目迅速部署到云端，如果你的 Next.js 项目本身运行就是基于 express 自定义服务的，那么你需要在项目中自定义入口文件 sls.js，需要参考你的服务启动文件进行修改，以下是一个模板文件：

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
