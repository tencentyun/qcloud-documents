
## API概览

### 实例相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| [设置实例属性](/doc/api/431/5832) | CreateQueue|用于在用户账户下创建一个新队列。|
| [获取实例属性](/doc/api/431/5834)  | GetQueueAttributes|用于获取某个已创建队列的属性。|
| [获取实例列表](/doc/api/431/5835) | SetQueueAttributes | 用于修改消息队列的属性。|
| [删除日志](/doc/api/431/5841) | BatchDeleteMessage | 用于批量删除已经被消费过的消息。|


### 主题相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [创建主题](/doc/api/431/5837) | SendMessage| 用于发送一条消息到指定的队列。|
| [删除主题](/doc/api/431/5838) | BatchSendMessage | 用于发送批量消息到指定的队列。|
| [修改主题属性](/doc/api/431/5839)  | ReceiveMessage| 用于消费队列中的一条消息。|
| [获取主题属性](/doc/api/431/5924) | BatchReceiveMessage | 用于消费队列中的多条消息。|
| [获取主题列表](/doc/api/431/5840) | DeleteMessage | 用于删除已经被消费过的消息。|
| [增加分区](/doc/api/431/5841) | BatchDeleteMessage | 用于批量删除已经被消费过的消息。|

### 访问控制相关接口
| [增加主题白名单](/doc/api/431/5841) | BatchDeleteMessage | 用于批量删除已经被消费过的消息。|
| [删除主题白名单](/doc/api/431/5841) | BatchDeleteMessage | 用于批量删除已经被消费过的消息。|
