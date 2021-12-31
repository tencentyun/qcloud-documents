RabbitMQ 客户端支持的接口列表如下：

| 接口                   | 说明                                                     |
| ---------------------- | -------------------------------------------------------- |
| exchangeDeclare        | 声明一个 Exchange，没有则创建。                          |
| exchangeDeclareNoWait  | 声明一个 Exchange，没有则异步创建。                      |
| exchangeDeclarePassive | 声明一个 Exchange，没有则报异常。                         |
| exchangeDelete         | 删除 Exchange。                                          |
| exchangeUnbindNoWait   | 异步取消绑定。                                           |
| queueDeclare           | 声明一个 Queue，没有则创建。                             |
| queueDeclareNoWait     | 声明一个 Queue，没有则异步创建。                         |
| queueDeclarePassive    | 声明一个 Queue，没有则报异常。                           |
| queueDelete            | 删除 Queue。                                             |
| queueBind              | 声明 Queue 和某一 Exchange 的绑定关系，没有则绑定。      |
| queueBindNoWait        | 声明 Queue 和某一 Exchange 的绑定关系，没有则异步绑定。  |
| queuePurge             | 重置消费位点，从最新消费（原生 RabbitMQ 相应为删除消息）。 |
| queueUnbind            | 取消绑定。                                               |
| queueUnbindNoWait      | 异步取消绑定。                                           |

