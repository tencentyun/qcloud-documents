## 操作场景

数据接入平台提供数据流出能力，您可以将 CKafka 数据分发至 Elasticsearch Service（ES）便于海量数据存储搜索、实时日志分析等操作。
>?只支持7.0以上版本的 Elasticsearch Service。

## 前提条件

- 该功能目前依赖 Elasticsearch Service 服务，使用时需开通相关产品功能。
- 已创建好数据流出目标 Elasticsearch Service 连接。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **日志服务（CLS）**，单击**下一步**。
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
>- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用使用 [数据处理](https://cloud.tencent.com/document/product/597/73131#.E5.A4.84.E7.90.86.E5.AD.97.E7.AC.A6.E4.B8.B2.E5.BA.8F.E5.88.97.E5.8C.96-json-.E6.A0.BC.E5.BC.8F.E6.97.A5.E5.BF.97) 进行简单的消息格式转换。 
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/597/76063)。
7. 单击**下一步**，配置数据目标信息。
![](https://qcloudimg.tencent-cloud.cn/raw/1c2284d1a0a76ad6e44b8eaab34997b6.png)
   - 源数据：点击拉取源 Topic 数据。
   - 数据目标：选择提前创建好的数据流出的目标 Elasticsearch Service 连接。
   - 索引名称：填写索引名称，索引名称必须全部为小写。
   - 按日期拆分索引名称：可选，开启后需选择好日期格式，写入 ES 的索引为%（索引名称）\_%（日期）。
   - 保留非 JSON 数据：如果保留非 JSON 数据开启，则会指定 key 进行组装投递，关闭则丢弃。
   - KEY：源 topic 内数据不是 JSON 格式时，可以指定 key 组装为 JSON 投递到 ES 中。
   - ES 文档 ID 字段：指定该字段内的值作为 ES 文档 ID 的值。
   - 失败消息处理：指定投递失败消息的处理方式，支持**丢弃**或者**保留**。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。



