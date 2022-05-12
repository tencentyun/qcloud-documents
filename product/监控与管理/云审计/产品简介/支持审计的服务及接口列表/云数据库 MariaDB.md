云数据库 MariaDB 是基于 OLTP 场景下高安全性的企业级云数据库，十余年来一直应用于腾讯计费业务，MariaDB 兼容 MySQL 语法，拥有诸如线程池、审计、异地容灾等高级功能，同时具有云数据库的易扩展性、简单性和高性价比。

下表为云审计支持的云数据库 MariaDB 操作列表：

| 操作名称            | 资源类型    | 事件名称                           |
|-----------------|---------|--------------------------------|
| 解隔离后付费实例        | mariadb | ActivateHourDBInstance         |
| 恢复独享实例          | mariadb | ActiveDedicatedDBInstance      |
| 检查 IP 状态          | mariadb | CheckIpStatus                  |
| 克隆账号            | mariadb | CloneAccount                   |
| 关闭外网地址          | mariadb | CloseDBExtranetAccess          |
| 创建帐号            | mariadb | CreateAccount                  |
| 创建参数模板          | mariadb | CreateConfigTemplate           |
| 创建实例            | mariadb | CreateDBInstance               |
| 创建后付费实例         | mariadb | CreateHourDBInstance           |
| 回档实例            | mariadb | CreateTmpInstances             |
| 删除帐号            | mariadb | DeleteAccount                  |
| 删除参数模板          | mariadb | DeleteConfigTemplate           |
| 删除临时实例          | mariadb | DeleteTmpInstance              |
| 获取权限列表          | mariadb | DescribeAccountPrivileges      |
| 查看帐号列表          | mariadb | DescribeAccounts               |
| 查询审计日志          | mariadb | DescribeAuditLogs              |
| 查询审计规则详情        | mariadb | DescribeAuditRuleDetail        |
| 查询审计规则列表        | mariadb | DescribeAuditRules             |
| 查询审计策略          | mariadb | DescribeAuditStrategies        |
| 获取自定义备份时间       | mariadb | DescribeBackupTime             |
| 批量 mariadb 实例续费询价 | mariadb | DescribeBatchRenewalPrice      |
| 查询 binlog 时间      | mariadb | DescribeBinlogTime             |
| 查询参数配置历史        | mariadb | DescribeConfigHistories        |
| 查询参数模板          | mariadb | DescribeConfigTemplate         |
| 查询参数模板列表        | mariadb | DescribeConfigTemplates        |
| 查询实例对象          | mariadb | DescribeDatabaseObjects        |
| 查询实例 db 名         | mariadb | DescribeDatabases              |
| 查询实例表的列信息       | mariadb | DescribeDatabaseTable          |
| 查询监控信息详情        | mariadb | DescribeDBDetailMetrics        |
| 查询实例密钥信息        | mariadb | DescribeDBEncryptAttributes    |
| 查询实例详情          | mariadb | DescribeDBInstanceDetail       |
| 查询实例 ha 信息        | mariadb | DescribeDBInstanceHAInfo       |
| 查看实例列表          | mariadb | DescribeDBInstances            |
| 查询实例规格          | mariadb | DescribeDBInstanceSpecs        |
| 获取日志列表          | mariadb | DescribeDBLogFiles             |
| 查询监控信息          | mariadb | DescribeDBMetrics              |
| 查看数据库参数         | mariadb | DescribeDBParameters           |
| 查看实例性能数据        | mariadb | DescribeDBPerformance          |
| 查看实例性能数据详情      | mariadb | DescribeDBPerformanceDetails   |
| 查看实例资源使用情况      | mariadb | DescribeDBResourceUsage        |
| 查看实例资源使用详情      | mariadb | DescribeDBResourceUsageDetails |
| 查询实例安全组信息       | mariadb | DescribeDBSecurityGroups       |
| 获取慢查询记录详情       | mariadb | DescribeDBSlowLogAnalysis      |
| 查询慢查询日志列表       | mariadb | DescribeDBSlowLogs             |
| 查询实例同步模式        | mariadb | DescribeDBSyncMode             |
| 查询临时实例          | mariadb | DescribeDBTmpInstances         |
| 查询独享集群规格        | mariadb | DescribeFenceDBInstanceSpecs   |
| 查询流程状态          | mariadb | DescribeFlow                   |
| 查询实例 proxy 配置     | mariadb | DescribeInstanceProxyConfig    |
| 查询实例 ssl 状态       | mariadb | DescribeInstanceSSLAttributes  |
| 查询 dba 最新检查结果     | mariadb | DescribeLatestCloudDBAReport   |
| 查看备份日志设置        | mariadb | DescribeLogFileRetentionPeriod |
| 查询订单信息          | mariadb | DescribeOrders                 |
| 查询价格            | mariadb | DescribePrice                  |
| 查询项目            | mariadb | DescribeProjects               |
| 查询项目安全组信息       | mariadb | DescribeProjectSecurityGroups  |
| 查询实例续费价格        | mariadb | DescribeRenewalPrice           |
| 查询售卖可用区         | mariadb | DescribeSaleInfo               |
| 查询同步任务列表        | mariadb | DescribeSyncTasks              |
| 查询实例升级价格        | mariadb | DescribeUpgradePrice           |
| 查询用户任务信息        | mariadb | DescribeUserTasks              |
| 设置权限            | mariadb | GrantAccountPrivileges         |
| 初始化实例           | mariadb | InitDBInstances                |
| 隔离独享实例          | mariadb | IsolateDedicatedDBInstance     |
| 隔离后付费实例         | mariadb | IsolateHourDBInstance          |
| 修改帐号备注          | mariadb | ModifyAccountDescription       |
| 批量设置自动续费        | mariadb | ModifyAutoRenewFlag            |
| 设置自定义备份时间       | mariadb | ModifyBackupTime               |
| 修改参数模板          | mariadb | ModifyConfigTemplate           |
| 修改实例加密信息        | mariadb | ModifyDBEncryptAttributes      |
| 修改实例名称          | mariadb | ModifyDBInstanceName           |
| 修改云数据库安全组       | mariadb | ModifyDBInstanceSecurityGroups |
| 修改实例所属项目        | mariadb | ModifyDBInstancesProject       |
| 修改数据库参数         | mariadb | ModifyDBParameters             |
| 修改实例同步模式        | mariadb | ModifyDBSyncMode               |
| 修改实例网络          | mariadb | ModifyInstanceNetwork          |
| 修改 ssl 信息         | mariadb | ModifyInstanceSSLAttributes    |
| 修改实例 vip         | mariadb | ModifyInstanceVip              |
| 修改实例 VPORT       | mariadb | ModifyInstanceVport            |
| 修改备份日志设置        | mariadb | ModifyLogFileRetentionPeriod   |
| 开放外网地址          | mariadb | OpenDBExtranetAccess           |
| 续费实例            | mariadb | RenewDBInstance                |
| 重置帐号密码          | mariadb | ResetAccountPassword           |
| 启动智能 dba         | mariadb | StartSmartDBA                  |
| 切换实例 ha          | mariadb | SwitchDBInstanceHA             |
| 临时实例替换原实例       | mariadb | SwitchRollbackInstance         |
| 销毁独享实例          | mariadb | TerminateDedicatedDBInstance   |
| 实例扩容            | mariadb | UpgradeDBInstance              |
| 升级独享实例          | mariadb | UpgradeDedicatedDBInstance     |
| 升级后付费实例         | mariadb | UpgradeHourDBInstance          |


