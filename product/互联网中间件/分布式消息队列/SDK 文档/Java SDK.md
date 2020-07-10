## 操作场景
TDMQ 提供了 Java 语言的 SDK 来调用服务，进行消息队列的生产和消费。
本文主要介绍 Java SDK 的使用方式，提供代码编写示例，帮助工程师快速搭建 TDMQ 测试工程。

## 前提条件
- 已完成 Java SDK 的下载和安装（参考 [Java SDK 下载方式](https://cloud.tencent.com/document/product/1179/44914)）。
- 已获取调用地址（URL）和路由 ID（NetModel）。
这两个参数均可以在【[环境管理](https://console.cloud.tencent.com/tdmq/env)】的接入点列表中获取，路由 ID 即`netModel`，地址即`URL`。请根据客户端部署的云服务器或其他资源所在的私有网络选择正确的接入点来复制参数信息，否则会有无法连接的问题。![](https://main.qcloudimg.com/raw/4edd20db5dabb96bbc42df441a5bebdf.png)
- 已在 API 密钥管理页面获取 SecretID 和 SecretKey。
  - SecretID 用于标识 API 调用者的身份。
  - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，SecretKey 需妥善保管，避免泄露。

## 操作步骤
### 创建 Client

```java
  Map<String, String> authParams = new HashMap<>();
  authParams.put("secretId", "***********************************************");
  authParams.put("secretKey", "***********************************************");
  authParams.put("ownerUin", "***************");//主账号
  authParams.put("uin", "****************");//子账号
  authParams.put("region", "ap-guangzhou");//地域信息
  PulsarClient client = PulsarClient.builder().authenticationCloud(
           "org.apache.pulsar.client.impl.auth.AuthenticationCloudCam", authParams)
           .netModelKey("1300*****0/vpc-******/subnet-********")#填写接入点的路由ID
           .serviceUrl("pulsar://*.*.*.*:6000")#填写接入点的地址
	   .build();
 ```
 
关于其中 authParam 参数的详细说明，请参考 [认证字段说明](#cam)。

### 生产消息
创建好 Client 之后，通过创建一个 Producer，就可以生产消息到指定的 Topic 中。

```java
Producer<byte[]> producer = client.newProducer().topic("persistent://1300****30/default/mytopic").create();
producer.send("My message".getBytes());
```
Topic 名称需要填入完整路径，即“persistent://appid/environment/Topic”，appid/environment/topic 的部分可以从控制台上【[Topic管理](https://console.cloud.tencent.com/tdmq/topic)】页面直接复制。![](https://main.qcloudimg.com/raw/5a1fe96ea23b1d4906b7067a3abfd7b5.png)

这种生产方式是阻塞的方式生产消息到指定的 Topic 中，我们还可以使用异步发送的方式生产消息。
```java
    producer.sendAsync("my-async-message".getBytes()).thenAccept(msgId -> {
    	System.out.printf("Message with ID %s successfully sent", msgId);
    });
```

TDMQ 的消息中除了可以保存消息体之外，还可以设置其他的消息属性。
```java
producer.newMessage()
	.key("my-message-key")//默认相同key路由到同一个partition中
	.value("my-async-message".getBytes())
	.property("my-key", "my-value")
	.property("my-other-key", "my-other-value")
	.send();
```

消息延迟传递：
```java
producer.newMessage().deliverAfter(3L, TimeUnit.Minute).value("Hello Tdmq!").send();
```

设置消息标签（TAG）：
```java
producer.newMessage()
	.key("my-message-key")
	.value("my-sync-message".getBytes())
	//支持设置多个标签
	.tags("TagA", "TagB","TagC")
	.send();
```

路由模式：

| Mode   |   Description |
| ------------ | ------------ |
|   RoundRobinPartition |  如果消息没有指定 key，为了达到最大吞吐量，消息会以 round-robin 方式被路由所有分区。 请注意 round-robin 并不是作用于每条单独的消息，而是作用于延迟处理的批次边界，以确保批处理有效。 如果为消息指定了 key，发往分区的消息会被分区生产者根据 key 做 hash，然后分散到对应的分区上。 这是默认的模式。 |
|   SinglePartition |  如果消息没有指定 key，生产者将会随机选择一个分区，并发送所有消息。 如果为消息指定了 key，发往分区的消息会被分区生产者根据 key 做 hash，然后分散到对应的分区上。 |
|   CustomPartition  |  使用自定义消息路由，可以定制消息如何进入特定的分区。 可以使用 Java client 或实现 MessageRouter 接口来实现自定义的路由模式。|

顺序保证：

| 顺序保证  | Description  |路由策略与消息 Key|
| ------------ | ------------ |------------ |
|每个 key 分区   |  所有具有相同 key 的消息将按顺序排列并放置在相同的分区（Partition）中。 |自同一生产者的所有消息都是有序的|
|  同一个生产者 |自同一生产者的所有消息都是有序的   |自同一生产者的所有消息都是有序的|

### 订阅消息

#### Consumer
##### 通过指定 Topic 和订阅名进行消费消息
- 主动拉取
```java
Consumer consumer = client.newConsumer()
	.topic("persistent://1300****30/default/mytopic")
	//.subscriptionType(SubscriptionType.Shared)
	//.enableRetry(true)默认关闭，如果需要重试则开启
	.subscriptionName("my-subscription")
	.subscribe();
while (true) {
  //等待接收消息
  Message msg = consumer.receive();
  try {
  	  System.out.printf("Message received: %s", new String(msg.getData()));
      //消息ACK
  	  consumer.acknowledge(msg);   
  } catch (Exception e) {
    //处理出错
	// enableRetry=true 才能使用重试方法
	consumer.reconsumeLater(msg, 1000L, TimeUnit.MILLISECONDS);//消息按照指定的延迟时间重试
	//consumer.reconsumeLater(msg);按照延迟等级进行重试，多次重试默认自增延迟等级
    //consumer.reconsumeLater(msg, 1);按照指定的延迟等级进行重试
	//delayLevel =1 代表1s,
	//delayLevel =2 代表5s,
	//默认延迟等级"1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h"
  }
}
```

- 被动接收
```java
Consumer<byte[]> consumer = client.newConsumer()
   .topic("persistent://1300****30/default/mytopic")
   .messageListener(new  MessageListener<byte[]> () {
          @Override
           public void received(Consumer<byte[]> consumer, Message<byte[]> msg) {
                   //处理消息
            }
     })
	.subscriptionName("my-subscription")
	.subscribe();
```

- 指定标签（TAG） 
```java
Consumer consumer = client.newConsumer()
		.topicByTag(”persistent://1300****30/default/mytopic“, "TagA || TagB")
		//.topic(”my-topic“, "*") 订阅所有
		//.topicByTagsPattern(”my-topic“, "Tag.*")正则表达式
		.subscriptionName("my-subscription")
		.subscriptionType(SubscriptionType.Shared)
		.subscribe();
```

##### 异步订阅

```java
CompletableFuture<Message> msg = consumer.receiveAsync();
// 处理消息
System.out.printf("Message received: %s", new String(msg.get().getData()));
```

##### 批量订阅

```java
Consumer consumer = client.newConsumer() 
	.topic("persistent://1300****30/default/mytopic") 
	.subscriptionName("my-subscription") 
	.batchReceivePolicy(BatchReceivePolicy.builder() 
	.maxNumMessages(100) 
	.maxNumBytes(1024 * 1024) 
	.timeout(200, TimeUnit.MILLISECONDS) 
	.build()) 
	.subscribe(); 
Messages messages = consumer.batchReceive();
for (message in messages) {
  // 处理消息
}
consumer.acknowledge(messages)
```

##### 多主题订阅
- 订阅指定的 Topic 列表：
```java
List<String> topics = Arrays.asList(
        "persistent://1300****30/default/mytopic1",
        "persistent://1300****30/default/mytopic2",
        "persistent://1300****30/default/mytopic3"
);
Consumer multiTopicConsumer = consumerBuilder
        .topics(topics)
        .subscribe();
```

- 订阅一个 namaspace (即控制台中的环境)下的所有 Topic：
```java
Pattern allTopicsInNamespace = Pattern.compile("persistent://1300****30/default/.*");
Consumer allTopicsConsumer = consumerBuilder
	.topicsPattern(allTopicsInNamespace)
	.subscribe();
```

- 通过一个正则表达式订阅一个 namaspace (即控制台中的环境)下匹配的 Topic：
```java
Pattern someTopicsInNamespace = Pattern.compile("persistent://1300****30/default/foo.*");
Consumer allTopicsConsumer = consumerBuilder
        .topicsPattern(someTopicsInNamespace)
        .subscribe();
```
>!这种方式只支持匹配同一个环境（Namespace）下的 Topic，Namespace不能做正则匹配。

#### Reader
通过 Reader 的订阅模式，可以从指定的消息开始读取消息。

```java
ReaderConfiguration conf = new ReaderConfiguration();
byte[] msgIdBytes = // 消息ID 的字节数组
MessageId id = MessageId.fromByteArray(msgIdBytes);
Reader reader = pulsarClient.newReader()
        .topic(topic)
        .startMessageId(id)
        .create();

while (true) {
    Message message = reader.readNext();
    // 处理消息
}
```

### 关闭链接

生产和消费数据完成之后，注意需要关闭链接，包括 Consumer 和 Producer 的链接，以及 Client 的链接。
```java
producer.close();
consumer.close();
client.close();
```

<span id="cam"></span>
### 认证信息字段说明

Client 进行消息生产或消费时，访问 TDMQ 时会经过 CAM 认证，所以需要在创建 Client 的时候配置`AuthCloud`参数，`AuthCloud`参数由一个 Map 映射`authParam`组成，关于`authParam`参数的字段说明见下表：

| 字段      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| secretId  | 在 [云 API 密钥](https://console.cloud.tencent.com/capi) 上申请的标识身份的 SecretId，一个 SecretId 对应唯一的 SecretKey ，而 SecretKey 会用来生成请求签名 Signature。 |
| secretKey | 在 [云 API 密钥](https://console.cloud.tencent.com/capi) 上由 SecretId 生成的一串密钥，一个 SecretId 对应唯一的 SecretKey ，而 SecretKey 会用来生成请求签名 Signature。 |
| region    | 字符串                                                       |
| ownerUin  | 主账号的账号 ID                                               |
| uin       | 当前账号的账号 ID                                             |


