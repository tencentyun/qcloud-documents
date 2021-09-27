

为了适用不同场景的需求，TDMQ Pulsar 版提供多种订阅方式。订阅可以灵活组合出很多可能性：
- 如果您想实现传统的 “发布-订阅消息”形式 ，可以让每个消费者都有一个唯一的订阅名称（独占）。
- 如果您想实现传统的“消息队列” 形式，可以使多个消费者使用同一个的订阅名称（共享、灾备）。
- 如果您想同时实现以上两点，可以让一些消费者使用独占方式，剩余消费者使用其他方式。

![](https://main.qcloudimg.com/raw/ab3396672d1e49642485686f2df3f479.png)

## 独占模式（Exclusive）
如果两个及以上的消费者尝试以同样方式去订阅主题，消费者将会收到错误，适用于全局有序消费的场景。
```java
 Consumer<byte[]> consumer1 = client.newConsumer()
                .subscriptionType(SubscriptionType.Exclusive)
                .topic(topic)
                .subscriptionName(groupName)
                .subscribe();
//consumer1启动成功
 Consumer<byte[]> consumer2 = client.newConsumer()
                .subscriptionType(SubscriptionType.Exclusive)
                .topic(topic)
                .subscriptionName(groupName)
                .subscribe();
//consumer2启动失败
```

## 灾备模式（Failover）
consumer 将会按字典顺序排序，第一个 consumer 被初始化为唯一接受消息的消费者。 
```java
 Consumer<byte[]> consumer1 = client.newConsumer()
                .subscriptionType(SubscriptionType.Failover)
                .topic(topic)
                .subscriptionName(groupName)
                .subscribe();
//consumer1启动成功
 Consumer<byte[]> consumer2 = client.newConsumer()
                .subscriptionType(SubscriptionType.Failover)
                .topic(topic)
                .subscriptionName(groupName)
                .subscribe();
//consumer2启动成功
```
当 master consumer 断开时，所有的消息（未被确认和后续进入的）将会被分发给队列中的下一个 consumer。

## 共享模式（Shared）
消息通过 round robin 轮询机制（也可以自定义）分发给不同的消费者，并且每个消息仅会被分发给一个消费者。当消费者断开连接，所有被发送给他，但没有被确认的消息将被重新安排，分发给其它存活的消费者。
```java
 Consumer<byte[]> consumer = client.newConsumer()
                .subscriptionType(SubscriptionType.Shared)
                .topic(topic)
                .subscriptionName(groupName)
                .subscribe();
```
