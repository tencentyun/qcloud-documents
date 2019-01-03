#### 下列操作可支持资源级权限

| 操作名 | API名 |配置后控制台是否生效|
| :-------- | :------------------------ |:------------------------ |
| 查询实例升级价格 | DescribeDCDBUpgradePrice |NO|
| 续费实例 | RenewDCDBInstance |NO|
| 查询实例续费价格 | DescribeDCDBRenewalPrice |NO|
| 实例扩容 | UpgradeDCDBInstance |NO|
| 查看实例列表 | DescribeDCDBInstances |YES|
| 获取日志列表 | DescribeDBLogFiles |YES|
| 初始化实例 | InitDCDBInstances |NO|
| 创建帐号 | CreateAccount |YES|
| 查询帐号列表 | DescribeAccounts |YES|
| 删除帐号 | DeleteAccount |YES|
| 设置帐号权限 | GrantAccountPrivileges |YES|
| 查询帐号权限 | DescribeAccountPrivileges |YES|
| 复制帐号权限 | CopyAccountPrivileges |NO|
| 修改数据库帐号备注 | ModifyAccountDescription |NO|
| 重置帐号密码 | ResetAccountPassword |YES|
| 查看数据库参数 | DescribeDBParameters |NO|
| 修改数据库参数 | ModifyDBParameters |NO|
| 克隆帐号 | CloneAccount |YES|
| 获取SQL日志 | DescribeSqlLogs |NO|
