## 操作场景

生产者将消息发送到 Exchange 中，Exchange 根据消息的属性或内容将消息路由到一个或多个 Queue 中（或者丢弃），Consumer从 Queue 中拉取消息进行消费。

该任务指导您使用消息队列 TDMQ RabbitMQ 版时在控制台上创建，删除和查询 Exchange。

## 前提条件

已创建好对应的 Vhost（参考 [创建 Vhost](https://cloud.tencent.com/document/product/1495/61833)）。

## 操作步骤

### 创建 Exchange

1. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，选择地域后，单击目标集群的 ID 进入集群基本信息页面。
2. 单击顶部 **Exchange** 页签，选择 Vhost 后，单击**新建**进入创建 Exchange 页面。
3. 在新建 Exchange 对话框中，填写以下信息。
   ![](https://main.qcloudimg.com/raw/a05cf17275616133497dd8334e39fd05.png)
   - Exchange 名称：填写 Exchange 名称（创建后不可修改），3-64个字符，只能包含字母、数字、“-”及“_”
   - 路由类型：选择路由类型，包括：Direct、Fanout、Topic，路由类型选择后不可修改（关于路由类型的详细说明，请参考 [Exchange](https://cloud.tencent.com/document/product/1495/61834)）
     - Direct：该类型 Exchange 会把消息路由到 RoutingKey 和 BindingKey 完全匹配的 Queue 中
     - Fanout：该类型 Exchange 会将消息路由到所有与其绑定的 Queue 中
     - Topic：该类型 Exchange 支持多条件匹配和模糊匹配，即使用 Routing Key 模式匹配和字符串比较的方式将消息路由至与其绑定的 Queue 中
   - Exchange 说明：填写 Exchange 的说明信息，最多128个字符
4. 单击**提交**，在 Exchange 列表中即可看见创建好的 Exchange。

### 编辑 Exchange

1. 在 Exchange 列表中，找到需要编辑的 Exchange ，单击操作栏中的**编辑**。
2. 在弹出的对话框中可以对 Exchange 的说明进行编辑。
3. 单击**提交**即完成对 Exchange 的编辑。

### 删除 Exchange

> !Exchange 删除后，该 Exchange 下的所有配置将会被清空，且无法恢复。

1. 在 Exchange 列表中，找到需要删除的 Exchange ，单击操作列中的**删除**。
2. 在弹出的提示框中，单击**删除**，完成删除。
