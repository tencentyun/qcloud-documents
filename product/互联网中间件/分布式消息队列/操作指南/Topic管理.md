## 操作场景

Topic 是 TDMQ Pulsar 版中的核心概念。Topic 通常用来对系统生产的各类消息做一个集中的分类和管理，例如和交易的相关消息可以放在一个名为 “trade” 的 Topic 中，供其他消费者订阅。
在实际应用场景中，一个 Topic 往往代表着一个业务聚合，由开发者根据自身系统设计、数据架构设计来决定如何设计不同的 Topic。

本文档可以指导您使用 TDMQ Pulsar 版时，利用 Topic 对消息进行分类管理。

## 前提条件

已创建好对应的命名空间。

## 操作步骤

### 创建 Topic

1. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，在左侧导航栏单击 **Topic 管理**。
2. 在 Topic 管理页面，单击**新建**，弹出新建 Topic 的对话框。
3. 在新建 Topic 对话框中，填写以下信息：
 - Topic 名称：只能包含字母、数字、“-”及“_”
 - 类型：选择消息类型，包括：普通、全局顺序、局部顺序（关于消息类型的说明，请参考 [消息类型](https://cloud.tencent.com/document/product/1179/44833)）
 - 分区数：全局顺序只有1个分区，其他为1-128个分区
 - 说明：填写 Topic 的说明信息，不超过128字符
4. 单击**保存**，在 Topic 列表中即可看见创建好的 Topic。
   ![](https://main.qcloudimg.com/raw/3a53fe8fa4ae2e0e1307b8fccf2afc8f.png)

### 查询 Topic

您可以在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 页右上角的搜索框中，通过 Topic 名称进行搜索查询，TDMQ Pulsar 版将会模糊匹配并呈现搜索结果。

### 编辑 Topic

1. 在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 中，找到需要编辑的 Topic ，单击操作栏中的**编辑**。
2. 在弹出的对话框中可以对 Topic 的分区数（全局顺序型消息只有1个分区，不可编辑）和说明进行编辑。
3. 单击**提交**即完成对 Topic 的编辑。

### 发送消息

TDMQ Pulsar 版控制台支持手动发送消息，在控制台进行相应的操作即可实现消息发送给指定的 Topic 。

1. 在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 中，找到需要编辑的 Topic ，单击操作列中的**发送消息**。
2. 在弹出的对话框中输入消息内容。消息长度不超过64KB。
   ![](https://main.qcloudimg.com/raw/2962bfe289ab88a167fb8d94feed37fe.png)
3. 单击**提交**，完成消息的发送。消息发送后即可被 Topic 下的任意订阅者消费。

### 新增订阅

TDMQ Pulsar 版控制台支持手动创建订阅，在控制台进行相应的操作后即可完成订阅的创建。
1. 在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 中，找到需要创建订阅的 Topic ，单击操作列中的**新增订阅**。
2. 在弹出的对话框中输入订阅的名称和说明。
 - 订阅名称：只能包含字母、数字、“-”及“_”
 - 自动创建重试&死信队列：可以选择是否创建重试和死信 Topic
 - 说明：不超过128字符
   ![](https://main.qcloudimg.com/raw/bc07c3f60f26b9e5521ec127cb171bea.png)
3. 单击**提交**完成创建。
   创建后可通过单击操作列的**查看订阅**，查看订阅了该 Topic 的订阅，即可在列表中看到刚刚创建的订阅。

>?
>
>- 如果选择自动创建重试和死信 Topic，TDMQ Pulsar 版会自动帮用户创建好一个重试队列和死信队列，以两个新的 Topic 呈现于 Topic 列表，分别以 “订阅名”+“RETRY” 和 “订阅名”+“DLQ” 命名。
>- 关于重试队列和死信队列的概念和用法请参考 [重试队列和死信队列](https://cloud.tencent.com/document/product/1179/44834) 文档。

### 删除 Topic

>!删除了 Topic 之后也会清除该 Topic 下积累的未消费消息，请谨慎执行。

1. 在 **Topic 管理**中，找到需要删除的 Topic ，单击操作列中的**更多** > **删除**，或者勾选多个 Topic 之后单击 Topic 列表顶部的**删除**。
2. 在弹出的提示框中，单击**提交**，完成删除。
强制删除：开启后，Topic 有订阅也可连带删除。
<img src="https://main.qcloudimg.com/raw/017f18e218e06cf617b17ecd4450f113.png" width="600">

