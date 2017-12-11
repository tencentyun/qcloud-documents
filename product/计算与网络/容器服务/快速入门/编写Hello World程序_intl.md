## Description
This document shows how to quickly create an Node.js "hello world" service in a container cluster. For more information about how to build a Docker image, please see [Build a Docker Image](https://cloud.tencent.com/document/product/457/7208).

You can view [Instructions](https://cloud.tencent.com/document/product/457/6781#.E6.8E.A8.E9.80.81.E9.95.9C.E5.83.8F.E5.88.B0.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93) in "My Image" to learn about how to upload images to Tencent Cloud image warehouse.

## Step 1: Write Code to Create an Image
### Write Application
1. Create a folder named "hellonode" and add file "server.js" to it.
```shell
[root@VM_88_88_centos ~]# mkdir hellonode
[root@VM_88_88_centos ~]# cd hellonode/
[root@VM_88_88_centos hellonode]# vim server.js
[root@VM_88_88_centos hellonode]# ls
server.js
```

	File "server.js" is shown below:
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
2. Test the application "hello world".
```shell
[root@VM_88_88_centos ~]# node server.js
```

	Open a new console and test the application with "curl", or access the application from the browser using "<IP address:port>". Port is 8080.

	```shell
	[root@VM_88_88_centos ~]# curl 127.0.0.1:8080
	Hello World!
	```

	Here, you have completed the "helloworld" application.

### Create Docker Image
For more information about how to create a Docker image, please see [Build Docker Image](https://cloud.tencent.com/document/product/457/7208).
Create file "Dockerfile" under the "hellonode" folder:
```shell
FROM node:4.4
EXPOSE 8080
COPY server.js .
CMD node server.js
```
Build image using the "Docker build" command
```shell
[root@VM_88_88_centos hellonode]# vim Dockerfile 
[root@VM_88_88_centos hellonode]# ls
Dockerfile server.js
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

### Upload Image to Tencent Cloud Image Warehouse
For more information about image operations, please see [Image Warehouse Basic Instruction](https://cloud.tencent.com/document/product/457/6781).
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

## Step 2: Create Cluster
First, you need a cluster where containers can run. If you have no cluster, you need to create one. For more information, please see [Create Cluster](https://cloud.tencent.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4).

## Step 3: Create a Service with the Image
Click the "Create Service" button, choose the cluster to run the service, enter port configuration and click "Create":
![Alt text](https://mc.qcloudimg.com/static/img/814ed6eaf9ca44126e1c50c0866a4ae9/examples_2_1.jpg)

You will be redirected to the event list where you can view the details of the creation process.
![Alt text](https://mc.qcloudimg.com/static/img/620cd9c69e4319b5050ae063c2609881/examples_2_2.jpg)
![Alt text](https://mc.qcloudimg.com/static/img/d71e64acf8e996891979ddaa1cb14533/examples_2_3.jpg)

When creation is completed, click the service to view its details. You can access the service through its public IP or load balancer domain.
![Alt text](https://mc.qcloudimg.com/static/img/62def9ed65f1d0b1172325ded2b248fe/examples_2_4.jpg)

Enter the IP address in the browser, you will see "Hello World!"
![Alt text](https://mc.qcloudimg.com/static/img/1342aa5ff1575e683ef2ed813b872721/Image+034.png)
