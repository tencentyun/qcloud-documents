## 操作场景

本文以调用 Java SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。



## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/81854)
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
       // 设置Virtual Hosts (开源 RabbitMQ 控制台复制完整Vhost名称)
       factory.setVirtualHost(VHOST_NAME);
       // 设置用户名 (开源 RabbitMQ 控制台中Vhost的配置权限中的user名称)
       factory.setUsername(USERNAME);
       // 设置密码 (对应user的密钥)
       factory.setPassword("****");
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
<td align="left">Exchange 名称，填写在开源 RabbitMQ 控制台创建的 Exchange 名称</td>
</tr>
<tr>
<td align="left">factory.setUri</td>
<td align="left">集群接入地址，在集群基本信息页面的<strong>私有网络</strong>模块获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/04d5cad31290beb1445625c8bf373031.png" alt="img"></td>
</tr>
<tr>
<td align="left">factory.setVirtualHost</td>
<td align="left">Vhost 名称，填写在开源 RabbitMQ 控制台创建的 Vhost 名称。</td>
</tr>
<tr>
<td align="left">factory.setUsername</td>
<td align="left">用户名称，填写在开源 RabbitMQ 控制台创建的用户名。</td>
</tr>
<tr>
<td align="left">factory.setPassword</td>
<td align="left">用户密码，填写在开源 RabbitMQ 控制台创建的用户密码。</td>
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
       // 设置Virtual Hosts (开源 RabbitMQ 控制台中复制完整Vhost名称)
       factory.setVirtualHost(VHOST_NAME);
       // 设置用户名 (开源 RabbitMQ 控制台中Vhost的配置权限中的user名称)
       factory.setUsername(USERNAME);
       // 设置密码 (对应user的密钥)
       factory.setPassword("****");
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
<td align="left">Queue 名称，填写在开源 RabbitMQ 控制台创建的 Queue 名称</td>
</tr>
<tr>
<td align="left">EXCHANGE_NAME</td>
<td align="left">Exchange 名称，填写在开源 RabbitMQ 控制台创建的 Exchange 名称</td>
</tr>
<tr>
<td align="left">factory.setUri</td>
<td align="left">集群接入地址，在集群基本信息页面的<strong>私有网络</strong>模块获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/04d5cad31290beb1445625c8bf373031.png" alt="img"></td>
</tr>
<tr>
<td align="left">factory.setVirtualHost</td>
<td align="left">Vhost 名称，填写在开源 RabbitMQ 控制台创建的 Vhost 名称。</td>
</tr>
<tr>
<td align="left">factory.setUsername</td>
<td align="left">用户名称，填写在开源 RabbitMQ 控制台创建的用户名。</td>
</tr>
<tr>
<td align="left">factory.setPassword</td>
<td align="left">用户密码，填写在开源 RabbitMQ 控制台创建的用户密码。</td>
</tr>
</tbody></table>





