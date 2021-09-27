## 操作场景

该任务指导您在控制台创建集群、命名空间等资源后，下载 Demo 并进行简单的测试，了解运行一个客户端的操作步骤。

## 前提条件

- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo.zip)

## 操作步骤

### 步骤1：添加依赖

在 pom.xml 中添加以下依赖。

```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client</artifactId>
    <version>4.5.2</version>
</dependency>
```

### 步骤2：发送消息

1. 创建发送消息程序 ProducerWithNamespace.java，并配置相关参数。

   ```java
   import org.apache.rocketmq.acl.common.AclClientRPCHook;
   import org.apache.rocketmq.acl.common.SessionCredentials;
   import org.apache.rocketmq.client.producer.DefaultMQProducer;
   import org.apache.rocketmq.client.producer.SendResult;
   import org.apache.rocketmq.common.message.Message;
   import org.apache.rocketmq.remoting.RPCHook;
   
   public class ProducerWithNamespace {
   
       //请按照文档指引在控制台配置好命名空间密钥鉴权后进行配置，此处从【角色管理】处复制Token填入
       //文档指引详见 https://cloud.tencent.com/document/product/1493/61599
       private static final String ACL_ACCESS_KEY = "eyJr****";
       //此处填写角色名或者"rop"（通用角色名）
       private static final String ACL_SECRET_KEY = "rop";
       public static void main(String[] args) throws Exception {
   
           // rocketmq-****|namespace指命名空间的名称，在控制台命名空间页面复制，producerGroup指生产者Group的名称，控制台【Group】页面复制；
           DefaultMQProducer producer = new DefaultMQProducer("rocketmq-xxxx|namespace", "producerGroup", getAclRPCHook());
           // 集群接入地址，在控制台集群管理页面的集群列表操作栏的接入地址处获取。
           producer.setNamesrvAddr("rocketmq-xxxx.rocketmq.ap-sh.public.tencenttdmq.com:xxxx");
   
           producer.start();
           int total = 0;
           for (int i = 0; i<10; i++) {
               Message message = new Message("topic", "tags", ("Hello world——" + i).getBytes());
               // topic指topic的名称，在控制台 topic 页面复制，tags 指消息标签。
               try {
                   SendResult result = producer.send(message);
                   total++;
                   System.out.printf("Topic:%s send success, queueId is: %s%n", message.getTopic(),
                           result.getMessageQueue().getQueueId());
                   Thread.sleep(1000);
               } catch (Exception e) {
                   e.printStackTrace();
               }
           }
           System.out.println("total ===> " + total);
           producer.shutdown();
       }
   
       static RPCHook getAclRPCHook() {
           return new AclClientRPCHook(new SessionCredentials(ACL_ACCESS_KEY, ACL_SECRET_KEY));
       }
   }
   ```


| 参数                     | 说明                                                         |
| ------------------------ | ------------------------------------------------------------ |
| username                 | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| password                 | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| rocketmq-xxxx\|namespace | 命名空间的名称，在控制台**命名空间**页面复制。               |
| producerGroup            | 生产者 Group 的名称，在控制台 **Group** 页面复制。           |
| setNamesrvAddr           | 集群接入地址，在控制台**集群管理**页面的集群列表操作栏的**接入地址**处获取。 |
| topic                    | Topic 的名称，在控制台 **topic** 页面复制。                  |
| tags                     | 消息过滤的标签。                                             |

2. 编译并运行 ProducerWithNamespace.java 程序。

3. 查看运行结果，运行成功结果如下。

   ```
   Topic:topic1 send success, queueId is: 0
   Topic:topic1 send success, queueId is: 0
   Topic:topic1 send success, queueId is: 1
   Topic:topic1 send success, queueId is: 2
   Topic:topic1 send success, queueId is: 0
   Topic:topic1 send success, queueId is: 1
   ```

### 步骤3：消费消息

1. 创建发送消息程序 PushConsumerWithNamespace.java，并配置相关参数。

   ```java
   import org.apache.rocketmq.acl.common.AclClientRPCHook;
   import org.apache.rocketmq.acl.common.SessionCredentials;
   import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
   import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
   import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
   import org.apache.rocketmq.common.consumer.ConsumeFromWhere;
   import org.apache.rocketmq.remoting.RPCHook;
   
   import java.util.concurrent.atomic.AtomicLong;
   
   public class PushConsumerWithNamespace {
   
       //请按照文档指引在控制台配置好命名空间密钥鉴权后进行配置，此处从【角色管理】处复制Token填入
       //文档指引详见 https://cloud.tencent.com/document/product/1493/61599
       private static final String ACL_ACCESS_KEY = "eyJr****";
       //此处填写角色名或者"rop"（通用角色名）
       private static final String ACL_SECRET_KEY = "rop";
   
       public static void main(String[] args) throws Exception {
           // rocketmq-xxxx|namespace指命名空间的名称，在控制台【命名空间】页面复制，consumerGroup指消费者Group的名称，控制台【Group】页面复制；
           DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer("rocketmq-xxxx|namespace", "consumerGroup", getAclRPCHook());
           // 集群接入地址，在控制台【集群管理】页面的集群列表操作栏的【接入地址】处获取；
           defaultMQPushConsumer.setNamesrvAddr("rocketmq-xxxx.rocketmq.ap-sh.public.tencenttdmq.com:xxxx");
           // topic指topic的名称，在控制台【topic】页面复制。
           defaultMQPushConsumer.subscribe("topic", "*");
   
           defaultMQPushConsumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
   
           AtomicLong curTime = new AtomicLong(System.currentTimeMillis());
           AtomicLong count = new AtomicLong(0L);
           defaultMQPushConsumer.registerMessageListener((MessageListenerConcurrently)(msgs, context) -> {
               msgs.forEach((msg) -> {
                   System.out.println(" body=" + new String(msg.getBody()));
                   curTime.set(System.currentTimeMillis());
                   count.incrementAndGet();
                   System.out.println("total ====> " + count.get());
               });
               return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
           });
           defaultMQPushConsumer.start();
       }
   
       static RPCHook getAclRPCHook() {
           return new AclClientRPCHook(new SessionCredentials(ACL_ACCESS_KEY, ACL_SECRET_KEY));
       }
   }
   ```


| 参数                     | 说明                                                         |
| ------------------------ | ------------------------------------------------------------ |
| username                 | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| password                 | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
| rocketmq-xxxx\|namespace | 命名空间的名称，在控制台**命名空间**页面复制。               |
| consumerGroup            | 消费者 Group 的名称，在控制台 **Group** 页面复制。           |
| setNamesrvAddr           | 集群接入地址，在控制台**集群管理**页面的集群列表操作栏的**接入地址**处获取。 |
| topic                    | Topic 的名称，在控制台 **topic** 页面复制。                  |

2. 编译并运行 PushConsumerWithNamespace.java。程序。

3. 查看运行结果，运行成功结果如下。

   ```bash
    body=Hello world——4
   total ====> 1
    body=Hello world——6
   total ====> 2
    body=Hello world——7
    body=Hello world——11
    body=Hello world——8
   ```

4. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。

   ![](https://main.qcloudimg.com/raw/de8b5d914ce93f5140c59dce9652f820.png)
