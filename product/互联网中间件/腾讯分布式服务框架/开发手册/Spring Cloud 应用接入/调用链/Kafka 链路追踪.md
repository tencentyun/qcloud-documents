Kafka 的链路追踪能力通过 Spring Boot 的自动配置方式实现。

## 1.16.0-Edgware 版本说明

实现方式是向 bean 容器中各加入了一个 producerFactory 和 consumerFactory 类的 bean。他们各自分别重写了 createKafkaProducer 方法和 createKafkaConsumer 方法。使用该 producerFactory/consumerFactory 便具有了链路追踪的能力。建议使用 Spring 默认的 KafkaTemplate，无须自定义。

 **1.16.0-Edgware** 版使用的 spring-kafka 版本必须在**1.3.0**以上，因为从这个版本开始 kafka-client 中增加了请求头，这才能方便的实现链路追踪。

```xml
<!--支持 kafka 使用调用链-->
        <dependency>
            <groupId>org.springframework.kafka</groupId>
            <artifactId>spring-kafka</artifactId>
            <version>1.3.0.RELEASE</version>
        </dependency>
```

参考配置：

```properties
#============== kafka ===================
# 指定 kafka 代理地址，可以多个
spring.kafka.bootstrap-servers=
  
#=============== provider  =======================
spring.kafka.producer.retries=0
# 每次批量发送消息的数量
spring.kafka.producer.batch-size=16384
spring.kafka.producer.buffer-memory=33554432
  
# 指定消息 key 和消息体的编解码方式
spring.kafka.producer.key-serializer=org.apache.kafka.common.serialization.StringSerializer
spring.kafka.producer.value-serializer=org.apache.kafka.common.serialization.StringSerializer
  
#=============== consumer  =======================
# 指定默认消费者 Group ID
spring.kafka.consumer.group-id=test-consumer-group
  
spring.kafka.consumer.auto-offset-reset=earliest
spring.kafka.consumer.enable-auto-commit=true
spring.kafka.consumer.auto-commit-interval=100
  
# 指定消息 key 和消息体的编解码方式
spring.kafka.consumer.key-deserializer=org.apache.kafka.common.serialization.StringDeserializer
spring.kafka.consumer.value-deserializer=org.apache.kafka.common.serialization.StringDeserializer
```

其他更详细配置、使用方法详见 [Demo 示例](https://github.com/tencentyun/tsf-simple-demo)。

## 1.16.0-Finchley 版本说明

实现方式是向 Spring 容器中各增加了一个对切面，分别作用于 ProducerFactory.createProducer 方法和 ConsumerFactory.createConsumer 方法的，使得通过他们返回的 KafkaProducer 和 KafkaConsumer 具有链路追踪的能力。

使用 1.16.0-Finchley 版本**无须**考虑 spring-kafka 版本问题，无须指定它的版本，因为底层依赖的 Finchley 版本的 spring cloud 会自动为它配置高于 1.3.0.RELEASE 版本的spring-kafka。

```xml
        <!--支持kafka使用调用链-->
        <dependency>
            <groupId>org.springframework.kafka</groupId>
            <artifactId>spring-kafka</artifactId>
        </dependency>
```

参考配置：

```yml
  server:
    servlet:
      context-path: /
    port: xxxxx
  spring:
    application:
      name: xxxxxx
    kafka:
      bootstrap-servers: xxxxxx
      #生产者的配置，大部分我们可以使用默认的，这里列出几个比较重要的属性
      producer:
        #每批次发送消息的数量
        batch-size: 16
        #设置大于0的值将使客户端重新发送任何数据，一旦这些数据发送失败。注意，这些重试与客户端接收到发送错误时的重试没有什么不同。允许重试将潜在的改变数据的顺序，如果这两个消息记录都是发送到同一个partition，则第一个消息失败第二个发送成功，则第二条消息会比第一条消息出现要早。
        retries: 0
        #producer可以用来缓存数据的内存大小。如果数据产生速度大于向broker发送的速度，producer会阻塞或者抛出异常，以“block.on.buffer.full”来表明。这项设置将和producer能够使用的总内存相关，但并不是一个硬性的限制，因为不是producer使用的所有内存都是用于缓存。一些额外的内存会用于压缩（如果引入压缩机制），同样还有一些用于维护请求。
        buffer-memory: 33554432
        #key序列化方式
        key-serializer: org.apache.kafka.common.serialization.StringSerializer
        value-serializer: org.apache.kafka.common.serialization.StringSerializer
      #消费者的配置
      consumer:
        #Kafka中没有初始偏移或如果当前偏移在服务器上不再存在时,默认区最新 ，有三个选项 【latest, earliest, none】
        auto-offset-reset: latest
        #是否开启自动提交
        enable-auto-commit: true
        #自动提交的时间间隔
        auto-commit-interval: 100
        #key的解码方式
        key-deserializer: org.apache.kafka.common.serialization.StringDeserializer
        #value的解码方式
        value-deserializer: org.apache.kafka.common.serialization.StringDeserializer
        #在/usr/local/etc/kafka/consumer.properties中有配置
        group-id: test-consumer-group
  tsf:
    swagger:
      enabled: false
  logging:
    file: /tsf-demo-logs/${spring.application.name}/root.log
```

其他更详细配置、使用方法详见 [Demo 示例](https://github.com/tencentyun/tsf-simple-demo)。
