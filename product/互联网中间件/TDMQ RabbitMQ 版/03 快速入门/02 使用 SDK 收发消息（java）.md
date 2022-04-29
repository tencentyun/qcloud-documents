## 操作场景

本文以调用 Java SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。



<dx-alert infotype="explain" title="">
以 Java 客户端为例说明，其他语言客户端请参见 [SDK 文档](https://cloud.tencent.com/document/product/1495/64515)。
</dx-alert>



## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rabbitmq/tdmq-rabbitmq-java-sdk-demo.zip)

## 操作步骤

### 步骤1：安装 Java 依赖库

在 pom.xml 添加以下依赖：
<dx-codeblock>
:::  xml
<!-- in your <dependencies> block -->
<dependency>
    <groupId>com.rabbitmq</groupId>
    <artifactId>amqp-client</artifactId>
    <version>5.13.0</version>
</dependency>
:::
</dx-codeblock>

### 步骤2：生产消息

编译并运行 MessageProducer.java。
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">EXCHANGE_NAME</td>
<td align="left">Exchange 名称，在控制台 Exchange 列表获取。</td>
</tr>
<tr>
<td align="left">factory.setUri</td>
<td align="left">集群接入地址，在<strong>集群管理</strong>页面操作列的<strong>获取接入地址</strong>获取。<img src="https://main.qcloudimg.com/raw/0253d014dd12c0b406cf2d2dfb63c88f.png" alt="img"></td>
</tr>
<tr>
<td align="left">factory.setVirtualHost</td>
<td align="left">Vhost 名称，在控制台 Vhost 页面复制，格式是<strong>“集群 ID + | + vhost 名称”</strong>。<img src="https://main.qcloudimg.com/raw/de750dc729a5bd60e9c1fa398af8c910.png" alt="img"></td>
</tr>
<tr>
<td align="left">factory.setUsername</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">factory.setPassword</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/65ef236aaaa1b664dfe7fd7bdcbd3576.png" alt="img"></td>
</tr>
</tbody></table>

### 步骤3：消费消息

编译并运行 MessageConsumer.java。
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">QUEUE_NAME</td>
<td align="left">Queue名称，在控制台 Queue 列表获取。</td>
</tr>
<tr>
<td align="left">EXCHANGE_NAME</td>
<td align="left">Exchange 名称，在控制台 Exchange 列表获取。</td>
</tr>
<tr>
<td align="left">factory.setUri</td>
<td align="left">集群接入地址，在<strong>集群管理</strong>页面操作列的<strong>获取接入地址</strong>获取。<img src="https://main.qcloudimg.com/raw/0253d014dd12c0b406cf2d2dfb63c88f.png" alt="img"></td>
</tr>
<tr>
<td align="left">factory.setVirtualHost</td>
<td align="left">Vhost 名称，在控制台 Vhost 页面复制，格式是<strong>“集群 ID + | + vhost 名称”</strong>。<img src="https://main.qcloudimg.com/raw/de750dc729a5bd60e9c1fa398af8c910.png" alt="img"></td>
</tr>
<tr>
<td align="left">factory.setUsername</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">factory.setPassword</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/65ef236aaaa1b664dfe7fd7bdcbd3576.png" alt="img"></td>
</tr>
</tbody></table>

### 步骤4：查询消息

如果您想确认消息是否成功发送至 TDMQ RabbitMQ 版，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)** > **Queue** 页面查看接入的消费者情况。

![](https://qcloudimg.tencent-cloud.cn/raw/4a3eee6e8b2899916f787c30412f1087.png)

>?上述是基于 RabbitMQ 的发布订阅模型的一个简单示例。其他示例可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rabbitmq/tdmq-rabbitmq-java-sdk-demo.zip) 或 [RabbitMQ 官网](https://www.rabbitmq.com/getstarted.html) 实例。
