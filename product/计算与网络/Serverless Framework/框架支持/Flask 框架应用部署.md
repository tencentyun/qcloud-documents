应用中心框架部署方案已经全新升级，您可以通过 `SCF Web Function`，快速部署您的 Flask 业务上云。


>! **应用控制台部署与函数直接部署有什么区别？**
通过应用部署或函数部署，均可以基于 Web 函数，快速部署常见 Web 框架。
- 如果您只关注代码逻辑开发，无需额外资源创建，可以通过 SCF 云函数控制台，完成快速部署。
- 如果除了代码部署外，您还需要更多能力或资源创建，如自动创建层托管依赖、一键实现静态资源分离、支持代码仓库直接拉取等，可以通过应用控制台，完成 Web 应用的创建工作。

本篇文档为您介绍应用控制台的部署方案，您也可以通过命令行完成部署，具体操作请参考 [产品文档](https://cloud.tencent.com/document/product/583/58183)。

## 模版部署 -- 部署 Flask 示例代码
1. 登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)。
2. 选择**Web 应用>Flask 框架**，如下图所示：
![](https://main.qcloudimg.com/raw/5085acaefb589659b38d6ad796ce80f0.png)
3. 单击“下一步”，完成基础配置选择。
![](https://main.qcloudimg.com/raw/9f22f8c1e5426b5d3d54631caabde012.png)
4. 上传方式，选择**示例代码**直接部署，单击**完成**，即可开始应用的部署。
5. 部署完成后，您可在应用详情页面，查看示例应用的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Flask 项目。
![](https://main.qcloudimg.com/raw/e51451316771ac660b543f7ebacd69b7.png)

## 自定义部署 -- 快速部署 Web 应用
### 本地开发
1. 首先需要确认您本地的环境内已经安装好 Flask。
```shell
pip install Flask
```
2. 本地创建 `Hello World` 示例项目
在项目目录下，新建 `app.py` 项目，实现最简单的 Hello World 应用，示例代码如下：
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
```
3. 本地运行 app.py 文件，在浏览器里访问 `http://127.0.0.1:5000`，即可在本地完成Express 示例项目的访问。
```shell
$ python3 app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [22/Jun/2021 09:41:04] "GET / HTTP/1.1" 200 -
```
![](https://main.qcloudimg.com/raw/6319dcbb13adb70086eded667476c80a.png)

### 部署上云

接下来，我们对本地已经创建完成的项目进行简单修改，使其可以通过 Web Function 快速部署，对于 Flask，具体改造步骤如下：

**1. 安装依赖包**

由于 SCF 云上标准环境内没有 Flask 依赖库，此处您必须将依赖文件安装完成后，与项目代码一起打包上传，首先新建 `requirements.txt` 文件：
```txt
#requirements.txt

Flask==1.0.2
werkzeug==0.16.0
```
接下来执行安装：
```shell
pip install -r requirements.txt
```

>! 由于 SCF 内置运行环境版本 (Python 3.6) 限制，werkzeug 只能使用低版本(<=1.0.x)，高版本可能无法正常运行，函数运行环境版本升级已在规划中，敬请期待。
>

**2. 修改监听地址与端口**

在 Web 函数内，限制了监听端口必须为 `9000`，因此需要对监听地址端口进行修改，改为 `0.0.0.0:9000`。
![](https://main.qcloudimg.com/raw/ea0a28fae8c9ab16dbe447bfe883aafe.png)
>! 您也可以在 `scf_bootstrap` 中，通过环境变量配置监听端口。

**3. (可选)配置 scf_bootstrap 启动文件**

在项目根目录下新建 `scf_bootstrap` 启动文件，在里面完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动。

```shell
#!/bin/bash
/var/lang/python3/bin/python3 app.py
```
创建完成后，注意修改您的可执行文件权限，默认需要 `777` 或 `755` 权限。
```
chmod 777 scf_bootstrap
```

>!
>- 您也可以在控制台完成该模块配置
>- 在 SCF 环境内，只有 `/tmp` 文件可读写，建议输出文件时选择 `/tmp`，其它目录会由于缺少权限而写入失败
>- 如果想要在日志中输出环境变量，启动命令前需要加 `-u` 参数，示例：`python -u app.py`


**4. 控制台上传**

登录 [Serverless 应用控制台](https://console.cloud.tencent.com/sls)，选择**Web 应用>Flask 框架**，上传方式可以选择**本地上传**或**代码仓库拉取**。

您可以在控制台完成启动文件 `scf_bootstrap` 内容配置，配置完成后，控制台将为您自动生成 启动文件，和项目代码一起打包部署。
>! 启动文件以项目内文件为准，如果您的项目里已经包含 `scf_bootstrap` 文件，将不会覆盖该内容。

配置完成后，单击**完成**，部署您的 Flask 项目。
![](https://main.qcloudimg.com/raw/a28efc9156bc3ba9ab817be16a463a02.png)

#### 高级配置管理
您可在“高级配置”里进行更多应用管理操作，如创建层、绑定自定义域名、配置环境变量等。
![](https://main.qcloudimg.com/raw/5a788f4872c1e431e375f445f157b1e2.png)
