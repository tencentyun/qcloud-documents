本文主要介绍 TDMQ RocketMQ 版中消息过滤的功能、应用场景和使用方式。

## 功能介绍

消息过滤功能指消息生产者向 Topic 中发送消息时，设置消息属性对消息进行分类，消费者订阅 Topic 时，根据消息属性设置过滤条件对消息进行过滤，只有符合过滤条件的消息才会被投递到消费端进行消费。

消费者订阅 Topic 时若未设置过滤条件，无论消息发送时是否有设置过滤属性，Topic 中的所有消息都将被投递到消费端进行消费。

## 应用场景

通常，一个 Topic 中存放的是相同业务属性的消息，例如交易流水 Topic 包含了下单流水、支付流水、发货流水等，业务若只想消费者其中一种类别的流水，可在客户端进行过滤，但这种过滤方式会带来带宽的资源浪费。

针对上述场景，TDMQ 提供 Broker 端过滤的方式，用户可在生产消息时设置一个或者多个 Tag 标签，消费时指定 Tag 订阅。

![](https://main.qcloudimg.com/raw/32953b29d96dce605fa4a1598b3f5146.png)

## 使用方式

### 发送消息

发送消息时，每条消息必须指明 Tag。

```java
Message msg = new Message("TOPIC","TagA","Hello world".getBytes());                
```

### 订阅消息

- 订阅所有 Tag 
消费者如需订阅某 Topic 下所有类型的消息，Tag 用星号（*）表示。
```java
    consumer.subscribe("TOPIC", "*", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println(message.getMsgID());
            return Action.CommitMessage;
        }
    });                
```

- 订阅单个 Tag 
消费者如需订阅某 Topic 下某一种类型的消息，请明确标明 Tag。
```java
    consumer.subscribe("TOPIC", "TagA", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println(message.getMsgID());
            return Action.CommitMessage;
        }
    });                
```

- 订阅多个 Tag
消费者如需订阅某 Topic 下多种类型的消息，请在多个 Tag 之间用两个竖线（||）分隔。
```java
    consumer.subscribe("TOPIC", "TagA||TagB", new MessageListener() {
        public Action consume(Message message, ConsumeContext context) {
            System.out.println(message.getMsgID());
            return Action.CommitMessage;
        }
    });                      
```
