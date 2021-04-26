弹性 MapReduce（EMR）结合云技术和 Hadoop、Hive、Spark、Storm 等社区开源技术，提供安全、低成本、高可靠、可弹性伸缩的云端托管 Hadoop 服务。您可以在数分钟内创建安全可靠的专属 Hadoop 集群，以分析位于集群内数据节点或 COS 上的 PB 级海量数据。

下表为云审计支持的弹性 MapReduce 操作列表：

| 操作名称              | 资源类型 | 事件名称                                 |
|-------------------|------|--------------------------------------|
| 添加自动扩缩容规格         | emr  | AddAutoScaleSpec                     |
| 添加配置组             | emr  | AddConfigGroup                       |
| 添加指标负载扩缩容规则       | emr  | AddMetricScaleStrategy               |
| 增加节点规格配置         | emr  | AddNodeResourceConfig                |
| 校验用户自定义配置参数       | emr  | CheckCustomConfig                    |
| 检查 Hive 元数据库网络连接    | emr  | CheckMetaDBNet                       |
| 创建 EMR 实例           | emr  | CreateInstance                       |
| 删除自动扩缩容规格         | emr  | DeleteAutoScaleSpec                  |
| 删除自动扩缩容规则         | emr  | DeleteAutoScaleStrategy              |
| 删除配置组             | emr  | DeleteConfigGroup                    |
| 删除节点规格配置          | emr  | DeleteNodeResourceConfig             |
| 获取自动扩缩容全局配置       | emr  | DescribeAutoScaleGlobalConf          |
| 获取自动扩缩容元数据        | emr  | DescribeAutoScaleMetaRange           |
| 获取自动扩缩容历史记录       | emr  | DescribeAutoScaleRecords             |
| 获取自动扩缩容规格         | emr  | DescribeAutoScaleSpecs               |
| 获取自动扩缩容规则         | emr  | DescribeAutoScaleStrategies          |
| 获取自动扩缩容白名单        | emr  | DescribeAutoScaleWhiteList           |
| 获取引导脚本            | emr  | DescribeBootScript                   |
| 描述 cbs 加密           | emr  | DescribeCbsEncrypt                   |
| 查询 CDB 价格           | emr  | DescribeCdbPrice                     |
| 查询 EMR 集群的硬件节点信息    | emr  | DescribeClusterNodes                 |
| 描述配置组             | emr  | DescribeConfigGroup                  |
| 查询云服务器规格          | emr  | DescribeCvmSpec                      |
| 集群销毁信息            | emr  | DescribeDestroyInfo                  |
| 获取分散置放群组信息        | emr  | DescribeDisasterRecoverGroup         |
| 获取 Hive 统一元数据库信息    | emr  | DescribeEmrMetaDB                    |
| 查询 EMR 角色           | emr  | DescribeEmrRole                      |
| 查询导出配置            | emr  | DescribeExportConfs                  |
| 查询支持导出配置文件的列表     | emr  | DescribeExportConfsList              |
| 配置页面拉取文件所在IP列表    | emr  | DescribeFileIps                      |
| 查询 EMR 集群流程个数       | emr  | DescribeFlowNum                      |
| 查询 EMR 实例流程状态       | emr  | DescribeFlowStatus                   |
| 查询 EMR 任务运行详情状态     | emr  | DescribeFlowStatusDetail             |
| 获取 Hbase 表级监控数据概览接口 | emr  | DescribeHbaseTableMetricDataOverview |
| 获取安装组件信息          | emr  | DescribeInstallSoftwareInfo          |
| 展示告警信息            | emr  | DescribeInstanceAlerts               |
| 获取别名              | emr  | DescribeInstanceAlias                |
| 获取实例操作日志          | emr  | DescribeInstanceOplog                |
| 查询 EMR 实例           | emr  | DescribeInstances                    |
| 获取不同级别监控的监控维度值    | emr  | DescribeMetricsDimension             |
| 查询变配订单            | emr  | DescribeModifyGoodsDetail            |
| 获取节点规格配置          | emr  | DescribeNodeResourceConfig           |
| 快速获取节点规格配置        | emr  | DescribeNodeResourceConfigFast       |
| 查询备选规格白名单         | emr  | DescribeOptionalSpecWhiteList        |
| 查询续费订单            | emr  | DescribeRenewGoodsDetail             |
| 描述可扩容的服务          | emr  | DescribeScaleoutableService          |
| 查询扩容订单            | emr  | DescribeScaleoutGoodsDetail          |
| 获取 EMR 安全组          | emr  | DescribeSecurityGroup                |
| 查询服务配置            | emr  | DescribeServiceConfs                 |
| 查询服务组信息           | emr  | DescribeServiceGroups                |
| 查询服务进程信息          | emr  | DescribeServiceNodeInfos             |
| 描述 EMR 子任务流程        | emr  | DescribeSubJobFlowStatus             |
| 获取账户余额            | emr  | DescribleAccountBalance              |
| 生成创建集群订单          | emr  | GenerateCreateGoodsDetail            |
| 生成变配订单            | emr  | GenerateModifyGoodsDetail            |
| 生成续费订单            | emr  | GenerateRenewGoodsDetail             |
| 生成扩容订单            | emr  | GenerateScaleoutGoodsDetail          |
| 查询创建 EMR 集群的订单参数    | emr  | GetCreateGoodsDetail                 |
| 创建实例询价            | emr  | InquiryPriceCreateInstance           |
| 续费询价              | emr  | InquiryPriceRenewInstance            |
| 扩容询价              | emr  | InquiryPriceScaleOutInstance         |
| 变配询价              | emr  | InquiryPriceUpdateInstance           |
| 后开启 Cos            | emr  | InstallCos                           |
| 安装组件              | emr  | InstallSoftware                      |
| 获取配置下发日志          | emr  | ListConfLogs                         |
| 更新自动扩缩容全局配置       | emr  | ModifyAutoScaleGlobalConf            |
| 修改自动扩缩容规则         | emr  | ModifyAutoScaleStrategy              |
| 修改引导脚本            | emr  | ModifyBootScript                     |
| 修改配置组             | emr  | ModifyConfigGroup                    |
| 修改集群名称            | emr  | ModifyInstanceBasic                  |
| 变配实例              | emr  | ModifyResource                       |
| 修改服务组件参数          | emr  | ModifyServiceParams                  |
| 修改规则优先级           | emr  | ModifyStrategyPriority               |
| 重启组件服务            | emr  | RestartService                       |
| 回滚配置              | emr  | RollBackConf                         |
| 实例扩容              | emr  | ScaleOutInstance                     |
| 设置节点规格配置默认属性      | emr  | SetNodeResourceConfigDefault         |
| 启动组件监控            | emr  | StartMonitor                         |
| 启动组件服务            | emr  | StartService                         |
| 停止组件监控            | emr  | StopMonitor                          |
| 停止组件服务            | emr  | StopService                          |
| 同步配置检查            | emr  | SynchronizeGroupConfCheck            |
| 销毁所有自动扩缩容节点       | emr  | TerminateAutoScaleNodes              |
| 销毁 EMR 实例           | emr  | TerminateInstance                    |
| 销毁节点              | emr  | TerminateNodes                       |
| 缩容 Task 节点          | emr  | TerminateTasks                       |
| 更新代理组件密码          | emr  | UpdateWebproxyPassword               |
