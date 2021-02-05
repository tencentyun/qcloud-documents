## 操作场景

该任务指导您在购买 TDMQ 服务和腾讯云服务器后，下载 Demo 并进行简单的测试，了解运行一个客户端的操作步骤。

## 前提条件

- 已 [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)
- 已 [购买云服务器](https://buy.cloud.tencent.com/cvm)


## 操作步骤

1. 完成 Java SDK 的下载和安装，可参考 [Java SDK 下载方式](https://cloud.tencent.com/document/product/1179/44914)。
2. 下载 Demo（[Demo下载地址](https://tdmq-gz-1255613487.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-java-client.zip)），并配置相关参数。
	- **创建Client**
<dx-codeblock>
:::  java
PulsarClient client = PulsarClient.builder()
		.serviceUrl("pulsar://**.**.**.**:****/")//ip:port 替换成路由地址，位于【集群管理】接入点列表
		.listenerName("custom:pulsar-****/vpc-****/subnet-****")//custom:替换成路由ID，位于【集群管理】接入点列表
		.authentication(AuthenticationFactory.token("eyJr****"))//替换成角色密钥，位于【角色管理】页面
		.build();
	System.out.println(">> pulsar client created.");
:::
</dx-codeblock>
  
    > ?
   > - serviceUrl 即路由地址，可以在控制台【[集群管理](https://console.cloud.tencent.com/tdmq/cluster)】接入点页面查看并复制。
   > - listenerName 即 “custom:” 拼接路由 ID（NetModel），路由 ID 可以在控制台【[集群管理](https://console.cloud.tencent.com/tdmq/cluster)】接入点页面查看并复制。
   > - token 即角色的密钥，角色密钥可以在【[角色管理](https://console.cloud.tencent.com/tdmq/role)】中复制。
   > - 密钥泄露很可能导致您的数据泄露，请妥善保管您的密钥。

   - **创建消费者进程**   
<dx-codeblock>
:::  java
Consumer<byte[]> consumer = client.newConsumer()
		.topic("persistent://pulsar-****")//topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
		.subscriptionName("****")//需要现在控制台或者通过控制台API创建好一个订阅，此处填写订阅名
		.subscriptionType(SubscriptionType.Exclusive)//声明消费模式为exclusive（独占）模式
		.subscriptionInitialPosition(SubscriptionInitialPosition.Earliest)//配置从最早开始消费，否则可能会消费不到历史消息
		.subscribe();
	System.out.println(">> pulsar consumer created.");
:::
</dx-codeblock>

    > ?
   >- Topic 名称需要填入完整路径，即“persistent://clusterid/namespace/topic”，clusterid/namespace/topic 的部分可以从控制台上【[Topic管理](https://console.cloud.tencent.com/tdmq/topic)】页面直接复制。
   >- subscriptionName 需要写入订阅名，可在【消费管理】界面查看。

   - **创建生产者进程**
<dx-codeblock>
:::  java
Producer<byte[]> producer = client.newProducer()
		.topic("persistent://pulsar-****")//topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
		.create();
	System.out.println(">> pulsar producer created.");
:::
</dx-codeblock>

    >?Topic 名称需要填入完整路径，即“persistent://clusterid/namespace/topic”，clusterid/namespace/topic 的部分可以从控制台上【[Topic管理](https://console.cloud.tencent.com/tdmq/topic)】页面直接复制。

  - **生产消息**
<dx-codeblock>
:::  java
//生产5条消息
for (int i = 0; i < 5; i++) {
    String value = "my-sync-message-" + i;
    MessageId msgId = producer.newMessage().value(value.getBytes()).send();//发送消息
    System.out.println("deliver msg " + msgId + ",value:" + value);
}
producer.close();//关闭生产进程
:::
</dx-codeblock>

   - **消费消息**
<dx-codeblock>
:::  java
//消费5条消息
for (int i = 0; i < 5; i++) {
      Message<byte[]> msg = consumer.receive();//接收当前offset对应的一条消息
      String msgId = msg.getMessageId().toString();
      String value = new String(msg.getValue());
      System.out.println("receive msg " + msgId + ",value:" + value);
      consumer.acknowledge(msg);//接收到之后必须要ack，否则offset会一直停留在当前消息，无法继续消费
}
:::
</dx-codeblock>

3. 在终端输入命令`mvn clean package`，或者通过 IDE 自带的功能打包整个工程，在 target 目录下生成一个可运行的 jar 文件。
   ![](https://main.qcloudimg.com/raw/097d7bc213100b2c17e1db235dd02048.png)
4. 运行成功后将 jar 文件上传到云服务器，具体操作参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

5. 登录云服务器，进入到刚刚上传 jar 文件所在的目录，可看到文件已上传到云服务器。
   ![](https://main.qcloudimg.com/raw/408be8532bab78314333802a1b42afbe.png)

   执行命令`java -jar tdmq-demo-cloud-1.0.1.jar`，运行 Demo，可查看运行日志。
   ![](https://main.qcloudimg.com/raw/ce7144d04ee5dcfd14ab1a06d266ad12.png)

6. 登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)，单击【Topic管理】>【Topic名称】进入消费管理页面，单击订阅名下方右三角号，可查看生产消费记录。
   ![](https://main.qcloudimg.com/raw/da7ce2bc5ac606c91982efecdb3b53bb.png)

7. 在【[消息查询](https://console.cloud.tencent.com/tdmq/message)】页面，单击操作列的【查看消息轨迹】即可查看 Demo 运行后的消息轨迹。
![](https://main.qcloudimg.com/raw/f268bb6bf66ca08369d0458a42b68b82.png)

