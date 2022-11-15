
容器服务 TKE 产品自从对外提供服务以来，服务了众多用户，随产品能力日益丰富，为进一步提高用户体验，容器服务 TKE 计划于 2022 年 6 月 15 日正式将 TKE 云 API 2.0 相关接口下线。全新的 API 3.0 接口文档更加规范和全面，统一的参数风格和公共错误码，统一的 SDK/CLI 版本与 API 文档严格一致，给您带来简单快捷的使用体验。本次接口下线不涉及数据迁移，接口下线后可能会对您的集群管理造成影响，为避免影响您的业务，建议尽快将服务升级至 TKE API 3.0 接口。



### TKE API 2.0 切换 TKE API 3.0 接口对照表

| 2.0 调用接口 	| 2.0 调用接口名称 	| 3.0 调用接口 	|
|---	|---	|---	|
| AddClusterInstances 	| 扩展集群节点 	| [CreateClusterInstances](https://cloud.tencent.com/document/product/457/36707) 	|
| CheckClusterRouteTableCidrConflict 	| 检查集群路由表 CIDR 冲突 	| [DescribeRouteTableConflicts](https://cloud.tencent.com/document/product/457/37180) 	|
| CreateCluster 	| 创建集群 	| [CreateCluster](https://cloud.tencent.com/document/product/457/34527) 	|
| CreateClusterNamespace 	| 创建集群命名空间 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| CreateClusterRoute 	| 创建集群路由 	| [CreateClusterRoute](https://cloud.tencent.com/document/product/457/37186) 	|
| CreateClusterService 	| 创建服务 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| CreateEmptyCluster 	| 创建空集群 	| 下线 	|
| CreateLogCollector 	| 创建集群日志收集规则 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DeleteCluster 	| 删除集群 	| [DeleteCluster](https://cloud.tencent.com/document/product/457/36704) 	|
| DeleteClusterInstances 	| 删除集群节点 	| [DeleteClusterInstances](https://cloud.tencent.com/document/product/457/31864) 	|
| DeleteClusterRoute 	| 删除集群路由 	| [DeleteClusterRoute](https://cloud.tencent.com/document/product/457/37184) 	|
| DeleteClusterRouteTable 	| 删除集群路由表 	|  DeleteClusterRouteTables 	|
| DeleteInstances 	| 删除实例 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DescribeClusterApiServerEndpoint 	| 获取集群访问地址 	| [DescribeClusterSecurity](https://cloud.tencent.com/document/product/457/36703) 	|
| DescribeClusterAsg 	| 查询集群伸缩组 	| [DescribeClusterAsGroups](https://cloud.tencent.com/document/product/457/40471) 	|
| DescribeClusterContainer 	| 获取集群容器列表 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DescribeClusterInstances 	| 获取集群节点列表 	| [DescribeClusterInstances](https://cloud.tencent.com/document/product/457/31863) 	|
| DescribeClusterNameSpaces 	| 查询集群的命名空间 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DescribeClusterRequestLimitInfo 	| 查询集群 Request 和 Limit 信息 	|  下线  	|
| DescribeClusterRoute 	| 查询集群路由 	| [DescribeClusterRoutes](https://cloud.tencent.com/document/product/457/37181) 	|
| DescribeClusterRouteTable 	| 查询集群路由表 	| [DescribeClusterRouteTables](https://cloud.tencent.com/document/product/457/37182) 	|
| DescribeClusterSecurityInfo 	| 获取集群外网访问凭据 	| [DescribeClusterSecurity](https://cloud.tencent.com/document/product/457/36703) 	|
| DescribeClusterService 	| 获取服务列表 	| DescribeClusterServices（后期下线） 	|
| DescribeClusterServiceInfo 	| 获取服务详情 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DescribeIngress 	| 查询ingress列表 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DescribeInstanceLog 	| 获取容器日志 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DescribeServiceEvent 	| 服务事件列表 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DescribeServiceInstance 	| 服务实例列表 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| DisableClusterAsg 	| 停用集群伸缩组 	| [ModifyClusterAsGroupAttribute](https://cloud.tencent.com/document/product/457/40470) 	|
| EnableClusterAsg 	| 启用集群伸缩组 	| [ModifyClusterAsGroupAttribute](https://cloud.tencent.com/document/product/457/40470) 	|
| GetLogDaemonStatus 	| 获取集群日志启用状态 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| GetMasterVip 	| 查询 LB 任务状态 	| [DescribeClusterEndpointStatus](https://cloud.tencent.com/document/product/457/39409) <br>  [DescribeClusterEndpointVipStatus](https://cloud.tencent.com/document/product/457/39410) 	|
| ListLogCollector 	| 列出日志收集规则 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| ModifyClusterService 	| 修改服务 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| ModifyClusterServiceImage 	| 更新服务镜像 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| ModifyServiceReplicas 	| 修改服务实例副本数 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| MosifyIngress 	| 修改 Ingress 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| RedeployClusterService 	| 服务重新部署 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|
| RollBackClusterService 	| 回滚服务到上一个版本 	| 原 API 2.0 接口已下线，建议通过 [kubernetes api](https://github.com/kubernetes/client-go) 直接调用 	|


如您有任何问题，可以咨询 [在线客服](https://cloud.tencent.com/act/event/Online_service) 或 [提交工单](https://console.cloud.tencent.com/workorder/category) 与我们联系。另外，您也可以拨打 4009100100 联系我们的客服人员。




