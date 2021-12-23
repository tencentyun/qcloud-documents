## 操作场景

本文以调用 Java SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/tdmq-pulsar-java-sdk-demo.zip)

## 操作步骤

1. Java 项目中引入相关依赖，以 Maven 工程为例，在 pom.xml 添加以下依赖：
<dx-codeblock>
:::  xml
 <dependency>
		 <groupId>org.apache.pulsar</groupId>
		 <artifactId>pulsar-client</artifactId>
		 <version>2.7.2</version>
 </dependency>
:::
</dx-codeblock>
>? 建议使用 2.7.2 及以上版本。
2. 创建 Pulsar 客户端。
<dx-codeblock>
:::  java
    PulsarClient pulsarClient = PulsarClient.builder()
                   // 服务接入地址
                   .serviceUrl(SERVICE_URL)
                   // 授权角色密钥
                   .authentication(AuthenticationFactory.token(AUTHENTICATION)).build();
:::
</dx-codeblock>
<table>
<tr>
<th>参数	</th>
<th>说明</th>
</tr>
<tr>
<td>SERVICE_URL</td>
<td>集群接入地址，可以在控制台 <a href = "https://console.cloud.tencent.com/tdmq/cluster"><b>集群管理</b></a> 页面查看并复制。<br><img src = "https://qcloudimg.tencent-cloud.cn/raw/1221f6b1be8ad150a6544a3f9394a8eb.png"></td>
</tr>
<tr>
<td>AUTHENTICATION</td>
<td>	角色密钥，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制密钥列复制。<br><img src = "https://qcloudimg.tencent-cloud.cn/raw/fe61f06117eb0aaf85974545e72e1637.png"></td>
</tr>
</table>
3. 创建生产者。
<dx-codeblock>
:::  java
   // 构建byte[]类型的生产者
   Producer<byte[]> producer = pulsarClient.newProducer()
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
       .topic("persistent://pulsar-xxx/sdk_java/topic1").create();
:::
</dx-codeblock>
> ?Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
4. 发送消息。
<dx-codeblock>
:::  java
   //发送消息
   MessageId msgId = producer.newMessage()
       // 消息内容
       .value("this is a new message.".getBytes(StandardCharsets.UTF_8))
       // 业务key
       .key("youKey")
       // 业务相关参数
       .property("mykey", "myvalue").send();
:::
</dx-codeblock>
5. 资源释放。
<dx-codeblock>
:::  java
   // 关闭生产者
   producer.close();
   // 关闭客户端
   pulsarClient.close();
:::
</dx-codeblock>
6. 创建消费者。
<dx-codeblock>
:::  java
   // 构建byte[]类型（默认类型）的消费者
   Consumer<byte[]> consumer = pulsarClient.newConsumer()
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
       .topic("persistent://pulsar-xxx/sdk_java/topic1")
       // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
       .subscriptionName("sub_topic1")
       // 声明消费模式为exclusive（独占）模式
       .subscriptionType(SubscriptionType.Exclusive)
       // 配置从最早开始消费，否则可能会消费不到历史消息
       .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest)
       // 订阅
       .subscribe();
:::
</dx-codeblock>
> ?
> - Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
>   ![](https://qcloudimg.tencent-cloud.cn/raw/dc1bc50c434546755565c6dcb8d3e7f0.png)
> - subscriptionName 需要写入订阅名，可在**消费管理**界面查看。
7. 消费消息。
<dx-codeblock>
:::  java
   // 接收当前offset对应的一条消息
   Message<byte[]> msg = consumer.receive();
   MessageId msgId = msg.getMessageId();
   String value = new String(msg.getValue());
   System.out.println("receive msg " + msgId + ",value:" + value);
   // 接收到之后必须要ack，否则offset会一直停留在当前消息，导致消息积压
   consumer.acknowledge(msg);
:::
</dx-codeblock>
8. 使用监听器进行消费。
<dx-codeblock>
:::  java
   // 消息监听器
   MessageListener<byte[]> myMessageListener = (consumer, msg) -> {
       try {
           System.out.println("Message received: " + new String(msg.getData()));
           // 回复ack
           consumer.acknowledge(msg);
       } catch (Exception e) {
           // 消费失败，回复nack
           consumer.negativeAcknowledge(msg);
       }
   };
   pulsarClient.newConsumer()
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
       .topic("persistent://pulsar-mmqwr5xx9n7g/sdk_java/topic1")
       // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
       .subscriptionName("sub_topic1")
       // 声明消费模式为exclusive（独占）模式
       .subscriptionType(SubscriptionType.Exclusive)
       // 设置监听器
       .messageListener(myMessageListener)
       // 配置从最早开始消费，否则可能会消费不到历史消息
       .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest)
       .subscribe();
:::
</dx-codeblock>
9. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，依次点击 **Topic 管理** > **Topic 名称**进入消费管理页面，点开订阅名下方右三角号，可查看生产消费记录。
![img](https://main.qcloudimg.com/raw/da7ce2bc5ac606c91982efecdb3b53bb.png)

>?上述是对消息的发布和订阅方式的简单介绍。更多操作可参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/tdmq-pulsar-java-sdk-demo.zip) 或 [Pulsar 官方文档](https://pulsar.apache.org/docs/en/client-libraries-java/)。
