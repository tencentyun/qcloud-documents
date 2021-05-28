## 操作场景
本文档指导您如何通过 Web 函数，快速迁移本地的 Express 服务上云。


## 前提条件
- 在使用腾讯云容器服务之前，您需要 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
- 本地已安装 Nodejs 环境，请参见 [官方文档](https://nodejs.org/zh-cn/download/)。

## 操作步骤

### 本地开发

#### 初始化 Express 项目（可选）
本地执行以下命令，快速创建一个 Express 项目。项目详情请参见 [Expressjs 项目官方文档](https://expressjs.com/en/starter/generator.html)。
```shell
npx express-generator
```
 如果您的本地已有项目，可跳过此步骤。
 
#### 安装依赖包
执行以下命令，进入您的项目目录，并安装相关依赖包。
```shell
cd <Project-Folder>
npm install
```

#### 本地运行项目
- 对于 MacOS or Linux 环境，执行以下命令：
```
DEBUG=myapp:* npm start
```
- 对于 Windows 环境，执行以下命令：
```
set DEBUG=myapp:* & npm start
```

运行后，访问 http://localhost:3000/ ，即可在本地查看您的项目。

### 云端部署
1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏的【函数服务】。
2. 在主界面上方选择期望创建函数的地域，并单击【新建】，进入函数创建流程。
3. 在“新建函数”页面，选择【自定义创建】，并填写函数基础配置。
 - **函数类型**：选择 “Web 函数”。
 - **函数名称**：填写您自己的函数名称。
 - **地域**：填写您的函数部署地域，默认为广州。
 - **运行环境**：选择 “Nodejs 12.16”。
 - **部署方式**：选择“代码部署”，上传您的本地项目。
 <dx-alert infotype="notice" title="">
上传本地项目前，您需要将项目中的监听端口改为`9000`，否则函数无法正常运行。
</dx-alert>
4. 在"高级配置"中，配置启动命令文件。您可以选择 SCF 为您提供的默认 Express 框架模版，也可以基于您的实际项目情况，编写您自己的启动命令。
5. 在"触发器配置"中，触发器目前只支持 API 网关触发，将自动按照默认配置创建触发器。
6. 单击【完成】，即可创建函数。




### 函数管理

函数创建完成后，您可在“函数管理”页面，查看函数的基本信息，并通过 API 网关生成的访问路径 URL 进行访问。

