## 操作场景
本文档介绍如何快速创建一个基于容器服务开源版（TKE Stack）集群内的 Node.js 版的 Hello World 服务。



## 前提条件

- 已部署 TKEStack 控制台，详情请参见 [控制台安装](https://cloud.tencent.com/document/product/1205/43828#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.AE.89.E8.A3.85)。
- 已创建集群，详情请参见 [新建独立集群](https://cloud.tencent.com/document/product/1205/43828#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E6.96.B0.E5.BB.BA.E7.8B.AC.E7.AB.8B.E9.9B.86.E7.BE.A4)。
- 由于 Master 节点的预设置，请参考 [添加节点](https://cloud.tencent.com/document/product/1205/43828#addNode) 步骤，向集群中增加节点后再创建服务。
- 已登录节点，且该节点已安装 Node.js。

## 操作步骤
### 编写代码制作镜像
#### 编写应用程序
1. 依次执行以下命令，创建并进入 helloworld 的文件夹。
```shell
mkdir helloworld
```
```
cd helloworld/
```
2. 执行以下命令，新建并打开 server.js 文件。
```
vim server.js
```
3. 按 **i** 切换至编辑模式，将以下内容输入 server.js。
```js
var http = require('http');
var handleRequest = function(request, response) {
  console.log('Received request for URL: ' + request.url);
  response.writeHead(200);
  response.end('Hello World!');
};
var www = http.createServer(handleRequest);
www.listen(80);
```
4. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，执行 server.js 文件。
```shell
node server.js
```
可通过以下两种方式，测试 Hello World 程序。
 - 再次登录节点，执行以下命令。
```shell
curl 127.0.0.1:80
```
显示如下，则说明 Hello World 程序运行成功。
![](https://main.qcloudimg.com/raw/d784c0301f19f9bf5cb735b373bd58d5.png)
 - 打开浏览器，以节点 IP 地址：端口的形式访问，端口为80。
显示如下，则说明 Hello World 程序运行成功。
![](https://main.qcloudimg.com/raw/cde29bf2b18dca76b6c87db7a598062e.png)


#### 创建 Docker 镜像
1. 依次执行以下命令，在 helloworld 文件夹下，创建 Dockerfile 文件。
```
cd /helloworld
```
```
vim Dockerfile
```
2. 按 **i** 切换至编辑模式，将以下内容输入 Dockerfile 文件。
```shell
FROM node:4.4
EXPOSE 80
COPY server.js .
CMD node server.js
```
按 **Esc**，输入 **:wq**，保存文件并返回。
3. 执行以下命令，构建镜像。
```shell
docker build -t helloworld:v1 .
```
4. <span id="search">执行以下命令，查看构建好的 helloworld 镜像。</span>
```
docker images | grep ^helloworld
```
显示结果如下，则说明 helloworld 镜像已成功构建，记录其 IMAGE ID。如下图所示：
![](https://main.qcloudimg.com/raw/209f1971dea72af32ce0a1747bfb0522.png)

#### 上传镜像到镜像仓库
>!请参考 [创建命名空间](#createNamespace) 及 [创建访问凭证](#accessCredentials)，准备可用的镜像仓库。
>
1. 执行以下命令，登录镜像仓库。
```
sudo docker login -u tkestack -p 访问凭证 default.registry.tke.com
```
请将命令中的“访问凭证”替换为您已获取的访问凭证。
2. 依次执行以下命令，上传镜像到仓库。
```shell
sudo docker tag IMAGEID default.registry.tke.com/命名空间/helloworld:v1
```
```
sudo docker push default.registry.tke.com/命名空间/helloworld:v1
```
	- 请将命令中的 IMAGEID 替换为 [查看镜像](#search) 中已获取的 IMAGE ID。
	- 请将命令中的“命名空间”替换为已创建的命名空间。
显示以下结果，则说明镜像上传成功。
![](https://main.qcloudimg.com/raw/d43bddd9198a6deb62581b4f099076a9.png)



#### 在镜像仓库命名空间中进行确认
1. 登录 TKEStack 控制台，选择左侧导航栏中的【组织资源】>【镜像仓库管理】。
2. 在“命名空间”页面，选择命名空间名称。
3. 在该命名空间的“镜像列表”下，可查看已成功上传的镜像。如下图所示：
![](https://main.qcloudimg.com/raw/6e367c0cb9c7c0c41edb435af71925b3.png)



### 通过该镜像创建 Hello World 服务
1. 选择左侧导航栏中【集群管理】，进入“集群管理”页面。
2. 单击需要创建服务的集群 ID，进入工作负载 “Deployment” 页面。
3. 在 “Deployment” 页面中，单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/a45f80e8c8ce02f5977da3b5a3b6164d.png)
4. 在 “新建Workload” 页面，根据以下提示，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/55d40b7b13606d7a50d0c10c91d360ff.png)
 - **工作负载名**：输入要创建的工作负载的名称，本文以 helloworld 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **helloworld**。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷。
5. 在“实例内容器”中，参考以下信息进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/0289030b9ac4006b4cdff5d3ab9bf7ad.png)
主要参数信息如下：
	- **名称**：输入 helloworld。
	- **镜像**：输入 default.registry.tke.com/命名空间/helloworld。本文以 default.registry.tke.com/test/helloworld 为例。
	- **镜像版本（Tag）**：输入 v1。
其余选项请保持默认设置。
7. 在“实例数量”中，参考以下信息设置服务的实例数量。如下图所示：
![](https://main.qcloudimg.com/raw/24fd3b152d94f5ca2f7170dc06e3eeda.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击`+`或`-`控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。
8.  根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://main.qcloudimg.com/raw/a5f3c1270c3ce46e70cdfebd5df30bb9.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“主机端口访问”。
 - **端口映射**：选择 TCP 协议，将容器端口和服务端口都设置为80，主机端口设为30001。
 >!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题。
9. 单击【创建Workload】，完成 Hello World 服务的创建。

### 访问 Hello World 服务
可通过以下两种方式访问 Hello World 服务。

#### 通过主机节点端口访问 Hello World 服务
1. 单击左侧导航栏中【集群管理】，进入“集群管理”页面。
2. 选择 Nginx 服务所在的集群 ID，进入该集群 “Deployment” 页面。
3. 选择左侧菜单栏中的【服务】>【Service】，进入 “Service” 页面。
3. 在 “Service” 页面，可查看 Hello world 已经运行，如下图所示：
![](https://main.qcloudimg.com/raw/5c12ca6f74d98d6d753d3a7eaa816552.png)
4. 在浏览器地址栏访问集群任意节点 IP 的30001端口即可访问服务。

#### 通过服务名称访问 Hello World 服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 Hello World 服务
访问服务时显示如下，则 Hello World 服务创建成功。
![](https://main.qcloudimg.com/raw/34f065f69409928229f691b9b014220f.png)


## 相关操作
### 创建命名空间<span id="createNamespace"></span>
1. 选择 TKEStack 控制台左侧导航栏中的【组织资源】>【镜像仓库管理】。
2. 在“命名空间”页面，单击【新建】。
3. 在打开的“新建命名空间”页面，参考以下信息进行填写。如下图所示：
>?命名空间将用于分类容器镜像，也是您创建的私人镜像地址的前缀。
>
![](https://main.qcloudimg.com/raw/51f34479b66c5cffd06b95f0a42cbf0b.png)
 - **名称**：自定义命名空间名称，本文以 test 为例。
 - **权限类型**：支持【公有】和【私有】，本文以选择【私有】为例。
4. 单击【确认】即可成功创建。


### 创建访问凭证<span id="accessCredentials"></span>
1. 选择 TKEStack 控制台左侧导航栏中的【组织资源】>【访问凭证】。
2. 在“访问凭证”页面，单击【新建】。
3. 在打开的“创建访问凭证”页面，按需选择凭证有效时间，并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/8065813ccaca5060aca3c4bd79a027b2.png)
