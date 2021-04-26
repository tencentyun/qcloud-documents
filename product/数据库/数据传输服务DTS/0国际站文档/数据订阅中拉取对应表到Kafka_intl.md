This document provides a simple example that walks you through how to pull a table from data subscription to Kafka, and an easy [KaflkaDemo Download](https://main.qcloudimg.com/raw/cf803ad5ddbb3f20534d98a5a0a23334/KafkaDemo.zip). We are going through the following procedure in a Centos operating system.
### Environment configuration
1. Java environment configuration 
```
yum install java-1.8.0-openjdk-devel 
```

2. Downloads
 - [Data Subscription SDK](https://mc.qcloudimg.com/static/archive/2a5032c6100b9cb3316f978bb32519e5/binlogsdk-- 2.6.0-release.jar.zip)
 - [SLF4J Components](https://main.qcloudimg.com/raw/f8a577788af1d57cd269410fbe436a35/SLF4J.zip)
 - [Kafka-clients](https://main.qcloudimg.com/raw/a60f793a4eafe5f77e63615c5ce920e8/kafka-clients-1.1.0.jar)

### Install Kafka 
For more information, please see http://kafka.apache.org/quickstart.
After Kafka is launched, create a "testtop" topic.
```
[root@VM_71_10_centos kafka_2.11-1.1.0]# bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testtop
Created topic "testtop".
```
### Obtain a key
Log in to the [Tencent Cloud console](https://console.cloud.tencent.com/), and click **Cloud Products** -> **Management Tools** -> **Cloud API Key** in the navigation bar, or you can also click here to enter the [Cloud Database console](https://console.cloud.tencent.com/cam/capi).

![](https://main.qcloudimg.com/raw/c6fa15fc47536b875448f911b00ed290.png)

### Select data subscription
1. Log in to the [DTS console](https://console.cloud.tencent.com/dtsnew/migrate/page), and select **Data Subscription** on the left to go to the Data Subscription page.
2. Click the name of a TencentDB instance to be synced to launch it. Then, go back to Data Subscription, and click the data subscription you have created. For more information, please see [How to Obtain Data Subscription](https://cloud.tencent.com/document/product/571/13707).
3. Check the corresponding DTS tunnel, IP, and Port, and enter the key you previously obtained in the KafkaDemo.java file.
```
  // Enter the key obtained from the cloud API
       
 final String TOPIC = "testtop";  Subscription topic
        Properties props = new Properties();
	props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092"); Enter the ip:port of your kafka
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        final Producer<String, String> producer = new KafkaProducer<String, String>(props);
               context.setSecretId("AKIDfdsfdsfsdt1331431sdfds");  Enter the secretID obtained from the cloud API
        context.setSecretKey("test111usdfsdfsddsfRkeT"); Enter
        the secretKey obtained from the cloud API.
	// Enter the ip:port obtained through the data subscription in the data migration service
        context.setServiceIp("10.66.112.181"); Enter the IP obtained from the data subscription configuration
        context.setServicePort(7507);
        Enter the PORT obtained from the data subscription configuration
        final DefaultSubscribeClient client = new DefaultSubscribeClient(context);
	// Enter the names of both database and table to be synced, and modify the name of the file where they are stored
        final String targetDatabase = "test"; Enter the name of the database to be subscribed to
                 client.addClusterListener(listener);
	// Enter the configuration information of dts-channel obtained from the configuration option subscribed to through the data migration
	client.askForGUID("dts-channel-e4FQxtYV3It4test"); Enter the name of the channel "dts" obtained from the data subscription
        client.start();
```




### Compiling and test
1. 
```
javac -classpath binlogsdk-2.6.0-release.jar:slf4j-api-1.7.25.jar:slf4j-log4j12-1.7.2.jar:kafka-clients-1.1.0.jar -encoding UTF-8 KafkaDemo.java 
```

2. Once launched, the data subscription works normally if no exception occurs.
```
java -XX:-UseGCOverheadLimit -Xms2g -Xmx2g  -classpath .:binlogsdk-2.6.0-release.jar:kafka-clients-1.1.0.jar:slf4j-api-1.7.25.jar:slf4j-log4j12-1.7.2.jar  KafkaDemo
```

3. You can see the data that has been stored in the "testtop" subscribed to by Kafka by inserting a data record into the table "alantest."

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


