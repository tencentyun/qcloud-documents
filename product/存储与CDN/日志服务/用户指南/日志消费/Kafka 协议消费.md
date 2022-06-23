## 概述
您可以通过 Kafka 协议消费，将采集到日志服务（Cloud Log Service，CLS）的数据，消费到下游的大数据组件或者数据仓库。例如，Kafka、HDFS、Hive、Flink，以及腾讯云产品 Oceanus、EMR 等。   

本文提供了 Flink、Logstash 消费日志主题的 demo。


### 支持的 Kafka 协议版本
Kafka 1.1.1及更早的版本

### 内网消费和外网消费说明
- 内网和外网的定义：例如您在广州地域的日志主题，使用 Kafka 消费协议，消费到广州地域的腾讯云 Oceanus，则属于内网消费。若消费到上海地域的腾讯云 Oceanus，则属于外网消费。
- 计费的区别：内网流量费用0.18元/GB，外网流量费用0.8元/GB。
- 消费服务域名的区别：在控制台页面会给出内网服务域名和外网服务域名，请按需选择。

## 前提条件
- 已开通日志服务，创建日志集与日志主题，并成功采集到日志数据。   
- 确保当前操作账号拥有开通 Kafka 协议消费的权限，权限问题请参见 [自定义权限策略示例](https://cloud.tencent.com/document/product/614/68374)。


## 操作步骤[](id:steps)

1. 登录日志服务控制台，选择左侧导航栏中的 **[日志主题](https://console.cloud.tencent.com/cls/topic)**。
3. 在“日志主题”页面，单击需要使用 Kafka 协议消费的日志主题 ID/名称，进入日志主题管理页面。
4. 在日志主题管理页面中，单击 **Kafka协议消费** 页签。
5. 单击右侧的**编辑**，将“当前状态”的开关按钮设置为打开状态后，单击**确定**。
6. 根据 CLS 给出消费的 Topic 信息，构造消费者。完成后如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e3b9925ff0542efb8470a74a7e76bf3d.png)


## Flink 消费 CLS 日志

### 开启日志的 kafka 消费协议
参考 [操作步骤](#steps) 开启日志的 kafka 消费协议，并获取消费的服务域名和 Topic。


### 确认 flink-connector-kafka 依赖 
确保 flink lib 中有 flink-connector-kafka 后，直接在 sql 中注册 kafka 表即可使用。依赖如下：
```xml
<dependency>
  <groupId>org.apache.flink</groupId>
  <artifactId>flink-connector-kafka</artifactId>
  <version>1.14.4</version>
</dependency>
```

### 注册 flink 表
```sql
CREATE TABLE `nginx_source`
(
    `@metadata` STRING,     -- 日志中字段
    `@timestamp` TIMESTAMP, -- 日志中字段
    `agent` STRING,         -- 日志中字段
    `ecs` STRING,           -- 日志中字段
    `host` STRING,          -- 日志中字段
    `input` STRING,         -- 日志中字段
    `log` STRING,           -- 日志中字段
    `message` STRING,       -- 日志中字段
    `partition_id` BIGINT METADATA FROM 'partition' VIRTUAL,    -- kafka分区
    `ts` TIMESTAMP(3) METADATA FROM 'timestamp'                 
)  WITH (
  'connector' = 'kafka',
  'topic' = 'YourTopic',  -- cls kafka协议消费控制台给出的的主题名称，例如out-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX 
  'properties.bootstrap.servers' = 'kafkaconsumer-ap-guangzhou.cls.tencentcs.com:9096',   -- cls kakfa协议消费控制台给出的服务地址，例子中是广州地域的外网消费地址，请按照您的实际情况填写
  'properties.group.id' = 'kafka_flink', -- kafka 消费组名称
  'scan.startup.mode' = 'earliest-offset', 
  'format' = 'json',
  'json.fail-on-missing-field' = 'false', 
  'json.ignore-parse-errors' = 'true' ,
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="your username" password="your password";',--用户名是日志主题所属的日志集合ID，例如ca5cXXXX-dd2e-4ac0-af12-92d4b677d2c6，密码是用户的secretid#secrectkey组合的字符串，比AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#。
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN'
);
```

### 查询使用
执行成功后，即可查询使用。
```sql
select count(*) , host from nginx_source group by host;
```

## Flume 消费 CLS 日志
若您需将日志数据消费到自建的 HDFS，Kafka 集群，则可以通过 Flume 组件来中转，具体操作参考如下示例。


### 开启日志的 kafka 消费协议
参考 [操作步骤](#steps) 开启日志的 kafka 消费协议，并获取消费的服务域名和 Topic。

### Flume 配置

```
a1.sources = source_kafka
a1.sinks = sink_local
a1.channels = channel1

// 配置Source
a1.sources.source_kafka.type = org.apache.flume.source.kafka.KafkaSource
a1.sources.source_kafka.batchSize = 10
a1.sources.source_kafka.batchDurationMillis = 200000
a1.sources.source_kafka.kafka.bootstrap.servers = kafkaconsumer-ap-guangzhou.cls.tencentcs.com:9096 --cls kakfa协议消费控制台给出的服务地址，例子中是广州地域的外网消费地址，请按照您的实际情况填写
a1.sources.source_kafka.kafka.topics = YourClsTopic -- cls kafka协议消费控制台给出的的主题名称,例如out-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX 
a1.sources.source_kafka.kafka.consumer.group.id = cls_flume_kafka
a1.sources.source_kafka.kafka.consumer.auto.offset.reset = earliest
a1.sources.source_kafka.kafka.consumer.security.protocol = SASL_PLAINTEXT
a1.sources.source_kafka.kafka.consumer.sasl.mechanism = PLAIN
a1.sources.source_kafka.kafka.consumer.sasl.jaas.config = org.apache.kafka.common.security.plain.PlainLoginModule required username="YourUsername" 
password="YourPassword";--用户名是日志主题所属的日志集合ID，例如ca5cXXXX-dd2e-4ac0-af12-92d4b677d2c6，密码是用户的secretid#secrectkey组合的字符串，例如AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#



//配置sink
a1.sinks.sink_local.type = logger

a1.channels.channel1.type = memory
a1.channels.channel1.capacity = 1000
a1.channels.channel1.transactionCapacity = 100

//将source和sink绑定到channel
a1.sources.source_kafka.channels = channel1
a1.sinks.sink_local.channel = channel1
```


## Python SDK
```
import uuid
from kafka import KafkaConsumer,TopicPartition,OffsetAndMetadata
consumer = KafkaConsumer(
//将控制台中的主题名称填写到此处，您将使用这个topic进行消费    
'out-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX',  
group_id = uuid.uuid4().hex,
auto_offset_reset='earliest',
//Kafka协议服务地址，将上图中服务接入信息填写到此处，如果您是在外网消费，请填写
外网服务域名+端口，如果您在内网消费，请填写内网服务域名+端口。例子中使用的是内网服务。
bootstrap_servers = ['kafkaconsumer-ap-guangzhou.cls.tencentyun.com:9096'],
security_protocol = "SASL_PLAINTEXT",
sasl_mechanism = 'PLAIN',   
//SASL信息，将日志主题所属的日志集id填入此处   
sasl_plain_username = "ca5cXXXX-dd2e-4ac0-af12-92d4b677d2c6",
//SASL信息，#填入用户的secretid#secrectkey组合的字符串，注意不要丢失#
sasl_plain_password = "AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac",
api_version = (1,1,1)
)
print('begin')
for message in consumer:
    print('begins')
    print ("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" % (message.topic, message.partition, message.offset, message.value))
    print('end')
```
