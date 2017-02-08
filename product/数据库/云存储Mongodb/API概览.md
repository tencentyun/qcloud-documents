## 1. 地域相关接口
| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [查询可创建规格（支持可用区、配置自定义）] | DescribeMongoDBProduct | 查询可创建的实例规格 |


## 2. 实例相关接口

| 接口名 | Action Name | 功能描述 |
|---------|---------|---------|
| [查询复制集实例价格(包年包月)] | InquiryMongoDBReplSetPrice | 获取复制集实例价格(包年包月),支持新购、续费、升级实例时价格查询 |
| [创建复制集实例（包年包月）] | CreateMongoDBReplSet | 创建复制集实例（包年包月），并扣除[查询复制集实例价格(包年包月)]接口返回的费用|
| [续费实例(包年包月)] | RenewMongoDB| 续费指定实例，并扣除[查询复制集实例价格(包年包月)]接口返回的费用|
| [升级实例(包年包月)] | UpgradeMongoDB| 升级指定实例，并扣除[查询复制集实例价格(包年包月)]接口返回的费用|
| [查询订单详情] | DescribeMongodbDealDetail | 查询新购、续费、升级订单的详情|
| [设置自动续费]| SetMongoDBAutoRenew | 设置或取消自动续费， 设置自动续费后，系统将在实例到期时，自动发起续费|
| [修改实例名称] | ModifyMongoDBName | 修改实例名称|
| [修改实例项目] | ModifyMongoDBProject| 修改实例所属项目|
| [查询复制集实例列表] | DescribeMongoDBReplSet |  按条件查询复制集实例详情列表 | 
| [重置实例密码] | ResetMongoDBPassword | 重置实例密码 |
| [查询任务结果] | GetMongoDBJobInfo | 查询任务执行结果 |  