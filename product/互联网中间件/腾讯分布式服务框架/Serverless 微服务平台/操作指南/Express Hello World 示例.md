> ?
>
> - TSF Serverless 是微服务的应用托管平台，主要支持东西向微服务框架（如 Spring Cloud 和 Service Mesh）。
> - Web 服务（Express、Koa）推荐使用 [Serverless Framework](https://cloud.tencent.com/product/sls)。

## 创建 Nodejs Express 项目

1. 根据实际需求，选择目录路径，并在该路径下创建新的目录，用作于项目目录。
   例如：创建一个名称为 helloexpress 的项目目录。
2. 进入 helloexpress 目录，并在该目录下执行以下命令，初始化 node 项目。
```bash
npm init
```
>?命令执行后所有选项均保持默认即可。

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

5. 在项目目录下创建 start.sh 启动脚本文件，并输入以下内容：
```bash
#! /bin/bash
node index.js
```

6. 执行以下命令，进行项目的本地验证。
```bash
/bin/bash start.sh
```
显示结果如下，则说明服务已启动。
```bash
listening port 8080
Example app listening on 8080
```

 在浏览器地址栏输入 `localhost:8080` 后访问，窗口显示 `Hello World!`，本地创建项目成功。

7. 打包本地项目，准备上传。
   **您需要在项目的根路径（start.sh 所在路径）下执行打包**。您可以在 [TSF  Serverless 使用须知](https://cloud.tencent.com/document/product/649/38960#.E4.B8.8A.E4.BC.A0.E7.A8.8B.E5.BA.8F.E5.8C.85.E8.A6.81.E6.B1.82) 查看程序包的要求。
```bash
zip code.zip * -r
```

## 创建 Hello World 服务

### 步骤1：新建 Serverless 集群[](id:step1)

首先您需要创建 Serverless 集群。集群是实例、Serverless 等云资源的集合。

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧导航栏中，单击**集群**，进入集群列表页。
3. 在集群列表页，单击**新建集群**。
4. 设置集群的基本信息。
	- **集群类型**：选择 **Serverless集群**。
	- **集群名称**：集群名称，不超过60个字符。
	- **集群网络**：为集群内主机分配在云服务器网络地址范围内的 IP 地址。参阅 [私有网络和子网](https://cloud.tencent.com/document/product/215/20046)。
	- **集群描述**：集群的描述，不超过200个字符。

### 步骤2：创建 Serverless 应用

1. 在左侧导航栏，单击 **[应用管理](https://console.cloud.tencent.com/tsf/app?rid=1)**，进入应用列表。
2. 在应用列表上方单击**新建应用**。
3. 设置应用信息后，单击**提交**。
   - 部署方式：选择 **Serverless部署**
   - 运行环境：选择 **Nodejs** 

### 步骤3：上传程序包[](id:step3)

1. 在 [应用管理列表](https://console.cloud.tencent.com/tsf/app) 页 ，单击目标应用的**ID/应用名**，进入应用详情页。
2. 在应用详情页的上方，单击**程序包管理**标签页，单击**上传程序包**。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/be1deb9761e7bd651cac8c7a561277eb.png)
3. 在**上传程序包**对话框中填写相关参数。
	- 上传程序包：单击**选择文件**，选择编译为 jar 格式的程序包
	- 程序包版本：填写版本号，或单击**用时间戳作为版本号**
	- 备注：填写备注  
4. 单击**提交**，程序包上传成功后出现在程序包列表中。

### 步骤4：创建部署组并添加实例

1. 在 [应用管理列表](https://console.cloud.tencent.com/tsf/app) 页 ，单击目标应用的**ID/应用名**，进入应用详情页。
2. 单击**新建部署组**，设置部署组相关信息：
	- 部署组名称：部署组的名称，不超过60个字符。
	- 集群：选择 [步骤1](#step1) 中创建的集群。
	- 命名空间：选择集群关联的系统命名空间。
	- 日志配置项：应用的日志配置项用于指定 TSF 采集应用的日志路径。参考 [日志服务](https://cloud.tencent.com/document/product/649/13697)。
3. 单击**提交**。

### 步骤5：部署应用

1. 在上步操作中单击**下一步**即可完成部署，如部署失败，可在部署组列表页的右侧，单击**部署应用**重试。
   ![](https://main.qcloudimg.com/raw/ee0e779344c6f058fd181fb24c8582bc.png)
2. 选择 [步骤3](#step3) 中已上传成功的程序包后，单击**提交**。
3. 应用部署成功后，部署组中**运行实例数**的数值发生变化。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/496b6bf194126fa102a6c1ea8306a3d8.png)
