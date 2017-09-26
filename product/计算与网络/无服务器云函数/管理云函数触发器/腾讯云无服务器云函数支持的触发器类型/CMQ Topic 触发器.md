用户可以编写 SCF 函数来处理 CMQ Topic 主题队列中收到的消息。CMQ Topic 可将消息传递给 SCF 函数并将消息内容和相关信息作为参数来调用该函数。

CMQ Topic 主题队列触发器具有以下特点：

- Push 模型：CMQ Topic 主题队列在接受到消息后，会将消息推送给所有订阅该主题的订阅者，配置了触发 SCF 函数的情况下，函数也会被作为订阅者接收到队列的推送。在推模型中，CMQ Topic 主题队列会保存对 SCF 云函数的事件源映射。
- 异步调用：CMQ Topoic 主题队列始终使用异步调用类型来调用函数，结果不会返回给调用方。有关调用类型的更多信息，请参阅[调用类型](https://www.qcloud.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B)。

## CMQ Topic 主题队列触发器属性

- CMQ Topic（必选）：配置的 CMQ Topic 主题队列，仅支持选择同地域下的 CMQ 队列。

## CMQ Topic 触发器绑定限制
 
由于 CMQ Topic 主题队列，在单个 Topic 下最多支持 100 个订阅者。因此在 SCF 云函数触发器绑定时，如果达到此限制，可能绑定失败。在未达到此限制前，一个 Topic 下可以绑定多个 SCF 云函数。

同时，目前 CMQ Topic 触发器仅支持同地域 CMQ Topic 消息发，即广州区创建的 SCF 函数，在配置 CMQ Topic 触发器时，仅支持选择广州区（华南）的 CMQ Topic。如果您想要使用特定地域的 CMQ Topic 消息来触发 SCF 函数，可以通过在对应地域下创建函数来实现。

## CMQ Topic 触发器的事件消息结构
在指定的 CMQ Topic 主题队列接受到消息时，会将类似以下的 JSON 格式事件数据发送给绑定的 SCF 函数。

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
        "msgTag": ["tag1","tag2"]
      }
    }
  ]
}
```