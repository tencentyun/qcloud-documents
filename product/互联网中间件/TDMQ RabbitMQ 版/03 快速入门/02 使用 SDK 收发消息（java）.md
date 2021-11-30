## 操作场景

该任务以 Java 客户端为例介绍您在控制台创建集群、Vhost、Exchange 等资源后，下载 Demo 并进行简单的测试，了解运行一个客户端的操作步骤。

## 前提条件

- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-client-demo.zip)

## 操作步骤

1. 在 pom.xml 中添加以下依赖。
   ```xml
   <dependency>
       <groupId>com.rabbitmq</groupId>
       <artifactId>amqp-client</artifactId>
       <version>5.13.0</version>
   </dependency>
   ```

2. 创建收发消息程序 AoPTest.java，并配置相关参数。
   ```java
   package com.qcloud.tdmq.aop.client.test;
   
   import com.rabbitmq.client.AMQP;
   import com.rabbitmq.client.BuiltinExchangeType;
   import com.rabbitmq.client.Channel;
   import com.rabbitmq.client.Connection;
   import com.rabbitmq.client.ConnectionFactory;
   import com.rabbitmq.client.DefaultConsumer;
   import com.rabbitmq.client.Envelope;
   import com.rabbitmq.client.RecoveryDelayHandler;
   
   import java.io.IOException;
   import java.text.SimpleDateFormat;
   import java.util.Date;
   import java.util.concurrent.TimeoutException;
   
   public class AoPTest {
   
       // 填写您的用户名和密钥，在控制台“角色管理”页面获取
       private static final String username = "role";
       private static final String password = "eyJr****";
       //集群接入地址，在集群管理页面操作列的获取接入地址获取。
       private static final String uri = "amqp://amqp-****.com:5***";
       //Vhost 名称，在控制台 Vhost 页面复制，格式是“集群 ID + | + vhost 名称”
       private static final String vhostname = "amqp-****|vhost";
       //Exchange 名称，在控制台创建好后复制
       private static final String exchange = "exchange";
       //Queue 名称，在控制台创建好后复制
       private static final String queue = "queue";
   
       private ConnectionFactory connectionFactory;
       private Connection connection;
       private Channel channel;
   
       public AoPTest(String uri, String vhost) throws Exception {
           connectionFactory = new ConnectionFactory();
           connectionFactory.setUri(uri);
           connectionFactory.setVirtualHost(vhost);
           connectionFactory.setUsername(username);
           connectionFactory.setPassword(password);
           connectionFactory.setAutomaticRecoveryEnabled(true);
           connectionFactory.setRecoveryDelayHandler(new RecoveryDelayHandler.ExponentialBackoffDelayHandler());
           connection = connectionFactory.newConnection();
           channel = connection.createChannel();
           channel.basicQos(1);
       }
   
       public void close() throws IOException, TimeoutException {
           if (channel != null) {
               channel.close();
           }
           if (connection != null) {
               connection.close();
           }
       }
   
       public void publish(String exchange, String routingKey, int count) throws InterruptedException {
           SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
           for (int i = 0; i < count; i++) {
               try {
                   AMQP.BasicProperties properties = new AMQP.BasicProperties.Builder()
                           .appId("rabbitmq-client")
                           .contentType("text/plain")
                           .messageId("messageId-" + i)
                           .priority(2)
                           .build();
                   channel.basicPublish(exchange, routingKey, properties, ("hello - " + format.format(new Date()) + " - " + i).getBytes());
               } catch (Exception e) {
                   e.printStackTrace();
               }
               Thread.sleep(100);
           }
           System.out.println("publish ok...");
       }
   
       public void consume(String queue) throws IOException {
           channel.basicConsume(queue, false, "clientTag", new DefaultConsumer(channel) {
               @Override
               public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties,
                                          byte[] body) throws IOException {
                   System.out.println("properties: " + properties.toString());
                   System.out.println("consumerTag: " + consumerTag + ", deliveryTag: " + envelope.getDeliveryTag() +
                           ", receive msg: " + new String(body));
                   channel.basicAck(envelope.getDeliveryTag(), false);
               }
           });
       }
     
       public static void main(String[] args) throws Exception {
           
           AoPTest aopTest = new AoPTest(uri, vhostname);
	   //开启持续消费c
           aopTest.consume(queue);
	   //开始生产消息
           aopTest.publish(exchange, "routingKey", 10);
   
           Thread.sleep(10_000);
           aopTest.close();
       }
   }  
   ```
   
	 
   | 参数       | 说明                                                         |
   | ---------- | ------------------------------------------------------------ |
   | username   | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
   | password   | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | exchange   | Exchange 名称，在控制台 Exchange 列表获取。                  |
   | queue        | Queue名称，在控制台 Queue 列表获取。                         |
   | uri        | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
   | vhostname  | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |
   | routingKey | 消息的路由规则，在控制台 绑定关系列表的**绑定 Key**列获取。![](https://main.qcloudimg.com/raw/66d31e7d7ec8519843a8fc67bff87265.png) |
   
3. 编译并运行 AoPTest.java 程序，运行成功结果如下。

   ![](https://main.qcloudimg.com/raw/c7f33820fecd715a977276bbcdfc2aba.png)

4. 在控制台上 **[集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)** > **Queue** 页面可查看接入的消费者情况。
   ![](https://main.qcloudimg.com/raw/a7d78cc58efadfb614b890cc33d08632.png)

