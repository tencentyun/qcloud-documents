## 操作场景
本文档旨在帮助大家了解如何快速创建一个容器集群内的 Hello World 的 Node.js 版的服务。更多关于如何构建 Docker 镜像的教程可参阅 [如何构建 docker 镜像](https://cloud.tencent.com/document/product/457/9115)。

## 前提条件

- 已创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。
- 已登录节点，且该节点已安装 Node.js。

## 操作步骤
### 编写代码制作镜像
#### 编写应用程序
1. 依次执行以下命令，创建并进入 hellonode 的文件夹。
```shell
mkdir hellonode
```
 ```shell
cd hellonode/
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
 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
4. 执行以下命令，执行 server.js 文件。
```shell
node server.js
```
以下提供两种方式，测试 Hello World 程序。
 - 再次登录节点，执行以下命令。
```shell
curl 127.0.0.1:80
```
 显示如下，则说明 Hello World 程序运行成功。
![](https://main.qcloudimg.com/raw/4b97b9e2fdaee77376b114ef92f90936.png)
 - 打开本地浏览器，以 `IP 地址：端口` 的形式访问，端口为80。
 显示如下，则说明 Hello World 程序运行成功。
![](https://main.qcloudimg.com/raw/1fb82340313ab81dcffd693f9577624d.png)


#### 创建 Docker 镜像
>?更多 Docker 镜像请参见 [如何构建 docker 镜像](https://cloud.tencent.com/document/product/457/9115)。
>
1. 依次执行以下命令，在 hellonode 文件夹下，创建 Dockerfile 文件。
```
cd hellonode
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
按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
3. 执行以下命令，构建镜像。
```shell
docker build -t hello-node:v1 .
```
4. [](id:search)执行以下命令，查看构建好的 hello-node 镜像。
```
docker images 
```
显示结果如下，则说明 hello-node 镜像已成功构建，记录其 IMAGE ID。如下图所示：
![](https://main.qcloudimg.com/raw/d5bf4dfa0f805d6f90399c814b3152b1.png)


#### 上传该镜像到 qcloud 镜像仓库
>!上传镜像需满足以下条件：
>- 已在 [我的镜像](https://console.cloud.tencent.com/tke2/registry/user/space) 创建命名空间。
>- 已登录 [腾讯云 registry](https://cloud.tencent.com/document/product/1141/50332#.E6.8E.A8.E9.80.81.E9.95.9C.E5.83.8F.E5.88.B0.E9.95.9C.E5.83.8F.E4.BB.93.E5.BA.93)，更多镜像操作请参见 [镜像仓库基本教程](https://cloud.tencent.com/document/product/457/9117)。

依次执行以下命令，上传镜像到 qcloud 镜像仓库。
```shell
sudo docker tag IMAGEID ccr.ccs.tencentyun.com/命名空间/helloworld:v1
```
```
sudo docker push ccr.ccs.tencentyun.com/命名空间/helloworld:v1
```
>?
>- 请将命令中的 IMAGEID 替换为 [查看镜像](#search) 中记录的 IMAGEID。
>- 请将命令中的命名空间替换为您已创建的命名空间。
>
显示以下结果，则说明镜像上传成功。
![](https://main.qcloudimg.com/raw/1aadc58e8663488200e3e34a532642c4.png)


### 通过该镜像创建 Hello World 服务
>!在创建使用 Hello World 服务之前，您必须拥有：
>- 已注册腾讯云账户，请前往 [注册页面](https://cloud.tencent.com/register) 填写相关信息注册腾讯云账户。
>- 已创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。
>
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，选择需创建服务的集群 ID，进入集群的工作负载 “Deployment” 页面并单击**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/19997a6644943a2c6ec1587404eb8ca0.png)
3. 在“新建Workload” 页面，根据以下信息，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/c159a688ff1f40022ca46269591ca159.png)
 - **工作负载名**：输入要创建的工作负载的名称，本文以 helloworld 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **helloworld**。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volumne 管理](https://cloud.tencent.com/document/product/457/31713)。
4. 参考以下信息设置“实例内容器”。如下图所示：
输入实例内容器名称，本文以 helloworld 为例
![](https://main.qcloudimg.com/raw/483f16423c0119de4f8f7a24699acdca.png)
单击**选择镜像**，在弹出框中选择**我的镜像**，通过搜索框功能查找出 helloworld 镜像，并单击 **确定**。如下图所示：
![](https://main.qcloudimg.com/raw/1e405dfbead6c6ae96d16c33fc0aa175.png)
主要参数信息如下：
 - **镜像版本（Tag）**：使用默认值 v1。
 - **镜像拉取策略**：提供以下3种策略，请按需选择，本文以不进行设置使用默认策略为例。
若不设置镜像拉取策略，当镜像版本为空或 `latest` 时，使用 Always 策略，否则使用 IfNotPresent 策略。
    - **Always**：总是从远程拉取该镜像。
    - **IfNotPresent**：默认使用本地镜像，若本地无该镜像则远程拉取该镜像。
    - **Never**：只使用本地镜像，若本地没有该镜像将报异常。
5. 在“实例数量”中，根据以下信息设置服务的实例数量。如下图所示：
![](https://main.qcloudimg.com/raw/08f24d05d98670d6c2566d688388941f.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容](https://cloud.tencent.com/document/product/457/14209)。
6.   根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://main.qcloudimg.com/raw/3f722201e228c2bebc63cad0ea3d76c7.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“提供公网访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，将容器端口和服务端口都设置为80 。
 >!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题，详情请参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
7. 单击**创建Workload**，完成 Hello World 服务的创建。

### 访问 Hello World 服务
可通过以下两种方式访问 Hello World 服务。

#### 通过负载均衡 IP 访问 Hello World 服务
1. 单击左侧导航栏中 **[集群](https://console.cloud.tencent.com/tke2/cluster)**，进入 “集群管理” 页面。
2. 单击 Hello World 服务所在的集群 ID，选择**服务** > **Service**。
3. 在服务管理页面，复制 helloworld 服务的负载均衡 IP，如下图所示：
![](https://main.qcloudimg.com/raw/3b570e8ab6180118c1ecba68349efe5b.png)

#### 通过服务名称访问 Hello World 服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 Hello World 服务
访问服务时显示如下，则 Hello World 服务创建成功。
![](https://main.qcloudimg.com/raw/817c981526ac6297c778c1cb154a8d90.png)
若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。
