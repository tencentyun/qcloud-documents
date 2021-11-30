普通消息被发送到普通消息队列时， 初始状态为 **Active**，当其被取走后在 VisibilityTimeout 的时间内状态为 **Inactive**，若超过 VisibilityTimeout 时间后消息还未被删除，消息会重新变成 **Active** 状态；如果在 VisibilityTimeout 时间内被删除，消息状态将变为 **Deleted**。消息的最长存活时间由创建队列时指定的 MessageRetentionPeriod 属性值决定， 超过此时间后消息状态变成 **Expired** 并将被回收。

消费者只能取到处于 **Active** 状态的消息。这保证了同一条消息不会同时被多次消费，但可被顺序性地多次消费。

![](https://main.qcloudimg.com/raw/063f581951bdf7a4fef8706fd8a878ad.jpg)

- Component 1 将 Message A 发送到一个队列，该消息在 TDMQ CMQ 版服务器间提供多份冗余。

- 当 Component 2 准备好处理消息时，就从队列检索消息，然后 Message A 返回。在 Message A 处理期间，它仍然停留在队列中，在**取出消息隐藏时长**阶段，其他业务不可获取 Message A。

- Component 2 可从队列删除 Message A，以避免一旦**取出消息隐藏时长**过期后该消息被再次接受并处理；也可以不删除 Message A，该消息可以被其他业务多次消费。
