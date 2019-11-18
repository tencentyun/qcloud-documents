> TSF Serverless目前出于内测阶段，欢迎填写[使用申请](https://cloud.tencent.com/apply/p/om62iz2gqx)。

您可以通过[TSF Serverless 简介](xxxx)、[使用须知](xxxx)了解更多信息。

## 操作场景

本文旨在通过 Express、Koa 和 Egg 的 Hello World 示例介绍 TSF Serverless 的使用方法，帮助您了解 TSF Serverless 的基本使用流程和控制台的基本操作。例如创建应用、上传程序包、创建部署组、配置外网访问和查看运行日志和监控。

您可以结合示例步骤进行项目开发，服务创建及访问验证。本文示例步骤如下：

1. 使用 Node.js Web 框架（Express、Koa、Egg）在本地完成项目开发和本地测试。
2. 在 TSF 控制台创建Serverless应用，并上传打包后的项目代码。
3. 创建部署组并开启外网访问，验证服务的运行情况。

## 前提条件

 - 本地已安装 [Node.js](https://nodejs.org/)。
 - 已开通 TSF Serverless 白名单。点此[申请开通](https://cloud.tencent.com/apply/p/om62iz2gqx)。


## 操作步骤

### Express Hello World 示例

#### 创建 Nodejs Express 项目

1. 根据实际需求，选择目录路径，并在该路径下创建新的目录，用作于项目目录。
   例如，创建一个名称为 helloexpress 的项目目录。
2. 进入 helloexpress 目录，并在该目录下执行以下命令，初始化 node 项目。

```bash
npm init
```

> 命令执行后所有选项均保持默认即可。

3. 执行以下命令，安装 Express 包。

```bash
npm install express --save
```

4. 在项目目录下创建 index.js 文件，并输入以下内容：

```javascript
const express = require('express')
const app = express()
app.get('/', (req, res) => res.send('Hello World!'))
const port = 8080
console.log('listening port',port)
app.listen(port, () => console.log('Example app listening on',port))
```

>  服务需要监听8080端口。

5.  在项目目录下创建 start.sh 启动脚本文件，并输入以下内容：

```bash
#! /bin/bash

node index.js
```

6.  执行以下命令，进行项目的本地验证。

```bash
/bin/bash start.sh
```

显示结果如下，则说明服务已启动。

```bash
listening port 8080
Example app listening on 8080
```

在浏览器地址栏输入 `localhost:8080` 后访问，窗口显示 `Hello World!`，本地创建项目成功。

7.  打包本地项目，准备上传。**您需要在项目的根路径（start.sh所在路径）下执行打包**。您可以在[这里](链接到tsf serverless使用须知的上传程序包要求)查看程序包的要求。
```bash
zip code.zip * -r
```

#### 创建 Hello World 服务

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)，选择地域（本文以广州为例）。
2. 选择左侧导航栏【应用管理】，单击【新建应用】。如下图所示：
   ![](https://main.qcloudimg.com/raw/33412f865526c045a594f6f7cabd9647.png)
3. 在【新建应用】页面，填写应用基本信息，单击【提交】。如下图所示：

 - **应用名**：填写 helloexpress。

 - **部署方式**：选择"Serverless部署"。

  > 使用Serverless部署，用户不需要关系应用部署的计算资源，系统自动提供资源调度、资源计算、弹性伸缩能力

 - **运行环境**：TSF Serverless目前仅支持Nodejs 8.9。
 - **备注**：填写备注信息。

4. 应用创建完成后，按照提示前往【程序包管理】上传程序包。如下图所示：

![](https://main.qcloudimg.com/raw/e396d6da043a769f7d79eb425548065f.png)

5. 点击【上传程序包】，填写基本信息，点击【提交】。如下图所示：

![](https://main.qcloudimg.com/raw/00421be1f15b258bf9fef1d4daaca863.png)

* **上传程序包**：之前在本地打包完成的压缩包。您可以在[这里](链接到tsf serverless使用须知的上传程序包要求)查看程序包的要求。
* **程序包版本**：填写版本信息。
* **备注**：填写备注信息。

6. 程序包上传完成后，前往【部署组】创建部署组。如下图所示：

![](https://main.qcloudimg.com/raw/4ef52680d0643412ea0175022f6f32cf.png)

7. 选择之前上传的程序包，创建新的部署组。如下图所示：

![](https://main.qcloudimg.com/raw/ec2abdf2d4c80842d65e0177df51c045.png)

> 部署组可以认为是一个特定版本程序的部署实例。一个应用可以有多个部署组，从而实现版本灰度发布。
>
> 当前TSF Serverless尚未支持版本灰度功能，所以限制一个应用只能有一个部署组。后续会放开限制。

* **名称**：填写部署组名称。
* **选择程序包**：选择之前上传的程序包。
* **开启访问VPC**：如果**您的程序需要访问VPC内云资源，例如访问VPC内的数据库**，那么您可以开启访问VPC，并配置VPC信息。

8. 部署组创建完成后，你可以在【访问管理】配置外网访问。如下图所示：

![](https://main.qcloudimg.com/raw/014586e748d986d8179750f0eabec61b.png)

> TSF Serverless的外网访问是通过关联创建API网关实现的。**您可以前往API网关控制台查看关联创建的API网关资源，并在API网关控制台使用其他高级功能，如自定义域名**。

![](https://main.qcloudimg.com/raw/2f728b5bf99fe5db16dd7e2f1b597ae9.png)

9. 您可以通过【部署应用】来更新部署组的程序包版本。如下图所示：

![](https://main.qcloudimg.com/raw/52138bd09e72f735b177bae715d38853.png)

10. 您可以点击部署组操作栏的【查看日志】来查看实时日志和历史日志。如下图所示：

![](https://main.qcloudimg.com/raw/52138bd09e72f735b177bae715d38853.png)

* **实时日志**：当【自动刷新】开启时，将从**当前时刻起拉取实时日志（当前时刻之前的日志不显示）**。
* **历史日志**：关闭【自动刷新】后，可以选择时间段查看历史日志。

11. 您可以点击【监控信息】来查看监控数据。当前支持：

* 请求数（次）：请求次数。
* 请求耗时（ms）：请求的整体耗时，单位ms。
* 前台错误数（次）：这里是API网关的概念，前台错误数是请求未到达后端Serverless应用即出现的错误的请求数量（4xx、5xx）
* 后台错误数（次）：这里是API网关的概念，后台错误数是由用户的业务代码直接返回错误的请求数量（4xx、5xx）
* 长连接数（条）：TCP长连接数。

### Koa Hello World 示例

1. 根据实际需求，选择目录路径，并在该路径下创建新的目录，用作于项目目录。
   例如，创建一个名称为 hellokoa 的项目目录。
2. 进入 hellokoa 目录，并在该目录下执行以下命令，初始化 node 项目。

```bash
npm init
```

> 命令执行后所有选项均保持默认即可。

3. 执行以下命令，安装 Koa 包。

```bash
npm install koa --save
```

4. 在项目目录下创建文件 index.js，并输入以下内容

```javascript
const koa = require('koa')
const app = new koa()
app.use(async ctx => {
    ctx.body = 'Hello World';
});
const port = 8080
console.log('listening port',port)
app.listen(port, () => console.log('Example app listening on',port))
```

> 服务需要监听8080端口。

5.  在项目目录下创建 start.sh 启动脚本文件，并输入以下内容：

```bash
#! /bin/bash

node index.js
```

6.  执行以下命令，进行项目的本地验证。

```bash
/bin/bash start.sh
```

显示结果如下，则说明服务已启动。

```bash
listening port 8080
Example app listening on 8080
```

在浏览器地址栏输入 `localhost:8080` 后访问，窗口显示 `Hello World!`，本地创建项目成功。

7.  打包本地项目，准备上传。您需要在项目的根路径（start.sh所在路径）下执行打包。

```bash
zip code.zip * -r
```

8. 创建服务步骤同 [Express示例项目的创建 Hello World 服务](#create)。

### Egg Hello World 示例

1. 根据实际需求，选择目录路径，并在该路径下创建新的目录，用作于项目目录。
   例如，创建一个名称为 helloegg 的项目目录。
2. 进入 helloegg 目录，并在该目录下依次执行以下命令，使用脚手架初始化一个 egg 项目。

```bash
npm init egg --type=simple
npm i
```

> 命令执行后所有选项均保持默认即可。

3. 由于egg默认监听的端口是7001，我们需要修改配置文件来使应用监听8080端口。

   在config文件夹下找到**config.default.js**文件，添加如下代码：

```javascript
config.cluster = {
  listen: {
    path: '',
    port: 8000,
    hostname: '0.0.0.0',
  }
};
```

4. 在项目目录下创建 start.sh 启动脚本文件，并输入以下内容：

```bash
#! /bin/bash

npm run dev
```

5. 执行以下命令，进行项目的本地验证。

```bash
/bin/bash start.sh
```

显示结果如下，则说明服务已启动。

```bash
2019-11-01 18:03:21,744 INFO 53687 [master] agent_worker#1:53689 started (676ms)
2019-11-01 18:03:22,535 INFO 53687 [master] egg started on http://0.0.0.0:8000 (1469ms)
```

在浏览器地址栏输入 `localhost:8080` 后访问，窗口显示 `hi, egg`，本地创建项目成功。

6. 打包本地项目，准备上传。您需要在项目的根路径（start.sh所在路径）下执行打包。

```bash
zip code.zip * -r
```

7. 创建服务步骤同 [创建 Hello World 服务](#create)。