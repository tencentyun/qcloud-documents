## 说明
本文旨在帮助大家了解如何快速创建一个容器集群内的hello world的Node.js版的服务，更多关于如何构建Docker镜像的教程可参考[构建Docker镜像](https://www.qcloud.com/document/product/457/7208)。

如何上传镜像到到腾讯云镜像仓库，可在我的镜像中查看[使用指引](https://www.qcloud.com/document/product/457/6781#.E6.8E.A8.E9.80.81.E9.95.9C.E5.83.8F.E5.88.B0.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93)。

## 第一步：编写代码制作镜像
### 编写应用程序
1.创建一个hellonode的文件夹，加入server.js文件。
```shell
[root@VM_88_88_centos ~]# mkdir hellonode
[root@VM_88_88_centos ~]# cd hellonode/
[root@VM_88_88_centos hellonode]# vim server.js
[root@VM_88_88_centos hellonode]# ls
server.js
```

server.js文件如下：
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
2.测试hello world程序。
```shell
[root@VM_88_88_centos ~]# node server.js
```

打开新终端使用curl测试应用程序，或在浏览器以IP地址：端口的形式访问，端口为8080。
```shell
[root@VM_88_88_centos ~]# curl 127.0.0.1:8080
Hello World!
```

到这里helloworld应用程序编写完成。

### 创建Docker镜像
制作Docker镜像更多详情见：[构建Docker镜像教程](https://www.qcloud.com/document/product/457/7208)。
在hellonode文件夹下，创建Dockerfile文件：
```shell
FROM node:4.4
EXPOSE 8080
COPY server.js .
CMD node server.js
```
通过Docker build命令构建镜像
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

### 上传该镜像到qcloud 镜像仓库
更多镜像操作详情见：[镜像仓库基本教程](https://www.qcloud.com/document/product/457/6781)。
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

## 第二步：创建集群
1.首先要拥有一个可运行容器的集群。如无集群新建一个集群，详情查看[新建集群](https://www.qcloud.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4)。

## 第三步：通过该镜像创建服务
点击【创建服务】按钮，选择运行集群，填写端口配置，点击【创建】：
![Alt text](https://mc.qcloudimg.com/static/img/cb114031ca66d0c126ee92a6671f6eb5/Image+073.png)

跳转到事件列表，可查看具体创建流水。
![Alt text](https://mc.qcloudimg.com/static/img/7121a486db35c98a81e8e1408e97b585/Image+074.png)
![Alt text](https://mc.qcloudimg.com/static/img/922306ca4c4524e7113802d0840be86d/Image+075.png)

创建完成后点击服务,查看服务详情，可以通过服务外网IP或负载均衡器域名访问。
![Alt text](https://mc.qcloudimg.com/static/img/81e12259e6947039374295a7f838e298/Image+076.png)

在浏览器中输入IP地址，即可看到Hello World！
![Alt text](https://mc.qcloudimg.com/static/img/1342aa5ff1575e683ef2ed813b872721/Image+034.png)
