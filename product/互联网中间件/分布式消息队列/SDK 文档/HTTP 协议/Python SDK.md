## 操作场景

本文以  Python 语言为例介绍通过 HTTP 协议接入 TDMQ Pulsar 版并收发消息的操作方法。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 Python](https://www.python.org/downloads/)
- [安装 pip](https://pip-cn.readthedocs.io/en/latest/installing.html)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-python-http-demo.zip)

## 操作步骤

1. 准备环境。

   参考 [Python SDK 安装](https://cloud.tencent.com/document/sdk/Python)安装 Python SDK。

   ```shell
   pip install --upgrade tencentcloud-sdk-python
   ```

2. 创建 TDMQ 客户端。

   ```python
   # 认证信息
   cred = credential.Credential(SECRET_ID, SECRET_KEY)
   httpProfile = HttpProfile()
   httpProfile.endpoint = ENDPOINT
   
   clientProfile = ClientProfile()
   clientProfile.httpProfile = httpProfile
   # 创建tdmq客户端
   client = tdmq_client.TdmqClient(cred, REGION, clientProfile)
   ```

   | 参数                  | 说明                                                         |
   | :-------------------- | :----------------------------------------------------------- |
   | SECRET_ID、SECRET_KEY | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，在**访问密钥** > **API 密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/8ec140474be0ced1352695b372b2934d.png) |
   | ENDPOINT              | 接口请求域名： tdmq.tencentcloudapi.com。                    |
   | REGION                | 集群所属地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1179/46067#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |

3. 发送消息。

   ```python
   # 发送消息请求参数
   req = models.SendMessagesRequest()
   params = {
       # 已授权角色密钥
       "StringToken": token,
       # topic全称, 格式为: 集群（租户）ID/命名空间/Topic名称
       "Topic": topicName,
       # 消息内容
       "Payload": "this is a new message.",
       # 已授权角色名称
       "ProducerName": userName,
       # 发送超时时间
       "SendTimeout": 3000,
   }
   req.from_json_string(json.dumps(params))
   
   # 发送消息
   resp = client.SendMessages(req)
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | token     | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | userName  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**名称**列复制。 |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |

4. 消费消息

   ```python
   # 接收消息请求参数
   req = models.ReceiveMessageRequest()
   params = {
       # topic全称, 格式为: 集群（租户）ID/命名空间/Topic名称
       "Topic": topicName,
       # 订阅名称
       "SubscriptionName": subName,
       # consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
       "ReceiverQueueSize": 10,
       # 设置consumer初始接收消息的位置，可选参数为：Earliest, Latest
       "SubInitialPosition": "Latest"
   }
   req.from_json_string(json.dumps(params))
   
   # 接收消息
   resp = client.ReceiveMessage(req)
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | subName   | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

5. 确认消息

   ```python
   # 确认消息请求参数
   req = models.AcknowledgeMessageRequest()
   params = {
       # 待确认的消息id
       "MessageId": messageId,
       # topic全称, 格式为: 集群（租户）ID/命名空间/Topic名称
       "AckTopic": topicName,
       # 订阅名称
       "SubName": subName
   }
   req.from_json_string(json.dumps(params))
   
   # 确认消息
   resp = client.AcknowledgeMessage(req)
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | messageId | 消费消息获取导的消息 ID。                                    |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | subName   | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

上述是对消息收发操作的简单介绍，完整实例可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-python-http-demo.zip) 或 [云API Explorer](https://console.cloud.tencent.com/api/explorer?Product=tdmq&Version=2020-02-17&Action=ModifyCluster&SignVersion=)。

