## 操作场景

本文以 Java SDK 为例介绍客户端接入 TDMQ CMQ 版服务并收发消息的操作步骤。

## 前提条件

- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/cmq/tdmq-cmq-Java-sdk-demo.zip)

## 队列模型
### 操作步骤
1. 在控制台创建符合需求的队列服务，参见 [创建队列服务](https://cloud.tencent.com/document/product/1496/61015)。
2. 引入 CMQ 客户端相关依赖。
<dx-codeblock>
:::  xml
   <!-- cmq sdk -->
   <dependency>
       <groupId>com.qcloud</groupId>
       <artifactId>cmq-http-client</artifactId>
       <version>1.0.7</version>
   </dependency>
:::
</dx-codeblock>
3. 发送消息。
<dx-codeblock>
:::  java
   Account account = new Account(SERVER_ENDPOINT, SECRET_ID, SECRET_KEY);
   Queue queue = account.getQueue(queueName);
   String msg = "hello client, this is a message. Time:" + new Date();
   CmqResponse response = queue.send(msg);
:::
</dx-codeblock>
<table>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
<tr>
<td>SERVER_ENDPOINT</td>
<td>API 调用地址，在 <a href = "https://console.cloud.tencent.com/tdmq">TDMQ CMQ 版控制台</a> 的<b>队列服务</b> > <b>API 请求地址</b>处复制。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/f6334447f903ae629b518280e933c31b.png">
</td>
</tr>
<tr>
<td>SECRET_ID、SECRET_KEY</td>
<td>云 API 密钥，登录 <a href = "https://console.cloud.tencent.com/cam/overview">访问管理控制台</a>，在<b>访问密钥</b> > <b>API 密钥管理</b>页面复制。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/867837e2b1e6d347ecb04d7085938c08.png">
</td>
</tr>
<tr>
<td>queueName </td>
<td>队列名称，在 <a href = "https://console.cloud.tencent.com/tdmq">TDMQ CMQ 版控制台</a> 的<b>队列服务</b>列表页面获取。</td>
</tr>
</table> 
4. 消费消息。
<dx-codeblock>
:::  java
   Account account = new Account(SERVER_ENDPOINT, SECRET_ID, SECRET_KEY);
   Queue queue = account.getQueue(queueName);
   Message message = queue.receiveMessage();
   // 消费成功，删除消息。未删除的消息，将在一定时间后可重新投递
   queue.deleteMessage(message.receiptHandle);
:::
</dx-codeblock>
<table>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
<tr>
<td>SERVER_ENDPOINT</td>
<td>API 调用地址，在 <a href = "https://console.cloud.tencent.com/tdmq">TDMQ CMQ 版控制台</a> 的<b>队列服务</b> > <b>API 请求地址</b>处复制。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/f6334447f903ae629b518280e933c31b.png">
</td>
</tr>
<tr>
<td>SECRET_ID、SECRET_KEY</td>
<td>云 API 密钥，登录 <a href = "https://console.cloud.tencent.com/cam/overview">访问管理控制台</a>，在<b>访问密钥</b> > <b>API 密钥管理</b>页面复制。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/867837e2b1e6d347ecb04d7085938c08.png">
</td>
</tr>
<tr>
<td>queueName </td>
<td>队列名称，在 <a href = "https://console.cloud.tencent.com/tdmq">TDMQ CMQ 版控制台</a> 的<b>队列服务</b>列表页面获取。</td>
</tr>
</table> 
   

## 主题模型
### 操作步骤
1. 在控制台创建资源。
   1. 在控制台创建主题，参见 [主题管理](https://cloud.tencent.com/document/product/1496/61021)。
   2. 给主题创建一个订阅者，参见 [订阅管理](https://cloud.tencent.com/document/product/1496/61022)。
2. 引入 CMQ 客户端相关依赖。
<dx-codeblock>
:::  xml
   <!-- cmq sdk -->
   <dependency>
       <groupId>com.qcloud</groupId>
       <artifactId>cmq-http-client</artifactId>
       <version>1.0.7</version>
   </dependency>
:::
</dx-codeblock>
3. 创建 Topic 对象。
<dx-codeblock>
:::  java
   Account account = new Account(SERVER_ENDPOINT, SECRET_ID, SECRET_KEY);
   Topic topic = account.getTopic(topicName);
:::
</dx-codeblock>
<table>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
<tr>
<td>SERVER_ENDPOINT</td>
<td>API 调用地址，在 <a href = "https://console.cloud.tencent.com/tdmq">TDMQ CMQ 版控制台</a> 的<b>队列服务</b> > <b>API 请求地址</b>处复制。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/f6334447f903ae629b518280e933c31b.png">
</td>
</tr>
<tr>
<td>SECRET_ID、SECRET_KEY</td>
<td>云 API 密钥，登录 <a href = "https://console.cloud.tencent.com/cam/overview">访问管理控制台</a>，在<b>访问密钥</b> > <b>API 密钥管理</b>页面复制。
<img src = "https://qcloudimg.tencent-cloud.cn/raw/867837e2b1e6d347ecb04d7085938c08.png">
</td>
</tr>
<tr>
<td>topicName </td>
<td>主题订阅名称，在 <a href = "https://console.cloud.tencent.com/tdmq">TDMQ CMQ 版控制台</a> 的<b>主题订阅</b>列表页面获取。</td>
</tr>
</table> 
4.  发送 TAG 类型消息。
<dx-codeblock>
:::  java
   String msg = "hello client, this is a message. tag=TAG1. Time:" + new Date();
   List<String> tags = Collections.singletonList("TAG1");
   String messageId = topic.publishMessage(msg, tags, null);
:::
</dx-codeblock>
5. 发送 route 消息。
<dx-codeblock>
:::  java
   String msg = "hello client, this is a message. route(abc) Time:" + new Date();
   String messageId = topic.publishMessage(msg, "abc");
:::
</dx-codeblock>
6. 消费消息，使用订阅者对应的 queue 进行消费。
<dx-codeblock>
:::  java
   Account account = new Account(SERVER_ENDPOINT, SECRET_ID, SECRET_KEY);
   Queue queue = account.getQueue(queueName);
   Message message = queue.receiveMessage();
   // 消费成功，删除消息。未删除的消息，将在一定时间后可重新投递
   queue.deleteMessage(message.receiptHandle);
:::
</dx-codeblock>

>?以上是 CMQ 两种模型下的生产和消费方式的简单介绍，更多使用可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/cmq/tdmq-cmq-Java-sdk-demo.zip)。
