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
     - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/76516)。
     - CKafka Topic：选择在 CKafka 创建好的实例和 Topic，一条数据流出任务最多支持选择 5 个源 Topic，选中的 Topic 内的数据格式需要保持一致方可转储成功。详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
   - 起始位置：选择转储时历史消息的处理方式，topic offset 设置。
5. 设置上述信息后，单击**下一步**，单击**预览 Topic 数据**，将会选取**源 Topic** 中的第一条消息进行解析。
>? 目前解析消息需要满足以下条件：
>
>- 消息为 JSON 字符串结构。
>- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用 [数据处理](https://cloud.tencent.com/document/product/597/73131#.E5.A4.84.E7.90.86.E5.AD.97.E7.AC.A6.E4.B8.B2.E5.BA.8F.E5.88.97.E5.8C.96-json-.E6.A0.BC.E5.BC.8F.E6.97.A5.E5.BF.97) 进行简单的消息格式转换。 
   解析完成后，控制台将会出现解析后的消息字段，可以通过修改预览结果中的 type 属性来确定投递到目标对应列的类型。
   当选择 type 为 `Date` 或 `DateTime` 时，如果源消息格式为整型，将会尝试使用 `unix timestamp` 格式解析；如果源消息格式为字符串，将会尝试用常用的时间格式模式串解析。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4c238e5b241311845b9f92dacb39ef91.png)
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/597/76063)。
7. 单击**下一步**，配置数据目标信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4f159bc2a6c3a47a2387834d12230103.png)
   - 源数据：点击拉取源 Topic 数据。源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用 [数据处理](https://cloud.tencent.com/document/product/597/73131#.E5.A4.84.E7.90.86.E5.B5.8C.E5.A5.97.E7.B1.BB.E5.9E.8B.E6.A0.BC.E5.BC.8F.E6.97.A5.E5.BF.97) 功能进行转换。
   - 数据目标：选择创建好的 Clickhouse 连接。
   - cluster： ClickHouse 的集群名称（默认为 `default_cluster`）。
   - database：ClickHouse 设置的数据库名称。
   - table：在该数据库内构建的表名称，目前数据流出 ClickHouse 服务不会自动创建表，**需要客户手动创建当前 ClickHouse 目标表**。
   - 丢弃解析消息：消息解析失败原因一般是消息字段与目标库字段 type 不一致。若不丢弃解析失败消息，则任务异常，转储不再继续。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。




