## 操作背景

该任务以 Java 客户端为例指导您在公网网络环境下，使用 SASL_SSL 方式接入消息队列 CKafka 并收发消息。

SSL 证书的核心功能是保护服务器-客户端通信。数据通过 SSL 证书加密，其他人无法拥有解锁它的私钥，只能由预期的服务端解锁。

## 前提条件

- [安装 1.8 或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装 2.5 或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)
- [下载 Demo](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/javakafkademo/PUBLIC_SASL)
- [下载 SASL_SSL 证书](https://ckafka-public-certs-1255613487.cos.ap-guangzhou.myqcloud.com/ssl-certs/client.truststore.jks)

## 操作步骤

### 步骤一：控制台配置
1. 创建接入点。
	1. 在 **[实例列表](https://console.cloud.tencent.com/ckafka/index)** 页面，单击目标实例 ID，进入实例详情页。
	2. 在 **基本信息** > **接入方式** 中，单击**添加路由策略**，在打开窗口中选择：`路由类型：公网域名接入`,`接入方式：SASL_SSL`。
![](https://qcloudimg.tencent-cloud.cn/raw/46e6b0bb08a7b73084cb51fabe9d03f2.png)

2. 创建角色。
在**用户管理**页面新建角色，设置密码。
![](https://qcloudimg.tencent-cloud.cn/raw/fb78b8290232e6342397a30a4c554ef9.png)

3. 创建 Topic。
在控制台 **topic 管理**页面新建 Topic（参考 [创建 Topic](https://cloud.tencent.com/document/product/597/20247#.E5.88.9B.E5.BB.BA-topic)）。


### 步骤二：添加配置文件

1. 在 pom.xml 中添加以下依赖。
```xml
<dependency>
   <dependency>
      <groupId>org.apache.kafka</groupId>
      <artifactId>kafka-clients</artifactId>
      <version>2.1.0</version>
   </dependency>
   <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>1.7.5</version>
   </dependency>
   <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-simple</artifactId>
      <version>1.6.4</version>
   </dependency>
</dependency>

```

2. 创建 JAAS 配置文件 `ckafka_client_jaas.conf`，使用**用户管理**界面创建的用户进行修改。
```properties
KafkaClient {
org.apache.kafka.common.security.plain.PlainLoginModule required
username="yourinstance#yourusername"
password="yourpassword";
};
```
>?username 是`实例 ID` + `#` + `配置的用户名`，password 是配置的用户密码。

3. 创建消息队列 CKafka 配置文件 kafka.properties。
```properties
## 配置接入网络，在控制台的实例详情页面接入方式模块的网络列复制。
bootstrap.servers=xx.xx.xx.xx:xxxx
## 配置 Topic，在控制台上 topic 管理页面复制。
topic=XXX
## 配置 consumer group，您可以自定义设置
group.id=XXX
## SASL 配置
java.security.auth.login.config.plain=/xxxx/ckafka_client_jaas.conf
## SSL 证书配置,接入方式选择为 SASL_SSL 时生效
ssl.truststore.location=/xxxx/client.truststore.jks
ssl.truststore.password=5fi6R!M
ssl.endpoint.identification.algorithm=
```

| 参数                                  | 说明                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| `bootstrap.servers`                      | 接入网络，在控制台的实例详情页面**接入方式**模块的网络列复制。<br/>![](https://qcloudimg.tencent-cloud.cn/raw/6117de422e8b46cf75b7b249bb88c817.png) |
| `topic`                                  | Topic 名称，您可以在控制台上 **topic管理**页面复制。<br/>![](https://main.qcloudimg.com/raw/e7d353c89bbb204303501e8366f59d2c.png) |
| `group.id`                               | 您可以自定义设置，Demo 运行成功后可以在 **Consumer Group** 页面看到该消费者。 |
| `java.security.auth.login.config.plain` | 填写 JAAS 配置文件 `ckafka_client_jaas.conf` 的路径。          |
| `client.truststore.jks`                  | 采用 `SASL_SSL` 方式接入时，所需的证书路径。          |


4. 创建配置文件加载程序 CKafkaConfigurer.java。
```java
public class CKafkaConfigurer {

    private static Properties properties;

    public static void configureSaslPlain() {
        //如果用 -D 或者其它方式设置过，这里不再设置。
        if (null == System.getProperty("java.security.auth.login.config")) {
            //请注意将 XXX 修改为自己的路径。
            System.setProperty("java.security.auth.login.config",
                    getCKafkaProperties().getProperty("java.security.auth.login.config.plain"));
        }
    }

    public synchronized static Properties getCKafkaProperties() {
        if (null != properties) {
            return properties;
        }
        //获取配置文件 kafka.properties 的内容。
        Properties kafkaProperties = new Properties();
        try {
            kafkaProperties.load(CKafkaProducerDemo.class.getClassLoader().getResourceAsStream("kafka.properties"));
        } catch (Exception e) {
            System.out.println("getCKafkaProperties error");
        }
        properties = kafkaProperties;
        return kafkaProperties;
    }
}
```

### 步骤三：发送消息

1. 创建发送消息程序 KafkaSaslProducerDemo.java。
```java
   public class KafkaSaslProducerDemo {

   public static void main(String[] args) {
      //设置 JAAS 配置文件的路径。
      CKafkaConfigurer.configureSaslPlain();

      //加载 kafka.properties。
      Properties kafkaProperties = CKafkaConfigurer.getCKafkaProperties();

      Properties props = new Properties();
      //设置接入点，请通过控制台获取对应 Topic 的接入点。
      props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
              kafkaProperties.getProperty("bootstrap.servers"));

      //
      //  SASL_SSL 公网接入
      //
      //  接入协议。
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_SSL");
      //  SASL 采用 Plain 方式。
      props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");
      //  SSL 加密。
      props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, kafkaProperties.getProperty(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG));
      props.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, kafkaProperties.getProperty(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG));
      props.put(SslConfigs.SSL_ENDPOINT_IDENTIFICATION_ALGORITHM_CONFIG,kafkaProperties.getProperty(SslConfigs.SSL_ENDPOINT_IDENTIFICATION_ALGORITHM_CONFIG));

      //消息队列 Kafka 版消息的序列化方式。
      props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,
              "org.apache.kafka.common.serialization.StringSerializer");
      props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,
              "org.apache.kafka.common.serialization.StringSerializer");
      //请求的最长等待时间。
      props.put(ProducerConfig.MAX_BLOCK_MS_CONFIG, 30 * 1000);
      //设置客户端内部重试次数。
      props.put(ProducerConfig.RETRIES_CONFIG, 5);
      //设置客户端内部重试间隔。
      props.put(ProducerConfig.RECONNECT_BACKOFF_MS_CONFIG, 3000);
      //构造 Producer 对象，注意，该对象是线程安全的，一般来说，一个进程内一个Producer对象即可。
      KafkaProducer<String, String> producer = new KafkaProducer<>(props);

      //构造一个消息队列 Kafka 版消息。
      String topic = kafkaProperties.getProperty("topic"); //消息所属的Topic，请在控制台申请之后，填写在这里。
      String value = "this is ckafka msg value"; //消息的内容。

      try {
         //批量获取 Future 对象可以加快速度。但注意，批量不要太大。
         List<Future<RecordMetadata>> futures = new ArrayList<>(128);
         for (int i = 0; i < 100; i++) {
            //发送消息，并获得一个Future对象。
            ProducerRecord<String, String> kafkaMessage = new ProducerRecord<>(topic,
                    value + ": " + i);
            Future<RecordMetadata> metadataFuture = producer.send(kafkaMessage);
            futures.add(metadataFuture);

         }
         producer.flush();
         for (Future<RecordMetadata> future : futures) {
            //同步获得 Future 对象的结果。
            RecordMetadata recordMetadata = future.get();
            System.out.println("Produce ok:" + recordMetadata.toString());
         }
      } catch (Exception e) {
         //客户端内部重试之后，仍然发送失败，业务要应对此类错误。
         System.out.println("error occurred");
      }
   }
}
```
2. 编译并运行 KafkaSaslProducerDemo.java 发送消息。
   
3. 运行结果（输出）。
```bash
Produce ok:ckafka-topic-demo-0@198
Produce ok:ckafka-topic-demo-0@199
```
4. 在 CKafka 控制台 **topic管理**页面，选择对应的 Topic，单击**更多** > **消息查询**，查看刚刚发送的消息。
![](https://main.qcloudimg.com/raw/ec5fbf218cf50ff3d760be15f6331867.png)



### 步骤四：消费消息

1. 创建 Consumer 订阅消息程序 `KafkaSaslConsumerDemo.java`。
```java
public class KafkaSaslConsumerDemo {

   public static void main(String[] args) {
      //设置JAAS配置文件的路径。
      CKafkaConfigurer.configureSaslPlain();

      //加载kafka.properties。
      Properties kafkaProperties = CKafkaConfigurer.getCKafkaProperties();

      Properties props = new Properties();
      //设置接入点，请通过控制台获取对应Topic的接入点。
      props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
              kafkaProperties.getProperty("bootstrap.servers"));

      //
      //  SASL_SSL 公网接入
      //
      //  接入协议。
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_SSL");
      //  SASL 采用 Plain 方式。
      props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");
      //  SSL 加密。
      props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, kafkaProperties.getProperty(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG));
      props.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, kafkaProperties.getProperty(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG));
      props.put(SslConfigs.SSL_ENDPOINT_IDENTIFICATION_ALGORITHM_CONFIG,kafkaProperties.getProperty(SslConfigs.SSL_ENDPOINT_IDENTIFICATION_ALGORITHM_CONFIG));

      //两次 Poll 之间的最大允许间隔。
      //消费者超过该值没有返回心跳，服务端判断消费者处于非存活状态，服务端将消费者从Consumer Group移除并触发Rebalance，默认30s。
      props.put(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, 30000);
      //每次 Poll 的最大数量。
      //注意该值不要改得太大，如果 Poll 太多数据，而不能在下次 Poll 之前消费完，则会触发一次负载均衡，产生卡顿。
      props.put(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, 30);
      //消息的反序列化方式。
      props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,
              "org.apache.kafka.common.serialization.StringDeserializer");
      props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,
              "org.apache.kafka.common.serialization.StringDeserializer");
      //当前消费实例所属的消费组，请在控制台申请之后填写。
      //属于同一个组的消费实例，会负载消费消息。
      props.put(ConsumerConfig.GROUP_ID_CONFIG, kafkaProperties.getProperty("group.id"));
      //构造消费对象，也即生成一个消费实例。
      KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
      //设置消费组订阅的 Topic，可以订阅多个。
      //如果 GROUP_ID_CONFIG 是一样，则订阅的 Topic 也建议设置成一样。
      List<String> subscribedTopics = new ArrayList<String>();
      //如果需要订阅多个 Topic，则在这里添加进去即可。
      //每个 Topic 需要先在控制台进行创建。
      String topicStr = kafkaProperties.getProperty("topic");
      String[] topics = topicStr.split(",");
      for (String topic : topics) {
         subscribedTopics.add(topic.trim());
      }
      consumer.subscribe(subscribedTopics);

      //循环消费消息。
      while (true) {
         try {
            ConsumerRecords<String, String> records = consumer.poll(1000);
            //必须在下次 Poll 之前消费完这些数据, 且总耗时不得超过 SESSION_TIMEOUT_MS_CONFIG。
            for (ConsumerRecord<String, String> record : records) {
               System.out.println(
                       String.format("Consume partition:%d offset:%d", record.partition(),
                               record.offset()));
            }
         } catch (Exception e) {
            System.out.println("consumer error!");
         }
      }
   }
}
```
2. 编译并运行 KafkaSaslConsumerDemo.java 消费消息。
   
3. 运行结果。
```bash
   Consume partition:0 offset:298
   Consume partition:0 offset:299   
```
4. 在 CKafka 控制台 **Consumer Group** 页面，选择对应的消费组名称，在主题名称输入 Topic 名称，单击**查询详情**，查看消费详情。
![](https://main.qcloudimg.com/raw/27775267907600f4ff759e6a197195ee.png)
