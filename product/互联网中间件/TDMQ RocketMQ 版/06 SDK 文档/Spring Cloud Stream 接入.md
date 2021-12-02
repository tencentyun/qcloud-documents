## 操作场景

本文以调用 Spring Cloud Stream 接入为例介绍实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-springcloud-stream-demo.zip)

## 操作步骤

1. 在 pom.xml 中引入 `stream-rocketmq` 相关依赖。

   ```xml
    <dependency>
        <groupId>org.apache.rocketmq</groupId>
        <artifactId>rocketmq-client</artifactId>
        <version>4.7.1</version>
   </dependency>
   <dependency>
       <groupId>org.apache.rocketmq</groupId>
       <artifactId>rocketmq-acl</artifactId>
       <version>4.7.1</version>
   </dependency>
   
   <!--spring-cloud-starter-stream-rocketmq 里面的 RocketMQ 版本较老,需要排除掉,然后单独引用新的版本-->
   <dependency>
       <groupId>com.alibaba.cloud</groupId>
       <artifactId>spring-cloud-starter-stream-rocketmq</artifactId>
       <version>2.2.5-RocketMQ-RC1</version>
       <exclusions>
           <exclusion>
               <groupId>org.apache.rocketmq</groupId>
               <artifactId>rocketmq-client</artifactId>
           </exclusion>
           <exclusion>
               <groupId>org.apache.rocketmq</groupId>
               <artifactId>rocketmq-acl</artifactId>
           </exclusion>
       </exclusions>
   </dependency>
   ```

2. 在配置文件中增加 RocketMQ 相关配置。

   ```yaml
   spring:
     cloud:
       stream:
         rocketmq:
           bindings:
             # channel名称, 与spring.cloud.stream.bindings下的channel名称对应
             Topic-test1:
               consumer:
                 # 订阅的tag类型，根据消费者实际情况进行配置（默认是订阅所有消息）
                 subscription: TAG1
             # channel名称
             Topic-test2:
               consumer:
                 subscription: TAG2
           binder:
             # 服务地址全称
             name-server: rocketmq-xxx.rocketmq.ap-bj.public.tencenttdmq.com:9876
             # 角色名称
             secret-key: admin
             # 角色密钥
             access-key: eyJrZXlJZ...
             # namespace全称
             namespace: rocketmq-xxx|namespace1
             # 生成者group名称
             group: group1
         bindings:
           # channel名称
           Topic-send:
             # 指定topic, 对应创建的topic名称
             destination: topic1
             content-type: application/json
             # 要使用group名称
             group: group1
           # channel名称
           Topic-test1:
             destination: topic1
             content-type: application/json
             group: group1
           # channel名称
           Topic-test2:
             destination: topic1
             content-type: application/json
             group: group2
   ```

   | 参数          | 说明                                                         |
   | :------------ | :----------------------------------------------------------- |
   | name-server   | 集群接入地址，在控制台**集群管理**页面的集群列表操作栏的**接入地址**处获取。 |
   | secret-key    | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
   | access-key    | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | namespace     | 命名空间的名称，在控制台**命名空间**页面复制。               |
   | group         | 生产者 Group 的名称，在控制台 **Group** 页面复制。           |
   | destination   | Topic 的名称，在控制台 **topic** 页面复制。                  |
   | subExpression | 用来设置消息的 TAG。                                         |

3. 配置channel，channel分为输入和输出，可根据自己的业务进行单独配置。

   ```java
   import org.springframework.cloud.stream.annotation.Input;
   import org.springframework.cloud.stream.annotation.Output;
   import org.springframework.messaging.MessageChannel;
   
   /**
    * 自定义通道 Binder
    */
   public interface CustomChannelBinder {
   
       /**
        * 发送消息(消息生产者)
        * 绑定配置中的channel名称
        */
       @Output("Topic-send")
       MessageChannel sendChannel();
   
   
       /**
        * 接收消息1(消费者1)
        * 绑定配置中的channel名称
        */
       @Input("Topic-test1")
       MessageChannel testInputChannel1();
   
       /**
        * 接收消息2(消费者2)
        * 绑定配置中的channel名称
        */
       @Input("Topic-test2")
       MessageChannel testInputChannel2();
   }
   ```

4. 在配置类或启动类上添加相应注解，如果有多个binder配置，都要在此注解中进行指定。

   ```java
   @EnableBinding({CustomChannelBinder.class})
   ```

5. 发送消息。

   1. 在要发送消息的类中，注入 `CustomChannelBinder`。

      ```java
      @Autowired
      private CustomChannelBinder channelBinder;
      ```

   2. 发送消息，调用对应的输出流channel进行消息发送。

      ```java
      Message<String> message = MessageBuilder.withPayload("This is a new message.").build();
      channelBinder.sendChannel().send(message);
      ```

6. 消费消息。

   ```java
   @Service
   public class TestStreamConsumer {
       private final Logger logger = LoggerFactory.getLogger(DemoApplication.class);
   
       /**
        * 监听channel (配置中的channel名称)
        *
        * @param messageBody 消息内容
        */
       @StreamListener("Topic-test1")
       public void receive(String messageBody) {
           logger.info("Receive1: 通过stream收到消息，messageBody = {}", messageBody);
       }
   
       /**
        * 监听channel (配置中的channel名称)
        *
        * @param messageBody 消息内容
        */
       @StreamListener("Topic-test2")
       public void receive2(String messageBody) {
           logger.info("Receive2: 通过stream收到消息，messageBody = {}", messageBody);
       }
   }
   ```

具体使用可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-springcloud-stream-demo.zip) 或 [Spring cloud stream 官网](https://github.com/alibaba/spring-cloud-alibaba/wiki/RocketMQ-en)。

