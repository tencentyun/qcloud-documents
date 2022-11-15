## 操作背景

该任务以 Java 客户端为例指导您在公网网络环境下接入消息队列 CKafka 并收发消息。

其他语言客户端请参见 [SDK 文档](https://cloud.tencent.com/document/product/597/54816)。

## 前提条件

- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/javakafkademo/PUBLIC_SASL)

## 操作步骤

#### 步骤1：准备配置

1. 将下载的 Demo 进行解压，进入 javakafkademo 下的 PUBLIC_SASL 目录。
2. 修改 JAAS 配置文件 ckafka_client_jaas.conf。
<dx-codeblock>
:::  bash
KafkaClient {
org.apache.kafka.common.security.plain.PlainLoginModule required
username="yourinstance#yourusername"
password="yourpassword";
};
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
username 是`实例 ID` + `#` + `配置的用户名`，password 是配置的用户密码。
</dx-alert>
2. 修改消息队列 CKafka 配置文件 kafka.properties。
<dx-codeblock>
:::  bash
## 配置接入网络，在控制台的实例详情页面接入方式模块的网络列复制。
bootstrap.servers=ckafka-xxxxxxx
## 配置Topic，在控制台上topic管理页面复制。
topic=XXX
## 配置Consumer Group，您可以自定义设置
group.id=XXX
##JAAS配置文件ckafka_client_jaas.conf的路径。
java.security.auth.login.config.plain=/xxxx/ckafka_client_jaas.conf
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>bootstrap.servers</td>
<td>接入网络，在控制台的实例详情页面<strong>接入方式</strong>模块的网络列复制。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/265f18deec301adabebc6493cc60d582.png" alt=""></td>
</tr>
<tr>
<td>topic</td>
<td>topic 名称，您可以在控制台上<strong>topic管理</strong>页面复制。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/cc84df4a26a9ace1fa134216f49343a2.png" alt=""></td>
</tr>
<tr>
<td>group.id</td>
<td>您可以自定义设置，demo运行成功后可以在<strong>Consumer Group</strong>页面看到该消费者组。</td>
</tr>
<tr>
<td>java.security.auth.login.config.plain</td>
<td>填写 JAAS 配置文件 ckafka_client_jaas.conf 的路径。</td>
</tr>
</tbody></table>


#### 步骤2：发送消息

1. 编译并运行发送消息程序 KafkaSaslProducerDemo.java。
<dx-codeblock>
:::  java
public class KafkaSaslProducerDemo {

	 public static void main(String args[]) {
			 //设置JAAS配置文件的路径。
			 CKafkaConfigurer.configureSaslPlain();

			 //加载kafka.properties。
			 Properties kafkaProperties =  CKafkaConfigurer.getCKafkaProperties();

			 Properties props = new Properties();
			 //设置接入点，请通过控制台获取对应Topic的接入点。
			 props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, kafkaProperties.getProperty("bootstrap.servers"));

			 //接入协议。
			 props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
			 //Plain方式。
			 props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");

			 //消息队列Kafka版消息的序列化方式。
			 props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");
			 props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");
			 //请求的最长等待时间。
			 props.put(ProducerConfig.MAX_BLOCK_MS_CONFIG, 30 * 1000);
			 //设置客户端内部重试次数。
			 props.put(ProducerConfig.RETRIES_CONFIG, 5);
			 //设置客户端内部重试间隔。
			 props.put(ProducerConfig.RECONNECT_BACKOFF_MS_CONFIG, 3000);
			 //构造Producer对象，注意，该对象是线程安全的，一般来说，一个进程内一个Producer对象即可。
			 KafkaProducer<String, String> producer = new KafkaProducer<>(props);

			 //构造一个消息队列Kafka版消息。
			 String topic = kafkaProperties.getProperty("topic"); //消息所属的Topic，请在控制台申请之后，填写在这里。
			 String value = "this is ckafka msg value"; //消息的内容。

			 try {
					 //批量获取Future对象可以加快速度。但注意，批量不要太大。
					 List<Future<RecordMetadata>> futures = new ArrayList<>(128);
					 for (int i =0; i < 100; i++) {
							 //发送消息，并获得一个Future对象。
							 ProducerRecord<String, String> kafkaMessage = new ProducerRecord<>(topic, value + ": " + i);
							 Future<RecordMetadata> metadataFuture = producer.send(kafkaMessage);
							 futures.add(metadataFuture);

					 }
					 producer.flush();
					 for (Future<RecordMetadata> future: futures) {
							 //同步获得Future对象的结果。
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
3. 运行结果（输出）。
<dx-codeblock>
:::  bash
Produce ok:ckafka-topic-demo-0@198
Produce ok:ckafka-topic-demo-0@199
:::
</dx-codeblock>
3. 在 CKafka 控制台**topic管理**页面，选择对应的 topic，单击**更多** > **消息查询**，查看刚刚发送的消息。
![](https://main.qcloudimg.com/raw/cca4f62e86898eec49d8a9cde7ae9fa8.png)

#### 步骤3：消费消息

1. 编译并运行 Consumer 订阅消息程序 KafkaSaslConsumerDemo.java。
<dx-codeblock>
:::  java
public class KafkaSaslConsumerDemo {
    public static void main(String args[]) {
        //设置JAAS配置文件的路径。
        CKafkaConfigurer.configureSaslPlain();

        //加载kafka.properties。
        Properties kafkaProperties =  CKafkaConfigurer.getCKafkaProperties();

        Properties props = new Properties();
        //设置接入点，请通过控制台获取对应Topic的接入点。
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, kafkaProperties.getProperty("bootstrap.servers"));

        //接入协议。
        props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
        //Plain方式。
        props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");
        //两次Poll之间的最大允许间隔。
        //消费者超过该值没有返回心跳，服务端判断消费者处于非存活状态，服务端将消费者从Consumer Group移除并触发Rebalance，默认30s。
        props.put(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, 30000);
        //每次Poll的最大数量。
        //注意该值不要改得太大，如果Poll太多数据，而不能在下次Poll之前消费完，则会触发一次负载均衡，产生卡顿。
        props.put(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, 30);
        //消息的反序列化方式。
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
        //当前消费实例所属的消费组，请在控制台申请之后填写。
        //属于同一个组的消费实例，会负载消费消息。
        props.put(ConsumerConfig.GROUP_ID_CONFIG, kafkaProperties.getProperty("group.id"));
        //构造消费对象，也即生成一个消费实例。
        KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
        //设置消费组订阅的Topic，可以订阅多个。
        //如果GROUP_ID_CONFIG是一样，则订阅的Topic也建议设置成一样。
        List<String> subscribedTopics =  new ArrayList<String>();
        //如果需要订阅多个Topic，则在这里添加进去即可。
        //每个Topic需要先在控制台进行创建。
        String topicStr = kafkaProperties.getProperty("topic");
        String[] topics = topicStr.split(",");
        for (String topic: topics) {
            subscribedTopics.add(topic.trim());
        }
        consumer.subscribe(subscribedTopics);

        //循环消费消息。
        while (true){
            try {
                ConsumerRecords<String, String> records = consumer.poll(1000);
                //必须在下次Poll之前消费完这些数据, 且总耗时不得超过SESSION_TIMEOUT_MS_CONFIG。
                for (ConsumerRecord<String, String> record : records) {
                    System.out.println(String.format("Consume partition:%d offset:%d", record.partition(), record.offset()));
                }
            } catch (Exception e) {
                System.out.println("consumer error!");
            }
        }
    }
}
:::
</dx-codeblock>
2. 运行结果。
<dx-codeblock>
:::  bash
Consume partition:0 offset:298
Consume partition:0 offset:299
:::
</dx-codeblock>
3. 在 CKafka 控制台**Consumer Group**页面，选择对应的消费组名称，在主题名称输入 topic 名称，单击**查询详情**，查看消费详情。
![](https://qcloudimg.tencent-cloud.cn/raw/bfc19f9d6fff0eec137f87d95b983f12.png)

