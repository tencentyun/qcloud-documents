## 操作场景
本文以 [原 TKE 控制台](https://console.cloud.tencent.com/tke) 为例进行操作，快速创建一个容器集群内的 Hello World 的 Node.js 版的服务。

## 前提条件
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建集群。关于创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/9091#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4)。
- 已 [登录节点](https://cloud.tencent.com/document/product/457/9091#.E7.99.BB.E5.BD.95.E5.88.B0.E8.8A.82.E7.82.B9)。
- 该节点已安装 Node.js。

## 操作步骤
### 编写代码制作镜像
#### 编写应用程序
1. 依次执行以下命令，创建一个 hellonode 的文件夹，创建 server.js 文件。
```shell
[root@VM_88_88_centos ~]# mkdir hellonode
[root@VM_88_88_centos ~]# cd hellonode/
[root@VM_88_88_centos hellonode]# vim server.js
```
2. 按 “**i**” 进入编辑模式，并向 server.js 文件输入以下内容。
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
输入完成后，按 “**Esc**” 退出编辑模式，并输入 “**：wq**” 保存并退出。
3. 通过以下三种方式可测试 Hello World 程序。
 - 执行以下命令，测试程序。
```shell
[root@VM_88_88_centos ~]# node server.js
```
 - 打开新终端，执行以下命令使用 curl 测试程序。
```shell
[root@VM_88_88_centos ~]# curl 127.0.0.1:8080
Hello World!
```
 - 在浏览器地址栏输入 `节点 IP 地址：端口`的形式访问，端口为8080 。

#### 创建 Docker 镜像
>?更多关于构建 Docker 镜像，详情请参见 [如何构建 Docker 镜像](https://cloud.tencent.com/document/product/457/9115) 。
>
1. 执行以下命令，在 hellonode 文件夹下，创建 Dockerfile 文件。
```
[root@VM_88_88_centos hellonode]# vim Dockerfile 
```
按 “**i**” 进入编辑模式，并向 Dockerfile 文件输入以下内容：
```shell
FROM node:4.4
EXPOSE 8080
COPY server.js .
CMD node server.js
```
按 “**Esc**” 退出编辑模式，并输入 “**：wq**” 保存并退出。
2. 执行以下命令，构建镜像。
```shell
[root@VM_88_88_centos hellonode]# docker build -t hello-node:v1 .
Sending build context to Docker daemon 3.072 kB
Step 1 : FROM node:4.4
Trying to pull repository docker.io/library/node ... 
4.4: Pulling from docker.io/library/node
......
......
Removing intermediate container 1e8d01dc319f
Successfully built 027232e62e3f
```
<span id = "step3"></span>
3. 执行以下命令，查看 docker 下的所有镜像。
```
[root@VM_88_88_centos hellonode]# docker images 
REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
hello-node                                     v1                  027232e62e3f        54 minutes ago      647.4 MB
```

#### 上传该镜像到 qcloud 镜像仓库
依次执行以下命令，上传镜像至仓库。
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
>?
>- 其中 `027232e62e3f` 为 [查看镜像](#step3) 中，hello-node 镜像的 IMAGE ID。 
>- 其中 `test` 为已创建的命名空间名。
>- 更多镜像操作，详情请参见 [镜像仓库基本教程](https://cloud.tencent.com/document/product/457/9117) 。
>

### 通过该镜像创建 Hello World 服务
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke) 。
2. 单击左侧导航栏中的【服务】，选择服务列表页上方的【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/52a50479664ee2649d8531184489e8c9.png)
3. 设置服务的基本信息。如下图所示：
 - **服务名称**：要创建的服务的名称。服务名称由小写字母、数字和 - 组成，且由小写字母开头，小写字母或数字结尾。本例中服务名称为 helloworld。
 - **所在地域**：选择运行该服务集群所在的地域。
 - **运行集群**：选择服务所要运行的集群，选择运行中和集群内有可用主机的集群。
 - **服务描述**：创建服务的相关信息。该信息将显示在**服务信息**页面。
>!其他选项保持为默认设置。
>
![](https://main.qcloudimg.com/raw/c12ebf0d45f9cd9ef0f9b8d2f7e78065.png)
4. 选择镜像。输入运行容器的名称（以 helloworld 为例）后，单击【选择镜像】 。如下图所示：
![](https://main.qcloudimg.com/raw/a3010cf2a7087f9bdc58edcf45706322.png)
在**我的镜像**下，选择 helloworld 镜像，单击 【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/afde48cc67327ca134325dd810f98089.png)
5. 设置端口映射。将容器端口和服务端口都设置为80 。如下图所示：
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题。详情参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
>
![](https://mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)
6. 单击**创建服务**，即可完成 Hello World 服务的创建。


### 访问 Hello World 服务
可通过以下三种方式访问 Hello World 服务。
#### 通过负载均衡 IP 来访问 Hello World 服务
1. 进入集群 [服务列表](https://console.cloud.tencent.com/tke/service/detail/container) 页。
2. 单击【服务信息】查看负载均衡 IP 。 如下图所示：
![](https://main.qcloudimg.com/raw/77bf09bfc20d7231e7234c9dd55a65cc.png)
3. 在浏览器地址栏输入负载均衡 IP，按 “**Enter**” 即可访问服务。

#### 通过域名来访问 Hello World 服务
1. 进入服务信息详情页，单击服务的负载均衡 ID。如下图所示：
![](https://main.qcloudimg.com/raw/09b369258510f6c2eb0f573a40735a14.png)
2. 进入负载均衡详情页，查看域名。如下图所示：
![](https://main.qcloudimg.com/raw/19421ac01769cb5158aecbb92bd3d0aa.png)
3. 在浏览器地址栏输入该域名，按 “**Enter**” 即可访问服务。

#### 通过服务名称访问服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 Hello World 服务
服务创建成功，访问服务时直接进入 Hello World 服务器的欢迎页。如下图所示：
![](https://mc.qcloudimg.com/static/img/ef9e2067f34004f49f7fe1360f20c3a5/image.png)


若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。
