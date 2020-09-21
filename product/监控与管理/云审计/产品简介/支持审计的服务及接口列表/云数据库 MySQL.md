腾讯云数据库 MySQL（TencentDB for MySQL）为用户提供安全可靠，易于维护的数据库服务。MySQL 是世界上最流行的开源关系数据库，通过腾讯云数据库 MySQL，您可实现分钟级别的数据库部署和弹性扩展，不仅经济实惠，而且稳定可靠，易于运维。云数据库 MySQL 提供备份恢复、监控、容灾、快速扩容、数据传输等全套解决方案，为您简化数据库运维工作，使您能更加专注于业务发展。

下表为云审计支持的云数据库 MySQL 操作列表：

| 操作名称               | 资源类型 | 事件名称                           |
|--------------------|------|--------------------------------|
| 为云数据库实例添加维护时间窗     | cdb  | AddTimeWindow                  |
| 批量绑定安全组            | cdb  | AssociateSecurityGroups        |
| 均衡 Ro 组内的负载          | cdb  | BalanceRoGroupLoad             |
| 取消任务               | cdb  | CancelDBInstanceTask           |
| 关闭实例外网访问           | cdb  | CloseWanService                |
| 创建云数据库的账户          | cdb  | CreateAccounts                 |
| 创建云数据库备份           | cdb  | CreateBackup                   |
| 创建数据导入任务           | cdb  | CreateDBImportJob              |
| 创建云数据库实例           | cdb  | CreateDBInstance               |
| 创建云数据库按量计费实例       | cdb  | CreateDBInstanceHour           |
| 监控模板创建监控项          | cdb  | CreateMonitorTemplate          |
| 创建参数模板             | cdb  | CreateParamTemplate            |
| Ro 示例绑定独立 vip        | cdb  | CreateRoInstanceIp             |
| 删除云数据库的账号          | cdb  | DeleteAccounts                 |
| 删除云数据库备份           | cdb  | DeleteBackup                   |
| 监控模板删除监控项          | cdb  | DeleteMonitorTemplate          |
| 删除参数模板             | cdb  | DeleteParamTemplate            |
| 删除与云数据库实例相关的时间窗口   | cdb  | DeleteTimeWindow               |
| 查询云数据库账户的权限信息      | cdb  | DescribeAccountPrivileges      |
| 查询云数据库的所有账号信息      | cdb  | DescribeAccounts               |
| 查询云数据库实例异步任务的执行结果  | cdb  | DescribeAsyncRequestInfo       |
| 查询云数据库备份配置信息       | cdb  | DescribeBackupConfig           |
| 查询备份数据库列表          | cdb  | DescribeBackupDatabases        |
| 查询云数据库实例的备份日志      | cdb  | DescribeBackups                |
| 查询指定数据库的备份数据表列表    | cdb  | DescribeBackupTables           |
| 获取云数据库实例的二进制日志     | cdb  | DescribeBinlogs                |
| 查询云数据库实例的数据库       | cdb  | DescribeDatabases              |
| 批量查询云数据库实例的数据库     | cdb  | DescribeDatabasesForInstances  |
| 查询导入任务操作日志         | cdb  | DescribeDBImportRecords        |
| 查询云数据库实例的字符集       | cdb  | DescribeDBInstanceCharset      |
| 查询云数据库实例的配置        | cdb  | DescribeDBInstanceConfig       |
| 查询云数据库实例的预期重启时间    | cdb  | DescribeDBInstanceRebootTime   |
| 查询实例列表             | cdb  | DescribeDBInstances            |
| 查询云数据库的路由          | cdb  | DescribeDBRoutes               |
| 查询实例安全组信息          | cdb  | DescribeDBSecurityGroups       |
| 获取实例切换记录           | cdb  | DescribeDBSwitchRecords        |
| 查询默认的可设置参数列表       | cdb  | DescribeDefaultParams          |
| 获取云数据库实例的错误解析日志    | cdb  | DescribeErrLogInfo             |
| 查询实例的参数修改历史        | cdb  | DescribeInstanceParamRecords   |
| 查询实例的可设置参数列表       | cdb  | DescribeInstanceParams         |
| 查询监控模板监控项          | cdb  | DescribeMonitorTemplate        |
| 查询参数模板详情           | cdb  | DescribeParamTemplateInfo      |
| 查询参数模板列表           | cdb  | DescribeParamTemplates         |
| 查询项目安全组信息          | cdb  | DescribeProjectSecurityGroups  |
| 查询异步任务的执行结果        | cdb  | DescribeRequestResult          |
| 查询 Ro 组的详细信息         | cdb  | DescribeRoGroupInfo            |
| 查询指定主实例的 Ro 组信息      | cdb  | DescribeRoGroups               |
| 查询可回档的时间           | cdb  | DescribeRollbackRangeTime      |
| 获取只读实例购买的最小规格      | cdb  | DescribeRoMinScale             |
| 获取云数据库实例的慢查询解析日志   | cdb  | DescribeSlowLogInfo            |
| 获取云数据库实例的慢查询日志     | cdb  | DescribeSlowLogs               |
| 查询云数据库实例支持的权限信息    | cdb  | DescribeSupportedPrivileges    |
| 查询数据库表的列           | cdb  | DescribeTableColumns           |
| 查询数据库表             | cdb  | DescribeTables                 |
| 查询云数据库实例的任务列表      | cdb  | DescribeTasks                  |
| 查询与实例相关的时间窗口       | cdb  | DescribeTimeWindow             |
| 文件导入：获取已经上传的文件     | cdb  | DescribeUploadedFiles          |
| 安全组批量解绑            | cdb  | DisassociateSecurityGroups     |
| 初始化云数据库            | cdb  | InitDBInstances                |
| 隔离云数据库实例           | cdb  | IsolateDBInstance              |
| 终止云数据库的执行线程        | cdb  | KillDBProcessByIds             |
| 修改云数据库实例账号的备注信息    | cdb  | ModifyAccountDescription       |
| 修改云数据库实例账号的密码      | cdb  | ModifyAccountPassword          |
| 修改云数据库实例账号的权限      | cdb  | ModifyAccountPrivileges        |
| 修改云数据库实例的自动续费标记    | cdb  | ModifyAutoRenewFlag            |
| 修改云数据库备份配置信息       | cdb  | ModifyBackupConfig             |
| 修改云数据库实例名          | cdb  | ModifyDBInstanceName           |
| 修改云数据库实例的所属项目      | cdb  | ModifyDBInstanceProject        |
| 修改实例绑定的安全组         | cdb  | ModifyDBInstanceSecurityGroups |
| 修改云数据库实例的vip和vport | cdb  | ModifyDBInstanceVipVport       |
| 修改实例参数             | cdb  | ModifyInstanceParam            |
| 修改参数模板             | cdb  | ModifyParamTemplate            |
| 更新 Ro 组的信息           | cdb  | ModifyRoGroupInfo              |
| 修改 Ro 组的 vip 和 vport    | cdb  | ModifyRoGroupVipVport          |
| 更新与实例关联时间窗口        | cdb  | ModifyTimeWindow               |
| 开启数据库实例加密          | cdb  | OpenDBInstanceEncryption       |
| 开启云数据库实例的 GTID      | cdb  | OpenDBInstanceGTID             |
| 开通实例外网访问           | cdb  | OpenWanService                 |
| 解隔离云数据库实例          | cdb  | ReleaseIsolatedDBInstances     |
| 重启云数据库实例           | cdb  | RestartDBInstances             |
| 查看 MySQL 的执行线程       | cdb  | ShowProcessList                |
| 发起批量回档任务           | cdb  | StartBatchRollback             |
| 终止数据导入任务           | cdb  | StopDBImportJob                |
| 云数据库灾备实例切换为主实例     | cdb  | SwitchDrInstanceToMaster       |
| 升级切换 VIP            | cdb  | SwitchForUpgrade               |
| 升级云数据库实例           | cdb  | UpgradeDBInstance              |
| 升级云数据库实例版本         | cdb  | UpgradeDBInstanceEngineVersion |
