## 操作场景

数据接入平台提供数据流出能力，您可以将 CKafka 数据分发至日志服务 CLS 便于解决业务问题定位，指标监控，安全审计等日问题。

## 前提条件

该功能目前依赖 CLS 服务，使用时需开通相关产品功能。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **日志服务（CLS）**，单击**下一步**。
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
>
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/1591/74495)。
7. 单击**下一步**，配置数据目标信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a4edbd19313cdbe9573d4fdad296f2b8.png)
   - 源数据：单击**点击拉取**可以拉取源数据，数据按 JSON 解析后投递。
   - KEY：源 Topic 内数据不是 JSON 格式时，可以指定 key 组装为 JSON 投递到 CLS 中。默认为 content。
   - 日志集：选择日志集，日志集日志服务的项目管理单元，用于区分不同项目的日志。
   - 日志主题：自动创建日志主题或者选择已有日志主题。一个 [日志集](https://cloud.tencent.com/document/product/614/35676) 可以包含多个日志主题，一个日志主题对应一类应用或服务，建议将不同机器上的同类日志收集到同一个日志主题。
   - 日志时间：可以指定源数据中的某一字段作为日志时间。
   - 角色授权：使用日志服务（CLS）产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。
