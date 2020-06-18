## 操作场景
TDMQ 提供了 Go 语言的 SDK 来调用服务，进行消息队列的生产和消费。

本文主要介绍 Go SDK 的使用方式，提供 Demo 工程的安装、下载、配置及运行示例，帮助工程师快速搭建 TDMQ 测试工程。

## 操作步骤

### 准备 Demo 环境

1. 安装 IDE
您可以 [安装 GoLand](https://www.jetbrains.com/zh-cn/go/promo) 或其它的 Go IDE 来运行这个 Demo，本文以 Go Land 为例。

2. 下载 TDMQ 的 [Demo 工程](https://github.com/TencentCloud/tdmq-go-client) 到本地。

### 配置 Demo工程

使用 IDE 打开 Demo 项目，如下：
![](https://main.qcloudimg.com/raw/2baca719f9cf4e56b9ba0d2f6561680d.png)

需要关注的是其中的 example 包中的 Demo工程。
![](https://main.qcloudimg.com/raw/e8d04b09e65f7781dc230180b93a5561.png)


Demo 基础的版本，只需要成功启动了 TDMQ 的集群即可，无需配置其它认证数据。

在 consumer.go 和 producer.go 文件中相关代码处配置 Broker 服务的地址：

```go
client, err := pulsar.NewClient(pulsar.ClientOptions{
	URL: "pulsar://localhost:6650",  //这里的改成Broker的服务地址
})
if err != nil {
	log.Fatal(err)
}
defer client.Close()
```

之后先启动 consumer.go，再启动 producer.go，观察控制台消息：

在 producer.go 运行的控制台可以看到有10条消息发送成功：

```bash
2020/02/20 20:20:20 Published message:  &{581 0 0 0 <nil> <nil>}
2020/02/20 20:20:20 Published message:  &{581 1 0 0 <nil> <nil>}
2020/02/20 20:20:20 Published message:  &{581 2 0 0 <nil> <nil>}
2020/02/20 20:20:20 Published message:  &{581 3 0 0 <nil> <nil>}
2020/02/20 20:20:21 Published message:  &{581 4 0 0 <nil> <nil>}
2020/02/20 20:20:21 Published message:  &{581 5 0 0 <nil> <nil>}
2020/02/20 20:20:21 Published message:  &{581 6 0 0 <nil> <nil>}
2020/02/20 20:20:21 Published message:  &{581 7 0 0 <nil> <nil>}
2020/02/20 20:20:21 Published message:  &{581 8 0 0 <nil> <nil>}
2020/02/20 20:20:22 Published message:  &{581 9 0 0 <nil> <nil>}
```

在 consumer.go运行的控制台可以看到消息被成功接收并打印出来：
```bash
Received message msgId: &pulsar.messageID{ledgerID:581, entryID:0, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 0' -- topic : 'persistent://public/default/topic-1'

Received message msgId: &pulsar.messageID{ledgerID:581, entryID:1, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 1' -- topic : 'persistent://public/default/topic-1'

Received message msgId: &pulsar.messageID{ledgerID:581, entryID:2, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 2' -- topic : 'persistent://public/default/topic-1'

Received message msgId: &pulsar.messageID{ledgerID:581, entryID:3, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 3' -- topic : 'persistent://public/default/topic-1'

...//后续省略
```

则 Go 版本的 SDK Demo 运行成功。

### 配置 CAM 认证

配置 CAM 认证方式访问 TDMQ 的集群需要在创建 Client 的时候配置 AuthCloud 参数，CAM 认证的配置方式示例如下，需要正确配置需要的参数：
```go 
authParams := make(map[string]string)
authParams["secretId"] = "AKxxxxxxxxxxCx"
authParams["secretKey"] = "SDxxxxxxxxxxCb"
authParams["region"] = "ap-guangzhou"
authParams["ownerUin"] = "xxxxxxxxxx"
authParams["uin"] = "xxxxxxxxxx"
client, err := pulsar.NewClient(pulsar.ClientOptions{
	URL:       "pulsar://9.xx.xx.8:6650",
	AuthCloud: pulsar.NewAuthenticationCloudCam(authParams), //在这里配置CAM认证
})
if err != nil {
	log.Fatal(err)
}
defer client.Close()
```

配置完成之后，即可正常创建生产者和消费者来使用 TDMQ 服务，创建的方式如下所示：
```go
//创建 Producer
producer, err := client.CreateProducer(pulsar.ProducerOptions{
	DisableBatching: true,
	Topic:           "persistent://xx/xx/topic1",
})
if err != nil {
	log.Fatal(err)
}
defer producer.Close()

//创建 Consumer
consumer, err := client.Subscribe(pulsar.ConsumerOptions{
	Topics:           []string{"topic-1", "topic-2"},
	SubscriptionName: "my-sub",
	Type:             pulsar.Shared,
	EnableRetry:      true,
})
if err != nil {
	log.Fatal(err)
}
defer consumer.Close()
```



