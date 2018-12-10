CKafka支持配置SASL鉴权和ACL规则，增强对公网/内网传输中的用户访问控制，增加对topic等资源的生产消费权限控制。
当前该功能在灰度中，如有需求可以[工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=335&source=0&data_title=%E6%B6%88%E6%81%AF%E9%98%9F%E5%88%97CMQ/CKAFKA/IoT%20MQ&step=1)开通白名单试用。

### 配置步骤说明

#### 1. 创建实例
控制台创建CKafka实例

#### 2. 添加路由，选取SASL的鉴权
在添加路由策略时，路由类型选取公网域名接入
接入方式选取SASL_PLAINTEXT。

![Alt text](./1543931400680.png)

#### 3. 配置用户信息（CKafka实例/client端）

##### 3.1 client端配置
在CKafka实例的用户管理页面，点击新建，创建用户
![Alt text](./1543931477646.png)

输入用户名、密码信息，增加用户
![Alt text](./1543931486494.png)

##### 3.2 CKafka实例配置

1. 在client.properties配置文件中 增加如下配置

```
sasl.mechanism=PLAIN
security.protocol=SASL_PLAINTEXT
```

2. 配置用户名及密码

```
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginM
odule required
username="INSTANCE-2#admin" password="admin";
```

其中，sasl.jaas.config部分username和password说明如下： 
- username包含实例名和用户名，使用 ‘#’ 拼接，实例名为客户端需要连接的CKafka实例，通过腾讯云控制台可查看，用户名可通过**控制台ACL模块**进行设置。
- password部分为用户名对应的密码。

#### 4. 配置ACL策略

ACL策略管理中，支持添加ACL策略，步骤如下
1. 选择需要配置策略的topic资源，点击编辑ACL策略
2. 配置用户及ip，不选为默认所有用户/host都支持
> ACL策略示例： 允许/拒绝 用户 user 通过 ip 读/写 topic资源  resource
![Alt text](./1543932107527.png)

> 说明
- 开通路由只影响接入时的验证方式，设置的ACL权限则是全局的
- 假如开通公网访问路由的同时还使用了PLAINTEXT方式接入kafka，之前为topic设置的ACL仍然会生效，如果希望PLAINTEXT方式的访问不受影响，需要通过api为实例添加`ANONYMOUS`用户，然后为PLAINTEXT需要访问的topic添加`ANONYMOUS`用户的可读写的权限。

#### 5. 连通性测试

##### 5.1 kafka自带工具脚本
将SASL_PLAINTEXT方式需要的配置写入producer.properties文件中，运行下列命令生产消息：
```bash
/yourkafka/bin/kafka-console-producer.sh --broker-list yourservers --topic yourtopic --producer.config producer.properties
```

将SASL_PLAINTEXT方式需要的配置写入consumer.properties文件中，运行如下命令消费消息：
```bash
/yourkafka/bin/kafka-console-consumer.sh --bootstrap-server yourservers --from-beginning --new-consumer --topic yourtopic --consumer.config consumer.properties
```

##### 5.2 java客户端
ckafka的server使用了CA认证的证书，而java自带了根证书，因此不需要指定证书
如果使用其他方式接入，则替换相关配置即可
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


##### 5.3 kafka-python 1.3.5客户端
python与java的配置参数有一些区别，因此这里列出了各种方式
```python
#ssl_calfile        信任证书pem存放路径
#                   因为服务器的证书为root认证，因此从https://www.digicert.com/digicert-root-certificates.htm下载即可
#yourinstance       需要连接的CKafka实例，通过腾讯云控制台可查看
#yourusername       可通过控制台ACL模块进行设置
#yourpassword       用户名对应的密码。
#brokers            实例对应的域名或ip:port

#SASL_PLAINTEXT:
producer = KafkaProducer (
    bootstrap_servers=brokers,
    ssl_check_hostname=False,
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism='PLAIN',
    sasl_plain_username='yourinstance#yourusername',
    sasl_plain_password='yourpassword',
)

consumer = KafkaConsumer (
   'yourtopic',
    auto_offset_reset='earliest',
    bootstrap_servers=brokers,
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism='PLAIN',
    sasl_plain_username='yourinstance#youruser',
    sasl_plain_password='yourpassword'
)

#SASL_SSL:
producer = KafkaProducer(
    bootstrap_servers=brokers,
    security_protocol='SASL_SSL',
    ssl_cafile='DigiCertGlobalRootCA.pem',
    ssl_check_hostname=False,
    sasl_mechanism='PLAIN',
    sasl_plain_username='yourinstance#youruser',
    sasl_plain_password='yourpassword'
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
)

#SSL:
producer = KafkaProducer(
    bootstrap_servers=brokers,
    client_id='yourinstance#youruser#yourpassword#yourclientid',
    security_protocol='SSL',
    ssl_check_hostname=False,
    ssl_cafile='DigiCertGlobalRootCA.pem'
)
consumer = KafkaConsumer (
    'yourtopic',
    auto_offset_reset='earliest',
    bootstrap_servers=brokers,
    client_id='yourinstance#youruser#yourpassword#yourclientid',
    security_protocol='SSL',
    ssl_cafile='DigiCertGlobalRootCA.pem',
    ssl_check_hostname=False
)
```
更多python-kafka配置及用法参考[文档](https://kafka-python.readthedocs.io/en/master/apidoc/modules.html)


