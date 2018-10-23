腾讯云容器服务(Tencent Kubernetes Engines)是高度可扩展的高性能容器管理服务，您可以在托管的云服务器实例集群上轻松运行应用程序。使用该服务，您将无需安装、运维、扩展您的集群管理基础设施，只需进行简单的 API 调用，便可启动和停止 Docker 应用程序，查询集群的完整状态，以及使用各种云服务。您可以根据资源需求和可用性要求在集群中安排容器的置放，满足业务或应用程序的特定要求。

了解腾讯云容器服务，会涉及到以下基本概念：
- **[集群](https://cloud.tencent.com/doc/product/457/6779)**：是指容器运行所需云资源的集合，包含了若干台云服务器、负载均衡器等腾讯云资源。
- **[服务](https://cloud.tencent.com/doc/product/457/6780)**：由多个相同配置的容器和访问这些容器的规则组成的微服务。
- **[配置项](https://cloud.tencent.com/document/product/457/10173)**:配置项是多个配置的集合，帮您管理不同环境和不同业务。
- **[Ingress](https://cloud.tencent.com/document/product/457/9111)***:Ingress 是用于将外部 HTTP(S) 流量路由到服务（service）的规则集合。
- **[镜像仓库](https://cloud.tencent.com/doc/product/457/6781)**：用于存放 Docker 镜像，Docker 镜像用于部署容器服务。
- **实例(Pod)**：由相关的一个或多个容器构成一个实例，对应 kubernetes 的 pod，这些容器共享相同的存储和网络空间。
- **节点(Node)**：一台已注册到集群内的云服务器。

## 腾讯云容器服务怎么用
见下图，您只需要三步即可运行服务。
1. 创建集群
2. 创建服务
3. 运行服务
![Alt text](https://mc.qcloudimg.com/static/img/cb0d84fd7c9547d492ab07f2992093d1/Image+054.png)

## 相关服务

- 通过购买若干个云服务器组成容器服务集群，容器运行在云服务器中。有关更多信息，请参阅 [云服务器产品文档](https://cloud.tencent.com/doc/product/213)。
- 集群可以建立在私有网络下，集群内主机可以分配在不同可用区的子网下。有关更多信息，请参阅 [私有网络产品文档](https://cloud.tencent.com/doc/product/215)。
- 可以使用负载均衡，自动分配横跨多个云服务实例的客户端请求流量，再转发到主机内容器。有关更多信息，请参阅 [负载均衡产品文档](https://cloud.tencent.com/doc/product/214)。
- 监控容器服务集群和容器实例的运行统计数据，可使用云监控。有关更多信息，请参阅 [云监控产品文档](https://cloud.tencent.com/doc/product/248)。

## 腾讯云容器服务定价

容器服务暂不收取服务本身费用，用户只需要按实际使用的云资源收费。关于收费模式和具体价格，请参阅 [容器服务定价](https://cloud.tencent.com/doc/product/457/6770)。
