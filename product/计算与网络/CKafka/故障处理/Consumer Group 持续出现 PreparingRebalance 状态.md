## 问题概述
Consumer Group 持续出现 PreparingRebalance 的状态。


## 可能原因
1. 有新的消费者加入消费者组。
2. 当前运行消费者停止运行，离开消费者组。常见的情况如消费者重启，消费者应用崩溃，消费者进程上报的心跳超时等（详请参见 [CKafka 常用参数配置指南](https://cloud.tencent.com/document/product/597/30203)）。
3. 分区数变动的时候（增加或删除）。




## 解决方法

1和3两种情况无法避免 rebalance。正常情况，rebalance 在30s内能完成。如果出现长期的 rebalance，需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行处理。

如果是由于心跳超时或者两次 poll 时间间隔太大导致的问题，您可以调整如下参数：
```bash
# 使用 Kafka 消费分组机制时，消费者超时时间。当 Broker 在该时间内没有收到消费者的心跳时，认为该消费者故障失败，Broker 发起重新 Rebalance 过程。目前该值的配置必须在 Broker 配置group.min.session.timeout.ms=6000和group.max.session.timeout.ms=300000 之间
session.timeout.ms=10000

# 使用 Kafka 消费分组机制时，消费者发送心跳的间隔。这个值必须小于 session.timeout.ms，一般小于它的三分之一
heartbeat.interval.ms=3000

# 使用 Kafka 消费分组机制时，再次调用 poll 允许的最大间隔。如果在该时间内没有再次调用 poll，则认为该消费者已经失败，Broker 会重新发起 Rebalance 把分配给它的 partition 分配给其他消费者
max.poll.interval.ms=300000
```

如果出现一个消费者订阅了很多的 Topic，您可以尝试减少 Group 订阅 Topic 的数量。
