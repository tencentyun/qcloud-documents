## 操作场景

本文以  Go 语言为例介绍通过 HTTP 协议接入 TDMQ Pulsar 版并收发消息的操作方法。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 Go](https://golang.org/dl/)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-go-http-demo.zip)

## 操作步骤

1. 准备环境。

   1. 使用腾讯云镜像加速下载。

      1. Linux 或 MacOS。

         ```shell
         export GOPROXY=https://mirrors.tencent.com/go/
         ```

      2. Windows。

         ```shell
         set GOPROXY=https://mirrors.tencent.com/go/
         ```

   2. 安装基础包与产品包。

      1. 安装公共基础包。

         ```shell
         go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common
         ```

      2. 安装 TDMQ 对应的产品包。

         ```shell
         go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tdmq
         ```

      可参考 [Go SDK 安装](https://cloud.tencent.com/document/sdk/Go)。

2. 创建 TDMQ 客户端。

   ```go
   // 认证信息
   credential := common.NewCredential(SECRET_ID, SECRET_KEY)
   cpf := profile.NewClientProfile()
   cpf.HttpProfile.Endpoint = ENDPOINT
   // 创建tdmq客户端
   client, _ := tdmq.NewClient(credential, REGION, cpf)
   ```

   | 参数                  | 说明                                                         |
   | :-------------------- | :----------------------------------------------------------- |
   | SECRET_ID、SECRET_KEY | 云 API 密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，在**访问密钥** > **API 密钥管理**页面复制。![img](https://main.qcloudimg.com/raw/8ec140474be0ced1352695b372b2934d.png) |
   | ENDPOINT              | 接口请求域名： tdmq.tencentcloudapi.com                      |
   | REGION                | 集群所属地域，详见产品支持的 [地域列表](https://cloud.tencent.com/document/api/1179/46067#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。 |

3. 发送消息。

   ```go
   request := tdmq.NewSendMessagesRequest()
   // 已授权角色密钥
   request.StringToken = common.StringPtr(token)
   // 已授权角色名称
   request.ProducerName = common.StringPtr(userName)
   // 设置topic名称, 格式为：集群（租户）ID/命名空间/Topic名称
   request.Topic = common.StringPtr(topicName)
   // 消息内容
   request.Payload = common.StringPtr("this is a new message.")
   // 发送消息超时时间
   request.SendTimeout = common.Int64Ptr(3000)
   // 发送消息
   response, err := client.SendMessages(request)
   if _, ok := err.(*errors.TencentCloudSDKError); ok {
       fmt.Printf("An API error has returned: %s", err)
       return
   }
   if err != nil {
       panic(err)
   }
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | token     | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | userName  | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**名称**列复制。 |
   | topicName | Topic 名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |

4. 消费消息。

   ```go
   request := tdmq.NewReceiveMessageRequest()
   // 设置topic名称, 格式为：集群（租户）ID/命名空间/Topic名称
   request.Topic = common.StringPtr(topicName)
   // 设置订阅名称
   request.SubscriptionName = common.StringPtr(subName)
   // consumer接收的消息会首先存储到receiverQueueSize这个队列中，用作调优接收消息的速率
   request.ReceiverQueueSize = common.Int64Ptr(10)
   // 设置consumer初始接收消息的位置，可选参数为：Earliest, Latest
   request.SubInitialPosition = common.StringPtr("Latest")
   // 消费消息
   response, err := client.ReceiveMessage(request)
   if _, ok := err.(*errors.TencentCloudSDKError); ok {
       fmt.Printf("An API error has returned: %s", err)
       return
   }
   if err != nil {
       panic(err)
   }
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | subName   | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

5. 确认消息。

   ```go
   request := tdmq.NewAcknowledgeMessageRequest()
   // 设置消息id
   request.MessageId = common.StringPtr(messageId)
   // 设置topic名称, 格式为：集群（租户）ID/命名空间/Topic名称
   request.AckTopic = common.StringPtr(topicName)
   // 设置订阅信息
   request.SubName = common.StringPtr(subName)
   // 确认消息
   response, err := client.AcknowledgeMessage(request)
   if _, ok := err.(*errors.TencentCloudSDKError); ok {
       fmt.Printf("An API error has returned: %s", err)
       return
   }
   if err != nil {
       panic(err)
   }
   ```

   | 参数      | 说明                                                         |
   | :-------- | :----------------------------------------------------------- |
   | messageId | 消费消息获取导的消息 ID。                                    |
   | topicName | Topic名称，格式为: 集群（租户）ID/命名空间/Topic名称，示例：pulsar-xxx/sdk_http/topic1。可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。 |
   | subName   | 订阅名称，可在控制台**集群管理 **> **消费者**tab页面复制。   |

上述是对消息收发操作的简单介绍，完整实例可参考 [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/http/tdmq-pulsar-go-http-demo.zip) 或 [云API Explorer](https://console.cloud.tencent.com/api/explorer?Product=tdmq&Version=2020-02-17&Action=ModifyCluster&SignVersion=)。
