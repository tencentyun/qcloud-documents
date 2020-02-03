## 创建 Nodejs Express 项目
1. 根据实际需求，选择目录路径，并在该路径下创建新的目录，用作于项目目录。
   例如，创建一个名称为 helloexpress 的项目目录。
2. 进入 helloexpress 目录，并在该目录下执行以下命令，初始化 node 项目。
```bash
npm init
```
>? 命令执行后所有选项均保持默认即可。
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
>?服务需要监听8080端口。
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
7.  打包本地项目，准备上传。
**您需要在项目的根路径（start.sh 所在路径）下执行打包**。您可以在 [TSF  Serverless 使用须知](https://cloud.tencent.com/document/product/649/38960#.E4.B8.8A.E4.BC.A0.E7.A8.8B.E5.BA.8F.E5.8C.85.E8.A6.81.E6.B1.82) 查看程序包的要求。
```bash
zip code.zip * -r
```

## 创建 Hello World 服务
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf)，选择地域（本文以广州为例）。
2. 在左侧导航栏，选择【[应用管理](https://console.cloud.tencent.com/tsf/app?rid=1)】，单击【新建应用】。
3. 在【新建应用】页面，填写应用基本信息，单击【提交】。
 - **应用名**：填写 helloexpress。
 - **部署方式**：选择"Serverless部署"。
  使用 Serverless 部署，用户不需要关系应用部署的计算资源，系统自动提供资源调度、资源计算、弹性伸缩能力。
 - **运行环境**：TSF Serverless目前仅支持 Nodejs8.9。
 - **备注**：填写备注信息。
4. 应用创建完成后，按照提示前往【程序包管理】上传程序包。
![](https://main.qcloudimg.com/raw/f0ab9af0dcad281051ee4ecb24016301.png)
5. 单击【上传程序包】，填写基本信息，单击【提交】。
![](https://main.qcloudimg.com/raw/baa94f117949086b7665a1854f51d51c.png)
 - **上传程序包**：之前在本地打包完成的压缩包。您可以在 [这里](链接到tsf serverless使用须知的上传程序包要求) 查看程序包的要求。
 - **程序包版本**：填写版本信息。
 - **备注**：填写备注信息。
6. 程序包上传完成后，前往【部署组】创建部署组。
![](https://main.qcloudimg.com/raw/63f50aaf7a50823b3960b908e50a58ba.png)
7. 选择之前上传的程序包，创建新的部署组。
 - 部署组可以认为是一个特定版本程序的部署实例。一个应用可以有多个部署组，从而实现版本灰度发布。
 - 当前 TSF Serverless 尚未支持版本灰度功能，所以限制一个应用只能有一个部署组。后续会放开限制。
![](https://main.qcloudimg.com/raw/211d0a9b418379440bba1821c4715ce8.png)
 * **名称**：填写部署组名称。
 * **选择程序包**：选择之前上传的程序包。
 * **开启访问 VPC**：如果**您的程序需要访问 VPC 内云资源，例如访问 VPC 内的数据库**，那么您可以开启访问 VPC，并配置 VPC 信息。
8. 部署组创建完成后，您可以在【访问管理】配置外网访问。
![](https://main.qcloudimg.com/raw/55c0ca30e160ac1d35fbc82452cb2cbb.png)
TSF Serverless 的外网访问是通过关联创建 API 网关实现的。**您可以前往 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) 查看关联创建的 API 网关资源，并在 API 网关控制台使用其他高级功能，如自定义域名**。
9. 您可以单击部署组操作栏的【部署应用】来更新部署组的程序包版本。
![](https://main.qcloudimg.com/raw/f5d47e1c5db8c8aaa3dd8e733e18ab76.png)
10. 您可以单击部署组操作栏的【查看日志】来查看实时日志和历史日志。
 * **实时日志**：当【自动刷新】开启时，将从**当前时刻起拉取实时日志（当前时刻之前的日志不显示）**。
 * **历史日志**：关闭【自动刷新】后，可以选择时间段查看历史日志。
11. 您可以单击【监控信息】来查看监控数据。当前支持以下维度的监控：
 * 请求数（次）：请求次数。
 * 请求耗时（ms）：请求的整体耗时，单位为 ms。
 * 前台错误数（次）：这里是 API 网关的概念，前台错误数是请求未到达后端Serverless应用即出 现的错误的请求数量（4xx、5xx）。
 * 后台错误数（次）：这里是 API 网关的概念，后台错误数是由用户的业务代码直接返回错误的请求数量（4xx、5xx）。
 * 长连接数（条）：TCP 长连接数。



