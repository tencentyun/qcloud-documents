您可以通过 Kafka 协议消费，将采集到日志服务（Cloud Log Service,CLS）的数据，消费到下游的大数据组件或者数据仓库，例如自建 Kafka 集群，开源的 ClickHouse、Hive、Flink，以及腾讯云弹性 MapReduce（EMR）、流计算 Oceanus 等。

## 内外网消费说明

- 内网和外网的消费定义：例如您在广州地域的日志主题使用了 Kafka 消费协议，则消费到广州地域的 EMR-Hive 属于内网消费，消费到上海地域的 EMR-Hive 属于外网消费。
- 计费的区别：内网流量费用0.18元/GB，外网流量费用0.8元/GB。
- 消费服务域名的区别：在控制台页面会给出内网服务域名和外网服务域名，请按需选择。

## 操作步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击**日志主题**。
3. 单击需要使用 Kafka 协议消费的日志主题 ID/名称，进入日志主题管理页面。
4. 单击 **Kafka协议消费**页签。
5. 单击右侧的**编辑**。
![](https://qcloudimg.tencent-cloud.cn/raw/3d96169dbd0eb52f3ff3f2bcca537b3c.png)
6. 将**当前状态**设置为打开状态，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/172bc37310b75d92d9e5eeb4b504b458.png)
7. 根据 CLS 给出消费的 Topic 信息，构造消费者即可。
![](https://qcloudimg.tencent-cloud.cn/raw/bbd3cc0ffe3e7bc24ac5da73d1b7ed6e.png)


## 操作示例

示例：通过 Python 构造 Consumer.py
```
import uuid
from kafka import KafkaConsumer,TopicPartition,OffsetAndMetadata
consumer = KafkaConsumer(
//将上图中的主题名称填写到此处，您将使用这个topic进行消费    
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
api_version = (0,10,0)
)
print('begin')
for message in consumer:
    print('begins')
    print ("Topic:[%s] Partition:[%d] Offset:[%d] Value:[%s]" % (message.topic, message.partition, message.offset, message.value))
    print('end')
```



