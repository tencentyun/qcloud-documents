分布式 HTAP 数据库 TBase（TencentDB for TBase，TBase）是腾讯自主研发的分布式数据库系统。TBase 集高扩展性、高 SQL 兼容度、完整的分布式事务支持、多级容灾能力及多维度资源隔离等能力于一身，采用无共享的集群架构，提供容灾、备份、恢复、监控、安全、审计等全套解决方案，适用于GB级 - PB级的海量 HTAP 场景。

下表为云审计支持的分布式 HTAP 数据库操作列表：

| 操作名称          | 资源类型  | 事件名称                            |
|---------------|-------|---------------------------------|
| 创建云数据库实例（预付费） | tbase | CreateInstance                  |
| 查询云数据库实例账号    | tbase | DescribeAccounts                |
| 查询可选的字符集      | tbase | DescribeAvailableCharset        |
| 查询支持的引擎版本     | tbase | DescribeAvailableEngineVersions |
| 查询云数据库可售卖规格   | tbase | DescribeAvailableZoneConfig     |
| 查询云数据库实例备份详情  | tbase | DescribeBackupDetails           |
| 查询云数据库实例备份列表  | tbase | DescribeBackupLists             |
| 查询云数据库实例备份规则  | tbase | DescribeBackupRules             |
| 查询实例配置变更记录    | tbase | DescribeDBConfigHistory         |
| 查询实例数据库名列表    | tbase | DescribeDbNameList              |
| 查询实例参数配置      | tbase | DescribeDBParameters            |
| 查询实例安全组信息     | tbase | DescribeDBSecurityGroups        |
| 查询实例错误日志      | tbase | DescribeErrorLog                |
| 查询实例详细信息      | tbase | DescribeInstanceDetails         |
| 查询实例列表        | tbase | DescribeInstances               |
| 查询任务状态        | tbase | DescribeInstanceTaskStatus      |
| 查询实例慢日志       | tbase | DescribeSlowLog                 |
| 修改云数据库安全组     | tbase | ModifyDBInstanceSecurityGroups  |
| 修改实例参数配置      | tbase | ModifyDBParameters              |
| 修改云数据库实例名称    | tbase | ModifyInstanceName              |
| 重置云数据库账号密码    | tbase | ResetAccountPassword            |
| 重启云数据库实例      | tbase | RestartInstance                 |
| 设置云数据库实例备份规则  | tbase | SetBackupRules                  |



