应用中心框架部署方案已经全新升级，您可以通过 `SCF Web Function`，快速部署您的 Nest.js 业务上云。


>! **应用控制台部署与函数直接部署有什么区别？**
通过应用部署或函数部署，均可以基于 Web 函数，快速部署常见 Web 框架。
- 如果您只关注代码逻辑开发，无需额外资源创建，可以通过 SCF 云函数控制台，完成快速部署。
- 如果除了代码部署外，您还需要更多能力或资源创建，如自动创建层托管依赖、一键实现静态资源分离、支持代码仓库直接拉取等，可以通过应用控制台，完成 Web 应用的创建工作。


## 前提条件
- 在使用腾讯云云函数服务之前，您需要 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
  
>! 本文档主要介绍控制台部署方案，您也可以通过命令行完成部署，请参考具体操作请参考 [产品文档](https://cloud.tencent.com/document/product/583/58183)。

## 操作步骤

### 模版部署 -- 部署 Nest.js 示例代码
1. 登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)。
2. 选择**Web 应用>Nest.js 框架**，如下图所示：
![](https://main.qcloudimg.com/raw/2ad8857337c06a56df2f5bfd733b40b3.png)
3. 单击“下一步”，完成基础配置选择
![](https://main.qcloudimg.com/raw/9f22f8c1e5426b5d3d54631caabde012.png)
4. 上传方式，选择**示例代码**直接部署，单击**完成**，即可开始应用的部署。
5. 部署完成后，您可在应用详情页面，查看示例应用的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Nest.js 项目
![](https://main.qcloudimg.com/raw/3f58b9b4fb41611ef57a7863a36e2a3b.png)


### 自定义部署 -- 快速部署 Web 应用
#### 前提条件

本地已安装 Node.js 运行环境。

#### 本地开发

1. 参考 [Nest.js](https://nestjs.bootcss.com/first-steps) 官方文档，初始化您的 Nest.js 项目：
```sh
npm i -g @nestjs/cli
nest new nest-app
```
2. 在根目录下，执行以下命令在本地直接启动服务。
```shell
cd nest-app && npm run start
```
3. 打开浏览器访问 `http://localhost:3000`，即可在本地完成 Nest.js 示例项目的访问。
![](https://main.qcloudimg.com/raw/cff5858199e1433f793022572903b134.png)

#### 部署上云

接下来执行以下步骤，对已初始化的项目进行简单修改，使其可以通过 Web Function 快速部署，此处项目改造通常分为以下两步：

- 新增 `scf_bootstrap` 启动文件。
- 修改监听地址与端口为 `0.0.0.0:9000`。

具体步骤如下：
1. 修改启动文件`./dist/main.js`，监听端口改为`9000`:
![](https://main.qcloudimg.com/raw/4f32f01747c5868a89d513f7ff8e91f2.png)

2. 在项目根目录下新建 `scf_bootstrap` 启动文件，在该文件添加如下内容（用于启动服务）：
>? 您也可以在控制台完成该模块配置。
>
```sh
#!/bin/bash

SERVERLESS=1 /var/lang/node12/bin/node ./dist/main.js
```

>! 
1. 此处仅为示例启动文件，具体请根据您的业务场景进行调整。
2. 示例使用的是云函数标准 node 环境路径，本地调试时，注意修改成您的本地路径。
>

新建完成后，还需执行以下命令修改文件可执行权限，默认需要 `777` 或 `755` 权限才可正常启动。示例如下：
```sh
chmod 777 scf_bootstrap
```
3. 本地配置完成后，执行启动文件，确保您的服务可以本地正常启动，接下来，登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)，选择**Web 应用>Nest.js 框架**，上传方式可以选择**本地上传**或**代码仓库拉取**。

您可以在控制台完成启动文件 `scf_bootstrap` 内容配置，配置完成后，控制台将为您自动生成 启动文件，和项目代码一起打包部署。
>! 启动文件以项目内文件为准，如果您的项目里已经包含 `scf_bootstrap` 文件，将不会覆盖该内容。
>

配置完成后，单击**完成**，部署您的 Nest.js 项目。
![](https://main.qcloudimg.com/raw/a28efc9156bc3ba9ab817be16a463a02.png)
