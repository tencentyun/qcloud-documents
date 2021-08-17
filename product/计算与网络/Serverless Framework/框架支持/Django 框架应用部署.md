应用中心框架部署方案已经全新升级，您可以通过 `SCF Web Function`，快速部署您的 Django 业务上云。

>! **应用控制台部署与函数直接部署有什么区别？**
通过应用部署或函数部署，均可以基于 Web 函数，快速部署常见 Web 框架。
- 如果您只关注代码逻辑开发，无需额外资源创建，可以通过 SCF 云函数控制台，完成快速部署。
- 如果除了代码部署外，您还需要更多能力或资源创建，如自动创建层托管依赖、一键实现静态资源分离、支持代码仓库直接拉取等，可以通过应用控制台，完成 Web 应用的创建工作。

本篇文档为您介绍应用控制台的部署方案，您也可以通过命令行完成部署，具体操作请参考 [产品文档](https://cloud.tencent.com/document/product/583/58183)。

## 模版部署 -- 部署 Django 示例代码
1. 登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)。
2. 选择**Web 应用>Django 框架**，如下图所示：
![](https://main.qcloudimg.com/raw/3c03bbfe813cf5d094318593b1cc4ce8.png)
3. 单击“下一步”，完成基础配置选择。
![](https://main.qcloudimg.com/raw/9f22f8c1e5426b5d3d54631caabde012.png)
4. 上传方式，选择**示例代码**直接部署，单击**完成**，即可开始应用的部署。
5. 部署完成后，您可在应用详情页面，查看示例应用的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Django 项目。
![](https://main.qcloudimg.com/raw/ed52f5307da4bc7c06a939edbc84ab54.png)

## 自定义部署 -- 快速部署 Web 应用
### 本地开发
1. 执行以下命令，确认您本地的环境已安装好 Django。
```shell
python -m pip install Django
```
2. 在本地创建 `Hello World` 示例项目。
```sh
django-admin startproject helloworld && cd helloworld
```
目录结构如下：
```
$ tree
. manage.py 管理器
|--*** 
|   |-- __init__.py 包
|   |-- settings.py  设置文件
|   |-- urls.py   路由
|   `-- wsgi.py   部署
```
3. 在本地执行 `python manage.py runserver` 命令运行启动文件。示例如下：
```
$ python manage.py runserver
July 27, 2021 - 11:52:20
Django version 3.2.5, using settings 'helloworld.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
4. 打开浏览器访问 `http://127.0.0.1:8000`，即可在本地完成 Django 示例项目的访问。如下图所示：
![](https://main.qcloudimg.com/raw/a09696d7d24c719ecb2f276c4bba93ce.png)

### 部署上云

接下来执行以下步骤，对本地已创建完成的项目进行简单修改，使其可以通过 Web Function 快速部署，对于 Django，具体修改步骤如下：


**1. 安装依赖包**

由于 SCF 云上标准环境内未提供 Django 依赖库，此处您必须将依赖文件安装完成后，与项目代码一起打包上传。请先新建 `requirements.txt` 文件，文件内容如下：
```txt
Django==3.1.3
```
执行以下命令进行安装：
```shell
pip install -r requirements.txt -t .
```
>! 由于初始化的默认项目引用了`db.sqlite3` 库，请同步安装该依赖，或将项目文件内 `setting.py` 里 `DATABASES` 字段部分配置注释掉。


**2. (可选)配置 scf_bootstrap 启动文件**

>? 您也可以在控制台完成该模块配置。
>
在 Web 函数内，限制了监听端口必须为**9000**，因此需要修改监听地址端口，在项目根目录下新建 `scf_bootstrap` 启动文件，在该文件添加如下内容（用于完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动）：
```
#!/bin/bash
/var/lang/python3/bin/python3 manage.py runserver 9000
```
创建完成后，还需执行以下命令修改文件可执行权限，默认需要 `777` 或 `755` 权限才可以正常启动。示例如下：
```shell
chmod 777 scf_bootstrap
```
>! 
>- 在 SCF 环境内，只有 `/tmp` 文件可读写，建议输出文件时选择 `/tmp`，其他目录会由于缺少权限而写入失败。
>- 如需在日志中输出环境变量，需在启动命令前加 `-u` 参数，例如 `python -u app.py`。

本地配置完成后，执行以下命令启动服务（如下命令为在 scf_bootstrap 目录下执行时示例），确保您的服务在本地可以正常启动。
>! 本地测试时注意将 python 路径改为本地路径。
>
```shell
./scf_bootstrap
```


**3. 控制台上传**


登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)，选择**Web 应用>Django 框架**，上传方式可以选择**本地上传**或**代码仓库拉取**

您可以在控制台完成启动文件 `scf_bootstrap` 内容配置，配置完成后，控制台将为您自动生成 启动文件，和项目代码一起打包部署。
>! 启动文件以项目内文件为准，如果您的项目里已经包含 `scf_bootstrap` 文件，将不会覆盖该内容。

配置完成后，单击**完成**，部署您的 Django 项目。
![](https://main.qcloudimg.com/raw/a28efc9156bc3ba9ab817be16a463a02.png)

#### 高级配置管理
您可在“高级配置”里进行更多应用管理操作，如创建层、绑定自定义域名、配置环境变量等。
![](https://main.qcloudimg.com/raw/5a788f4872c1e431e375f445f157b1e2.png)
