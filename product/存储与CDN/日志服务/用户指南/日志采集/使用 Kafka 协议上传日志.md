日志服务（Cloud Log Service，CLS）目前已支持使用 Kafka Producer SDK 和其他 Kafka 相关 agent 上传日志到 CLS。

## 相关限制

- 支持 Kafka 协议版本为："0.11.0.X"，"1.0.X"，"1.1.X"，"2.0.X"，"2.1.X"，"2.2.X"，"2.3.X"，"2.4.X"，"2.5.X"，"2.6.X"，"2.7.X"，"2.8.X"
- 支持压缩方式："gzip"，"snappy"，"lz4"
- confluent-kafka-go 的 Kafka 库的代码（V3版本 Kafka协议，暂不支持，预计12月初支持），可以使用 sarama 库代替。
- 当前使用非强制（SASL_PLAINTEXT）认证。




## 配置方式

使用 kafka 协议上传日志时，需要配置一下参数：

| 参数 | 说明 |
|---------|---------|
| 链接类型 | 当前支持 SASL_PLAINTEXT |
| hosts | 初始连接的集群地址，详细参见服务入口：</br><ul  style="margin: 0;"><li>内网使用：端口为 9095。例如：gz-producer.cls.tencentyun.com:9095</li><li>外网使用：端口为 9096。例如：gz-producer.cls.tencentcs.com:9096</li></ul>**注意**：示例以广州为例，内外网域名用不同端口标识，其他地域替换地址前缀。请参考 [可用域名-Kafka上传日志](https://cloud.tencent.com/document/product/614/18940#Kafka) |
| topic | 配置为日志主题 ID。例如：76c63473-c496-466b-XXXX-XXXXXXXXXXXX |
| username | 配置为日志集 ID。  例如：0f8e4b82-8adb-47b1-XXXX-XXXXXXXXXXXX |
| password | 格式为 `${SecurityId}#${SecurityKey}`。例如：XXXXXXXXXXXXXX#YYYYYYYY |


## 服务入口 

<table>
	<tr><th>地域</th><th>网络类型</th><th>服务入口</th></tr>
	<tr><td rowspan=2>广州</td><td>内网</td><td>gz-producer.cls.tencentyun.com:9095</td></tr>
	<tr><td>外网</td><td>gz-producer.cls.tencentcs.com:9096</td></tr>
</table>

>? 本文档以广州地域为例，由于内外网域名用不同端口标识，其他地域请替换地址前缀。
>

## 使用场景

日志应用中使用 Kafka 作为消息管道是非常普遍的场景。先通过机器上的开源采集客户端或者使用 producer 直接写入收集日志，再通过消费管道提供给下游如 spark、flink 等进行消费。CLS 具备完整的 Kafka 数据管道上下行能力，以下主要介绍哪些场景适合您使用 Kafka 协议上传日志，更多 Kafka 协议消费场景请参考 [Kafka 协议实时消费](https://cloud.tencent.com/document/product/614/63036) 文档。

- **场景1**：您已有基于开源采集的自建系统，不希望有复杂的二次改造，您可以通过修改配置文件将日志上传到 CLS。
例如，您之前使用 ELK 搭建日志系统的客户，现在只需要通过修改 Filebeat 或者 Logstash 的配置文件，将 Output 配置（详情请参考 [filebeat 配置](#filebeat)）到 CLS，即可非常方便简洁的将日志上传。
- **场景2**：您希望通过 Kafka producer 来采集日志并上传，不必再安装采集 Agent。
CLS 支持您使用各类 Kafka producer SDK 采集日志，并通过 Kafka 协议上传到 CLS。（详情请参考本文提供的 [SDK 调用示例](#SDKSample) ）


## 示例

<span id="SDKSample"></span>
### SDK 调用示例

#### Golang SDK 调用示例

```golang
import (
    "fmt"
    "github.com/Shopify/sarama"
)

func main() {
    config := sarama.NewConfig()

    config.Net.SASL.Mechanism = "PLAIN"
    config.Net.SASL.Version = int16(1)
    config.Net.SASL.Enable = true
    config.Net.SASL.User = "${logsetID}"                        // TODO 日志集 ID
    config.Net.SASL.Password = "${SecurityId}#${SecurityKey}"   // TODO 格式为 ${SecurityId}#${SecurityKey}
    config.Producer.Return.Successes = true
    config.Producer.RequiredAcks = ${acks}                      // TODO 根据使用场景选择acks的值
    config.Version = sarama.V0_11_0_0
    config.Producer.Compression = ${compress}                   // TODO 配置压缩方式

    // TODO 服务地址；公网端口9096，内网端口9095
    producer, err := sarama.NewSyncProducer([]string{"${region}-producer.cls.tencentyun.com:9096"}, config)
    if err != nil {
        panic(err)
    }

    msg := &sarama.ProducerMessage{
        Topic: "${topicID}", // TODO topicID
        Value: sarama.StringEncoder("goland sdk sender demo"),
    }
    // 发送消息
    for i := 0; i <= 5; i++ {
        partition, offset, err := producer.SendMessage(msg)
        if err != nil {
            panic(err)
        }
        fmt.Printf("send response; partition:%d, offset:%d\n", partition, offset)
    }

    _ = producer.Close()

}
```

#### Python SDK 调用示例

```python
from kafka import KafkaProducer

if __name__ == '__main__':
    produce = KafkaProducer(
        # TODO 服务地址；公网端口9096，内网端口9095
        bootstrap_servers=["${region}-producer.cls.tencentyun.com:9096"],
        security_protocol='SASL_PLAINTEXT',
        sasl_mechanism='PLAIN',
        # TODO 日志集 ID
        sasl_plain_username='${logsetID}',
        # TODO 格式为 ${SecurityId}#${SecurityKey}
        sasl_plain_password='${SecurityId}#${SecurityKey}',
        api_version=(0, 11, 0),
        # TODO 配置压缩方式
        compression_type="${compress_type}",
    )

    for i in range(0, 5):
        # 发送消息 TODO topicID
        future = produce.send(topic="${topicID}", value=b'python sdk sender demo')
        result = future.get(timeout=10)
        print(result)
```

#### Java SDK 调用示例

maven 依赖：
```maven
<dependencies>
  <!--https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients-->
  <dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>0.11.0.2</version>
  </dependency>
</dependencies>
```

代码示例：
```java
import org.apache.kafka.clients.producer.*;

import java.util.Properties;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class ProducerDemo {
    public static void main(String[] args) throws InterruptedException, ExecutionException, TimeoutException {
        // 0.配置一系列参数
        Properties props = new Properties();
        // TODO 使用时
        props.put("bootstrap.servers", "${region}-producer.cls.tencentyun.com:9096");
        // TODO 以下值根据业务场景设置 
        props.put("acks", ${acks});
        props.put("retries", ${retries});
        props.put("batch.size", ${batch.size});
        props.put("linger.ms", ${linger.ms});
        props.put("buffer.memory", ${buffer.memory});
        props.put(ProducerConfig.COMPRESSION_TYPE_CONFIG, "${compress_type}"); // TODO 配置压缩方式
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        props.put("security.protocol", "SASL_PLAINTEXT");
        props.put("sasl.mechanism", "PLAIN");
        // TODO 用户名为logsetID；密码为securityID和securityKEY的组合  securityID#securityKEY
        props.put("sasl.jaas.config",
                "org.apache.kafka.common.security.plain.PlainLoginModule required username='${logsetID}' password='${SecurityId}#${SecurityKey}';");

        // 1.创建一个生产者对象
        Producer<String, String> producer = new KafkaProducer<String, String>(props);
        
        // 2.调用send方法
        Future<RecordMetadata> meta = producer.send(new ProducerRecord<String, String>("${topicID}", ${message}));
        RecordMetadata recordMetadata = meta.get(${timeout}, TimeUnit.MILLISECONDS);
        System.out.println("offset = " + recordMetadata.offset());

        // 3.关闭生产者
        producer.close();
    }
}
```

### Agent 调用示例

<span id="filebeat"></span>
#### filebeat 配置

```filebeat
output.kafka:
  enabled: true
  hosts: ["${region}-producer.cls.tencentyun.com:9096"] # TODO 服务地址；公网端口9096，内网端口9095
  topic: "${topicID}" #  TODO topicID
  version: "0.11.0.2"
  compression: "${compress}"   # TODO 配置压缩方式
  username: "${logsetID}"
  password: "${SecurityId}#${SecurityKey}"
```





 
 
