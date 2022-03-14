## 操作场景

本文以 Spring Boot Starter 接入为例介绍实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-springboot-demo.zip)

## 操作步骤

### 步骤1：添加依赖

在项目中引入 Pulsar Starter 相关依赖。
<dx-codeblock>
:::  xml
<dependency>
    <groupId>io.github.majusko</groupId>
    <artifactId>pulsar-java-spring-boot-starter</artifactId>
    <version>1.0.7</version>
</dependency>
<!-- https://mvnrepository.com/artifact/io.projectreactor/reactor-core -->
<dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.4.11</version>
</dependency>
:::
</dx-codeblock>


### 步骤2：准备配置

在配置文件中 添加 Pulsar 相关配置信息。
<dx-codeblock>
:::  yaml
pulsar:
  # 命名空间名称
  namespace: namespace_java
  # 服务接入地址
  service-url: http://pulsar-xxx.tdmq.ap-gz.public.tencenttdmq.com:8080
  # 授权角色密钥
  token-auth-value: eyJrZXlJZC....
  # 集群 ID
  tenant: pulsar-xxx
:::
</dx-codeblock>
<table>
<tr>
<th>参数	</th>
<th>说明</th>
</tr>
<tr>
<td>namespace</td>
<td>命名空间名称，在控制台 <a href = "https://console.cloud.tencent.com/tdmq/env"><b>命名空间</b></a> 管理页面中复制。</td>
</tr>
<tr>
<td>service-url</td>
<td>集群接入地址，可以在控制台 <a href = "https://console.cloud.tencent.com/tdmq/cluster"><b>集群管理</b></a> 页面查看并复制。<br><img src = "https://qcloudimg.tencent-cloud.cn/raw/d9cc1ac7ceeae77df150143127f2396e.png"></td>
</tr>
<tr>
<td>token-auth-value</td>
<td>角色密钥，在 <a href = "https://console.cloud.tencent.com/tdmq/role"><b>角色管理</b></a> 页面复制密钥列复制。<br><img src = "https://qcloudimg.tencent-cloud.cn/raw/6abfb90ff4e80bdf8c00a555f3dd3634.png"></td>
</tr>
<tr>
<td>tenant</td>
<td>集群 ID，在控制台 <a href = "https://console.cloud.tencent.com/tdmq/cluster"><b>集群管理</b></a> 页面中获取。</td>
</tr>
</table>

### 步骤3：生产消息

1. 生产者工厂配置。
<dx-codeblock>
:::  java
 @Configuration
 public class ProducerConfiguration {

		 @Bean
		 public ProducerFactory producerFactory() {
				 return new ProducerFactory()
								 // topic1 使用String类型生产者
								 .addProducer("topic1", String.class)
								 // topic2 使用byte[]类型(默认类型)生产者
								 .addProducer("topic2")
								 // topic3 使用MyMessage类型生产者 (自定义消息类型)
								 .addProducer("topic4", MyMessage.class);
		 }
 }
:::
</dx-codeblock>
2. 注入生产者。
<dx-codeblock>
:::  java
@Autowired
private PulsarTemplate<byte[]> defaultProducer;  // byte[]类型生产者

@Autowired
private PulsarTemplate<String> stringProducer;   // String类型生产者

@Autowired
private PulsarTemplate<MyMessage> customProducer;  // MyMessage类型生产者 (自定义消息类型)
:::
</dx-codeblock>
3. 发送消息。
<dx-codeblock>
:::  java
// 发送String类型的消息
stringProducer.send("topic1", "Hello pulsar client.");

// 发送MyMessage类型消息 (自定义消息类型)
MyMessage myMessage = new MyMessage();
myMessage.setData("Hello client, this is a custom message.");
myMessage.setSendDate(new Date());
customProducer.send("topic4", myMessage);

// 发送byte[]类型消息
defaultProducer.send("topic2", ("Hello pulsar client, this is a order message" + i + ".").getBytes(StandardCharsets.UTF_8));
:::
</dx-codeblock>
> !
>
> - 发送消息的 Topic 是在生产者配置中已经声明的 Topic。
> - PulsarTemplate 类型应与发送消息的类型一致。
> - 发送消息到指定 Topic 时，消息类型需要与生产者工厂配置中的 Topic 绑定的消息类型对应。

### 步骤4：消费消息

消费者配置。
<dx-codeblock>
:::  java
@PulsarConsumer(topic = "topic1",  // 订阅topic名称
                subscriptionName = "sub_topic1", // 订阅名称
                clazz = String.class, // 消息类型，需要与生产者保持一致，绑定后不能修改类型
                serialization = Serialization.JSON, // 序列化方式
                subscriptionType = SubscriptionType.Shared, // 订阅模式，默认为独占模式
                consumerName = "firstTopicConsumer", // 消费者名称
                maxRedeliverCount = 3, // 最大重试次数
                deadLetterTopic = "sub_topic1-DLQ" // 死信topic名称
               )
public void topicConsume(String msg) {
    // TODO process your message
    System.out.println("Received a new message. content: [" + msg + "]");
    // 如果消费失败，请抛出异常，这样消息会进入重试队列，之后可以重新消费，直到达到最大重试次数之后，进入死信队列。前提是要创建重试和死信topic
}
:::
</dx-codeblock>



### 步骤5：查询消息

1. 登录控制台，进入 **[消息查询](https://console.cloud.tencent.com/tdmq/message)** 页面，可查看 Demo 运行后的消息轨迹。
![](https://qcloudimg.tencent-cloud.cn/raw/bb160d0e4cbe3bb77437713025b1fcca.png)
   消息轨迹如下：
![](https://qcloudimg.tencent-cloud.cn/raw/a5794d7dad969cc77b1d0b78d0a93dab.png)

>?以上是基于 Springboot Starter 方式对 Pulsar 简单使用的配置。详细使用可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-springboot-demo.zip) 或 [Starter 文档](https://github.com/majusko/pulsar-java-spring-boot-starter)。
