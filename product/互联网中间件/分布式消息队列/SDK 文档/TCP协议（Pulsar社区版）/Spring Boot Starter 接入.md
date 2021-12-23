## 操作场景

本文以 Spring Boot Starter 接入为例介绍实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备]()
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/tdmq-pulsar-springboot-demo.zip)

## 操作步骤

### 步骤1. 添加依赖

在项目中引入 Pulsar Starter 相关依赖。

```xml
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
```

### 步骤2. 准备配置

在配置文件中 添加 Pulsar 相关配置信息。

```yaml
pulsar:
  # 命名空间名称
  namespace: namespace_java
  # 服务接入地址
  service-url: http://pulsar-xxx.tdmq.ap-gz.public.tencenttdmq.com:8080
  # 授权角色密钥
  token-auth-value: eyJrZXlJZC....
  # 集群名称
  tenant: pulsar-xxx
```

| 参数             | 说明                                                         |
| :--------------- | :----------------------------------------------------------- |
| namespace        | 命名空间名称，在控制台 **[命名空间](https://console.cloud.tencent.com/tdmq/env)** 管理页面中复制。 |
| service-url      | 集群接入地址，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 页面查看并复制。![img](https://main.qcloudimg.com/raw/a1bbc4b3857903e04f16fc46d9194c57.png) |
| token-auth-value | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| tenant           | 集群 ID，在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 页面中获取。 |

### 步骤3. 生产消息

1. 生产者工厂配置。

   ```java
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
   ```

   > ?
   >
   > Topic 名称需要填入完整路径，即“persistent://clusterid/namespace/Topic”，clusterid/namespace/topic 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。

2. 注入生产者。

   ```java
   @Autowired
   private PulsarTemplate<byte[]> defaultProducer;  // byte[]类型生产者
   
   @Autowired
   private PulsarTemplate<String> stringProducer;   // String类型生产者
   
   @Autowired
   private PulsarTemplate<MyMessage> customProducer;  // MyMessage类型生产者 (自定义消息类型)
   ```

3. 发送消息。

   ```java
   // 发送String类型的消息
   stringProducer.send("topic1", "Hello pulsar client.");
   
   // 发送MyMessage类型消息 (自定义消息类型)
   MyMessage myMessage = new MyMessage();
   myMessage.setData("Hello client, this is a custom message.");
   myMessage.setSendDate(new Date());
   customProducer.send("topic4", myMessage);
   
   // 发送byte[]类型消息
   defaultProducer.send("topic2", ("Hello pulsar client, this is a order message" + i + ".").getBytes(StandardCharsets.UTF_8));
   ```

> !
>
> - 发送消息的 Topic 是在生产者配置中已经声明的 Topic。
> - PulsarTemplate 类型应与发送消息的类型一致。
> - 发送消息到指定 Topic 时，消息类型需要与生产者工厂配置中的 Topic 绑定的消息类型对应。

### 步骤4. 消费消息

消费者配置。

```java
@PulsarConsumer(topic = "topic1",  // 订阅topic名称
                subscriptionName = "sub_topic1", // 订阅名称
                clazz = String.class, // 消息类型，需要与生产者保持一致，绑定后不能修改类型
                serialization = Serialization.JSON, // 序列化方式
                subscriptionType = SubscriptionType.Shared, // 订阅模式，默认为共享模式
                consumerName = "firstTopicConsumer", // 消费者名称
                maxRedeliverCount = 3, // 最大重试次数
                deadLetterTopic = "sub_topic1-DLQ" // 死信topic名称
               )
public void topicConsume(String msg) {
    // TODO process your message
    System.out.println("Received a new message. content: [" + msg + "]");
    // 如果消费失败，请抛出异常，这样消息会进入重试队列，之后可以重新消费，直到达到最大重试次数之后，进入死信队列。前提是要创建重试和死信topic
}
```

> ?
>
> - Topic 名称需要填入完整路径，即“persistent://clusterid/namespace/Topic”，clusterid/namespace/topic 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
>
> - subscriptionName需要写入订阅名，可在**消费管理**界面查看。



### 步骤5. 查询消息

1. 登录控制台，进入 **[消息查询](https://console.cloud.tencent.com/tdmq/message)** 页面，可查看 Demo 运行后的消息轨迹。
   ![img](https://qcloudimg.tencent-cloud.cn/raw/6178970f9e7395b8e7430275fc039d47.png)
   消息轨迹如下：
   ![img](https://main.qcloudimg.com/raw/eaa0125f6dcd7675e367c4e3e069c915.png)

以上是基于 Springboot Starter 方式对 Pulsar 简单使用的配置。详细使用可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/tdmq-pulsar-springboot-demo.zip) 或 [Starter 文档](https://github.com/majusko/pulsar-java-spring-boot-starter)。
