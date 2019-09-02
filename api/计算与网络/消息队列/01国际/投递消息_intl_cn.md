## 1. Queue Endpoint 订阅

CMQ 会将发布主题的消息原文，推送到订阅的队列Queue中，从而消费者可以从Queue中读取到相应的消息。

## 2. Http Endpoint 订阅

### 1. 投递描述
CMQ 通过发送 POST 请求将主题消息推送到订阅的 Http Endpoint 端，消息格式支持两种：JSON 格式和 SIMPLIFIED 精简格式。

JSON 格式：推送的 Http 请求 Body 包含消息的正文和消息的属性信息。

SIMPLIFIED 格式：推送的 Http 请求 Body 即为消息正文，而 msgId 等信息会在 Http 请求 Header 中传递给订阅方。

订阅方的 Http 服务返回标准的 2xx 响应（例如，200），代表投递成功，否则，投递失败，并触发重试投递策略；超时不响应，CMQ 也会认为失败，同样触发重试投递策略，检测超时时间约为15秒。

### 2. 投递的 Http 请求 Header
| 参数名称 | 描述 |
|---------|-------|
| x-cmq-request-id | 此次推送消息的 requestId |
| x-cmq-message-id | 此次推送消息的 msgId |
| x-cmq-message-tag | 此次推送消息的消息标签 |

### 3. 投递的 Http 请求 Body
- 在 JSON 格式下，Http Body 包含消息的正文和消息的属性信息。

| 参数名称 | 类型 | 描述 |
|---------|-------|-------|
| TopicOwner |String| 被订阅的主题拥有者的appId |
| topicName |String| 主题名称 |
| subscriptionName |String| 订阅名称 |
| msgId |String| 消息id |
| msgBody |String| 消息正文 |
| publishTime |Int| 消息的发布时间 |

- 在 SIMPLIFIED 格式下，Http Body 即为发布者发布的消息正文

### 4. 投递的 Http 请求响应
订阅方 Http 服务正常处理投递消息，返回 2xx 响应；其他响应码或者超时不响应，当作错误，并触发重试投递策略。

### 5. 请求示例
例如，订阅的 Http Endpoint 为：```http://test.com/cgi```

JSON 格式：

```
POST /cgi HTTP/1.1
Host: test.com
Content-Length: 761
Content-Type: text/plain
User-Agent: Qcloud Notification Service Agent
x-cmq-request-id: 2394928734
x-cmq-message-id: 6942316962
x-cmq-message-tag: a, b

{"TopicOwner":100015036,"topicName":"MyTopic","subscriptionName":"mysubscription","msgId":"6942316962","msgBody":"test message","publishTime":11203432}

```

SIMPLIFIED 格式：

```
POST /cgi HTTP/1.1
Host: test.com
Content-Length: 123
Content-Type: text/plain
User-Agent: Qcloud Notification Service Agent
x-cmq-request-id: 2394928734
x-cmq-message-id: 6942316962
x-cmq-message-tag: a, b

test message
```
