## 步骤1：编写基础应用

1. 创建名为 `helloworld` 的新目录，并转到此目录中：
<dx-codeblock>
:::  plaintext
mkdir helloworld
cd helloworld
:::
</dx-codeblock>
2. 创建一个包含以下内容的 `package.json` 文件：
<dx-codeblock>
:::  json
{
  "name": "helloworld",
  "description": "Simple hello world sample in Node",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "author": "Tencent CloudBase",
  "license": "Apache-2.0",
  "dependencies": {
    "express": "^4.17.1"
  }
}
:::
</dx-codeblock>
3. 在同一目录中，创建一个 `index.js` 文件，并将以下代码行复制到其中：
<dx-codeblock>
:::  js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`Hello World!`);
});

const port = 80;
app.listen(port, () => {
  console.log(`helloworld: listening on port ${port}`);
});
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
此代码会创建一个基本的 Web 服务器，侦听 `80` 端口。
</dx-alert>

## 步骤2：将应用容器化

1. 在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：
<dx-codeblock>
:::  docker
FROM alpine:3.13

# 容器默认时区为UTC，如需使用上海时间请启用以下时区设置命令
# RUN apk add tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo Asia/Shanghai > /etc/timezone

# 安装依赖包，如需其他依赖包，请到alpine依赖包管理(https://pkgs.alpinelinux.org/packages?name=php8*imagick*&branch=v3.13)查找。
RUN apk add --update --no-cache nodejs npm

# # 指定工作目录
WORKDIR /app

# 拷贝包管理文件
COPY package*.json /app

# npm 源，选用国内镜像源以提高下载速度
RUN npm config set registry https://mirrors.cloud.tencent.com/npm/
# RUN npm config set registry https://registry.npm.taobao.org/

# npm 安装依赖
RUN npm install

# 将当前目录（dockerfile所在目录）下所有文件都拷贝到工作目录下（.gitignore中的文件除外）
COPY . /app

# 执行启动命令.
# 写多行独立的CMD命令是错误写法！只有最后一行CMD命令会被执行，之前的都会被忽略，导致业务报错。
# 请参考[Docker官方文档之CMD命令](https://docs.docker.com/engine/reference/builder/#cmd)
CMD ["npm", "start"]
:::
</dx-codeblock>
2. 添加一个 `.dockerignore` 文件，以从容器映像中排除文件：
<dx-codeblock>
:::  sh
Dockerfile
.dockerignore
node_modules
npm-debug.log
:::
</dx-codeblock>

## 步骤3（可选）：本地构建镜像

1. 如果您本地已经安装了 Docker，可以运行以下命令，在本地构建 Docker 镜像：
<dx-codeblock>
:::  sh
docker build -t helloworld
:::
</dx-codeblock>
2. 构建成功后，运行 `docker images`，可以看到构建出的镜像，随后您可以将此镜像上传至您的镜像仓库。
<dx-codeblock>
:::  sh
REPOSITORY     TAG       IMAGE ID         CREATED          SIZE
helloworld   latest    1c8dfb88c823     8 seconds ago      146MB
:::
</dx-codeblock>


## 步骤4：部署到云托管

详情请参见 [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。
