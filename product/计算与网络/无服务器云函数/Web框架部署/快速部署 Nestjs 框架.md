## 操作场景

本文将为您指导如何通过 Web Function，将您的本地 Nest.js 项目快速部署到云端。


>?本文档主要介绍控制台部署方案，您也可以通过命令行完成部署，详情请参见 [通过命令行完成框架部署](https://cloud.tencent.com/document/product/583/59439)。


## 前提条件
在使用腾讯云云函数服务之前，您需要 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。



## 操作步骤

### 模版部署 -- 一键部署 Nest.js 项目

1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
2. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
3. 选择使用**模版创建**来新建函数，在搜索框里输入 `nest` 筛选函数模版，选择**Nest框架模版**并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/78fac7caa422b20739c552b210fe820e.png)
4. 在**新建**页面，您可以查看模版项目的具体配置信息并进行修改。
5. 单击**完成**即可创建函数。函数创建完成后，您可在**函数管理**页面查看 Web 函数的基本信息。
6. 您可以通过 API 网关生成的访问路径 URL，访问您部署的 Nest.js 项目。单击左侧菜单栏中的**触发管理**，查看访问路径。如下图所示：
![](https://main.qcloudimg.com/raw/e451680762dbdb5b427efd168fe2a2c4.png)
7. 单击访问路径 URL，即可访问服务 Nest.js 项目。如下图所示：
![](https://main.qcloudimg.com/raw/c2d8e3d74650c1a06c23a386bae961b9.png)


### 自定义部署 -- 快速迁移本地项目上云


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
3. 打开浏览器访问 `http://localhost:3000`，即可在本地完成 Nest.js 示例项目的访问。如下图所示：
![](https://main.qcloudimg.com/raw/a124e604e2770f73c8293c4bf09b4993.png)

#### 部署上云

接下来执行以下步骤，对已初始化的项目进行简单修改，使其可以通过 Web Function 快速部署，此处项目改造通常分为以下两步：

- 新增 `scf_bootstrap` 启动文件。
- 修改监听地址与端口为 `0.0.0.0:9000`。

具体步骤如下：
1. 修改启动文件`./dist/main.js`，监听端口改为`9000`。如下图所示：
![](https://main.qcloudimg.com/raw/4f32f01747c5868a89d513f7ff8e91f2.png)
2. 在项目根目录下新建 `scf_bootstrap` 启动文件，在该文件添加如下内容（用于启动服务）：
<dx-codeblock>
:::  sh
#!/bin/bash
SERVERLESS=1 /var/lang/node12/bin/node ./dist/main.js
:::
</dx-codeblock>
 <dx-alert infotype="notice" title="">
- 此处仅为示例启动文件，具体请根据您的业务场景进行调整。
- 示例使用的是云函数标准 Node 环境路径，本地调试时，需修改成您的本地路径。
</dx-alert>
3. 新建完成后，还需执行以下命令修改文件可执行权限，默认需要 `777` 或 `755` 权限才可正常启动。示例如下：
<dx-codeblock>
:::  sh
chmod 777 scf_bootstrap
:::
</dx-codeblock>
4. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
5. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
6. 选择**自定义创建**新建函数，根据页面提示配置相关选项。如下图所示：
![](https://main.qcloudimg.com/raw/5ea3c99b29d6a21d158635f314f760e3.png)
	- **函数类型**：选择 “Web 函数”。
	- **函数名称**：填写您自己的函数名称。
	- **地域**：填写您的函数部署地域，默认为广州。
	- **运行环境**：选择 “Nodejs 12.16”。
	- **部署方式**：选择“代码部署”，上传您的本地项目。
	- **提交方法**：选择“本地上传文件夹”。
	- **函数代码**：选择函数代码在本地的具体文件夹。
7. 单击**完成**完成 Nest.js 项目的部署。



#### 开发管理
部署完成后，即可在 SCF 控制台快速访问并测试您的 Web 服务，并且体验云函数多项特色功能，例如层绑定、日志管理等，享受 Serverless 架构带来的低成本、弹性扩缩容等优势。
