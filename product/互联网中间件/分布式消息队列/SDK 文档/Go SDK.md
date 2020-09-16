## 操作场景
TDMQ 提供了 Go 语言的 SDK 来调用服务，进行消息队列的生产和消费。

本文主要介绍 Go SDK 的使用方式，提供 Demo 工程的环境配置、下载、代码编写及运行示例，帮助工程师快速搭建 TDMQ 测试工程。

## 前提条件

- 已经在本地安装 Golang 开发环境（[下载地址](https://studygolang.com/dl)）。
- 已经准备好 Go 1.11+ 的部署环境（云服务器或其他云资源），且该环境所在的 VPC 已接入TDMQ（参考 [VPC 接入指南](https://cloud.tencent.com/document/product/1179/46240)）。
- 已获取调用地址（URL）和路由 ID（NetModel）。
这两个参数均可以在【[环境管理](https://console.cloud.tencent.com/tdmq/env?rid=1)】的接入点列表中获取。请根据客户端部署的云服务器或其他资源所在的私有网络选择正确的接入点来复制参数信息，否则会有无法连接的问题。![](https://main.qcloudimg.com/raw/4edd20db5dabb96bbc42df441a5bebdf.png)
- 已参考 角色与鉴权 文档配置好了角色与权限，并获取到了对应角色的密钥（Token）

## 操作步骤

### 准备 Demo 环境

1. 安装 IDE
   您可以 [安装 GoLand](https://www.jetbrains.com/zh-cn/go/promo) 或其它的 Go IDE 运行这个 Demo，直接通过`go run`执行也可以。

2. 配置 GCC 环境
   因为现在的 SDK 依赖了 CGO 的库，所以需要本地配置64位 GCC，可以通过 [MinGW](http://mingw-w64.org/) 来安装。

3. 打开命令控制台，运行以下命令：
```bash
go get -u github.com/TencentCloud/tdmq-go-client
```


如果国内网络环境下载比较慢，可以通过配置 [Go Proxy](https://goproxy.io/zh/) 来解决。
如果处于无法连接外网的环境下，需要先行下载依赖文件 [压缩包](https://github.com/TencentCloud/tdmq-go-client/releases/download/v0.1.1/download.zip)，将压缩包里的文件放在`%GOPATH/pkg/mod/cache/download`文件夹下即可，`%GOPATH`可通过如下指令获取：


```bash
# linux
go env | grep GOPATH 

# Windows
go env | findstr GOPATH
```
> 目前 Pulsar 官方尚未更新最新适配的客户端，腾讯云已将适配后的 Go 客户端提交至社区，即将在下个版本发布，在官方适配之前需要先使用腾讯云提供的SDK

### 创建 Demo工程

1.使用 IDE 创建一个新工程，在文件夹中创建 go.mod 文件并编辑如下：
```go
module example/godemo

go 1.12

require github.com/TencentCloud/tdmq-go-client v0.1.1
```

上述v0.1.1是 GO SDK 的版本，云上资源环境中下载的依赖文件压缩包也需要是同样的版本。

2.创建 producer.go 和 consumer.go 测试 Demo 文件。

- producer.go 代码内容如下，其中```listenerName```即 ```custom:``` 拼接路由ID（NetModel），路由ID可以在控制台【环境管理】接入点查看并复制，```NewAuthenticationToken```即角色密钥，可以在【角色管理】页面复制

```go
package main

import (
	"context"
	"github.com/TencentCloud/tdmq-go-client/pulsar"
	"log"
	"strconv"
)

func main() {

	client, err := NewClient(ClientOptions{
      		URL:            "pulsar://*.*.*.*:6000",
  		ListenerName:	"custom:1300*****0/vpc-******/subnet-********",
      		Authentication: NewAuthenticationToken("eyJh****"),
    	})
	if err != nil {
		log.Fatal(err)
	}
	defer client.Close()

	producer, err := client.CreateProducer(pulsar.ProducerOptions{
		DisableBatching: true,
		Topic:           "persistent://appid/namespace/topic-1",
	})
	if err != nil {
		log.Fatal(err)
	}
	defer producer.Close()

	ctx := context.Background()

	for j := 0; j < 10; j++ {
		if msgId, err := producer.Send(ctx, &pulsar.ProducerMessage{
			Payload: []byte("Hello " + strconv.Itoa(j)),
		}); err != nil {
			log.Fatal(err)
		} else {
			log.Println("Published message: ", msgId)
		}
	}
}
```

其中 Topic 名称需要填入完整路径，即`persistent://appid/environment/Topic`的组合，其中`appid/environment/topic`的部分可以从控制台【[Topic管理](https://console.cloud.tencent.com/tdmq/topic)】页面直接复制。
![](https://main.qcloudimg.com/raw/5a1fe96ea23b1d4906b7067a3abfd7b5.png)


- consumer.go 的代码内容如下：

```go
package main

import (
	"context"
	"fmt"
	"github.com/TencentCloud/tdmq-go-client/pulsar"
	"log"
)

func main() {

	client, err := pulsar.NewClient(pulsar.ClientOptions{
		URL:       	"pulsar://10.*.*.*:6000",//更换为接入点地址
		ListenerName:	"custom:1300*****0/vpc-******/subnet-********",
      		Authentication: NewAuthenticationToken("eyJh****"),
	})
	if err != nil {
		log.Fatal(err)
	}
	defer client.Close()

	consumer, err := client.Subscribe(pulsar.ConsumerOptions{
		Topics:           []string{"persistent://appid/namespace/topic-1"},
		SubscriptionName: "my-sub",
		Type:             pulsar.Shared,
	})
	if err != nil {
		log.Fatal(err)
	}
	defer consumer.Close()

	for ; ; {
		msg, err := consumer.Receive(context.Background())
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("Received message msgId: %#v -- content: '%s' -- topic : '%v'\n",
			msg.ID(), string(msg.Payload()), msg.Topic())
	}
}
```

### 测试验证

您需要先将 Demo 代码打包上传到云服务器上，且确认该云服务器所在的私有网络 VPC 和 TDMQ 中配置的接入点吻合。

接下来进入 Demo 测试，先执行`go run`指令启动`consumer.go`，命令如下：

```bash
go run consumer.go
```

再类似启动 producer.go，观察控制台消息：

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

在 consumer.go 运行的控制台可以看到消息被成功接收并打印出来：

```bash
Received message msgId: &pulsar.messageID{ledgerID:581, entryID:0, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 0' -- topic : 'persistent://appid/namespace/topic-1'

Received message msgId: &pulsar.messageID{ledgerID:581, entryID:1, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 1' -- topic : 'persistent://appid/namespace/topic-1'

Received message msgId: &pulsar.messageID{ledgerID:581, entryID:2, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 2' -- topic : 'persistent://appid/namespace/topic-1'

Received message msgId: &pulsar.messageID{ledgerID:581, entryID:3, batchIdx:0, partitionIdx:0, tracker:(*pulsar.ackTracker)(nil), consumer:(*pulsar.partitionConsumer)(0xc000198000)} -- content: 'Hello 3' -- topic : 'persistent://appid/namespace/topic-1'

...//后续省略
```

则 Go 版本的 SDK Demo 运行成功。


### Tag 功能

为了配置 Go SDK 的 Tag 支持，需要在消费者订阅的时候配置相应的 Tag 参数，如下：

```go
consumer, err := client.Subscribe(pulsar.ConsumerOptions{
	Topics:           []string{"persistent://appid/namespace/topic-1"},
	SubscriptionName: "my-sub",
	Type:             pulsar.Shared,
    TagMapTopicNames: map[string]string{"persistent://appid/namespace/topic-1":"a||b"},
})
if err != nil {
	log.Fatal(err)
}
defer consumer.Close()
```

不同的 Tag 之间用“||”符号分隔，此时创建的 consumer 就会只消费 Tag 中包含 a 或 b 的消息，如下创建 producer 并发送消息：

```go
// 创建 Producer 对象
producer, err := client.CreateProducer(pulsar.ProducerOptions{
	Topic:           "persistent://appid/namespace/topic-1",
})
if err != nil {
	log.Fatal(err)
}
defer producer.Close()
// 发送消息
for j := 0; j < 10; j++ {
	if msgId, err := producer.Send(ctx, &pulsar.ProducerMessage{
		Payload: []byte("Hello " + strconv.Itoa(j)),
		Tags:    []string{"a","b"},
	}); err != nil {
		log.Fatal(err)
	} else {
		log.Println("Published message: ", msgId)
	}
}
```

可以用 consumer 来接收消息，完成消费。

### 消息延迟重试

有时我们接收到一条消息时希望能在可控的延迟时间之后再次消费这个消息，这个功能现在也集成在 SDK 中，首先我们需要在创建 consumer 时配置相应的参数：

```go
consumer, err := client.Subscribe(pulsar.ConsumerOptions{
	Topics:           []string{"persistent://appid/namespace/topic-1"},
	SubscriptionName: "my-sub",
	Type:             pulsar.Shared,
    //EnableRetry 设为 true 是必须的，否则默认关闭 Retry 功能
	EnableRetry:      true,
    //DelayLevelUtil 不是必须配置的，系统会有缺省值
	DelayLevelUtil:   pulsar.NewDelayLevelUtil("1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m"),
})
if err != nil {
	log.Fatal(err)
}
defer consumer.Close()
```

在消息重试的时候，我们提供了两个接口，分别是异步和同步的方式来重试，示例如下：

```go
//同步的方式
err = consumer.ReconsumeLater(msg,pulsar.NewReconsumeOptionsWithLevel(2))
if err != nil{
    log.Fatal(err)
}
//异步的方式，提供了一个回调方法，会在 Retry 消息发送出去后进行调用
consumer.ReconsumeLaterAsync(msg, pulsar.NewReconsumeOptionsWithLevel(2), func(id pulsar.MessageID, message *pulsar.ProducerMessage, err error) {
	if err != nil {
		fmt.Printf("Error %v when send retry msg", err)
	} else {
		fmt.Printf("Retry message send success with id : %v", id)
	}
})
```

