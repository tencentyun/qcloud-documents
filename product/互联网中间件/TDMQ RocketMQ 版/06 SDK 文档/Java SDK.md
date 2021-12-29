## 操作场景

本文以调用 Java SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-java-sdk-demo.zip)

## 操作步骤

### 步骤1：安装 Java 依赖库

在 Java 项目中引入相关依赖，以 Maven 工程为例，在 pom.xml 添加以下依赖：
>?依赖版本要求 >= 4.6.1。
>
```xml
<!-- in your <dependencies> block -->
<dependency>
	 <groupId>org.apache.rocketmq</groupId>
	 <artifactId>rocketmq-client</artifactId>
	 <version>4.6.1</version>
</dependency>

<dependency>
	 <groupId>org.apache.rocketmq</groupId>
	 <artifactId>rocketmq-acl</artifactId>
	 <version>4.6.1</version>
</dependency>
```

### 步骤2：生产消息

#### 1. 创建消息生产者

   ```java
   // 实例化消息生产者Producer
   DefaultMQProducer producer = new DefaultMQProducer(
       namespace, 
       groupName,
       new AclClientRPCHook(new SessionCredentials(accessKey, secretKey)) // ACL权限
   );
   // 设置NameServer的地址
   producer.setNamesrvAddr(nameserver);
   // 启动Producer实例
   producer.start();
   ```

   | 参数       | 说明                                                         |
   | :--------- | :----------------------------------------------------------- |
   | namespace  | 命名空间的名称，在控制台**命名空间**页面复制，格式是**集群 ID + \| + 命名空间**。 |
   | groupName  | 生产者组名称，在控制台集群管理中`Group` 页签中复制。         |
   | nameserver | 集群接入地址，在控制台**集群管理**页面的集群列表操作栏的**接入地址**处获取。 |
   | secretKey  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
   | accessKey  | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |

#### 2. 发送消息

发送消息由多种方式，同步发送、异步发送、单向发送等。

- 同步发送

```java
for (int i = 0; i < 10; i++) {
	 // 创建消息实例，设置topic和消息内容
	 Message msg = new Message(topic_name, "TAG", ("Hello RocketMQ " + i).getBytes(RemotingHelper.DEFAULT_CHARSET));
	 // 发送消息
	 SendResult sendResult = producer.send(msg);
	 System.out.printf("%s%n", sendResult);
}
```

| 参数       | 说明                                                      |
| :--------- | :-------------------------------------------------------- |
| topic_name | 在控制台集群管理中**`Topic`** 页签中复制具体 Topic 名称。 |
| TAG        | 用来设置消息的TAG。                                       |

- 异步发送

```java
// 设置发送失败后不重试
producer.setRetryTimesWhenSendAsyncFailed(0);
// 设置发送消息的数量
int messageCount = 10;
final CountDownLatch countDownLatch = new CountDownLatch(messageCount);
for (int i = 0; i < messageCount; i++) {
	 try {
			 final int index = i;
			 // 创建消息实体，设置topic和消息内容
			 Message msg = new Message(topic_name, "TAG", ("Hello rocketMq " + index).getBytes(RemotingHelper.DEFAULT_CHARSET));
			 producer.send(msg, new SendCallback() {
					 @Override
					 public void onSuccess(SendResult sendResult) {
							 // 消息发送成功逻辑
							 countDownLatch.countDown();
							 System.out.printf("%-10d OK %s %n", index, sendResult.getMsgId());
					 }

					 @Override
					 public void onException(Throwable e) {
							 // 消息发送失败逻辑
							 countDownLatch.countDown();
							 System.out.printf("%-10d Exception %s %n", index, e);
							 e.printStackTrace();
					 }
			 });
	 } catch (Exception e) {
			 e.printStackTrace();
	 }
}
countDownLatch.await(5, TimeUnit.SECONDS);
```

| 参数       | 说明                                                      |
| :--------- | :-------------------------------------------------------- |
| topic_name | 在控制台集群管理中**`Topic`** 页签中复制具体 Topic 名称。 |
| TAG        | 用来设置消息的TAG。                                       |

- 单向发送

```java
for (int i = 0; i < 10; i++) {
	 // 创建消息实例，设置topic和消息内容
	 Message msg = new Message(topic_name, "TAG", ("Hello RocketMQ " + i).getBytes(RemotingHelper.DEFAULT_CHARSET));
	 // 发送单向消息
	 producer.sendOneway(msg);
}
```

| 参数       | 说明                                                      |
| :--------- | :-------------------------------------------------------- |
| topic_name | 在控制台集群管理中**`Topic`** 页签中复制具体 Topic 名称。 |
| TAG        | 用来设置消息的TAG。                                       |

批量发送及其他情况可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-java-sdk-demo.zip) 或 [RocketMQ 官方文档](https://rocketmq.apache.org/docs/simple-example/)。


### 步骤3：消费消息

#### 1. 创建消费者
TDMQ RocketMQ 版支持 push 和 pull 两种消费模式。

- push 消费者

```java
// 实例化消费者
DefaultMQPushConsumer pushConsumer = new DefaultMQPushConsumer(
	 namespace,                                                  
	 groupName,                                              
	 new AclClientRPCHook(new SessionCredentials(accessKey, secretKey))); //ACL权限
// 设置NameServer的地址
pushConsumer.setNamesrvAddr(nameserver);
```

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| namespace  | 命名空间的名称，在控制台**命名空间**页面复制，格式是**集群 ID + \|+ 命名空间**。 |
| groupName  | 生产者组名称，在控制台集群管理中`Group` 页签中复制。         |
| nameserver | 集群接入地址，在控制台**集群管理**页面的集群列表操作栏的**接入地址**处获取。 |
| secretKey  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| accessKey  | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |

- pull 消费者

```java
// 实例化消费者
DefaultLitePullConsumer pullConsumer = new DefaultLitePullConsumer(
	 namespace,                                               
	 groupName,                                             
	 new AclClientRPCHook(new SessionCredentials(accessKey, secretKey)));
// 设置NameServer的地址
pullConsumer.setNamesrvAddr(nameserver);
// 设置从第一个偏移量开始消费
pullConsumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
```

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| namespace  | 命名空间的名称，在控制台**命名空间**页面复制，格式是**集群 ID + \|+ 命名空间**。 |
| groupName  | 生产者组名称，在控制台集群管理中`Group` 页签中复制。         |
| nameserver | 集群接入地址，在控制台**集群管理**页面的集群列表操作栏的**接入地址**处获取。 |
| secretKey  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
| accessKey  | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |

更多消费类型可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-java-sdk-demo.zip) 或 [RocketMQ 官方文档](https://rocketmq.apache.org/docs/simple-example/) 。

#### 2. 订阅消息
根据消费模式不同，订阅方式也有所区别。

- push 订阅

```java
// 订阅topic
pushConsumer.subscribe(topic_name, "*");
// 注册回调实现类来处理从broker拉取回来的消息
pushConsumer.registerMessageListener((MessageListenerConcurrently) (msgs, context) -> {
	 // 消息处理逻辑
	 System.out.printf("%s Receive New Messages: %s %n", Thread.currentThread().getName(), msgs);
	 // 标记该消息已经被成功消费, 根据消费情况，返回处理状态
	 return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
});
// 启动消费者实例
pushConsumer.start();
```

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| topic_name | 在控制台集群管理中**`Topic`** 页签中复制具体 Topic 名称。    |
| "*"        | 订阅表达式如果为 null 或*表达式表示订阅全部，同时支持 "tag1 \|\| tag2 \|\| tag3" 标识订阅多个类型的 tag。 |

- pull 订阅

```java
// 订阅topic
pullConsumer.subscribe(topic_name, "*");
// 启动消费者实例
pullConsumer.start();
try {
	 System.out.printf("Consumer Started.%n");
	 while (true) {
			 // 拉取消息
			 List<MessageExt> messageExts = pullConsumer.poll();
			 System.out.printf("%s%n", messageExts);
	 }
} finally {
	 pullConsumer.shutdown();
}
```

| 参数       | 说明                                                         |
| :--------- | :----------------------------------------------------------- |
| topic_name | 在控制台集群管理中**`Topic`** 页签中复制具体 Topic 名称。    |
| "*"        | 订阅表达式如果为 null 或*表达式表示订阅全部，同时支持 "tag1 \|\| tag2 \|\| tag3" 标识订阅多个类型的 tag。 |



### 步骤4：查看消费详情

登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。
![img](https://main.qcloudimg.com/raw/7187da67219534d767206553e2a383ab.png)

上述是对消息的发布和订阅方式的简单介绍。更多操作可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-java-sdk-demo.zip) 或 [RocketMQ 官方文档](https://rocketmq.apache.org/docs/simple-example/)。
