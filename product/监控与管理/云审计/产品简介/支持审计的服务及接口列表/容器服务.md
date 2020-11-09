腾讯云容器服务（Tencent Kubernetes Engine，TKE）基于原生 kubernetes 提供以容器为核心的、高度可扩展的高性能容器管理服务。腾讯云容器服务完全兼容原生 kubernetes API ，扩展了腾讯云的云硬盘、负载均衡等 kubernetes 插件，为容器化的应用提供高效部署、资源调度、服务发现和动态伸缩等一系列完整功能，解决用户开发、测试及运维过程的环境一致性问题，提高了大规模容器集群管理的便捷性，帮助用户降低成本，提高效率。容器服务提供免费使用，涉及的其他云产品另外单独计费。

下表为云审计支持的容器服务操作列表：

| 操作名称                   | 资源类型 | 事件名称                                |
|------------------------|------|-------------------------------------|
| 添加已有节点                 | tke  | AddExistedInstances                 |
| 取消安装应用                 | tke  | CancelClusterRelease                |
| 开启集群访问端口               | tke  | CreateClusterEndpoint               |
| 开启集群访问端口\(托管集群外网\)     | tke  | CreateClusterEndpointVip            |
| 添加\(新增\)集群节点           | tke  | CreateClusterInstances              |
| 集群创建应用                 | tke  | CreateClusterRelease                |
| 删除集群                   | tke  | DeleteCluster                       |
| 删除集群伸缩组                | tke  | DeleteClusterAsGroups               |
| 删除集群访问端口               | tke  | DeleteClusterEndpoint               |
| 删除集群访问端口\(托管集群外网\)     | tke  | DeleteClusterEndpointVip            |
| 删除集群节点                 | tke  | DeleteClusterInstances              |
| 集群伸缩组属性                | tke  | DescribeClusterAsGroupOption        |
| 集群伸缩组列表                | tke  | DescribeClusterAsGroups             |
| 查询集群访问端口状态             | tke  | DescribeClusterEndpointStatus       |
| 查询集群开启访问端口状态\(托管集群外网\) | tke  | DescribeClusterEndpointVipStatus    |
| 查询集群节点                 | tke  | DescribeClusterInstances            |
| 查询正在安装中的应用             | tke  | DescribeClusterPendingReleases      |
| 查询集群应用详情               | tke  | DescribeClusterReleaseDetails       |
| 查询集群中已安装应用             | tke  | DescribeClusterReleases             |
| 查询集群密钥                 | tke  | DescribeClusterSecurity             |
| 驱逐节点                   | tke  | DrainClusterNode                    |
| 修改集群伸缩组属性              | tke  | ModifyClusterAsGroupAttribute       |
| 修改集群伸缩属性               | tke  | ModifyClusterAsGroupOptionAttribute |
| 修改集群属性                 | tke  | ModifyClusterAttribute              |
| 修改集群端口安全组\(托管集群外网\)    | tke  | ModifyClusterEndpointSP             |
| 删除已安装应用                | tke  | UninstallClusterRelease             |
| 升级集群的授权模式              | tke  | UpgradeClusterAuthorizationMode     |
| 升级应用                   | tke  | UpgradeClusterRelease               |
| 批量删除镜像仓库             | ccr | BatchDeleteRepository              |
| 批量删除镜像 Tag           | ccr | BatchDeleteTag                     |
| 创建镜像仓库命名空间           | ccr | CreateCCRNamespace                 |
| 创建镜像仓库               | ccr | CreateRepository                   |
| 扩展节点                 | ccs | AddClusterInstances                |
| 添加已有节点               | ccs | AddClusterInstancesFromExistedCvm  |
| 检查集群路由表是否冲突          | ccs | CheckClusterRouteTableCidrConflict |
| 创建集群                 | ccs | CreateCluster                      |
| 创建集群命名空间             | ccs | CreateClusterNamespace             |
| 创建集群路由               | ccs | CreateClusterRoute                 |
| 创建集群路由表              | ccs | CreateClusterRouteTable            |
| 创建服务                 | ccs | CreateClusterService               |
| 创建负载均衡               | ccs | CreateIngress                      |
| 创建日志收集器              | ccs | CreateLogCollector                 |
| 删除集群                 | ccs | DeleteCluster                      |
| 删除集群命名空间             | ccs | DeleteClusterNamespace             |
| 删除集群路由               | ccs | DeleteClusterRoute                 |
| 删除集群路由表              | ccs | DeleteClusterRouteTable            |
| 删除服务                 | ccs | DeleteClusterService               |
| 删除实例                 | ccs | DeleteInstances                    |
| 删除日志收集器              | ccs | DeleteLogCollector                 |
| 拉取集群列表               | ccs | DescribeCluster                    |
| 拉取集群容器列表             | ccs | DescribeClusterContainer           |
| 拉取主机列表               | ccs | DescribeClusterInstances           |
| 拉取命名空间列表             | ccs | DescribeClusterNamespaces          |
| 拉取集群request、limit 信息 | ccs | DescribeClusterRequestLimitInfo    |
| 查询集群路由               | ccs | DescribeClusterRoute               |
| 查询集群路由表              | ccs | DescribeClusterRouteTable          |
| 拉取服务列表               | ccs | DescribeClusterService             |
| 拉取服务详细信息             | ccs | DescribeClusterServiceInfo         |
| 拉取7层负载均衡列表           | ccs | DescribeIngress                    |
| 获取容器日志               | ccs | DescribeInstanceLog                |
| 拉取服务事件列表             | ccs | DescribeServiceEvent               |
| 拉取实例列表               | ccs | DescribeServiceInstance            |
| 启用集群日志服务             | ccs | EnableLogDaemon                    |
| 获取日志收集器              | ccs | GetLogCollector                    |
| 获取集群日志收集服务开启状态       | ccs | GetLogDaemonStatus                 |
| 列出日志收集器              | ccs | ListLogCollector                   |
| 设置集群节点为是否可调度         | ccs | ModifyClusterNodeSchedulable       |
| 修改服务                 | ccs | ModifyClusterService               |
| 修改集群服务镜像             | ccs | ModifyClusterServiceImage          |
| 更新实例数量               | ccs | ModifyServiceReplicas              |
| 修改负载均衡               | ccs | MosifyIngress                      |
| 服务重新部署               | ccs | RedeployClusterService             |
| 回滚服务                 | ccs | RollbackClusterService             |


