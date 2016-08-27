
## 队列模型

### 队列相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| 创建队列 | [CreateQueue](/doc/api/431/5832)|用于在用户账户下创建一个新队列。|
| 获取队列列表 | [ListQueue](/doc/api/431/5833)|用于列出帐号下的队列列表，可分页获取数据。|
| 获取队列属性 | [GetQueueAttributes](/doc/api/431/5834) |用于获取某个已创建队列的属性。|
| 修改队列属性 | [SetQueueAttributes](/doc/api/431/5835) | 用于修改消息队列的属性。|
| 删除队列 | [DeleteQueue](/doc/api/431/5836)| 用于删除一个已创建的队列。|


### 消息相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| 发送消息 | [SendMessage](/doc/api/431/5837)| 用于发送一条消息到指定的队列。|
| 批量发送消息 | [BatchSendMessage](/doc/api/431/5838) | 用于发送批量消息到指定的队列。|
| 消费消息 | [ReceiveMessage](/doc/api/431/5839) | 用于消费队列中的一条消息。|
| 批量消费消息 | [BatchReceiveMessage](/doc/api/431/5924) | 用于消费队列中的多条消息。|
| 删除消息 | [DeleteMessage](/doc/api/431/5840) | 用于删除已经被消费过的消息。|
| 批量删除消息 | [BatchDeleteMessage](/doc/api/431/5841) | 用于批量删除已经被消费过的消息。|



