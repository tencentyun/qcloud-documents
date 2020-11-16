数据传输服务（Data Transmission Service，DTS）是提供数据迁移、数据同步、数据订阅于一体的数据库数据传输服务。帮助用户在业务不停服的前提下轻松完成数据库迁移，利用实时同步通道轻松构建异地容灾的高可用数据库架构，利用数据订阅提供的云数据库实时增量更新数据，用户可根据自身业务需求自由消费增量数据。

下表为云审计支持的数据传输服务操作列表：

| 操作名称         | 资源类型 | 事件名称                         |
|--------------|------|------------------------------|
| 完成数据迁移       | dts  | CompleteMigrateJob           |
| 配置数据对比任务     | dts  | ConfigDataComparisonJob      |
| 创建 AccessKey  | dts  | CreateAccessKey              |
| 创建迁移校验任务     | dts  | CreateMigrateCheckJob        |
| 创建数据迁移任务     | dts  | CreateMigrateJob             |
| 创建数据订阅       | dts  | CreateSubscribe              |
| 删除迁移任务       | dts  | DeleteMigrateJob             |
| 查询 Access Key | dts  | DescribeAccessKeys           |
| 查询数据对比结果     | dts  | DescribeDataComparisonResult |
| 查询校验任务结果     | dts  | DescribeMigrateCheckJob      |
| 查看迁移任务       | dts  | DescribeMigrateJobs          |
| 查看迁移库表       | dts  | DescribeMigrateObject        |
| 查询订阅配置       | dts  | DescribeSubscribeConf        |
| 查询订阅实例是否可以退换 | dts  | DescribeSubscribeReturnable  |
| 查询订阅实例列表     | dts  | DescribeSubscribes           |
| 隔离订阅实例       | dts  | IsolateSubscribe             |
| 修改迁移任务       | dts  | ModifyMigrateJob             |
| 修改迁移名称       | dts  | ModifyMigrateName            |
| 修改订阅通道消费时间位点 | dts  | ModifySubscribeConsumeTime   |
| 修改订阅名称       | dts  | ModifySubscribeName          |
| 修改数据订阅对象     | dts  | ModifySubscribeObjects       |
| 修改订阅服务地址     | dts  | ModifySubscribeVipVport      |
| 下线已隔离的实例     | dts  | OfflineIsolatedSubscribe     |
| 重置数据订阅通道     | dts  | ResetSubscribe               |
| 启动迁移任务       | dts  | StartMigrateJob              |
| 撤销迁移任务       | dts  | StopMigrateJob               |
