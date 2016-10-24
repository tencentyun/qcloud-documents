## 1. 实例相关接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 创建实例（包年包月）| [CreateCdb](/doc/api/253/1334) | 创建包年包月的云数据库实例 |
| 查询价格（包年包月）| [InquiryCdbPrice](/doc/api/253/1332) | 查询某个云数据库实例规格包年包月的价格 |
| 创建实例（按量计费）| [CreateCdbHour](/doc/api/253/5175) | 创建按量计费的云数据库实例 |
| 查询价格（按量计费）| [InquiryCdbPriceHour](/doc/api/253/5176) | 查询某个云数据库实例规格按量计费的价格 |
| 查询可创建规格（支持可用区、配置自定义）| [DescribeCdbProductListNew](/doc/api/253/6109) | 查询可创建的云数据库实例类型 |
| 查询可创建规格 | [DescribeCdbProductList](/doc/api/253/1333) | 查询可创建的云数据库实例类型 |
| 查询实例列表 | [DescribeCdbInstances](/doc/api/253/1266) | 查询云数据库实例列表。可根据云数据库实例ID，名称或者访问地址作过滤条件来查询实例列表。|
| 查询只读实例列表 | [GetCdbReadOnlyInstances](/doc/api/253/6417) | 查询只读实例列表 |
| 初始化实例 | [CdbMysqlInit](/doc/api/253/5335) | 初始化云数据库实例 |
| 查询初始化任务详情 | [GetCdbInitInfo](/doc/api/253/5334) | 查询初始化云数据库实例异步任务详情 |
| 修改名称 | [ModifyCdbInstanceName](/doc/api/253/1270) | 修改云数据库实例名称 |
| 重置密码 | [ResetCdbInstancesPassword](/doc/api/253/1271) | 重置云数据库实例密码 |
| 续费实例 | [RenewCdb](/doc/api/253/1331) | 续费云数据库实例 |
| 恢复实例（按量计费） | [OpenCdbHour](/doc/api/253/6416) | 恢复实例（按量计费） |
| 销毁实例（按量计费） | [CloseCdbHour](/doc/api/253/6415) | 销毁实例（按量计费） |
| 设置自动续费 | [SetCdbAutoRenew](/doc/api/253/4112)| 设置云数据库实例为自动续费 |
| 修改字符集 | [ModifyCdbCharset](/doc/api/253/4113) | 修改云数据库实例字符集 |
| 修改端口 | [ModifyCdbInstanceVport](/doc/api/253/6543) | 修改云数据库实例端口 |
| 查询参数列表 | [GetCdbParams](/doc/api/253/6369) | 查询数据库参数列表 |
| 修改参数 | [ModifyCdbParams](/doc/api/253/6368) | 修改数据库参数 |
| 查询修改参数任务详情 | [GetCdbModifyParamsJobTask](/doc/api/253/6428) | 查询修改参数任务详情 |
| 查询参数修改记录 | [GetCdbParamsModifyHistory](/doc/api/253/6367) | 查询数据库参数修改记录 |
| 查询参数模板列表 | [GetCdbParamTemplateList](/doc/api/253/6549) | 查询数据库参数模板列表 |
| 查询默认参数模板详情 | [GetCdbDefaultParamInfo](/doc/api/253/6544) | 查询默认数据库参数模板详情 |
| 新增参数模板 | [AddCdbParamTemplate](/doc/api/253/6548) | 新增数据库参数模板 |
| 删除参数模板 | [DelCdbParamTemplate](/doc/api/253/6547) | 删除数据库参数模板 |
| 修改参数模板 | [ModifyCdbParamTemplate](/doc/api/253/6546) | 修改数据库参数模板 |
| 查询参数模板详情 | [GetCdbParamTemplateInfo](/doc/api/253/6545) | 查询数据库参数模板详情 |
| 查询回档任务详情 | [GetCdbRollbackJobTask](/doc/api/253/4114) | 查询云数据库实例回档任务详情 |
| 查询回档任务列表 | [GetCdbRollbackJob](/doc/api/253/4115) | 查询云数据库实例回档任务 |
| 查询私有网络子网实例数量 | [GetCdbInstanceNumByVpcSubnetId](/doc/api/253/5440) | 查询私有网络子网下的云数据库实例数量 |


## 3. 监控相关接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 查询物理机监控信息 |[GetCdbDeviceMonitorInfo](/doc/api/253/4687)| 查询物理机监控信息 |
| 查询统计信息 | [QueryCdbStatisticsInfo](/doc/api/253/4688) | 查询云数据库统计信息，查询的是最近一分钟的统计数据 |


## 4. 日志相关接口

| 接口功能 | Action ID | 功能描述 | 
|---------|---------|---------|
| 查询慢查询日志 | [DescribeCdbSlowQueryLog](/doc/api/253/4690) | 根据云数据库实例ID查询慢查询日志。返回一天的日志信息。|
| 查询备份与日志 |[GetCdbExportLogUrl](/doc/api/253/4691)| 查询实例冷备数据、二进制日志和慢查询日志 |
| 查询备份数据的库表 |[GetBackupDatabaseTableList](/doc/api/253/5105)| 查询备份数据的库表 |
| 查询备份地址（支持分库表） |[GetExportBackupUrl](/doc/api/253/5125)| 查询备份数据的地址，支持分库表查询 |