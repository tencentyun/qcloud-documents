## 操作场景

本文档指导您如何通过 Web 函数，快速迁移本地的 Laravel 服务上云。


>?本文档主要介绍控制台部署方案，您也可以通过命令行完成部署，详情请参见 [通过命令行完成框架部署](https://cloud.tencent.com/document/product/583/59439)。

## 前提条件

在使用腾讯云云函数服务之前，您需要 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。


## 操作步骤

### 模版部署 -- 一键部署 Laravel 项目
1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
2. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
3. 选择使用**模版创建**来新建函数，在搜索框里筛选 `WebFunc`，筛选所有 Web 函数模版，选择**Laravel 框架模版**并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/5aaff988896823fd718b5b8a36234cfd.png)
4. 在**新建**页面，您可以查看模版项目的具体配置信息并进行修改。
5. 单击**完成**即可创建函数。函数创建完成后，您可在**函数管理**页面查看 Web 函数的基本信息。
6. 您可以通过 API 网关生成的访问路径 URL，访问您部署的 Laravel 项目。单击左侧菜单栏中的**触发管理**，查看访问路径。如下图所示：[](id:step1-6)
![](https://main.qcloudimg.com/raw/976c50da475f63367cda54caba20afc2.png)
7. 单击访问路径 URL，即可访问服务 Laravel 项目。如下图所示：
![](https://main.qcloudimg.com/raw/c862404be796d10bd999a577b69f8316.png)



### 自定义部署 -- 快速迁移本地项目上云

#### 本地开发

1. 参考 [Laravel](https://laravel.com/docs/8.x#getting-started-on-macos) 官方文档，在本地环境中完成 Laravel 的开发环境搭建。
2. 在本地创建 Laravel 示例项目。进入项目目录下，执行以下命令，初始化 Laravel 示例应用：
<dx-codeblock>
:::  sh
composer create-project --prefer-dist laravel/laravel blog
:::
</dx-codeblock>
3. 执行以下命令，在本地启动示例项目。示例如下：
<dx-codeblock>
:::  sh
$ php artisan serve --host 0.0.0.0 --port 9000
   Laravel development server started: <http://0.0.0.0:9000>
   [Wed Jul  7 11:22:05 2021] 127.0.0.1:54350 [200]: /favicon.ico
:::
</dx-codeblock>
4. 打开浏览器访问 `http://0.0.0.0:9000`，即可在本地完成 Laravel 示例项目的访问。如下图所示：
![](https://main.qcloudimg.com/raw/38c23a62b4ad72f777f9469af7c60c49.png)



#### 部署上云



在该文件添加如下内容（用于配置环境变量和启动服务，此处仅为示例，具体操作请以您实际业务场景来调整）：


接下来执行以下步骤，对已初始化的项目进行简单修改，使其可以通过 Web Function 快速部署，具体修改步骤如下：



1. **新增 `scf_bootstrap` 启动文件**
在项目根目录下新建 `scf_bootstrap` 启动文件，在该文件完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动。
>!
>- `scf_bootstrap` 必须有 `755` 或者 `777` 的可执行权限。
>- 如需在日志中输出环境变量，需在启动命令前需要加 `-u` 参数，例如 `python -u app.py`。
2. **修改文件读写路径**
由于在 SCF 环境内，只有 `/tmp` 文件可读写，其他目录会由于缺少权限而写入失败，因此需要在 `scf_bootstrap` 里，以环境变量的方式注入，调整 Laravel 框架的输出目录：
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
3. **修改监听地址与端口**
在 Web 函数内，限制了监听端口必须为`9000`，因此需要在 `scf_bootstrap` 中通过以下命令指定监听端口：
```sh
/var/lang/php7/bin/php artisan serve --host 0.0.0.0 --port 9000
```
 完整 `scf_bootstrap` 内容如下：
![](https://main.qcloudimg.com/raw/089fb093fba05db7ebf41b6fc1cb7c86.png)
4. **部署上云**
本地配置完成后，执行启动文件，确保您的服务可以本地正常启动。执行以下步骤部署 Laravel：
	1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
	2. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
	3. 选择**自定义创建**新建函数，根据页面提示配置相关选项。如下图所示：
	![](https://main.qcloudimg.com/raw/783db24ab94568c430e84a3dae99f84d.png)
		- **函数类型**：选择 “Web 函数”。
		- **函数名称**：填写您自己的函数名称。
		- **地域**：填写您的函数部署地域，例如成都。
		- **部署方式**：选择“代码部署”，上传您的本地项目。
		- **运行环境**：选择 “Php7”。
	4. 部署完成后，单击生成的 URL，即可访问您的 Laravel 应用。如下图所示：
![](https://main.qcloudimg.com/raw/a30df3d4ef68cc608bd01871f23bfba0.png)



#### 开发管理

部署完成后，即可在 SCF 控制台快速访问并测试您的 Web 服务，并且体验云函数多项特色功能如层绑定、日志管理等，享受 Serverless 架构带来的低成本、弹性扩缩容等优势。
![](https://main.qcloudimg.com/raw/cb3031f5cb9f5cf5a8b1e2e06cb18d26.png)

