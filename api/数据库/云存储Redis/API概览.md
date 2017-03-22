## 1. 地域相关接口
| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [查询售卖可用区](http://www.qcloud.com/doc/api/260/4951) | DescribeRedisZones | 查询可以购买redis的可用区列表 |
| [查询可售卖规格](http://www.qcloud.com/doc/api/260/4974) | DescribeRedisProduct | 查询可购买实例的规格，比如最大容量、可购买数量等 |


## 2. 实例相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [查询实例价格（包年包月）](http://www.qcloud.com/doc/api/260/5324) | InquiryRedisPrice | 查询创建实例和续费实例需要的费用 |
| [创建实例（包年包月）](http://www.qcloud.com/doc/api/260/5325) | CreateRedis | 按照指定的规格、网络等配置，创建redis实例， 并扣除[查询实例价格](http://www.qcloud.com/doc/api/260/5324)接口返回的费用|
| [续费实例（包年包月）](http://www.qcloud.com/doc/api/260/5326)  | RenewRedis| 续费指定实例， 并扣除[查询实例价格](http://www.qcloud.com/doc/api/260/5324)接口返回的费用|
| [查询升级实例价格（包年包月）](http://www.qcloud.com/doc/api/260/5327) | UpgradeRedisInquiryPrice | 查询升级实例到指定规格的费用|
| [升级实例 （包年包月）](http://www.qcloud.com/doc/api/260/5328)| UpgradeRedis | 升级实例到指定的规格，并扣除[查询升级实例价格](http://www.qcloud.com/doc/api/260/5327)接口返回的费用信息|
| [查询订单详情](http://www.qcloud.com/doc/api/260/5329) | DescribeRedisDealDetail | 查询订单详细信息|
| [设置自动续费](http://www.qcloud.com/doc/api/260/5330)  | SetRedisAutoRenew| 设置或取消自动续费， 设置自动续费后，系统将在实例到期时，自动发起续费|
| [查询 CRS 实例及实例列表](http://www.qcloud.com/doc/api/260/1384) | DescribeRedis |  按条件查询实例详情列表 | 
| [修改CRS实例密码](http://www.qcloud.com/doc/api/260/1390) | ModfiyRedisPassword | 修改实例密码|
| [重置CRS实例密码](/document/product/239/1390) | ResetRedisPassword | 重置实例密码|
| [修改Redis实例项目](http://www.qcloud.com/doc/api/260/1385) | ModifyRedisProject |  修改实例所属项目 |
| [清空CRS实例](http://www.qcloud.com/doc/api/260/1386) | ClearRedis |  清空实例数据 | 
| [CRS查询任务结果](http://www.qcloud.com/doc/api/260/1387) | DescribeTaskInfo | 查询任务执行结果 |
| [手动备份 CRS 实例](/document/product/239/8402) | ManualBackupInstance | 手动备份 CRS 实例 |
| [查询 CRS 实例备份列表](/document/product/239/8403) | GetRedisBackupList | 查询 CRS 实例备份列表 |  
| [恢复 CRS 实例](/document/product/239/8401) | RestoreInstance | 恢复 CRS 实例 |
| [导出CRS实例备份](/document/product/239/8430) | ExportRedisBackup | 导出CRS实例备份 |  
| [查询 CRS 实例的任务列表](/document/product/239/8404) | GetRedisTaskList | 查询 CRS 实例的任务列表 |
