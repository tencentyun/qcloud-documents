## 操作场景

本文章介绍了 SpringCloud 应用托管到腾讯云容器服务 TKE 的最佳实践。

**SpringCloud 应用托管到 TKE 具有以下优势：**

- 提升资源利用率。
- Kubernetes 天然适合微服务架构。
- 提升运维效率，便于 Devops 落地实施。
- Kubernetes 的高弹性，可轻松实现应用的动态扩缩容。
- 容器服务 TKE 提供 Kubernetes Master 托管功能，可减少 Kubernetes 集群运维和管理的负担。
- 容器服务 TKE 和腾讯云的其他云原生产品进行了整合和优化，帮助用户更好的使用腾讯云上产品。

## 最佳实践实例介绍

### PiggyMetrics 概述

本文最佳实践通过 fork  GitHub 上的开源项目 [PiggyMetrics](https://github.com/sqshq/piggymetrics) ，对其进行修改以适应腾讯云产品，并以最终修改后的版本为例，详细介绍 SpringCloud 应用托管到 TKE 的整个过程。

>?修改后的 PiggyMetrics 部署项目托管在 [GitHub](https://github.com/TencentCloud/container-demo/tree/main/springcloud-on-tke) 上。在 [搭建基础服务集群](#create) 后，可直接下载部署工程并在 TKE 上进行部署。



PiggyMetrics 首页如下图所示：
![](https://main.qcloudimg.com/raw/40a504b665b76ab16e32394f2594350f.jpg)

PiggyMetrics 是一个采用微服务架构，并使用 SpringCloud 框架开发的个人记账理财应用。

PiggyMetrics 微服务组成如下：


| 微服务              | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| API 网关            | 基于 Spring Cloud Zuul 的网关，是调用后台 API 的聚合入口，提供反向路由和负载均衡（Eureka+Ribbon）、限流熔断（Hystrix）等功能。CLIENT 单页应用和 ZUUL 网关暂住在一起，简化部署。 |
| 服务注册和发现      | 基于 Spring Cloud Eureka 的服务注册中心。业务服务启动时通过 Eureka 注册，服务之间调用也通过 Eureka 进行服务发现。 |
| 授权认证服务        | 基于 Spring Security OAuth2 的授权认证中心。客户端登录时通过 AUTHSERVICE 获取访问令牌。服务之间调用也通过 AUTHSERVICE 获取访问令牌（走客户端模式）。令牌校验方式，各资源服务器通过 AUTHSERVICE 集中校验令牌。 |
| 配置服务            | 基于 Spring Cloud Config 的配置中心，集中管理所有 Spring 服务的配置文件。 |
| 软负载和限流熔断    | 基于 Spring Cloud Ribbon&Hystrix，Zuul 调用后台服务，服务之间相互调用都通过 Ribbon 实现软负载，也通过 Hystrix 实现熔断限流保护。 |
| METRICS & DASHBOARD | 基于 Spring Cloud Turbine + Hystrix Dashboard，对所有 Hystrix 产生的 Metrics 流进行聚合，并展示在 Hystrix Dashboard 上。 |






### PiggyMetrics 部署架构和组件[](id:deploy)


本文最佳实践实例模拟将原先部署在云服务器 CVM 的应用进行容器化，并托管到容器服务 TKE 的场景。在该场景中需要采用一个 VPC，并划分为以下两个子网：

- **Subnet-Basic** 中部署有状态的基础服务，包括 Dubbo 的服务注册中心 Nacos，MySQL 和 Redis 等。
- **Subnet-K8S** 中部署 PiggyMetrics 的应用服务，所有服务都进行了容器化，运行在容器服务 TKE 上。

子网划分如下图所示：
![](https://main.qcloudimg.com/raw/5fae267e9b523840cdae3356bb06b9ee.jpeg)

PiggyMetrics 实例的网络规划如下表所示：

| 网络规划          | 说明                                                         |
| :---------------- | :----------------------------------------------------------- |
| Region / AZ       | 南京 / 南京一区                                              |
| VPC               | CIDR：10.0.0.0/16                                            |
| 子网 Subnet-Basic | 南京一区，CIDR：10.0.1.0/24                                  |
| 子网 Subnet-K8S   | 南京一区，CIDR：10.0.2.0/24                                  |
| Nacos 集群        | 采用 3 台 “标准型SA2” 1C2G 机型的 CVM 构建 Nacos 集群，对应的 IP 为：10.0.1.9，10.0.1.14，10.0.1.15 |

PiggyMetrics 实例中用到的组件如下表所示：

| 组件        |       版本       |   来源   | 备注                                                         |
| :---------- | :--------------: | :------: | :----------------------------------------------------------- |
| K8S         |      1.8.4       |  腾讯云  | TKE 托管模式                                                 |
| MongoDB     |       4.0        |  腾讯云  | TencentDB for MongoDB WiredTiger 引擎版                      |
| CLS         |       N/A        |  腾讯云  | 日志服务                                                     |
| TSW         |       N/A        |  腾讯云  | 采用 Skywalking 8.4.0 版的 agent 接入，点此 [下载](https://archive.apache.org/dist/skywalking/8.4.0/apache-skywalking-apm-8.4.0.tar.gz) |
| Java        |       1.8        | 开源社区 | Docker 镜像：java:8-jre                                      |
| SrpingCloud | Finchley.RELEASE | 开源社区 | [Spring Cloud 官网](https://spring.io/projects/spring-cloud) |


## 服务介绍


### TCR 介绍

腾讯云 [容器镜像服务 TCR](https://cloud.tencent.com/product/tcr)（Tencent Container Registry，TCR），提供了个人版和企业版两种镜像仓库。两者区别如下：

- 个人版镜像仓库仅部署在腾讯云广州，企业版在每个地域都有部署。
- 个人版未提供服务 SLA 保证。

![](https://main.qcloudimg.com/raw/169e2d9b46f59b2eeb58a935dc5e0c30.jpeg)


PiggyMetrics 是一个 Dubbo 容器化的 Demo 项目，因此容器镜像服务个人版完全满足需求。但对于企业用户，推荐使用 [企业版 TCR](https://console.cloud.tencent.com/tcr)。如需使用镜像仓库，请见 [镜像仓库基本操作](https://cloud.tencent.com/document/product/1141/41811)。



### TSW 介绍

腾讯云 [微服务观测平台 TSW](https://cloud.tencent.com/product/tsw)（Tencent Service Watcher，TSW）提供云原生服务可观察性解决方案，能够追踪到分布式架构中的上下游依赖关系，绘制拓扑图，提供服务、接口、实例、中间件等多维度调用观测。
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
![](https://main.qcloudimg.com/raw/314b04572a404ffa944e2ae3a599257c.png)



## 操作步骤

### 基础服务集群搭建[](id:create)

- 在 [Mongodb 控制台](https://console.cloud.tencent.com/mongodb) 创建实例，并执行以下命令进行初始化：
  <dx-codeblock>
  :::  sh

# 下载 mongo client, 解压，进入 bin 目录

wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.6.18.tgz
tar -zxvf mongodb-linux-x86_64-3.6.18.tgz
cd mongodb-linux-x86_64-3.6.18/bin

# 使用下面命令初始化 mongodb，其中 mongouser 为创建 mongodb 实例时创建的管理员账号

./mongo -u mongouser -p --authenticationDatabase "admin" [mongodb的IP]/piggymetrics mongo-init.js
:::
</dx-codeblock>
 <dx-alert infotype="explain" title="">
  mongodb 初始化脚本 **mongo-init.js** 中默认创建了一个 piggymetrics 库的用户 **guest**，可按您的需求进行修改。
</dx-alert>

- 在 [CLB 控制台](https://console.cloud.tencent.com/clb) 为子网 Subnet-K8S 新建一个内网型的 CLB（后续实践中会使用到该 CLB 实例 ID）。
- 申请通过 [TSW 内测](https://cloud.tencent.com/apply/p/rvo6c9fnug)。TSW 目前处于内测阶段，支持 Java 和 Golang 两种语言接入。







### 构建 Docker 镜像

#### 编写 Dockerfile

下文以 account-service 为例为您简单介绍如何编写 Dockerfile。示例展示的是 account-service 的工程目录结构，**Dockerfile** 位于工程的根目录下，**account-service.jar** 是打包后的文件，需要添加到镜像中。

```sh
➜  account-service tree
├── Dockerfile
├── skywalking
│   ├── account.config
│   └── skywalking-agent.zip
├── pom.xml
├── src
│    ....
├── target
│    .....
│   └── account-service.jar
└── account-service.iml
```


>? 此处使用 skywalking-agent 作为 TSW 接入客户端，向 TSW 后台上报调用链信息。下载 Skywalking-agent 详情可参见 [PiggyMetrics 部署架构和组件](#deploy)。

account-service 的 Dockerfile 如下所示：

<dx-codeblock>
:::  docker
FROM java:8-jre

# 容器中的工作目录为 

/appWORKDIR /app

# 将本地打包出来的应用添加到镜像中

ADD ./target/account-service.jar

# 将 skywalking agent 拷贝到镜像中

COPY ./skywalking/skywalking-agent.zip 

# 解压 skywalking agent  并删除原始压缩文件

RUN unzip skywalking-agent.zip && rm -f skywalking-agent.zip

# 添加 skywalking 的配置文件

COPY ./skywalking/account.config ./skywalking-agent/config/agent.config

# 启动应用

CMD ["java", "-Xmx256m", "-javaagent:/app/skywalking-agent/skywalking-agent.jar", "-jar", "/app/account-service.jar"]

# 应用的端口说明

EXPOSE 6000
:::
</dx-codeblock>


>! Dockerfile 中每多一个 RUN 命令，生成的镜像就多一层，推荐将这些 RUN 命令合成一条。







#### 镜像构建


容器镜像服务 TCR 提供自动和手工两种构建镜像方式，详情可参见 [镜像构建](https://cloud.tencent.com/document/product/1141/50337) 文档。为展示具体的构建过程，本文采用手工构建方式。

镜像名称需要符合规范 `ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]`：

- 其中命名 namespace 为方便镜像管理使用，可以按项目取名。本文采用 piggymetrics 表示 PiggyMetrics 项目下的所有镜像。
- ImageName 可以包含 subpath，一般用于企业用户多项目场景。此外，如果本地已构建好镜像，可使用 `docker tag` 命令，按命名规范对镜像重命名。



1. 执行以下命令构建镜像。示例如下：
   <dx-codeblock>
   :::  sh

# 推荐的构建方式，可省去二次打 tag 操作

sudo docker build -t ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]

# 本地构建 account-service 镜像，最后一个 . 表示 Dockerfile 存放在当前目录（user-service）下

➜  account-service docker build -t ccr.ccs.tencentyun.com/piggymetrics/account-service:1.0.0 .

# 将已存在镜像按命名规范对镜像重命名

sudo docker tag [ImageId] ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
:::
</dx-codeblock>

2. 构建完成后，可执行以下命令查看本地仓库中的所有镜像。
```sh
docker images | grep piggymetrics
```
 示例如下图所示：
 ![](https://main.qcloudimg.com/raw/64ebfe03265b1d95ebe6bb5a3cf02bf1.png)





### 上传镜像到 TCR


#### 创建命名空间

PiggyMetrics 项目采用个人版镜像仓库（建议企业客户使用企业版镜像仓库）。


1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2) 。
2. 选择**镜像仓库** > **个人版** > **命名空间**进入“命名空间”页面。
3. 单击**新建**，在弹出的新建命名窗口中新建命名空间 piggymetrics。PiggyMetrics 项目所有的镜像都存放于该命名空间下。如下图所示：
   ![](https://main.qcloudimg.com/raw/5162654ffab4033164b41e889b50d408.jpg)



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
```
 如下图所示：
![](https://main.qcloudimg.com/raw/466adcd0ebf9adf2c16421885a0c6567.png)
3. 在 [我的镜像](https://console.cloud.tencent.com/tke2/registry/user/self?rid=1) 中可以查看上传的所有镜像，下图展示的是上传到腾讯云镜像仓库中 PiggyMetrics 的 9 个镜像。
![](https://main.qcloudimg.com/raw/bbe50d859ab272ddeffdcd339d43213b.png)
<dx-alert infotype="explain" title="">
默认镜像类型为“私有”，如需提供镜像给他人使用，可在**镜像信息**中将镜像类型设置为公有。如下图所示：
![](https://main.qcloudimg.com/raw/88b73306c07a4ea281cef52a77d3246c.png)
</dx-alert>




### 在 TKE 上部署服务

#### 创建 K8S 集群 PiggyMetrics

1. 实际部署前，需要新建一个 K8S 集群。有关集群的创建，请参见 [创建集群](https://cloud.tencent.com/document/product/457/54231) 文档。
>!在创建集群时，在“选择机型” 页面建议开启“置放群组功能”，该功能可将 CVM 打散到不同母机上，增加系统可靠性。如下图所示：
![](https://main.qcloudimg.com/raw/6aba7922f3b7247cda8cb8e5b8959578.jpg)
2. 创建完成后，在容器服务控制台的 [集群管理](https://console.cloud.tencent.com/tke2/cluster) 页面可以看到新建的集群信息。本文新建的集群名称为 piggyMetrics。如下图所示：
![](https://main.qcloudimg.com/raw/1157a6c99171ef8080c860eae636881a.png)
3. 单击集群 PiggyMetrics-k8s-demo 进入“基本信息”页面，可以查看整个集群的配置信息。
4. （可选）如需使用 kubectl 和 lens 等 K8S 管理工具，还需进行以下两步操作：
	1. 开启外网访问。
	2. 将 API 认证 Token 保存为本地 `用户 home/.kube` 下的 config 文件中（若 config 文件已有内容，需要替换），以确保每次访问都能进入默认集群中。如果选择不保存为 `.kube` 下的 config 文件中，则可参考控制台**集群APIServer信息**下的 **通过Kubectl连接Kubernetes集群操作说明**。如下图所示：
![](https://main.qcloudimg.com/raw/fc1ce98044d792325b75c3eb4c34feae.jpeg)



#### 创建 Namespace

Namespaces 是 Kubernetes 在同一个集群中进行逻辑环境划分的对象， 通过 Namespaces 可以进行多个团队多个项目的划分。您可以通过以下三种方式创建 Namespace，推荐使用方式1命令行方式创建。


<dx-tabs>
::: 方式1：使用命令行
执行以下命令即可创建 Namespace：
<dx-codeblock>
:::  sh
kubectl create namespace piggymetrics
:::
</dx-codeblock>
:::
::: 方式2：使用控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID/名称进入集群详情页面。
2. 单击**命名空间** > **新建**，创建名称为 PiggyMetrics 的 Namespace。
:::
::: 方式3：使用\sYAML\s部署
执行以下命令使用 YAML 创建 Namespace：
<dx-codeblock>
:::  sh
kubctl create –f namespace.yaml
:::
</dx-codeblock>其中 namespace.yaml 如下： 
<dx-codeblock>
:::  yaml
  # 创建命名空间 piggymetrics
  apiVersion: v1
  kind: Namespace
  metadata: 
    name: piggymetrics
  spec: 
    finalizers:
    - kubernetes
:::
</dx-codeblock>
:::
</dx-tabs>




#### 使用 ConfigMap 存放配置信息

通过 ConfigMap 可以将配置和运行的镜像进行解耦，使应用程序有更强的移植性。PiggyMetrics 后端服务需要从环境变量中获取 MongoDB 的主机和端口信息，并使用 ConfigMap 来保存。
您可通过以下两种方式使用 ConfigMap 存放配置信息：

<dx-tabs>
::: 方式1：使用\sYAML
下文为 PiggyMetrics 的 ConfigMap YAML，其中**纯数字类型的 value 需要使用双引号**。
<dx-codeblock>
:::  yaml
# 创建 ConfigMap
apiVersion: v1
kind: ConfigMap
metadata: 
  name: piggymetrics-env
  namespace: piggymetrics
data: 
  # MongDB 的 IP 地址
  MONGODB_HOST: 10.0.1.13 
  # TSW 接入地址，后文介绍
  SW_AGENT_COLLECTOR_BACKEND_SERVICES: ap-shanghai.tencentservicewatcher.com:11800
:::
</dx-codeblock>
:::
::: 方式2：使用控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID/名称进入集群详情页面。
2. 单击**配置管理** > **ConfigMap** > **新建**，创建名称为 piggymetrics-env 的 ConfigMap 用于存放相关配置。其中命名空间 piggymetrics，如下图所示：
![](https://main.qcloudimg.com/raw/e2d17c01ca797b0b5f88c41634371917.jpg)
:::
</dx-tabs>



#### 使用 Secret 存放敏感信息

Secret 可用于存储密码、令牌、密钥等敏感信息，降低直接对外暴露的风险。PiggyMetrics 使用 Secret 来保存相关的账号和密码信息。
您可通过以下两种方式使用 Secret 存放敏感信息：


<dx-tabs>
::: 方式1：使用\sYAML
下文为 PiggyMetrics 创建 Secret 的 YAML。其中 Secret 的 value 需要是 base64 编码后的字符串。
<dx-codeblock>
:::  yaml
# 创建 Secret
apiVersion: v1
kind: Secret
metadata: 
  name: piggymetrics-keys
  namespace: piggymetrics
  labels: 
    qcloud-app: piggymetrics-keys
data: 
  # 请将下面的 XXX 替换为实际值
  MONGODB_USER: XXX
  MONGODB_PASSWORD: XXX
  SW_AGENT_AUTHENTICATION: XXX
type: Opaque
:::
</dx-codeblock>
:::
::: 方式2：使用控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击集群 ID/名称进入集群详情页面。 
2. 单击**配置管理** > **Secret** > **新建**，创建名称为 piggymetrics-keys  的 Secret，如下图所示：
![](https://main.qcloudimg.com/raw/dc936d7e77ea248b79605c7d11aec9f6.jpg)
:::
</dx-tabs>





#### 使用 StatefulSet 部署有状态服务

StatefulSet 主要用于管理有状态的应用，创建的 Pod 拥有根据规范创建的持久型标识符。Pod 迁移或销毁重启后，标识符仍会保留。在需要持久化存储时，您可以通过标识符对存储卷进行一一对应。
PiggyMetrics 项目下的配置服务、注册中心、rabbitmq 等基础组件和服务，本身保存有数据，因此适合使用 StatefulSet 进行部署。

以下是 config-server 对应的部署 YAML 示例：


<dx-codeblock>
:::  yaml
---
kind: Service
apiVersion: v1
metadata: 
  name: config-server
  namespace: piggymetrics
spec: 
  clusterIP: None
  ports: 
    - name: http
      port: 8888
      targetPort: 8888
      protocol: TCP
  selector: 
    app: config
    version: v1

---
apiVersion: apps/v1
kind: StatefulSet
metadata: 
  name: config
  namespace: piggymetrics
  labels: 
    app: config
    version: v1
spec: 
  serviceName: "config-server"
  replicas: 1
  selector: 
    matchLabels: 
      app: config
      version: v1
  template: 
    metadata: 
      labels: 
        app: config
        version: v1
    spec: 
      terminationGracePeriodSeconds: 10
      containers: 
        - name: config
          image: ccr.ccs.tencentyun.com/piggymetrics/config-server:2.0.03
          ports: 
            - containerPort: 8888
              protocol: TCP
:::
</dx-codeblock>



#### 部署工作负载 Deployment

Deployment 声明了 Pod 的模板和控制 Pod 的运行策略，适用于部署无状态的应用程序。PiggyMetrics 的 account 等后台服务都属于无状态应用，适合使用 Deployment。

以下是 account-service Deployment 的 YAML 参数说明：

| 参数             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| replicas         | 表示需要创建的 Pod 数量                                      |
| image            | 镜像的地址                                                   |
| imagePullSecrets | 拉取镜像时需要使用的 key，可在 **[集群](https://console.cloud.tencent.com/tke2/)**>**配置管理** > **Secret**中获取。使用公共镜像时可省略 |
| env              | <li>定义了 pod 的环境变量和取值<br><li>ConfigMap 中定义的 key-value 可使用 configMapKeyRef 引用<br><li>Secret 中定义的 key-value 可使用 secretKeyRef 引用 |
| ports            | 指定容器的端口号，account-service 的端口号为6000       |


account-service Deployment 的 完整 YAML 文件示例如下：

<dx-codeblock>
:::  yaml
# account-service Deployment
apiVersion: apps/v1
kind: Deployment
metadata: 
  name: account-service
  namespace: piggymetrics
  labels: 
    app: account-service
    version: v1
spec: 
  replicas: 1
  selector: 
    matchLabels: 
      app: account-service
      version: v1
  template: 
    metadata: 
      labels: 
        app: account-service
        version: v1
    spec: 
      containers: 
        - name: account-service
          image: ccr.ccs.tencentyun.com/piggymetrics/account-service:1.0.1
          env: 
            # mongodb 的IP地址
            - name: MONGODB_HOST
              valueFrom: 
                configMapKeyRef: 
                  key: MONGODB_HOST
                  name: piggymetrics-env
                  optional: false
            # mongodb 用户名
            - name: MONGODB_USER
              valueFrom: 
                secretKeyRef: 
                  key: MONGODB_USER
                  name: piggymetrics-keys
                  optional: false
            # mongodb 密码
            - name: MONGODB_PASSWORD
              valueFrom: 
                secretKeyRef: 
                  key: MONGODB_PASSWORD
                  name: piggymetrics-keys
                  optional: false
            # TSW 接入点
            - name: SW_AGENT_COLLECTOR_BACKEND_SERVICES
              valueFrom: 
                configMapKeyRef: 
                  key: SW_AGENT_COLLECTOR_BACKEND_SERVICES
                  name: piggymetrics-env
                  optional: false
            # TSW 接入 token
            - name: SW_AGENT_AUTHENTICATION
              valueFrom: 
                secretKeyRef: 
                  key: SW_AGENT_AUTHENTICATION
                  name: piggymetrics-keys
                  optional: false
          ports: 
            # 容器端口
            - containerPort: 6000
              protocol: TCP
      imagePullSecrets: # 拉取镜像的 token
        - name: qcloudregistrykey
:::
</dx-codeblock>




#### 部署服务 Service

Kubernetes 的 ServiceTypes 允许指定 Service 类型，默认为 ClusterIP 类型。ServiceTypes 可取如下值：

- LoadBalancer：提供公网、VPC、内网访问。
- NodePort：可通过“云服务器 IP + 主机端口”访问服务。
- ClusterIP：可通过“服务名 + 服务端口”访问服务。


PiggyMetrics 的前端页面和 gateway 打包在一块，需要对外提供服务，因此指定 LoadBalancer 类型的 ServiceType。TKE 对 LoadBalancer 模式进行了扩展，通过 Annotation 注解配置 Service，可实现更丰富的负载均衡能力。

若使用 `service.kubernetes.io/qcloud-loadbalancer-internal-subnetid` 注解，在 service 部署时，会创建内网类型 CLB。一般建议事先创建好 CLB，service 的部署 YAML 中使用注解 `service.kubernetes.io/loadbalance-id` 直接指定，可提升部署效率。

以下是 gateway service 部署 YAML：


<dx-codeblock>
:::  yaml
# 部署 gateway service
apiVersion: v1
kind: Service
metadata: 
  name: gateway
  namespace: piggymetrics
  annotations: 
    # 请替换成 Subnet-K8S 子网的 CLB 实例 ID
    service.kubernetes.io/loadbalance-id: lb-hfyt76co
spec: 
  externalTrafficPolicy: Cluster
  ports: 
    - name: http
      port: 80
      targetPort: 4000
      protocol: TCP
  selector: # 将后端服务 gateway 和该 Service 进行映射
    app: gateway
    version: v1
  type: LoadBalancer
:::
</dx-codeblock>



#### 查看部署结果

至此，您已完成 PiggyMetrics 在容器服务 TKE 上的部署，可通过以下步骤查看部署结果：

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/)，单击集群 ID/名称进入集群详情页面。
2. 单击**服务与路由** > **Service**进入 “Service 页面”，可查看到创建的 Service。通过 gateway service 的 VIP 即可访问 PiggyMetrics 页面。
![](https://main.qcloudimg.com/raw/0d1934460a8cf1d218eeb9abaad70a01.png)




### 集成 CLS 日志服务

#### 开启容器日志采集功能

容器日志采集功能默认关闭，使用前需要开启，步骤如下：

1. 登录容器服务控制台，选择左侧导航栏中的**集群运维** > **[功能管理](https://console.cloud.tencent.com/tke2/ops/list?rid=1)**。
2. 在“功能管理”页面上方选择地域，单击需要开启日志采集的集群右侧的**设置**。
![](https://main.qcloudimg.com/raw/3d55d97eb5b3fa9f0cfe1c9ea4266561.png)
3. 在“设置功能”页面，单击日志采集**编辑**，开启日志采集后确认。如下图所示：
 ![](https://main.qcloudimg.com/raw/3720d6096ce9486419475ebb5efbaf99.png)





#### 创建日志主题和日志集

日志服务区分地域，为了降低网络延迟，尽可能选择与服务邻近的服务地域创建日志资源。日志资源管理主要分为日志集和日志主题，一个日志集表示一个项目，一个日志主题表示一类服务，单个日志集可以包含多个日志主题。

PiggyMetrics 部署在南京，在“日志主题”页面选择南京地域。因此在创建日志集时应当选择南京地域：
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/logset)，在“日志主题”页面选择南京地域。
2. 单击**创建日志主题**，在弹出的窗口中根据页面提示填写相关信息，如下图所示：
![](https://main.qcloudimg.com/raw/ee9cfda2cb9f49f795d60503627394b3.jpg)
	- **日志主题名称**：输入 piggymetrics。
	- **日志集操作**：选择**创建日志集**。
	- **日志集名称**：输入 piggymetrics-logs。
3. 单击**确定**即可创建日志主题和日志集。
>?PiggyMetrics 有多个后端微服务，为每个微服务建个日志主题便于日志归类。
>- PiggyMetrics 每个服务都建立了一个日志主题。
>- 日志主题 ID，为容器创建日志规则时需要用到。



#### 配置日志采集规则

您可通过控制台或 CRD 两种方式配置容器日志采集规则。


<dx-tabs>
::: 方式1：使用控制台
日志规则指定了日志在容器内的位置：
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/)，选择左侧导航栏中的**集群运维** > **日志规则**。
2. 在“日志规则”页面，单击**新建**新建日志规则：
	- **日志源**：指定容器日志位置，PiggyMetrics 采用 SpringCloud 的默认配置，所有日志都打印到标准输出中，因而使用容器标准输出，并指定具体的 Pod Label。
	- **消费端**：选择之前创建的日志集和主题。
![](https://main.qcloudimg.com/raw/7fc048475e1a0aa9b0df2fe72f8b6ae4.png)
3. 单击**下一步**，进入“日志解析方式”，其中本文示例 PiggyMetrics 使用单行文本方式。了解更多 CLS 支持的日志格式，请参见 [采集文本日志](https://cloud.tencent.com/document/product/614/17418) 文档。
:::
::: 方式2：使用\sCRD
用户还可通过自定义资源定义（CustomResourceDefinitions，CRD）的方式配置日志采集规则。PiggyMetrics 使用了容器文件路径的采集方式，日志格式为单行文本。下文是 account-service 日志采集具体的配置 YAML。了解更多的 CRD 采集配置请参见 [使用 CRD 配置日志采集](https://cloud.tencent.com/document/product/457/48425) 文档。
<dx-codeblock>
:::  yaml
apiVersion: cls.cloud.tencent.com/v1
kind: LogConfig
metadata: 
  name: account-log-rule
spec: 
  clsDetail: 
    extractRule: {}
    # 单行文本
    logType: minimalist_log
    # 日志主题ID
    topicId: 8438cc9b-888f-469f-9cff-9891270a0a13
  inputDetail: 
    # 容器标准输出
    containerStdout: 
      container: account-service
      includeLabels: 
        app: account-service
        version: v1
      namespace: piggymetrics
    type: container_stdout
:::
</dx-codeblock>
:::
</dx-tabs>





#### 查看日志

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/search)，进入“检索分析”页面。
2. 检索分析中可先为日志**新建索引**，索引完毕之后再单击**检索分析**即可查看日志。
![](https://main.qcloudimg.com/raw/b220ef68730b4db35627b178df74a43a.png)
>!若未新建索引，则检索不到日志。



### 集成 TSW 观测服务


微服务观测平台 TSW 目前处于内测阶段，可在广州和上海进行了部署，本文选择上海接入（PiggyMetrics 部署在南京）。


#### 接入 TSW — 获取接入点信息

1. 登录 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm)，选择左侧导航栏种的**服务观测** > **服务列表**。
2. 单击**接入服务**，选择 Java 语言与 SkyWalking 的数据采集方式。接入方式下提供了如下接入信息：**接入点**和 **Token**。
![](https://main.qcloudimg.com/raw/b6333d66cf38310a9fe2403bee7bbb4a.png)


#### 接入 TSW — 应用和容器配置

将上一步骤中获取的 TSW 的**接入点**和 **Token** 分别填写到 skywalking 的 agent.config 里的配置项 collector.backend_service 和 agent.authentication。“agent.service_name” 配置对应的服务名称，可使用 “agent.namespace” 对同一领域下的微服务归类。如下图为 user-service 配置：
![](https://main.qcloudimg.com/raw/905e1c628fdc2c2d5978fb53abf548bf.png)

Skywalking agent 也支持使用环境变量方式进行配置，PiggyMetrics 使用 ConfigMap 和 Secret 配置对应的环境变量：
- 使用 ConfigMap 配置 `SW_AGENT_COLLECTOR_BACKEND_SERVICES`
- 使用 Secret 配置 `SW_AGENT_AUTHENTICATION`

如下图所示：
![](https://main.qcloudimg.com/raw/8754378056b4627fc6a4699a606c050d.png)

至此 TSW 接入工作已完成，启动容器服务后，在 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm) 即可查看调用链、服务拓扑、SQL 分析等功能。


### 使用 TSW 观测服务

#### 通过服务接口和调用链查看调用异常


1. 登录 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm)，选择左侧导航栏中的**服务观测** > **接口观测**。
2. 在接口观测页面可查看一个服务下所有接口的调用情况，包括请求量、成功率、错误率、响应时间等指标。如下图所示：
![](https://main.qcloudimg.com/raw/be6a75b0051e2b1e4dd391e5fd8bf421.png)
图中展示的是最近1小时内 gateway 和 account-service 响应时间过大，statistic-service 所有请求全部失败。
4. 单击服务名称 statistics-service 进入该服务的信息页，单击**接口观测**可以查看到接口 `{PUT}/{accountName}` 抛出了 NestedServletException 异常，从而导致该接口不可用。如下图所示：
![](https://main.qcloudimg.com/raw/ce6e9378efdcb463996be66f8688f2fa.png)
4. 单击 Trace ID 后可以查看完整的调用链详情。如下图所示：
![](https://main.qcloudimg.com/raw/1950bf30b2f0f29b6858a58e613ce58b.png)



#### 查看服务拓扑

1.  登录 [腾讯微服务观测平台控制台](https://console.cloud.tencent.com/apm)，选择左侧导航栏中的**链路追踪** > **分布式依赖拓扑**。
2.  在“分布式依赖拓扑”页面可查看完成的服务依赖情况，以及调用次数和平均延迟等信息。如下图所示：
![](https://main.qcloudimg.com/raw/b10385d0e2721effa6a0652cd243ab6b.png)

```
