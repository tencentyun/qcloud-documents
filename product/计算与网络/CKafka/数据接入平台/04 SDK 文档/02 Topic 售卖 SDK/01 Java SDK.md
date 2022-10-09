## 操作场景

本文介绍使用  Java 客户端连接数据接入平台 Topic 并收发消息的操作步骤。

## 前提条件
- [安装 1.8 或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装 2.5 或以上版本 Maven](http://maven.apache.org/download.cgi#)

## 操作步骤

### 步骤1：创建 Topic 和订阅关系

1. 在 DIP 控制台的 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 页面创建一个 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/775cd1e3c0a102b485565915ed7b3864.png)
2. 单击 Topic 的 “ID” 进入基本信息页面，获取用户名、密码和地址信息。
![](https://qcloudimg.tencent-cloud.cn/raw/3b1e8ccf0d9c0f2bf9e24831dc250255.png)
3. 在**订阅关系**页签，新建一个订阅关系（消费组）。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ea08126a23715f24c50936d564421655.png)



### 步骤2：添加配置文件

1. 在 pom.xml 中添加以下依赖。
<dx-codeblock>
:::  xml
<dependencies>
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
</dependencies>
:::
</dx-codeblock>
2. 创建 JAAS 配置文件 `ckafka_client_jaas.conf`，使用**用户管理**界面创建的用户进行修改。
<dx-codeblock>
:::  yaml
KafkaClient {
org.apache.kafka.common.security.plain.PlainLoginModule required
username="username"
password="password";
};
:::
</dx-codeblock>
3. 创建消息队列 CKafka 配置文件 kafka.properties。
<dx-codeblock>
:::  yaml
## 配置接入地址，在 DIP 控制台的 Topic 基本信息页面获取。
bootstrap.servers=xx.xx.xx.xx:port
## Topic 名称，在 DIP 控制台的 Topic 基本信息页面获取。
topic=XXX
## 消费组名称，在 DIP 控制台的 **订阅关系**列表获取。
group.id=XXX
## SASL 配置
java.security.auth.login.config.plain=/xxxx/ckafka_client_jaas.conf
:::
</dx-codeblock>
4. 创建配置文件加载程序 CKafkaConfigurer.java。
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>bootstrapServers</code></td>
<td align="left">接入地址，在 DIP 控制台的 Topic 基本信息页面获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/f355a1dd5fbbcfb9cda85154107ed4ec.png" alt=""></td>
</tr>
<tr>
<td align="left"><code>username</code></td>
<td align="left">用户名，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>password</code></td>
<td align="left">用户密码，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>topic</code></td>
<td align="left">Topic 名称，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>group.id</code></td>
<td align="left">消费组名称，在 DIP 控制台的 <strong>订阅关系</strong>列表获取。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/aca7b72ff1cf38af6657a34897fbff8d.png" alt=""></td>
</tr>
</tbody></table>





### 步骤3：生产消息

1. 创建发送消息程序 KafkaSaslProducerDemo.java。
<dx-codeblock>
:::  java
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
      //  SASL_PLAINTEXT 公网接入
      //
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
      //  SASL 采用 Plain 方式。
      props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");

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
      //ack=0   producer 将不会等待来自 broker 的确认，重试配置不会生效。注意如果被限流了后，就会被关闭连接。
      //ack=1   broker leader 将不会等待所有 broker follower 的确认，就返回 ack。
      //ack=all broker leader 将等待所有 broker follower 的确认，才返回 ack。
      props.put(ProducerConfig.ACKS_CONFIG, "all");
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
:::
</dx-codeblock>
2. 编译并运行 KafkaSaslProducerDemo.java 发送消息。
3. 运行结果（输出）。
<dx-codeblock>
:::  log
Produce ok:ckafka-topic-demo-0@198
Produce ok:ckafka-topic-demo-0@199
:::
</dx-codeblock>


### 步骤4：消费消息
1. 创建 Consumer 订阅消息程序 `KafkaSaslConsumerDemo.java`。
<dx-codeblock>
:::  java
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
      //  SASL_PLAINTEXT 公网接入
      //
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
      //  SASL 采用 Plain 方式。
      props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");

      //消费者超时时长
      //消费者超过该值没有返回心跳，服务端判断消费者处于非存活状态，服务端将消费者从Consumer Group移除并触发Rebalance，默认30s
      props.put(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, 30000);
      //两次poll的最长时间间隔
      //0.10.1.0 版本前这2个概念是混合的，都用session.timeout.ms表示
      props.put(ConsumerConfig.MAX_POLL_INTERVAL_MS_CONFIG, 30000);
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
:::
</dx-codeblock>
2. 编译并运行 KafkaSaslConsumerDemo.java 消费消息。
3. 运行结果。
<dx-codeblock>
:::  log
   Consume partition:0 offset:298
   Consume partition:0 offset:299   
:::
</dx-codeblock>
