日志服务（Cloud Log Service，CLS）目前已支持使用 Kafka Producer SDK 和其他 Kafka 相关 agent 上传日志日志到 CLS。

## 相关限制

- 支持 Kafka 协议版本为："0.11.0.0"，" 0.11.0.1"，" 0.11.0.2"
- confluent-kafka-go 的 Kafka 库的代码（暂不支持 V3 版本 Kafka 协议）可以使用 sarama 库代替。
- 不支持压缩传输。
- 使用非强制（SASL_PLAINTEXT）认证。



## 配置方式

使用 kafka 协议上传日志时，需要配置一下参数：

| 参数 | 说明 |
|---------|---------|
| 链接类型 | 当前支持 SASL_PLAINTEXT |
| hosts | 初始连接的集群地址，详细参见服务入口：</br><ul  style="margin: 0;"><li>内网使用：端口为 9095。例如：gz-producer.cls.tencentyun.com:9095</li><li>外网使用：端口为 9096。例如：gz-producer.cls.tencent.com:9096</li></ul> |
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
  
## 示例

### Java 上传日志到 CLS

#### Java SDK 示例

```java
Properties props = new Properties(); 
props.put("bootstrap.servers", "xxxxxxxxxxxxxxxx:9895");    //produce 服务域名
props.put("acks", "all");
props.put("retries", xxx); 
props.put("batch.size", xxxx); 
props.put("tinger.ms", x); 
props.put("buffer.memory", xxxxxx) 
props.put("key.seriaLizer", "org.apache.kafka.common.serialization.StringSeriatizer");
props.put("vatue.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("security.protocol", "SASL_PLAINTEXT"); 
props.put("sasl.mechanism", "PLAIN");
props.put("sasl.jaas.config", "org.apache.kafka..common.security.plain.PlainLoginModule required username='xxxxxxxx', password='xxxxxxxxxx#xxxxxxxxx';")    //username 填写日志集 ID，格式为 ${SecurityID}#${SecurityKey}#
return props;
```


### 通过 filebeat 采集日志到日志服务

#### Filebeat 

```
output.kafka:
  hosts: ["gz-producer.cls.tencentyun.com:9095"]
  topic: "1e36939e-xxxx-xxxx-xxxx-3806ad46e9e2"
  version: "0.11.0.0"
  compression: "none"
  username: "0f8e4b82-xxxx-xxxx-xxxx-8d7b7f62da72"
  password: "XXXXXXXXXX#YYYYYYYYYY"
```

### 通过 Golang SDK 上传日志到日志服务 
 
####  Golang SDK 示例

```
func main() {
	config := sarama.NewConfig()
	config.Net.SASL.Mechanism = "PLAIN"
	config.Net.SASL.Version = int16(1)
	config.Net.SASL.Enable = true
	config.Net.SASL.User = "0f8e4b82-xxxx-xxxx-xxxx-8d7b7f62da72"
	config.Net.SASL.Password = "XXXXXXXXXX#YYYYYYYYYY"
	config.Producer.Return.Successes = true
	config.Version = sarama.V0_11_0_0
	producer, err := sarama.NewSyncProducer([]string{"gzopen-producer.cls.tencentyun.com:9095"}, config)
	if err != nil {
		fmt.Println("new sync producer err : ", err)
		return
	}
	defer producer.Close()
	msg := &sarama.ProducerMessage{
		Topic: "1e36939e-xxxx-xxxx-xxxx-3806ad46e9e2",
		Value: sarama.StringEncoder("go kafka client test - inner:9095 "),
	}
	// 发送消息
	for {
		message, offset, err := producer.SendMessage(msg)
		if err != nil {
			fmt.Println("SendMessage err : ", err)
			return
		}
		fmt.Println(message, " ", offset)
		time.Sleep(time.Duration(1) * time.Second)
	}
}
```

### 通过 Kafka Sarama SDK 上传日志到日志服务

```
func StartKafka() {
	config := sarama.NewConfig()
	config.Producer.Return.Successes = true
	config.Version = sarama.V0_11_0_0
	producer, err := sarama.NewSyncProducer([]string{"gz-producer.cls.tencentcs.com:9096"}, config)
	if err != nil {
		fmt.Println("new sync producer err : ", err)
		return
	}
	defer producer.Close()
	msg := &sarama.ProducerMessage{
		Topic: "xxxxx",
		Value: sarama.StringEncoder("go kafka client test - inner:9095 "),
	}
	// 发送消息
	for {
		message, offset, err := producer.SendMessage(msg)
		if err != nil {
			fmt.Println("SendMessage err : ", err)
			return
		}
		fmt.Println(message, " ", offset)
		time.Sleep(time.Duration(1) * time.Second)
	}
}
```
 
 


 
 


