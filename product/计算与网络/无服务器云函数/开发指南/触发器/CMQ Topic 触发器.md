用户可以编写云函数来处理 CMQ Topic 主题队列中收到的消息。CMQ Topic 可将消息传递给云函数并将消息内容和相关信息作为参数来调用该函数。

CMQ Topic 主题队列触发器具有以下特点：

- **Push 模型**：CMQ Topic 主题队列在接受到消息后，会将消息推送给所有订阅该主题的订阅者，配置了触发云函数的情况下，函数也会被作为订阅者接收到队列的推送。在推模型中，CMQ Topic 主题队列会保存对云函数的事件源映射。
- **异步调用**：CMQ Topoic 主题队列始终使用异步调用类型来调用函数，结果不会返回给调用方。有关调用类型的更多信息，请参阅 [调用类型](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B)。

## CMQ Topic 主题队列触发器属性
**CMQ Topic（必选）**：配置的 CMQ Topic 主题队列，仅支持选择同地域下的 CMQ 队列。

## CMQ Topic 触发器绑定限制
 
由于 CMQ Topic 主题队列，在单个 Topic 下最多支持100个订阅者。因此在云函数触发器绑定时，如果达到此限制，可能绑定失败。在未达到此限制前，一个 Topic 下可以绑定多个云函数。

同时，目前 CMQ Topic 触发器仅支持同地域 CMQ Topic 消息触发，即广州区创建的云函数，在配置 CMQ Topic 触发器时，仅支持选择广州地区（华南）的 CMQ Topic。如果您想要使用特定地域的 CMQ Topic 消息来触发云函数，可以通过在对应地域下创建函数来实现。

## CMQ Topic 触发器的事件消息结构
在指定的 CMQ Topic 主题队列接受到消息时，会将类似以下的 JSON 格式事件数据发送给绑定的云函数。

```
{
  "Records": [
    {
      "CMQ": {
        "type": "topic",
        "topicOwner":120xxxxx,
        "topicName": "testtopic",
        "subscriptionName":"xxxxxx",
        "publishTime": "1970-01-01T00:00:00.000Z",
        "msgId": "123345346",
        "requestId":"123345346",
        "msgBody": "Hello from CMQ!",
        "msgTag": "tag1,tag2"
      }
    }
  ]
}
```

数据结构内容详细说明如下：

|    结构名    | 内容 |
| ---------- | --- |
| Records |  列表结构，可能有多条消息合并在列表中 |
| CMQ       |  标识数据结构来源为 CMQ 消息队列 |
| type | 使用 type 区分消息来源为 topic 或 queue |
| topicOwner | 记录 topic 所有者账号 ID |
| topicName |  记录 topic 名称  |
| subscriptionName | 记录云函数在 topic 处的订阅名称 |
| publishTime | 记录消息的发布时间 |
| msgId | 记录消息的唯一 ID |
| requestId | 记录消息推送的请求 ID |
| msgBody | 记录消息内容 |
| msgTag | 通过字符串记录消息标签 |
