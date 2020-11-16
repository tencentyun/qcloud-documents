
本文以一个简单案例来说明数据订阅中拉取对应表到 Kafka 的功能，并提供简易 [KafkaDemo 下载](https://main.qcloudimg.com/raw/cf803ad5ddbb3f20534d98a5a0a23334/KafkaDemo.zip)。

## 配置环境
- 操作系统：CentOS
- 相关下载
 - [数据订阅 SDK](https://subscribesdk-1254408587.cos.ap-beijing.myqcloud.com/binlogsdk-2.8.2-jar-with-dependencies.jar?_ga=1.22270587.1971922487.1581299091)
 - [SLF4J 组件](https://main.qcloudimg.com/raw/f8a577788af1d57cd269410fbe436a35/SLF4J.zip)
 - [Kafka-clients](https://main.qcloudimg.com/raw/a60f793a4eafe5f77e63615c5ce920e8/kafka-clients-1.1.0.jar)
- Java 环境配置 
```
yum install java-1.8.0-openjdk-devel 
```

## 安装 Kafka 
1. 请参考 [Kafka 介绍](http://kafka.apache.org/quickstart) 安装 Kafka。
2. 启动之后创建一个 testtop 主题。
```
[root@VM_71_10_centos kafka_2.11-1.1.0]# bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testtop
Created topic "testtop".
```

## 获取密钥
登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 获取密钥。

## 选择数据订阅
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dtsnew/migrate/page)，选择左侧的【数据订阅】，进入数据订阅页面。
2. 在订阅列表，单击订阅名，进入订阅详情页，查看对应的通道 ID、服务 IP 和服务端口。
3. 结合之前的密钥填写到对应 KafkaDemo.java 里。
```
  // 从访问管理控制台获取的密钥，填写到此处      
 final String TOPIC = "testtop";  订阅的主题
        Properties props = new Properties();
	props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092"); 填写 kafka 对应的 ip:port
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        final Producer<String, String> producer = new KafkaProducer<String, String>(props);
               context.setSecretId("AKIDfdsfdsfsdt1331431sdfds"); 填写获取的 secretID
        context.setSecretKey("test111usdfsdfsddsfRkeT"); 填写获取的 secretKey
	// 从订阅详情页获取的ip，port，填写到此处
        context.setServiceIp("10.66.112.181"); 填写获取的 IP
        context.setServicePort(7507); 填写获取的 PORT
        final DefaultSubscribeClient client = new DefaultSubscribeClient(context);
	// 填写对应要同步的数据库和表名，并修改对应要落地存储的文件名
        final String targetDatabase = "test"; 填写要订阅的库名
                 client.addClusterListener(listener);
	// 订阅详情页获取的 dts-channel 配置信息，填写到此处
	client.askForGUID("dts-channel-e4FQxtYV3It4test"); 填写您获取的通道 ID
        client.start();
```


##  编译操作与检验
1. 编译客户端程序 KafkaDemo.java。
```
javac -classpath binlogsdk-2.6.0-release.jar:slf4j-api-1.7.25.jar:slf4j-log4j12-1.7.2.jar:kafka-clients-1.1.0.jar -encoding UTF-8 KafkaDemo.java 
```
2. 执行启动，如无异常报错即为正常在服务。
```
java -XX:-UseGCOverheadLimit -Xms2g -Xmx2g  -classpath .:binlogsdk-2.6.0-release.jar:kafka-clients-1.1.0.jar:slf4j-api-1.7.25.jar:slf4j-log4j12-1.7.2.jar  KafkaDemo
```
3. 通过对表 alantest 插入一条数据，发现在 Kafka 订阅的 testtop 里面能看到已经有数据过来了。

```
MySQL [test]> insert into alantest values(123456,'alan');
Query OK, 1 row affected (0.02 sec)

[root@VM_71_10_centos kafka_2.11-1.1.0]#  bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testtop --from-beginning 
checkpoint:144251@3@1275254@1153089
record_id:00000100000000001198410000000000000001
record_encoding:utf8
fields_enc:latin1,utf8
gtid:4f21864b-3bed-11e8-a44c-5cb901896188:5552
source_category:full_recorded
source_type:mysql
table_name:alantest
record_type:INSERT
db:test
timestamp:1524649133
primary:id

Field name: id
Field type: 3
Field length: 6
Field value: 123456
Field name: name
Field type: 253
Field length: 4
Field value: alan
```

