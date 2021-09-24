## 操作场景

Topic 是 TDMQ RocketMQ 版中的核心概念。Topic 通常用来对系统生产的各类消息做一个集中的分类和管理，例如和交易的相关消息可以放在一个名为 “trade” 的 Topic 中，供其他消费者订阅。
在实际应用场景中，一个 Topic 往往代表着一个业务聚合，由开发者根据自身系统设计、数据架构设计来决定如何设计不同的 Topic。

本文档可以指导您使用 TDMQ RocketMQ 版时，利用 Topic 对消息进行分类管理。

## 前提条件

已创建好对应的命名空间。

## 操作步骤

### 创建 Topic

1. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，选择地域后，单击目标集群的ID进入集群基本信息页面。
2. 单击顶部**Topic**页签，选择命名空间后，单击**新建**进入创建 Topic 页面。
3. 在新建 Topic 对话框中，填写以下信息。
   ![](https://main.qcloudimg.com/raw/51c79615c68090464f867fe76abebe68.png)
   - Topic 名称：填写 Topic 名称（创建后不可修改），3-64个字符，只能包含字母、数字、“-”及“_”
   - 类型：选择消息类型，包括：普通、全局顺序、局部顺序（关于消息类型的说明，请参考 [消息类型](https://cloud.tencent.com/document/product/1179/44833)）
   - 说明：填写 Topic 的说明信息
4. 单击**提交**，在 Topic 列表中即可看见创建好的 Topic。

### 查看订阅的Group

1. 在 Topic 列表中，单击目标Topic的**订阅 Group 数**栏下的数字。
2. 页面跳转到 Group 列表，展示订阅该 Topic 的 Group 信息。

### 查询 Topic

您可以在 Topic 列表页右上角的搜索框中，通过 Topic 名称进行搜索查询，TDMQ RocketMQ 版将会模糊匹配并呈现搜索结果。

### 编辑 Topic

1. 在 Topic 列表中，找到需要编辑的 Topic ，单击操作栏中的**编辑**。
2. 在弹出的对话框中可以对 Topic 的说明进行编辑。
3. 单击**提交**即完成对 Topic 的编辑。

### 删除 Topic

> !删除了 Topic 之后也会清除该 Topic 下积累的未消费消息，请谨慎执行。

1. 在 Topic 列表中，找到需要删除的 Topic ，单击操作列中的**删除**。
2. 在弹出的提示框中，单击**提交**，完成删除。
