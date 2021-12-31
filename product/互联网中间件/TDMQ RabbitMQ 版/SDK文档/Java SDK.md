## 操作场景

本文以调用 Java SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-java-sdk-demo.zip)

## 操作步骤

### 步骤1：安装 Java 依赖库

在 pom.xml 添加以下依赖：

```xml
<!-- in your <dependencies> block -->
<dependency>
    <groupId>com.rabbitmq</groupId>
    <artifactId>amqp-client</artifactId>
    <version>5.13.0</version>
</dependency>
```

### 步骤2：生产消息

创建并编译运行 MessageProducer.java。

```java
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.tencent.tdmq.demo.cloud.Constant;

/**
 * 消息生产者
 */
public class MessageProducer {

    /**
     * 交换机名称
     */
    private static final String EXCHANGE_NAME = "exchange_name";

    public static void main(String[] args) throws Exception {
        // 连接工厂
        ConnectionFactory factory = new ConnectionFactory();
        // 设置服务地址 (完整复制控制台接入点地址)
        factory.setUri("amqp://***");
        // 设置Virtual Hosts (Vhost控制台复制完整Vhost名称)
        factory.setVirtualHost(VHOST_NAME);
        // 设置用户名 (具体使用Vhost的配置权限中的角色名称)
        factory.setUsername(USERNAME);
        // 设置密码 (对应角色的密钥)
        factory.setPassword("eyJh****");
        // 获取连接、建立通道
        try (Connection connection = factory.newConnection(); Channel channel = connection.createChannel()) {
            // 绑定消息交换机 (EXCHANGE_NAME必须在消息队列RabbitMQ版控制台上已存在，并且Exchange的类型与控制台上的类型一致)
            channel.exchangeDeclare(EXCHANGE_NAME, "fanout");
            for (int i = 0; i < 10; i++) {
                String message = "this is rabbitmq message " + i;
                // 发布消息到交换机，交换机自动将消息投递到相应队列
                channel.basicPublish(EXCHANGE_NAME, "", null, message.getBytes());
                System.out.println(" [producer] Sent '" + message + "'");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

| 参数                   | 说明                                                         |
| :--------------------- | :----------------------------------------------------------- |
| EXCHANGE_NAME          | Exchange 名称，在控制台 Exchange 列表获取。                  |
| factory.setUri         | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
| factory.setVirtualHost | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |
| factory.setUsername    | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| factory.setPassword    | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |

### 步骤3：消费消息

创建并编译运行 MessageConsumer.java。

```java
import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DefaultConsumer;
import com.rabbitmq.client.Envelope;
import com.tencent.tdmq.demo.cloud.Constant;

import java.io.IOException;
import java.nio.charset.StandardCharsets;

/**
 * 消息消费者
 */
public class MessageConsumer1 {

    /**
     * 队列名称
     */
    public static final String QUEUE_NAME = "queue_name";

    /**
     * 交换机名称
     */
    private static final String EXCHANGE_NAME = "exchange_name";

    public static void main(String[] args) throws Exception {
        // 连接工厂
        ConnectionFactory factory = new ConnectionFactory();
        // 设置服务地址 (完整复制控制台接入点地址)
        factory.setUri("amqp://***");
        // 设置Virtual Hosts (Vhost控制台复制完整Vhost名称)
        factory.setVirtualHost(VHOST_NAME);
        // 设置用户名 (具体使用Vhost的配置权限中的角色名称)
        factory.setUsername(USERNAME);
        // 设置密码 (对应角色的密钥)
        factory.setPassword("eyJh****");
        // 获取连接
        Connection connection = factory.newConnection();
        // 建立通道
        Channel channel = connection.createChannel();
        // 绑定消息交换机
        channel.exchangeDeclare(EXCHANGE_NAME, "fanout");
        // 声明队列信息
        channel.queueDeclare(QUEUE_NAME, true, false, false, null);
        // 绑定消息交换机 (EXCHANGE_NAME必须在消息队列RabbitMQ版控制台上已存在，并且Exchange的类型与控制台上的类型一致)
        channel.queueBind(QUEUE_NAME, EXCHANGE_NAME, "");
        System.out.println(" [Consumer1] Waiting for messages.");
        // 订阅消息
        channel.basicConsume(QUEUE_NAME, false, "ConsumerTag", new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope,
                                       AMQP.BasicProperties properties, byte[] body)
                    throws IOException {
                //接收到的消息，进行业务逻辑处理。
                System.out.println("Received： " + new String(body, StandardCharsets.UTF_8) + ", deliveryTag: " + envelope.getDeliveryTag() + ", messageId: " + properties.getMessageId());
                channel.basicAck(envelope.getDeliveryTag(), false);
            }
        });
    }
}
```

| 参数                   | 说明                                                         |
| :--------------------- | :----------------------------------------------------------- |
| QUEUE_NAME             | Queue名称，在控制台 Queue 列表获取。                         |
| EXCHANGE_NAME          | Exchange 名称，在控制台 Exchange 列表获取。                  |
| factory.setUri         | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
| factory.setVirtualHost | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |
| factory.setUsername    | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| factory.setPassword    | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |

### 步骤4：查询消息

如果您想确认消息是否成功发送至 TDMQ RabbitMQ 版，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)** > **Queue** 页面查看接入的消费者情况。

![](https://main.qcloudimg.com/raw/a7d78cc58efadfb614b890cc33d08632.png)

上述是基于 RabbitMQ 的发布订阅模型的一个简单示例。其他示例可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-java-sdk-demo.zip) 或 [RabbitMQ 官网](https://www.rabbitmq.com/getstarted.html) 实例。


