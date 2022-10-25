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
   ![](https://qcloudimg.tencent-cloud.cn/raw/27e26efb1d41905affe40ae686d8e80c.png)
    - Topic 名称：不能为空，支持数字字母以及符号 “-\_=:.”，长度不超过128个字符。
    - Topic 类型：支持**持久化**和**非持久化**两种类型。
      - 持久化：持久化的消息会以多副本形式落盘，保证消息不丢失，多适用于金融、交易等高可靠场景。
      - 非持久化：非持久化主题的消息不会落盘，直接投递给当前在线的订阅，投递完成既删除。如果当前没有在线订阅，会直接删除，消息在服务端不保留。多适用于数据可靠性要求不高、流处理等场景（非持久化消息仅支持普通消息的即时收发，不支持消息查询、消息轨迹、延迟消息、消息过滤、消息回溯等功能）。
<dx-alert infotype="notice" title="使用注意事项：">
非持久化类型主题，在收发消息的时候，要填写完整的前缀为 `non-persistent://` 主题名。
</dx-alert>
    - 是否分区：
      - Pulsar 内部可以保证单个分区内的消息有序，即如果创建1分区的 Topic 则可以保证全局有序。
      - 单分区的 Topic 会在性能上弱于多分区 Topic，如果希望兼顾性能与有序性， 可以参见 [订阅模式](https://cloud.tencent.com/document/product/1179/44818) 使用 Key-shared 模式进行消费，实现局部有序，标记同一个 key 让需要有序的消息落在同一分区即可。
    - 说明：填写 Topic 的说明信息，不超过128字符。
4. 单击**保存**，在 Topic 列表中即可看见创建好的 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/d0328e4a60fb563b8f45a3808912de61.png)
<table>
<tr>
<th>参数	</th>
<th>说明</th>
</tr>
<tr>
<td>Topic 名称</td>
<td>Topic 名称，格式为 pulsar-****/namespace/topicName。</td>
</tr>
<tr>
<td>监控</td>
<td>单击 <img src = "https://qcloudimg.tencent-cloud.cn/raw/ac572a960433508f64f226e6ea218c10.png"> 查看 Topic 监控详情，关于监控指标说明请参见 <a href = "https://cloud.tencent.com/document/product/1179/66709">查看监控</a>。 </td>
</tr>
<tr>
<td>类型</td>
<td>消息类型，包括：普通、全局顺序、局部顺序（关于消息类型的说明，请参见 <a href = "https://cloud.tencent.com/document/product/1179/44833"><b>消息类型</b></a>）。</td>
</tr>
<tr>
<td>创建来源</td>
<td>用户创建或系统创建。</td>
</tr>
<tr>
<td>分区</td>
<td>Topic 的分区数量。</td>
</tr>
<tr>
<td>客户端</td>
<td><ul><li>生产者：生产者数量/生产者数量上限，点击可跳转至生产详情页，详情参见 <a href = "https://cloud.tencent.com/document/product/1179/66708"><b>查看生产者详情</b></a>。</li>
<li>消费者：展示消费者数量/消费者数量上限，点击可跳转至消费详情页，详情参见 <a href = "https://cloud.tencent.com/document/product/1179/44821#.E6.9F.A5.E7.9C.8B.E8.AE.A2.E9.98.85.E8.AF.A6.E6.83.85"><b>查看订阅详情</b></a>。</li></ul>
<b>说明：</b>当展示为 warning 的橙色， 代表分数数值达到80%，当展示为 Error 红色，则代表分数数值达到90%，请及时断开不需要使用的客户端链接。
</td>
</tr>
<tr>
<td>创建时间</td>
<td>Topic 的创建时间。</td>
</tr>
<tr>
<td>说明</td>
<td>Topic 的说明信息。</td>
</tr>
</table>



### 查询 Topic

您可以在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 页右上角的搜索框中，通过 Topic 名称进行搜索查询，TDMQ Pulsar 版将会模糊匹配并呈现搜索结果。

您也可以在 Topic 列表中通过**类型**和**创建来源**对 Topic 进行筛选。

### 编辑 Topic

1. 在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 中，找到需要编辑的 Topic ，单击操作栏中的**编辑**。
2. 在弹出的对话框中可以对 Topic 的分区数（全局顺序型消息只有1个分区，不可编辑）和说明进行编辑。
3. 单击**提交**即完成对 Topic 的编辑。

### 发送消息

TDMQ Pulsar 版控制台支持手动发送消息，在控制台进行相应的操作即可实现消息发送给指定的 Topic 。

1. 在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 中，找到需要发送消息的 Topic ，单击操作列中的**发送消息**。
2. 在弹出的对话框中输入消息内容。消息长度不超过64KB。
   ![](https://main.qcloudimg.com/raw/2962bfe289ab88a167fb8d94feed37fe.png)
3. 单击**提交**，完成消息的发送。消息发送后即可被 Topic 下的任意订阅者消费。





### 新增订阅

TDMQ Pulsar 版控制台支持手动创建订阅，在控制台进行相应的操作后即可完成订阅的创建。

1. 在 [Topic 管理](https://console.cloud.tencent.com/tdmq/topic) 中，找到需要创建订阅的 Topic ，单击操作列中的**新增订阅**。
2. 在弹出的对话框中输入订阅的名称和说明。
 - 订阅名称：长度不超过64个字符
 - 自动创建重试&死信队列：可以选择是否自动创建重试和死信 Topic
 - 说明：不超过2字符
![](https://qcloudimg.tencent-cloud.cn/raw/97151a4e137b3688f7a2753b78bea89f.png)
3. 单击**提交**完成创建。
   创建后可通过单击操作列的**查看订阅**，查看订阅了该 Topic 的订阅，即可在列表中看到刚刚创建的订阅。

>?
>
>- 如果选择自动创建重试和死信 Topic，TDMQ Pulsar 版会自动帮用户创建好一个重试队列和死信队列，以两个新的 Topic 呈现于 Topic 列表，分别以 “订阅名”+“RETRY” 和 “订阅名”+“DLQ” 命名。
>- 关于重试队列和死信队列的概念和用法请参见 [重试队列和死信队列](https://cloud.tencent.com/document/product/1179/44834)。

### 删除 Topic

>!删除了 Topic 之后也会清除该 Topic 下积累的未消费消息，请谨慎执行。

1. 在 **Topic 管理**中，找到需要删除的 Topic ，单击操作列中的**更多** > **删除**，或者勾选多个 Topic 之后单击 Topic 列表顶部的**删除**。
2. 在弹出的提示框中，单击**提交**，完成删除。
   强制删除：开启后，Topic 有订阅也可连带删除。
   <img src="https://main.qcloudimg.com/raw/017f18e218e06cf617b17ecd4450f113.png" width="600">
