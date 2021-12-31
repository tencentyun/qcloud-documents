本文主要介绍消息队列 TDMQ RocketMQ 版中定时与延迟消息的概念和使用方式。

## 相关概念

- **定时消息**：消息在发送至服务端后，实际业务并不希望消费端马上收到这条消息，而是推迟到某个时间点被消费，这类消息统称为定时消息。
- **延时消息**：消息在发送至服务端后，实际业务并不希望消费端马上收到这条消息，而是推迟一段时间后再被消费，这类消息统称为延时消息。

实际上，延时消息可以看成是定时消息的一种特殊用法，其实现的最终效果和定时消息是一致的。

## 使用方式

开源 Apache RocketMQ 没有提供让用户自由设定延时时间的 API 的，TDMQ RocketMQ 版为了保证向开源 RocketMQ Client 的兼容，设计了一种通过添加 message 的 property 键值对来指定消息发送时间的方法。该方法只要在需要定时发送消息的 `property` 属性中增加 `__STARTDELIVERTIME` 属性值，就能在一定范围内（40天）实现该消息在任意时间的定时发送。延时消息则可以先通过计算得到定时发送的时间点，再以定时消息的形式发送。

下面给出一段具体代码示例来展示如何使用 TDMQ RocketMQ 版的定时和延时消息，[查看完整示例 >>](https://github.com/streamnative/rop/blob/master/examples/src/main/java/org/streamnative/rocketmq/example/delaymessage/DelayProduceDemo.java)

### 定时消息

定时消息直接在 message 发送前写入标准毫秒化的时间戳到  `__STARTDELIVERTIME` 属性即可。

```java
Message msg = new Message("test-topic", ("message content").getBytes(StandardCharsets.UTF_8));
// 设定消息在 2021-10-01 00:00:00 被发送
try {
    long timeStamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").parse("2021-10-01 00:00:00").getTime();
    //将 __STARTDELIVERTIME 设定到 msg 的属性中
    msg.putUserProperty("__STARTDELIVERTIME", String.valueOf(timeStamp));
    SendResult result = producer.send(msg);
    System.out.println("Send delay message: " + result);
} catch (ParseException e) {
    //TODO 添加对 Timestamp 解析失败的处理方法
    e.printStackTrace();
}
```

### 延时消息

延时消息先通过 `System.currentTimeMillis() + delayTime` 计算得到定时发送的时间点，再以定时消息的方式发送。

```java
Message msg = new Message("test-topic", ("message content").getBytes(StandardCharsets.UTF_8));

// 设定消息在10秒之后被发送
long delayTime = System.currentTimeMillis() + 10000;
// 将 __STARTDELIVERTIME 设定到 msg 的属性中
msg.putUserProperty("__STARTDELIVERTIME", String.valueOf(delayTime));

SendResult result = producer.send(msg);
System.out.println("Send delay message: " + result);
```



## 使用限制

- 使用延时消息时，请确保客户端的机器时钟和服务端的机器时钟（所有地域均为UTC+8 北京时间）保持一致，否则会有时差。
- 定时和延时消息在精度上会有1秒左右的偏差。
- 关于定时和延时消息的时间范围，最大均为40天。
- 使用定时消息时，设置的时刻在当前时刻以后才会有定时效果，否则消息将被立即发送给消费者。
- 该延时消息在使用方式上不兼容 RocketMQ ONS 客户端的延时消息，但实现效果可以做到一致。
