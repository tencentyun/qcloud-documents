## 步骤1：编写基础应用（使用 flask 框架）

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
    app.run(debug=True, host='0.0.0.0', port=80)
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
以上代码会创建一个基本的 Web 服务器，并监听 `80` 端口。
</dx-alert>


## 步骤2：将应用容器化

1. 在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：
<dx-codeblock>
:::  docker
# 选择基础镜像。如需更换，请到[dockerhub官方仓库](https://hub.docker.com/_/python?tab=tags)自行选择后替换。
# 已知alpine镜像与pytorch有兼容性问题会导致构建失败，如需使用pytorch请务必按需更换基础镜像。
FROM alpine:3.13

# 容器默认时区为UTC，如需使用上海时间请启用以下时区设置命令
# RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai > /etc/timezone

# 安装依赖包，如需其他依赖包，请到alpine依赖包管理(https://pkgs.alpinelinux.org/packages?name=php8*imagick*&branch=v3.13)查找。
# 选用国内镜像源以提高下载速度
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tencent.com/g' /etc/apk/repositories \
# 安装python3
&& apk add --update --no-cache python3 py3-pip \
&& rm -rf /var/cache/apk/*

# 拷贝当前项目到/app目录下（.dockerignore中文件除外）
COPY . /app

# 设定当前的工作目录
WORKDIR /app

# 安装依赖到指定的/install文件夹
# 选用国内镜像源以提高下载速度
RUN pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple \
&& pip config set global.trusted-host mirrors.cloud.tencent.com \
&& pip install --upgrade pip \
# pip install scipy 等数学包失败，可使用 apk add py3-scipy 进行， 参考安装 https://pkgs.alpinelinux.org/packages?name=py3-scipy&branch=v3.13
&& pip install --user -r requirements.txt

# 暴露端口。
# 此处端口必须与部署时填写的端口一致，否则会部署失败。
EXPOSE 80

# 执行启动命令
# 写多行独立的CMD命令是错误写法！只有最后一行CMD命令会被执行，之前的都会被忽略，导致业务报错。
# 请参考[Docker官方文档之CMD命令](https://docs.docker.com/engine/reference/builder/#cmd)
CMD ["python3", "run.py", "0.0.0.0", "80"]
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


## 步骤4：部署到云托管

详情请参见 [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。
