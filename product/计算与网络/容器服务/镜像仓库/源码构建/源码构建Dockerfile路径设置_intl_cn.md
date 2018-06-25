# 源码构建功能 Dockerfile 路径问题指南

腾讯云容器服务提供了镜像自动构建能力，在源码构建配置中，可以指定Dockerfile文件路径，本文将说明该路径与镜像构建的关系。

## 源码构建功能 Dockerfile路径该怎么填 ?

![](https://mc.qcloudimg.com/static/img/f6e42dc6f8cbf2ad75e66d31e841ea38/ci-config-demo-1.png)

答案: **填写以项目为根路径的相对路径**

以下面例子中的项目为例，应填写 `qcloud/Dockerfile`

## 构建Demo

*下面通过手动构建一个镜像来说明源码构建功能如何执行镜像构建*

项目结构:

```shell
[root@TENCENT64 ~]# cd demo
[root@TENCENT64 demo]# tree .
.
├── qcloud
│   ├── Dockerfile
│   └── main.js
├── README.md
└── main.js

[root@TENCENT64 ~]#
```

在Dockerfile文件所在目录，有一个空文件`main.js`，
用于验证`ADD`命令拷贝的是根目录下的文件(`main.js`)。

通过`ADD`命令添加文件 `main.js` 到 `/data/`目录。

随后，执行`RUN cat` 命令输出文件内容，验证是否是我们期望添加的文件。

```shell
[root@TENCENT64 ~]# cat qcloud/Dockerfile
FROM node:latest

ADD main.js /data/
RUN cat /data/main.js
CMD ["node", "/data/main.js"]

[root@TENCENT64 demo]# cat /qcloud/main.js

//for test

[root@TENCENT64 demo]#
```

在项目根目录执行构建:

```shell
[root@TENCENT64 demo]# docker build -f qcloud/Dockerfile .
Sending build context to Docker daemon  152.1kB
Step 1/4 : FROM node:latest
 ---> 6cc3b1eca1bc
Step 2/4 : ADD main.js /data/
 ---> 710a9a9bca77
Removing intermediate container 3c62a5cc07a1
Step 3/4 : RUN cat /data/main.js
 ---> Running in 7c1e4a1d8f64
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('hello, world');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
 ---> 4fbe7455964c
Removing intermediate container 7c1e4a1d8f64
Step 4/4 : CMD node /data/main.js
 ---> Running in 57bedd3467c6
 ---> 2668fd5461d2
Removing intermediate container 57bedd3467c6
Successfully built 2668fd5461d2
```

通过 `RUN cat /data/main.js` 命令，可以看到根目录下的文件 `main.js` 被拷贝到 `/data/main.js`。

**腾讯云容器服务源码构建功能的build过程**类似于该demo的构建过程。

## 源码构建功能如何使用Dockerfile ?

源码构建功能首先clone用户指定的仓库，然后在仓库根目录执行 `docker build -f $DOCKERFILE_PATH .` 构建出容器镜像。

## Dockerfile文件中的源路径应该怎么写 ?

对于 `COPY`，`ADD` 等涉及源路径的命令，如果Dockerfile不在项目根目录中，需特别注意源路径应该写成相对于项目根目录的*相对路径*。

## 为什么要在根目录执行构建而不是Dockerfile所在的目录 ?

Dockerfile不允许通过 `..` 引用构建目录之外的文件，
如果我们在该目录下执行构建，那不得不将需要拷贝的文件放在构建目录中，
这并不符合大多数项目的结构。

