## 操作场景
本文档指导您如何通过 Web 函数，快速迁移本地的 Laravel 服务上云。

## 前提条件
- 在使用腾讯云云函数服务之前，您需要 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
> 本文档主要介绍控制台部署方案，您也可以通过命令行完成部署，请参考具体操作请参考[产品文档](https://cloud.tencent.com/document/product/583/58183)

## 操作步骤

### 模版部署 -- 一键部署 Laravel 项目
1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的【函数服务】。
2. 在主界面上方选择期望创建函数的地域，并单击【新建】，进入函数创建流程。
3. 选择使用【模版创建】来新建函数，在搜索框里筛选 `WebFunc`，筛选所有 Web 函数模版，选择 `Laravel 框架模版`，点击“下一步”。如下图所示：
![](https://main.qcloudimg.com/raw/78657911b63663ce80fa02fc96369696.png)
4. 在“配置”页面，您可以查看模版项目的具体配置信息并进行修改。
5. 单击【完成】，即可创建函数。
函数创建完成后，您可在“函数管理”页面，查看 Web 函数的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Laravel 项目
![](https://main.qcloudimg.com/raw/75d23fa483ebe94273deaf846e606618.png)

### 自定义部署 -- 快速迁移本地项目上云
#### 本地开发
1. 首先请在本地环境里，完成 Laravel 的开发环境搭建，参考[官网文档](https://laravel.com/docs/8.x#getting-started-on-macos)


2. 本地创建 Laravel 示例项目
在项目目录下，通过以下指令，初始化 Laravel 示例应用：

```shell
composer create-project --prefer-dist laravel/laravel blog
```

3. 本地启动示例项目后，在浏览器里访问 `http://0.0.0.0:9000`，即可在本地完成Laravel 示例项目的访问

```shell
$ php artisan serve --host 0.0.0.0 --port 9000

   Laravel development server started: <http://0.0.0.0:9000>
   [Wed Jul  7 11:22:05 2021] 127.0.0.1:54350 [200]: /favicon.ico
```
![](https://main.qcloudimg.com/raw/38c23a62b4ad72f777f9469af7c60c49.png)

#### 部署上云

接下来，我们对本地已经创建完成的项目进行部分修改，使其可以通过 Web Function 快速部署，对于 Laravel，具体改造步骤如下：

**1. 新增 `scf_bootstrap` 启动文件**

在项目根目录下新建 `scf_bootstrap` 启动文件，在里面完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动

> 注意
>- `scf_bootstrap` 必须有 `755` 或者 `777` 的可执行权限
>- 如果想要在日志中输出环境变量，启动命令前需要加 `-u` 参数，示例：`python -u app.py`

**2. 修改文件读写路径**
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

**3. 修改监听地址与端口**

在 Web 函数内，限制了监听端口必须为 `9000`，因此需要在在 `scf_bootstrap` 中，通过指定监听端口：

```
/var/lang/php7/bin/php artisan serve --host 0.0.0.0 --port 9000
```

完整 `scf_bootstrap` 内容如下：
![](https://main.qcloudimg.com/raw/089fb093fba05db7ebf41b6fc1cb7c86.png)


**4. 部署上云**

本地配置完成后，执行启动文件，确保您的服务可以本地正常启动，接下来，登陆腾讯云云函数控制台，新建 Web 函数以部署您的 Laravel 项目：
![](https://main.qcloudimg.com/raw/b1b672ad7e46218e66232430a68a830e.png)

部署完成后，点击生成的 URL，即可访问您的 Laravel 应用：
![](https://main.qcloudimg.com/raw/a30df3d4ef68cc608bd01871f23bfba0.png)

### 开发管理
部署完成后，即可在 SCF 控制台快速访问并测试您的 Web 服务，并且体验云函数多项特色功能如层绑定、日志管理等，享受 Serverless 架构带来的低成本、弹性扩缩容等优势。
![](https://main.qcloudimg.com/raw/cb3031f5cb9f5cf5a8b1e2e06cb18d26.png)

