本文主要介绍消息队列 TDMQ RocketMQ 版中集群消费和广播消费的概念定义和适用场景。

## 功能介绍

- 集群消费：当使用集群消费模式时，任意一条消息只需要被集群内的任意一个消费者处理即可。
- 广播消费：当使用广播消费模式时，每条消息会被推送给集群内所有注册过的消费者，保证消息至少被每个消费者消费一次。

## 应用场景

集群消费：适用于每条消息只需要被处理一次的场景。

广播消费：适用于每条消息需要被集群下每一个消费者处理的场景。

## 代码示例

- **集群订阅**
同一个 Group ID 所标识的所有 Consumer 平均分摊消费消息。例如某个 Topic 有9条消息，一个Group ID 有3个 Consumer 实例，那么在集群消费模式下每个实例平均分摊，只消费其中的3条消息。
```java
// 集群订阅方式设置（不设置的情况下，默认为集群订阅方式）。
properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.CLUSTERING);
```

- **广播订阅**
同一个 Group ID 所标识的所有 Consumer 都会各自消费某条消息一次。例如某个 Topic 有9条消息，一个 Group ID 有3个 Consumer 实例，那么在广播消费模式下每个实例都会各自消费9条消息。
```java
// 广播订阅方式设置。
properties.put(PropertyKeyConst.MessageModel, PropertyValueConst.BROADCASTING);               
```
>?请确保同一个 Group ID 下所有 Consumer 实例的订阅关系保持一致。





  
