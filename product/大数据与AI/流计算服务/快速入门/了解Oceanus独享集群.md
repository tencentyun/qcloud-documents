流计算 Oceanus 目前提供基于独享集群的购买和部署模式，用户可以在自己的集群中运行各类作业，并进行相关资源管理。
>? 基于流计算 Oceanus 的这种架构模式，流计算 Oceanus 访问用户 VPC 下的各类资源前，需要获得用户帐户的访问授权，详情请参见 [流计算服务委托授权](https://cloud.tencent.com/document/product/849/38290)。

用户可以在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/cluster) 创建自己的独享计算集群，集群拥有与其他用户完全独立的资源（CPU、内存、磁盘、网络），以确保 Flink 作业运行时的安全性和隔离性。独享集群以 VPC 的方式进行隔离，因此在独享模式下支持用户自定义 JAR 作业和用户自定义 UDF 函数，满足您的定制化业务需求。

当独享集群的 VPC 与用户指定的 VPC 建立互通关系后，JAR 模式的作业即可访问用户特定 VPC 下的所有网络可达的资源，包括但不限于该 VPC 下的各项腾讯云服务，例如消息队列、数据库、API 服务、云服务器 CVM 等。

此外，如果在这个指定的 VPC 下购买 [NAT 网关](https://cloud.tencent.com/document/product/552) 并妥善配置路由表，即可访问公网的互联网地址（例如公网上的 API、其他云服务厂商的组件等），进一步增强流计算作业的处理能力。
![共享集群架构](https://main.qcloudimg.com/raw/e898529172c0950320a953d8de962fab.png)

