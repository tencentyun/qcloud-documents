## 操作场景

数据接入平台提供数据流出能力，您可以将 CKafka 数据分发至数据仓库 ClickHouse 以对数据进行存储、查询和分析。

## 前提条件

- 若使用腾讯云维护的 ClickHouse 产品，使用时需开通相关产品功能。同时也支持数据流出至自建 ClickHouse。
- 在 ClickHouse 建好表，建表的时候需要指定好 Column 和 Type。
- 已创建好数据流出目标 ClickHouse 连接。

## 操作步骤

### 创建任务

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **数据仓库（ClickHouse）**，单击**下一步**。
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
>- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用 [数据处理](https://cloud.tencent.com/document/product/1591/77082#3) 进行简单的消息格式转换。 
> 解析完成后，控制台将会出现解析后的消息字段，可以通过修改预览结果中的 type 属性来确定投递到目标对应列的类型。
>  当选择 type 为 `Date` 或 `DateTime` 时，如果源消息格式为整型，将会尝试使用 `unix timestamp` 格式解析；如果源消息格式为字符串，将会尝试用常用的时间格式模式串解析。
>  ![](https://qcloudimg.tencent-cloud.cn/raw/4c238e5b241311845b9f92dacb39ef91.png)
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/1591/74495)。
7. 单击**下一步**，配置数据目标信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4f159bc2a6c3a47a2387834d12230103.png)
   - 数据目标：选择创建好的 Clickhouse 连接。
   - cluster： ClickHouse 的集群名称（默认为 `default_cluster`）。
   - database：ClickHouse 设置的数据库名称。
   - table：在该数据库内构建的表名称，目前数据流出 ClickHouse 服务不会自动创建表，**需要客户手动创建当前 ClickHouse 目标表**。
   - 源数据：单击拉取源 Topic 数据。源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用 [数据处理](https://cloud.tencent.com/document/product/1591/77082#3) 功能进行转换。
   - 失败消息处理：选择投递失败的消息的处理方式，支持**丢弃**、**保留**和**投递至 CLS** （需指定投递到的日志集和日志主题并授权访问日志服务 CLS）三种方式。
     - 保留：适合用于测试环境，任务运行失败时将会终止任务不会重试，并且在事件中心中记录失败原因。
     - 丢弃：适合用于生产环境，任务运行失败时将会忽略当前失败消息。建议使用 "保留" 模式测试无误后，再将任务编辑成 "丢弃" 模式用于生产。
     - 投递至 CLS：适合用于严格生产环境，任务运行失败时会将失败消息及元数据和失败原因上传到指定 CLS 主题中。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。
