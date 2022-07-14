云数据库 MongoDB（TencentDB for MongoDB）是腾讯云基于开源非关系型数据库 MongoDB 专业打造的高性能分布式数据存储服务，完全兼容 MongoDB 协议，适用于面向非关系型数据库的场景。

下表为云审计支持的云数据库 MongoDB 操作列表：

| 操作名称          | 资源类型    | 事件名称                        |
|---------------|---------|-----------------------------|
| 分配项目          | mongodb | AssignProject               |
| 手动备份实例        | mongodb | BackupDBInstance            |
| 创建用户          | mongodb | CreateAccountUser           |
| 创建实例          | mongodb | CreateDBInstance            |
| 创建按量计费实例      | mongodb | CreateDBInstanceHour        |
| 删除账号          | mongodb | DeleteAccountUser           |
| 查询用户          | mongodb | DescribeAccountUsers        |
| 获取备份下载授权      | mongodb | DescribeBackupAccess        |
| 查询备份规则        | mongodb | DescribeBackupRules         |
| 拉取实例列表        | mongodb | DescribeDBInstances         |
| 查询实例回档列表      | mongodb | DescribeInstanceCollections |
| 查询 oplog 信息     | mongodb | DescribeOplogInfo           |
| 查询只读实例主从时延    | mongodb | DescribeReadonlyDelay       |
| 隔离云数据库实例      | mongodb | IsolateDBInstance           |
| 调整云数据库实例配置    | mongodb | ModifyDBInstanceSpec        |
| 下线隔离状态的云数据库实例 | mongodb | OfflineIsolatedDBInstance   |
| 删除临时实例        | mongodb | RemoveCloneInstance         |
| 重命名实例         | mongodb | RenameInstance              |
| 续费实例          | mongodb | RenewInstance               |
| 调整实例 oplog 大小   | mongodb | ResizeOplog                 |
| 实例重启          | mongodb | RestartInstance             |
| 回档数据库实例       | mongodb | RestoreDBInstance           |
| 设置用户权限        | mongodb | SetAccountUserPrivilege     |
| 设置自动续费        | mongodb | SetAutoRenew                |
| 设置自动备份规则      | mongodb | SetBackupRules              |
| 临时实例转正        | mongodb | SetInstanceFormal           |
| 设置实例维护时间窗     | mongodb | SetInstanceMaintenance      |
| 设置密码          | mongodb | SetPassword                 |
| 设置只读实例为正式实例   | mongodb | SetReadonlyToNormal         |
| 销毁按量计费实例      | mongodb | TerminateDBInstance         |
| 实例升级          | mongodb | UpgradeDBInstance           |


