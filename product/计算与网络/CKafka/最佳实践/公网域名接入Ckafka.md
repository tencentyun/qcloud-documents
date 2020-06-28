## 操作场景

需要通过公网访问消息队列CKAFKA服务时，可以通过管控台增加公网路由，并通过配置SASL鉴权和ACL规则实现公网访问CKAFKA Topic的生产和消费消息。

## 操作步骤

### 创建公网路由

控制台在实例基本信息中添加路由策略-公网域名接入，接入方式目前只支持SASL_PLAINTEXT，单击提交即可。

![image-20200628170809176](https://main.qcloudimg.com/raw/aa16bacebc80525a74daec5991825803.png)

![image-20200628170957505](https://main.qcloudimg.com/raw/c5011c43de887de55add986b35fb90ed.png)

![image-20200628171401978](https://main.qcloudimg.com/raw/06ba59f2e488f8656d0740bc3188488e.png)



### 创建用户

实例-用户管理中新增用户信息(包括用户名、密码)，用于SASL访问用户认证，单击提交即可

![image-20200628171441925](https://main.qcloudimg.com/raw/b1aa8bd6d5e9c4198b3d83693b977cad.png)

![image-20200628171505915](https://main.qcloudimg.com/raw/b3002e02076596065f1ac04671895a9f.png)

![image-20200628171551902](https://main.qcloudimg.com/raw/693da4a3b9911538e5e418f71cfa1411.png)

### ACL策略授权

对现有topic进行ACL权限管理(包括读写)，只有拥有权限的用户才能对topic进行相关读写权限操作

1.控制台实例-ACL策略管理，选择topic对其编辑ACL策略

![image-20200628171918152](https://main.qcloudimg.com/raw/b2a4fd86a79983b309ecb89f4dfd6b61.png)

2.新增ACL策略，给用户赋予资源topic权限，提交即可



![image-20200628172004517](https://main.qcloudimg.com/raw/2d94449b247b8bdf46d8890b7add4a50.png)

![image-20200628172040636](https://main.qcloudimg.com/raw/bc9ea3849a576b6333b00a19744baae5.png)

![image-20200628172127637](https://main.qcloudimg.com/raw/1c3982f3297c7f9091b2e9f16152782d.png)

>?
>
>Ckafka相关SASL和ACL，用户管理访问控制详情见（https://cloud.tencent.com/document/product/597/31528 ）文档。
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

