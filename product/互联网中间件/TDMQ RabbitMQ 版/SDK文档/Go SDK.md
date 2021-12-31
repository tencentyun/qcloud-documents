## 操作场景

本文以调用 Go SDK 为例介绍通过开源 SDK 实现消息收发的操作过程，帮助您更好地理解消息收发的完整过程。

## 前提条件

- [完成资源创建与准备](https://cloud.tencent.com/document/product/1495/61829)
- [安装 Go](https://golang.org/dl/)
- [下载 Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-go-sdk-demo.zip)

## 操作步骤

1. 执行如下命令在客户端环境安装所需包。
```shell
go get "github.com/rabbitmq/amqp091-go"
```

2. 安装完成后，即可引入到您的 GO 工程文件中。
```go
import (amqp "github.com/rabbitmq/amqp091-go")
```

引入之后即可在您的项目中使用客户端。


## 使用示例

1. 建立连接和通信信道。
   ```go
   // 所需参数
   const (
   	host     = "amqp-xx.rabbitmq.x.tencenttdmq.com" // 服务接入地址
   	username = "roleName" // 角色控制台对应的角色名称
   	password = "eyJrZX..." // 角色对应的密钥
   	vhost    = "amqp-xx|Vhost" // 要使用的Vhost全称
   )
   // 创建连接
   conn, err := amqp.Dial("amqp://" + username + ":" + password + "@" + host + ":5672/" + vhost)
   failOnError(err, "Failed to connect to RabbitMQ")
   defer func(conn *amqp.Connection) {
   	err := conn.Close()
   	if err != nil {
   	}
   }(conn)
   
   // 建立通道
   ch, err := conn.Channel()
   failOnError(err, "Failed to open a channel")
   defer func(ch *amqp.Channel) {
   	err := ch.Close()
   	if err != nil {
   	}
   }(ch)
   ```


   | 参数     | 说明                                                         |
   | :------- | :----------------------------------------------------------- |
   | host     | 集群接入地址，在**集群管理**页面操作列的**获取接入地址**获取。![img](https://main.qcloudimg.com/raw/0238d2d64bd896704ebef400fc08a7f1.png) |
   | username | 角色名称，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制。 |
   | password | 角色密钥，在 **[角色管理](https://console.cloud.tencent.com/tdmq/role)** 页面复制**密钥**列复制。![](https://main.qcloudimg.com/raw/52907691231cc11e6e4801298ba90a6c.png) |
   | vhost    | Vhost 名称，在控制台 Vhost 页面复制，格式是**“集群 ID + \| + vhost 名称”**。![img](https://main.qcloudimg.com/raw/ae6ec1a5a94c9befea289ad7f5b46aed.png) |

2. 声明交换机。
   ```go
   // 声明交换机 （名称和类型需要与存在的交换机保持一致）
   	err = ch.ExchangeDeclare(
   		"logs-exchange",   // 交换机名称
   		"fanout", // 交换机类型
   		true,     // durable
   		false,    // auto-deleted
   		false,    // internal
   		false,    // no-wait
   		nil,      // arguments
   	)
   	failOnError(err, "Failed to declare a exchange")
   ```

   
3. 发布消息。

   消息可发给交换机，也可以直接发到指定队列 ( hello world 和 work queues 消息模型)。
	 发布消息到交换机：
   ```go
   // 消息内容
   body := "this is new message."
   // 发布消息到交换机   
   err = ch.Publish(
   	"logs-exchange",         // exchange
   	"", // routing key   （根据使用的交换机类型可选择的是否需要routing key），如果不选择交换机，该参数为消息队列名称
   	false,      // mandatory
   	false,      // immediate
   	amqp.Publishing{
   		ContentType: "text/plain",
   		Body:        []byte(body),
   	})
   failOnError(err, "Failed to publish a message")
   ```
发布消息到指定队列：
   ```go
   // 发布消息到指定的消息队列
   err = ch.Publish(
   	"",         // exchange
   	queue.Name, // routing key
   	false,      // mandatory
   	false,      // immediate
   	amqp.Publishing{
   		ContentType: "text/plain",
   		Body:        []byte(body),
   	})
   failOnError(err, "Failed to publish a message")
   ```

4. 订阅消息。
   ```go
   // 创建消费者并消费指定消息队列中的消息
   msgs, err := ch.Consume(
   	"message-queue", // message-queue
   	"",           // consumer
   	false,        // 设置为非自动确认(可根据需求自己选择)
   	false,        // exclusive
   	false,        // no-local
   	false,        // no-wait
   	nil,          // args
   )
   failOnError(err, "Failed to register a consumer")
   
   // 获取消息队列中的消息
   forever := make(chan bool)
   go func() {
   	for d := range msgs {
   		log.Printf("Received a message: %s", d.Body)
   		t := time.Duration(1)
   		time.Sleep(t * time.Second)
   		// 手动回复ack
   		d.Ack(false)
   	}
   }()
   log.Printf(" [Consumer] Waiting for messages.")
   <-forever
   ```

5. 消费者使用 routing key。
   ```go
   // 需要在消息队列中指定 交换机 和 routing key
   err = ch.QueueBind(
   	q.Name, // queue name
   	"routing_key",     // routing key
   	"topic_demo", // exchange
   	false,
   	nil,
   )
   failOnError(err, "Failed to bind a queue")
   ```

详细使用示例可参考 [Demo](https://tdmq-1300957330.cos.ap-guangzhou.myqcloud.com/TDMQ-demo/tdmq-rabbitmq-demo/tdmq-rabbitmq-go-sdk-demo.zip) 或 [RabbitMQ 官网](https://www.rabbitmq.com/getstarted.html)。

