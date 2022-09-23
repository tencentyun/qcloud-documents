云数据库 Redis（TencentDB for Redis）是基于腾讯云在分布式缓存领域多年技术沉淀，提供的兼容 Redis 协议、高可用、高可靠、高弹性的数据库服务。云数据库 Redis 兼容 Redis 2.8、Redis 4.0、Redis 5.0 版本协议，提供标准和集群两大架构版本。最大支持4TB的存储容量，千万级的并发请求，满足业务在缓存、存储、计算等不同场景中的需求。

下表为云审计支持的云数据库 Redis 操作列表：

| 操作名称                    | 资源类型  | 事件名称                          |
|-------------------------|-------|-------------------------------|
| 回收站下线实例                 | redis | CleanUpInstance               |
| CreateInstanceAccount   | redis | CreateInstanceAccount         |
| DeleteInstanceAccount   | redis | DeleteInstanceAccount         |
| 查询实例备份下载 URL             | redis | DescribeBackupUrl             |
| DescribeInstanceAccount | redis | DescribeInstanceAccount       |
| 查询实例订单信息                | redis | DescribeInstanceDealDetail    |
| 查询实例参数修改历史              | redis | DescribeInstanceParamRecords  |
| 查询实例参数                  | redis | DescribeInstanceParams        |
| DescribeInstances       | redis | DescribeInstances             |
| 查询实例安全组信息               | redis | DescribeInstanceSecurityGroup |
| 查询实例分片信息                | redis | DescribeInstanceShards        |
| 查询项目安全组信息               | redis | DescribeProjectSecurityGroup  |
| 查询任务信息                  | redis | DescribeTaskInfo              |
| 查询任务列表信息                | redis | DescribeTaskList              |
| 销毁后付费实例                 | redis | DestroyPostpaidInstance       |
| 销毁预付费实例                 | redis | DestroyPrepaidInstance        |
| 关闭实例副本只读                | redis | DisableReplicaReadonly        |
| 开启实例副本只读                | redis | EnableReplicaReadonly         |
| 修改 Redis 密码               | redis | ModfiyInstancePassword        |
| 设置自动备份时间                | redis | ModifyAutoBackupConfig        |
| ModifyInstanceAccount   | redis | ModifyInstanceAccount         |
| 修改实例参数                  | redis | ModifyInstanceParams          |
| 修改实例网络                  | redis | ModifyNetworkConfig           |
| 回收站开启实例                 | redis | StartupInstance               |


