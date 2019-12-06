## Ckafka Schema Registry 简介
无论是使用传统的 Avro API 自定义序列化类与反序列化类，还是使用 Twitter 的 Bijection 类库实现 Avro 的序列化与反序列化，两种方法有相同的缺点：在每条 Kafka 记录里都嵌入了 Schema，从而导致记录的大小成倍增加。但是不管怎样，在读取记录时仍然需要用到整个 Schema，所以要先找到 Schema。
CKafka 提供了数据共用一个 Schema 的方法：将 Schema 中的内容注册到 Confluent Schema Registry，Kafka Producer 和 Kafka Consumer 通过识别 Confluent Schema Registry 中的 schema 内容进行序列化和反序列化。
![](https://main.qcloudimg.com/raw/28d3fc8adb8c684f21643c98da1417ca.png)


## Schema Registry 接入 CKafka
### 环境依赖
- Java1.8 
- CKafka1.1.1
- Confluent oss 4.1.1 

### 环境配置
1. 下载 Confluent 
`wget http://packages.confluent.io/archive/4.1/confluent-oss-4.1.1-2.11.tar.gz`
2. oss 配置文件
>!启动 oss 会创建 _schemas 主题，所以实例中开启了自动创建主题。

![](https://main.qcloudimg.com/raw/5482de42c702cf4d43a3498e4592f420.png)
控制台显示如下：
![](https://main.qcloudimg.com/raw/010043c4d40b163bb89057ef8120afaa.png)
3. 启动 Schema Registry
`bin/schema-registry-start etc/schema-registry/schema-registry.properties`
![](https://main.qcloudimg.com/raw/289772a734dcf0657e9f540555641598.png)
	
### 案例说明
现有 schema 文件，其中内容如下： 
```
{
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "id", "type": "int"},
        {"name": "name",  "type": "string"},
        {"name": "age", "type": "int"}
    ]
}
```

1. 注册 schema 到对应 topic（注册 topic 为 test）
```
curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
--data '{"schema": "{\"type\": \"record\", \"name\": \"User\", \"fields\": [{\"name\": \"id\", \"type\": \"int\"}, {\"name\": \"name\",  \"type\": \"string\"}, {\"name\": \"age\", \"type\": \"int\"}]}"}' \
http://127.0.0.1:8081/subjects/test/versions
```
![](https://main.qcloudimg.com/raw/e3dc1f1fefd9fb98a5a41694dd75c476.png)

2.  Kafka Producer 发送数据
```
package schemaTest;
import java.util.Properties;
import java.util.Random;
import org.apache.avro.Schema;
import org.apache.avro.generic.GenericData;
import org.apache.avro.generic.GenericRecord;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;
public class SchemaProduce {
	 public static final String USER_SCHEMA = "{\"type\": \"record\", \"name\": \"User\", " + 
	            "\"fields\": [{\"name\": \"id\", \"type\": \"int\"}, " + 
	            "{\"name\": \"name\",  \"type\": \"string\"}, {\"name\": \"age\", \"type\": \"int\"}]}";
	    public static void main(String[] args) throws Exception {
	        Properties props = new Properties();
	        props.put("bootstrap.servers", "172.26.0.8:9092");
	        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
	        // 使用 Confluent 实现的 KafkaAvroSerializer
	        props.put("value.serializer", "io.confluent.kafka.serializers.KafkaAvroSerializer");
	        // 添加 schema 服务的地址，用于获取 schema
	        props.put("schema.registry.url", "http://127.0.0.1:8081");
	        Producer<String, GenericRecord> producer = new KafkaProducer<>(props);	       
	        Schema.Parser parser = new Schema.Parser();
	        Schema schema = parser.parse(USER_SCHEMA);     
	        Random rand = new Random();
	        int id = 0;
	        while(id < 100) {
	            id++;
	            String name = "name" + id;
	            int age = rand.nextInt(40) + 1;
	            GenericRecord user = new GenericData.Record(schema);
	            user.put("id", id);
	            user.put("name", name);
	            user.put("age", age);	            
	            ProducerRecord<String, GenericRecord> record = new ProducerRecord<>("test", user);	            
	            producer.send(record);
	            Thread.sleep(1000);
	        }
	        producer.close();
	    }
}
```

如下图监控看 生产是成功
![](https://main.qcloudimg.com/raw/7625063d06fa2bd79278659e3508b698.png)

3. Kafka Consumer 消费数据
```
package schemaTest;
import java.util.Collections;
import java.util.Properties;
import org.apache.avro.generic.GenericRecord;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
public class SchemaProduce {
    public static void main(String[] args) throws Exception {
        Properties props = new Properties();
        props.put("bootstrap.servers", "172.26.0.8:9092");
        props.put("group.id", "schema");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        // 使用Confluent实现的KafkaAvroDeserializer
        props.put("value.deserializer", "io.confluent.kafka.serializers.KafkaAvroDeserializer");
        // 添加schema服务的地址，用于获取schema
        props.put("schema.registry.url", "http://127.0.0.1:8081");
        KafkaConsumer<String, GenericRecord> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Collections.singletonList("test"));
        try {
            while (true) {
                ConsumerRecords<String, GenericRecord> records = consumer.poll(10);
                for (ConsumerRecord<String, GenericRecord> record : records) {
                    GenericRecord user = record.value();
                    System.out.println("value = [user.id = " + user.get("id") + ", " + "user.name = "
                            + user.get("name") + ", " + "user.age = " + user.get("age") + "], "
                            + "partition = " + record.partition() + ", " + "offset = " + record.offset());
                }
            }
        } finally {
            consumer.close();
        }
    }
}
```
4. 测试结果
查看 schema 这个消费分组。
![](https://main.qcloudimg.com/raw/aff0af7032f82e8e547931c405f5f9ca.png)
启动消费者，消费截图。
![](https://main.qcloudimg.com/raw/ff59e6fab31b490b705ca46d378e6df7.png)
![](https://main.qcloudimg.com/raw/a55147f38ef884f79a06c009cdbb7ef6.png)
控制台消费完毕。
