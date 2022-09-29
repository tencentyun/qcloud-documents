## 操作场景

数据接入平台提供数据流出能力，您可以将 CKafka 数据分发至 Elasticsearch Service（ES）便于海量数据存储搜索、实时日志分析等操作。
>?只支持7.0以上版本的 Elasticsearch Service。

## 前提条件

- 该功能目前依赖 Elasticsearch Service 服务，使用时需开通相关产品功能。
- 已创建好数据流出目标 Elasticsearch Service 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **Elasticsearch Service**，单击**下一步**。
4. 配置数据源信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f8b47026ccb8b0982605b59d7b926f5b.png)
   - 源 Topic 类型：选择数据源 Topic
     - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/1591/77020)。
     - CKafka Topic：选择在 CKafka 创建好的实例和 Topic，一条数据流出任务最多支持选择 5 个源 Topic，选中的 Topic 内的数据格式需要保持一致方可转储成功。详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
   - 起始位置：选择转储时历史消息的处理方式，topic offset 设置。
5. 设置上述信息后，单击**下一步**，单击**预览 Topic 数据**，将会选取**源 Topic** 中的第一条消息进行解析。
>? 目前解析消息需要满足以下条件：
>
>- 消息为 JSON 字符串结构。
>- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用使用 [数据处理](https://cloud.tencent.com/document/product/1591/77082#3) 进行简单的消息格式转换。 
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/1591/74495)。
7. 单击**下一步**，配置数据目标信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1c2284d1a0a76ad6e44b8eaab34997b6.png)
   - 源数据：单击拉取源 Topic 数据。
   - 数据目标：选择提前创建好的数据流出的目标 Elasticsearch Service 连接。
   - 索引名称：填写索引名称，索引名称必须全部为小写，支持 jsonpath 语法。
   - 按日期拆分索引名称：可选，开启后需选择日期格式，写入 ES 的索引为%（索引名称）\_%（日期）。
   - 保留非 JSON 数据：如果保留非 JSON 数据开启，则会指定 key 进行组装投递，关闭则丢弃。
   - KEY：源 topic 内数据不是 JSON 格式时，可以指定 key 组装为 JSON 投递到 ES 中。
   - 数据库同步模式：本选项仅用于 DIP 订阅 MySQL，PostgreSQL 数据库到 Topic（仅支持1分区的 Topic）里面的数据（增删改）同步更新到 ES。会识别数据库的增删改，保持 ES 的数据与源表的数据一致。
   - 主键：开启**数据库同步模式**后，需要指定数据库表的主键作为 ES 文档 ID 的值。
   - ES 文档 ID 字段：未开启**数据库同步模式**时，指定该字段内的值作为 ES 文档 ID 的值。
   - 失败消息处理：选择投递失败的消息的处理方式，支持**丢弃**、**保留**和**投递至 CLS** （需指定投递到的日志集和日志主题并授权访问日志服务 CLS）三种方式。
     - 保留：适合用于测试环境，任务运行失败时将会终止任务不会重试，并且在事件中心中记录失败原因。
     - 丢弃：适合用于生产环境，任务运行失败时将会忽略当前失败消息。建议使用 "保留" 模式测试无误后，再将任务编辑成 "丢弃" 模式用于生产。
     - 投递至 CLS：适合用于严格生产环境，任务运行失败时会将失败消息及元数据和失败原因上传到指定 CLS 主题中。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。
