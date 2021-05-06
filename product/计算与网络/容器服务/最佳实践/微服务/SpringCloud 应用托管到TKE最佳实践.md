## 1. 最佳实践场景

本文章介绍了 SpringCloud 应用托管到腾讯云容器服务 TKE 的最佳实践。

SpringCloud 应用托管到 TKE 具有以下优势：

- 提升资源利用率
- Kubernetes 天然适合微服务架构
- 提升运维效率，便于 Devops 落地实施
- Kubernetes 的高弹性，可轻松实现应用的动态扩缩容
- TKE 提供了 Kubernetes Master 托管功能，减少了 Kubernetes 集群运维和管理的负担
- TKE 和腾讯云的其它云原生产品做了整合和优化，帮助用户更好的使用腾讯云上产品

## 2. 最佳实践实例介绍

### 2.1 PiggyMetrics 介绍

本最佳实践 fork 了 github 上的开源项目 [PiggyMetrics](https://github.com/sqshq/piggymetrics) ，并对其做了修改以适应腾讯云上产品，并以最终修改后的版本为例，详细介绍 SpringCloud 应用托管到 TKE 的整个过程。PiggyMetrics 首页如下图展所示：

![](https://main.qcloudimg.com/raw/40a504b665b76ab16e32394f2594350f.jpg)

PiggyMetrics 是一个采用微服务架构，并使用 SpringCloud 框架开发的个人记账理财的应用。PiggyMetrics 服务组成如下：

-  **API网关** ：基于Spring Cloud Zuul的网关，是调用后台API的聚合入口，实现反向路由和负载均衡(Eureka+Ribbon)、限流熔断(Hystrix)等功能。CLIENT单页应用和ZUUL网关暂住在一起，简化部署。
-  **服务注册和发现** ：基于Spring Cloud Eureka 的服务注册中心。业务服务启动时通过Eureka注册，服务之间调用也通过Eureka做服务发现。
-  **授权认证服务** ：基于Spring Security OAuth2 的授权认证中心。客户端登录时通过 AUTHSERVICE 获取访问令牌。服务之间调用也通过AUTHSERVICE获取访问令牌(走客户端模式)。令牌校验方式~各资源服务器去AUTHSERVICE集中校验令牌。
-  **配置服务** ：基于 Spring Cloud Config 的配置中心，集中管理所有Spring服务的配置文件。
-  **软负载和限流熔断** ：基于Spring Cloud Ribbon&Hystrix，Zuul 调用后台服务，服务之间相互调用都通过Ribbon实现软负载，也通过Hystrix实现熔断限流保护。
-  **METRICS & DASHBOARD** ：基于 Spring Cloud Turbine + Hystrix Dashboard，对所有 Hystrix 产生的 Metrics 流进行聚合，并展示在Hystrix Dashboard上。

修改后的 PiggyMetrics 部署项目托管在 GitHub 上，对应的地址为 <https://github.com/TencentCloud/container-demo/tree/main/springcloud-on-tke>


### 2.2 PiggyMetrics 部署架构和组件

最佳实践实例模拟将原先部署在 CVM 上的应用容器化并托管到 TKE 的场景。采用一个 VPC，并划分为两个子网：

- Subnet-Basic 中部署了有状态的基础服务，包括 Dubbo 的服务注册中心 Nacos，MySQL 和 Redis 等。
- Subnet-K8S 中部署 PiggyMetrics 的应用服务，所有服务都进行了容器化，运行在 TKE 上；

![](https://main.qcloudimg.com/raw/4aac0ba2c480d69ba6a581bb8a4fcdd1.png)

PiggyMetrics 实例的网络规划如下表所示：

| 网络规划              | 说明    |
| :--------------| :---- | 
| Region / AZ          | 南京 / 南京一区    |
| VPC                     | CIDR：10.0.0.0/16 |
| 子网 Subnet-Basic | 南京一区，CIDR：10.0.1.0/24 |
| 子网 Subnet-K8S   | 南京一区，CIDR：10.0.2.0/24 |
| Nacos 集群           | 采用 3 台 “标准型SA2“ 1C2G 机型的 CVM 构建 Nacos 集群，对应的 IP 为：10.0.1.9，10.0.1.14，10.0.1.15 |

PiggyMetrics 实例中用到的组件如下表所示：

| 组件  | 版本   | 来源       | 备注       |
|:---- |:------:|:------:|:------|
| K8S  | 1.8.4  | 腾讯云    | TKE 托管模式 |
| MongoDB  |  4.0         | 腾讯云    | TencentDB for MongoDB WiredTiger 引擎版 |
| CLS      |  N/A        | 腾讯云    | 日志服务 |
| TSW      |  N/A       | 腾讯云    | 采用 Skywalking 8.4.0 版的 agent 接入，点此 [下载](https://archive.apache.org/dist/skywalking/8.4.0/apache-skywalking-apm-8.4.0.tar.gz) |
| JAVA    | 1.8           | 开源社区  | Docker 镜像：java:8-jre |
| SrpingCloud | Finchley.RELEASE | 开源社区  | [Spring Cloud 官网](https://spring.io/projects/spring-cloud) |


## 3. 基础服务集群搭建

- 在 [Mongodb 控制台](https://console.cloud.tencent.com/mongodb) 创建好实例, 初始化；

   ~~~sh
   # 下载 mongo client, 解压，进入 bin 目录
   wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.6.18.tgz
   
   tar -zxvf mongodb-linux-x86_64-3.6.18.tgz
   cd mongodb-linux-x86_64-3.6.18/bin
   
   # 使用下面命令初始化 mongodb，其中 mongouser 为创建 mongodb 实例时创建的管理员账号
   ./mongo -u mongouser -p --authenticationDatabase "admin" [mongodb的IP]/piggymetrics mongo-init.js

   ~~~
   
   mongodb 初始化脚本 **mongo-init.js** 中默认创建了一个 piggymetrics 库的用户 **guest**，可按你的需要修改。


- 在 [CLB 控制台](https://console.cloud.tencent.com/clb) 为子网 Subnet-K8S 新建个内网型的 CLB（后面会用到该 CLB 实例 ID）。


## 4. 构建 docker 镜像

### 4.1 编写 Dockerfile

下面以 account-service 为例简单介绍下 Dockerfile 的编写。下面展示的是 account-service 的工程目录结构，**Dockerfile** 位于工程的根目录下，**account-service.jar** 是打包后的文件，需要添加到镜像中的。

~~~sh
➜  account-service tree
├── Dockerfile
├── skywalking
│   ├── account.config
│   └── skywalking-agent.zip
├── pom.xml
├── src
│    ....
├── target
│    .....
│   └── account-service.jar
└── account-service.iml
~~~

account-service 的 Dockerfile 如下：
 
~~~docker
FROM java:8-jre# 容器中的工作目录为 /appWORKDIR /app
# 将本地打包出来的应用添加到镜像中ADD ./target/account-service.jar  .

#  将 skywalking agent 拷贝到镜像中COPY ./skywalking/skywalking-agent.zip .
#  解压 skywalking agent  并删除原始压缩文件RUN unzip skywalking-agent.zip && rm -f skywalking-agent.zip
# 添加 skywalking 的配置文件COPY ./skywalking/account.config ./skywalking-agent/config/agent.config
# 启动应用CMD ["java", "-Xmx256m", "-javaagent:/app/skywalking-agent/skywalking-agent.jar", "-jar", "/app/account-service.jar"]
# 应用的端口说明EXPOSE 6000
~~~

> **【Tips】:**
> - Dockerfile 中每多一个 RUN 命令，生成的镜像就多一层，最佳做法是将这些 RUN 命令合成一条。


### 4.2 镜像构建

TKE 容器服务提供了自动和手工构建方式，文档 [镜像构建](https://cloud.tencent.com/document/product/1141/50337) 中有详细描述。为了展示具体的构建过程，本文采用手工构建方式。

镜像名称需要符合规范 ***ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]***，其中命名 namespace 是为了方便镜像管理使用，可以按项目取名，本人采用 piggymetrics 表示 PiggyMetrics 项目下的所有镜像；ImageName 可以包含 subpath 一般用于企业用户多项目情形下。此外，如果本地已构建好了镜像，可以使用 `docker tag` 命令，按命名规范对镜像重命名。

~~~sh
# 推荐的构建方式，可省去二次打 tag 操作
sudo docker build -t ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]

# 本地构建 account-service 镜像，最后一个 . 表示 Dockerfile 存放在当前目录（user-service）下
➜  account-service docker build -t ccr.ccs.tencentyun.com/piggymetrics/account-service:1.0.0 .

# 将已存在镜像按命名规范对镜像重命名
sudo docker tag [ImageId] ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
~~~

构建完成后，可使用 `docker images` 命令查看本地仓库中的所有镜像。

![](https://main.qcloudimg.com/raw/64ebfe03265b1d95ebe6bb5a3cf02bf1.png)

## 5 上传镜像到 TCR

### 5.1 TCR

腾讯云[容器镜像服务 TCR](https://cloud.tencent.com/product/tcr)，提供了个人版和企业版两种镜像仓库。两者区别如下：

- 个人版镜像仓库仅部署在腾讯云广州，企业版在每个地域都有部署；
- 个人版没有服务 SLA 保证。

![](https://main.qcloudimg.com/raw/5238be60ec6209b7885d7865d205622b.png)

由于 PiggyMetrics 只是个 Dubbo 容器化的 demo 项目，因而个人版完全满足需求。但对于企业用户，推荐使用[企业版 TCR](https://console.cloud.tencent.com/tcr)。有关镜像仓库的具体操作，请见文档 [“镜像仓库基本操作”](https://cloud.tencent.com/document/product/1141/41811)。


### 5.2 创建命名空间

PiggyMetrics 项目采用个人版镜像仓库（对于企业客户建议使用企业版镜像仓库）。在 [容器服务控制台](https://console.cloud.tencent.com/tke2) 下的 【镜像仓库】->【个人版】-> 【命名空间】新建一个命名空间 piggymetrics。PiggyMetrics 项目所有的镜像都存放于该命名空间下。

![](create-tcr-ns.png)
![](https://main.qcloudimg.com/raw/8ce7fe4038a8255a5b92daf732c868a0.png)

### 5.3 上传镜像


镜像上传，需要两个步骤：登录腾讯云 registry 和 上传镜像，下面详细介绍 PiggyMetrics 镜像的上传过程。


- **Step 1.  登录腾讯云registry**

  ~~~sh
  docker login --username=[腾讯云账号 ID] ccr.ccs.tencentyun.com
  ~~~

  腾讯云账号 ID 可在 [账号信息](https://console.cloud.tencent.com/developer) 页面获取。若忘记 **镜像仓库登录密码**，可在下图所示的容器服务控制台中重置。

  ![](change-trc-pwd.png)
	![](https://main.qcloudimg.com/raw/665fd18ad26a7d96303228ed4c3325cd.png)

  若提示无权限，请加上 sudo 执行上述命令时，需要输入两个密码：第一个为 sudo 所需的主机管理员密码；第二个为 **镜像仓库登录密码**。

  ~~~sh
  sudo docker login --username=[腾讯云账号 ID] ccr.ccs.tencentyun.com
  ~~~

  ![](registry-pwd.png)
	![](https://main.qcloudimg.com/raw/49dae6333017df06971523f184a7ea55.png)


- **Step 2：上传镜像**

  本地生成好的镜像，使用下面命令即可上传到 TKE 的镜像仓库中。

  ~~~sh
  docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
  ~~~

  ![](upload-user-image.png)
	![](https://main.qcloudimg.com/raw/fe77822b6ef853063f593042698e112b.png)

在 [我的镜像](https://console.cloud.tencent.com/tke2/registry/user/self?rid=1) 中可以查看上传的所有镜像，下图展示的是上传到腾讯云镜像仓库中 PiggyMetrics 的 9 个镜像。

![](my-images.png)
![](https://main.qcloudimg.com/raw/8b7943e0e4d2b4d440e7db385360d7ec.png)

TCR 镜像默认镜像为“私有”，若想供任何人使用，可在【镜像信息】中设置为公有。

![](public-registry.png)
![](https://main.qcloudimg.com/raw/dc189577913dc49539ffb21186e7b9a8.png)


## 6. 在TKE 上部署服务

### 6.1 创建 k8s 集群 PiggyMetrics

实际部署前，需要新建个 K8S 集群。有关集群的创建，官方文档 [购买容器集群](https://cloud.tencent.com/document/product/457/9082) 中有详细说明。但有一点需要注意：在创建集群第二步 “选择机型” 时，建议开启 “置放群组功能” 可将 CVM 打散到到不同母机上，增加系统可靠性。

![](zhifangqunzu.png)
![](https://main.qcloudimg.com/raw/4a361e6e09f65d1acfbe96c2d5571fd2.png)

创建完成后，在容器服务控制台的 [集群管理](https://console.cloud.tencent.com/tke2/cluster) 页面可以看到新建的集群信息。这里我们新建的集群名称为 piggyMetrics。

![](piggymetrics-k8s-cluster.png)
![](https://main.qcloudimg.com/raw/2868bf23d0b5940237ce96a66cf7e8af.png)

选择集群 PiggyMetrics-k8s-demo 点击进入 **基本信息** 页面，可以看到整个集群的配置信息。

![](k8s-cluster-basic-info.png)
![](https://main.qcloudimg.com/raw/c26177c48fefa201d400f37c4cc70d1f.png)

如果需要使用 kubectl 和 lens 等 K8S 管理工具，还需要以下两步操作：

- 开启外网访问
- 将 api 认证 Token 保存为本地 `用户 home/.kube` 下的 config 文件中（若 config 文件已有内容，需要替换），这样每次访问都能进入默认集群中。当然也可以不保存为 `.kube` 下的 config 文件中，相关操作指引见  **集群APIServer信息** 下的 **通过Kubectl连接Kubernetes集群操作说明**。

![](apiserver.png)
![](https://main.qcloudimg.com/raw/d447b8df5f1cbcc1c585e0080e11bf84.png)


### 6.2 创建 Namespace

Namespaces 是 Kubernetes 在同一个集群中进行逻辑环境划分的对象， 可以通过 Namespaces 进行管理多个团队多个项目的划分。在[容器服务控制台](https://console.cloud.tencent.com/tke2) ->【集群】->【命名空间】下创建名称为 PiggyMetrics 的Namespace；

更快捷也是推荐的方法是在本地使用命令 kubectl 命令创建：

- 方式 1：直接使用命令行

  ~~~sh
  kubectl create namespace piggymetrics
  ~~~

- 方式 2：使用 yaml 部署

  ~~~sh
   kubctl create –f namespace.yaml
  ~~~

  其中 namespace.yaml 如下： 

  ~~~yaml
  # 创建命名空间 piggymetrics
  apiVersion: v1
  kind: Namespace
  metadata:
    name: piggymetrics
  spec:
    finalizers:
    - kubernetes
  ~~~

### 6.3 使用 ConfigMap 存放配置信息

通过 ConfigMap 可以将配置和运行的镜像进行解耦，使得应用程序有更强的移植性。PiggyMetrics 后端服务需要从环境变量中获取 MongoDB 的主机和端口信息，这里使用 ConfigMap 来保存。
下面是 PiggyMetrics 的 ConfigMap yaml，需要注意一点：纯数字类型的 value 需要用引号括起来。

~~~yaml
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
~~~

此外，也可以手工在[容器服务控制台](https://console.cloud.tencent.com/tke2) ->【集群】 ->【配置管理】-> ConfigMap 下创建名称为 piggymetrics-env 的 ConfigMap 用于存放相关配置。创建是选择命名空间 PiggyMetrics，如下图:

![](https://main.qcloudimg.com/raw/e7e206387834bba8fa29658c579dea24.png)

### 6.4 使用 Secret 存放敏感信息

Secret 可用于存储密码、令牌、密钥等敏感信息，降低直接对外暴露的风险。PiggyMetrics 使用 Secret 来保存相关的账号和密码信息。下面是为 PiggyMetrics 创建 Secret 的 yaml。使用 yaml 时需要注意一点：Secret 的 value 需要是 base64 编码后的字符串。

~~~yaml
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
~~~
  
此外，也可以手工在[容器服务控制台](https://console.cloud.tencent.com/tke2) ->【集群】 ->【配置管理】-> Secret 下创建名称为 **PiggyMetrics-keys**  的 secret，如下图所示。

![](create-secret.png)
![](https://main.qcloudimg.com/raw/674ea465fc79423a85cb118a2f717ded.png)


### 6.5 使用 StatefulSet 部署有状态服务

StatefulSet 主要用于管理有状态的应用，创建的 Pod 拥有根据规范创建的持久型标识符。Pod 迁移或销毁重启后，标识符仍会保留。 在需要持久化存储时，您可以通过标识符对存储卷进行一一对应。
PiggyMetrics 项目下的配置服务、注册中心、rabbitmq 等基础组件和服务，本身保存有数据，因而适合使用 StatefulSet 来部署。
下面是 config-server 对应的部署 yaml。

~~~yaml
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
~~~


### 6.6 部署工作负载 Deployment

Deployment 声明了 Pod 的模板和控制 Pod 的运行策略，适用于部署无状态的应用程序。PiggyMetrics 的 account 等后台服务都属于无状态应用，适合使用 Deployment。

下面是 account-service Deployment 的 yaml，有几点需要说明：

- replicas：表示需要创建的 pod 数量；
- image：镜像的地址；
- imagePullSecrets：拉取镜像时需要使用的key，在【集群 ->【配置管理 ->【Secret】里可以找到。使用公共镜像时，可省略。
- env：定义了 pod 的环境变量和取值，ConfigMap 中定义的 key-value 可使用 configMapKeyRef 引用；Secret 中定义的 key-value 可使用 secretKeyRef 引用。
- ports：指定容器的端口号，account-service 的端口号为 6000。

~~~yaml
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
~~~


### 6.7 部署服务 Service

Kubernetes 的 ServiceTypes 允许指定 Service 类型，默认为 ClusterIP 类型。ServiceTypes 的可取如下值：

- LoadBalancer：提供 公网、VPC、内网 访问；
- NodePort：可以通过 云服务器 IP + 主机端口 访问服务；
- ClusterIP：可以通过 服务名 + 服务端口 访问服务；

PiggyMetrics 的前端页面和 gateway 打包在一块，需要对外提供服务，因而指定 LoadBalancer 类型的 ServiceType。TKE 对 LoadBalancer 模式进行了扩展，通过 Annotation 注解配置 Service，可实现更丰富的负载均衡能力。若使用 **service.kubernetes.io/qcloud-loadbalancer-internal-subnetid** 注解，在 service 部署时，会创建内网类型 CLB。一般都事先创建好 CLB，service 的部署 yaml 中使用注解 **service.kubernetes.io/loadbalance-id** 直接指定，提升部署效率。下面是 gateway service 部署 yaml。

~~~yaml
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
~~~

### 6.8 查看部署结果

至此，已完成 PiggyMetrics 在 TKE 上的部署。通过容器服务控制台，在【集群】->【服务与路由】->【Service】下可以看到创建的 Service，通过 gateway service 的 VIP 就可以访问 PiggyMetrics 的页面了。

![](https://main.qcloudimg.com/raw/20b3d6cb1aa6c59cb8b54d2e37cbb705.png)

## 7 集成 CLS 日志服务

### 7.1 开启容器日志采集功能

容器日志采集功能默认关闭，使用前需要开启，步骤如下：

- 登录 容器服务控制台，选择左侧导航栏中的【集群运维】->【功能管理】。
- 在“功能管理”页面上方选择地域，单击需要开启日志采集的集群右侧的【设置】。

  ![](https://main.qcloudimg.com/raw/e81ce8f47754e08e4d865705765546e7.png)

  在“设置功能”页面，单击日志采集【编辑】，开启日志采集后确认。如下图所示：

  ![](https://main.qcloudimg.com/raw/bb1204a25d3621de4f37c857e38aaf0c.png)

### 7.2 创建日志集

日志服务区分地域，为了降低网络延迟，尽可能选择与服务邻近的服务地域创建日志资源。日志资源管理主要分为日志集和日志主题，一个日志集表示一个项目，一个日志主题表示一类服务，单个日志集可以包含多个日志主题。PiggyMetrics 部署在南京，故在 [日志服务控制台](https://console.cloud.tencent.com/cls/logset) 选择日志服务区域南京。然后点击“创建日志集” 创建日志集 PiggyMetrics-logs。

![](https://main.qcloudimg.com/raw/33c5481392818f830fd060df830eedfa.png)

### 7.3 创建日志主题

在 [日志服务控制台](https://console.cloud.tencent.com/cls/logset) 单击“日志集名称”，进入到日志主题管理页面。单击 “新增日志主题”，开始创建日志主题。PiggyMetrics 有多个后端微服务，为每个微服务建个日志主题便于日志归类。

- PiggyMetrics 每个服务都建立了一个日志主题。
- 日志主题 ID，为容器创建日志规则时需要用到。

![](https://main.qcloudimg.com/raw/6e55eb8600d3315aff38ccd24dd30255.png)


### 7.4 配置日志采集规则

可通过控制台或 CRD 两种方式配置容器日志采集规则。

#### 7.4.1 通过容器服务控制台配置日志采集规则

日志规则指定了日志在容器内的位置，在容器服务控制台左侧导航栏中的【集群运维】->【日志规则】中可新建日志规则。

- 日志源：指定容器日志位置，PiggyMetrics采用SpringCloud的默认配置，所有日志都打印到标准输出中，因而使用容器标准输出，并指定具体的 Pod Label。
- 消费端：选择之前创建的日志集和主题。

![](https://main.qcloudimg.com/raw/582d521d7fb3af06fdcebb08936df2e9.png)

点击下一步，进入 “日志解析方式”，简单起见 PiggyMetrics 使用单行文本方式，这里不再赘述。 CLS 支持的日志格式见文档：<https://cloud.tencent.com/document/product/614/17418> 。

#### 7.4.2 通过 CRD 创建容器日志采集规则

用户还可通过自定义资源定义（CustomResourceDefinitions，CRD）的方式配置日志采集规则。PiggyMetrics 使用了容器文件路径的采集方式，日志格式为单行文本，下面是 account-service 日志采集具体的配置 yaml。更多的 CRD 采集配置参考：<https://cloud.tencent.com/document/product/457/48425>

~~~yaml
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
~~~

### 7.5 查看日志

在[日志服务控制台](https://console.cloud.tencent.com/cls/search)的【检索分析】中可先为日志【新建索引】，让后点击 【检索分析】按钮即可查看日志。未建索引，会看不到日志，这点需要注意。

![](https://main.qcloudimg.com/raw/58d120aaf5b52d789cc7b32ccab3bd01.png)

## 8 集成 TSW 观测服务

### 8.1 TSW 简介

腾讯微服务观测平台 TSW（Tencent Service Watcher）提供云原生服务可观察性解决方案，能够追踪到分布式架构中的上下游依赖关系，绘制拓扑图，提供服务、接口、实例、中间件等多维度调用观测。有关 TSW 的详细特性和使用方式，参见：<https://cloud.tencent.com/product/tsw>

![](https://main.qcloudimg.com/raw/c8a7d6384a7f40a8761d9b622b58e6f5.png)

TSW 在架构上分为以下四大模块：

- 数据采集（Client）：

  使用开源探针或 SDK 用于采集数据。对于迁移上云的用户，可保留 Client 端的大部分配置，仅更改上报地址和鉴权信息即可。

- 数据处理（Server）：

  数据经由 Pulsar 消息队列上报到 Server，同时 Adapter 会将数据转换为统一的 Opentracing 兼容格式。根据数据的使用场景，分配给实时计算与离线计算。实时计算提供实时监控、统计数据展示，并对接告警平台快速响应。离线计算处理长时段大量数据的统计汇聚，利用大数据分析能力提供业务价值。
  
- 存储（Storage）：

  存储层可满足不同数据类型的使用场景，适配 Server 层的写入与 Data Usage 层的查询与读取请求。
  
- 数据使用（Data Usage）：

  为控制台操作、数据展示、告警提供底层支持。

![](https://main.qcloudimg.com/raw/314b04572a404ffa944e2ae3a599257c.png)

### 8.2 接入 TSW — 获取接入点信息

TSW 目前处于公测阶段，可在页面 <https://cloud.tencent.com/apply/p/rvo6c9fnug> 申请内测后使用 TSW 控制台 <https://console.cloud.tencent.com/tsw> 接入服务。目前 TSW 支持 JAVA 和 Golang 两种语言接入。

在 TSW 控制台的【服务观测】->【服务列表】页，单击【接入服务】，选择 Java 语言与 SkyWalking 的数据采集方式。接入方式下提供了如下接入信息：**接入点** 和 **Token**。

![](https://main.qcloudimg.com/raw/e579bdec92d1a2cd08c8bdbdfc6c161a.png)

>TSW 目前处于公测阶段，只在 广州 和 上海 进行了部署，在写本实例时选择了上海接入（PiggyMetrics 部署在南京）。

### 8.3 接入 TSW — 应用和容器配置

将上一节中获取的 TSW 的 接入点 和 Token 分别与填写到 skywalking 的 agent.config 里的配置项 collector.backend_service 和 agent.authentication。“agent.service_name” 配置上对应的服务名称，可使用 “agent.namespace” 对同一领域下的微服务归类。下图是 user-service 的配置。

![](https://main.qcloudimg.com/raw/905e1c628fdc2c2d5978fb53abf548bf.png)

Skywalking agent 也支持使用环境变量方式进行配置，PiggyMetrics 使用 ConfigMap 和 Secret 配置对应的环境变量：

- 使用 ConfigMap 配置 `SW_AGENT_COLLECTOR_BACKEND_SERVICES`
- 使用 Secret 配置 `SW_AGENT_AUTHENTICATION`

![](https://main.qcloudimg.com/raw/8754378056b4627fc6a4699a606c050d.png)

至此 TSW 接入工作已完成，启动容器服务后，在 TSW 控制台即可查看调用链、服务拓扑、SQL分析等功能。

### 8.4 使用 TSW 观测服务

#### 8.4.1 通过服务接口和调用链查看调用异常

在 [TSW 控制台](https://console.cloud.tencent.com/tsw)【服务观测】-> 【接口观测】页面可查看一个服务下所有接口的调用情况：请求量、成功率、错误率、响应时间等指标。

![](https://main.qcloudimg.com/raw/3a8e11a677817132afbad70270ccb5b7.png)

上图展示了最近1小时内 gateway 和 account-service 的响应时间过大，statistic-service 所有请求全部失败。点击服务名称 statistics-service 进入该服务的信息页，再点击【接口观测】可以看到接口 `{PUT}/{accountName}` 抛了 NestedServletException 异常，从而导致该接口不可用。

![](https://main.qcloudimg.com/raw/914ea9842ca29f7aa065d79f61b6c7a4.png)

点击 Trace ID 后可以看到完整的调用链详情：

![](https://main.qcloudimg.com/raw/9cb209440a99f4c50b8036e1e2b34159.png)


### 8.4.2 查看服务拓扑

在 TSW 控制台【链路追踪】-> 【分布式依赖拓扑】页面可查看完成的服务依赖情况，以及调用次数和平均延迟等信息。

![](https://main.qcloudimg.com/raw/37a22ad8baf1259621cb5d6357bf635b.png)

