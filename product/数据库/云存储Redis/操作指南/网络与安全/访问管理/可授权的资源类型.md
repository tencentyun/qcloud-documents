资源级权限指的是能够指定用户对哪些资源具有执行操作的能力。Redis 部分支持资源级权限，即表示针对支持资源级权限的 Redis 操作，您可以控制何时允许用户执行操作或是允许用户使用特定资源。访问管理 CAM 中可授权的资源类型如下：

| 资源类型                     | 授权策略中的资源描述方法                                     |
| ---------------------------- | ------------------------------------------------------------ |
| [云数据库 Redis 实例相关](#xiangguan) | `qcs::redis:$region::instance/*`<br>`qcs::redis:$region:$account:instance/$instance` |

下表将介绍当前支持资源级权限的 Redis API 操作，以及每个操作支持的资源。指定资源路径的时候，您可以在路径中使用 * 通配符。

<span id="xiangguan"></span>
### [支持资源级授权的 API 列表](id:xiangguan)

| API 操作                                 | 资源路径                                                     |
| ---------------------------------------- | ------------------------------------------------------------ |
| AssignProject                            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| AssociateSecurityGroups                  | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| AutoRenew                                | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| BackupInstance                           | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| CleanInstance                            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| CleanUpInstance                          | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ClearInstance                            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ClearRedis                               | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| CreateInstance                           | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| CreateInstanceAccount                    | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| CreateInstanceHour                       | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| CreateInstances                          | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| CreateRedis                              | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DeleteInstance                           | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DeleteInstanceAccount                    | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeAutoBackupConfig                 | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeBackupUrl                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeDBSecurityGroupsDetail           | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceAccount                  | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceBackups                  | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceDealDetail               | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceParamRecords             | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceParams                   | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceSecurityGroup            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceSecurityGroupsAssociated | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceShards                   | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstanceSlowlog                  | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeInstances                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeProjectSecurityGroup             | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeRedis                            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeRedisDealDetail                  | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeRedisProduct                     | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeRedisProductList                 | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeRedisRegions                     | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeRedisZones                       | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeSlowLog                          | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeTaskInfo                         | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeTaskList                         | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeTasks                            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DescribeVPCRedis                         | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DestroyPostpaidInstance                  | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DestroyPrepaidInstance                   | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| DisableReplicaReadonly                   | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| EnableReplicaReadonly                    | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ExportRedisBackup                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| GetBackupDownloadUrl                     | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| GetRedisBackupList                       | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| GetRedisPerformance                      | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| GetRedisSlowLogList                      | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| GetRedisTaskList                         | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| InitRedisPassword                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| InquiryRedisPrice                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ManualBackupInstance                     | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModfiyInstancePassword                   | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModfiyRedisPassword                      | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyAutoBackupConfig                   | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyDBInstanceSecurityGroups           | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyInstance                           | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyInstanceAccount                    | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyInstanceParams                     | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyInstanceSecurityGroup              | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyNetworkConfig                      | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyRedisName                          | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyRedisParams                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ModifyRedisProject                       | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| RenewInstance                            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| RenewRedis                               | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ResetPassword                            | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| ResetRedisPassword                       | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| RestoreInstance                          | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| SetRedisAutoRenew                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| StartupInstance                          | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| SwitchInstanceVip                        | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| UnAssociateSecurityGroups                | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| UpgradeInstance                          | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| UpgradeRedis                             | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |
| UpgradeRedisInquiryPrice                 | `qcs::redis:$region:$account:instance/*`    `qcs::redis:$region:$account:instance/$instance` |

### 非资源级授权的 API 列表
针对不支持资源级权限的云数据库 API 操作，您仍可以向用户授予使用该操作的权限，但策略语句的资源元素必须指定为 *。

| API 操作                       | API 描述                      |
| ----------------------------- | ---------------------------- |
| CreateInstances              | 创建 Redis 实例 |
| CreateParamTemplate           | 创建参数模板                 |
| DeleteParamTemplate           | 删除参数模板           |
| DescribeInstanceDealDetail      | 查询订单信息       |
| DescribeParamTemplateInfo                 | 获取参数模板详情     |
| DescribeParamTemplates         | 获取参数模板列表          |
| DescribeTaskInfo         | 查询任务信息          |
| DescribeTasks         | 查询任务列表          |
| ModifyParamTemplate           | 修改参数模板                 |
