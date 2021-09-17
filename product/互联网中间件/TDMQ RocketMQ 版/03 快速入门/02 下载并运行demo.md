## 操作场景

该任务指导您在控制台创建集群、命名空间等资源后，下载 Demo 并进行简单的测试，了解运行一个客户端的操作步骤。

## 前提条件

- [安装1.8或以上版本JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本Maven](http://maven.apache.org/download.cgi#)
- [下载demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo.zip)

## 操作步骤

### 步骤1. 添加依赖

在 pom.xml 中添加以下依赖。

```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client</artifactId>
    <version>4.5.2</version>
</dependency>
```

### 步骤2. 发送消息

1. 创建发送消息程序 ProducerWithNamespace.java，并配置相关参数。

   ```java
   package org.apache.rocketmq.example.namespace;
   
   import java.util.concurrent.TimeUnit;
   import org.apache.rocketmq.client.producer.DefaultMQProducer;
   import org.apache.rocketmq.client.producer.SendResult;
   import org.apache.rocketmq.common.message.Message;
   
   public class ProducerWithNamespace {
       public static void main(String[] args) throws Exception {
   
           DefaultMQProducer producer = new DefaultMQProducer("rocketmq-xxxx|namespace", "producerGroup");
           // rocketmq-****|namespace指命名空间的名称，在控制台【命名空间】页面复制，producerGroup指生产者Group的名称，控制台【Group】页面复制；
           producer.setNamesrvAddr("rocketmq-xxxx.rocketmq.ap-sh.public.tencenttdmq.com:xxxx");
           // 集群接入地址，在控制台【集群管理】页面的集群列表操作栏的【接入地址】处获取。
           producer.start();
           int total = 0;
           for (int i = 0; true; i++) {
               Message message = new Message("topic", "tags", ("Hello world——" + i).getBytes());
               // topic指topic的名称，在控制台【topic】页面复制，tags指消息标签。
               try {
                   SendResult result = producer.send(message);
                   total++;
                   //TimeUnit.SECONDS.sleep(1);
                   System.out.printf("Topic:%s send success, queueId is: %s%n", message.getTopic(),
                           result.getMessageQueue().getQueueId());
                   Thread.sleep(1000);
               } catch (Exception e) {
                   e.printStackTrace();
               }
           }
   //        System.out.println("total ===> " + total);
   //        producer.shutdown();
       }
   }
   ```

   | 参数                     | 说明                                                         |
   | ------------------------ | ------------------------------------------------------------ |
   | rocketmq-xxxx\|namespace | 命名空间的名称，在控制台【命名空间】页面复制。               |
   | producerGroup            | 生产者 Group 的名称，在控制台【Group】页面复制。             |
   | setNamesrvAddr           | 集群接入地址，在控制台【集群管理】页面的集群列表操作栏的【接入地址】处获取。 |
   | topic                    | Topic 的名称，在控制台【topic】页面复制。                    |
   | tags                     | 消息过滤的标签，使用说明参考[消息过滤]()。                   |

2. 编译并运行 ProducerWithNamespace.java程序。

3. 查看运行结果，运行成功结果如下。

   ```
   Topic:topic1 send success, queueId is: 0
   Topic:topic1 send success, queueId is: 0
   Topic:topic1 send success, queueId is: 1
   Topic:topic1 send success, queueId is: 2
   Topic:topic1 send success, queueId is: 0
   Topic:topic1 send success, queueId is: 1
   ```

### 步骤3. 消费消息

1. 创建发送消息程序 PushConsumerWithNamespace.java，并配置相关参数。

   ```java
   package org.apache.rocketmq.example.namespace;
   
   import java.util.concurrent.atomic.AtomicLong;
   import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
   import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
   import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
   import org.apache.rocketmq.common.consumer.ConsumeFromWhere;
   
   public class PushConsumerWithNamespace {
       public static void main(String[] args) throws Exception {
           DefaultMQPushConsumer defaultMQPushConsumer = new DefaultMQPushConsumer("rocketmq-xxxx|namespace", "consumerGroup");
           // rocketmq-xxxx|namespace指命名空间的名称，在控制台【命名空间】页面复制，consumerGroup指消费者Group的名称，控制台【Group】页面复制；
           defaultMQPushConsumer.setNamesrvAddr("rocketmq-xxxx.rocketmq.ap-sh.public.tencenttdmq.com:xxxx");
           // 集群接入地址，在控制台【集群管理】页面的集群列表操作栏的【接入地址】处获取。
           defaultMQPushConsumer.subscribe("topic", "*");
           // topic指topic的名称，在控制台【topic】页面复制，。
           defaultMQPushConsumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
   
           AtomicLong curTime = new AtomicLong(System.currentTimeMillis());
           AtomicLong count = new AtomicLong(0L);
           defaultMQPushConsumer.registerMessageListener((MessageListenerConcurrently)(msgs, context) -> {
               msgs.stream().forEach((msg) -> {
                   long dur = System.currentTimeMillis() - msg.getBornTimestamp();
                   System.out.println(" body=" + new String(msg.getBody()));
                   curTime.set(System.currentTimeMillis());
                   count.incrementAndGet();
                   System.out.println("total ====> " + count.get());
               });
               //context.setDelayLevelWhenNextConsume();
               return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
           });
   
           defaultMQPushConsumer.start();
       }
   }
   ```

   | 参数                     | 说明                                                         |
   | ------------------------ | ------------------------------------------------------------ |
   | rocketmq-xxxx\|namespace | 命名空间的名称，在控制台【命名空间】页面复制。               |
   | consumerGroup            | 消费者 Group 的名称，在控制台【Group】页面复制。             |
   | setNamesrvAddr           | 集群接入地址，在控制台【集群管理】页面的集群列表操作栏的【接入地址】处获取。 |
   | topic                    | Topic 的名称，在控制台【topic】页面复制。                    |

2. 编译并运行 PushConsumerWithNamespace.java。程序。

3. 查看运行结果，运行成功结果如下。

   ```
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
