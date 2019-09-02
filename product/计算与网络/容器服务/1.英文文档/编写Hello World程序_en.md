This document aims to help create an Node.js "Hello World" service in a container cluster. For more information on how to build a Docker image, please see [How to Build Docker Image](/doc/product/457/9115).

## Step 1: Writing Codes to Create an Image
### Writing Application
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
2. Testing "Hello World" application.
```shell
[root@VM_88_88_centos ~]# node server.js
```
Open a new console and test the application with "curl", or access the application from the browser using "IP address:port". Port is 8080.
```shell
[root@VM_88_88_centos ~]# curl 127.0.0.1:8080
Hello World!
```

### Creating Docker Image
For more information on how to build a Docker image, please see [How to Build Docker Image](/doc/product/457/9115).
1. Create file "Dockerfile" under the "hellonode" folder:
```shell
FROM node:4.4
EXPOSE 8080
COPY server.js .
CMD node server.js
```
2. Build an image using the "Docker build" command
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

### Uploading Image to Tencent Cloud Image Registry
For more information about image operations, please see [Image Registry](/doc/product/457/9117).
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

## Step 2: Creating Service with the Image
### Preconditions
You need to create a cluster first. For more information on how to create a cluster, please see [New Cluster](/doc/product/457/9091).

### Steps
1. Log in to [CCS Console](https://console.cloud.tencent.com/ccs).
2. Click "Service" in the left navigation bar, and click "+ New" in the service list page.
![](//mc.qcloudimg.com/static/img/11f7f75d7b051a815da8bfe1e744a8e8/image.png)
3. Enter basic service information.
 - **Service name**: The name of the service to be created, which is "helloworld" in this example.
 - **Region**: Select a closest region based on your location.
 - **Running cluster**: Select an appropriate cluster and Namespace.
 - **Service description**: Service information. This information is displayed in **Service Information** page.
![](//mc.qcloudimg.com/static/img/a09e01f2f54a5d68720d4078d21e7c46/image.png)
4. Select an image. Enter the name of the running container, which is "helloworld" here. Click [Select Image].
![](//mc.qcloudimg.com/static/img/abb29fc594b5d87d7c475585b1dbe143/image.png)
In **My Image**, enter "helloworld" in the search box, and click "Search". Select "helloworld" in search results, and click [OK].
![](//mc.qcloudimg.com/static/img/3f4e4dada565b815788720fb6436a6c6/image.png)
5. Configuring port mapping. Set the container port to 8080.
![](//mc.qcloudimg.com/static/img/6e2110856cd51efe51431a4a3977e3ea/image.png)
6. Click [Create Service] to complete the creation of "helloworld" service.
>**Note:**
>Keep default settings for other options.

## Accessing "helloworld" Service
1. Click "Service Information" on the service page to check the load balancer ID and load balancer IP. 
![](//mc.qcloudimg.com/static/img/7891c817f167f7726b67615696cfff08/image.png)
2. Accessing "helloworld" service by the following ways.
 - Via load balancer IP.
 - Via **domain name**.
 Copy the domain name by clicking "Load Balance" -> "TCP/UDP" in the left navigation bar of the container console to access the service.
![](//mc.qcloudimg.com/static/img/a1bd366e0154dff0a15c7d062c500699/image.png)
 
3. Enter the IP address in the browser, and you can see "Hello World!".
![](//mc.qcloudimg.com/static/img/ef9e2067f34004f49f7fe1360f20c3a5/image.png)

