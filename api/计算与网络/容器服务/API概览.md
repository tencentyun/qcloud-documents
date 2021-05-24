>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>

##  集群相关接口

| 接口功能                       | Action ID                                                    | 功能描述                                       |
| ------------------------------ | ------------------------------------------------------------ | ---------------------------------------------- |
| 创建集群                       | [CreateCluster ](https://cloud.tencent.com/document/product/457/9444) | 用于创建集群                                   |
| 创建空集群                     | [CreateEmptyCluster ](https://cloud.tencent.com/document/product/457/18259) | 用于创建空集群                                 |
| 校验 CIDR                      | [ CheckClusterCIDR ](https://cloud.tencent.com/document/product/457/18159) | 用于校验指定 CIDR 创建集群是否冲突             |
| 扩展集群节点                   | [AddClusterInstances](https://cloud.tencent.com/doc/api/457/9447) | 用于集群扩展节点                               |
| 添加已存在云服务器到集群       | [AddClusterInstancesFromExistedCvm](https://cloud.tencent.com/doc/api/457/9450) | 用于添加已存在的云服务器到集群                 |
| 查询加入集群的主机列表         | [DescribeExistedCvmForAddClusterInstances](https://cloud.tencent.com/document/product/457/18321) | 用于查询加入集群的主机列表                     |
| 查询集群列表                   | [DescribeCluster](https://cloud.tencent.com/doc/api/457/9448) | 用于查询集群列表                               |
| 查询集群节点列表               | [DescribeClusterInstances](https://cloud.tencent.com/doc/api/457/9449) | 用于查询集群节点，该接口返回集群内节点信息     |
| 查询集群 Request 和 Limit 信息 | [ DescribeClusterRequestLimitInfo ](https://cloud.tencent.com/document/product/457/18333) | 用于查询集群 CPU、内存的 Request 和 Limit 信息 |
| 获取集群外网访问凭据           | [DescribeClusterSecurityInfo](https://cloud.tencent.com/document/product/457/17560) | 用于获取集群外网访问凭据                       |
| 修改节点 Label                 | [ModifyClusterNodeLabel](https://cloud.tencent.com/document/product/457/13999) | 用于修改节点 Label                             |
| 修改集群属性                   | [ModifyClusterAttributes](https://cloud.tencent.com/document/product/457/17558) | 用于修改集群属性                               |
| 驱逐集群节点                   | [DrainClusterNode](https://cloud.tencent.com/document/product/457/18323) | 用于驱逐集群节点                               |
| 设置集群节点为是否可调度       | [ModifyClusterNodeSchedulable](https://cloud.tencent.com/document/product/457/18322) | 用于设置集群节点为是否可调度                   |
| 添加第三方私有镜像仓库         | [AddHubInfo](https://cloud.tencent.com/document/product/457/17559) | 用于添加第三方私有镜像仓库                     |
| 删除集群节点                   | [DeleteClusterInstances](https://cloud.tencent.com/doc/api/457/9446) | 用于删除集群节点                               |
| 删除集群                       | [DeleteCluster](https://cloud.tencent.com/doc/api/457/9445)  | 用于删除集群                                   |

## 集群自动扩缩容相关接口

| 接口功能                           | Action ID                                                    | 功能描述                                   |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------ |
| 创建集群伸缩组                     | [CreateClusterAsg](https://cloud.tencent.com/document/product/457/15491) | 用于新建集群伸缩组                         |
| 启用集群伸缩组                     | [nableClusterAsg](https://cloud.tencent.com/document/product/457/15494) | 用于启用已停用的集群伸缩组                 |
| 查询集群伸缩组列表                 | [DescribeClusterAsg](https://cloud.tencent.com/document/product/457/15495) | 用于查询集群伸缩组信息                     |
| 修改集群伸缩组是否启用缩容         | [ModifyClusterAsgScaleDown](https://cloud.tencent.com/document/product/457/15488) | 用于修改集群伸缩组是否启用缩容             |
| 修改集群伸缩组的最大最小值及 label | [ModifyClusterAsgRange](https://cloud.tencent.com/document/product/457/15489) | 用于修改集群伸缩组的最大值、最小值和 label |
| 修改集群伸缩组 label               | [ModifyClusterAsgLabel](https://cloud.tencent.com/document/product/457/15487) | 用于修改集群伸缩组 label                   |
| 重置集群伸缩组 label               | [ResetClusterAsgLabel](https://cloud.tencent.com/document/product/457/15496) | 用于重置集群伸缩组 label                   |
| 停用集群伸缩组                     | [DisableClusterAsg](https://cloud.tencent.com/document/product/457/15490) | 用于停用已启用的集群伸缩组                 |
| 删除集群伸缩组 label               | [DeleteClusterAsgLabel](https://cloud.tencent.com/document/product/457/15493) | 用于删除集群伸缩组 label                   |
| 删除集群伸缩组                     | [DeleteClusterAsg](https://cloud.tencent.com/document/product/457/15492) | 用于删除集群伸缩组                         |

## 服务相关接口

| 接口功能                    | Action ID                                                    | 功能描述                                               |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| 创建服务                    | [CreateClusterService](https://cloud.tencent.com/doc/api/457/9436) | 用于创建服务                                           |
| 查询服务列表                | [DescribeClusterService](https://cloud.tencent.com/doc/api/457/9440) | 用于查询服务列表，该接口返回的列表只包含服务的扼要信息 |
| 查询服务详情                | [DescribeClusterServiceInfo](https://cloud.tencent.com/doc/api/457/9441) | 用于查询单个服务详情                                   |
| 获取服务事件列表            | [DescribeServiceEvent](https://cloud.tencent.com/doc/api/457/9443) | 用于查询服务最近一小时的事件列表                       |
| 获取服务的 yaml 文本信息    | [DescribeClusterServiceText](https://cloud.tencent.com/document/product/457/17557) | 用于获取服务的文本信息                                 |
| 修改服务                    | [ModifyClusterService](https://cloud.tencent.com/doc/api/457/9434) | 用于更新服务                                           |
| 修改服务描述                | [ModifyServiceDescription](https://cloud.tencent.com/doc/api/457/9435) | 用于修改服务描述                                       |
| 修改服务镜像                | [ModifyClusterServiceImage](https://cloud.tencent.com/document/product/457/9630) | 用于修改服务的镜像                                   |
| 修改服务的标签（Label）信息 | [ModifyServiceLabels](https://cloud.tencent.com/document/product/457/17556) | 用于修改服务的标签(Label)信息                          |
| 回滚服务                    | [RollBackClusterService](https://cloud.tencent.com/doc/api/457/9438) | 用于回滚服务至升级前的配置，只能回滚至上一个配置       |
| 服务重部署                  | [RedeployClusterService](https://cloud.tencent.com/document/product/457/9685) | 用于将服务实例重新部署                                 |
| 暂停服务更新                | [PauseClusterService](https://cloud.tencent.com/doc/api/457/9439) | 用于暂停升级中的服务                                   |
| 继续服务更新                | [ResumeClusterService](https://cloud.tencent.com/doc/api/457/9442) | 用于继续被暂停中的服务更新                             |
| 删除服务                    | [DeleteClusterService](https://cloud.tencent.com/doc/api/457/9437) | 用于删除服务                                           |

## 服务实例相关接口

| 接口功能           | Action ID                                                    | 功能描述                     |
| ------------------ | ------------------------------------------------------------ | ---------------------------- |
| 查询服务实例列表   | [DescribeServiceInstance](https://cloud.tencent.com/doc/api/457/9433) | 用于查询服务的实例列表       |
| 修改服务实例副本数 | [ModifyServiceReplicas](https://cloud.tencent.com/doc/api/457/9431) | 用于修改服务的容器数量       |
| 获取服务实例日志   | [DescribeInstanceLog](https://cloud.tencent.com/document/product/457/17555) | 用于获取实例容器中的日志信息 |
| 删除服务实例       | [DeleteInstances](https://cloud.tencent.com/doc/api/457/9432) | 用于删除实例                 |

## 命名空间相关接口

| 接口功能         | Action ID                                                    | 功能描述               |
| ---------------- | ------------------------------------------------------------ | ---------------------- |
| 查询集群命名空间 | [DescribeClusterNameSpaces](https://cloud.tencent.com/doc/api/457/9430) | 用于查询集群的命名空间 |
| 创建集群命名空间 | [CreateClusterNamespace](https://cloud.tencent.com/doc/api/457/9428) | 用于创建命名空间       |
| 删除集群命名空间 | [DeleteClusterNamespace](https://cloud.tencent.com/doc/api/457/9429) | 用于删除命名空间       |

## Ingress 相关接口

| 接口功能          | Action ID                                                    | 功能描述              |
| ----------------- | ------------------------------------------------------------ | --------------------- |
| 创建 Ingress      | [CreateIngress](https://cloud.tencent.com/document/product/457/17544) | 用于创建 Ingress      |
| 查询 Ingress 列表 | [ DescribeIngress ](https://cloud.tencent.com/document/product/457/17546) | 用于查询 Ingress 列表 |
| 修改 Ingress      | [ MosifyIngress ](https://cloud.tencent.com/document/product/457/17543) | 用于修改 Ingress 列表 |
| 删除 Ingress      | [ DeleteIngress](https://cloud.tencent.com/document/product/457/17545) | 用于删除 Ingress      |

## 日志相关接口

| 接口功能               | Action ID                                                    | 功能描述                                       |
| ---------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| 启用集群日志收集服务   | [ GetLogDaemonStatus ](https://cloud.tencent.com/document/product/457/17551) | 用于查看某个集群是否已经开启日志服务           |
| 创建集群日志收集规则   | [ CreateLogCollector ](https://cloud.tencent.com/document/product/457/17548) | 用于创建日志收集规则                           |
| 列出日志收集规则       | [ ListLogCollector ](https://cloud.tencent.com/document/product/457/17553) | 用于获取某个集群中所有已经创建的日志收集规则   |
| 更新日志收集规则       | [ UpdateLogCollector ](https://cloud.tencent.com/document/product/457/17550) | 用于更新日志收集规则                           |
| 获取日志收集器信息     | [ GetLogCollector ](https://cloud.tencent.com/document/product/457/17554) | 用于获取已经创建的日志收集规则                 |
| 获取日志收集器状态信息 | [ GetLogDaemonStatus ](https://cloud.tencent.com/document/product/457/18255) | 用于获取集群日志启用状态                       |
| 检查日志收集器名称     | [ CheckIfLogCollectorName ](https://cloud.tencent.com/document/product/457/17552) | 用于查看某个集群是否拥有相同名称的日志收集规则 |
| 删除日志收集规则       | [ DeleteLogCollector ](https://cloud.tencent.com/document/product/457/17549) | 用于删除已经创建的日志收集规则                 |

## 监控相关接口

| 接口功能             | Action ID                                                    | 功能描述                     |
| -------------------- | ------------------------------------------------------------ | ---------------------------- |
| 查询容器服务监控信息 | [ GetMonitorData ](https://cloud.tencent.com/document/product/457/9505) | 用于查询容器服务相关监控信息 |

## 镜像仓库相关接口

| 接口功能                  | Action ID                                                    | 功能描述                                                   |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| 创建镜像仓库              | [CreateRepository](https://cloud.tencent.com/document/product/457/14646) | 用于创建镜像仓库                                           |
| 批量删除仓库              | [BatchDeleteRepository](https://cloud.tencent.com/document/product/457/14650) | 用于批量删除仓库                                           |
| 查询镜像仓库信息          | [GetRepositoryInfo](https://cloud.tencent.com/document/product/457/14656) | 用于查询镜像仓库信息                                       |
| 镜像仓库是否存在          | [RepositoryisExists](https://cloud.tencent.com/document/product/457/14662) | 用于检查镜像仓库是否存在                                   |
| 查询 Tencent Hub 仓库列表 | [GetRepositoryList](https://cloud.tencent.com/document/product/457/17939) | 用于查询 TencentHub 公共仓库列表（包括官方的和用户公开的） |
| 更改镜像仓库描述内容      | [UpdateRepositoryDesc](https://cloud.tencent.com/document/product/457/14651) | 用于更改镜像仓库描述内容                                   |
| 更改镜像仓库访问属性      | [UpdateRepositoryPublic](https://cloud.tencent.com/document/product/457/14652) | 用于更改镜像仓库访问属性                                   |
| 获取 tag 列表             | [GetTagList](https://cloud.tencent.com/document/product/457/14658) | 用于获取镜像 tag 列表                                      |
| 批量删除 tag              | [BatchDeleteTag](https://cloud.tencent.com/document/product/457/14649) | 用于批量删除 tag                                           |
| 复制镜像版本              | [DuplicateImage](https://cloud.tencent.com/document/product/457/14648) | 用于复制镜像版本                                           |
| 设置仓库 tag 超额保留策略 | [SetAutoDelStrategy](https://cloud.tencent.com/document/product/457/14661) | 用于设置仓库 tag 超额保留策略                              |
| 获取仓库 tag 超额保留策略 | [GetAutoDelStrategy](https://cloud.tencent.com/document/product/457/14659) | 用于获取仓库 tag 超额保留策略                              |
| 关闭仓库 tag 超额保留策略 | [CloseAutoDelStrategy](https://cloud.tencent.com/document/product/457/14645) | 用于关闭仓库 tag 超额保留策略                              |
| 添加触发器                | [ AddUpdateServiceTrigger ](https://cloud.tencent.com/document/product/457/14657) | 用于添加触发器                                             |
| 获取触发器                | [  ListTrigger ](https://cloud.tencent.com/document/product/457/14660) | 用于获取触发器                                             |
| 删除触发器                | [ DeleteUpdateServiceTrigger ](https://cloud.tencent.com/document/product/457/14647) | 用于删除触发器                                             |
| 修改服务更新触发器        | [ ModifyUpdateServiceTrigger ](https://cloud.tencent.com/document/product/457/14644) | 用于修改服务更新触发器                                     |
| 修改密码                  | [ ChangePassword ](https://cloud.tencent.com/document/product/457/14643) | 用于修改镜像仓库密码                                       |
| 查询用户配额              | [ GetLimit ](https://cloud.tencent.com/document/product/457/14654) | 用于查询用户配额                                           |
| 查询用户仓库列表          | [ SearchUserRepository ](https://cloud.tencent.com/document/product/457/14653) | 用于查询用户仓库列表                                       |
| 添加收藏                  | [ AddFavor ](https://cloud.tencent.com/document/product/457/17938) | 用于把仓库加入收藏                                         |
| 取消收藏                  | [ DeleteFavor ](https://cloud.tencent.com/document/product/457/17937) | 用于取消收藏                                          |
