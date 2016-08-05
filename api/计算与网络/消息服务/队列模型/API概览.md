
## 1. 队列相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 创建队列 | [CreateQueue]() | 用于在用户账户下创建一个新队列。
| 修改队列属性 | [SetQueueAttributes]() | 用于修改消息队列的属性。
| 获取队列属性 | [GetQueueAttributes]() | 用于获取某个已创建队列的属性。
| 删除队列 | [DeleteQueue]() | 用于删除一个已创建的队列。
| 获取队列列表 | [ListQueue]() | 用于列出帐号下的队列列表，可分页获取数据。

## 2. 消息相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 发送消息 | [SendMessage]() |  用于发送一条消息到指定的队列。
| 批量发送消息 | [BatchSendMessage]() |  用于发送批量消息到指定的队列。
| 消费消息 | [ReceiveMessage]() |  用于消费队列中的一条消息。
| 批量消费消息 | [BatchReceiveMessage]() |  用于消费队列中的多条消息。
| 删除消息 | [DeleteMessage]() |  用于删除已经被消费过的消息。
| 批量删除消息 | [BatchDeleteMessage]() |  用于批量删除已经被消费过的消息。



