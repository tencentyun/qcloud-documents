## 操作场景

本文以调用 Spring Boot Starter SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/rocketmq/tdmq-rocketmq-springboot-demo.zip)

## 操作步骤

### 步骤1：添加依赖

在 pom.xml 中添加依赖。
<dx-codeblock>
:::  xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-spring-boot-starter</artifactId>
    <version>2.2.1</version>
</dependency>
:::
</dx-codeblock>



### 步骤2：准备配置

在配置文件中添加配置信息。
<dx-codeblock>
:::  yaml
server:
     port: 8082
   
   #rocketmq配置信息
   rocketmq:
     # tdmq-rocketmq服务接入地址
     name-server: rocketmq-xxx.rocketmq.ap-bj.public.tencenttdmq.com:9876
     # 生产者配置
     producer:
       # 生产者组名
       group: group111
       # 角色密钥
       access-key: eyJrZXlJZC....
       # 已授权的角色名称
       secret-key: admin
     # 消费者公共配置
     consumer:
       # 角色密钥
       access-key: eyJrZXlJZC....
       # 已授权的角色名称
       secret-key: admin
   
     # 用户自定义配置
     namespace: rocketmq-xxx|namespace1
     producer1:
       topic: testdev1
     consumer1:
       group: group111
       topic: testdev1
       subExpression: TAG1
     consumer2:
       group: group222
       topic: testdev1
       subExpression: TAG2
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
<td align="left">name-server</td>
<td align="left">集群接入地址，在控制台<strong>集群管理</strong>页面的集群列表操作栏的<strong>接入地址</strong>处获取。新版共享集群与专享集群命名接入点地址在<strong>命名空间</strong>列表获取。</td>
</tr>
<tr>
<td align="left">group</td>
<td align="left">生产者 Group 的名称，在控制台 <strong>Group</strong> 页面复制。</td>
</tr>
<tr>
<td align="left">secret-key</td>
<td align="left">角色名称，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制。</td>
</tr>
<tr>
<td align="left">access-key</td>
<td align="left">角色密钥，在 <strong><a href="https://console.cloud.tencent.com/tdmq/role">角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" alt="img"></td>
</tr>
<tr>
<td align="left">namespace</td>
<td align="left">命名空间的名称，在控制台<strong>命名空间</strong>页面复制。</td>
</tr>
<tr>
<td align="left">topic</td>
<td align="left">Topic 的名称，在控制台 <strong>topic</strong> 页面复制。</td>
</tr>
<tr>
<td align="left">subExpression</td>
<td align="left">用来设置消息的 TAG。</td>
</tr>
</tbody></table>

### 步骤3：发送消息

1. 在需要发送消息的类中注入 **`RcoketMQTemplate`** 。
<dx-codeblock>
:::  java
   @Value("${rocketmq.namespace}%${rocketmq.producer1.topic}")
         private String topic;  // topic名称 (需要使用topic全称，所以在这里对topic名称进行拼接)
         
         @Autowired
         private RocketMQTemplate rocketMQTemplate;
:::
</dx-codeblock>
2. 发送消息，消息体可以是自定义对象，也可以是 Message 对象（org.springframework.messaging包中）。
<dx-codeblock>
:::  java
   SendResult sendResult = rocketMQTemplate.syncSend(destination, message);
	 /*------------------------------------------------------------------------*/
rocketMQTemplate.syncSend(destination, MessageBuilder.withPayload(message).build())
:::
</dx-codeblock>
3. 完整示例如下。
<dx-codeblock>
:::  java
   /**
		* Description: 消息生产者
		*/
	 @Service
	 public class SendMessage {
		// 需要使用topic全称，所以进行topic名称的拼接，也可以自己设置  格式：namespace全称%topic名称
			 @Value("${rocketmq.namespace}%${rocketmq.producer1.topic}")
			 private String topic;

			 @Autowired
			 private RocketMQTemplate rocketMQTemplate;


			 /**
				* 同步发送
				*
				* @param message 消息内容
				* @param tags    订阅tags
				*/
			 public void syncSend(String message, String tags) {
					 // springboot不支持使用header传递tags，根据要求，需要在topic后进行拼接 formats: `topicName:tags`，不拼接标识无tag
					 String destination = StringUtils.isBlank(tags) ? topic : topic + ":" + tags;
					 SendResult sendResult = rocketMQTemplate.syncSend(destination,
									 MessageBuilder.withPayload(message)
													 .setHeader(MessageConst.PROPERTY_KEYS, "yourKey")   // 指定业务key
													 .build());
					 System.out.printf("syncSend1 to topic %s sendResult=%s %n", topic, sendResult);
			 }
	 }
:::
</dx-codeblock>
   
>?该示例为同步发送。异步发送，单向发送等请参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-springboot-demo.zip) 或参见 [RocketMQ Spring](https://github.com/apache/rocketmq-spring)。

### 步骤4：消费消息 
<dx-codeblock>
:::  java
@Service
   @RocketMQMessageListener(
           consumerGroup = "${rocketmq.namespace}%${rocketmq.consumer1.group}",  // 消费组，格式：namespace全称%group名称
       	// 需要使用topic全称，所以进行topic名称的拼接，也可以自己设置  格式：namespace全称%topic名称
           topic = "${rocketmq.namespace}%${rocketmq.consumer1.topic}",
           selectorExpression = "${rocketmq.consumer1.subExpression}" // 订阅表达式, 不配置表示订阅所有消息
   )
   public class MessageConsumer implements RocketMQListener<String> {
   
       @Override
       public void onMessage(String message) {
           System.out.println("Tag1Consumer receive message：" + message);
       }
   }
:::
</dx-codeblock>

可根据业务需求配置多个消费者。消费者其他配置可根据具体业务需求进行配置。

>?完整示例参见 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-springboot-demo.zip) 或参见 [RocketMQ Spring](https://github.com/apache/rocketmq-spring)。

### 步骤5：查看消费详情

登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，在**集群管理** > **Group** 页面，可查看与 Group 连接的客户端列表，单击操作列的**查看详情**，可查看消费者详情。
![img](https://main.qcloudimg.com/raw/7187da67219534d767206553e2a383ab.png)

