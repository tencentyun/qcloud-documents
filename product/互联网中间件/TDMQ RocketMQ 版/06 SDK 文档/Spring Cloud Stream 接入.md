## 操作场景

本文以调用 Spring Cloud Stream 接入为例介绍实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rocketmq-demo/tdmq-rocketmq-springcloud-stream-demo.zip)

## 操作步骤
### 步骤1：引入依赖
在 pom.xml 中引入 `stream-rocketmq` 相关依赖。
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

### 步骤2：添加配置
在配置文件中增加 RocketMQ 相关配置。
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
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">name-server</td>
<td align="left">集群接入地址，在控制台<strong>集群管理</strong>页面的集群列表操作栏的<strong>接入地址</strong>处获取。</td>
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
<td align="left">group</td>
<td align="left">生产者 Group 的名称，在控制台 <strong>Group</strong> 页面复制。</td>
</tr>
<tr>
<td align="left">destination</td>
<td align="left">Topic 的名称，在控制台 <strong>topic</strong> 页面复制。</td>
</tr>
<tr>
<td align="left">subExpression</td>
<td align="left">用来设置消息的 TAG。</td>
</tr>
</tbody></table>

### 步骤3：配置 channel
channel 分为输入和输出，可根据自己的业务进行单独配置。
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

### 步骤4：添加注解
在配置类或启动类上添加相应注解，如果有多个binder配置，都要在此注解中进行指定。
```java
@EnableBinding({CustomChannelBinder.class})
```

### 步骤5：发送消息

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

### 步骤6：消费消息
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

