## 操作场景

本文介绍了 Dubbo 应用托管到腾讯云容器服务 TKE 的最佳实践。

#### Dubbo 应用托管到 TKE 的优势

- 提升资源利用率。
- Kubernetes 天然适合微服务架构。
- 提升运维效率，便于 Devops 落地实施。
- Kubernetes 的高弹性，可轻松实现应用的动态扩缩容。
- 容器服务 TKE 提供 Kubernetes Master 托管功能，可减少 Kubernetes 集群运维和管理的负担。
- 容器服务 TKE 和腾讯云的其他云原生产品进行了整合和优化，帮助用户更好的使用腾讯云上产品。


## 最佳实践实例介绍
本文以 Q 云书城（Q Cloud Book Mall，QCBM）项目为最佳实践实例，详细介绍 Dubbo 应用托管到 TKE 的过程。


### QCBM 概述


QCBM 首页如下图展所示：
![](https://main.qcloudimg.com/raw/958f718bb6e1656449e8bcdd9dd88ae2.png)

QCBM 是采用微服务架构，并使用 dubbo-2.7.8 框架开发的一个网上书城 Demo 项目。QCBM 的部署和代码托管在 Coding，详情可参见 [QCBM 项目](https://github.com/TencentCloud/container-demo/tree/main/dubbo-on-tke)。QCBM 包含以下微服务：


| 微服务                          | 说明                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| QCBM-Front                      | 使用 React 开发的前端项目，基于 Nginx 官方提供的 [1.19.8 Docker 镜像](https://hub.docker.com/_/nginx) 构建和部署。 |
| QCBM-Gateway                    | API 网关，接受前端的 HTTP 请求，并将其转化为后台的 Dubbo 请求。  |
| User-Service                    | 基于 Dubbo 的微服务，提供用户注册、登录、鉴权等功能。        |
| Favorites-Service             | 基于 Dubbo 的微服务，提供用户图书收藏功能。                  |
| Order-Service                   | 基于 Dubbo 的微服务，提供用户订单生成和查询等功能。          |
| Store-Service                   | 基于 Dubbo 的微服务，提供图书信息的存储等功能。              |



#### QCBM 架构和组件

本文最佳实践实例模拟将原先部署在云服务器 CVM 的应用进行容器化，并托管到容器服务 TKE 的场景。在该场景中需要采用一个 VPC，并划分为以下两个子网：
- **Subnet-Basic**：部署有状态的基础服务，包括 Dubbo 的服务注册中心 Nacos、MySQL 和 Redis 等。
- **Subnet-K8S**：部署 QCBM 的应用服务，所有服务都进行容器化，并运行在容器服务 TKE 上。

子网划分如下图所示：
![](https://main.qcloudimg.com/raw/e0cd362e05f73d3a5236d34febe02708.jpeg)

QCBM 实例的网络规划如下表所示：

| 网络规划                       | 说明                                                         |
| :----------------------------- | :----------------------------------------------------------- |
| Region/AZ                      | 南京/南京一区                                                |
| VPC                            | CIDR：10.0.0.0/16                                            |
|子网 Subnet-Basic | 南京一区，CIDR：10.0.1.0/24                                  |
| 子网 Subnet-K8S                | 南京一区，CIDR：10.0.2.0/24                                  |
| Nacos 集群                     | 采用3台 “标准型SA2” 1C2G 机型的 CVM 构建 Nacos 集群，对应的 IP 为：10.0.1.9，10.0.1.14，10.0.1.15 |

QCBM 实例中用到的组件如下表所示：

| 组件  | 版本  |         来源          | 备注                                                         |
| :---- | :---: | :-------------------: | :----------------------------------------------------------- |
| k8s   | 1.8.4 |        腾讯云         | TKE 托管模式                                                 |
| MySQL |  5.7  |        腾讯云         | TencentDB for MySQL 双节点                                   |
| Redis |  5.0  |        腾讯云         | TencentDB for Redis 标准型                                   |
| CLS   |  N/A  |        腾讯云         | 日志服务                                                     |
| TSW   |  N/A  |        腾讯云         | 采用 Skywalking 8.4.0 版的 Agent 接入，点此 [下载](https://archive.apache.org/dist/skywalking/8.4.0/apache-skywalking-apm-es7-8.4.0.tar.gz) |
| Java  |  1.8  |       开源社区        | Docker 镜像为 java:8-jre                                     |
| Nacos | 2.0.0 |       开源社区        | 点此 [下载](https://github.com/alibaba/nacos/releases/download/2.0.0-bugfix/nacos-server-2.0.0.tar.gz) |
| Dubbo | 2.7.8 | 开源社区| [Github 地址](https://github.com/apache/dubbo)               |


## 服务介绍
### TCR 介绍

腾讯云 [容器镜像服务 TCR](https://cloud.tencent.com/product/tcr) 提供个人版和企业版两种镜像仓库。两者区别如下图所示：
![](https://main.qcloudimg.com/raw/169e2d9b46f59b2eeb58a935dc5e0c30.jpeg)


QCBM 是一个 Dubbo 容器化的 Demo 项目，因此容器镜像服务个人版完全满足需求。但对于企业用户，推荐使用 [容器镜像服务企业版](https://cloud.tencent.com/document/product/1141/39287)。如需使用镜像仓库，请参见 [镜像仓库基本操作](https://cloud.tencent.com/document/product/1141/41811)。


### TSW 介绍

[腾讯微服务观测平台 TSW](https://console.cloud.tencent.com/apm)（Tencent Service Watcher）提供云原生服务可观察性解决方案，能够追踪到分布式架构中的上下游依赖关系，绘制拓扑图，提供服务、接口、实例、中间件等多维度调用观测。详细介绍如下图所示：
![](https://main.qcloudimg.com/raw/6f66070b3859087a2350215d0fb281b9.jpeg)

TSW 在架构上分为以下四大模块：
<dx-accordion>
::: 数据采集（Client）
使用开源探针或 SDK 用于采集数据。对于迁移上云的用户，可保留 Client 端的大部分配置，仅更改上报地址和鉴权信息即可。
:::
::: 数据处理（Server）
  数据经由 Pulsar 消息队列上报到 Server，同时 Adapter 会将数据转换为统一的 Opentracing 兼容格式。根据数据的使用场景，分配给实时计算与离线计算：
	- 实时计算提供实时监控、统计数据展示，并对接告警平台快速响应。
	- 离线计算处理长时段大量数据的统计汇聚，利用大数据分析能力提供业务价值。
:::
::: 存储（Storage）
存储层可满足不同数据类型的使用场景，适配 Server 层的写入与 Data Usage 层的查询与读取请求。
:::
::: 数据使用（Data\sUsage）
为控制台操作、数据展示、告警提供底层支持。
:::
</dx-accordion><br>

架构图如下所示：
![](https://main.qcloudimg.com/raw/8ad0a1b76bdda3c101cc4505c3952242.png)











## 操作步骤

### 搭建基础服务集群

- 在 [Mysql 控制台](https://console.cloud.tencent.com/cdb) 创建实例，并使用 [qcbm-ddl.sql](https://tencent-cloud-native.coding.net/public/qcbm-k8s/qcbm-k8s/git/files/master/qcbm-ddl.sql) 初始化。详情请参见 [创建 MySQL 实例](https://cloud.tencent.com/document/product/236/46433)。
- 在 [Redis 控制台](https://console.cloud.tencent.com/redis) 创建实例并初始化。详情请参见 [创建 Redis 实例](https://cloud.tencent.com/document/product/239/30871)。
- 在 [负载均衡控制台](https://console.cloud.tencent.com/clb) 为子网 Subnet-K8S 新建一个**内网型**的负载均衡（后续实践中会使用到该 CLB 实例 ID）。详情请参见 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)。
- 申请通过 [TSW 内测](https://cloud.tencent.com/apply/p/rvo6c9fnug)。TSW 目前处于内测阶段，支持 Java 和 Golang 两种语言接入。
- 部署 Nacos 集群：
  1. 在 [云服务器控制台](https://console.cloud.tencent.com/cvm) 购买3台 “标准型SA2” 1核2G的云服务器，详情请参见 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。
  2. 登录实例，执行以下命令安装 Java。
```plaintext
yum install java-1.8.0-openjdk.x86_64
```   执行以下命令，如有输出 java 版本信息，则说明 java 安装成功。
```plaintext
java - version
```  3. 部署 Nacos 集群，详情请参见 Nacos 官方文档 [集群部署说明](https://nacos.io/zh-cn/docs/cluster-mode-quick-start.html) 。

 




### 构建 Docker 镜像

#### 编写 Dockerfile

下文以 user-service 为例为您简单介绍如何编写 Dockerfile。示例展示的是 user-service 的工程目录结构，**Dockerfile** 位于工程的根目录下，**user-service-1.0.0.zip** 是打包后的文件，需要添加到镜像中。

```sh
➜  user-service tree
├── Dockerfile
├── assembly
│    ....
├── bin
│    ....
├── pom.xml
├── src
│    ....
├── target
│    .....
│   └── user-service-1.0.0.zip
└── user-service.iml
```

user-service 的 Dockerfile 如下所示：

```docker
FROM java:8-jre

ARG APP_NAME=user-service
ARG APP_VERSION=1.0.0
ARG FULL_APP_NAME=${APP_NAME}-${APP_VERSION}

# 容器中的工作目录为 /app
WORKDIR /app

# 将本地打包出来的应用添加到镜像中
COPY ./target/${FULL_APP_NAME}.zip .

# 创建日志目录 logs，解压并删除原始文件和解压后的目录
RUN mkdir logs \
      && unzip ${FULL_APP_NAME}.zip \
      && mv ${FULL_APP_NAME}/** . \
      && rm -rf ${FULL_APP_NAME}*

# user-service 的启动脚本和参数
ENTRYPOINT ["/app/bin/user-service.sh"] CMD ["start", "-t"]

# dubbo 端口号
EXPOSE 20880
```

>!
>- 生产中的 Java 应用有很多配置参数，导致启动脚本很复杂。将启动脚本里的内容全部写到 dockerfile 中工作量很大，其次 dockerfile 远没有 Shell 脚本灵活，若出现问题也无法快速定位，因此不建议弃用启动脚本。 
>- 通常在启动脚本最后使用 **nohup** 启动 Java 应用，但该方式启动的 deamon 进程会导致容器运行后直接退出。因此 `nohup java ${OPTIONS} -jar user-service.jar > ${LOG_PATH} 2>&1 &`  需改成 `java ${OPTIONS} -jar user-service.jar > ${LOG_PATH} 2>&1`。
>- Dockerfile 中每多一个 RUN 命令，生成的镜像就多一层，推荐将这些 RUN 命令合成一条。


#### 构建镜像

容器镜像服务 TCR 提供了自动和手工构建镜像方式，详情可参见 [镜像构建](https://cloud.tencent.com/document/product/1141/50337) 文档。为展示具体的构建过程，本文采用手工构建方式。

镜像名称需要符合规范 `ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]`：

- 其中命名 namespace 为方便镜像管理使用，可以按项目取名。本文采用 QCBM 表示 Q 云书城项目下的所有镜像。
- ImageName 可以包含 subpath，一般用于企业用户多项目场景。此外，如果本地已构建好镜像，可使用 `docker tag` 命令，按命名规范对镜像重命名。


1. 执行以下命令构建镜像。示例如下：
```sh
# 推荐的构建方式，可省去二次打 tag 操作
sudo docker build -t ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
# 本地构建 user-service 镜像，最后一个 . 表示 Dockerfile 存放在当前目录（user-service）下
➜  user-service docker build -t ccr.ccs.tencentyun.com/qcbm/user-service:1.0.0 .
# 将已存在镜像按命名规范对镜像重命名
sudo docker tag [ImageId] ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
```
2. 构建完成后，可执行以下命令查看本地仓库中的所有镜像。
```sh
docker images
```
 示例如下图所示：
![](https://main.qcloudimg.com/raw/3ef0c5d4ff3b33f8ddf8cabfda518665.png)


### 上传镜像到 TCR



#### 创建命名空间

QCBM 项目采用个人版镜像仓库（建议企业客户使用企业版镜像仓库）。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2) 。
2. 选择**镜像仓库** > **个人版** > **命名空间**进入“命名空间”页面。
3. 单击**新建**，在弹出的新建命名窗口中新建命名空间 qcbm。QCBM 项目所有的镜像都存放于该命名空间下。如下图所示：
   ![](https://main.qcloudimg.com/raw/d41dc91e084a7b21f44078445360895d.png)


#### 上传镜像


上传镜像需要完成以下步骤：登录腾讯云 registry 和上传镜像。


1. 执行以下命令登录腾讯云 registry。
```sh
 docker login --username=[腾讯云账号 ID] ccr.ccs.tencentyun.com
```
 <dx-alert infotype="explain" title="">
- 腾讯云账号 ID 可在 [账号信息](https://console.cloud.tencent.com/developer) 页面获取。
- 若忘记**镜像仓库登录密码**，可前往容器服务镜像仓库个人版 [我的镜像](https://console.cloud.tencent.com/tke2/registry/user) 中进行重置。
  ![](https://main.qcloudimg.com/raw/4a5f86637fbef74e7ebb48431e743658.png)
- 若执行命令提示无权限，请在上述命令前加上 sudo 再执行，如下所示。此时需要输入两个密码，第一个为 sudo 所需的主机管理员密码，第二个为**镜像仓库登录密码**。
```sh
 sudo docker login --username=[腾讯云账号 ID] ccr.ccs.tencentyun.com
```如下图所示：
![](https://main.qcloudimg.com/raw/d34997020efabeb1f52f3eb9327f20cb.png)
</dx-alert>
2. 执行以下命令将本地生成的镜像推送至 TKE 的镜像仓库中。
```sh
docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
```如下图所示：
![](https://main.qcloudimg.com/raw/466adcd0ebf9adf2c16421885a0c6567.png)
3. 在 [我的镜像](https://console.cloud.tencent.com/tke2/registry/user/self?rid=1) 中可以查看上传的所有镜像，下图展示的是上传到腾讯云镜像仓库中 QCBM 的5个镜像。
   ![](https://main.qcloudimg.com/raw/05c412370fb69e675bfb9149b33063a6.png)
<dx-alert infotype="explain" title="">
默认镜像类型为“私有”，如需提供镜像给他人使用，可在**镜像信息**中将镜像类型设置为公有。如下图所示：
![](https://main.qcloudimg.com/raw/88b73306c07a4ea281cef52a77d3246c.png)
</dx-alert>
<br>








### 在 TKE 上部署服务


#### 创建 k8s 集群 QCBM


1. 实际部署前，需要新建一个 k8s 集群。有关集群的创建，请参见 [创建集群](https://cloud.tencent.com/document/product/457/54231) 文档。
>! 创建集群时，在“选择机型”页面建议开启“置放群组功能”，该功能可将 CVM 打散到不同母机上，增加系统可靠性。如下图所示：
>![](https://main.qcloudimg.com/raw/e02eb656cd91db18eb58eabf34b0da69.png)
2. 集群创建完成后，在容器服务控制台的 [集群管理](https://console.cloud.tencent.com/tke2/cluster) 页面可以查看新建的集群信息。本文新建的集群名称为 qcbm-k8s-demo。如下图所示：
   ![](https://main.qcloudimg.com/raw/37105f08a2ccf070621f0a621e972b0a.png)
3. 单击集群名称进入“基本信息”页面，查看集群的配置信息。如下图所示：
   ![](https://main.qcloudimg.com/raw/8de9b997674164f32a05104d613a24b9.png)
4. （可选）如需使用 Kubectl 和 lens 等 k8s 管理工具，还需进行以下两步操作：
   1. 开启外网访问。
   2. 将 API 认证 Token 保存在本地 `用户 home/.kube` 下的 config 文件中（若 config 文件已有内容，则需要替换），以确保每次访问都能进入默认集群中。如果选择不将 API 认证 Token 保存在 `.kube` 下的 config 文件中，则可参考控制台**集群APIServer信息**下的 **通过Kubectl连接Kubernetes集群操作说明**。如下图所示：
      ![](https://main.qcloudimg.com/raw/fc1ce98044d792325b75c3eb4c34feae.jpeg)


#### 创建 Namespace

Namespaces 是 Kubernetes 在同一个集群中进行逻辑环境划分的对象，通过 Namespaces 可以进行多个团队多个项目的划分。您可以通过以下三种方式创建 Namespace，推荐使用方式1命令行方式创建。


<dx-tabs>
::: 方式1：使用命令行
执行以下命令即可创建 Namespace：
```sh
 kubectl create namespace qcbm
```
:::
::: 方式2：使用控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID/名称进入集群详情页面。  
2. 单击**命名空间** > **新建**，创建名称为 qcbm 的 Namespace。
:::
::: 方式3：使用\sYAML\s部署
执行以下命令使用 YAML 创建 Namespace：
```
shkubctl create –f namespace.yaml
```其中 namespace.yaml 如下： 
```yaml
  # 创建命名空间 qcbm
  apiVersion: v1
  kind: Namespace
  metadata:
    name: qcbm
  spec:
    finalizers:
    - kubernetes
```
:::
</dx-tabs>




#### ConfigMap 存放配置信息

通过 ConfigMap 可以将配置和运行的镜像进行解耦，使应用程序有更强的移植性。QCBM 后端服务需要从环境变量中获取 Nacos、MySQL、Redis 主机和端口信息，并将其使用 ConfigMap 进行保存。
您可通过以下两种方式使用 ConfigMap 存放配置信息：


<dx-tabs>
::: 方式1：使用\sYAML
下文为 QCBM 的 ConfigMap YAML，其中**纯数字类型的 value 需要使用双引号**。例如，下文示例 YAML 中的 MYSQL_PORT：
<dx-codeblock>
:::  yaml

# 创建 ConfigMap

apiVersion: v1
kind: ConfigMap
metadata: 
  name: qcbm-env
  namespace: qcbm
data: 
  NACOS_HOST: 10.0.1.9 
  MYSQL_HOST: 10.0.1.13 
  REDIS_HOST: 10.0.1.16 
  NACOS_PORT: "8848"
  MYSQL_PORT: "3306"
  REDIS_PORT: "6379"
  SW_AGENT_COLLECTOR_BACKEND_SERVICES: xxx   # TSW 接入地址，后文介绍
:::
</dx-codeblock>
:::
::: 方式2：使用控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID/名称进入集群详情页面。 
2. 单击**配置管理** > **ConfigMap** > **新建**，创建名称为 qcbm-env 的 ConfigMap 用于存放相关配置。其中命名空间 qcbm，如下图所示:
   ![](https://main.qcloudimg.com/raw/48845cae9238f2bc45ef1b197c343618.png)
   :::
   </dx-tabs>






#### 使用 Secret 存放敏感信息

Secret 可用于存储密码、令牌、密钥等敏感信息，降低直接对外暴露的风险。QCBM 使用 Secret 来保存相关的账号和密码信息。
您可通过以下两种方式使用 Secret 存放敏感信息：

<dx-tabs>
::: 方式1：使用\sYAML
下文为 QCBM 创建 Secret 的 YAML。其中 Secret 的 value 需要是 base64 编码后的字符串。
<dx-codeblock>
:::  yaml
# 创建 Secret
apiVersion: v1
kind: Secret
metadata: 
  name: qcbm-keys
  namespace: qcbm
  labels: 
    qcloud-app: qcbm-keys
data: 
  # xxx 为base64 编码后的字符串，可使用 shell 命令 “echo -n 原始字符串 | base64” 生成
  MYSQL_ACCOUNT:  xxx
  MYSQL_PASSWORD: xxx
  REDIS_PASSWORD: xxx
  SW_AGENT_AUTHENTICATION: xxx  # TSW 接入 token，后文介绍
type: Opaque
:::
</dx-codeblock>
:::
::: 方式2：使用控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID/名称进入集群详情页面。 
2. 单击**配置管理** > **Secret** > **新建**，创建名称为 qcbm-keys  的 Secret，如下图所示：
   ![](https://main.qcloudimg.com/raw/8f97446c6d7ab3e75415a19a636c1081.png)
   :::
   </dx-tabs>





#### 部署工作负载 Deployment

Deployment 声明了 Pod 的模板和控制 Pod 的运行策略，适用于部署无状态的应用程序。QCBM 的 front 和 Dubbo 服务都属于无状态应用，适合使用 Deployment。

以下是 user-service Deployment 的 YAML 参数说明：

| 参数             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| replicas         | 表示需要创建的 pod 数量                                      |
| image            | 镜像的地址                                                   |
| imagePullSecrets | 拉取镜像时需要使用的 key，可在 **[集群](https://console.cloud.tencent.com/tke2/)**>**配置管理** > **Secret**中获取。使用公共镜像时可省略 |
| env              | <li>定义了 pod 的环境变量和取值<br><li>ConfigMap 中定义的 key-value 可使用 configMapKeyRef 引用<br><li>Secret 中定义的 key-value 可使用 secretKeyRef 引用 |
| ports            | 指定容器的端口号，由于是 Dubbo 应用，所以端口号为20880       |

user-service Deployment 的 完整 YAML 文件示例如下：

<dx-codeblock>
:::  yaml

# user-service Deployment

apiVersion: apps/v1
kind: Deployment
metadata: 
  name: user-service
  namespace: qcbm
  labels: 
    app: user-service
    version: v1
spec: 
  replicas: 1
  selector: 
    matchLabels: 
      app: user-service
      version: v1
  template: 
    metadata: 
      labels: 
        app: user-service
        version: v1
    spec: 
      containers: 
        - name: user-service
          image: ccr.ccs.tencentyun.com/qcbm/user-service:1.1.4
          env: 
            - name: NACOS_HOST  # dubbo服务注册中心nacos的IP地址
              valueFrom: 
                configMapKeyRef: 
                  key: NACOS_HOST
                  name: qcbm-env
                  optional: false
            - name: MYSQL_HOST  # Mysql 地址
              valueFrom: 
                configMapKeyRef: 
                  key: MYSQL_HOST
                  name: qcbm-env
                  optional: false
            - name: REDIS_HOST  # Redis的IP地址
              valueFrom: 
                configMapKeyRef: 
                  key: REDIS_HOST
                  name: qcbm-env
                  optional: false
            - name: MYSQL_ACCOUNT  # Mysql 账号
              valueFrom: 
                secretKeyRef: 
                  key: MYSQL_ACCOUNT
                  name: qcbm-keys
                  optional: false
            - name: MYSQL_PASSWORD  # Mysql 密码
              valueFrom: 
                secretKeyRef: 
                  key: MYSQL_PASSWORD
                  name: qcbm-keys
                  optional: false
            - name: REDIS_PASSWORD  # Redis 密码
              valueFrom: 
                secretKeyRef: 
                  key: REDIS_PASSWORD
                  name: qcbm-keys
                  optional: false
            - name: SW_AGENT_COLLECTOR_BACKEND_SERVICES  # Skywalking 后端服务地址
              valueFrom: 
                configMapKeyRef: 
                  key: SW_AGENT_COLLECTOR_BACKEND_SERVICES
                  name: qcbm-env
                  optional: false
            - name: SW_AGENT_AUTHENTICATION    # Skywalking agent 连接后端服务的认证 token
              valueFrom: 
                secretKeyRef: 
                  key: SW_AGENT_AUTHENTICATION
                  name: qcbm-keys
                  optional: false
          ports: 
            - containerPort: 20880 # dubbo 端口号
              protocol: TCP
      imagePullSecrets:   # 拉取镜像时需要使用的 key，QCBM 所有服务的镜像已开放为公共镜像，故此处可省略
        - name: qcloudregistrykey
:::
</dx-codeblock>



#### 部署服务 Service

Kubernetes 的 ServiceTypes 允许指定 Service 类型，默认为 ClusterIP 类型。ServiceTypes 可取如下值：

- LoadBalancer：提供公网、VPC、内网访问。
- NodePort：可通过“云服务器 IP + 主机端口”访问服务。
- ClusterIP：可通过“服务名 + 服务端口”访问服务。

对于实际生产系统来说，gateway 需要能在 VPC 或内网范围内进行访问， front 前端需要能对内/外网提供访问。因此，QCBM 的 gateway 和 front 需要制定 LoadBalancer 类型的 ServiceType。
TKE 对 LoadBalancer 模式进行了扩展，通过 Annotation 注解配置 Service，可实现更丰富的负载均衡能力。

若使用 `service.kubernetes.io/qcloud-loadbalancer-internal-subnetid` 注解，在 service 部署时，会创建内网类型 CLB。一般建议事先创建好 CLB，service 的部署 YAML 中使用注解 `service.kubernetes.io/loadbalance-id` 直接指定，可提升部署效率。

以下为 qcbm-front service 部署 YAML：


<dx-codeblock>
:::  yaml
# 部署 qcbm-front service
apiVersion: v1
kind: Service
metadata: 
  name: qcbm-front
  namespace: qcbm
  annotations: 
    # Subnet-K8S 子网的 CLB 实例 ID
    service.kubernetes.io/loadbalance-id: lb-66pq34pk
spec: 
  externalTrafficPolicy: Cluster
  ports: 
    - name: http
      port: 80
      targetPort: 80
      protocol: TCP
  selector: # 将后端服务 qcbm-gateway 和该 Service 进行映射
    app: qcbm-front
    version: v1
  type: LoadBalancer
:::
</dx-codeblock>


#### 部署 Ingress

Ingress 是允许访问到集群内 Service 规则的集合。一般使用 Ingress 提供对外访问，而不直接暴露 Service 。QCBM 项目需要为 qcbm-front 创建 Ingress，对应的 YAML 如下：


<dx-codeblock>
:::  yaml

# 部署 qcbm-front ingress

apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata: 
  name: front
  namespace: qcbm
  annotations: 
    ingress.cloud.tencent.com/direct-access: "false"
    kubernetes.io/ingress.class: qcloud
    kubernetes.io/ingress.extensiveParameters: '{"AddressIPVersion":"IPV4"}'
    kubernetes.io/ingress.http-rules: '[{"host":"qcbm.com","path":"/","backend":{"serviceName":"qcbm-front","servicePort":"80"}}]'
spec: 
  rules: 
    - host: qcbm.com
      http: 
        paths: 
          - path: /
            backend:  # 关联到后端服务
              serviceName: qcbm-front
              servicePort: 80
:::
</dx-codeblock>


#### 查看部署结果

至此，您已完成 QCBM 在容器服务 TKE 上的部署，可通过以下步骤查看部署结果：

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/)，单击集群 ID/名称进入集群详情页面。
2. 单击**服务与路由** > **Ingress**进入 Ingress 页面，可查看到创建的 Ingress。通过 Ingress 的 VIP 即可访问 Q 云书城页面。
   ![](https://main.qcloudimg.com/raw/bbdd5e7a884adc639f12a4c5b21815e8.png)



### 集成 CLS 日志服务

#### 开启容器日志采集功能

容器日志采集功能默认关闭，使用前需要开启，步骤如下：

1. 登录容器服务控制台，选择左侧导航栏中的**集群运维** > **[功能管理](https://console.cloud.tencent.com/tke2/ops/list?rid=1)**。
2. 在“功能管理”页面上方选择地域，单击需要开启日志采集的集群右侧的**设置**。
   ![](https://main.qcloudimg.com/raw/2402b7869f3687bf6237bfb5d3940817.png)
3. 在“设置功能”页面，单击日志采集**编辑**并勾选**开启日志采集**。如下图所示：
   ![](https://main.qcloudimg.com/raw/3720d6096ce9486419475ebb5efbaf99.png)
4. 单击**确定**即可开启容器日志采集功能。



#### 创建日志主题和日志集

QCBM 部署在南京地域，因此在创建日志集时应当选择南京地域：

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/topic)，在“日志主题”页面选择南京地域。
2. 单击**创建日志主题**，在弹出的窗口中根据页面提示填写相关信息，如下图所示：
   <img src="https://main.qcloudimg.com/raw/402a29ab53c4a048b350ced921009a52.jpg" width="70%"><br>
 - **日志主题名称**：输入 qcbm。
 - **日志集操作**：选择**创建日志集**。
 - **日志集名称**：输入 qcbm-logs。
3. 单击**确定**即可创建日志主题和日志集。
>?QCBM 有多个后端微服务，为每个微服务建个日志主题便于日志归类。
>- QCBM 每个服务都建立了一个日志主题。
>- 日志主题 ID，为容器创建日志规则时需要用到。




#### 配置日志采集规则

您可通过控制台或 CRD 两种方式配置容器日志采集规则。


<dx-tabs>
::: 方式1：使用控制台
日志规则指定了日志在容器内的位置：

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/)，选择左侧导航栏中的**集群运维** > **日志规则**。
2. 在“日志规则”页面，单击**新建**新建日志规则：
   - **日志源**：指定容器日志位置，QCBM 的日志都统一输出到 /app/logs 目录下，因而使用容器文件路径并指定具体的工作负载和日志位置。
   - **消费端**：选择之前创建的日志集和主题。
     ![](https://main.qcloudimg.com/raw/84a02a836cb2fa7e40bb55880153767c.png)
3. 单击**下一步**进入 “日志解析方式”， 其中本文示例 QCBM 使用单行文本方式。 了解更多 CLS 支持的日志格式，请参见 [采集文本日志](https://cloud.tencent.com/document/product/614/17418) 文档。
   :::
   ::: 方式2：使用\sCRD
   您还可通过自定义资源定义（CustomResourceDefinitions，CRD）的方式配置日志采集。QCBM 使用了容器文件路径的采集方式，日志格式为单行文本。下文是 user-service 日志采集具体的配置 YAML。了解更多 CRD 采集配置请参见 [使用 CRD 配置日志采集](https://cloud.tencent.com/document/product/457/48425) 文档。
   <dx-codeblock>
   :::  yaml
   apiVersion: cls.cloud.tencent.com/v1
   kind: LogConfig
   metadata: 
     name: user-log-rule
   spec: 
     clsDetail: 
    extractRule: {}
    # 单行文本
    logType: minimalist_log
    # 日志主题 user-log 的 ID
    topicId: 0c544491-03c9-4ed0-90c5-9bedc0973478
     inputDetail: 
    # 日志所在的容器、工作负载以及日志输出目录
    containerFile: 
      container: user-service
      filePattern: '*.log'
      logPath: /app/logs
      namespace: qcbm
      workload: 
        kind: deployment
        name: user-service
    # 日志采集类型为容器文件路径
    type: container_file
   :::
   </dx-codeblock>
   :::
   </dx-tabs>



#### 查看日志

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/search)，进入“检索分析”页面。
2. 检索分析中可先为日志**新建索引**，索引完毕之后再单击**检索分析**即可查看日志。
   ![](https://main.qcloudimg.com/raw/e42971d17c20115d12ace2adb861e6a6.png)

>!若未新建索引，则检索不到日志。


### 集成 TSW 观测服务



TSW 目前处于内测阶段，可在广州和上海进行部署，本文选择上海接入（QCBM 部署在南京）。



#### 接入 TSW — 获取接入点信息

1. 登录 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm)，选择左侧导航栏种的**服务观测** > **服务列表**。
2. 单击**接入服务**，选择 Java 语言与 SkyWalking 的数据采集方式。接入方式下提供了如下接入信息：**接入点**和 **Token**。
   ![](https://main.qcloudimg.com/raw/b6333d66cf38310a9fe2403bee7bbb4a.png)



#### 接入 TSW — 应用和容器配置

将上一步骤中获取的 TSW 的**接入点**和 **Token** 分别填写到 skywalking 的 agent.config 配置项中的 collector.backend_service 和 agent.authentication。“agent.service_name” 配置对应的服务名称，可使用 “agent.namespace” 对同一领域下的微服务归类。如下图为 user-service 配置：
![](https://main.qcloudimg.com/raw/a6a1818458fd003f8fd826d3b05e2087.png)

Skywalking agent 也支持使用环境变量方式进行配置，QCBM 使用 ConfigMap 和 Secret 配置对应的环境变量：

- 使用 ConfigMap 配置 SW_AGENT_COLLECTOR_BACKEND_SERVICES
- 使用 Secret 配置 SW_AGENT_AUTHENTICATION

如下图所示：
![](https://main.qcloudimg.com/raw/5f3a034b41fd6e4df08b9fa2c23ce7c0.png)

至此 TSW 接入工作已完成，启动容器服务后，在 TSW 控制台即可查看调用链、服务拓扑、SQL 分析等功能。



### 使用 TSW 观测服务

#### 通过服务接口和调用链查看调用异常

1. 登录 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm)，选择左侧导航栏中的**服务观测** > **接口观测**。
2. 在接口观测页面可查看一个服务下所有接口的调用情况，包括请求量、成功率、错误率、响应时间等指标。如下图所示：
   ![](https://main.qcloudimg.com/raw/d35983cddeb99eb027cd4f76fa927cab.png)
3. 上图中 qcbm-gateway 的两个接口：查询用户收藏夹 `/api/favorites/query/{userId}` 和查询用户订单 `/api/order/{userId}` 出现调用异常。单击查询用户收藏夹接口，可以查看到该接口的所有调用记录，找到异常的调用链，单击进入可以查看具体异常原因。如下图所示：
   ![](https://main.qcloudimg.com/raw/094f5b7c95526aed7626187ec4b21e03.png)
   通过分析可以发现 favorites-service 因 time-out 导致调用异常。如下图所示：
   ![](https://main.qcloudimg.com/raw/094b6ef0fae35dad87f23123bf6bb187.png)


#### 使用 TSW 分析 SQL 和缓存等组件调用情况

1. 登录 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm)，选择左侧导航栏中的**组件调用观测** > **SQL 调用**。
2. 在“SQL 调用”页面可查看 SQL、NOSQL、MQ 及其它组件的调用情况。例如，通过 SQL 的请求量及耗时，可以快速定位应用中的高频 SQL 和慢查询。如下图所示：
   ![](https://main.qcloudimg.com/raw/43376cf371bc037bd7a07b3a1782a5e6.png)



#### 查看服务拓扑

1.  登录 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm)，选择左侧导航栏中的**链路追踪** > **分布式依赖拓扑**。
2.  在“分布式依赖拓扑”页面可查看完成的服务依赖情况，以及调用次数和平均延迟等信息。如下图所示：
    ![](https://main.qcloudimg.com/raw/f17189bbf5e40ce6a4132caa2b00e0ee.png)
