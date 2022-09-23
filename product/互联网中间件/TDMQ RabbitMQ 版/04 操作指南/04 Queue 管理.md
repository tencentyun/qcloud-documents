## 操作场景

队列（Queue）用于存储消息，每个消息都会被投入到一个或多个 Queue 里，Producer 生产消息并最终投递到 Queue 中，Consumer 可以从 Queue 中拉取消息进行消费。

多个 Consumer 可以订阅同一个 Queue，这时 Queue 中的消息会被平均分摊给多个 Consumer 进行处理，而不是每个 Consumer 都收到所有的消息并处理。

该任务指导您使用消息队列 TDMQ RabbitMQ 版时在控制台上创建，删除和查询 Queue。

## 前提条件

需要提前创建好对应的 Vhost。

## 操作步骤

### 创建 Queue

1. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，选择地域后，单击目标集群的 ID 进入集群基本信息页面。
2. 单击顶部 **Queue** 页签，选择Vhost后，单击**新建**进入创建 Queue 页面。
3. 填写 Queue 相关信息。
   ![](https://main.qcloudimg.com/raw/dfabbd7014042b368168621ff6ebd10e.png)
   - Queue 名称：填写 Queue 名称（创建后不可修改），3-64个字符，只能包含字母、数字、“-”及“_”
   - 自动清除：开启后，最后一个消费者取消订阅后立即删除该 Queue。
   - Queue 说明：填写 Queue 说明，最多128个字符。
4. 单击**提交**，完成 Queue 创建。

### 查看 Queue 详情

在 **Queue** 列表，单击 Queue 左边的右三角，可查看该 Queue 的详情。

您可以看到：

- 基本信息（消息堆积、自动删除、创建时间和在线消费者）
- 消费者列表：展示订阅该 Queue 的消费者信息

![](https://main.qcloudimg.com/raw/a7d78cc58efadfb614b890cc33d08632.png)

### 查看绑定关系

在 Queue 列表中，单击目标 Queue 操作列的**查看绑定关系**，可查看与该 Queue 绑定的路由关系。

### 编辑 Queue

1. 在 Queue 列表中，单击目标 Queue 操作列的**编辑**。
2. 在弹窗中，对 Queue 信息进行编辑。
3. 单击**提交**，完成修改。

### 删除 Queue

> !Queue 删除后，该 Queue 下的所有配置将会被清空，且无法恢复。

1. 在 Queue 列表中，找到需要删除的 Queue，单击操作列的**删除**。
2. 在弹出的提示框中，单击**删除**，完成删除。
