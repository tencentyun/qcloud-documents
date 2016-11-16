## Hello World Node.js服务

### 编写应用程序
1.创建一个hellonode的文件夹，加入server.js文件
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
2.测试hello world程序
```shell
[root@VM_88_88_centos ~]# node server.js
```

打开新终端使用curl测试应用程序，或直接浏览器访问IP地址+端口（8080）
```shell
[root@VM_88_88_centos ~]# curl 127.0.0.1:8080
Hello World!
```

到这里helloworld应用程序编写完成

### 创建Docker镜像
制作docker镜像更多详情见：[构建doker镜像教程](待补充)
在hellonode文件夹下，创建Dockerfile文件:
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
更多镜像操作详情见：[镜像仓库基本教程](待补充)
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
### 通过该镜像创建服务
点击创建服务按钮，选择运行集群，填写端口配置，点击创建：
![Alt text](https://mc.qcloudimg.com/static/img/979bd2db10439e2c8b6a31ce01842d66/%7BCEE6F806-ED8C-45FA-8E2E-CC8611FB5537%7D.png)
创建完成后点击服务,查看服务详情，可以通过服务外网IP或负载均衡器域名访问
![Alt text](https://mc.qcloudimg.com/static/img/519490b36fd393d54c6400bda799db1b/%7B8B32B5C8-F46E-4FF6-8931-5A910390B383%7D.png)
在浏览器中输入ip地址，即可看到helloworld
![Alt text](https://mc.qcloudimg.com/static/img/3b69a1b409ea64246e3e2ddd3cf8dadc/%7BA2F39A4B-2E83-4157-BC57-FACB02F30EF2%7D.png)