## 操作场景

数据接入平台提供数据流出能力，您可以将 CKafka 数据分发至云数据库 MySQL 以对数据进行存储、查询和分析。

## 前提条件

该功能目前依赖云数据库 MySQL 产品，使用时需开通相关产品功能。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **数据库 MySQL**，单击**下一步**。
4. 配置数据源信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f8b47026ccb8b0982605b59d7b926f5b.png)
   - 源 Topic 类型：选择数据源 Topic
     - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
     - CKafka Topic：选择在 CKafka 创建好的实例和 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
   - 起始位置：选择转储时历史消息的处理方式，topic offset 设置。
5. 设置上述信息后，单击**下一步**，单击**预览 Topic 数据**，将会选取**源 Topic** 中的第一条消息进行解析。
   >? 目前解析消息需要满足以下条件：
   >
   >- 消息为 JSON 字符串结构。
   >- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用使用 [数据处理](https://cloud.tencent.com/document/product/1591/77082#3) 进行简单的消息格式转换。 
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/1591/74495)。
7. 单击**下一步**，配置数据目标信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1983155c3585d09e9f4ca1a1ebaffbd4.png)
   - 数据目标：选择提前创建好的 MySQL 连接。
   - database：选择数据流出的数据库。
   - table：选择数据流出的表。
   - 源数据：单击拉取源 Topic 数据，当预览结果目标表字段和来源表字段类型不匹配时，会提示报错。
   - 插入模式：支持 **insert** 或者 **upsert**，选择 upsert 时需选择**主键**（当插入行冲突时，任务将更新冲突行除主键之外其余的列）。
   - 失败消息处理：选择投递失败的消息的处理方式，支持**丢弃**、**保留**两种方式。
     - 保留：适合用于测试环境，任务运行失败时将会终止任务不会重试，并且在事件中心中记录失败原因。
     - 丢弃：适合用于生产环境，任务运行失败时将会忽略当前失败消息。建议使用 "保留" 模式测试无误后，再将任务编辑成 "丢弃" 模式用于生产。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。


