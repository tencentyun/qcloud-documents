## 操作场景
TDMQ 提供了 Go 语言的 SDK 来调用服务，进行消息队列的生产和消费。

本文主要介绍 Go SDK 的使用方式，提供 Demo 工程的安装、下载、配置及运行示例，帮助工程师快速搭建 TDMQ 测试工程。

## 操作步骤

### 准备 Demo 环境

1. 安装 IDE
您可以 [安装 GoLand](https://www.jetbrains.com/zh-cn/go/promo) 或其它的 Go IDE 来运行这个 Demo，本文以 Go Land 为例。

2. 下载 TDMQ 的 [Demo 工程](https://github.com/apache/pulsar-client-go) 到本地。

### 配置 Demo工程

使用 IDE 打开 Demo 项目，如下：
![](https://main.qcloudimg.com/raw/2baca719f9cf4e56b9ba0d2f6561680d.png)

需要关注的是其中的 example 包中的 Demo工程。
![](https://main.qcloudimg.com/raw/e8d04b09e65f7781dc230180b93a5561.png)


Demo 基础的版本，只需要成功启动了 pulsar 的集群即可，无需配置其它认证数据。

需要在 Producer 和 Consumer 中配置 TDMQ 的 broker 地址，如下所示：

在 consumer.go 文件中配置，替换这部分的地址：
![](https://main.qcloudimg.com/raw/d055c9e4e5b339c29f3da9a3dc83342d.png)

在 producer.go 中也要进行类似配置：
![](https://main.qcloudimg.com/raw/d6e35344b08612843df526cb292f28fc.png)

之后先启动 consumer.go，再启动 producer.go，观察控制台消息：

在 producer 的控制台可以看到消息发送成功：
![](https://main.qcloudimg.com/raw/e021cf6b299ea35ef55c66ab2450cca3.png)

在 consumer 的控制台可以看到消息被成功接收：
![](https://main.qcloudimg.com/raw/a06c89f3d03ca28af53c14cc471d2d4e.png)

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



