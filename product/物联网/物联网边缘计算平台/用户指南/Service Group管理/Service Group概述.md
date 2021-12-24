原生 Kubernetes 无法控制 工作负载的 Pod 创建的具体节点位置，往往需要对不同机房或区域划分不同集群来进行隔离，避免服务跨区域访问。IECP 提供 ServiceGroup 功能，轻松实现上百地域的服务部署，且无需进行应用适配或改造。
假设以下业务场景：在跨地域的酒店项目中共有30个边缘节点，每个酒店部署3个节点，若以原生 Kubernetes 机制约需要10个边缘单元提供服务实现业务隔离。
![](https://qcloudimg.tencent-cloud.cn/raw/ef1e4c6fdb19305581bce6df9b5afdde.png)
IECP 的 ServiceGroup 功能提供 DeploymentGrid 和 ServiceGrid 两种自研 Kubernetes 资源，用户只需提前规划好 NodeGroup 及 Zone 和边缘节点的关系，即可方便地将服务分别部署到这些节点组中，并进行服务流量管控。
在同样场景下，30个边缘节点可以纳管到同一个边缘单元中，大大减少边缘单元消耗。用户通过 NodeGroup 可下发 Grid 资源，在所属 zone 内节点即可自动完成边缘服务的部署。
![](https://qcloudimg.tencent-cloud.cn/raw/e50d64fcc20efc9c07ca7bf0a33b980d.png)
