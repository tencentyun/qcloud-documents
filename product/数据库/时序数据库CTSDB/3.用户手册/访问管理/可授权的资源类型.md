时序数据库 CTSDB 支持资源级授权，您可以指定子账号拥有特定资源的接口权限。

支持资源级授权的接口列表如下：
>?表中未列出的云数据库 API 操作，即表示该 CTSDB API 操作不支持资源级权限。针对不支持资源级权限的 CTSDB API 操作，您仍可以向用户授予使用该操作的权限，但策略语句的资源元素必须指定为 *。

| API 名                  | API 描述                 |  资源六段式示例                                       |
| ----------------------- | ------------------------ |---------------------------------------------------- |
| ModifyDBInstanceUserPassword | 修改数据库实例用户密码   |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| DescribeDBInstances   | 查询实例列表 |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| InitDBInstance     | 初始化数据库实例 |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| ModifyDBInstanceName     | 修改数据库实例名称 |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| ModifyDBInstanceProject | 修改数据库实例项目         |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| RecycleDBInstance       | 回收数据库实例      |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| DescribeDBInstanceMetricInfo    | 查询数据库实例 Metric 信息     |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| DescribeDBInstanceMetricList  | 查询数据库实例 Metric 列表   |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |
| DescribeDBInstanceMetricQuery        | 查询数据库实例 Metric 查询 |  `qcs::ctsdb:$region:$account:instanceId/*`    `qcs::ctsdb:$region:$account:instanceId/$instanceId` |

