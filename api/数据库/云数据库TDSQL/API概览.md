## 1. 帐号相关接口

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

## 2. 备份与恢复相关接口
| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 获取日志列表 |[CdbTdsqlGetLog](/doc/api/309/5402)| 获取全量冷备、binlog、errlog的日志列表和下载地址 |

## 3. 参数管理接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 查看数据库参数 |[CdbTdsqlGetConfigList](/doc/api/309/5403)| 查看当前数据库参数 |
| 修改数据库参数 | [CdbTdsqlModifyConfig](/doc/api/309/5405) | 修改数据库参数 |
| 查看备份日志设置 | [CdbTdsqlQueryLogConfig](/doc/api/309/5406) | 查看备份日志设置，目前只提供保存天数的信息 |
| 修改备份日志设置 | [CdbTdsqlModifyLogConfig](/doc/api/309/5407) | 修改备份日志设置，目前只提供保存天数修改的功能 |

## 4. 监控管理接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 查看实例资源使用情况 | [CdbTdsqlGetResourceUsageInfo](/doc/api/309/5408) | 查看实例资源使用情况，如磁盘可用空间，CPU利用率等|
| 查看实例性能数据 |[CdbTdsqlGetPerformanceInfo](/doc/api/309/5409)| 查看实例性能数据,如活跃连接数，磁盘每秒IO次数 |