## 操作场景


本文将为您指导如何通过 Web Function，将您的本地 Django 快速部署到云端。

>?本文档主要介绍控制台部署方案，您也可以通过命令行完成部署，详情请参见 [通过命令行完成框架部署](https://cloud.tencent.com/document/product/583/59439)。


## 前提条件
在使用腾讯云云函数服务之前，您需要 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤

### 模版部署 -- 一键部署 Django 项目

1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
2. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
3. 选择使用**模版创建**来新建函数，在搜索框里输入 `Django` 选择 **Django 框架模版**并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/d714890cf3c19a01aee574be4720678c.png)
4. 在**新建**页面，您可以查看模版项目的具体配置信息并进行修改。
5. 单击**完成**即可创建函数。函数创建完成后，您可在**函数管理**页面查看 Web 函数的基本信息。
6. 您可以通过 API 网关生成的访问路径 URL，访问您部署的 Django 项目。单击左侧菜单栏中的**触发管理**，查看访问路径。如下图所示：
![](https://main.qcloudimg.com/raw/0f11b58bdcff56598230144bb6b7be1b.png)
7. 单击访问路径 URL，即可访问服务 Django 项目。如下图所示：
![](https://main.qcloudimg.com/raw/ed52f5307da4bc7c06a939edbc84ab54.png)



### 自定义部署 -- 快速迁移本地项目上云

#### 本地开发

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
<dx-codeblock>
:::  python
$ python manage.py runserver
July 27, 2021 - 11:52:20
Django version 3.2.5, using settings 'helloworld.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
:::
</dx-codeblock>
4. 打开浏览器访问 `http://127.0.0.1:8000`，即可在本地完成 Django 示例项目的访问。如下图所示：
![](https://main.qcloudimg.com/raw/a09696d7d24c719ecb2f276c4bba93ce.png)


#### 部署上云

接下来执行以下步骤，对本地已创建完成的项目进行简单修改，使其可以通过 Web Function 快速部署，对于 Django，具体修改步骤如下：


1. **安装依赖包**
 1. 由于 SCF 云上标准环境内未提供 Django 依赖库，此处您必须将依赖文件安装完成后，与项目代码一起打包上传。请先新建 `requirements.txt` 文件，文件内容如下：
```txt
Django==3.1.3
```
 2. 执行以下命令进行安装：
```shell
pip install -r requirements.txt -t .
```
>? 由于初始化的默认项目引用了`db.sqlite3` 库，请同步安装该依赖，或将项目文件内 `setting.py` 里 `DATABASES` 字段部分配置注释。
>
2. **新增 `scf_bootstrap` 启动文件**
在 Web 函数内，限制了监听端口必须为**9000**，因此需要修改监听地址端口，在项目根目录下新建 `scf_bootstrap` 启动文件，在该文件添加如下内容（用于完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动）：
```
#!/bin/bash
/var/lang/python3/bin/python3 manage.py runserver 9000
```

3. 创建完成后，还需执行以下命令修改文件可执行权限，默认需要 `777` 或 `755` 权限才可以正常启动。示例如下：
```shell
chmod 777 scf_bootstrap
```
>!
>- 在 SCF 环境内，只有 `/tmp` 文件可读写，建议输出文件时选择 `/tmp`，其他目录会由于缺少权限而写入失败。
>- 如需在日志中输出环境变量，需在启动命令前加 `-u` 参数，例如 `python -u app.py`。
>
4. 本地配置完成后，执行以下命令启动服务（如下命令为在 scf_bootstrap 目录下执行时示例），确保您的服务在本地可以正常启动。
>! 本地测试时注意将 python 路径改为本地路径。
```shell
./scf_bootstrap
```

5. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
6. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
7. 选择**自定义创建**新建函数，根据页面提示配置相关选项。如下图所示：
![](https://main.qcloudimg.com/raw/ab6e9b2544d07521e5010fcaee5c94dd.png)
	- **函数类型**：选择 “Web 函数”。
	- **函数名称**：填写您自己的函数名称。
	- **地域**：填写您的函数部署地域，例如成都。
	- **部署方式**：选择“代码部署”，上传您的本地项目。
	- **运行环境**：选择 “Python3.6”。
8. 单击**完成**完成 Django 项目的部署。


#### 开发管理
部署完成后，即可在 SCF 控制台快速访问并测试您的 Web 服务，并且体验云函数多项特色功能，例如层绑定、日志管理等，享受 Serverless 架构带来的低成本、弹性扩缩容等优势，如下图所示：
![](https://main.qcloudimg.com/raw/c87151ecbb2f7c7e7f2c6877a043eda6.png)
