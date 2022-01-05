## 操作场景

本文以  PHP 语言为例介绍通过 HTTP 协议接入 TDMQ Pulsar 版并收发消息的操作方法。



## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 PHP 5.6 或以上版本](https://www.php.net/manual/en/install.php)
- [安装 PEAR](https://pear.php.net/manual/en/installation.getting.php)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-php-http-demo.zip)

## 操作步骤

1. 准备环境。

   1. 添加依赖。

      ```shell
      composer require tencentcloud/tencentcloud-sdk-php
      ```

   2. 添加引用。

      ```php
      require '/path/to/vendor/autoload.php';
      ```

   详细信息可参考 [PHP SDK 3.0安装使用](https://cloud.tencent.com/document/sdk/PHP)。

2. 创建 TDMQ 客户端。

   ```php
   // 认证信息
   $cred = new Credential($secretId, $secretKey);
   $httpProfile = new HttpProfile();
   $httpProfile->setEndpoint($endpoint);
   
   $clientProfile = new ClientProfile();
   $clientProfile->setHttpProfile($httpProfile);
   // 创建tdmq客户端
   $client = new TdmqClient($cred, $region, $clientProfile);
   ```

   | 参数                  | 说明                                                         |
   | :-------------------- | :----------------------------------------------------------- |
   | $secretId、$secretKey | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，在**访问密钥** > **API 密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/8ec140474be0ced1352695b372b2934d.png) |
   | $endpoint             | 接口请求域名： tdmq.tencentcloudapi.com                      |
   | $region               | 集群所属地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1179/46067#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |

3. 发送消息。

   ```php
   $req = new SendMessagesRequest();
   
   $params = array(
       // 已授权角色密钥
       "StringToken" => $token,
       // topic全称, 格式为: 集群（租户）ID/命名空间/Topic名称
       "Topic" => $fullTopicName,
       // 消息内容
       "Payload" => "this is a new message.",
       // 已授权角色名称
       "ProducerName" => $userName,
       // 发送消息超时时间
       "SendTimeout" => 3000A
   );
   $req->fromJsonString(json_encode($params));
   
   // 发送消息
   $resp = $client->SendMessages($req);
   ```

   | 参数           | 说明                                                         |
   | :------------- | :----------------------------------------------------------- |
   | $token         | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | $userName      | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**名称**列复制。 |
   | $fullTopicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |

4. 消费消息

   ```php
   $req = new ReceiveMessageRequest();
   
   $params = array(
       // topic全称, 格式为: 集群（租户）ID/命名空间/Topic名称
       "Topic" => $fullTopicName,
       // 订阅名称
       "SubscriptionName" => $subName,
       // consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
       "ReceiverQueueSize" => 10,
       // 设置consumer初始接收消息的位置，可选参数为：Earliest, Latest
       "SubInitialPosition" => "Latest"
   );
   $req->fromJsonString(json_encode($params));
   
   // 接收消息
   $resp = $client->ReceiveMessage($req);
   ```

   | 参数           | 说明                                                         |
   | :------------- | :----------------------------------------------------------- |
   | $fullTopicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | $subName       | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

5. 确认消息

   ```php
   $req = new AcknowledgeMessageRequest();
   
   $params = array(
       // 带确认消息id
       "MessageId" => $messageId,
       // topic全称, 格式为: 集群（租户）ID/命名空间/Topic名称
       "AckTopic" => $fullTopicName,
       // 订阅名称
       "SubName" => $subName
   );
   $req->fromJsonString(json_encode($params));
   
   // 确认消息
   $resp = $client->AcknowledgeMessage($req);
   ```

   | 参数           | 说明                                                         |
   | :------------- | :----------------------------------------------------------- |
   | $messageId     | 消费消息获取导的消息 ID。                                    |
   | $fullTopicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | $subName       | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

上述是对消息收发操作的简单介绍，完整实例可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-php-http-demo.zip) 或 [云API Explorer](https://console.cloud.tencent.com/api/explorer?Product=tdmq&Version=2020-02-17&Action=ModifyCluster&SignVersion=)。
