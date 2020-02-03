1. 根据实际需求，选择目录路径，并在该路径下创建新的目录，用作于项目目录。
   例如，创建一个名称为 helloegg 的项目目录。
2. 进入 helloegg 目录，并在该目录下依次执行以下命令，使用脚手架初始化一个 Egg 项目。
```bash
npm init egg --type=simple
npm i
```
> ?命令执行后所有选项均保持默认即可。
3. 由于 egg 默认监听的端口是7001，我们需要修改配置文件来使应用监听 8080 端口。
   在 config 文件夹下找到 **config.default.js** 文件，添加如下代码：
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
6. 打包本地项目，准备上传。您需要在项目的根路径（start.sh 所在路径）下执行打包。
```bash
zip code.zip * -r
```
7. 创建服务步骤同 [创建 Hello World 服务](https://cloud.tencent.com/document/product/649/38963#.E5.88.9B.E5.BB.BA-hello-world-.E6.9C.8D.E5.8A.A1)。
