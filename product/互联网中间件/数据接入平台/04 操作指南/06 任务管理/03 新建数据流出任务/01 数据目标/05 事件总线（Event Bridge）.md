## 操作场景

数据接入平台提供数据流出能力，CKafka 数据经过事件总线数据可以流出至以下对象：COS，CLS 和 Elasticsearch Service。

数据流出至事件总线 Event Bridge 基于云函数 SCF 服务提供。SCF 为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282)，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。

## 前提条件

该功能目前依赖 SCF 服务。使用时需开通云函数 SCF 服务及功能。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据流出**，数据目标类型选择 **事件总线（Event Bridge）**，单击**下一步**。
>?通过云函数和事件总线处理，需要确认同意 [云函数使用说明](https://cloud.tencent.com/document/product/583) 和 [云函数计费说明](https://cloud.tencent.com/document/product/583/17299)。
4. 配置数据源信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/fe8388925ab1276671f1940943a1144b.png)
   - 源 Topic 类型：只支持 CKafka Topic 类型。
     - CKafka Topic：选择在 CKafka 创建好的实例和 Topic，一条数据流出任务最多支持选择 5 个源 Topic，选中的 Topic 内的数据格式需要保持一致方可转储成功。详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
   - 起始位置：选择转储时历史消息的处理方式，topic offset 设置。
5. 设置上述信息后，单击**下一步**，单击**预览 Topic 数据**，将会选取**源 Topic** 中的第一条消息进行解析。
   >? 目前解析消息需要满足以下条件：
   >
   >- 消息为 JSON 字符串结构。
   >- 源数据必须为单层 JSON 格式，嵌套 JSON 格式可使用使用 [数据处理](https://cloud.tencent.com/document/product/1591/77082#3) 进行简单的消息格式转换。 
6. （可选）开启数据处理规则，具体配置方法请参见 [简单数据处理](https://cloud.tencent.com/document/product/1591/74495)。
7. 单击**下一步**，配置数据目标信息。
   <dx-tabs>
   :::COS

   - 事件目标：选择 **COS**。
   - 源数据：点击拉取源 Topic 数据。
   - 目标存储桶：对不同的 Topic，选取相应的 COS 中 Bucket，则请求消息会自动在 Bucket 下创建 instance-id/topic-id/date/timestamp 为名称的文件路径进行存储。相关路径如无法满足业务需要，请创建完成后在云函数 CkafkaToCosConsumer 下自行修改。
   - 聚合方式：请至少填写一种聚合方式，文件将根据指定方式聚合进入 COS 存储桶。如果指定了两种聚合方式，则会同时生效。例：指定每1h或1GB聚合一次，若在1h之前达到1GB，则文件会聚合，同时在1h时也会聚合一次。
   - 角色授权：使用 SCF 云函数和事件总线（EventBridge）产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
   - 云函数授权：知晓并同意开通创建云函数和事件总线，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。

   :::

   :::CLS

   - 事件目标：选择 **CLS**。
   - 源数据：点击拉取源 Topic 数据。
   - 日志集：选择日志集，日志集日志服务的项目管理单元，用于区分不同项目的日志。
   - 日志主题：自动创建日志主题或者选择已有日志主题。一个 [日志集](https://cloud.tencent.com/document/product/614/35676) 可以包含多个日志主题，一个日志主题对应一类应用或服务，建议将不同机器上的同类日志收集到同一个日志主题。
   - 角色授权：使用事件总线（EventBridge）产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。

   :::

   :::ES

   - 事件目标：选择 **ES**。
   - 源数据：点击拉取源 Topic 数据。
   - 自建集群：如 ES 集群为自建集群，请将自建集群开关保持开启状态，并填写示例 IP。如 Elasticsearch 集群为腾讯云集群，则直接选取相关集群信息即可。
   - 实例集群：选取腾讯云 Elasticsearch Service 实例集群信息。
   - 实例用户名：输入 Elasticsearch 实例用户名，腾讯云 Elasticsearch 默认用户名为 elastic，且不可更改。
   - 实例密码：输入 Elasticsearch 实例密码。
   - 云函数授权：知晓并同意开通云函数和事件总线，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。

   :::

   </dx-tabs>
8. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以查看任务创建进度。



