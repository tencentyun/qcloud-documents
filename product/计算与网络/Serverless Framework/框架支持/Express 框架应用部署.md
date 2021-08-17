
应用中心框架部署方案已经全新升级，您可以通过 `SCF Web Function`，快速部署您的 Express 业务上云。

>! **应用控制台部署与函数直接部署有什么区别？**
通过应用部署或函数部署，均可以基于 Web 函数，快速部署常见 Web 框架。
- 如果您只关注代码逻辑开发，无需额外资源创建，可以通过 SCF 云函数控制台，完成快速部署。
- 如果除了代码部署外，您还需要更多能力或资源创建，如自动创建层托管依赖、一键实现静态资源分离、支持代码仓库直接拉取等，可以通过应用控制台，完成 Web 应用的创建工作。

本篇文档为您介绍应用控制台的部署方案，您也可以通过命令行完成部署，具体操作请参考 [产品文档](https://cloud.tencent.com/document/product/583/58183)。

## 模版部署 -- 部署 Express 示例代码
1. 登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)。
2. 选择**Web 应用>Express 框架**，如下图所示：
![](https://main.qcloudimg.com/raw/0f10503bf4936081ceddaa46cfa78333.png)
3. 单击“下一步”，完成基础配置选择。
![](https://main.qcloudimg.com/raw/9f22f8c1e5426b5d3d54631caabde012.png)
4. 上传方式，选择**示例代码**直接部署，单击**完成**，即可开始应用的部署。
5. 部署完成后，您可在应用详情页面，查看示例应用的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Express 项目。
![](https://main.qcloudimg.com/raw/d17b4eed35144ba019429a114601cb9a.png)

## 自定义部署 -- 快速部署 Web 应用
### 前提条件

本地已安装 Node.js 运行环境。

### 本地开发
1. 首先，在确保您的本地已安装 Node.js 运行环境后，安装 Express 框架和 express-generator 脚手架，初始化您的 Express 示例项目。
```shell
npm install express --save
npm install express-generator --save
express WebApp
```

2. 进入项目目录，安装依赖包。
```
cd WebApp
npm install
```

3. 安装完成后，本地直接启动，在浏览器里访问 `http://localhost:3000`，即可在本地完成 Express 示例项目的访问。
```
npm start
```

### 部署上云

接下来，我们对已初始化的项目进行简单修改，使其可以通过 Web Function 快速部署，此处项目改造通常分为两步：

- 修改监听地址与端口，改为 `0.0.0.0:9000`
- 新增 `scf_bootstrap` 启动文件

具体步骤如下：
1. 已知在 Express 示例项目中，通过 `./bin/www` 设置监听地址与端口，打开该文件可以发现，我们可以通过环境变量，设置指定监听端口，否则将自动监听 `3000`。
![](https://main.qcloudimg.com/raw/a32fd560e9a6e58e6a1f6a46356324e6.png)

2. 接下来，在项目根目录下新建 `scf_bootstrap` 启动文件，在里面配置环境变量，并指定服务启动命令。
 >? 您也可以在控制台完成该模块配置

```shell
#!/bin/bash
export PORT=9000
npm run start
```
创建完成后，注意修改您的可执行文件权限，默认需要 `777` 或 `755` 权限才可以正常启动。
```
chmod 777 scf_bootstrap
```
3. 本地配置完成后，执行启动文件，确保您的服务可以本地正常启动，接下来，登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)，选择**Web 应用>Express 框架**，上传方式可以选择**本地上传**或**代码仓库拉取**。

您可以在控制台完成启动文件 `scf_bootstrap` 内容配置，配置完成后，控制台将为您自动生成 启动文件，和项目代码一起打包部署。
>! 启动文件以项目内文件为准，如果您的项目里已经包含 `scf_bootstrap` 文件，将不会覆盖该内容。

配置完成后，单击**完成**，部署您的 Express 项目。
![](https://main.qcloudimg.com/raw/a28efc9156bc3ba9ab817be16a463a02.png)
