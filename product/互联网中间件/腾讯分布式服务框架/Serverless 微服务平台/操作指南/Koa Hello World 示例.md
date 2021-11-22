>?
>- TSF Serverless 是微服务的应用托管平台，主要支持东西向微服务框架（如 Spring Cloud 和 Service Mesh）。
>- Web 服务（Express、Koa）推荐使用 [Serverless 应用中心](https://cloud.tencent.com/product/sls)。

## 操作步骤
1. 根据实际需求，选择目录路径，并在该路径下创建新的目录，用作于项目目录。
   例如，创建一个名称为 hellokoa 的项目目录。
2. 进入 hellokoa 目录，并在该目录下执行以下命令，初始化 node 项目。
```bash
npm init
```
>?命令执行后所有选项均保持默认即可。
3. 执行以下命令，安装 Koa 包。
```bash
npm install koa --save
```
4. 在项目目录下创建文件 index.js，并输入以下内容：
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
7.  打包本地项目，准备上传。您需要在项目的根路径（start.sh所在路径）下执行打包。
```bash
zip code.zip * -r
```
8. 创建服务步骤同 [Express 示例项目的创建 Hello World 服务](https://cloud.tencent.com/document/product/649/38963#.E5.88.9B.E5.BB.BA-hello-world-.E6.9C.8D.E5.8A.A1)。

