应用中心框架部署方案已经全新升级，您可以通过 `SCF Web Function`，快速部署您的 Laravel 业务上云。

>! **应用控制台部署与函数直接部署有什么区别？**
通过应用部署或函数部署，均可以基于 Web 函数，快速部署常见 Web 框架。
- 如果您只关注代码逻辑开发，无需额外资源创建，可以通过 SCF 云函数控制台，完成快速部署。
- 如果除了代码部署外，您还需要更多能力或资源创建，如自动创建层托管依赖、一键实现静态资源分离、支持代码仓库直接拉取等，可以通过应用控制台，完成 Web 应用的创建工作。

本篇文档为您介绍应用控制台的部署方案，您也可以通过命令行完成部署，具体操作请参考 [产品文档](https://cloud.tencent.com/document/product/583/58183)。

### 模版部署 -- 部署 Laravel 示例代码
1. 登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)。
2. 选择**Web 应用>Laravel 框架**，如下图所示：
![](https://main.qcloudimg.com/raw/4c005329ab121bcc71e8f436932adb74.png)
3. 单击“下一步”，完成基础配置选择。
![](https://main.qcloudimg.com/raw/9f22f8c1e5426b5d3d54631caabde012.png)
4. 上传方式，选择**示例代码**直接部署，单击**完成**，即可开始应用的部署。
5. 部署完成后，您可在应用详情页面，查看示例应用的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Laravel 项目。
![](https://main.qcloudimg.com/raw/75d23fa483ebe94273deaf846e606618.png)

### 自定义部署 -- 快速部署 Web 应用
#### 本地开发
1. 首先请在本地环境里，完成 Laravel 的开发环境搭建，参考 [官网文档](https://laravel.com/docs/8.x#getting-started-on-macos)。


2. 本地创建 Laravel 示例项目
在项目目录下，通过以下指令，初始化 Laravel 示例应用：
```shell
composer create-project --prefer-dist laravel/laravel blog
```

3. 本地启动示例项目后，在浏览器里访问 `http://0.0.0.0:9000`，即可在本地完成 Laravel 示例项目的访问。
```shell
$ php artisan serve --host 0.0.0.0 --port 9000

   Laravel development server started: <http://0.0.0.0:9000 
   [Wed Jul  7 11:22:05 2021] 127.0.0.1:54350 [200]: /favicon.ico
```
![](https://main.qcloudimg.com/raw/38c23a62b4ad72f777f9469af7c60c49.png)

#### 部署上云

接下来执行以下步骤，对本地已创建完成的项目进行简单修改，使其可以通过 Web Function 快速部署，对于 Laravel 框架，具体改造说明如下：

- 修改监听地址与端口为 `0.0.0.0:9000`。
- 修改写入路径，serverless 环境下只有 `/tmp` 目录可读写。
- 新增 `scf_bootstrap` 启动文件。

**1. (可选)配置 scf_bootstrap 启动文件**

>? 您也可以在控制台完成该模块配置。
>

在项目根目录下新建 `scf_bootstrap` 启动文件，在里面完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动。

>! `scf_bootstrap` 必须有 `755` 或者 `777` 的可执行权限。
>



由于在 SCF 环境内，只有 `/tmp` 文件可读写，其它目录会由于缺少权限而写入失败，因此需要在 `scf_bootstrap` 里，以环境变量的方式注入，调整 Laravel 框架的输出目录：

```
#!/bin/bash

# 注入 SERVERLESS 标识
export SERVERLESS=1
# 修改模板编译缓存路径，云函数只有 /tmp 目录可读写
export VIEW_COMPILED_PATH=/tmp/storage/framework/views
# 修改 session 以内存方式（数组类型）存储
export SESSION_DRIVER=array
# 日志输出到 stderr
export LOG_CHANNEL=stderr
# 修改应用存储路径
export APP_STORAGE=/tmp/storage

# 初始化模板缓存目录
mkdir -p /tmp/storage/framework/views
```

同时，在 Web 函数内，限制了监听端口必须为 `9000`，因此需要在 `scf_bootstrap` 中，通过指定监听端口：

```
/var/lang/php7/bin/php artisan serve --host 0.0.0.0 --port 9000
```

完整 `scf_bootstrap` 内容如下：
![](https://main.qcloudimg.com/raw/089fb093fba05db7ebf41b6fc1cb7c86.png)


本地配置完成后，执行启动文件，确保您的服务可以本地正常启动，接下来，登录腾讯云云控制台，部署您的 Laravel 项目。

**2. 控制台上传**

登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)，选择**Web 应用>Laravel 框架**，上传方式可以选择**本地上传**或**代码仓库拉取**。

您可以在控制台完成启动文件 `scf_bootstrap` 内容配置，配置完成后，控制台将为您自动生成 启动文件，和项目代码一起打包部署。
>! 启动文件以项目内文件为准，如果您的项目里已经包含 `scf_bootstrap` 文件，将不会覆盖该内容。

配置完成后，单击**完成**，部署您的 Laravel 项目。
![](https://main.qcloudimg.com/raw/a28efc9156bc3ba9ab817be16a463a02.png)

部署完成后，点击生成的 URL，即可访问您的 Laravel 应用：
![](https://main.qcloudimg.com/raw/a30df3d4ef68cc608bd01871f23bfba0.png)

#### 高级配置管理
您可在“高级配置”里进行更多应用管理操作，如创建层、绑定自定义域名、配置环境变量等。
![](https://main.qcloudimg.com/raw/5a788f4872c1e431e375f445f157b1e2.png)
