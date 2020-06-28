## 操作场景

需要通过公网访问消息队列CKAFKA服务时，可以通过管控台增加公网路由，并通过配置SASL鉴权和ACL规则实现公网访问CKAFKA Topic的生产和消费消息。

## 操作步骤

### 创建公网路由

控制台在实例基本信息中添加路由策略-公网域名接入，接入方式目前只支持SASL_PLAINTEXT，单击提交即可。

![image-20200628170809176](/Users/hugo/Library/Application Support/typora-user-images/image-20200628170809176.png)

![image-20200628170957505](/Users/hugo/Library/Application Support/typora-user-images/image-20200628170957505.png)

![image-20200628171401978](/Users/hugo/Library/Application Support/typora-user-images/image-20200628171401978.png)



### 创建用户

实例-用户管理中新增用户信息(包括用户名、密码)，用于SASL访问用户认证，单击提交即可

![image-20200628171441925](/Users/hugo/Library/Application Support/typora-user-images/image-20200628171441925.png)

![image-20200628171505915](/Users/hugo/Library/Application Support/typora-user-images/image-20200628171505915.png)

![image-20200628171551902](/Users/hugo/Library/Application Support/typora-user-images/image-20200628171551902.png)

### ACL策略授权

对现有topic进行ACL权限管理(包括读写)，只有拥有权限的用户才能对topic进行相关读写权限操作

1.控制台实例-ACL策略管理，选择topic对其编辑ACL策略

![image-20200628171918152](/Users/hugo/Library/Application Support/typora-user-images/image-20200628171918152.png)

2.新增ACL策略，给用户赋予资源topic权限，提交即可



![image-20200628172004517](/Users/hugo/Library/Application Support/typora-user-images/image-20200628172004517.png)

![image-20200628172040636](/Users/hugo/Library/Application Support/typora-user-images/image-20200628172040636.png)

![image-20200628172127637](/Users/hugo/Library/Application Support/typora-user-images/image-20200628172127637.png)

>?
>
>Ckafka相关SASL和ACL，用户管理访问控制详情见（https://cloud.tencent.com/document/product/597/31528）文档。
### 公网生产和消费

控制台操作完成后，即可使用用户名和密码在公网访问实例资源

#### 生产

```java
Properties props = new Properties();
        //公网接入域名地址,即公网路由地址
        props.put("bootstrap.servers", "your_public_network_route_addr");
        props.put("acks", "all");
        props.put("retries",0);
        props.put("batch.size", 16384);
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("request.timeout.ms", 10000);
        props.put("max.block.ms", 30000);
        props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
        props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");
        //用户名密码，注：用户名是需要拼接，并非管控台的用户名：instanceId#username
        props.put("sasl.jaas.config",
                "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"yourinstance#yourusername\" password=\"yourpassword\";");
        Producer<String, String> producer = new KafkaProducer<String, String>(props);
        for (int i = 0; i < 1000; i++) {
            Future<RecordMetadata> future = producer.send(new ProducerRecord<>("topic1", UUID.randomUUID().toString()));
            System.out.println("produce offset:" + future.get().offset());
        }
        producer.close();
```



#### 消费

```java
Properties props = new Properties();
        //公网接入域名地址
        props.put("bootstrap.servers", "your_public_network_route_addr");
        props.put("group.id", "yourconsumegroup");
        props.put("enable.auto.commit", "true");
        props.put("auto.commit.interval.ms", "1000");
        props.put("session.timeout.ms", "30000");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
        props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");
        //用户名密码，注：用户名是需要拼接，并非管控台的用户名：instanceId#username
        props.put("sasl.jaas.config",
                "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"yourinstance#yourusername\" password=\"yourpassword\";");

        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Arrays.asList("yourtopic"));
        while (true) {
            ConsumerRecords<String, String> records = consumer.poll(100);
            for (ConsumerRecord<String, String> record : records) {
                System.out.printf("offset = %d, key = %s, value = %s", record.offset(), record.key(), record.value());
            }
        }
```

> ?
>
> 除了使用properties添加 sasl.jaas.config 配置的方式，也可以通过System.setProperty或-D的方式传入。
>
> System.setProperty("java.security.auth.login.config", "/etc/ckafka_client_jaas.conf");
>
> ```java
> KafkaClient {
> org.apache.kafka.common.security.plain.PlainLoginModule required
> username="yourinstance#yourusername"
> password="yourpassword";
> }; 
> ```

