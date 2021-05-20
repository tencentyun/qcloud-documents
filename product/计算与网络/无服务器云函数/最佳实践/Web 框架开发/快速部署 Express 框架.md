## 操作场景
本文档指导您如何通过 Web 函数，快速迁移本地的 Express 服务上云。


## 前提条件
- 已注册腾讯云账户。若未注册腾讯云账户，可 [点此](https://cloud.tencent.com/register) 进入注册页面。
- 本地已安装 Nodejs 环境（[参考文档](https://nodejs.org/zh-cn/download/)）

## 操作步骤

### 本地开发

1. 初始化 Express 项目(可选)

   本地执行以下命令，快速创建一个 Express 项目，详情请参考 [Expressjs 项目官方文档](https://expressjs.com/en/starter/generator.html)。

   ```shell
   npx express-generator
   ```

   如果您本地已有项目，可跳过此步骤。

2. 安装依赖包

   进入您的项目目录，并安装相关依赖包：

   ```shell
   cd <Project-Folder>
   npm install
   ```

3. 本地运行项目

- 对于 MacOS or Linux 环境，执行以下命令：
  ```
  DEBUG=myapp:* npm start
  ```
- 对于 Windows 环境，执行以下命令：

  ```
  set DEBUG=myapp:* & npm start
  ```
  运行后，直接访问 http://localhost:3000/，即可本地查看您的项目

### 云端部署
1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，选择左侧导航栏【函数服务】，单击【新建】。如下图所示：
![img](https://main.qcloudimg.com/raw/7a98b47314a65145d88796f63fd73bff.png)

2. 在“新建函数”页面，选择 `自定义创建`，填写函数基础配置，如下图所示：
 - **函数类型**：选择 “Web 函数”。
 - **函数名称**：填写您自己的函数名称。
 - **地域**：填写您的函数部署地域，默认为广州。
 - **运行环境**：选择 “Nodejs 12.16”。
 - **部署方式**：选择“代码部署”，上传您的本地项目。
   >! 上传前，注意将您项目里的监听端口改为 `9000`，否则函数无法正常运行

![img](https://main.qcloudimg.com/raw/37d8e9e48b950c1dc09789e2ea14a4f6.png)

3. 在"高级配置"部分，配置启动命令文件，可以选择 SCF 为您提供的默认 Express 框架模版，也可以基于您的实际项目情况，编写您自己的启动命令。
   ![](https://main.qcloudimg.com/raw/96cc689acdcacab22b56d164e5e11a3b.png)

### 函数管理
部署成功后，您可以在函数的控制台管理页面，查看函数详细信息，并通过访问生成的 URL 进行测试

![](https://main.qcloudimg.com/raw/3a30036df613ab16506caa4a97676363.png)
