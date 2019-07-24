## 操作场景
该任务指导您在使用消息队列 CKafka 时，通过控制台配置 SASL 鉴权和 ACL 规则，增强对公网/内网传输中的用户访问控制，增加对 Topic 等资源的生产消费权限控制。
>?
- Kafka 提供了多种安全认证机制，主要分为 SSL 和 SASL2 大类。其中 SASL/PLAIN 是基于账号密码的认证方式，比较常用。CKafka 支持 SASL_PLAINTEXT 认证。
- ACL 访问控制列表（Access Control List），帮助用户定义一组权限规则，允许/拒绝用户 user 通过 IP 读/写 Topic 资源  resource。

## 前提条件
该功能目前处于灰度测试阶段，如需试用请通过 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=335&source=0&data_title=%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97CMQ/CKAFKA/IoT%20MQ&step=1) 的方式开通白名单。

## 操作步骤

###  创建实例
单击实例列表页的【新建】，创建并购买实例。详情请参见 [创建实例](https://cloud.tencent.com/document/product/597/30931) 文档。


### 配置用户信息
您可以通过 Client 端或 CKafka 实例两种方式配置用户信息。

####  Client 端配置
1. 在 CKafka 实例的用户管理页面，单击【新建】，创建用户。
![](https://main.qcloudimg.com/raw/f164bde6857b4a0a23b69ccfd41f5c8e.png)
2. 输入用户名和密码信息，单击【提交】完成用户新增。
![](https://main.qcloudimg.com/raw/8c8e2e57d320ba2b25e0aecf0dbb3b28.png)

####  CKafka 实例配置
1. 在配置文件（参见 [配置文件示例](#配置文件示例)）中，增加如下配置：
```
sasl.mechanism=PLAIN
security.protocol=SASL_PLAINTEXT
```
2. 配置用户名及密码：
```
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="instanceId#admin" password="admin";
```
其中，sasl.jaas.config 部分的 username 和 password 说明如下： 
 - username：包含实例 ID 和用户名，使用`#`拼接，实例 ID 为客户端需要连接的 CKafka 实例（可通过腾讯云控制台可查看该实例），用户名可通过**控制台 ACL 策略管理模块**进行设置。
 - password：部分为用户名对应的密码。
 
**配置文件示例**<span id="配置文件示例"></span>
- 生产者配置文件名称为 producer.properties，SASL_PLAINTEXT 相关配置如下：
```
sasl.mechanism=PLAIN
security.protocol=SASL_PLAINTEXT
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="INSTANCE-2#admin" password="admin";
```
- 消费者配置文件名称为 consumer.properties，SASL_PLAINTEXT 相关配置如下：
```
sasl.mechanism=PLAIN
security.protocol=SASL_PLAINTEXT
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="INSTANCE-2#admin" password="admin";
```

###  配置 ACL 策略
1. 在 ACL 策略管理列表页，选择需要配置策略的 Topic 资源，单击操作列的【编辑 acl 策略】。
2. 在新增 ACL 策略的弹窗中，填选配置用户及 IP，不选为默认所有用户/host 都支持。
    ACL 策略示例： 允许/拒绝用户 user 通过 IP 读/写 Topic 资源  resource。
![](https://main.qcloudimg.com/raw/09d00ca8725b9f8ad080a05f5f3b8f7f.png)

>?
- 开通路由只影响接入时的验证方式，设置的 ACL 权限则是全局的。
- 如果您在开通公网访问路由的同时还使用了 PLAINTEXT 方式接入 Kafka，那么之前为  Topic 设置的 ACL 仍然会生效；如果希望 PLAINTEXT 方式的访问不受影响，则需要通过 API 为实例添加`ANONYMOUS`用户，并为 PLAINTEXT 需要访问的 Topic 添加`ANONYMOUS`用户的可读写的权限。

###  连通性测试
####  Kafka 自带工具脚本

将 SASL_PLAINTEXT 方式需要的配置写入 producer.properties（配置内容参见 [配置文件示例](#配置文件示例)）文件中，运行下列命令生产消息：
```bash
/yourkafka/bin/kafka-console-producer.sh --broker-list yourservers --topic yourtopic --producer.config producer.properties
```
将 SASL_PLAINTEXT 方式需要的配置写入 consumer.properties（配置内容参见 [配置文件示例](#配置文件示例)）文件中，运行如下命令消费消息：
```bash
/yourkafka/bin/kafka-console-consumer.sh --bootstrap-server yourservers --from-beginning --new-consumer --topic yourtopic --consumer.config consumer.properties
```

####  Java 客户端
Ckafka 的 Server 使用了 CA 认证的证书，而 Java 自带了根证书，因此不需要指定证书。
如果您使用其他方式接入，则只需替换相关配置即可。
```java
//SASL_PLAINTEXT
Properties props = new Properties();
props.put("bootstrap.servers", "yourbrokers");
props.put("security.protocol", "SASL_PLAINTEXT");
props.put("sasl.mechanism", "PLAIN");
props.put("session.timeout.ms", 30000);
props.put("key.serializer", "org.apache.kafka.common.serialization.IntegerSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"yourinstance#yourusername\" password=\"yourpassword\";");
org.apache.kafka.clients.producer.KafkaProducer<Integer, String> producer = new org.apache.kafka.clients.producer.KafkaProducer<>(props);


Properties props = new Properties();
props.put("bootstrap.servers", "yourbrokers");
props.put("security.protocol", "SASL_PLAINTEXT");
props.put("sasl.mechanism", "PLAIN");
props.put("key.serializer", "org.apache.kafka.common.serialization.IntegerSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("session.timeout.ms", 30000)
props.put("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"yourinstance#yourusername\" password=\"yourpassword\";");
org.apache.kafka.clients.consumer.KafkaConsumer<Integer, String> consumer = new org.apache.kafka.clients.consumer.KafkaConsumer<>(props);
```

####  Kafka-Python 1.3.5客户端
Python 与 Java 的配置参数有一些区别，具体配置方式如下：
```python
#ssl_calfile        信任证书 pem 存放路径
#                   因为服务器的证书为 root 认证，因此从 https://www.digicert.com/digicert-root-certificates.htm 下载即可
#yourinstance       需要连接的 CKafka 实例，通过腾讯云控制台可查看
#yourusername       可通过控制台 ACL 模块进行设置
#yourpassword       用户名对应的密码
#brokers            实例对应的域名或 ip:port

#SASL_PLAINTEXT:
producer = KafkaProducer (
    bootstrap_servers=brokers,
    ssl_check_hostname=False,
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism='PLAIN',
    sasl_plain_username='yourinstance#yourusername',
    sasl_plain_password='yourpassword',
    api_version=(0,10,0)
)

consumer = KafkaConsumer (
   'yourtopic',
    auto_offset_reset='earliest',
    bootstrap_servers=brokers,
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism='PLAIN',
    sasl_plain_username='yourinstance#youruser',
    sasl_plain_password='yourpassword',
    api_version=(0,10,0)
)

#SASL_SSL:
producer = KafkaProducer(
    bootstrap_servers=brokers,
    security_protocol='SASL_SSL',
    ssl_cafile='DigiCertGlobalRootCA.pem',
    ssl_check_hostname=False,
    sasl_mechanism='PLAIN',
    sasl_plain_username='yourinstance#youruser',
    sasl_plain_password='yourpassword',
    api_version=(0,10,0)
)
consumer = KafkaConsumer (
    'yourtopic',
    auto_offset_reset='earliest',
    bootstrap_servers=brokers,
    security_protocol='SASL_SSL',
    ssl_cafile='DigiCertGlobalRootCA.pem',
    ssl_check_hostname=False,
    sasl_mechanism='PLAIN',
    sasl_plain_username='yourinstance#youruser',
    sasl_plain_password='yourpassword',
    api_version=(0,10,0)
)

#SSL:
producer = KafkaProducer(
    bootstrap_servers=brokers,
    client_id='yourinstance#youruser#yourpassword#yourclientid',
    security_protocol='SSL',
    ssl_check_hostname=False,
    ssl_cafile='DigiCertGlobalRootCA.pem',
    api_version=(0,10,0)
)
consumer = KafkaConsumer (
    'yourtopic',
    auto_offset_reset='earliest',
    bootstrap_servers=brokers,
    client_id='yourinstance#youruser#yourpassword#yourclientid',
    security_protocol='SSL',
    ssl_cafile='DigiCertGlobalRootCA.pem',
    ssl_check_hostname=False,
    api_version=(0,10,0)
)
```
更多配置及用法请参考 [Python-Kafka 文档](https://kafka-python.readthedocs.io/en/master/apidoc/modules.html) 。


