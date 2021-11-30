## 操作场景


本文将为您指导如何通过 SCF Web Function，快速部署您的 Flask 业务上云。


>?本文档主要介绍控制台部署方案，您也可以通过命令行完成部署，详情请参见 [通过命令行完成框架部署](https://cloud.tencent.com/document/product/583/59439)。

## 前提条件

在使用腾讯云云函数服务之前，您需要 [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。


## 操作步骤

### 模版部署 -- 一键部署 Flask 项目

1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
2. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
3. 选择使用**模版创建**来新建函数，在搜索框里输入 `WebFunc` 筛选所有 Web 函数模版，选择**Flask 框架模版**并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/75e0b81b90ccd94fbd6afc016957a416.png)
4. 在**新建**页面，您可以查看模版项目的具体配置信息并进行修改。
5. 单击**完成**即可创建函数。函数创建完成后，您可在**函数管理**页面查看 Web 函数的基本信息。
6. 您可以通过 API 网关生成的访问路径 URL，访问您部署的 Flask 项目。单击左侧菜单栏中的**触发管理**，查看访问路径。如下图所示：
![](https://main.qcloudimg.com/raw/0f11b58bdcff56598230144bb6b7be1b.png)
7. 单击访问路径 URL，即可访问服务 Flask 项目。如下图所示：
![](https://main.qcloudimg.com/raw/fd6c71feeddd7f84cfdb0a974f9c794a.png)



### 自定义部署 -- 快速迁移本地项目上云

#### 本地开发

1. 执行以下命令，确认您本地的环境已安装好 Flask。
```shell
pip install Flask
```
2. 在本地创建 `Hello World` 示例项目。
在项目目录下，新建 `app.py` 文件，用于实现 Hello World 应用，示例代码如下：
<dx-codeblock>
:::  python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
:::
</dx-codeblock>
3. 在本地执行 `python3 app.py` 命令运行 app.py 文件。示例如下：
<dx-codeblock>
:::  shell
$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [22/Jun/2021 09:41:04] "GET / HTTP/1.1" 200 -
:::
</dx-codeblock>
4. 打开浏览器访问 `http://127.0.0.1:5000`，即可在本地完成 Flask 示例项目的访问。如下图所示：
![](https://main.qcloudimg.com/raw/4230ec2b5e5160f25ebd44a8a401524f.png)


#### 部署上云

接下来执行以下步骤，对本地已创建完成的项目进行简单修改，使其可以通过 Web Function 快速部署，对于 Flask，具体修改步骤如下：


1. **安装依赖包**
 1. 由于 SCF 云上标准环境内未提供 Flask 依赖库，此处您必须将依赖文件安装完成后，与项目代码一起打包上传。请先新建 `requirements.txt` 文件，文件内容如下：
```txt
#requirements.txt
Flask==1.0.2
werkzeug==0.16.0
```
>! 由于 SCF 内置运行环境版本 (Python 3.6) 限制，werkzeug 只能使用低版本(<=1.0.x)，高版本可能无法正常运行，函数运行环境版本升级已在规划中，敬请期待。

 2. 执行以下命令进行安装：
```shell
pip install -r requirements.txt
```
2. **修改监听地址与端口**
在 Web 函数内，限制了监听端口必须为**9000**，因此需要修改监听地址端口为 `0.0.0.0:9000`，如下图所示：
![](https://main.qcloudimg.com/raw/ea0a28fae8c9ab16dbe447bfe883aafe.png)
>?您也可以在 `scf_bootstrap` 中，通过环境变量配置监听端口。
3. **新增 `scf_bootstrap` 启动文件**
 1. 在项目根目录下新建 `scf_bootstrap` 启动文件，在该文件添加如下内容（用于完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动）：
```
#!/bin/bash
/var/lang/python3/bin/python3 app.py
```
 2. 创建完成后，还需执行以下命令修改文件可执行权限，默认需要 `777` 或 `755` 权限才可以正常启动。示例如下：
```shell
chmod 777 scf_bootstrap
```
>!
>- 在 SCF 环境内，只有 `/tmp` 文件可读写，建议输出文件时选择 `/tmp`，其他目录会由于缺少权限而写入失败。
>- 如需在日志中输出环境变量，需在启动命令前加 `-u` 参数，例如 `python -u app.py`。

4. 本地配置完成后，执行以下命令启动服务（如下命令为在 scf_bootstrap 目录下执行时示例），确保您的服务在本地可以正常启动。
<dx-codeblock>
:::  shell
./scf_bootstrap
:::
</dx-codeblock>
5. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的**函数服务**。
6. 在主界面上方选择期望创建函数的地域，并单击**新建**，进入函数创建流程。
7. 选择**自定义创建**新建函数，根据页面提示配置相关选项。如下图所示：
![](https://main.qcloudimg.com/raw/e86d6b23487ae5f73cbf3ea643ab6ac2.png)
	- **函数类型**：选择 “Web 函数”。
	- **函数名称**：填写您自己的函数名称。
	- **地域**：填写您的函数部署地域，例如成都。
	- **部署方式**：选择“代码部署”，上传您的本地项目。
	- **运行环境**：选择 “Python3.6”。
8. 单击**完成**完成 Flask 项目的部署。






#### 开发管理
部署完成后，即可在 SCF 控制台快速访问并测试您的 Web 服务，并且体验云函数多项特色功能，例如层绑定、日志管理等，享受 Serverless 架构带来的低成本、弹性扩缩容等优势。如下图所示：
![](https://main.qcloudimg.com/raw/8c8d1d225cfa53ca79fccdb1a50a81b0.png)
