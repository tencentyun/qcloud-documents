云数据库 CynosDB 是腾讯云自研的新一代高性能、高可用的企业级云数据库。云原生的数据库架构将传统数据库与云计算的优势相结合，完全兼容 MySQL 和 PostgreSQL，具有更高性价比，更灵活的弹性扩展，更智能的运维管理和更可靠的安全保障。

下表为云审计支持的云数据库 CynosDB 操作列表：

| 操作名称        | 资源类型    | 事件名称                           |
|-------------|---------|--------------------------------|
| 恢复实例访问      | cynosdb | ActivateInstance               |
| 关闭外网        | cynosdb | CloseWan                       |
| 创建集群        | cynosdb | CreateClusters                 |
| 删除账号        | cynosdb | DeleteAccounts                 |
| 查询数据库管理账号   | cynosdb | DescribeAccounts               |
| 查询备份配置信息    | cynosdb | DescribeBackupConfig           |
| 查询备份文件列表    | cynosdb | DescribeBackupList             |
| 查询集群访问地址    | cynosdb | DescribeClusterAddr            |
| 集群详情        | cynosdb | DescribeClusterDetail          |
| 查询实例组       | cynosdb | DescribeClusterInstanceGrps    |
| 查询集群网络信息    | cynosdb | DescribeClusterNetService      |
| 查询集群参数      | cynosdb | DescribeClusterParams          |
| 查询集群列表      | cynosdb | DescribeClusters               |
| 查询集群服务端信息   | cynosdb | DescribeClusterServerInfo      |
| 查询实例安全组信息   | cynosdb | DescribeDBSecurityGroups       |
| 错误日志列表      | cynosdb | DescribeErrorLogs              |
| 查询实例列表      | cynosdb | DescribeInstances              |
| 查询实例维护时间窗   | cynosdb | DescribeMaintainPeriod         |
| 查询有效回滚时间范围  | cynosdb | DescribeRollbackTimeRange      |
| 慢查询日志列表     | cynosdb | DescribeSlowLogs               |
| 隔离集群        | cynosdb | IsolateCluster                 |
| 隔离实例访问      | cynosdb | IsolateInstance                |
| 修改数据库账号描述信息 | cynosdb | ModifyAccountDescription       |
| 修改备份配置      | cynosdb | ModifyBackupConfig             |
| 修改集群名称      | cynosdb | ModifyClusterName              |
| 修改集群参数      | cynosdb | ModifyClusterParam             |
| 修改集群项目 ID    | cynosdb | ModifyClusterProject           |
| 修改云数据库安全组   | cynosdb | ModifyDBInstanceSecurityGroups |
| 修改实例名称      | cynosdb | ModifyInstanceName             |
| 修改维护时间配置    | cynosdb | ModifyMaintainPeriodConfig     |
| 下线实例        | cynosdb | OfflineInstance                |
| 开通外网        | cynosdb | OpenWan                        |
| 重置数据库账号密码   | cynosdb | ResetAccountPassword           |
| 设置自动续费标记    | cynosdb | SetRenewFlag                   |
| 升级实例        | cynosdb | UpgradeInstance                |
