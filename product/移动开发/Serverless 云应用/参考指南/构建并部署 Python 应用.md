代码示例：[Python](https://github.com/TencentCloudBase/cloudbase-examples/tree/master/cloudbaserun/python)


可单击下方按钮一键部署：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-examples&workDir=cloudbaserun%2Fpython&appName=python-hello-world" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div>


## 步骤1：编写基础应用

1. 创建名为 `helloworld-python` 的新目录，并转到此目录中：
<dx-codeblock>
:::  plaintext
mkdir helloworld-python
cd helloworld-python
:::
</dx-codeblock>
2. 创建名为 `main.py` 的文件，并将以下代码粘贴到其中：
<dx-codeblock>
:::  python
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
以上代码会创建一个基本的 Web 服务器，并监听 `8080` 端口。
</dx-alert>


## 步骤2：将应用容器化

1. 在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：
<dx-codeblock>
:::  docker
# 使用官方 Python 轻量级镜像
# https://hub.docker.com/_/python
FROM python:3.8-slim

# 将本地代码拷贝到容器内
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# 安装依赖
RUN pip install Flask gunicorn

# 启动 Web 服务
# 这里我们使用了 gunicorn 作为 Server，1 个 worker 和 8 个线程
# 如果您的容器实例拥有多个 CPU 核心，我们推荐您把线程数设置为与 CPU 核心数一致
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app
:::
</dx-codeblock>
2. 添加一个 `.dockerignore` 文件，以从容器映像中排除文件：
<dx-codeblock>
:::  docker
Dockerfile
README.md
*.pyc
*.pyo
*.pyd
__pycache__
.pytest_cache
:::
</dx-codeblock>

## 步骤3（可选）：本地构建镜像

1. 如果您本地已经安装了 Docker，可以运行以下命令，在本地构建 Docker 镜像：
<dx-codeblock>
:::  sh
docker build -t helloworld-python
:::
</dx-codeblock>
2. 构建成功后，运行 `docker images`，可以看到构建出的镜像，随后您可以将此镜像上传至您的镜像仓库。
<dx-codeblock>
:::  sh
REPOSITORY          TAG       IMAGE ID         CREATED            SIZE
helloworld-python   latest    1c8dfb88c823     8 seconds ago      123MB
:::
</dx-codeblock>


## 步骤4：部署到 CloudBase 云托管

详情请参见 [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。
