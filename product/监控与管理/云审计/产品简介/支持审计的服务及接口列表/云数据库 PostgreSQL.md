云数据库 PostgreSQL 能够让您在云端轻松设置、操作和扩展目前功能最强大的开源数据库 PostgreSQL，腾讯云将负责绝大部分处理复杂而耗时的管理工作，如 PostgreSQL 软件安装、存储管理、高可用复制、以及为灾难恢复而进行的数据备份，让您更专注于业务程序开发。

下表为云审计支持的云数据库 PostgreSQL 操作列表：

| 操作名称               | 资源类型     | 事件名称                            |
|--------------------|----------|---------------------------------|
| 关闭实例外网链接           | postgres | CloseDBExtranetAccess           |
| 关闭 serverless 实例外网   | postgres | CloseServerlessDBExtranetAccess |
| 创建 DB 实例             | postgres | CreateDBInstances               |
| 创建 ServerlessDB 实例   | postgres | CreateServerlessDBInstance      |
| 删除 ServerlessDB 实例   | postgres | DeleteServerlessDBInstance      |
| 获取实例用户列表           | postgres | DescribeAccounts                |
| 拉取数据库列表            | postgres | DescribeDatabases               |
| 查询实例备份列表           | postgres | DescribeDBBackups               |
| 获取错误日志             | postgres | DescribeDBErrlogs               |
| 查询实例详情             | postgres | DescribeDBInstanceAttribute     |
| 查询实例列表             | postgres | DescribeDBInstances             |
| 获取慢查询日志            | postgres | DescribeDBSlowlogs              |
| 获取实例 Xlog 列表         | postgres | DescribeDBXlogs                 |
| 查询售卖规格配置           | postgres | DescribeProductConfig           |
| 查询售卖地域             | postgres | DescribeRegions                 |
| 查询 ServerlessDB 实例列表 | postgres | DescribeServerlessDBInstances   |
| 查询售卖可用区            | postgres | DescribeZones                   |
| 销毁实例               | postgres | DestroyDBInstance               |
| 初始化实例              | postgres | InitDBInstances                 |
| 查询售卖价格             | postgres | InquiryPriceCreateDBInstances   |
| 修改帐号备注             | postgres | ModifyAccountRemark             |
| 修改实例名字             | postgres | ModifyDBInstanceName            |
| 将实例转至其他项目          | postgres | ModifyDBInstancesProject        |
| 开通外网               | postgres | OpenDBExtranetAccess            |
| 开通 serverless 实例外网   | postgres | OpenServerlessDBExtranetAccess  |
| 续费实例               | postgres | RenewInstance                   |
| 重置账户密码             | postgres | ResetAccountPassword            |
| 重启实例               | postgres | RestartDBInstance               |
| 设置自动续费             | postgres | SetAutoRenewFlag                |
| 升级实例               | postgres | UpgradeDBInstance               |


