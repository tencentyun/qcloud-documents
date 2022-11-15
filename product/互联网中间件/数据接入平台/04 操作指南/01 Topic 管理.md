## 操作场景

Topic（主题）是某一种分类的名字，消息在 Topic 中可以被存储和发布，生产者往 Topic 中写消息，消费者从 Topic 中读消息。为了做到水平扩展，一个 Topic 实际是由多个 Partition（分区）组成，遇到瓶颈时，可以通过增加 Partition 的数量进行横向扩容。

Topic 是数据接入平台订阅和发布的最小单位，用户可以用 Topic 来表示一类或者一种流数据，您可以在 DIP 控制台单独创建 Topic 作为数据任务的数据源或者数据目标。

## 操作步骤

### 创建 Topic

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击 **Topic 列表**，选择好地域后，单击**新建 Topic**。
3. 填写 Topic 信息后，单击**确定**，完成 Topic 创建。
   - Topic 名称：Topic 名称由“appid-[用户输入的名称]”构成，用户输入的名称只能包含字母、数字、下划线、“-”、“.”。
   - 备注：选填，Topic 备注信息。
   - 分区数：一个物理上分区的概念，一个 Topic 可以包含一个或者多个 Partition，CKafka 以 Partition 作为分配单位。单个 Topic 支持最大分区数：50。
   - 消息保留时间：范围1分钟到90天。在磁盘容量不足（即磁盘水位达到90%）时，将会提前删除旧的消息，以确保服务可用性。
     ![](https://qcloudimg.tencent-cloud.cn/raw/a169918e0a4deef31193c7c08be02d59.png)




### 查询 Topic

您可以在 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 页右上角的搜索框中，通过 Topic 名称进行搜索查询，DIP 将会模糊匹配并呈现搜索结果。

### 编辑 Topic

1. 在 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 中，找到需要编辑的 Topic ，单击操作栏中的**编辑**。
2. 在弹出的对话框中可以对 Topic 的备注，分区数和消息保留时间进行修改。
3. 单击**提交**即完成对 Topic 的编辑。

### 发送消息

DIP 控制台支持手动发送消息，在控制台进行相应的操作即可实现消息发送给指定的 Topic 。

1. 在 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 中，找到需要发送消息的 Topic ，单击操作列中的**发送消息**。
2. 在弹出的对话框中输入消息内容和消息 key，同时您也可以将消息发送到指定分区。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a10f1d3217c8ac24346b17ecd8747711.png)
3. 单击**提交**，完成消息的发送。消息发送后即可被 Topic 下的任意订阅者消费。
>?DIP Topic 创建完成后，可以连接本地客户端并收发消息。详情操作请参见 [SDK 文档](https://cloud.tencent.com/document/product/1591/77139)。

[](id:new_subscription)
### 新增订阅

DIP 控制台支持手动创建订阅，在控制台进行相应的操作后即可完成订阅的创建。

1. 在 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 中，找到需要创建订阅的 Topic ，单击 Topic 的 ID 进入 Topic 基本信息页面。
2. 在页面上方选择**订阅关系**页签，单击**新建订阅关系**，在弹出的对话框中输入消费者名称。
   ![](https://qcloudimg.tencent-cloud.cn/raw/38ed4f0bcfc2c5036ff58347f2cdf314.png)
3. 单击**提交**完成创建，即可在列表中看到刚刚创建的订阅。





### 删除 Topic

>!删除了 Topic 之后也会清除该 Topic 下积累的未消费消息，请谨慎执行。

1. 在 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 中，找到需要删除的 Topic ，单击操作列中的**删除**。
2. 在弹出的提示框中，单击**提交**，完成删除。
   ![](https://qcloudimg.tencent-cloud.cn/raw/7bf671ef5fe64662d9977d685a319eb3.png)
