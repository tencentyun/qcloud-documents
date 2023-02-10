## 概述

使用 Kafka 协议消费功能，您可以将一个日志主题，当作一个 Kafka Topic 来消费。在实际使用场景中，通过使用 Kafka Consumer 或者开源社区提供的 Kafka  connectors，如 flink-connector-kafka、Kafka-connector-jdbc 等，将采集到的日志数据，消费到下游的大数据组件或者数据仓库。例如 Spark、HDFS、Hive、Flink，以及腾讯云产品 Oceanus、EMR 等。

本文提供了 Flink、Flume 消费日志主题的 demo。

## 前提条件

- 已开通日志服务，创建日志集与日志主题，并成功采集到日志数据。   
- 确保当前操作账号拥有开通 Kafka 协议消费的权限，权限问题请参见 [自定义权限策略示例](https://cloud.tencent.com/document/product/614/68374#kafka-.E5.8D.8F.E8.AE.AE.E6.B6.88.E8.B4.B9)。


## 相关限制

- 支持 Kafka 协议版本为：1.1.1及更早的版本。
- 支持压缩方式：snappy，lz4。
- 用户认证方式：SASL_PLAINTEXT。
- 目前仅支持当前数据消费，不支持历史数据的消费。
- Topic 中的数据保留时间为2小时。




### 内网消费和外网消费说明

- **内网消费**：使用内网域名进行日志消费，流量费用为0.18元/GB。例如您的原始日志为100GB，消费时选择 Snappy 压缩，那么计量约为50GB，内网读流量费用为50GB * 0.18元，即9元。一般来说，如果您的消费端和日志主题在同一个 VPC 或者同一个地域，就可以使用内网消费。
- **外网消费**：使用外网域名进行日志消费，流量费用为0.8元/GB。例如您的原始日志为100GB，消费时选择 Snappy 压缩，那么计量约为50GB，外网读流量费用为50GB * 0.8元，即40元。一般来说，如果您的消费端和日志主题不在同一个 VPC，也不在同一个地域，需要使用外网消费。

![](https://qcloudimg.tencent-cloud.cn/raw/25badd05f8c18e2dd0fadaba81bec3dc.png)

[](id:steps)
## 操作步骤


1. 登录日志服务控制台，选择左侧导航栏中的 **[日志主题](https://console.cloud.tencent.com/cls/topic)**。
2. 在“日志主题”页面，单击需要使用 Kafka 协议消费的日志主题 ID/名称，进入日志主题管理页面。
3. 在日志主题管理页面中，单击**Kafka 协议消费**页签。
4. 单击右侧的**编辑**，将“当前状态”的开关按钮设置为打开状态后，单击**确定**。
5. 控制台给出 Topic、host+port 的信息。用户可以复制信息，构造消费者 SDK。 
![](https://qcloudimg.tencent-cloud.cn/raw/eccefedec25a68f6c3b1337fc24198a4.png)


## 消费者参数说明

Kafka 协议消费者的参数说明如下：

<table>
<thead>
<tr><th style="width: 20%">参数</th><th>说明</th></tr>
</thead>
<tbody><tr>
<td>用户认证方式</td>
<td>目前仅支持 SASL_PLAINTEXT。</td>
</tr>
<tr>
<td>hosts</td>
<td>内网消费:kafkaconsumer-${region}.cls.tencentyun.com:9095。

外网消费:kafkaconsumer-${region}.cls.tencentcs.com:9096，详细参见 <a href="https://cloud.tencent.com/document/product/614/18940#Kafka_Consume">可用域名- Kafka 消费日志</a>。</td>
</tr>
<tr>
<td>topic</td>
<td>CLS kafka 协议消费控制台给出的主题名称,点击旁边按钮可以复制。例如XXXXXX-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX。</td>
</tr>
<tr>
<td>username</td>
<td>配置为${logsetID}，即日志集 ID。  例如：0f8e4b82-8adb-47b1-XXXX-XXXXXXXXXXXX ，在日志主题列表中可以复制日志集 ID。</td>
</tr>
<tr>
<td>password</td>
<td>配置为<code>${SecretId}#${SecretKey}</code>。例如：XXXXXXXXXXXXXX#YYYYYYYY，请登录 <a href="https://console.cloud.tencent.com/cam">腾讯云访问管理</a> ，在左侧导航栏中单击<b>访问密钥</b>，API 密钥或者项目密钥均可使用，建议使用子账号密钥，为子账号授权时，遵循最小权限原则，即子账号的访问策略中的 action、resource 都配置为最小范围，可以满足操作即可。</td>
</tr>
</tbody></table>

>!下面的例子中的代码，jaas.config 的配置，<code>${SecretId}#${SecretKey}</code>后有(;分号)，不要漏填，否则会报错。
## Python SDK

```
import uuid
from kafka import KafkaConsumer,TopicPartition,OffsetAndMetadata
consumer = KafkaConsumer(
#cls kafka协议消费控制台给出的的主题名称，例如XXXXXX-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX,可在控制台复制
'您的消费主题',  
group_id = uuid.uuid4().hex,
auto_offset_reset='earliest',
#服务地址+端口，外网端口9096，内网端口9095,例子是内网消费，请根据您的实际情况填写
bootstrap_servers = ['kafkaconsumer-${region}.cls.tencentyun.com:9095'],
security_protocol = "SASL_PLAINTEXT",
sasl_mechanism = 'PLAIN',   
#用户名是日志集合ID，例如ca5cXXXXdd2e-4ac0af12-92d4b677d2c6  
sasl_plain_username = "${logsetID}",
#密码是用户的SecretId#SecretKey组合的字符串，比AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#。建议使用子账号密钥,为子账号授权时,遵循最小权限原则,即子账号的访问策略中的action、resource都配置为最小范围,可以满足操作即可.
sasl_plain_password = "${SecretId}#${SecretKey}",
api_version = (1,1,1)
)
print('begin')
for message in consumer:
    print('begins')
    print ("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" % (message.topic, message.partition, message.offset, message.value))
    print('end')
```

## 腾讯云 Oceanus 消费 CLS 日志
在 Oceanus 控制台新建作业。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5318b551bc537acb4bff0904361a2f6b.png)

```
CREATE TABLE `nginx_source`
(   # 日志中字段
    `@metadata` STRING,     
    `@timestamp` TIMESTAMP, 
    `agent` STRING,         
    `ecs` STRING,           
    `host` STRING,          
    `input` STRING,         
    `log` STRING,           
    `message` STRING,       
    `partition_id` BIGINT METADATA FROM 'partition' VIRTUAL,    -- kafka分区
    `ts` TIMESTAMP(3) METADATA FROM 'timestamp'                 
)  WITH (
  'connector' = 'kafka',
  #cls kafka协议消费控制台给出的的主题名称，例如XXXXXX-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX,可在控制台复制
  'topic' = '您的消费主题',  
  # 服务地址+端口，外网端口9096，内网端口9095,列子是内网消费，请根据您的实际情况填写
  'properties.bootstrap.servers' = 'kafkaconsumer-${region}.cls.tencentyun.com:9095',       
    # 请替换为您的消费组名称   
  'properties.group.id' = '您的消费组名称',  
  'scan.startup.mode' = 'earliest-offset', 
  'format' = 'json',
  'json.fail-on-missing-field' = 'false', 
  'json.ignore-parse-errors' = 'true' ,
  #用户名是日志集合ID，例如ca5cXXXXdd2e-4ac0af12-92d4b677d2c6
  #密码是用户的SecretId#SecretKey组合的字符串，比AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#。建议使用子账号密钥,为子账号授权时,遵循最小权限原则,即子账号的访问策略中的action、resource都配置为最小范围,可以满足操作即可,注意jaas.config最后有;分号,不填写会报错.
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="${logsetID}" password="${SecretId}#${SecretKey}";',
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN'
);

```



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
    #日志中的字段
    `@metadata` STRING,     
    `@timestamp` TIMESTAMP, 
    `agent` STRING,        
    `ecs` STRING,           
    `host` STRING,          
    `input` STRING,        
    `log` STRING,           
    `message` STRING, 
    #kafka分区      
    `partition_id` BIGINT METADATA FROM 'partition' VIRTUAL,    
    `ts` TIMESTAMP(3) METADATA FROM 'timestamp'                 
)  WITH (
  'connector' = 'kafka',
  #cls kafka协议消费控制台给出的的主题名称，例如XXXXXX-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX,可在控制台复制
  'topic' = '您的消费主题',  
  # 服务地址+端口，外网端口9096，内网端口9095,列子是内网消费，请根据您的实际情况填写
  'properties.bootstrap.servers' = 'kafkaconsumer-${region}.cls.tencentyun.com:9095', 
   # 请替换为您的消费组名称   
  'properties.group.id' = '您的消费组名称', 
  'scan.startup.mode' = 'earliest-offset', 
  'format' = 'json',
  'json.fail-on-missing-field' = 'false', 
  'json.ignore-parse-errors' = 'true' ,
  #用户名是日志集合ID，例如ca5cXXXXdd2e-4ac0af12-92d4b677d2c6
  #密码是用户的SecretId#SecretKey组合的字符串，比AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#。建议使用子账号密钥,为子账号授权时,遵循最小权限原则,即子账号的访问策略中的action、resource都配置为最小范围,可以满足操作即可,注意jaas.config最后有;分号,不填写会报错.
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="${logsetID}" password="${SecretId}#${SecretKey}";',
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

#配置Source
a1.sources.source_kafka.type = org.apache.flume.source.kafka.KafkaSource
a1.sources.source_kafka.batchSize = 10
a1.sources.source_kafka.batchDurationMillis = 200000
#服务地址+端口，外网端口9096，内网端口9095,例子是内网消费，请根据您的实际情况填写
a1.sources.source_kafka.kafka.bootstrap.servers = $kafkaconsumer-${region}.cls.tencentyun.com:9095
#cls kafka协议消费控制台给出的的主题名称，例如XXXXXX-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX,可在控制台复制
a1.sources.source_kafka.kafka.topics = 您的消费主题  
#请替换为您的消费组名称
a1.sources.source_kafka.kafka.consumer.group.id = 您的消费组名称
a1.sources.source_kafka.kafka.consumer.auto.offset.reset = earliest
a1.sources.source_kafka.kafka.consumer.security.protocol = SASL_PLAINTEXT
a1.sources.source_kafka.kafka.consumer.sasl.mechanism = PLAIN
#用户名是日志集合ID，例如ca5cXXXXdd2e-4ac0af12-92d4b677d2c6
#密码是用户的SecretId#SecretKey组合的字符串，比AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#。建议使用子账号密钥,为子账号授权时,遵循最小权限原则,即子账号的访问策略中的action、resource都配置为最小范围,可以满足操作即可,注意jaas.config最后有;分号,不填写会报错.
a1.sources.source_kafka.kafka.consumer.sasl.jaas.config = org.apache.kafka.common.security.plain.PlainLoginModule required username="${logsetID}" 
password="${SecretId}#${SecretKey}";



//配置sink
a1.sinks.sink_local.type = logger

a1.channels.channel1.type = memory
a1.channels.channel1.capacity = 1000
a1.channels.channel1.transactionCapacity = 100

//将source和sink绑定到channel
a1.sources.source_kafka.channels = channel1
a1.sinks.sink_local.channel = channel1
```
