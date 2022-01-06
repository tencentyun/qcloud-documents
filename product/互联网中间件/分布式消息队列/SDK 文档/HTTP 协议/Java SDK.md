## 操作场景

本文以  Java 语言为例介绍通过 HTTP 协议接入 TDMQ Pulsar 版并收发消息的操作方法。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装1.8或以上版本 JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
- [安装2.5或以上版本 Maven](http://maven.apache.org/download.cgi#)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-java-http-demo.zip)

## 操作步骤

1. 首先参考 [Java SDK](https://cloud.tencent.com/document/sdk/Java) 添加依赖。

   ```xml
   <dependency>
       <groupId>com.tencentcloudapi</groupId>
       <artifactId>tencentcloud-sdk-java-tdmq</artifactId>
       <!-- go to https://search.maven.org/search?q=tencentcloud-sdk-java and get the latest version. -->
       <!-- 请到https://search.maven.org/search?q=tencentcloud-sdk-java查询所有版本，最新版本如下 -->
       <version>3.1.423</version>
   </dependency>
   ```

2. 创建 TDMQ 客户端。

   ```java
   // 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
   // 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
   Credential cred = new Credential(secretId, secretKey);
   // 实例化一个http选项，可选的，没有特殊需求可以跳过
   HttpProfile httpProfile = new HttpProfile();
   httpProfile.setEndpoint(endpoint);
   // 实例化一个client选项，可选的，没有特殊需求可以跳过
   ClientProfile clientProfile = new ClientProfile();
   clientProfile.setHttpProfile(httpProfile);
   // 实例化要请求产品的client对象,clientProfile是可选的
   TdmqClient client = new TdmqClient(cred, region, clientProfile);
   ```

   | 参数                | 说明                                                         |
   | :------------------ | :----------------------------------------------------------- |
   | secretId、secretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，在**访问密钥** > **API 密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/8ec140474be0ced1352695b372b2934d.png) |
   | endpoint            | 接口请求域名： tdmq.tencentcloudapi.com                      |
   | region              | 集群所属地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1179/46067#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |

3. 发送消息。

   ```java
   // 实例化一个请求对象,每个接口都会对应一个request对象
   SendMessagesRequest req = new SendMessagesRequest();
   // 设置授权角色密钥
   req.setStringToken(token);
   // 设置授权角色名称
   req.setProducerName(userName);
   // 设置topic名称, 格式为: 集群（租户）ID/命名空间/Topic名称
   req.setTopic(topicName);
   // 消息内容
   req.setPayload("this is a new message.");
   // 设置发送超时时间
   req.setSendTimeout(3000L);
   // 返回的resp是一个SendMessagesResponse的实例，与请求对象对应
   SendMessagesResponse resp = client.SendMessages(req);
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | token     | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | userName  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**名称**列复制。 |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |

4. 消费消息。

   ```java
   // 实例化一个请求对象,每个接口都会对应一个request对象
   ReceiveMessageRequest req = new ReceiveMessageRequest();
   // 设置topic名称, 格式为persistent://集群（租户）ID/命名空间/Topic名称
   req.setTopic(topicName);
   // 设置订阅名称
   req.setSubscriptionName(subName);
   // consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
   req.setReceiverQueueSize(10L);
   // 设置consumer初始接收消息的位置，可选参数为：Earliest, Latest
   req.setSubInitialPosition("Latest");
   // 返回的resp是一个ReceiveMessageResponse的实例，与请求对象对应
   ReceiveMessageResponse resp = client.ReceiveMessage(req);
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | subName   | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

5. 确认消息。

   ```java
   // 实例化一个请求对象,每个接口都会对应一个request对象
   AcknowledgeMessageRequest req = new AcknowledgeMessageRequest();
   // 设置消息id
   req.setMessageId(messageId);
   // 设置topic名称, 格式为persistent://集群（租户）ID/命名空间/Topic名称
   req.setAckTopic(topicName);
   // 设置订阅名称
   req.setSubName(subName);
   // 返回的resp是一个AcknowledgeMessageResponse的实例，与请求对象对应
   AcknowledgeMessageResponse resp = client.AcknowledgeMessage(req);
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | messageId | 消费消息获取到的消息 ID。                                    |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | subName   | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

上述是对消息收发操作的简单介绍，完整实例可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-java-http-demo.zip) 或 [云API Explorer](https://console.cloud.tencent.com/api/explorer?Product=tdmq&Version=2020-02-17&Action=ModifyCluster&SignVersion=)。
