## 操作场景

本文以调用 Go SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1179/44814)
- [安装 Go](https://golang.org/dl/)
- [下载 Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-go-sdk-demo.zip)

## 操作步骤

1. 在客户端环境引入 `pulsar-client-go` 库。
   1. 在客户端环境执行如下命令下载 Pulsar 客户端相关的依赖包。
<dx-codeblock>
:::  shell
      go get -u "github.com/apache/pulsar-client-go/pulsar"
:::
</dx-codeblock>
   2. 安装完成后，即可通过以下代码引用到您的 Go 工程文件中。
<dx-codeblock>
:::  go
      import "github.com/apache/pulsar-client-go/pulsar"
:::
</dx-codeblock>
2. 创建 Pulsar Client。
<dx-codeblock>
:::  go
   // 创建pulsar客户端
   client, err := pulsar.NewClient(pulsar.ClientOptions{
       // 服务接入地址
       URL: serviceUrl,
       // 授权角色密钥
       Authentication:    pulsar.NewAuthenticationToken(authentication),
       OperationTimeout:  30 * time.Second,
       ConnectionTimeout: 30 * time.Second,
   })
   
   if err != nil {
       log.Fatalf("Could not instantiate Pulsar client: %v", err)
   }
   
   defer client.Close()
:::
</dx-codeblock>
<table>
    <thead>
    <tr>
        <th style='text-align:left;'>参数</th>
        <th style='text-align:left;'>说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style='text-align:left;'>serviceUrl</td>
        <td style='text-align:left;'>集群接入地址，可以在控制台 <a
                href='https://console.cloud.tencent.com/tdmq/cluster'><strong>集群管理</strong></a> 页面查看并复制。<br><img
                src="https://qcloudimg.tencent-cloud.cn/raw/1221f6b1be8ad150a6544a3f9394a8eb.png"
                referrerpolicy="no-referrer" alt="img"></td>
    </tr>
    <tr>
        <td style='text-align:left;'>Authentication</td>
        <td style='text-align:left;'>角色密钥，在 <strong><a
                href='https://console.cloud.tencent.com/tdmq/role'>角色管理</a></strong> 页面复制<strong>密钥</strong>列复制。<img
                src="https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png" referrerpolicy="no-referrer"
                alt="img"></td>
    </tr>
    </tbody>
</table>
3. 创建生产者。
<dx-codeblock>
:::  go
   // 使用客户端创建生产者
   producer, err := client.CreateProducer(pulsar.ProducerOptions{
       // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称
       Topic: "persistent://pulsar-mmqwr5xx9n7g/sdk_go/topic1",
   })
   
   if err != nil {
       log.Fatal(err)
   }
   defer producer.Close()
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
</dx-alert>
4. 发送消息。
<dx-codeblock>
:::  go
   // 发送消息
   _, err = producer.Send(context.Background(), &pulsar.ProducerMessage{
       // 消息内容
       Payload: []byte("hello go client, this is a message."),
       // 业务key
       Key: "yourKey",
       // 业务参数
       Properties: map[string]string{"key": "value"},
   })
:::
</dx-codeblock>
5. 创建消费者。
<dx-codeblock>
:::  go
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
:::
</dx-codeblock>
> ?
>
> - Topic 名称需要填入完整路径，即 `persistent://clusterid/namespace/Topic`，`clusterid/namespace/topic` 的部分可以从控制台上 **[Topic管理](https://console.cloud.tencent.com/tdmq/topic)** 页面直接复制。
>   ![img](https://qcloudimg.tencent-cloud.cn/raw/dc1bc50c434546755565c6dcb8d3e7f0.png)
> - subscriptionName 需要写入订阅名，可在**消费管理**界面查看。
6. 消费消息。
<dx-codeblock>
:::  go
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
:::
</dx-codeblock>
7. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，依次点击 **Topic 管理** > **Topic 名称**进入消费管理页面，点开订阅名下方右三角号，可查看生产消费记录。
   ![img](https://main.qcloudimg.com/raw/3bee532dab55b7cab1167416aac95f4d.png)

>?上述是对消息的发布和订阅方式的简单介绍。更多操作可参见 [Demo](https://tdmq-document-1306598660.cos.ap-nanjing.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91demo/pulsar/tcp/tdmq-pulsar-go-sdk-demo.zip) 或 [Pulsar 官方文档](https://pulsar.apache.org/docs/en/client-libraries-go/)。
