## 1. 地域相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [查询可创建实例规格](/document/product/240/8318) | DescribeMongoDBProduct | 查询可创建的实例规格 |

## 2. 实例相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [查询实例价格（包年包月）](/document/product/240/8311) | InquiryMongoDB | 获取实例价格(包年包月),支持新购、续费、升级实例时价格查询 |
| [创建实例（包年包月）](/document/product/240/8308) | CreateMongoDB | 创建实例（包年包月），并扣除[查询实例价格（包年包月）](/document/product/240/8311)接口返回的费用|
| [续费实例(包年包月)](/document/product/240/8314) | RenewMongoDB| 续费指定实例，并扣除[查询实例价格（包年包月）](/document/product/240/8311)接口返回的费用|
| [升级实例(包年包月)](/document/product/240/8309) | UpgradeMongoDB| 升级指定实例，并扣除[查询实例价格（包年包月）](/document/product/240/8311)接口返回的费用|
| [查询订单详情](/document/product/240/8313)| DescribeMongodbDealDetail | 查询新购、续费、升级订单的详情|
| [查询实例列表](/document/product/240/8312) | DescribeMongoDBInstances |  按条件查询副本集实例详情列表 | 
| [设置自动续费](/document/product/240/8315)| SetMongoDBAutoRenew | 设置或取消自动续费， 设置自动续费后，系统将在实例到期时，自动发起续费|
| [重置实例密码](/document/product/240/8316) | ResetMongoDBPassword | 重置实例密码 |
| [修改实例项目](/document/product/240/8307) | ModifyMongoDBProject| 修改实例所属项目|
| [修改实例名称](/document/product/240/8306) | ModifyMongoDBName | 修改实例名称|
| [查询任务结果](/document/product/240/8310) | GetMongoDBJobInfo | 查询任务执行结果 |
