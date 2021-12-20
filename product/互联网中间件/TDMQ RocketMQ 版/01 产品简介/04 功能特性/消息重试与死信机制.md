本文主要介绍消息队列 TDMQ RocketMQ 版中消息重试与死信的机制与使用方法。

## 功能介绍

当消息第一次被消费者消费后，没有得到正常的回应，TDMQ RocketMQ 版会通过消费重试机制自动重新投递该消息，直到该消息被成功消费，当重试达到一定次数后，消息仍未被成功消费，则会停止重试，将消息投递到死信队列中。

当消息进入到死信队列中，表示 TDMQ RocketMQ 版已经无法自动处理这批消息，一般这时就需要人为介入来处理这批消息。您可以通过编写专门的客户端来订阅死信 Topic，处理这批之前处理失败的消息。

>?只有当消费模式为集群消费模式 时，Broker 才会自动进行重试，广播消费模式下不会进行重试。

出现以下三种情况会按照消费失败处理并会发起重试：

1. 消费者返回 ConsumeConcurrentlyStatus.RECONSUME_LATER。
2. 消费者返回 null。
3. 消费者主动/被动抛出异常。

## 重试次数


当消息需要重试时，TDMQ RocketMQ 中配置了如下的 messageDelayLevel 参数来设置重试次数与时间间隔。
```
messageDelayLevel=1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h
```

重试次数与重试时间间隔关系如下：

| 第几次重试 | 距离上一次重试的时间间隔 | 第几次重试 | 距离上一次重试的时间间隔 |
| :--------- | :----------------------- | :--------- | :----------------------- |
| 1          | 1秒                      | 10         | 6分钟                    |
| 2          | 5秒                      | 11         | 7分钟                    |
| 3          | 10秒                     | 12         | 8分钟                    |
| 4          | 30秒                     | 13         | 9分钟                    |
| 5          | 1分钟                    | 14         | 10分钟                   |
| 6          | 2分钟                    | 15         | 20分钟                   |
| 7          | 3分钟                    | 16         | 30分钟                   |
| 8          | 4分钟                    | 17         | 1小时                    |
| 9          | 5分钟                    | 18         | 2小时                    |

## 使用方式

使用 DefaultMQProducer 进行普通消息发送时，可以设置消息发送失败后最大重试次数，并且能够灵活的配合超时时间进行业务重试逻辑的开发，使用方式如下：
```java
/**设置消息发送失败时最大重试次数*/
public void setRetryTimesWhenSendFailed(int retryTimesWhenSendFailed) {
    this.retryTimesWhenSendFailed = retryTimesWhenSendFailed;
}

/**同步发送消息，并指定超时时间*/
public SendResult send(Message msg,
                    long timeout) throws MQClientException, RemotingException, MQBrokerException, InterruptedException {
    return this.defaultMQProducerImpl.send(msg, timeout);
}

```

例如：设置生产者在3s内没有发送成功则重试3次的示例如下。
```java
/**同步发送消息，如果3秒内没有发送成功，则重试3次*/
DefaultMQProducer producer = new DefaultMQProducer("DefaultProducerGroup");
producer.setRetryTimesWhenSendFailed(3);
producer.send(msg, 3000L);
```

