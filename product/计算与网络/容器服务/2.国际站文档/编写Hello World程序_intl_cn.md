本文档旨在帮助大家了解如何快速创建一个容器集群内的 Hello World 的 Node.js 版的服务。更多关于如何构建 Docker 镜像的教程可参阅  [如何构建 Docker镜像](/doc/product/457/9115) 。

## 第一步：编写代码制作镜像
### 编写应用程序
1. 创建一个 hellonode 的文件夹，加入 server.js 文件。
```shell
[root@VM_88_88_centos ~]# mkdir hellonode
[root@VM_88_88_centos ~]# cd hellonode/
[root@VM_88_88_centos hellonode]# vim server.js
[root@VM_88_88_centos hellonode]# ls
server.js
```
server.js 文件如下：
```js
var http = require('http');
var handleRequest = function(request, response) {
  console.log('Received request for URL: ' + request.url);
  response.writeHead(200);
  response.end('Hello World!');
};
var www = http.createServer(handleRequest);
www.listen(8080);
```
2. 测试 Hello World 程序。
```shell
[root@VM_88_88_centos ~]# node server.js
```
打开新终端使用 curl 测试应用程序，或在浏览器以 IP 地址：端口的形式访问，端口为 8080 。
```shell
[root@VM_88_88_centos ~]# curl 127.0.0.1:8080
Hello World!
```

### 创建 Docker 镜像
构建 Docker 镜像更多详情见：[如何构建 Docker 镜像](/doc/product/457/9115) 。
1. 在 hellonode 文件夹下，创建 Dockerfile 文件：
```shell
FROM node:4.4
EXPOSE 8080
COPY server.js .
CMD node server.js
```
2. 通过 Docker build 命令构建镜像
```shell
[root@VM_88_88_centos hellonode]# vim Dockerfile 
[root@VM_88_88_centos hellonode]# ls
Dockerfile  server.js
[root@VM_88_88_centos hellonode]# docker build -t hello-node:v1 .
Sending build context to Docker daemon 3.072 kB
Step 1 : FROM node:4.4
Trying to pull repository docker.io/library/node ... 
4.4: Pulling from docker.io/library/node
......
......
Removing intermediate container 1e8d01dc319f
Successfully built 027232e62e3f
[root@VM_88_88_centos hellonode]# docker images 
REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
hello-node                                     v1                  027232e62e3f        54 minutes ago      647.4 MB
```

### 上传该镜像到 qcloud 镜像仓库
更多镜像操作详情见：[镜像仓库基本教程](/doc/product/457/9117) 。
```shell
[root@VM_3_224_centos hellonode]# sudo docker tag 027232e62e3f ccr.ccs.tencentyun.com/test/helloworld:v1
[root@VM_3_224_centos hellonode]# sudo docker push ccr.ccs.tencentyun.com/test/helloworld:v1
The push refers to a repository [ccr.ccs.tencentyun.com/test/helloworld]
1b8da8805305: Pushed 
20a6f9d228c0: Pushed 
80c332ac5101: Pushed 
04dc8c446a38: Pushed 
1050aff7cfff: Pushed 
66d8e5ee400c: Pushed 
2f71b45e4e25: Pushed 
v1: digest: sha256:38b194feeee09abf8ee45e7abca82b9fe494b18b953c771ce8ebefa387107be9 size: 1772
```

## 第二步：通过该镜像创建服务
### 前提条件
如果之前没有创建过集群，您需要先创建集群。有关如何创建集群的详细信息，参见 [新建集群](/doc/product/457/9091) 。

### 操作步骤
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的【服务】，在服务列表页单击【+新建】。
![](//mc.qcloudimg.com/static/img/11f7f75d7b051a815da8bfe1e744a8e8/image.png)
3. 填写服务的基本信息。
 - **服务名称**：要创建的服务的名称。本例中，服务名称为 helloworld。
 - **所在地域**：建议您根据所在地理位置选择靠近的地域。
 - **运行集群**：选择合适的集群和 Namespace。
 - **服务描述**：服务的相关信息。该信息将显示在 **服务信息** 页面。
![](//mc.qcloudimg.com/static/img/a09e01f2f54a5d68720d4078d21e7c46/image.png)
4. 选择镜像。输入运行容器的名称，此处以 helloworld 为例。单击【选择镜像】 。
![](//mc.qcloudimg.com/static/img/abb29fc594b5d87d7c475585b1dbe143/image.png)
在 **我的镜像** 下，在搜索框中输入 helloworld，单击搜索。在搜索结果中选择 helloworld，单击 【确定】。
![](//mc.qcloudimg.com/static/img/3f4e4dada565b815788720fb6436a6c6/image.png)
5. 设置端口映射。将容器端口设置为 8080 。
![](//mc.qcloudimg.com/static/img/6e2110856cd51efe51431a4a3977e3ea/image.png)
6. 单击【创建服务】。完成 helloworld 服务的创建。
>**注意：**
>其他选项保持为默认设置。

## 访问 helloworld 服务
1. 单击服务页面的【服务信息】查看负载均衡 ID 和负载均衡 IP 。 
![](//mc.qcloudimg.com/static/img/7891c817f167f7726b67615696cfff08/image.png)
2. 提供两种种方式访问  helloworld 服务。
 - 通过负载均衡 IP 来访问  helloworld 服务。
 - 通过 **域名** 来访问  helloworld 服务。
 在容器服务控制台左侧导航栏中，单击【负载均衡】，单击【TCP/UDP】，复制域名访问服务。
![](//mc.qcloudimg.com/static/img/a1bd366e0154dff0a15c7d062c500699/image.png)
 
3. 在浏览器中输入 IP 地址，即可看到 Hello World！
![](//mc.qcloudimg.com/static/img/ef9e2067f34004f49f7fe1360f20c3a5/image.png)
