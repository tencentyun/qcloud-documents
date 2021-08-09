## 操作场景

如果您需要通过公网访问消息队列 CKafka 服务，例如消费者或者生产者处于自建机房或其他云服务时，可以通过控制台增加公网路由，并通过配置 SASL 鉴权和 ACL 规则实现公网访问 CKafka 的 Topic 并生产和消费消息。


## 前提条件

已 [创建实例](https://cloud.tencent.com/document/product/597/53207)。
已 [创建 Topic](https://cloud.tencent.com/document/product/597/20247)。

## 操作步骤

### 创建公网路由

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏选择【实例列表】，单击目标实例 ID，进入实例基本信息页面。
3. 在实例基本信息页面，单击【接入方式】模块的【添加路由策略】。
   - 路由类型：公网域名接入
   - 接入方式：目前只支持 SASL_PLAINTEXT
     ![](https://main.qcloudimg.com/raw/65be6a54e2a2abcf1cd5c3b1507dca7d.png)
4. 单击【提交】，接入方式下将显示该路由策略。
   ![](https://main.qcloudimg.com/raw/642337483d8e59cbdc55cb96e81faf4b.png)




### 创建用户

1. 在实例基本信息页面，选择顶部的【用户管理】页签。
2. 在用户管理页面，单击【新建】，填写用户名和密码，创建一个用户。
   ![](https://main.qcloudimg.com/raw/971325c47e11c07ee728f82b50d54a7b.png)
3. 单击【提交】，新增的用户将显示在用户管理列表中。
   ![](https://main.qcloudimg.com/raw/c427790899d8ff8e0d4d8f88ddd126fe.png)

### ACL 策略授权

对现有 Topic 进行 ACL 权限管理（包括读写），只有拥有权限的用户才能对 Topic 进行相关读写权限操作。

1. 在实例详情页面，选择顶部的【ACL策略管理】页签。
2. 单击目标 Topic 操作列的【编辑ACL策略】，进入ACL策略页面。
3. 单击【新建】，填选配置用户及 IP，不选为默认所有用户/host 都支持。
   ![](https://main.qcloudimg.com/raw/632c3903a52bb1c71860b1dbd40ed43a.png)
4. 单击【提交】，该策略将显示在目标  Topic  的策略列表中。
   ![](https://main.qcloudimg.com/raw/f97473b3031d97efa6ae4aeec16560d9.png)

>?CKafka 相关 SASL 和 ACL，详情见 [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528) 文档。

### 公网生产和消费

控制台操作完成后，即可使用用户名和密码在公网访问实例资源。

#### 生产

```java
Properties props = new Properties();
        //公网接入域名地址,即公网路由地址,在实例详情页的接入方式模块获取。
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
        //用户名和密码，注：用户名是需要拼接，并非控制台的用户名：instanceId#username。
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
        //公网接入域名地址,即公网路由地址,在实例详情页的接入方式模块获取。
        props.put("bootstrap.servers", "your_public_network_route_addr");
        props.put("group.id", "yourconsumegroup");
        props.put("enable.auto.commit", "true");
        props.put("auto.commit.interval.ms", "1000");
        props.put("session.timeout.ms", "30000");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
        props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");
        //用户名和密码，注：用户名是需要拼接，并非控制台的用户名：instanceId#username。
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

>?除了使用 properties 添加 sasl.jaas.config 配置的方式，您也可以通过 System.setProperty 或 -D 的方式传入。
>
>- System.setProperty("java.security.auth.login.config", "/etc/ckafka_client_jaas.conf");

ckafka_client_jaas.conf` 文件的内容如下：

```java
KafkaClient {
	org.apache.kafka.common.security.plain.PlainLoginModule required
	username="yourinstance#yourusername"
  password="yourpassword";
}; 
```

>?username 是`实例 ID` + `#` + `配置的用户名`，password 是配置的用户密码。

