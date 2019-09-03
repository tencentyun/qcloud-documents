本文将以一个简单案例来说明数据订阅中拉取对应表到 Kafka 的功能，并且提供简易 [KaflkaDemo 下载](https://main.qcloudimg.com/raw/cf803ad5ddbb3f20534d98a5a0a23334/KafkaDemo.zip) 。以下操作将在 Centos 操作系统中完成。

## 配置环境
- Java环境配置 
```
yum install java-1.8.0-openjdk-devel 
```
- 相关下载
 - [数据订阅 SDK](https://main.qcloudimg.com/raw/2aa7b213535065def5655712c8494182/binlogsdk-2.7.0-official.jar)
 - [SLF4J 组件](https://main.qcloudimg.com/raw/f8a577788af1d57cd269410fbe436a35/SLF4J.zip)
 - [Kafka-clients](https://main.qcloudimg.com/raw/a60f793a4eafe5f77e63615c5ce920e8/kafka-clients-1.1.0.jar)

## 安装 Kafka 
具体请参考 [Kafka 介绍](http://kafka.apache.org/quickstart)。
启动之后创建一个 testtop 主题。
```
[root@VM_71_10_centos kafka_2.11-1.1.0]# bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testtop
Created topic "testtop".
```

## 获取密钥
登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 获取密钥。

## 选择数据订阅
1. 登录 [DTS 控制台](https://console.cloud.tencent.com/dtsnew/migrate/page)，选择左侧的【数据订阅】，进入数据订阅页面。
2. 选择需同步的 TencentDB 实例名，然后单击启动，再返回数据订阅，单击您所创建的数据订阅。 详细介绍请参考 [如何获取数据订阅](https://cloud.tencent.com/document/product/571/13707)。
3. 查看对应的 DTS 通道、IP 和 Port，然后结合之前的密钥填写到对应 KafkaDemo.java 里面。
```
  // 从云API获取密钥,填写到此处
       
 final String TOPIC = "testtop";  订阅的主题
        Properties props = new Properties();
	props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092"); 输入您的kafka对应ip:port
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        final Producer<String, String> producer = new KafkaProducer<String, String>(props);
               context.setSecretId("AKIDfdsfdsfsdt1331431sdfds"); 请填写您从云API获取的secretID。
        context.setSecretKey("test111usdfsdfsddsfRkeT"); 请填写
        您从云API获取的secretKey.
	// 在数据迁移服务里面通过数据订阅获取到对应的ip,port,填写到此处
        context.setServiceIp("10.66.112.181"); 请填写您从数据订阅配置获取到的IP
        context.setServicePort(7507);
        请填写您从数据订阅配置获取到的PORT
        final DefaultSubscribeClient client = new DefaultSubscribeClient(context);
	// 填写对应要同步的数据库和表名,并修改对应要落地存储的文件名.
        final String targetDatabase = "test"; 填写您所要订阅的库名
                 client.addClusterListener(listener);
	// 通过数据迁移订阅的配置选项获取到dts-channel的配置信息,填写到此处.
	client.askForGUID("dts-channel-e4FQxtYV3It4test"); 请填写您从数据订阅获取的通道dts的名称。
        client.start();
```


##  编译操作与检验
1. 
```
javac -classpath binlogsdk-2.6.0-release.jar:slf4j-api-1.7.25.jar:slf4j-log4j12-1.7.2.jar:kafka-clients-1.1.0.jar -encoding UTF-8 KafkaDemo.java 
```
2. 执行启动，如果没有异常报错就是正常在服务。
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

