## 1. 实例相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询实例列表](/document/api/236/1266) | DescribeCdbInstances | 查询云数据库实例列表。可根据云数据库实例ID、访问地址和状态等作过滤条件来查询实例列表。|
| [查询只读实例列表](/document/api/236/6417) | GetCdbReadOnlyInstances | 查询只读实例列表，支持通过传入一个或多个主实例ID查询主实例关联的只读实例列表 |
| [创建实例（按量计费）](/document/api/236/5175)| CreateCdbHour | 创建云数据库实例，计费模式为按量计费 |
| [查询价格（按量计费）](/document/api/236/5176)| InquiryCdbPriceHour | 查询某个云数据库实例规格按量计费的价格 |
| [查询可创建规格（支持可用区、配置自定义）](/document/api/236/6109)| DescribeCdbProductListNew | 查询可创建的云数据库实例规格，支持按可用区和自定义规格创建实例。推荐使用 |
| [查询可创建规格](/document/api/236/1333)  | DescribeCdbProductList| 查询可创建的云数据库实例规格 |
| [初始化实例](/document/api/236/5335) | CdbMysqlInit | 初始化云数据库实例，初始化时可同时设置实例的字符集、端口、root账号密码、表名大小写敏感。 |
| [查询初始化任务详情](/document/api/236/5334) | GetCdbInitInfo | 通过初始化任务ID查询初始化云数据库实例异步任务进度详情 |
| [升级实例](/document/api/236/7164) | UpgradeCdb | 升级云数据库实例，实例类型支持主实例、灾备实例和只读实例 |
| [查询升级价格](/document/api/236/7193) | InquiryCdbUpgradePrice | 查询云数据库实例的升级价格，实例类型包括主实例、灾备实例和只读实例 |
| [升级数据库引擎版本](/document/api/236/8371) | UpgradeCdbEngineVersion | 升级云数据库实例的引擎版本 |
| [查询升级实例任务详情](/document/api/236/8373) | GetCdbUpgradeJobInfo | 查询实例升级的任务详情，支持查询主实例、灾备实例和只读实例的升级详情 |
| [销毁实例（按量计费）](/document/api/236/6415) | CloseCdbHour | 按量计费模式的实例支持实时销毁实例 |
| [恢复实例（按量计费）](/document/api/236/6416) | OpenCdbHour | 按量计费模式的实例如果已被销毁，可通过此接口实时恢复 |
| [设置自动续费](/document/api/236/4112) | SetCdbAutoRenew| 设置云数据库实例为自动续费 |
| [修改所属项目](/document/api/236/6541) | ModifyCdbInstanceProject | 修改云数据库实例的所属项目 |
| [重置密码](/document/api/236/1271) | ResetCdbInstancesPassword | 重置云数据库实例root帐号的密码 |
| [修改名称](/document/api/236/1270) | ModifyCdbInstanceName | 修改云数据库实例名称 |
| [修改端口](/document/api/236/6543) | ModifyCdbInstanceVport | 修改云数据库实例端口，端口支持范围：1024-65535 |
| [修改字符集](/document/api/236/4113) | ModifyCdbCharset | 修改云数据库实例字符集 |
| [开通外网访问](/document/api/236/7165) | OpenCdbExtranetAccess | 开通云数据库实例的外网访问。开通外网访问后，您可通过外网域名和端口访问实例 |
| [关闭外网访问](/document/api/236/7166) | CloseCdbExtranetAccess | 关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问 |
| [灾备实例切换为主实例](/document/api/236/7460) | SwitchCdbDrToMaster | 云数据库灾备实例切换为主实例，公共参数的地域信息为灾备实例所在地域 |
| [开通GTID](/document/api/236/8372) | OpenCdbGtid | 开通云数据库实例的GTID |
| [查询实例GTID详情](/document/api/236/8374) | GetCdbGtidInfo | 查询实例GTID的详细信息 |
| [查询私有网络子网实例数量](/document/api/236/5440)  | GetCdbInstanceNumByVpcSubnetId | 查询私有网络子网下的云数据库实例数量 |


## 2. 账号相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询账号列表](/document/api/236/8010) | GetCdbInstanceAccountList | 查询数据库帐号列表 |
| [创建账号](/document/api/236/8011) | CreateCdbInstanceAccount | 创建数据库帐号 |
| [查询账号可设置权限](/document/api/236/8063) | GetCdbInstanceAccountAvailablePrivileges | 查询云数据库实例帐号可设置的权限 |
| [查询账号权限](/document/api/236/8062) | GetCdbInstanceAccountPrivileges | 查询云数据库实例帐号的权限 |
| [修改账号权限](/document/api/236/8060) | ModifyCdbInstanceAccountPrivileges | 修改云数据库实例帐号的访问权限 |
| [删除账号](/document/api/236/8012) | DelCdbInstanceAccount | 删除数据库帐号 |
| [修改账号备注](/document/api/236/8013) | ModifyCdbInstanceAccountRemarks | 修改数据库帐号的备注 |
| [修改账号密码](/document/api/236/8061) | ModifyCdbInstanceAccountPassword | 修改云数据库实例帐号的密码 |


## 3. 数据库相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询数据库模式](/document/api/236/8375) | GetCdbInstanceSchema | 查询数据库的模式详情 |
| [查询数据库](/document/api/236/7167) | QueryCdbDatabases | 查询云数据库实例的数据库信息 |
| [查询数据库表](/document/api/236/7176) | QueryCdbDatabaseTables | 查询云数据库实例的数据库表信息 |


## 4. 参数相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询默认参数模板详情](/document/api/236/7190) | GetCdbDefaultParamInfo | 查询默认数据库参数模板详情 |
| [查询参数模板列表](/document/api/236/7185) | GetCdbParamTemplateList | 查询数据库参数模板列表 |
| [新增参数模板](/document/api/236/7186) | AddCdbParamTemplate | 新增数据库参数模板 |
| [删除参数模板](/document/api/236/7187) | DelCdbParamTemplate | 删除数据库参数模板 |
| [查询参数模板详情](/document/api/236/7189) | GetCdbParamTemplateInfo | 查询云数据库参数模板详情 |
| [修改参数模板](/document/api/236/7188) | ModifyCdbParamTemplate | 修改数据库参数模板内容 |
| [查询参数列表](/document/api/236/6369) | GetCdbParams | 使用实例ID查询数据库参数列表 |
| [修改参数](/document/api/236/6368) | ModifyCdbParams | 修改数据库参数，提交成功后返回修改参数的任务ID |
| [查询参数修改记录](/document/api/236/6367) | GetCdbParamsModifyHistory | 查询数据库参数修改记录 |
| [查询修改参数任务详情](/document/api/236/6428) | GetCdbModifyParamsJobTask | 通过修改参数的任务ID查询修改参数任务详情 |


## 5. 监控相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询物理机监控信息](/document/api/236/4687) | GetCdbDeviceMonitorInfo | 查询物理机的监控信息，暂只支持最高配置实例查询 |
| [查询统计信息](/document/api/236/4688) | QueryCdbStatisticsInfo | 查询云数据库统计信息，查询的是最近一分钟的统计数据 |


## 6. 导入相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [上传导入文件](/document/api/236/8595) | UploadCdbImportSQLFile | 用于上传导入文件 |
| [发起文件导入任务](/document/api/236/8376) | StartCdbImportJob | 用于发起文件导入任务 |
| [终止文件导入任务](/document/api/236/8379) | StopCdbImportJob | 用于终止文件导入任务 |
| [查询导入文件列表](/document/api/236/8377) | GetCdbImportSQLFileList | 用于查询导入文件列表 |
| [查询最近导入文件记录](/document/api/236/8378) | GetCdbImportSQLFileHistory | 用于查询最近导入文件记录 |


## 7. 回档相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询回档任务详情](/document/api/236/4114) | GetCdbRollbackJobTask | 查询云数据库实例回档的任务详情 |
| [查询回档任务列表](/document/api/236/4115) | GetCdbRollbackJob | 查询云数据库实例回档任务列表 |
| [查询可回档时间](/document/api/236/7168) | QueryCdbRollbackRangeTime | 查询云数据库实例可回档的时间范围 |
| [执行回档库表](/document/api/236/7169) | RollbackCdbDatabaseTables | 批量回档云数据库实例的库表 |


## 8. 备份相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询备份与日志](/document/api/236/4691) | GetCdbExportLogUrl | 查询实例冷备数据、二进制日志和慢查询日志 |
| [查询备份数据的库表](/document/api/236/5105) | GetBackupDatabaseTableList | 查询备份数据的库表 |
| [查询备份地址（支持分库表）](/document/api/236/5125) | GetExportBackupUrl | 查询备份数据的地址，支持分库表查询 |
| [修改备份信息](/document/api/236/7397) | ModifyCdbBackupInfo | 修改备份信息，例如修改备份的名称 |


## 9. 数据迁移相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [创建数据迁移任务](/document/product/236/7724) | CreateCdbDataMigrationTask | 用于创建数据迁移任务 |
| [查询数据迁移任务列表](/document/product/236/7461) | GetCdbDataMigrationTaskList | 用于查询数据迁移任务列表 |
| [校验数据迁移任务](/document/product/236/7726) | CheckCdbDataMigrationTask | 用于校验数据迁移任务 |
| [启动数据迁移任务](/document/product/236/7712) | StartCdbDataMigrationTask | 用于启动数据迁移任务 |
| [停止数据迁移任务](/document/product/236/7710) | TerminateCdbDataMigrationTask | 用于停止数据迁移任务 |
| [修改数据迁移任务](/document/product/236/7725) | ModifyCdbDataMigrationTask | 用于修改数据迁移任务 |
| [删除数据迁移任务](/document/product/236/7709) | DelCdbDataMigrationTask | 用于停止数据迁移任务 |


## 10. 数据同步相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [创建数据同步任务](/document/product/236/7928) | CreateCdbDataSyncTask | 用于在主实例所在地域创建数据同步任务 |
| [查询数据同步任务列表](/document/product/236/7933) | GetCdbDataSyncTaskList | 用于查询数据同步任务列表 |
| [校验数据同步任务](/document/product/236/7931) | CheckCdbDataSyncTask | 用于校验数据同步任务 |
| [启动数据同步任务](/document/product/236/7930) | StartCdbDataSyncTask | 用于启动数据同步任务 |
| [删除数据同步任务](/document/product/236/7929) | DelCdbDataSyncTask | 用于删除数据同步任务 |


## 11. 任务相关接口
| 接口功能 | Action Name | 功能描述 | 
|---------|---------|---------|
| [查询任务列表](/document/api/236/7464) | GetCdbJobList | 查询云数据库任务列表 |