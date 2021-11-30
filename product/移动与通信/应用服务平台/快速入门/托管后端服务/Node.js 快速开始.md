代码示例：[Node.js](https://github.com/TencentCloudBase/cloudbase-examples/tree/master/cloudbaserun/node)

单击下方按钮一键部署：

<div style="background-color:#00A4FF; width: 125px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/tcb/env/index?action=CreateAndDeployCloudBaseProject&appUrl=https%3A%2F%2Fgithub.com%2FTencentCloudBase%2Fcloudbase-examples&workDir=cloudbaserun%2Fnode&appName=nodejs-hello-world" target="_blank"  style="color: white; font-size:13px;">部署到云开发</a></div><br>


## 步骤1：编写基础应用

创建名为 `helloworld` 的新目录，并转到此目录中：

```sh
mkdir helloworld
cd helloworld
```

创建一个包含以下内容的 `package.json` 文件：

```json
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
```

在同一目录中，创建一个 `index.js` 文件，并将以下代码行复制到其中：

```js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`Hello World!`);
});

const port = 8080;
app.listen(port, () => {
  console.log(`helloworld: listening on port ${port}`);
});
```

此代码会创建一个基本的 Web 服务器，侦听 `8080` 端口。

## 步骤2：将应用容器化

在项目根目录下，创建一个名为 `Dockerfile` 的文件，内容如下：

```docker
# 使用官方 Node.js 12 轻量级镜像.
# https://hub.docker.com/_/node
FROM node:12-slim

# 定义工作目录
WORKDIR /usr/src/app

# 将依赖定义文件拷贝到工作目录下
COPY package*.json ./

# 以 production 形式安装依赖
RUN npm install --only=production

# 将本地代码复制到工作目录内
COPY . ./

# 启动服务
CMD [ "node", "index.js" ]
```

添加一个 `.dockerignore` 文件，以从容器映像中排除文件：

```
Dockerfile
.dockerignore
node_modules
npm-debug.log
```

## 步骤3（可选）：本地构建镜像

如果您本地已经安装了 Docker，可以运行以下命令，在本地构建 Docker 镜像：

```sh
docker build -t helloworld .
```

构建成功后，运行 `docker images`，可以看到构建出的镜像：

```
REPOSITORY     TAG       IMAGE ID         CREATED          SIZE
helloworld   latest    1c8dfb88c823     8 seconds ago      146MB
```

随后您可以将此镜像上传至您的镜像仓库，详情请参见 [安装 docker](https://docs.docker.com/get-docker/)。

## 步骤4：部署到 CloudBase 云托管

请参考 [部署服务](https://cloud.tencent.com/document/product/1243/46127) 与 [版本配置说明](https://cloud.tencent.com/document/product/1243/49177)。
