# Guide on Dockerfile Path for Building with Source Code

Tencent CCS provides the capability of auto image building. In the configuration of building with source code, you can specify the path of Dockerfile. This document describes the relationship between the path and image building.

## How to Specify Dockerfile Path for Building with Source Code?

![](https://mc.qcloudimg.com/static/img/f6e42dc6f8cbf2ad75e66d31e841ea38/ci-config-demo-1.png)

Answer:  **Enter the relative path whose root path is the project name**

For example, for the project in the example below, you should enter `qcloud/Dockerfile`

## Building Demo

*Here, we manually build an image to show you how to do this through the feature of building with source code.*

Project structure:

```shell
[root@TENCENT64 ~]# cd demo
[root@TENCENT64 demo]# tree .
.
├── qcloud
│   ├── Dockerfile
│   └── main.js
├── README.md
└── main.js

[root@TENCENT64 ~]#
```

There is an empty file `main.js` in the directory where the Dockerfile is located.
This file is used to verify whether the file copied by command `ADD` is the one (`main.js`) in root directory.

Add the file `main.js` to the directory `/data/` via command `ADD`.

Then, execute command `RUN cat` to output the file content, so as to verify whether it is the file to be added.

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

Build image in the root directory of the project:

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

By executing the command `RUN cat /data/main.js`, you can see the file `main.js` in root directory is copied to `/data/main.js`.

**The process of building with source code of Tencent CCS** is similar to the demo building process.

## How to Use Dockerfile for Building with Source Code?

To implement the feature of building images with source code, you first need to clone the user-specified repository, and execute the command `docker build -f $DOCKERFILE_PATH` in the root directory of repository to build a container image.

## How to Specify the Source Path in Dockerfile?

For `COPY`, `ADD` and other commands related to source path, if Dockerfile is not in the project's root directory, you need to note that the source path should be a *relative path* to the project's root directory.

## Why Build an Image in Root Directory Instead of the Directory Where Dockerfile is Located?

Dockerfile does not allow users to use `..` to reference files outside the building directory.
If we build images in this directory, we have to add the copied file to the building directory.
This does not meet the structural requirements of most projects.


