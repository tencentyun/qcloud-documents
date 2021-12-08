## 操作场景

该任务指导您在购买 TDMQ Pulsar 版服务和腾讯云服务器后，下载 Demo 并进行简单的测试，了解运行一个客户端的操作步骤。

## 前提条件

- 已 [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)
- 已 [购买云服务器](https://buy.cloud.tencent.com/cvm)

## 操作步骤

1. 下载 Demo（[Demo下载地址](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-java-client.zip)），并配置相关参数。

   **添加 Maven 依赖**
   按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-java/) 添加 Maven 依赖。
   <dx-codeblock>
   :::  xml

```xml
<!-- in your <properties> block -->
<pulsar.version>2.7.1</pulsar.version>
<!-- in your <dependencies> block -->
<dependency>
	<groupId>org.apache.pulsar</groupId>
	<artifactId>pulsar-client</artifactId>
	<version>${pulsar.version}</version>
</dependency>
```

:::
</dx-codeblock>

   **创建 Client**	 
<dx-tabs>
::: 2.7.1版本及以上集群接入示例
<dx-codeblock>

:::  java

// 一个Pulsar client对应一个客户端链接
// 原则上一个进程一个client，尽量避免重复创建，消耗资源
// 关于客户端和生产消费者的最佳实践，可以参考官方文档 https://cloud.tencent.com/document/product/1179/58090

PulsarClient client = PulsarClient.builder()
        //替换成集群接入地址，位于【集群管理】页面接入地址
        .serviceUrl("http://pulsar-..tencenttdmq.com:8080")
        //替换成角色密钥，位于【角色管理】页面
        .authentication(AuthenticationFactory.token("eyJr"))
        .build(); 

System.out.println(">> pulsar client created.");

:::
</dx-codeblock>

- serviceUrl 即接入地址，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 页面查看并复制。

  ![](https://main.qcloudimg.com/raw/a1bbc4b3857903e04f16fc46d9194c57.png)

- token 即角色的密钥，角色密钥可以在**角色管理**中复制。

<dx-alert infotype="notice" title="">
密钥泄露很可能导致您的数据泄露，请妥善保管您的密钥。
</dx-alert>

:::
::: 2.6.1版本集群接入示例

<dx-codeblock>

:::  java

PulsarClient client = PulsarClient.builder()
    .serviceUrl("pulsar://...:6000/")//接入地址到集群管理-接入点列表完整复制
    .listenerName("custom:pulsar-/vpc-/subnet-")//custom:替换成路由ID，位于**集群管理**接入点列表
    .authentication(AuthenticationFactory.token("eyJr"))//替换成角色密钥，位于**角色管理**页面
    .build();
System.out.println(">> pulsar client created.");

:::
</dx-codeblock>

- serviceUrl 即接入地址，可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 接入点页面查看并复制。
- listenerName即 “custom:” 拼接路由ID（NetModel），路由ID可以在控制台 **[集群管理](https://console.cloud.tencent.com/tdmq/cluster)** 接入点页面查看并复制。
  ![](https://main.qcloudimg.com/raw/521d7585bb872e8150fc0277da1fe894.png)
- token 即角色的密钥，角色密钥可以在**角色管理**中复制。



<dx-alert infotype="notice" title="">
密钥泄露很可能导致您的数据泄露，请妥善保管您的密钥。
</dx-alert>
:::
</dx-tabs>

 **创建消费者进程**

```java
Consumer<byte[]> consumer = client.newConsumer()
                //topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
                .topic("persistent://pulsar-****/namespace/topicName")
                //需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
                .subscriptionName("subscriptionName")
                //声明消费模式为exclusive（独占）模式
                .subscriptionType(SubscriptionType.Exclusive)
                //配置从最早开始消费，否则可能会消费不到历史消息
                .subscriptionInitialPosition(SubscriptionInitialPosition.Earliest)
                .subscribe();
        System.out.println(">> pulsar consumer created.");
```

 <dx-alert infotype="explain" title="">

- Topic 名称需要填入完整路径，即“persistent://clusterid/namespace/Topic”，clusterid/namespace/topic 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
  ![](https://main.qcloudimg.com/raw/a2e32b311b825df9798b8c98df7c3416.png)
- subscriptionName需要写入订阅名，可在**消费管理**界面查看。
  </dx-alert>



   **创建生产者进程**

```java
Producer<byte[]> producer = client.newProducer()
                //topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
                .topic("persistent://pulsar-****/namespace/topicName")
                .create();
        System.out.println(">> pulsar producer created.");
```

<dx-alert infotype="explain" title="">
Topic 名称需要填入完整路径，即“persistent://clusterid/namespace/Topic”，clusterid/namespace/topic 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
</dx-alert>



   **生产消息**

```java
for (int i = 0; i < 5; i++) {
            String value = "my-sync-message-" + i;
            //发送消息
            MessageId msgId = producer.newMessage().value(value.getBytes()).send();
            System.out.println("deliver msg " + msgId + ",value:" + value);
        }
        //关闭生产者
        producer.close();
```

   **消费消息**

```java
for (int i = 0; i < 5; i++) {
            //接收当前offset对应的一条消息
            Message<byte[]> msg = consumer.receive();
            MessageId msgId = msg.getMessageId();
            String value = new String(msg.getValue());
            System.out.println("receive msg " + msgId + ",value:" + value);
            //接收到之后必须要ack，否则offset会一直停留在当前消息，无法继续消费
            consumer.acknowledge(msg);
        }
```

2. 在 `pom.xml` 所在目录执行命令 `mvn clean package`，或者通过 IDE 自带的功能打包整个工程，在 target 目录下生成一个可运行的 jar 文件。
   <img src="https://main.qcloudimg.com/raw/8a4808ea722fe0b19ad1cd91666088c7.png" width="450px"> 

3. 运行成功后将 jar 文件上传到云服务器，具体操作参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。

4. 登录云服务器，进入到刚刚上传jar文件所在的目录，可看到文件已上传到云服务器。
   ![](https://main.qcloudimg.com/raw/677e840a8f28802d217b38acc9745d85.png)
   执行命令 `java -jar tdmq-demo-1.0.0.jar`，运行 Demo，可查看运行日志。
   ![](https://main.qcloudimg.com/raw/cd31ccff67fe1f5fa926e383151c5aae.png)

5. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，依次点击 **Topic管理** > **Topic名称**进入消费管理页面，点开订阅名下方右三角号，可查看生产消费记录。

   ![](https://main.qcloudimg.com/raw/da7ce2bc5ac606c91982efecdb3b53bb.png)

6. 进入 **[消息查询](https://console.cloud.tencent.com/tdmq/message)** 页面，可查看 Demo 运行后的消息轨迹。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/6178970f9e7395b8e7430275fc039d47.png)
   消息轨迹如下：
   ![](https://main.qcloudimg.com/raw/eaa0125f6dcd7675e367c4e3e069c915.png)
