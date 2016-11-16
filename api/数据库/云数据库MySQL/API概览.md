## 1. 实例相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [创建实例（包年包月）](/doc/api/253/1334)| CreateCdb | 创建云数据库实例，计费模式为包年包月 |
| [查询价格（包年包月）](/doc/api/253/1332)| InquiryCdbPrice | 查询某个云数据库实例规格包年包月的价格 |
| [创建实例（按量计费）](/doc/api/253/5175)| CreateCdbHour | 创建云数据库实例，计费模式为按量计费 |
| [查询价格（按量计费）](/doc/api/253/5176)| InquiryCdbPriceHour | 查询某个云数据库实例规格按量计费的价格 |
| [查询可创建规格（支持可用区、配置自定义）](/doc/api/253/6109)| DescribeCdbProductListNew | 查询可创建的云数据库实例规格，支持按可用区和自定义规格创建实例。<font style="color:red">推荐使用</font> |
| [查询可创建规格](/doc/api/253/1333)  | DescribeCdbProductList| 查询可创建的云数据库实例规格 |
| [查询实例列表](/doc/api/253/1266) | DescribeCdbInstances | 查询云数据库实例列表。可根据云数据库实例ID、访问地址和状态等作过滤条件来查询实例列表。|
| [查询只读实例列表](/doc/api/253/6417) | GetCdbReadOnlyInstances | 查询只读实例列表，支持通过传入一个或多个主实例ID查询主实例关联的只读实例列表 |
| [初始化实例](/doc/api/253/5335) | CdbMysqlInit | 初始化云数据库实例，初始化时可同时设置实例的字符集、端口、root账号密码、表名大小写敏感。 |
| [查询初始化任务详情](/doc/api/253/5334) | GetCdbInitInfo | 通过初始化任务ID查询初始化云数据库实例异步任务进度详情 |
| [修改名称](/doc/api/253/1270) | ModifyCdbInstanceName | 修改云数据库实例名称 |
| [重置密码](/doc/api/253/1271) | ResetCdbInstancesPassword | 重置云数据库实例root帐号的密码 |
| [续费实例](/doc/api/253/1331) | RenewCdb | 续费云数据库实例 |
| [销毁实例（按量计费）](/doc/api/253/6415) | CloseCdbHour | 按量计费模式的实例支持实时销毁实例 |
| [恢复实例（按量计费）](/doc/api/253/6416) | OpenCdbHour | 按量计费模式的实例如果已被销毁，可通过此接口实时恢复 |
| [设置自动续费](/doc/api/253/4112) | SetCdbAutoRenew| 设置云数据库实例为自动续费 |
| [修改字符集](/doc/api/253/4113) | ModifyCdbCharset | 修改云数据库实例字符集 |
| [修改端口](/doc/api/253/6543) | ModifyCdbInstanceVport | 修改云数据库实例端口，端口支持范围：1024-65535 |
| [查询参数列表](/doc/api/253/6369) | GetCdbParams | 使用实例ID查询数据库参数列表 |
| [修改参数](/doc/api/253/6368) | ModifyCdbParams | 修改数据库参数，提交成功后返回修改参数的任务ID |
| [查询修改参数任务详情](/doc/api/253/6428) | GetCdbModifyParamsJobTask | 通过修改参数的任务ID查询修改参数任务详情 |
| [查询参数修改记录](/doc/api/253/6367) | GetCdbParamsModifyHistory | 查询数据库参数修改记录 |
| [查询参数模板列表](/doc/api/253/6549) | GetCdbParamTemplateList | 查询数据库参数模板列表 |
| [查询默认参数模板详情](/doc/api/253/6544) | GetCdbDefaultParamInfo | 查询默认数据库参数模板详情 |
| [新增参数模板](/doc/api/253/6548) | AddCdbParamTemplate | 新增数据库参数模板 |
| [删除参数模板](/doc/api/253/6547) | DelCdbParamTemplate | 删除数据库参数模板 |
| [修改参数模板](/doc/api/253/6546) | ModifyCdbParamTemplate | 修改数据库参数模板内容 |
| [查询参数模板详情](/doc/api/253/6545) | GetCdbParamTemplateInfo | 查询云数据库参数模板详情 |
| [查询回档任务详情](/doc/api/253/4114) | GetCdbRollbackJobTask | 查询云数据库实例回档的任务详情 |
| [查询回档任务列表](/doc/api/253/4115) | GetCdbRollbackJob | 查询云数据库实例回档任务列表 |
| [查询私有网络子网实例数量](/doc/api/253/5440)  | GetCdbInstanceNumByVpcSubnetId| 查询私有网络子网下的云数据库实例数量 |


## 2. 监控相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询物理机监控信息](/doc/api/253/4687) | GetCdbDeviceMonitorInfo | 查询物理机的监控信息，<font style='color:red'>暂只支持最高配置实例查询</font> |
| [查询统计信息](/doc/api/253/4688) | QueryCdbStatisticsInfo | 查询云数据库统计信息，查询的是最近一分钟的统计数据 |


## 3. 日志相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询慢查询日志](/doc/api/253/4690) | DescribeCdbSlowQueryLog | 根据云数据库实例ID查询慢查询日志。返回一天的日志信息。|
| [查询备份与日志](/doc/api/253/4691) | GetCdbExportLogUrl | 查询实例冷备数据、二进制日志和慢查询日志 |
| [查询备份数据的库表](/doc/api/253/5105) | GetBackupDatabaseTableList | 查询备份数据的库表 |
| [查询备份地址（支持分库表）](/doc/api/253/5125) | GetExportBackupUrl | 查询备份数据的地址，支持分库表查询 |