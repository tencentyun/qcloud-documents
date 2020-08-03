分布式数据库 TDSQL 是部署在腾讯云上的一种支持自动水平拆分、Shared Nothing 架构的分布式数据库。分布式数据库即业务获取的是完整的逻辑库表，而后端会将库表均匀地拆分到多个物理分片节点。TDSQL 默认部署主备架构，提供容灾、备份、恢复、监控、迁移等全套解决方案，适用于 TB 或 PB 级的海量数据库场景。

下表为云审计支持的分布式数据库 TDSQL 操作列表：

| 操作名称           | 资源类型 | 事件名称                           |
|----------------|------|--------------------------------|
| 解隔离 DCDB 后付费实例   | dcdb | ActiveHourDCDBInstance         |
| 检查 IP 状态         | dcdb | CheckIpStatus                  |
| 克隆账号           | dcdb | CloneAccount                   |
| 关闭实例外网         | dcdb | CloseDBExtranetAccess          |
| 创建账号           | dcdb | CreateAccount                  |
| 创建实例           | dcdb | CreateDCDBInstance             |
| 创建 DCDB 后付费实例    | dcdb | CreateHourDCDBInstance         |
| 回档 DCDB 实例       | dcdb | CreateTmpDCDBInstance          |
| 删除账号           | dcdb | DeleteAccount                  |
| 删除临时实例         | dcdb | DeleteTmpInstance              |
| 查询账号权限         | dcdb | DescribeAccountPrivileges      |
| 查询账号列表         | dcdb | DescribeAccounts               |
| 查询审计日志         | dcdb | DescribeAuditLogs              |
| 查询审计策略         | dcdb | DescribeAuditStrategies        |
| 批量 DCDB 实例续费询价   | dcdb | DescribeBatchDCDBRenewalPrice  |
| 查询实例对象         | dcdb | DescribeDatabaseObjects        |
| 查询实例 db 名        | dcdb | DescribeDatabases              |
| 查询实例表的列信息      | dcdb | DescribeDatabaseTable          |
| 获取日志列表         | dcdb | DescribeDBLogFiles             |
| 查询监控信息         | dcdb | DescribeDBMetrics              |
| 查看数据库参数        | dcdb | DescribeDBParameters           |
| 查询实例安全组信息      | dcdb | DescribeDBSecurityGroups       |
| 获取慢查询记录详情      | dcdb | DescribeDBSlowLogAnalysis      |
| 查询慢查询日志列表      | dcdb | DescribeDBSlowLogs             |
| 查询实例同步模式       | dcdb | DescribeDBSyncMode             |
| 获取实例回档生成的临时实例  | dcdb | DescribeDBTmpInstances         |
| 获取实例回档时可选的时间范围 | dcdb | DescribeDCDBBinlogTime         |
| 获取 DCDB 实例详情     | dcdb | DescribeDCDBInstanceDetail     |
| 查看实例列表         | dcdb | DescribeDCDBInstances          |
| 查询价格           | dcdb | DescribeDCDBPrice              |
| 查询实例续费价格       | dcdb | DescribeDCDBRenewalPrice       |
| 查询售卖可用区        | dcdb | DescribeDCDBSaleInfo           |
| 查询 DCDB 实例分片     | dcdb | DescribeDCDBShards             |
| 查询实例升级价格       | dcdb | DescribeDCDBUpgradePrice       |
| 查询独享集群规格       | dcdb | DescribeFenceShardSpec         |
| 查询流程状态         | dcdb | DescribeFlow                   |
| 查询 dba 最新检查结果    | dcdb | DescribeLatestCloudDBAReport   |
| 查看备份日志设置       | dcdb | DescribeLogFileRetentionPeriod |
| 查询项目           | dcdb | DescribeProjects               |
| 查询项目安全组信息      | dcdb | DescribeProjectSecurityGroups  |
| 查询实例规格         | dcdb | DescribeShardSpec              |
| 获取 SQL 日志        | dcdb | DescribeSqlLogs                |
| 设置账号权限         | dcdb | GrantAccountPrivileges         |
| 初始化实例          | dcdb | InitDCDBInstances              |
| 隔离独享实例         | dcdb | IsolateDedicatedDBInstance     |
| 隔离 DCDB 后付费实例    | dcdb | IsolateHourDCDBInstance        |
| 修改数据库账号备注      | dcdb | ModifyAccountDescription       |
| 批量设置自动续费       | dcdb | ModifyAutoRenewFlag            |
| 修改实例名称         | dcdb | ModifyDBInstanceName           |
| 修改云数据库安全组      | dcdb | ModifyDBInstanceSecurityGroups |
| 修改实例项目         | dcdb | ModifyDBInstancesProject       |
| 修改数据库参数        | dcdb | ModifyDBParameters             |
| 修改实例同步模式       | dcdb | ModifyDBSyncMode               |
| 修改实例所属网络       | dcdb | ModifyInstanceNetwork          |
| 修改实例备注         | dcdb | ModifyInstanceRemark           |
| 修改实例 vip        | dcdb | ModifyInstanceVip              |
| 修改备份日志设置       | dcdb | ModifyLogFileRetentionPeriod   |
| 开启外网           | dcdb | OpenDBExtranetAccess           |
| 重置账号密码         | dcdb | ResetAccountPassword           |
| 启动智能 dba        | dcdb | StartSmartDBA                  |
| 切换回档实例         | dcdb | SwitchRollbackInstance         |
| 销毁独享实例         | dcdb | TerminateDedicatedDBInstance   |
| 升级独享 DCDB 实例     | dcdb | UpgradeDedicatedDCDBInstance   |
| 升级 DCDB 后付费实例    | dcdb | UpgradeHourDCDBInstance        |
