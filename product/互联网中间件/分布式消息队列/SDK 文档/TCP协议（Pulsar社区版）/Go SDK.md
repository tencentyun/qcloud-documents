## 操作场景

本文以调用 Go SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 Go](https://golang.org/dl/)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-pulsar-demo/tdmq-pulsar-go-sdk-demo.zip)

## 操作步骤

1. 在客户端环境引入 `pulsar-client-go` 库。

   1. 在客户端环境执行如下命令下载 Pulsar 客户端相关的依赖包。

      ```shell
      go get -u "github.com/apache/pulsar-client-go/pulsar"
      ```

   2. 安装完成后，即可通过以下代码引用到您的 Go工程文件中。

      ```go
      import "github.com/apache/pulsar-client-go/pulsar"
      ```

2. 创建 Pulsar Client。

   ```go
   // 创建pulsar客户端
   client, err := pulsar.NewClient(pulsar.ClientOptions{
       // 服务接入地址
       URL: setviceUrl,
       // 授权角色密钥
       Authentication:    pulsar.NewAuthenticationToken(authentication),
       OperationTimeout:  30 * time.Second,
       ConnectionTimeout: 30 * time.Second,
   })
   
   if err != nil {
       log.Fatalf("Could not instantiate Pulsar client: %v", err)
   }
   
   defer client.Close()
   ```

   | 参数           | 说明                                                         |
   | :------------- | :----------------------------------------------------------- |
   | setviceUrl     | 集群接入地址，可以在控制台 [**集群管理**](https://console.cloud.tencent.com/tdmq/cluster) 页面查看并复制。<br/>![img](https://qcloudimg.tencent-cloud.cn/raw/1221f6b1be8ad150a6544a3f9394a8eb.png) |
   | Authentication | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![img](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |

3. 创建生产者。

   ```go
   // 使用客户端创建生产者
   producer, err := client.CreateProducer(pulsar.ProducerOptions{
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
       Topic: "persistent://pulsar-mmqwr5xx9n7g/sdk_go/topic1",
   })
   
   if err != nil {
       log.Fatal(err)
   }
   defer producer.Close()
   ```

   >  ?
   >
   > Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。

4. 发送消息。

   ```go
   // 发送消息
   _, err = producer.Send(context.Background(), &pulsar.ProducerMessage{
       // 消息内容
       Payload: []byte("hello go client, this is a message."),
       // 业务key
       Key: "yourKey",
       // 业务参数
       Properties: map[string]string{"key": "value"},
   })
   ```

5. 创建消费者。

   ```go
   // 使用客户端创建消费者
   consumer, err := client.Subscribe(pulsar.ConsumerOptions{
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
       Topic:            "persistent://pulsar-mmqwr5xx9n7g/sdk_go/topic1",
       // 订阅名称
       SubscriptionName: "topic1_sub",
       // 订阅模式
       Type:             pulsar.Shared,
   })
   if err != nil {
       log.Fatal(err)
   }
   defer consumer.Close()
   ```

   > ?
   >
   > - Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
   >   ![img](https://qcloudimg.tencent-cloud.cn/raw/dc1bc50c434546755565c6dcb8d3e7f0.png)
   > - subscriptionName 需要写入订阅名，可在**消费管理**界面查看。

6. 消费消息。

   ```go
   // 获取消息
   msg, err := consumer.Receive(context.Background())
   if err != nil {
       log.Fatal(err)
   }
   // 模拟业务处理
   fmt.Printf("Received message msgId: %#v -- content: '%s'\n",
              msg.ID(), string(msg.Payload()))
   
   // 消费成功，回复ack，消费失败根据业务需要选择回复nack或ReconsumeLater
   consumer.Ack(msg)
   ```

7. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，依次点击 **Topic 管理** > **Topic 名称**进入消费管理页面，点开订阅名下方右三角号，可查看生产消费记录。
   ![img](https://main.qcloudimg.com/raw/da7ce2bc5ac606c91982efecdb3b53bb.png)

上述是对消息的发布和订阅方式的简单介绍。更多操作可参考 `Demo` 或 [Pulsar 官方文档](https://pulsar.apache.org/docs/en/client-libraries-go/) 。
