## 操作场景

微服务引擎 TSE 提供将 K8s 集群关联到 Polarismesh 的能力，Polaris Controller 可以同步您 Kubernetes 集群上的 Namespace，Service，Endpoints 等资源到 Polaris 中，从而实现 K8s Service 自动注册到 Polarismesh ，使用 Polarismesh API 和多语言 SDK 可以访问，使用 gRPC 和 Spring Cloud 等开源框架也可以访问。主要适用于以下场景：

- 异构系统与多技术栈场景下，SpringCloud 等框架服务调用 K8s 集群服务。
- 跨集群场景下的服务调用。

本文介绍通过 TSE 控制台使用 K8s 集群的能力。


## 操作步骤

### 创建引擎

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击目标引擎的“ID”，进入基本信息页面。
3. 在左侧页签单击 **K8s 集群**，单击**关联集群**。根据自身业务需求选择目标关联的 K8s 集群，支持 [TKE](https://cloud.tencent.com/product/tke) (容器集群) / [EKS](https://cloud.tencent.com/product/eks) (弹性容器集群)。

![](https://qcloudimg.tencent-cloud.cn/raw/455c1e3826f61d957c94f8130d45af00.png)




