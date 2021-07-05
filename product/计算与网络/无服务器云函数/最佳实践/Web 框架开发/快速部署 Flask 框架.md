本篇教程将为您指导，如何通过 `SCF Web Function`，快速部署您的 Flask 业务上云。

### 模版部署 -- 一键部署 Flask 项目
1. 登录 [Serverless 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，单击左侧导航栏的【函数服务】。
2. 在主界面上方选择期望创建函数的地域，并单击【新建】，进入函数创建流程。
3. 选择使用【模版创建】来新建函数，在搜索框里筛选 `WebFunc`，筛选所有 Web 函数模版，选择 `Flask 框架模版`，点击“下一步”。如下图所示：
![](https://main.qcloudimg.com/raw/75e0b81b90ccd94fbd6afc016957a416.png)
4. 在“配置”页面，您可以查看模版项目的具体配置信息并进行修改。
5. 单击【完成】，即可创建函数。
函数创建完成后，您可在“函数管理”页面，查看 Web 函数的基本信息，并通过 API 网关生成的访问路径 URL 进行访问，查看您部署的 Flask 项目
![](https://main.qcloudimg.com/raw/e51451316771ac660b543f7ebacd69b7.png)

### 自定义部署 -- 快速迁移本地项目上云
#### 本地开发
1. 首先需要确认您本地的环境内已经安装好 Flask
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

3. 本地运行 app.py 文件，在浏览器里访问 `http://127.0.0.1:5000`，即可在本地完成Express 示例项目的访问

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

#### 部署上云

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

**2. 修改监听地址与端口**

在 Web 函数内，限制了监听端口必须为 `9000`，因此需要对监听地址端口进行修改，改为 `0.0.0.0:9000`
![](https://main.qcloudimg.com/raw/ea0a28fae8c9ab16dbe447bfe883aafe.png)

> 您也可以在 `scf_bootstrap` 中，通过环境变量配置监听端口

**3. 新增 `scf_bootstrap` 启动文件**

在项目根目录下新建 `scf_bootstrap` 启动文件，在里面完成环境变量配置，指定服务启动命令等自定义操作，确保您的服务可以通过该文件正常启动

```shell
#!/bin/bash
/var/lang/python3/bin/python3 app.py
```
创建完成后，注意修改您的可执行文件权限，默认需要 `777` 或 `755` 权限
```
chmod 777 scf_bootstrap
```

> 注意
>- 在 SCF 环境内，只有 `/tmp` 文件可读写，建议输出文件时选择 `/tmp`，其它目录会由于缺少权限而写入失败
>- 如果想要在日志中输出环境变量，启动命令前需要加 `-u` 参数，示例：`python -u app.py`

3. 本地配置完成后，执行启动文件，确保您的服务可以本地正常启动，接下来，登陆腾讯云云函数控制台，新建 Web 函数以部署您的 Flask 项目：
![](https://main.qcloudimg.com/raw/e86d6b23487ae5f73cbf3ea643ab6ac2.png)

#### 开发管理
部署完成后，即可在 SCF 控制台快速访问并测试您的 Web 服务，并且体验云函数多项特色功能如层绑定、日志管理等，享受 Serverless 架构带来的低成本、弹性扩缩容等优势。
![](https://main.qcloudimg.com/raw/b181b2695e293f1233dce631f2edb9c0.png)
