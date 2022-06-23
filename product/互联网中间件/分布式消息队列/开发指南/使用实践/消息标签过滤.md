本文主要介绍 TDMQ Pulsar 版中消息标签过滤的功能、应用场景和使用方式。

## 功能介绍

Tag，即消息标签，用于对某个Topic下的消息进行分类。TDMQ Pulsar 版的生产者在发送消息时，指定消息的Tag，消费者需根据已经指定的Tag来进行订阅。

消费者订阅 Topic 时若未设置 Tag，Topic 中的所有消息都将被投递到消费端进行消费。

## 应用场景

通常，一个 Topic 中存放的是相同业务属性的消息，例如交易流水 Topic 包含了下单流水、支付流水、发货流水等，业务若只想消费者其中一种类别的流水，可在客户端进行过滤，但这种过滤方式会带来带宽的资源浪费。

针对上述场景，TDMQ Pulsar 提供 Broker 端过滤的方式，用户可在生产消息时设置一个或者多个 Tag 标签，消费时指定 Tag 订阅。

![img](https://main.qcloudimg.com/raw/32953b29d96dce605fa4a1598b3f5146.png)



## 使用说明





Tag 消息目前是通过 Properties 的方式传入的，可以通过如下方式获取：

<dx-tabs>
:::Java
<dx-codeblock>
:::  xml
<dependency>
    <groupId>org.apache.pulsar</groupId>
    <artifactId>pulsar-client</artifactId>
    <version>2.x.x</version> <!-- 具体版本待补充 -->
</dependency>
:::
</dx-codeblock>


:::

:::Go

需要使用最新的 Go SDK master 版本。

<dx-codeblock>
:::  go
go get -u github.com/apache/pulsar-client-go@master
:::
</dx-codeblock>

:::
</dx-tabs>


### Tag 消息使用限制

- Tag 消息不支持 Batch 功能，Batch 功能默认是开启的。如果要使用 Tag 消息，需要在 Producer 侧禁用掉 batch，具体如下：
<dx-codeblock>
:::  Java
  // 构建生产者
  Producer<byte[]> producer = pulsarClient.newProducer()
          // 禁用掉batch功能
          .enableBatching(false)
          // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
          .topic("persistent://pulsar-xxx/sdk_java/topic2").create();
:::
:::  Go
  producer, err := client.CreateProducer(pulsar.ProducerOptions{
  	DisableBatching: true, // 禁用掉batch功能
  })
:::
</dx-codeblock>
- tag 消息的过滤只针对已设置 tag 的消息，未设置 tag 的消息，不在过滤范围内。即未设置 tag 的消息会推送给所有的订阅者。
- 如果要开启 Tag 消息，需要发送消息的时候，在 ProducerMessage 中设置 Properties 字段；同时在创建 Consumer 的时候需要在 ConsumerOptions 中指定 SubscriptionProperties 字段。
- 在 ProducerMessage 中设置 Properties 字段时，其中 key 为 tag 的名字，value 为固定值：`TAGS`。
- 在 ConsumerOptions 中指定 SubscriptionProperties 字段时，其中 key 为要订阅的 tag 的名字，value 为 tag 的版本信息，为保留字段，目前没有实质含义，用来做后续功能的扩展，具体如下：

<dx-accordion>
::: 指定单个 tag

<dx-codeblock>
:::  Java
     // 发送消息
     MessageId msgId = producer.newMessage()
         .property("tag1", "TAGS")
         .value(value.getBytes(StandardCharsets.UTF_8))
		    .send();
	  
     // 订阅相关参数，可用来设置订阅标签(TAG)
     HashMap<String, String> subProperties = new HashMap<>();
	  subProperties.put("tag1","1");
	  subProperties.put("tag2","1");
	  // 构建消费者
	  Consumer<byte[]> consumer = pulsarClient.newConsumer()
	      // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
         .topic("persistent://pulsar-xxxx/sdk_java/topic2")
         // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
         .subscriptionName("topic_sub1")
         // 声明消费模式为共享模式
         .subscriptionType(SubscriptionType.Shared)
         // 订阅相关参数，tag订阅等。。
         .subscriptionProperties(subProperties)
	      // 配置从最早开始消费，否则可能会消费不到历史消息
	      .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest).subscribe();
:::
:::  Go
	   // 发送消息
	   if msgId, err := producer.Send(ctx, &pulsar.ProducerMessage{
	              Payload: []byte(fmt.Sprintf("hello-%d", i)),
	     Properties: map[string]string{
	         "tag1": "TAGS",
	     },
	   	}); err != nil {
	              log.Fatal(err)
         }

    // 创建 consumer
         consumer, err := client.Subscribe(pulsar.ConsumerOptions{
   	            Topic:            "topic-1",
   	            SubscriptionName: "my-sub",
               	SubscriptionProperties: map[string]string{"tag1": "1"},
	      })
:::
</dx-codeblock>


:::
::: 指定多个 tag
<dx-codeblock>
:::  Java
	  // 发送消息
		MessageId msgId = producer.newMessage()
		    .property("tag1", "TAGS")
		    .property("tag2", "TAGS")
	      .value(value.getBytes(StandardCharsets.UTF_8))
		    .send();
     
     // 订阅相关参数，可用来设置订阅标签(TAG)
     HashMap<String, String> subProperties = new HashMap<>();
     subProperties.put("tag1","1");
     subProperties.put("tag2","1");
     // 构建消费者
     Consumer<byte[]> consumer = pulsarClient.newConsumer()
         // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
         .topic("persistent://pulsar-xxxx/sdk_java/topic2")
         // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
         .subscriptionName("topic_sub1")
         // 声明消费模式为共享模式
         .subscriptionType(SubscriptionType.Shared)
         // 订阅相关参数，tag订阅等。。
         .subscriptionProperties(subProperties)
         // 配置从最早开始消费，否则可能会消费不到历史消息
         .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest).subscribe();
:::
:::  Go
      // 创建 producer
      if msgId, err := producer.Send(ctx, &pulsar.ProducerMessage{
                 Payload: []byte(fmt.Sprintf("hello-%d", i)),
           	    Properties: map[string]string{
     	                  "tag1": "TAGS",
     	                  "tag2": "TAGS",
                 },
         }); err != nil {
                 log.Fatal(err)
         }
   
    // 创建 consumer
         consumer, err := client.Subscribe(pulsar.ConsumerOptions{
   	            Topic:            "topic-1",
   	            SubscriptionName: "my-sub",
   	            SubscriptionProperties: map[string]string{
   		                  "tag1": "1",
   		                  "tag2": "1",
   	            },
         })

:::
</dx-codeblock>

:::
::: tag 与 properties 混合
<dx-codeblock>
:::  Java
   	// 发送消息
   	MessageId msgId = producer.newMessage()
   	    .property("tag1", "TAGS")
   	    .property("tag2", "TAGS")
   	    .property("xxx", "yyy")
         .value(value.getBytes(StandardCharsets.UTF_8))
   	    .send();
     
     // 订阅相关参数，可用来设置订阅标签(TAG)
     HashMap<String, String> subProperties = new HashMap<>();
     subProperties.put("tag1","1");
     subProperties.put("tag2","1");
     // 构建消费者
     Consumer<byte[]> consumer = pulsarClient.newConsumer()
         // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
         .topic("persistent://pulsar-xxxx/sdk_java/topic2")
         // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
         .subscriptionName("topic_sub1")
         // 声明消费模式为共享模式
         .subscriptionType(SubscriptionType.Shared)
         // 订阅相关参数，tag订阅等。。
         .subscriptionProperties(subProperties)
         // 配置从最早开始消费，否则可能会消费不到历史消息
         .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest).subscribe();
:::
:::  Go
      // 创建 producer
      if msgId, err := producer.Send(ctx, &pulsar.ProducerMessage{
                 Payload: []byte(fmt.Sprintf("hello-%d", i)),
                 Properties: map[string]string{
     	                  "tag1": "TAGS",
     	                  "tag2": "TAGS",
     	                  "xxx": "yyy",
                 },
         }); err != nil {
                 log.Fatal(err)
         }
   
    // 创建 consumer
         consumer, err := client.Subscribe(pulsar.ConsumerOptions{
   	            Topic:            "topic-1",
   	            SubscriptionName: "my-sub",
   	            SubscriptionProperties: map[string]string{
   		                  "tag1": "1",
   		                  "tag2": "1",
   	            },
         })
:::
</dx-codeblock>

:::
</dx-accordion>


>!在 consumer 侧设置 SubscriptionProperties 字段时，一旦设定，这个订阅所处理的 tag 信息是不可变更的。如果需要更换订阅的 tag，可以将当前的订阅先 `Unsubscribe` 掉，然后再重新创建新的订阅来处理。
