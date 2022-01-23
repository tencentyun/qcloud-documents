## 操作场景

本文以调用 Spring Boot Starter SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-springboot-amqp-demo.zip)

## 操作步骤

### 步骤1：添加依赖

在 pom.xml 中添加依赖。
```xml
<!--rabbitmq-->
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-amqp</artifactId>
</dependency>
```

### 步骤2：准备配置

1. 在配置文件中加入 RabbitMQ 配置信息（以 yml 配置为）。
   ```yaml
   spring:
     rabbitmq:
     	# host地址可在控制台中获取 或 使用Rabbitmq服务地址
       host: amqp-xx.rabbitmq.x.tencenttdmq.com
       port: 5672
       # 要使用的角色名称 可在角色管理控制台获取
       username: admin
       # 角色密钥
       password: eyJrZXlJZ....
       # Vhost全称，可在集群控制台Vhost tab页获取
       virtual-host: amqp-xxx|Vhost
   ```


   | 参数         | 说明                                                         |
   | :----------- | :----------------------------------------------------------- |
   | host         | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
   | port         | 集群接入地址端口，在**集群管理**页面操作列的**获取接入地址**获取。 |
   | username     | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
   | password     | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | virtual-host | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |

2. 创建配置文件加载程序（以`Fanout交换机`为例。）
>?其他类型的交换机配置可参考具体 Demo 示例。

   ```java
   /**
    * Fanout交换机配置
    */
   @Configuration
   public class FanoutRabbitConfig {
   
       /**
        * 交换机
        */
       @Bean
       public FanoutExchange fanoutExchange() {
           return new FanoutExchange("fanout-logs", true, false);
       }
   
   
       /**
        * 消息队列
        */
       @Bean
       public Queue fanoutQueueA() {
           return new Queue("ps_queue", true);
       }
   
       @Bean
       public Queue fanoutQueueB() {
           // 可通过这种方式绑定死信队列
           Map<String, Object> requestParam = new HashMap<>();
           requestParam.put("x-dead-letter-exchange", "my-deadLetter-exchange");
           // 设置消息过期时长
           requestParam.put("x-message-ttl", 60000);
           return new Queue("ps_queue1", true, false,true, requestParam);
       }
   
       /**
        * 绑定消息队列与交换机
        */
       @Bean
       public Binding bindingFanoutA() {
           return BindingBuilder.bind(fanoutQueueA())
                   .to(fanoutExchange());
       }
   
       @Bean
       public Binding bindingFanoutB() {
           return BindingBuilder.bind(fanoutQueueB())
                   .to(fanoutExchange());
       }
   }
   ```

| 参数                   | 说明                                                         |
| ---------------------- | ------------------------------------------------------------ |
| fanout-logs            | 绑定的 Exchange 名称，在控制台 Exchange 列表获取。           |
| ps_queue               | 与 Exchange 绑定的第一个 Queue名称，在控制台 Queue 列表获取。 |
| my-deadLetter-exchange | 死信 Exchange 名称，在控制台 Exchange 列表获取。             |
| ps_queue1              | 与 Exchange 绑定的第二个 Queue名称，在控制台 Queue 列表获取。 |

### 步骤3：发送消息

创建并编译消息发送程序 DemoApplication.java，使用 RabbitTemplate 发送即可。

```java
@Autowired
private RabbitTemplate rabbitTemplate;

public String send() {
    String msg = "This is a new message.";
    // 发送消息  
    // 参数说明：参数1：交换机名称，在控制台 Exchange 列表获取。  参数2：routing key  参数3：消息内容
    rabbitTemplate.convertAndSend("direct_logs", "", msg);
    return "success";
}
```



### 步骤4：消费消息

创建并编译消息接收程序 FanoutReceiver.java。（以`Fanout交换机`为例。）

   ```java
@Component
public class FanoutReceiver {
	// 注册一个listener监听指定消息队列
    @RabbitHandler
    @RabbitListener(queues = "ps_queue")  //与 Exchange 绑定的 Queue名称，在控制台 Queue 列表获取。
    public void listenerPsQueue(String msg) {
        // 业务处理...
        System.out.println("(ps_queue) receiver message. [" + msg + "]");
    }
}
   ```

### 步骤5：查看消息

如果您想确认消息是否成功发送至 TDMQ RabbitMQ 版，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)** > **Queue** 页面查看接入的消费者情况。

![img](https://main.qcloudimg.com/raw/a7d78cc58efadfb614b890cc33d08632.png)



其他使用示例请参考 [Spring AMQP 官网](https://docs.spring.io/spring-amqp/reference/html/)。
