## 1. 实例相关接口
| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 查看实例列表| [CdbTdsqlGetInstanceList](/doc/api/309/5447) | 查看实例列表以及详情 |
| 修改实例名称 | [CdbTdsqlRenameInstance](/doc/api/309/5449) | 修改实例名称 |
| 实例扩容| [CdbTdsqlExpandInstance](/doc/api/309/5533) | 实例扩容|
| 修改实例所属项目 | [ CdbTdsqlAssignToProject](/doc/api/309/5534) | 修改实例所属项目|
| 开放外网地址 | [CdbTdsqlOpenWanIP](/doc/api/309/5535) | 开放外网地址 |
| 关闭外网地址 | [CdbTdsqlCloseWanIP](/doc/api/309/5536) | 关闭外网地址 |
| 查询实例规格 | [CdbTdsqlGetSpecList](/doc/api/309/5537) | 查询实例规格 |
| 查询价格 |[CdbTdsqlGetPrice](/doc/api/309/5538)| 查询价格 |
| 创建实例 |[CdbTdsqlCreateInstance](/doc/api/309/5539)| 创建实例（包年包月） |
| 初始化实例 |[CdbTdsqlInitInstance](/doc/api/309/5540)| 初始化实例 |
| 续费实例 |[CdbTdsqlRenewInstance](/doc/api/309/5541)| 续费实例 |
| 查询项目列表 |[CdbTdsqlGetProjectList](/doc/api/309/5604)| 查询项目列表 |
| 查询流程状态 |[CdbTdsqlGetFlowInfo](/doc/api/309/5605)| 查询流程状态 |
| 查询订单信息 |[CdbTdsqlGetOrderInfo](/doc/api/309/5690)| 查询订单信息 |
| 获取自定义备份时间 |[CdbTdsqlGetBackupTime](/doc/api/309/5970)| 获取自定义备份时间 |
| 设置自定义备份时间 |[CdbTdsqlSetBackupTime](/doc/api/309/5969)| 设置自定义备份时间 |

## 2. 帐号相关接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 创建帐号| [CdbTdsqlAddUser](/doc/api/309/5394) | 创建云数据库帐号 |
| 查看帐号列表 | [CdbTdsqlGetUserList](/doc/api/309/5395) | 获取实例的帐号列表 |
| 删除帐号| [CdbTdsqlDeleteUser](/doc/api/309/5396) | 删除实例帐号|
| 设置权限 | [ CdbTdsqlSetRight](/doc/api/309/5397) | 设置帐号访问数据库对象的权限|
| 获取权限列表 | [CdbTdsqlGetRightList](/doc/api/309/5398) | 获取帐号的权限列表 |
| 复制权限 | [CdbTdsqlCopyRight](/doc/api/309/5399) | 复制帐号的权限给另一个帐号 |
| 修改帐号备注 | [CdbTdsqlChangeUserDesc](/doc/api/309/5400) | 修改帐号的备注描述 |
| 重置帐号密码 |[CdbTdsqlResetCdbInstancesPassword](/doc/api/309/5401)| 重置数据库帐号的密码 |

## 3. 备份与恢复相关接口
| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 获取日志列表 |[CdbTdsqlGetLog](/doc/api/309/5402)| 获取全量冷备、binlog、errlog的日志列表和下载地址 |

## 4. 参数管理接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 查看数据库参数 |[CdbTdsqlGetConfigList](/doc/api/309/5403)| 查看当前数据库参数 |
| 修改数据库参数 | [CdbTdsqlModifyConfig](/doc/api/309/5405) | 修改数据库参数 |
| 查看备份日志设置 | [CdbTdsqlQueryLogConfig](/doc/api/309/5406) | 查看备份日志设置，目前只提供保存天数的信息 |
| 修改备份日志设置 | [CdbTdsqlModifyLogConfig](/doc/api/309/5407) | 修改备份日志设置，目前只提供保存天数修改的功能 |

## 5. 监控管理接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 查看实例资源使用情况 | [CdbTdsqlGetResourceUsageInfo](/doc/api/309/5408) | 查看实例资源使用情况，如磁盘可用空间，CPU利用率等|
| 查看实例性能数据 |[CdbTdsqlGetPerformanceInfo](/doc/api/309/5409)| 查看实例性能数据,如活跃连接数，磁盘每秒IO次数 |
| 查看实例资源使用详情 |[CdbTdsqlGetResourceUsageInfoDetail](/doc/api/309/5968)| 查看实例资源使用详情 |
| 查看实例性能数据详情 |[CdbTdsqlGetPerformanceInfoDetail](/doc/api/309/5967)| 查看实例性能数据详情 |
| 获取慢查询记录详情 |[CdbTdsqlGetSlowLogAnalysis](/doc/api/309/5972)| 获取慢查询记录详情 |
| 查询慢查询日志列表 |[CdbTdsqlGetSlowLogList](/doc/api/309/5973)| 查询慢查询日志列表 |
